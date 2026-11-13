# -*- coding: utf-8 -*-
"""Video 2 (9:16): calles asfaltadas sobre FOTO LIMPIA, trazo animado, pines con nombres del plano, cierre v5.
Usa el nucleo de estilo de video_build_v05.py (draw_style, Block, logos) y el kit (mock_kit.cierre_v5)."""
import os, sys, subprocess
import numpy as np, cv2
from PIL import Image, ImageDraw

BUILD = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(BUILD, 'video_build_v05.py'), encoding='utf-8').read()
exec(compile(src[:src.index('def C(k')], 'v05_core', 'exec'))          # fuentes, Block, draw_style, logos, W, H, FF, ...

sys.path.insert(0, r'E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\_KIT')
import mock_kit as MK

FPS = 25
OUT_NAME = 'N360_REMAX_PROPERTY_SANTAISABEL_REEL_9x16_video2_calles_v01'
LIMIT2 = float(os.environ.get('LIMIT_SEC', '0'))
YEL = np.array([236, 214, 40], np.float32) / 255
PHOTO = r'E:\Lotificación Alvarez\_marca\fotos_limpias\SI_FOTO_calles-desde-arriba_v01.jpg'
BG_CIERRE = r'E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001\work\sm\bgc_calles-desde-arriba_9x16.png'
FOTO_NIXON = ASSETS + r'\nixon_recorte.png'

im0 = Image.open(PHOTO).convert('RGB')
PW, PH = im0.size                                   # 1672 x 941
UP = im0.resize((PW * 2, PH * 2), Image.LANCZOS)

T_SCENE = 12.6
T_CIERRE = 4.2
T_FADE = 0.45
TOTAL2 = T_SCENE + T_CIERRE

# calles trazadas a mano sobre la foto (coordenadas de la foto 1672x941) - nombres del plano, confirmados por Nixon
STREETS = [
    ('Calle Isabel Poniente', [(590, 345), (604, 430), (624, 540), (644, 603)], 2.5, 'der'),
    ('Calle Los Colibríes', [(862, 388), (850, 440), (826, 520), (802, 585)], 4.6, 'izq'),
    ('Calle Isabel Sur', [(655, 612), (900, 612), (1128, 622)], 6.7, 'izq'),
    ('Calle Isabel Oriente', [(1142, 414), (1144, 500), (1146, 580), (1140, 616)], 8.6, 'izq'),
]
DUR_DRAW = 1.5
# cámara: (t, cx, cy, zoom) en coordenadas de la foto
CAM = [(0.0, 860, 470, 1.00), (2.2, 640, 470, 1.22), (4.4, 830, 480, 1.22), (6.5, 900, 520, 1.20),
       (8.4, 1090, 520, 1.22), (10.4, 960, 500, 1.05), (12.6, 880, 470, 1.00)]


def smooth(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)


def cam_at(t):
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
    box = (x0 * 2, y0 * 2, (x0 + cww) * 2, (y0 + chh) * 2)
    im = UP.resize((W, H), Image.LANCZOS, box=box)
    return np.asarray(im).astype(np.float32) / 255, (x0, y0, W / cww)


def to_out(p, v):
    x0, y0, sc = v
    return ((p[0] - x0) * sc, (p[1] - y0) * sc)


def partial(pts, frac):
    seg = [np.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts[:-1], pts[1:])]
    tot = sum(seg)
    goal, out, acc = tot * frac, [pts[0]], 0.0
    for (a, b), s in zip(zip(pts[:-1], pts[1:]), seg):
        if acc + s <= goal:
            out.append(b)
            acc += s
        else:
            r = (goal - acc) / s
            out.append((a[0] + (b[0] - a[0]) * r, a[1] + (b[1] - a[1]) * r))
            break
    return out


def draw_street(fr, pts_out, alpha=1.0, thick=15):
    if len(pts_out) < 2:
        return
    m = np.zeros((H, W), np.uint8)
    pp = np.array([[int(x), int(y)] for x, y in pts_out], np.int32)
    cv2.polylines(m, [pp], False, 255, thick, cv2.LINE_AA)
    mw = np.zeros((H, W), np.uint8)
    cv2.polylines(mw, [pp], False, 255, 62, cv2.LINE_AA)
    mwf = cv2.GaussianBlur(mw, (0, 0), 4).astype(np.float32)[..., None] / 255
    fr[:] = fr * (1 - 0.30 * mwf * alpha) + YEL * 0.30 * mwf * alpha
    glow = cv2.GaussianBlur(m, (0, 0), 14).astype(np.float32) / 255
    core = (m.astype(np.float32) / 255)[..., None]
    # relleno suave sobre la calle y brillo
    fr += YEL * glow[..., None] * 0.55 * alpha
    fr[:] = fr * (1 - 0.88 * core * alpha) + YEL * 0.88 * core * alpha


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
    if side == 'der':
        bx0 = cx + r + 8
    else:
        bx0 = cx - r - 8 - tw - 36 * k
    bx0 = min(max(bx0, 40), W - 40 - tw - 36 * k)
    by0, by1 = cy - int(30 * k), cy + int(30 * k)
    d.rounded_rectangle([bx0, by0, bx0 + tw + 36 * k, by1], radius=int(30 * k), fill=(12, 12, 12, 185))
    d.text((bx0 + 18 * k, cy), label, font=f, fill=(255, 255, 255, 255), anchor='lm')
    return L


def comp_layer(fr, L, alpha=1.0):
    a = np.asarray(L).astype(np.float32) / 255
    aa = a[..., 3:4] * alpha
    fr[:] = fr * (1 - aa) + a[..., :3] * aa


# ----- textos del kit
TITLE = Block([('Calles', 'conn', 90, 0.25), ('ASFALTADAS', 'protag', 175, 0.55), ('dentro de la lotificación', 'accent', 74, 1.1)],
              [[0], [1], [2]], y=1020, t_end=2.35)
CLOSE_T = Block([('PAZ Y TRANQUILIDAD', 'protag', 125, 9.9), ('a minutos de la ciudad', 'accent', 80, 10.5)], [[0], [1]], y=1020, t_end=12.3)


def cierre_frame(tc):
    """tc: segundos dentro del cierre. Foto: zoom in, mantiene, zoom out."""
    if tc < 1.4:
        s = 0.92 + 0.08 * smooth(tc / 1.4)
    elif tc < T_CIERRE - 0.9:
        s = 1.0
    else:
        s = 1.0 - 0.06 * smooth((tc - (T_CIERRE - 0.9)) / 0.9)
    return MK.cierre_v5(BG_CIERRE, FOTO_NIXON, None, (W, H), guias=False, fscale=s, falpha=min(1.0, tc / 0.3))


os.makedirs(OUTDIR, exist_ok=True)
SILENT2 = BUILD + rf'\{OUT_NAME}_mudo.mp4'
enc = subprocess.Popen([FF, '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p',
                        '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', SILENT2], stdin=subprocess.PIPE)
n_total = int(TOTAL2 * FPS)
if LIMIT2:
    n_total = int(LIMIT2 * FPS)
last_scene = None
for i in range(n_total):
    t = i / FPS
    if t < T_SCENE:
        fr, v = render_photo(t)
        for name, pts, t0, side in STREETS:
            if t >= t0:
                fr_prog = smooth((t - t0) / DUR_DRAW)
                draw_street(fr, [to_out(p, v) for p in partial(pts, fr_prog)])
        # etiquetas (pines) tras terminar cada trazo, visibles hasta que entra la siguiente
        for k, (name, pts, t0, side) in enumerate(STREETS):
            ta = t0 + DUR_DRAW * 0.8
            tb = STREETS[k + 1][2] + 0.2 if k + 1 < len(STREETS) else 10.0
            if ta <= t < tb or (t >= 10.0 and k >= 0 and False):
                a = smooth((t - ta) / 0.3) * (1 - smooth((t - (tb - 0.4)) / 0.4) if k + 1 < len(STREETS) else 1.0)
                mid = pts[len(pts) // 2]
                px, py = to_out(mid, v)
                comp_layer(fr, pin_layer(int(px), int(py), name, 1.0, side), a)
        if 9.2 <= t < 12.3:
            aj = smooth((t - 9.2) / 0.3) * (1 - smooth((t - 11.9) / 0.4))
            jx, jy = to_out((1000, 386), v)
            comp_layer(fr, pin_layer(int(jx), int(jy), 'Calle al Jicaral', 1.0, 'izq'), aj)
        for b in (TITLE, CLOSE_T):
            if b.active(t):
                b.apply(fr, t)
        paste_rgba(fr, LOGO_REMAX, (W - LOGO_REMAX.width) // 2, 1560 - LOGO_REMAX.height + PAD, min(1.0, t / 0.4))
        paste_rgba(fr, LOGO_SI, (W - LOGO_SI.width) // 2, 270 - PAD, min(1.0, t / 0.4))
        last_scene = fr
        out = fr
    else:
        tc = t - T_SCENE
        cf = np.asarray(cierre_frame(tc)).astype(np.float32) / 255
        if tc < T_FADE and last_scene is not None:
            a = smooth(tc / T_FADE)
            out = last_scene * (1 - a) + cf * a
        else:
            out = cf
    enc.stdin.write((np.clip(out, 0, 1) * 255).astype(np.uint8).tobytes())
    if i % 25 == 0:
        print('seg', i // 25, flush=True)
enc.stdin.close()
enc.wait()
print('LISTO', SILENT2)
