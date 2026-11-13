# -*- coding: utf-8 -*-
s = open('video_build_v05.py', encoding='utf-8').read()
s = s.replace("hookC_v05", "hookC_v06")
# 1. kit + pines
helpers = r'''
import sys as _sys
_sys.path.insert(0, r'E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\_KIT')
import mock_kit as MK
BG_CIERRE = r'E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001\work\sm\bgc_calles-desde-arriba_9x16.png'
FOTO_NIXON = ASSETS + r'\nixon_recorte.png'
T_CIERRE = 4.2
TOTAL = CARD + T_CIERRE


def smooth(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def pin_layer(x, y, label, k=1.0, side='der'):
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(L)
    r = int(30 * k)
    cx, cy = x, y - int(r * 2.2)
    d.polygon([(cx - r * .72, cy + r * .6), (cx + r * .72, cy + r * .6), (x, y)], fill=(236, 214, 40, 255), outline=(16, 16, 16, 255))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(236, 214, 40, 255), outline=(16, 16, 16, 255), width=3)
    d.ellipse([cx - r * .38, cy - r * .38, cx + r * .38, cy + r * .38], fill=(255, 255, 255, 255))
    f = font(SEG, int(36 * k))
    tw = d.textlength(label, font=f)
    bx0 = cx + r + 8 if side == 'der' else cx - r - 8 - tw - 36 * k
    bx0 = min(max(bx0, 40), W - 40 - tw - 36 * k)
    by0, by1 = cy - int(30 * k), cy + int(30 * k)
    d.rounded_rectangle([bx0, by0, bx0 + tw + 36 * k, by1], radius=int(30 * k), fill=(12, 12, 12, 185))
    d.text((bx0 + 18 * k, cy), label, font=f, fill=(255, 255, 255, 255), anchor='lm')
    return L


def comp_layer(fr, L, alpha=1.0):
    a = np.asarray(L).astype(np.float32) / 255
    aa = a[..., 3:4] * alpha
    fr[:] = fr * (1 - aa) + a[..., :3] * aa


# (toma, label, x, y, lado) - posiciones tomadas de la cuadricula confirmada por Nixon; nombres confirmados
PINS = [
    (1, 'Instituto Nacional de Comacarán', 277, 690, 'der'),
    (4, 'Calle al Jicaral', 95, 600, 'der'),
    (7, 'Parque central de Comacarán', 518, 460, 'der'),
    (7, 'Instituto Nacional de Comacarán', 348, 1040, 'der'),
]
PIN_CACHE = {}


def cierre_frame(tc):
    if tc < 1.4:
        sc = 0.92 + 0.08 * smooth(tc / 1.4)
    elif tc < T_CIERRE - 0.9:
        sc = 1.0
    else:
        sc = 1.0 - 0.06 * smooth((tc - (T_CIERRE - 0.9)) / 0.9)
    return np.asarray(MK.cierre_v5(BG_CIERRE, FOTO_NIXON, None, (W, H), guias=False, fscale=sc, falpha=min(1.0, tc / 0.3))).astype(np.float32) / 255

'''
a = "# ---------------- bucle principal ----------------"
assert a in s
s = s.replace(a, helpers + a)
# 2. pines dentro del bucle de tomas (despues de los bloques)
b = "        paste_rgba(fr, LOGO_REMAX,"
assert b in s
pins_code = '''        for (pk, plab, px, py, pside) in PINS:
            if pk == k and 0.25 <= tl < SH - 0.2:
                pa = smooth((tl - 0.25) / 0.3) * (1 - smooth((tl - (SH - 0.5)) / 0.3))
                key = (plab, px, py)
                if key not in PIN_CACHE:
                    PIN_CACHE[key] = pin_layer(px, py, plab, 1.0, pside)
                comp_layer(fr, PIN_CACHE[key], pa)
'''
s = s.replace(b, pins_code + b, 1)
# 3. placa final -> cierre v5 animado
i = s.index("# placa final\nnc = total_frames - fidx")
j = s.index("enc.stdin.close()", i)
new_end = '''# cierre v5 animado
nc = total_frames - fidx
last = None
for j in range(max(0, nc)):
    tl = j / FPSV
    fr = cierre_frame(tl)
    if tl < 0.4 and prev is not None:
        a = smooth(tl / 0.4)
        fr = prev * (1 - a) + fr * a
    enc.stdin.write((np.clip(fr, 0, 1) * 255).astype(np.uint8).tobytes())
    fidx += 1
'''
s = s[:i] + new_end + s[j:]
# guardar el ultimo cuadro de la ultima toma para fundir
s = s.replace("        enc.stdin.write((np.clip(fr, 0, 1) * 255).astype(np.uint8).tobytes())\n        fidx += 1\n    if k % 2 == 0:",
              "        enc.stdin.write((np.clip(fr, 0, 1) * 255).astype(np.uint8).tobytes())\n        prev = fr.copy() if j >= f1 - f0 - 2 else None\n        fidx += 1\n    if k % 2 == 0:")
s = s.replace("fidx = 0\nfor k, (name, ss) in enumerate(SHOTS):", "fidx = 0\nprev = None\nfor k, (name, ss) in enumerate(SHOTS):")
# 4. audio: rellenar hasta el final
s = s.replace("'-af', 'loudnorm=I=-14:TP=-1.5:LRA=9'", "'-af', f'apad=whole_dur={TOTAL:.2f},loudnorm=I=-14:TP=-1.5:LRA=9'")
open('video_build_v06.py', 'w', encoding='utf-8').write(s)
print('ok', len(s))
