"""Mocks del kit: cierre editable (9x16 y 4x5) y pines + contorno sobre toma cenital.
Lee kit_nixon_remax.json. Uso: python mock_kit.py"""
import json, os, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

KIT = os.path.dirname(os.path.abspath(__file__))
P = r"E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001"
SM = P + r"\work\sm"
cfg = json.load(open(KIT + r"\kit_nixon_remax.json", encoding="utf8"))
FD = r"C:\Windows\Fonts"
def F(name, size):
    return ImageFont.truetype(FD + "\\" + name, size)
IMPACT, GEORI, SEGBL = "impact.ttf", "georgiai.ttf", "seguibl.ttf"
YEL = (236, 214, 40)

def shadow_layer(img_rgba, blur, grow=0, alpha=0.8, off=(0, 6)):
    a = img_rgba.split()[3]
    if grow:
        a = a.filter(ImageFilter.MaxFilter(grow * 2 + 1))
    a = a.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * alpha))
    s = Image.new("RGBA", img_rgba.size, (0, 0, 0, 0)); s.putalpha(a)
    return ImageChops.offset(s, *off)

def text_layer(size, xy, txt, font, fill, anchor="ms", stroke=0, stroke_fill=(0, 0, 0)):
    L = Image.new("RGBA", size, (0, 0, 0, 0))
    ImageDraw.Draw(L).text(xy, txt, font=font, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=stroke_fill)
    return L

def comp(base, layer, shadow=True):
    if shadow:
        base = Image.alpha_composite(base, shadow_layer(layer, 14, 2, 0.85, (0, 8)))
        base = Image.alpha_composite(base, shadow_layer(layer, 4, 0, 0.9, (0, 3)))
    return Image.alpha_composite(base, layer)

def darken(bg, amt=0.35):
    bg = bg.convert("RGBA")
    W, H = bg.size
    v = np.zeros((H, W), np.float32)
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    v = np.clip(amt + 0.25 * d, 0, 0.75)
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ov.putalpha(Image.fromarray((v * 255).astype(np.uint8)))
    return Image.alpha_composite(bg, ov)

def cierre(bg_path, foto, out, size, fmt):
    W, H = size
    bg = Image.open(bg_path).convert("RGB")
    s = max(W / bg.width, H / bg.height); bg = bg.resize((int(bg.width * s), int(bg.height * s)), Image.LANCZOS)
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
    img = darken(bg, 0.30)
    c = cfg["cierre"]
    tall = H > 1500
    # foto
    ph = Image.open(foto).convert("RGBA")
    ph_h = int(H * (0.50 if tall else 0.52)); ph = ph.resize((int(ph.width * ph_h / ph.height), ph_h), Image.LANCZOS)
    px = (W - ph.width) // 2; py = int(H * (0.14 if tall else 0.10))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); lay.paste(ph, (px, py), ph)
    img = Image.alpha_composite(img, shadow_layer(lay, 26, 0, 0.7, (0, 14)))
    img = Image.alpha_composite(img, lay)
    # firma, frase, tel
    y = py + ph_h - int(H * 0.03)
    sig = text_layer((W, H), (W // 2, y), c["firma"]["texto"], F(GEORI, int(c["firma"]["tamano_px"] * (1 if tall else 0.9))), (255, 255, 255, 255), "ms")
    img = comp(img, sig)
    y += int(H * 0.040)
    fr = text_layer((W, H), (W // 2, y), c["frase"], F(SEGBL, 44 if tall else 40), (240, 232, 214, 255), "ms", 1)
    img = comp(img, fr)
    y += int(H * 0.075)
    tel = text_layer((W, H), (W // 2, y), c["telefono"]["texto"], F(IMPACT, int(c["telefono"]["tamano_px"] * (1 if tall else 0.9))), YEL + (255,), "ms", 2)
    img = comp(img, tel)
    # logos
    rm = Image.open(cfg["logos"]["remax_abajo_centro"]["archivo"]).convert("RGBA")
    rw = 270; rm = rm.resize((rw, int(rm.height * rw / rm.width)), Image.LANCZOS)
    gz = cfg["plataformas"]["master_9x16" if tall else "post_4x5"]["zona_segura_px"]
    base_y = H - gz["abajo"] - 75
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); lay.paste(rm, ((W - rw) // 2, base_y - rm.height), rm)
    img = comp(img, lay)
    # asterisco / disponibilidad (pequeño)
    fy = base_y + 24
    for t in (c["banco_asterisco"], c["disponibilidad"]):
        lay = text_layer((W, H), (W // 2, fy), t, F(SEGBL, 24), (255, 255, 255, 235), "ms", 1)
        img = comp(img, lay); fy += 30
    # guias de zona segura (solo mock)
    g = cfg["plataformas"]["master_9x16" if tall else "post_4x5"]["zona_segura_px"]
    d = ImageDraw.Draw(img)
    d.rectangle([g["izquierda"], g["arriba"], W - g["derecha"], H - g["abajo"]], outline=(255, 0, 80, 150), width=2)
    img.convert("RGB").save(out)

def pin(d, base, x, y, label, k=1.0):
    r = int(32 * k)
    cx, cy = x, y - int(r * 2.3)
    d.polygon([(cx - r * .72, cy + r * .6), (cx + r * .72, cy + r * .6), (x, y)], fill=YEL + (255,), outline=(16, 16, 16, 255))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=YEL + (255,), outline=(16, 16, 16, 255), width=3)
    d.ellipse([cx - r * .38, cy - r * .38, cx + r * .38, cy + r * .38], fill=(255, 255, 255, 255))
    f = F(SEGBL, int(34 * k)); tw = d.textlength(label, font=f)
    bx0 = cx + r + 10
    if bx0 + tw + 34 > 1020: bx0 = cx - r - 10 - tw - 34
    by0 = cy - int(28 * k); bx1 = bx0 + tw + 34; by1 = cy + int(28 * k)
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=int(28 * k), fill=(12, 12, 12, 175))
    d.text((bx0 + 17, cy), label, font=f, fill=(255, 255, 255, 255), anchor="lm")

def pines_contorno(bg_path, out):
    img = Image.open(bg_path).convert("RGBA")
    W, H = img.size
    # poligono de ejemplo (mock, no medido)
    poly = [(250, 560), (850, 470), (900, 1010), (300, 1090)]
    fill = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(fill).polygon(poly, fill=YEL + (36,))
    img = Image.alpha_composite(img, fill)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    gd.line(poly + [poly[0]], fill=YEL + (255,), width=14, joint="curve")
    img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(10)))
    ln = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(ln)
    ld.line(poly + [poly[0]], fill=YEL + (255,), width=5, joint="curve")
    for (x, y) in poly:
        ld.ellipse([x - 11, y - 11, x + 11, y + 11], fill=(255, 255, 255, 255), outline=(16, 16, 16, 255), width=3)
    img = comp(img, ln, shadow=True)
    d = ImageDraw.Draw(img, "RGBA")
    pin(d, img, 880, 1300, "Carretera principal")
    pin(d, img, 380, 1500, "Casco urbano")
    # guias seguras
    g = cfg["plataformas"]["master_9x16"]["zona_segura_px"]
    d.rectangle([g["izquierda"], g["arriba"], W - g["derecha"], H - g["abajo"]], outline=(255, 0, 80, 150), width=2)
    img.convert("RGB").save(out)

if __name__ == "__main__":
    foto = P + r"\assets\nixon_recorte.png"
    cierre(SM + r"\bg_calle.png", foto, SM + r"\mock_cierre_9x16.png", (1080, 1920), "9x16")
    cierre(SM + r"\bg_calle.png", foto, SM + r"\mock_cierre_4x5.png", (1080, 1350), "4x5")
    pines_contorno(SM + r"\bg_cenital.png", SM + r"\mock_pines_contorno.png")
    print("OK")


def gradient(size, y0, y1, a0, a1):
    W, H = size
    a = np.zeros((H, W), np.float32)
    ys = np.arange(H)
    col = np.interp(ys, [y0, y1], [a0, a1], left=a0 if y0 < y1 else a1, right=a1 if y0 < y1 else a0)
    a[:] = col[:, None]
    L = Image.new("RGBA", size, (0, 0, 0, 0)); L.putalpha(Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)))
    return L

def cierre_v2(bg_path, foto, out, size):
    """Lotificacion protagonista al centro, sin placas; asesor pequeno a un lado; solo sombras."""
    W, H = size
    tall = H > 1500
    gz = cfg["plataformas"]["master_9x16" if tall else "post_4x5"]["zona_segura_px"]
    img = Image.open(bg_path).convert("RGBA")
    img = Image.alpha_composite(img, gradient(size, int(H * 0.55), H, 0.0, 0.68))   # sombra inferior para leer
    img = Image.alpha_composite(img, gradient(size, 0, int(H * 0.22), 0.45, 0.0))   # sombra superior para logo
    cx = W // 2
    # logo proyecto arriba
    si = Image.open(P + r"\assets\logo_si_horizontal.png").convert("RGBA")
    sw = 520 if tall else 460; si = si.resize((sw, int(si.height * sw / si.width)), Image.LANCZOS)
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); lay.paste(si, ((W - sw) // 2, gz["arriba"] + (20 if tall else 0)), si)
    img = comp(img, lay)
    # frase + telefono
    ybase = H - gz["abajo"]            # limite inferior seguro
    y_logo_base = ybase - 14
    y_tel = y_logo_base - 330 if tall else y_logo_base - 270
    fr = text_layer(size, (cx, y_tel - 150), cfg["cierre"]["frase"], F(SEGBL, 46 if tall else 40), (240, 232, 214, 255), "ms", 1)
    img = comp(img, fr)
    tel = text_layer(size, (cx, y_tel), cfg["cierre"]["telefono"]["texto"], F(IMPACT, 132 if tall else 112), YEL + (255,), "ms", 2)
    img = comp(img, tel)
    # fila inferior: asesor (izq, pequeno) | RE/MAX (centro) | firma (der)
    ph = Image.open(foto).convert("RGBA")
    crop = ph.crop((0, 0, ph.width, int(ph.height * 0.62)))           # busto
    phh = 300 if tall else 250
    crop = crop.resize((int(crop.width * phh / crop.height), phh), Image.LANCZOS)
    # desvanecer borde inferior
    m = np.array(crop.split()[3], np.float32); fade = np.clip((np.arange(phh)[:, None] - (phh - 60)) / 60.0, 0, 1)
    crop.putalpha(Image.fromarray((m * (1 - fade)).astype(np.uint8)))
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); lay.paste(crop, (gz["izquierda"] - 10, y_logo_base - phh + 0), crop)
    img = Image.alpha_composite(img, shadow_layer(lay, 18, 0, 0.6, (0, 8)))
    img = Image.alpha_composite(img, lay)
    rm = Image.open(cfg["logos"]["remax_abajo_centro"]["archivo"]).convert("RGBA")
    rw = 235; rm = rm.resize((rw, int(rm.height * rw / rm.width)), Image.LANCZOS)
    bi = Image.open(P + "/assets/logo_bi_blanco.png").convert("RGBA")
    bw = 120; bi = bi.resize((bw, int(bi.height * bw / bi.width)), Image.LANCZOS)
    lx = 350
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); lay.paste(rm, (lx, y_logo_base - 130), rm)
    lay.paste(bi, (lx + rw + 28, y_logo_base - 130 + rm.height - bi.height - 4), bi)
    img = comp(img, lay)
    sig = text_layer(size, (W - gz["derecha"] - 10, y_logo_base - 70), "Nixon", F(GEORI, 58 if tall else 50), (255, 255, 255, 255), "rs")
    sig2 = text_layer(size, (W - gz["derecha"] - 10, y_logo_base - 12), "Hernández", F(GEORI, 58 if tall else 50), (255, 255, 255, 255), "rs")
    img = comp(img, sig); img = comp(img, sig2)
    # leyendas (dentro de zona segura)
    d_y = y_logo_base + 10
    for t in (cfg["cierre"]["banco_asterisco"], cfg["cierre"]["disponibilidad"]):
        L = text_layer(size, (cx, d_y), t, F(SEGBL, 21), (255, 255, 255, 235), "ms", 1); img = comp(img, L, shadow=False); d_y += 25
    d = ImageDraw.Draw(img)
    d.rectangle([gz["izquierda"], gz["arriba"], W - gz["derecha"], H - gz["abajo"]], outline=(255, 0, 80, 150), width=2)
    img.convert("RGB").save(out)

if __name__ == "__main__":
    foto = P + r"\assets\nixon_recorte.png"
    cierre_v2(SM + r"\bg_lote_9x16.png", foto, SM + r"\mock_cierre_v2_9x16.png", (1080, 1920))
    cierre_v2(SM + r"\bg_lote_4x5.png", foto, SM + r"\mock_cierre_v2_4x5.png", (1080, 1350))
    print("v2 OK")


def cierre_v3(bg_path, foto, out, size):
    """v3: calles asfaltadas protagonistas; asesor a la derecha con nombre pequeno debajo;
    RE/MAX y Banco Industrial grandes a la izquierda; solo sombras (sin placas)."""
    W, H = size
    tall = H > 1500
    k = 1.0 if tall else 0.82
    gz = cfg["plataformas"]["master_9x16" if tall else "post_4x5"]["zona_segura_px"]
    img = Image.open(bg_path).convert("RGBA")
    img = Image.alpha_composite(img, gradient(size, int(H * 0.50), int(H * 0.80), 0.0, 0.62))
    img = Image.alpha_composite(img, gradient(size, 0, int(H * 0.20), 0.40, 0.0))
    cx = W // 2
    ybase = H - gz["abajo"]
    # logo proyecto
    si = Image.open(P + "/assets/logo_si_horizontal.png").convert("RGBA")
    sw = int(520 * k); si = si.resize((sw, int(si.height * sw / si.width)), Image.LANCZOS)
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); lay.paste(si, ((W - sw) // 2, gz["arriba"] + 20), si)
    img = comp(img, lay)
    # frase + telefono
    y_tel = ybase - int(345 * k)
    img = comp(img, text_layer(size, (cx, y_tel - int(150 * k)), cfg["cierre"]["frase"], F(SEGBL, int(46 * k)), (240, 232, 214, 255), "ms", 1))
    img = comp(img, text_layer(size, (cx, y_tel), cfg["cierre"]["telefono"]["texto"], F(IMPACT, int(132 * k)), YEL + (255,), "ms", 2))
    # izquierda: RE/MAX grande, Banco Industrial grande
    x0 = gz["izquierda"]
    rm = Image.open(cfg["logos"]["remax_abajo_centro"]["archivo"]).convert("RGBA")
    rw = int(380 * k); rm = rm.resize((rw, int(rm.height * rw / rm.width)), Image.LANCZOS)
    bi = Image.open(P + "/assets/logo_bi_blanco.png").convert("RGBA")
    bw = int(300 * k); bi = bi.resize((bw, int(bi.height * bw / bi.width)), Image.LANCZOS)
    ytop = ybase - int(345 * k)
    lay = Image.new("RGBA", size, (0, 0, 0, 0))
    lay.paste(rm, (x0, ytop), rm)
    lay.paste(bi, (x0 + 4, ytop + rm.height + int(26 * k)), bi)
    img = comp(img, lay)
    yl = ytop + rm.height + int(26 * k) + bi.height + int(34 * k)
    for t in ("*Financiamiento con Banco Industrial", "sujeto a evaluación del banco.", "Sujeto a disponibilidad."):
        img = comp(img, text_layer(size, (x0 + 4, yl), t, F(SEGBL, int(21 * k)), (255, 255, 255, 235), "ls", 1), shadow=False)
        yl += int(25 * k)
    # derecha: asesor + nombre pequeno debajo
    ph = Image.open(foto).convert("RGBA")
    crop = ph.crop((0, 0, ph.width, int(ph.height * 0.64)))
    phh = int(330 * k)
    crop = crop.resize((int(crop.width * phh / crop.height), phh), Image.LANCZOS)
    m = np.array(crop.split()[3], np.float32); fade = np.clip((np.arange(phh)[:, None] - (phh - 50)) / 50.0, 0, 1)
    crop.putalpha(Image.fromarray((m * (1 - fade)).astype(np.uint8)))
    px = W - gz["derecha"] - crop.width + 20; py = ybase - int(26 * k) - phh - int(10 * k) + 30
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); lay.paste(crop, (px, py), crop)
    img = Image.alpha_composite(img, shadow_layer(lay, 18, 0, 0.6, (0, 8)))
    img = Image.alpha_composite(img, lay)
    img = comp(img, text_layer(size, (px + crop.width // 2 - 20, ybase - 6), "Nixon Hernández", F(GEORI, int(40 * k)), (255, 255, 255, 255), "ms"))
    d = ImageDraw.Draw(img)
    d.rectangle([gz["izquierda"], gz["arriba"], W - gz["derecha"], H - gz["abajo"]], outline=(255, 0, 80, 150), width=2)
    img.convert("RGB").save(out)


if __name__ == "__main__":
    foto = P + "/assets/nixon_recorte.png"
    cierre_v3(SM + "/bgc_calles-desde-arriba_9x16.png", foto, SM + "/mock_cierre_v3_9x16.png", (1080, 1920))
    cierre_v3(SM + "/bgc_calles-desde-arriba_4x5.png", foto, SM + "/mock_cierre_v3_4x5.png", (1080, 1350))
    print("v3 OK")


def cierre_v4(bg_path, foto, out, size, guias=True):
    """v4: telefono arriba; RE/MAX debajo del telefono; Banco Industrial (mismo ancho) a la par del nombre.
    RE/MAX y BI comparten eje vertical y ancho para dar armonia. Asesor a la derecha."""
    W, H = size
    tall = H > 1500
    k = 1.0 if tall else 0.82
    gz = cfg["plataformas"]["master_9x16" if tall else "post_4x5"]["zona_segura_px"]
    img = Image.open(bg_path).convert("RGBA")
    img = Image.alpha_composite(img, gradient(size, int(H * 0.45), int(H * 0.80), 0.0, 0.62))
    img = Image.alpha_composite(img, gradient(size, 0, int(H * 0.20), 0.40, 0.0))
    cx = W // 2
    yb = H - gz["abajo"]
    off = lambda v: yb - int(v * k)
    si = Image.open(P + "/assets/logo_si_horizontal.png").convert("RGBA")
    sw = int(520 * k); si = si.resize((sw, int(si.height * sw / si.width)), Image.LANCZOS)
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); lay.paste(si, ((W - sw) // 2, gz["arriba"] + 20), si)
    img = comp(img, lay)
    img = comp(img, text_layer(size, (cx, off(700)), cfg["cierre"]["frase"], F(SEGBL, int(46 * k)), (240, 232, 214, 255), "ms", 1))
    img = comp(img, text_layer(size, (cx, off(560)), cfg["cierre"]["telefono"]["texto"], F(IMPACT, int(132 * k)), YEL + (255,), "ms", 2))
    # eje comun de logos
    AX = int(gz["izquierda"] + 190 * k + 10)
    lw = int(360 * k)
    rm = Image.open(cfg["logos"]["remax_abajo_centro"]["archivo"]).convert("RGBA")
    rm = rm.resize((lw, int(rm.height * lw / rm.width)), Image.LANCZOS)
    bi = Image.open(P + "/assets/logo_bi_blanco.png").convert("RGBA")
    bi = bi.resize((lw, int(bi.height * lw / bi.width)), Image.LANCZOS)
    lay = Image.new("RGBA", size, (0, 0, 0, 0))
    lay.paste(rm, (AX - lw // 2, off(530)), rm)
    by = yb - int(28 * k) - bi.height
    lay.paste(bi, (AX - lw // 2, by), bi)
    img = comp(img, lay)
    yl = by - int(70 * k)
    for t in ("*Financiamiento con Banco Industrial", "sujeto a evaluación del banco.", "Sujeto a disponibilidad."):
        img = comp(img, text_layer(size, (AX, yl), t, F(SEGBL, int(21 * k)), (255, 255, 255, 235), "ms", 1), shadow=False)
        yl += int(25 * k)
    ph = Image.open(foto).convert("RGBA")
    crop = ph.crop((0, 0, ph.width, int(ph.height * 0.64)))
    phh = int(330 * k)
    crop = crop.resize((int(crop.width * phh / crop.height), phh), Image.LANCZOS)
    m = np.array(crop.split()[3], np.float32); fade = np.clip((np.arange(phh)[:, None] - (phh - 50)) / 50.0, 0, 1)
    crop.putalpha(Image.fromarray((m * (1 - fade)).astype(np.uint8)))
    px = W - gz["derecha"] - crop.width + 20; py = yb - int(36 * k) - phh + 30
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); lay.paste(crop, (px, py), crop)
    img = Image.alpha_composite(img, shadow_layer(lay, 18, 0, 0.6, (0, 8)))
    img = Image.alpha_composite(img, lay)
    img = comp(img, text_layer(size, (px + crop.width // 2 - 20, yb - 6), "Nixon Hernández", F(GEORI, int(40 * k)), (255, 255, 255, 255), "ms"))
    if guias:
        d = ImageDraw.Draw(img)
        d.rectangle([gz["izquierda"], gz["arriba"], W - gz["derecha"], H - gz["abajo"]], outline=(255, 0, 80, 150), width=2)
    img.convert("RGB").save(out)




def cierre_v5(bg_path, foto, out, size, guias=True):
    """v5 (RE/MAX grande y centrado; BI a la par del nombre): telefono arriba; RE/MAX debajo del telefono; Banco Industrial (mismo ancho) a la par del nombre.
    RE/MAX y BI comparten eje vertical y ancho para dar armonia. Asesor a la derecha."""
    W, H = size
    tall = H > 1500
    k = 1.0 if tall else 0.82
    gz = cfg["plataformas"]["master_9x16" if tall else "post_4x5"]["zona_segura_px"]
    img = Image.open(bg_path).convert("RGBA")
    img = Image.alpha_composite(img, gradient(size, int(H * 0.45), int(H * 0.80), 0.0, 0.62))
    img = Image.alpha_composite(img, gradient(size, 0, int(H * 0.20), 0.40, 0.0))
    cx = W // 2
    yb = H - gz["abajo"]
    off = lambda v: yb - int(v * k)
    si = Image.open(P + "/assets/logo_si_horizontal.png").convert("RGBA")
    sw = int(520 * k); si = si.resize((sw, int(si.height * sw / si.width)), Image.LANCZOS)
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); lay.paste(si, ((W - sw) // 2, gz["arriba"] + 20), si)
    img = comp(img, lay)
    img = comp(img, text_layer(size, (cx, off(700)), cfg["cierre"]["frase"], F(SEGBL, int(46 * k)), (240, 232, 214, 255), "ms", 1))
    img = comp(img, text_layer(size, (cx, off(560)), cfg["cierre"]["telefono"]["texto"], F(IMPACT, int(132 * k)), YEL + (255,), "ms", 2))
    # eje comun de logos
    AX = int(gz["izquierda"] + 190 * k + 10)
    lw = int(360 * k)
    rm = Image.open(cfg["logos"]["remax_abajo_centro"]["archivo"]).convert("RGBA")
    rwd = int(560 * k); rm = rm.resize((rwd, int(rm.height * rwd / rm.width)), Image.LANCZOS)
    bi = Image.open(P + "/assets/logo_bi_blanco.png").convert("RGBA")
    bi = bi.resize((lw, int(bi.height * lw / bi.width)), Image.LANCZOS)
    lay = Image.new("RGBA", size, (0, 0, 0, 0))
    lay.paste(rm, ((W - rwd) // 2 - 20, off(540)), rm)
    by = yb - int(28 * k) - bi.height
    lay.paste(bi, (AX - lw // 2, by), bi)
    img = comp(img, lay)
    yl = by - int(70 * k)
    for t in ("*Financiamiento con Banco Industrial", "sujeto a evaluación del banco.", "Sujeto a disponibilidad."):
        img = comp(img, text_layer(size, (AX, yl), t, F(SEGBL, int(21 * k)), (255, 255, 255, 235), "ms", 1), shadow=False)
        yl += int(25 * k)
    ph = Image.open(foto).convert("RGBA")
    crop = ph.crop((0, 0, ph.width, int(ph.height * 0.64)))
    phh = int(330 * k)
    crop = crop.resize((int(crop.width * phh / crop.height), phh), Image.LANCZOS)
    m = np.array(crop.split()[3], np.float32); fade = np.clip((np.arange(phh)[:, None] - (phh - 50)) / 50.0, 0, 1)
    crop.putalpha(Image.fromarray((m * (1 - fade)).astype(np.uint8)))
    px = W - gz["derecha"] - crop.width + 20; py = yb - int(36 * k) - phh + 30
    lay = Image.new("RGBA", size, (0, 0, 0, 0)); lay.paste(crop, (px, py), crop)
    img = Image.alpha_composite(img, shadow_layer(lay, 18, 0, 0.6, (0, 8)))
    img = Image.alpha_composite(img, lay)
    img = comp(img, text_layer(size, (px + crop.width // 2 - 20, yb - 6), "Nixon Hernández", F(GEORI, int(40 * k)), (255, 255, 255, 255), "ms"))
    if guias:
        d = ImageDraw.Draw(img)
        d.rectangle([gz["izquierda"], gz["arriba"], W - gz["derecha"], H - gz["abajo"]], outline=(255, 0, 80, 150), width=2)
    img.convert("RGB").save(out)




if __name__ == "__main__":
    foto = P + "/assets/nixon_recorte.png"
    cierre_v4(SM + "/bgc_calles-desde-arriba_9x16.png", foto, SM + "/mock_cierre_v4_9x16.png", (1080, 1920))
    cierre_v4(SM + "/bgc_calles-desde-arriba_4x5.png", foto, SM + "/mock_cierre_v4_4x5.png", (1080, 1350))
    print("v4 OK")

    cierre_v5(SM + "/bgc_calles-desde-arriba_9x16.png", foto, SM + "/mock_cierre_v5_9x16.png", (1080, 1920))
    cierre_v5(SM + "/bgc_calles-desde-arriba_4x5.png", foto, SM + "/mock_cierre_v5_4x5.png", (1080, 1350))
