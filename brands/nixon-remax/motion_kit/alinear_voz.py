# -*- coding: utf-8 -*-
"""Coloca la voz de Nixon exactamente donde va. Sin internet y sin programas extra (solo FFmpeg + numpy).
Como: Nixon lee las frases del guion haciendo una pausa corta entre una y otra. Este programa detecta cada frase hablada,
la corta y la pone en el segundo exacto que le toca en el video (si una frase es mas larga que su hueco, la acelera hasta 30 %).
Uso: python alinear_voz.py ID [archivo_de_voz]   -> voces/vo_<ID>_alineada.wav"""
import os, sys, glob, json, subprocess
import numpy as np

FF = r'C:\Users\Usuario\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe'
BASE = r'E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001'
VOCES = r'E:\NIXON360_CONTENTOPS\00_INBOX\N360-20261112-0001\voces'
SR = 48000
DUR = 30.0


def decode(path):
    raw = subprocess.run([FF, '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()


def segmentos(x, n_esperado, lineas=None):
    import itertools
    hop = int(SR * 0.01)
    n = len(x) // hop
    rms = np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1) + 1e-12)
    db = 20 * np.log10(rms)
    ref = np.percentile(db, 95)
    voz = db > ref - 30
    seg, ini, gap = [], None, 0
    for i, v in enumerate(voz):               # pausas de 0.12 s o mas separan trozos
        if v:
            if ini is None:
                ini = i
            gap = 0
        elif ini is not None:
            gap += 1
            if gap > 12:
                seg.append([ini, i - gap]); ini = None; gap = 0
    if ini is not None:
        seg.append([ini, n - 1 - gap])
    seg = [s for s in seg if s[1] - s[0] >= 25]
    if len(seg) > n_esperado:
        if lineas:   # elegir los cortes cuyo largo de frase se parezca mas al largo del texto
            chars = np.array([len(l[1]) for l in lineas], float)
            mejor = None
            for cortes in itertools.combinations(range(len(seg) - 1), n_esperado - 1):
                lim = [-1] + list(cortes) + [len(seg) - 1]
                d = np.array([seg[lim[k + 1]][1] - seg[lim[k] + 1][0] for k in range(n_esperado)], float)
                kf = (d * chars).sum() / (chars * chars).sum()
                err = ((d - kf * chars) ** 2).sum()
                if mejor is None or err < mejor[0]:
                    mejor = (err, lim)
            lim = mejor[1]
            seg = [[seg[lim[k] + 1][0], seg[lim[k + 1]][1]] for k in range(n_esperado)]
        else:
            while len(seg) > n_esperado:
                gaps = [seg[k + 1][0] - seg[k][1] for k in range(len(seg) - 1)]
                k = int(np.argmin(gaps))
                seg[k] = [seg[k][0], seg[k + 1][1]]
                del seg[k + 1]
    return [(a / 100.0, b / 100.0) for a, b in seg]


def estirar(chunk, factor):
    """factor > 1 = mas rapido (atempo)"""
    if factor <= 1.001:
        return chunk
    p = subprocess.run([FF, '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-filter:a', f'atempo={factor:.4f}',
                        '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-'], input=chunk.tobytes(), capture_output=True)
    return np.frombuffer(p.stdout, np.float32).copy()


def alinear(id_, ruta=None):
    lineas = json.load(open(BASE + r'\guiones_voz.json', encoding='utf-8'))[id_]['lineas']
    ruta = ruta or (glob.glob(VOCES + rf'\vo_{id_}.*') or [None])[0]
    if not ruta:
        raise SystemExit(f'No hay voz para {id_} en {VOCES}')
    x = decode(ruta)
    cj = VOCES + rf'\cortes_{id_}.json'      # opcional: [[ini,fin],...] en segundos, si la deteccion se equivoca
    seg = [tuple(c) for c in json.load(open(cj))] if os.path.exists(cj) else segmentos(x, len(lineas), lineas)
    print(f'{id_}: {len(lineas)} frases esperadas, {len(seg)} detectadas')
    if len(seg) != len(lineas):
        print('  AVISO: no coincide el numero de frases. Haga una pausa de 1 s entre frases (o repita la toma). '
              'Se usa lo detectado en orden.')
    out = np.zeros(int(DUR * SR), np.float32)
    avisos = []
    fin_prev = 0.0
    for i, (s, e) in enumerate(seg[:len(lineas)]):
        # si la frase anterior se alargo, esta empieza justo despues (sin encimarse), hasta 1.2 s tarde
        t_ini = max(lineas[i][0], fin_prev + 0.10)
        if t_ini > lineas[i][0] + 1.2:
            avisos.append(f'frase {i + 1} empieza {t_ini - lineas[i][0]:.1f}s tarde por la frase anterior')
        t_sig = lineas[i + 1][0] if i + 1 < len(lineas) else DUR
        hueco = max(0.8, t_sig - t_ini - 0.10)
        a, b = max(0, int((s - 0.06) * SR)), min(len(x), int((e + 0.12) * SR))
        ch = x[a:b]
        dur = len(ch) / SR
        f = dur / hueco
        if f > 1.0:
            f = min(f, 1.30)
            ch = estirar(ch, f)
            if dur / hueco > 1.30:
                avisos.append(f'frase {i + 1} dura {dur:.1f}s y su hueco es {hueco:.1f}s: se acelero al maximo y aun se pasa')
        fade = int(0.02 * SR)
        ch = ch.copy(); ch[:fade] *= np.linspace(0, 1, fade); ch[-fade:] *= np.linspace(1, 0, fade)
        p = int(t_ini * SR)
        fin_prev = t_ini + len(ch) / SR
        seg_out = out[p:p + len(ch)]
        seg_out += ch[:len(seg_out)]
        print(f'  {i + 1}. {t_ini:5.1f}s  natural {dur:4.1f}s  hueco {hueco:4.1f}s  {"x%.2f" % f if f > 1 else "ok"}  «{lineas[i][1][:42]}»')
    pico = np.max(np.abs(out)) or 1
    out = out / pico * 0.9
    dest = VOCES + rf'\vo_{id_}_alineada.wav'
    subprocess.run([FF, '-y', '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', dest], input=out.tobytes(), check=True)
    for a_ in avisos:
        print('  AVISO:', a_)
    print('  ->', dest)
    return dest


if __name__ == '__main__':
    alinear(sys.argv[1].upper(), sys.argv[2] if len(sys.argv) > 2 else None)
