# -*- coding: utf-8 -*-
"""Borrador N360-20261112-0001 (Santa Isabel, gancho C): montaje al pulso, subtitulos de mezcla, logos, placa final."""
import json, subprocess, sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FF = r'C:\Users\Usuario\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe'
ROOT = r'E:\NIXON360_CONTENTOPS'
PID = 'N360-20261112-0001'
PROX = ROOT + rf'\02_PROXIES\{PID}'
BUILD = ROOT + rf'\04_PROJECTS_EDITABLE\{PID}\build'
ASSETS = ROOT + rf'\04_PROJECTS_EDITABLE\{PID}\assets'
OUTDIR = ROOT + rf'\05_RENDERS_DRAFT\{PID}'
LOGOS = r'E:\Lotificación Alvarez\_marca\01_logos'
W, H = 1080, 1920
FPSV = 25
LIMIT = float(os.environ.get('LIMIT_SEC', '0'))   # prueba corta

tm = json.load(open(BUILD + r'\timing.json'))
CUTS, CARD, TOTAL = tm['cuts'], tm['card_start'], tm['total']
SH = tm['shot_sec']

# (proxy, inicio dentro de la toma) por cada una de las 11 tomas
SHOTS = [('0193', 0.0), ('0193', 2.6), ('0201', 0.0), ('0196', 1.0), ('0196', 6.5), ('orbita', 5.0),
         ('0197', 4.0), ('0199', 3.0), ('0198', 0.0), ('0192', 5.0), ('orbita', 25.0)]

SEG = r'C:\Windows\Fonts\seguibl.ttf'
SEGR = r'C:\Windows\Fonts\segoeui.ttf'
GEOB = r'C:\Windows\Fonts\georgiab.ttf'
_fc = {}


def font(p, s):
    k = (p, s)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(p, s)
    return _fc[k]


DG = (24, 57, 47)
CREAM = (248, 247, 242)
LIME = (224, 236, 174)


def ease_out(u):
    u = min(max(u, 0.0), 1.0)
    return 1 - (1 - u) ** 3


# ---------------- logos (v05: sin placa, sombra doble) ----------------
from PIL import ImageChops


def shadowed(lg, pad=44):
    """Logo RGBA con sombra doble densa (sin placa). Devuelve imagen con margen 'pad'."""
    base = Image.new('RGBA', (lg.width + 2 * pad, lg.height + 2 * pad), (0, 0, 0, 0))
    a = Image.new('L', base.size, 0)
    a.paste(lg.getchannel('A'), (pad, pad))
    for blur, k, dy in ((14, 0.95, 6), (5, 0.9, 3)):
        m = ImageChops.offset(a, 0, dy).filter(ImageFilter.GaussianBlur(blur)).point(lambda v: min(255, int(v * k * 1.6)))
        sh = Image.new('RGBA', base.size, (0, 0, 0, 0))
        sh.putalpha(m)
        base.alpha_composite(sh)
    base.alpha_composite(lg, (pad, pad))
    return base


def fit_w(im, w):
    return im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)


def load_logo(path, width, shadow=True):          # usado por la placa final
    lg = Image.open(path).convert('RGBA')
    lg = lg.crop(lg.getbbox())
    return fit_w(lg, width)


PAD = 44
LOGO_REMAX = shadowed(fit_w(Image.open(LOGOS + r'\remax\2.png').convert('RGBA'), 270), PAD)
LOGO_SI = shadowed(fit_w(Image.open(ASSETS + r'\logo_si_horizontal.png'), 520), PAD)


def paste_rgba(frame, logo, x, y, alpha=1.0):
    lw, lh = logo.size
    x0, y0 = max(x, 0), max(y, 0)
    x1, y1 = min(x + lw, W), min(y + lh, H)
    if x1 <= x0 or y1 <= y0:
        return
    sub = np.asarray(logo.crop((x0 - x, y0 - y, x1 - x, y1 - y))).astype(np.float32) / 255
    a = sub[..., 3:4] * alpha
    frame[y0:y1, x0:x1] = frame[y0:y1, x0:x1] * (1 - a) + sub[..., :3] * a


# ---------------- estilo "texto en capas" (v05) ----------------
FONTS = {'conn': r'C:\Windows\Fonts\georgiai.ttf', 'light': r'C:\Windows\Fonts\seguibl.ttf',
         'accent': r'C:\Windows\Fonts\ArialNovaCond-Bold.ttf', 'protag': r'C:\Windows\Fonts\impact.ttf'}
FILL = {'conn': (240, 232, 214), 'light': (255, 255, 255), 'accent': (236, 214, 40)}
OUTLINE = {'conn': 1, 'light': 1, 'accent': 1, 'protag': 2}
SHADOW = {'conn': 0.5, 'light': 0.5, 'accent': 0.45, 'protag': 0.6}
MAXW = 940
_rng = np.random.default_rng(11)


def _clouds(shape, scales=(8, 16, 32, 64)):
    h, w = shape
    acc = np.zeros(shape, np.float32)
    amp = 1.0
    for s in scales:
        g = _rng.random((h // s + 2, w // s + 2)).astype(np.float32)
        acc += amp * np.asarray(Image.fromarray((g * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC), np.float32) / 255
        amp *= 0.6
    return (acc - acc.min()) / (acc.max() - acc.min())


CLOUD = _clouds((H, W))
PAL_DARK = [np.array(c, np.float32) / 255 for c in ((6, 18, 48), (20, 92, 140), (30, 170, 190))]
PAL_LIGHT = [np.array(c, np.float32) / 255 for c in ((210, 225, 240), (245, 250, 255), (120, 225, 245))]


def _arr(im):
    return np.asarray(im).astype(np.float32)[..., None] / 255


def _layer(reg, m, fill, outline, shadow):
    m_out = _arr(m.filter(ImageFilter.MaxFilter(outline * 2 + 1)).filter(ImageFilter.GaussianBlur(0.7)))
    sh = _arr(m.filter(ImageFilter.GaussianBlur(16)))
    sh2 = np.roll(_arr(m.filter(ImageFilter.GaussianBlur(5))), 8, axis=0)
    reg = reg * (1 - shadow * sh) * (1 - 0.55 * sh2)
    reg = reg * (1 - m_out) + 0.04 * m_out
    mm = _arr(m.filter(ImageFilter.GaussianBlur(0.6)))
    return reg * (1 - mm) + fill * mm


def draw_style(frame, y0, y1, items, state):
    """items: dict(text, role, size, x, base, alpha, yo). Dibuja por capas en frame[y0:y1]."""
    h = y1 - y0
    masks = {r: Image.new('L', (W, h), 0) for r in FONTS}
    for it in items:
        if it['alpha'] <= 0:
            continue
        ImageDraw.Draw(masks[it['role']]).text((it['x'], it['base'] - y0 + it['yo']), it['text'], anchor='ls',
                                              font=font(FONTS[it['role']], it['size']), fill=int(255 * it['alpha']))
    allm = None
    for m in masks.values():
        allm = m if allm is None else ImageChops.lighter(allm, m)
    if allm.getbbox() is None:
        return
    orig = frame[y0:y1].copy()
    band = np.clip(_arr(allm.filter(ImageFilter.GaussianBlur(38))) * 4.0, 0, 1)
    reg = orig * (1 - 0.30 * band)
    for role in ('conn', 'light', 'accent', 'protag'):
        m = masks[role]
        bb = m.getbbox()
        if bb is None:
            continue
        if role != 'protag':
            fill = np.ones_like(reg) * (np.array(FILL[role], np.float32) / 255)
        else:
            sub = orig[bb[1]:bb[3], bb[0]:bb[2]]
            lum = float((0.299 * sub[..., 0] + 0.587 * sub[..., 1] + 0.114 * sub[..., 2]).mean())
            dark = state.get('dark', lum > 0.40)
            if dark and lum < 0.36:
                dark = False
            elif (not dark) and lum > 0.44:
                dark = True
            state['dark'] = dark
            c0, c1, c2 = PAL_DARK if dark else PAL_LIGHT
            xs = np.clip((np.arange(W, dtype=np.float32) - bb[0]) / max(bb[2] - bb[0], 1), 0, 1)[None, :, None]
            ys = np.clip((np.arange(h, dtype=np.float32)[:, None, None] - bb[1]) / max(bb[3] - bb[1], 1), 0, 1)
            g = np.where(xs < 0.5, c0 * (1 - np.clip(xs * 2, 0, 1)) + c1 * np.clip(xs * 2, 0, 1),
                         c1 * (1 - np.clip(xs * 2 - 1, 0, 1)) + c2 * np.clip(xs * 2 - 1, 0, 1))
            g = g * (1 - 0.18 * ys)
            tex = 0.80 + 0.40 * CLOUD[y0:y1, :, None]
            bgp = np.asarray(Image.fromarray((orig * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))).astype(np.float32) / 255
            fill = np.clip(0.88 * g * tex + 0.12 * bgp * 0.8, 0, 1)
        reg = _layer(reg, m, fill, OUTLINE[role], SHADOW[role])
    frame[y0:y1] = reg


def _layout(words, lines, y):
    """words: [(texto, rol, tamano, t0)]. Devuelve posiciones (x, baseline) y tamanos finales con ajuste de ancho."""
    d = ImageDraw.Draw(Image.new('L', (4, 4)))
    pos, sizes = {}, {}
    yy = y
    for ln in lines:
        sz = [words[i][2] for i in ln]
        for _ in range(2):
            wd = [d.textlength(words[i][0], font=font(FONTS[words[i][1]], int(sz[j]))) for j, i in enumerate(ln)]
            sp = [sz[j] * 0.28 for j in range(len(ln))]
            tot = sum(wd) + sum(sp[:-1])
            if tot > MAXW:
                sz = [s * MAXW / tot for s in sz]
            else:
                break
        sz = [int(s) for s in sz]
        wd = [d.textlength(words[i][0], font=font(FONTS[words[i][1]], sz[j])) for j, i in enumerate(ln)]
        sp = [sz[j] * 0.28 for j in range(len(ln))]
        x = (W - (sum(wd) + sum(sp[:-1]))) / 2
        mx = max(sz)
        base = yy + mx * 0.85
        for j, i in enumerate(ln):
            pos[i] = (x, base)
            sizes[i] = sz[j]
            x += wd[j] + sp[j]
        yy += int(mx * 1.12)
    return pos, sizes, yy


class Block:
    def __init__(self, words, lines, y, t_end, fade=0.25):
        self.words, self.t_end, self.fade = words, t_end, fade
        self.t0 = min(w[3] for w in words)
        self.pos, self.sizes, yy = _layout(words, lines, y)
        self.y0, self.y1 = max(0, int(y - 60)), min(H, int(yy + 90))
        self.state = {}

    def active(self, t):
        return self.t0 <= t < self.t_end

    def apply(self, frame, t):
        out_a = min(1.0, max(0.0, (self.t_end - t) / self.fade))
        items = []
        for i, (txt, role, size, ts) in enumerate(self.words):
            age = t - ts
            if age < 0:
                continue
            x, base = self.pos[i]
            items.append(dict(text=txt, role=role, size=self.sizes[i], x=x, base=base,
                              alpha=ease_out(age / 0.16) * out_a, yo=(1 - ease_out(age / 0.22)) * 26))
        draw_style(frame, self.y0, self.y1, items, self.state)


class Counter:
    def __init__(self, label, final, fmt, t_start, t_count, t_end, y, size=200, lsize=84):
        self.label, self.final, self.fmt = label, final, fmt
        self.ts, self.tc, self.te = t_start, t_count, t_end
        self.t0 = t_start
        words = [(label, 'conn', lsize, 0), (fmt(final), 'protag', size, 0)]
        self.pos, self.sizes, yy = _layout(words, [[0], [1]], y)
        self.y0, self.y1 = max(0, int(y - 60)), min(H, int(yy + 90))
        self.state = {}
        d = ImageDraw.Draw(Image.new('L', (4, 4)))
        self.xn_w = d.textlength(fmt(final), font=font(FONTS['protag'], self.sizes[1]))

    def active(self, t):
        return self.ts <= t < self.te

    def apply(self, frame, t):
        age = t - self.ts
        s = self.fmt(int(round(self.final * ease_out(age / self.tc))))
        out_a = min(1.0, max(0.0, (self.te - t) / 0.25)) * ease_out(age / 0.16)
        yo = (1 - ease_out(age / 0.22)) * 26
        xl, bl = self.pos[0]
        xn, bn = self.pos[1]
        items = [dict(text=self.label, role='conn', size=self.sizes[0], x=xl, base=bl, alpha=out_a, yo=yo),
                 dict(text=s, role='protag', size=self.sizes[1], x=xn, base=bn, alpha=out_a, yo=yo)]
        draw_style(frame, self.y0, self.y1, items, self.state)


def C(k, off=0.0):
    return CUTS[k] + off


BLOCKS = [
    # 0. Gancho C (0 - 3.0 s)
    Block([('Antes', 'conn', 84, 0.10), ('de', 'conn', 84, 0.32), ('decidir,', 'conn', 84, 0.54),
           ('CONÓZCALO', 'protag', 205, 1.05),
           ('desde', 'accent', 104, 1.75), ('el', 'accent', 104, 1.97), ('aire.', 'accent', 104, 2.19)],
          [[0, 1, 2], [3], [4, 5, 6]], y=900, t_end=3.05),
    # 2. Comacaran (toma 2)
    Block([('COMACARÁN', 'protag', 190, C(2, 0.12)), ('San Miguel', 'accent', 110, C(2, 0.40))],
          [[0], [1]], y=960, t_end=C(3) - 0.05),
    # 5. Escritura / agua (toma 5)
    Block([('Con', 'conn', 84, C(5, 0.12)), ('escritura', 'light', 120, C(5, 0.30)),
           ('AGUA CONECTADA', 'protag', 150, C(5, 0.92))],
          [[0, 1], [2]], y=960, t_end=C(6) - 0.05),
    # 6. Casco urbano (toma 6)
    Block([('Junto al', 'conn', 90, C(6, 0.12)), ('CASCO URBANO', 'protag', 170, C(6, 0.50))],
          [[0], [1]], y=960, t_end=C(7) - 0.05),
    # 8. Calles (toma 8)
    Block([('CALLES INTERIORES', 'protag', 150, C(8, 0.12)), ('y acceso directo', 'accent', 96, C(8, 0.78))],
          [[0], [1]], y=960, t_end=C(9) - 0.05),
]
COUNTERS = [
    Counter('Terrenos desde', 286, lambda n: f'{n} v²', C(3, 0.10), 0.9, C(5) - 0.05, y=900, size=260),
    Counter('desde', 24500, lambda n: 'US$' + f'{n:,}', C(10, 0.10), 0.9, C(11) - 0.02, y=900, size=240),
]
ALL = BLOCKS + COUNTERS


# ---------------- placa final ----------------
def end_card():
    im = Image.new('RGB', (W, H), DG)
    d = ImageDraw.Draw(im)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(24 - 8 * t), int(57 - 14 * t), int(47 - 12 * t)))
    rm = load_logo(LOGOS + r'\remax\2.png', 300, shadow=False)
    im.paste(rm, (70, 262), rm)
    si = load_logo(ASSETS + r'\logo_si_vertical.png', 500, shadow=False)
    im.paste(si, ((W - si.width) // 2, 400), si)
    y = 400 + si.height + 60
    t1 = 'Coordine su visita'
    d.text(((W - d.textlength(t1, font=font(GEOB, 88))) / 2, y), t1, font=font(GEOB, 88), fill=CREAM)
    y += 130
    d.rounded_rectangle([70, y, 1010 - 70 + 70, y + 200], radius=34, fill=LIME)
    t2, t3 = 'Escríbame al', '+503 7956 4399'
    d.text(((W - d.textlength(t2, font=font(SEG, 40))) / 2, y + 22), t2, font=font(SEG, 40), fill=DG)
    d.text(((W - d.textlength(t3, font=font(SEG, 84))) / 2, y + 74), t3, font=font(SEG, 84), fill=DG)
    y += 230
    t4 = 'Nixon Hernández OLY — Asesor Inmobiliario'
    d.text(((W - d.textlength(t4, font=font(SEGR, 34))) / 2, y), t4, font=font(SEGR, 34), fill=CREAM)
    y += 70
    bi = Image.open(LOGOS + r'\banco_industrial\logo-banco-industrial.png').convert('RGBA')
    bi = bi.crop(bi.getbbox())
    bh = 52
    bi = bi.resize((int(bi.width * bh / bi.height), bh), Image.LANCZOS)
    plate = Image.new('RGBA', (bi.width + 28, bh + 20), (248, 247, 242, 255))
    pm = Image.new('L', plate.size, 0)
    ImageDraw.Draw(pm).rounded_rectangle([0, 0, plate.width - 1, plate.height - 1], radius=12, fill=255)
    plate.alpha_composite(bi, (14, 10))
    im.paste(plate.convert('RGB'), (70, y), pm)
    fn = font(SEGR, 27)
    d.text((70 + plate.width + 24, y + 4), '*Financiamiento con Banco Industrial', font=fn, fill=(214, 226, 214))
    d.text((70 + plate.width + 24, y + 38), 'sujeto a evaluación del banco.', font=fn, fill=(214, 226, 214))
    d.text((70, y + 104), 'Sujeto a disponibilidad.', font=fn, fill=(190, 205, 190))
    return im


CARD_IMG = np.asarray(end_card()).astype(np.float32) / 255
CARD_IMG.setflags(write=False)


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

# ---------------- bucle principal ----------------
PROXY_FILE = {'0193': '0193', '0201': '0201', '0196': '0196', '0197': '0197', '0199': '0199', '0198': '0198',
              '0192': '0192', 'orbita': 'orbita'}


def read_shot(name, ss, nframes):
    """Lee la toma cuadro a cuadro (poca RAM): generador de arreglos uint8."""
    p = PROX + rf'\{PROXY_FILE[name]}_sdr_9x16.mp4'
    cmd = [FF, '-v', 'error', '-ss', f'{ss:.3f}', '-i', p, '-frames:v', str(nframes), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    size = W * H * 3
    last = None
    for _ in range(nframes):
        raw = pr.stdout.read(size)
        if len(raw) == size:
            last = np.frombuffer(raw, np.uint8).reshape(H, W, 3)
        yield last
    pr.stdout.close()
    pr.wait()


def zoom(frame_u8, z):
    if z <= 1.0005:
        return frame_u8.astype(np.float32) / 255
    cw, ch = W / z, H / z
    x0, y0 = (W - cw) / 2, (H - ch) / 2
    im = Image.fromarray(frame_u8).resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))
    return np.asarray(im).astype(np.float32) / 255


os.makedirs(OUTDIR, exist_ok=True)
NAME = 'N360_REMAX_PROPERTY_SANTAISABEL_REEL_9x16_hookC_v06'
SILENT = BUILD + rf'\{NAME}_mudo.mp4'
enc = subprocess.Popen([FF, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPSV),
                        '-i', '-', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p',
                        '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', SILENT],
                       stdin=subprocess.PIPE)
total_frames = int(round(TOTAL * FPSV))
if LIMIT:
    total_frames = int(LIMIT * FPSV)
fidx = 0
prev = None
for k, (name, ss) in enumerate(SHOTS):
    f0, f1 = int(round(CUTS[k] * FPSV)), int(round(CUTS[k + 1] * FPSV))
    if f0 >= total_frames:
        break
    frames = read_shot(name, ss, f1 - f0)
    for j in range(f1 - f0):
        if fidx >= total_frames:
            break
        t = fidx / FPSV
        tl = j / FPSV
        u = tl / SH
        z = 1.0 + 0.065 * u + 0.075 * max(0.0, 1 - tl / 0.16) ** 2
        fr = zoom(next(frames), z)
        for b in ALL:
            if b.active(t):
                b.apply(fr, t)
        for (pk, plab, px, py, pside) in PINS:
            if pk == k and 0.25 <= tl < SH - 0.2:
                pa = smooth((tl - 0.25) / 0.3) * (1 - smooth((tl - (SH - 0.5)) / 0.3))
                key = (plab, px, py)
                if key not in PIN_CACHE:
                    PIN_CACHE[key] = pin_layer(px, py, plab, 1.0, pside)
                comp_layer(fr, PIN_CACHE[key], pa)
        paste_rgba(fr, LOGO_REMAX, (W - LOGO_REMAX.width) // 2, 1560 - LOGO_REMAX.height + PAD, 1.0 if t > 0.25 else t / 0.25)
        if 2.95 <= t < C(2) - 0.15:
            a = min(1, (t - 2.95) / 0.25, (C(2) - 0.15 - t) / 0.25)
            paste_rgba(fr, LOGO_SI, (W - LOGO_SI.width) // 2, 270 - PAD, a)
        enc.stdin.write((np.clip(fr, 0, 1) * 255).astype(np.uint8).tobytes())
        prev = fr.copy() if j >= f1 - f0 - 2 else None
        fidx += 1
    if k % 2 == 0:
        print('toma', k + 1, 'ok', flush=True)
# cierre v5 animado
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
enc.stdin.close()
enc.wait()
print('video mudo listo', fidx, 'cuadros')

# mezcla final con audio y loudness
FINAL = OUTDIR + rf'\{NAME}.mp4'
subprocess.run([FF, '-y', '-v', 'error', '-i', SILENT, '-i', BUILD + r'\audio_mix.wav',
                '-af', f'apad=whole_dur={TOTAL:.2f},loudnorm=I=-14:TP=-1.5:LRA=9', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
                '-shortest', '-movflags', '+faststart', FINAL])
print('FINAL', FINAL)
