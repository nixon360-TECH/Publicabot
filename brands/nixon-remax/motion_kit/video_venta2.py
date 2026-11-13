# -*- coding: utf-8 -*-
"""Video 2 «venta» SET 2 (otras tomas, otros ganchos D/E/F, mismas palabras y orden) (9:16, 30 s): mismo cuerpo en 3 versiones, solo cambia el gancho (A/B/C).
Dice SIEMPRE: Lotificación Santa Isabel, ubicación, tamaño, precio, cercanía (parque central e instituto),
con escritura y agua conectada, Banco Industrial*, CTA.
Uso: python video_venta.py hookD|hookE|hookF|body   -> build/parts/v2_<parte>_mudo.mp4"""
import os, sys, subprocess
import numpy as np, cv2
from PIL import Image, ImageDraw

BUILD = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(BUILD, 'video_build_v05.py'), encoding='utf-8').read()
exec(compile(src[:src.index('def C(k')], 'v05_core', 'exec'))      # fuentes, Block, Counter, draw_style, logos, W, H, FF, PROX...
sys.path.insert(0, r'E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\_KIT')
import mock_kit as MK

PART = sys.argv[1] if len(sys.argv) > 1 else 'body'
LIM = float(os.environ.get('LIMIT_SEC', '0'))
FPS = 25
PARTS = BUILD + r'\parts'
os.makedirs(PARTS, exist_ok=True)
YEL = np.array([236, 214, 40], np.float32) / 255
PHOTO = r'E:\Lotificación Alvarez\_marca\fotos_limpias\SI_FOTO_calles-desde-arriba_v01.jpg'
BG_CIERRE = r'E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001\work\sm\bgc_vista-colinas_9x16.png'
FOTO_NIXON = ASSETS + r'\nixon_recorte.png'

# ---- cronologia global (s)
T1, T2, T3, T4, TC, TEND = 4.0, 11.0, 19.0, 25.0, 25.0, 30.0
S1_END, S2_END, S3_END, S4_END = 4.0, 11.0, 19.0, 25.0


def smooth(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def proxy_frames(name, ss, n):
    p = PROX + rf'\{name}_sdr_9x16.mp4'
    cmd = [FF, '-v', 'error', '-ss', f'{ss:.3f}', '-i', p, '-frames:v', str(n), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    size = W * H * 3
    last = None
    for _ in range(n):
        raw = pr.stdout.read(size)
        if len(raw) == size:
            last = np.frombuffer(raw, np.uint8).reshape(H, W, 3)
        yield last
    pr.stdout.close()
    pr.wait()


def zoom_f(fr_u8, z):
    if z <= 1.0005:
        return fr_u8.astype(np.float32) / 255
    cw, ch = W / z, H / z
    x0, y0 = (W - cw) / 2, (H - ch) / 2
    im = Image.fromarray(fr_u8).resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))
    return np.asarray(im).astype(np.float32) / 255


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
    d.rounded_rectangle([bx0, cy - int(30 * k), bx0 + tw + 36 * k, cy + int(30 * k)], radius=int(30 * k), fill=(12, 12, 12, 190))
    d.text((bx0 + 18 * k, cy), label, font=f, fill=(255, 255, 255, 255), anchor='lm')
    return L


def comp_layer(fr, L, alpha=1.0):
    a = np.asarray(L).astype(np.float32) / 255
    aa = a[..., 3:4] * alpha
    fr[:] = fr * (1 - aa) + a[..., :3] * aa


def legal_layer():
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(L)
    f = font(SEG, 24)
    for i, t in enumerate(('*Financiamiento con Banco Industrial sujeto a evaluación del banco.', 'Sujeto a disponibilidad.')):
        d.text((W // 2, 1372 + i * 30), t, font=f, fill=(255, 255, 255, 240), anchor='mm', stroke_width=2, stroke_fill=(0, 0, 0, 200))
    return L


def logos(fr, t, remax=True, si=False):
    if si:
        paste_rgba(fr, LOGO_SI, (W - LOGO_SI.width) // 2, 270 - PAD, min(1.0, t / 0.4))
    if remax:
        paste_rgba(fr, LOGO_REMAX, (W - LOGO_REMAX.width) // 2, 1560 - LOGO_REMAX.height + PAD, min(1.0, t / 0.4))


# ---- v01b: letras azules mas claras y con menos sombra (pedido de Nixon: no se veian a la izquierda)
PAL_DARK = [np.array(c, np.float32) / 255 for c in ((28, 92, 150), (38, 135, 188), (70, 195, 215))]
SHADOW['protag'] = 0.30

# ---------------- textos (estilo en capas del kit) ----------------
HOOKS = {
    'hookD': Block([('¿Sueña con', 'conn', 84, 0.2), ('SU CASA PROPIA', 'protag', 165, 0.9), ('en San Miguel?', 'accent', 96, 1.8)],
                   [[0], [1], [2]], y=960, t_end=S1_END - 0.05),
    'hookE': Block([('Terrenos desde', 'conn', 90, 0.2), ('286 v²', 'protag', 215, 0.9), ('en Comacarán', 'accent', 96, 1.8)],
                   [[0], [1], [2]], y=960, t_end=S1_END - 0.05),
    'hookF': Block([('Con escritura y', 'conn', 84, 0.2), ('AGUA CONECTADA', 'protag', 150, 0.9), ('en Comacarán', 'accent', 96, 1.8)],
                   [[0], [1], [2]], y=960, t_end=S1_END - 0.05),
}
HOOKS['hookG1'] = Block([('¿Cuánto cuesta un terreno', 'conn', 70, 0.2), ('EN COMACARÁN?', 'protag', 150, 0.8), ('Desde US$24,500', 'accent', 100, 1.9)],
                        [[0], [1], [2]], y=960, t_end=S1_END - 0.05)
HOOKS['hookG4'] = Block([('¿Y al comprar', 'conn', 90, 0.2), ('ME DAN MI', 'protag', 170, 0.7), ('ESCRITURA?', 'protag', 190, 1.3)],
                        [[0], [1], [2]], y=940, t_end=S1_END - 0.05)
HOOKS['hookH'] = Block([('Hermano lejano,', 'conn', 90, 0.2), ('SU TERRENO', 'protag', 175, 0.8), ('en Comacarán, El Salvador', 'accent', 80, 1.7)],
                       [[0], [1], [2]], y=960, t_end=S1_END - 0.05)
HOOK_CLIP = {'hookD': 'sm_0554', 'hookE': 'sm_0557', 'hookF': 'sm_0555', 'hookG1': 'sm_0560', 'hookG4': 'sm_0570', 'hookH': 'sm_0576'}
# S2: primero el nombre (sin logo arriba, para no repetir); despues SOLO los pines de ubicacion
B2a = Block([('Lotificación', 'conn', 80, T1 + 0.2), ('SANTA ISABEL', 'protag', 170, T1 + 0.6), ('Comacarán, San Miguel', 'accent', 84, T1 + 1.4)],
            [[0], [1], [2]], y=1090, t_end=T1 + 3.2)
B3 = Block([('Terrenos desde', 'conn', 80, T2 + 0.2), ('286 v²', 'protag', 200, T2 + 0.6), ('Con escritura y agua conectada', 'accent', 62, T2 + 1.4)],
           [[0], [1], [2]], y=1000, t_end=T2 + 3.3)
if PART == 'body2b':
    B3 = Block([('Terrenos desde', 'conn', 76, T2 + 0.2), ('286 v²', 'protag', 190, T2 + 0.6), ('Con escritura y agua conectada', 'accent', 60, T2 + 1.4),
                ('listos para construir', 'light', 70, T2 + 2.1)], [[0], [1], [2], [3]], y=960, t_end=T2 + 3.5)
CNT = Counter('Terrenos desde', 24500, lambda n: 'US$' + f'{n:,}', T3 + 0.1, 1.2, T4 - 0.05, y=860, size=215, lsize=84)
B4 = Block([('Financiamiento Banco Industrial*', 'accent', 62, T3 + 1.8)], [[0]], y=1230, t_end=T4 - 0.05)
LEGAL = legal_layer()

# ---------------- escena foto limpia (calles trazadas a mano, nombres del plano) ----------------
im0 = Image.open(PHOTO).convert('RGB')
PW, PH = im0.size
UP = im0.resize((PW * 2, PH * 2), Image.LANCZOS)
STREETS = [
    ('Calle Isabel Poniente', [(590, 345), (604, 430), (624, 540), (644, 603)], 3.5, 'der'),
    ('Calle Los Colibríes', [(862, 388), (850, 440), (826, 520), (802, 585)], 4.5, 'izq'),
    ('Calle Isabel Sur', [(655, 612), (900, 612), (1128, 622)], 5.5, 'izq'),
    ('Calle Isabel Oriente', [(1142, 414), (1144, 500), (1146, 580), (1140, 616)], 6.5, 'izq'),
]
DUR_DRAW = 1.0
CAM = [(0, 860, 470, 1.00), (3.2, 860, 470, 1.02), (4.0, 640, 470, 1.22), (5.0, 830, 480, 1.22), (6.0, 900, 520, 1.20),
       (7.0, 1090, 520, 1.22), (8.0, 960, 500, 1.05)]


def cam_at(t):
    t = min(max(t, 0), CAM[-1][0])
    for a, b in zip(CAM[:-1], CAM[1:]):
        if a[0] <= t <= b[0]:
            u = smooth((t - a[0]) / (b[0] - a[0]))
            return tuple(a[i] + (b[i] - a[i]) * u for i in (1, 2, 3))
    return CAM[-1][1:]


def view(t):
    cx, cy, z = cam_at(t)
    chh = PH / z
    cww = chh * W / H
    x0 = min(max(cx - cww / 2, 0), PW - cww)
    y0 = min(max(cy - chh / 2, 0), PH - chh)
    return x0, y0, cww, chh


def render_photo(t):
    x0, y0, cww, chh = view(t)
    im = UP.resize((W, H), Image.LANCZOS, box=(x0 * 2, y0 * 2, (x0 + cww) * 2, (y0 + chh) * 2))
    return np.asarray(im).astype(np.float32) / 255, (x0, y0, W / cww)


def to_out(p, v):
    return ((p[0] - v[0]) * v[2], (p[1] - v[1]) * v[2])


def partial(pts, frac):
    seg = [np.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts[:-1], pts[1:])]
    goal, out, acc = sum(seg) * frac, [pts[0]], 0.0
    for (a, b), s in zip(zip(pts[:-1], pts[1:]), seg):
        if acc + s <= goal:
            out.append(b)
            acc += s
        else:
            r = (goal - acc) / s
            out.append((a[0] + (b[0] - a[0]) * r, a[1] + (b[1] - a[1]) * r))
            break
    return out


def draw_street(fr, pts_out, thick=15):
    if len(pts_out) < 2:
        return
    pp = np.array([[int(x), int(y)] for x, y in pts_out], np.int32)
    m = np.zeros((H, W), np.uint8)
    cv2.polylines(m, [pp], False, 255, thick, cv2.LINE_AA)
    mw = np.zeros((H, W), np.uint8)
    cv2.polylines(mw, [pp], False, 255, 62, cv2.LINE_AA)
    mwf = cv2.GaussianBlur(mw, (0, 0), 4).astype(np.float32)[..., None] / 255
    fr[:] = fr * (1 - 0.30 * mwf) + YEL * 0.30 * mwf
    glow = cv2.GaussianBlur(m, (0, 0), 14).astype(np.float32) / 255
    core = (m.astype(np.float32) / 255)[..., None]
    fr += YEL * glow[..., None] * 0.55
    fr[:] = fr * (1 - 0.88 * core) + YEL * 0.88 * core


def cierre_frame(tc, dur=TEND - TC):
    if tc < 1.4:
        sc = 0.92 + 0.08 * smooth(tc / 1.4)
    elif tc < dur - 0.9:
        sc = 1.0
    else:
        sc = 1.0 - 0.06 * smooth((tc - (dur - 0.9)) / 0.9)
    return np.asarray(MK.cierre_v5(BG_CIERRE, FOTO_NIXON, None, (W, H), guias=False, fscale=sc, falpha=min(1.0, tc / 0.3))).astype(np.float32) / 255


# ---------------- generador de cuadros por parte (SET 2) ----------------
def load_up(name):
    im = Image.open(rf'E:\Lotificación Alvarez\_marca\fotos_limpias\SI_FOTO_{name}_v01.jpg').convert('RGB')
    return im.resize((im.width * 2, im.height * 2), Image.LANCZOS), im.size


def render_up(up, size, cx, cy, z):
    pw, ph = size
    chh = ph / z
    cww = chh * W / H
    x0 = min(max(cx - cww / 2, 0), pw - cww)
    y0 = min(max(cy - chh / 2, 0), ph - chh)
    im = up.resize((W, H), Image.LANCZOS, box=(x0 * 2, y0 * 2, (x0 + cww) * 2, (y0 + chh) * 2))
    return np.asarray(im).astype(np.float32) / 255


def gen_hook(key):
    n = int(S1_END * FPS)
    gen = proxy_frames(HOOK_CLIP[key], 0.0, n)
    b = HOOKS[key]
    for i in range(n):
        t = i / FPS
        z = 1.0 + 0.07 * (t / S1_END) + 0.075 * max(0.0, 1 - t / 0.16) ** 2
        fr = zoom_f(next(gen), z)
        if b.active(t):
            b.apply(fr, t)
        logos(fr, t)
        yield fr


def gen_body():
    # S2: nombre (sin logo arriba) y despues solo pines de ubicacion (0199)
    n2 = int((S2_END - T1) * FPS)
    g2 = proxy_frames('0199', 3.0, n2)
    for i in range(n2):
        tl = i / FPS
        t = T1 + tl
        z = 1.0 + 0.06 * (tl / (S2_END - T1))
        fr = zoom_f(next(g2), z)
        if B2a.active(t):
            B2a.apply(fr, t)
        for lab, px, py, ta in (('Parque central de Comacarán', 518, 460, 3.5), ('Instituto Nacional de Comacarán', 348, 1040, 4.3)):
            if tl >= ta:
                cx0, cy0 = W / 2, H / 2
                x, y = cx0 + (px - cx0) * z, cy0 + (py - cy0) * z
                key = ('pin', lab)
                if key not in PINC:
                    PINC[key] = pin_layer(int(x), int(y), lab, 1.2, 'der')
                comp_layer(fr, PINC[key], smooth((tl - ta) / 0.3) * (1 - smooth((tl - (S2_END - T1 - 0.4)) / 0.3)))
        logos(fr, t, si=False)
        yield fr
    # S3: dos fotos limpias con movimiento de camara
    upA, szA = load_up('vista-colinas')
    upB, szB = load_up('lote-borde')
    n3 = int((S3_END - T2) * FPS)
    for i in range(n3):
        tl = i / FPS
        t = T2 + tl
        a = render_up(upA, szA, 836 + 50 * tl / 4.4, 520, 1.0 + 0.28 * smooth(tl / 4.4))
        if tl > 3.7:
            b = render_up(upB, szB, 650 + 420 * smooth((tl - 3.7) / 4.3), 470, 1.12)
            m = smooth((tl - 3.7) / 0.5)
            fr = a * (1 - m) + b * m
        else:
            fr = a
        if B3.active(t):
            B3.apply(fr, t)
        logos(fr, t)
        yield fr
    # S4: precio sobre cenital 0558
    n4 = int((S4_END - T3) * FPS)
    g4 = proxy_frames('sm_0558', 2.0, n4)
    for i in range(n4):
        tl = i / FPS
        t = T3 + tl
        z = 1.0 + 0.06 * (tl / (S4_END - T3))
        fr = zoom_f(next(g4), z)
        if CNT.active(t):
            CNT.apply(fr, t)
        if B4.active(t):
            B4.apply(fr, t)
        if tl > 1.8:
            comp_layer(fr, LEGAL, smooth((tl - 1.8) / 0.3))
        logos(fr, t)
        yield fr
        last = fr
    ncz = int((TEND - TC) * FPS)
    for j in range(ncz):
        tc = j / FPS
        c = cierre_frame(tc)
        if tc < 0.4:
            a = smooth(tc / 0.4)
            c = last * (1 - a) + c * a
        yield c


PINC = {}
gen = {'hookD': lambda: gen_hook('hookD'), 'hookE': lambda: gen_hook('hookE'), 'hookF': lambda: gen_hook('hookF'), 'hookG1': lambda: gen_hook('hookG1'), 'hookG4': lambda: gen_hook('hookG4'), 'hookH': lambda: gen_hook('hookH'), 'body': gen_body, 'body2b': gen_body}[PART]()
OUT = PARTS + rf'\v2_{PART}_mudo.mp4'
enc = subprocess.Popen([FF, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-g', '25',
                        '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', OUT], stdin=subprocess.PIPE)
cnt = 0
for fr in gen:
    enc.stdin.write((np.clip(fr, 0, 1) * 255).astype(np.uint8).tobytes())
    cnt += 1
    if cnt % 25 == 0:
        print(PART, 'seg', cnt // 25, flush=True)
    if LIM and cnt >= LIM * FPS:
        break
enc.stdin.close()
enc.wait()
print('LISTO', PART, cnt, 'cuadros')
