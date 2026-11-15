"""Amplía el kit local de Santa Isabel: artes, collages, carruseles y copys.
Las fotografías y los logos existentes se leen sin modificarlos.
"""
import argparse
from datetime import date, datetime, timedelta, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import zipfile

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

REPO = Path(__file__).resolve().parents[1]
FONT = Path("C:/Windows/Fonts")
WHITE = (255, 255, 255)
NAVY = (27, 42, 74)
FORMATS = {"4x5": (1080, 1350), "9x16": (1080, 1920)}


def sha(path):
    with open(path, "rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def parse_agent_calendar(path):
    """Extrae fecha inicial y copys aprobados sin reescribir el calendario."""
    source = path.read_text(encoding="utf8")
    period = re.search(r"\*\*Periodo:\*\*\s*(\d{2}/\d{2}/\d{4})\s+al\s+(\d{2}/\d{2}/\d{4})", source)
    if not period:
        raise ValueError(f"Calendario sin periodo válido: {path}")
    start_date = datetime.strptime(period.group(1), "%d/%m/%Y").date()
    end_date = datetime.strptime(period.group(2), "%d/%m/%Y").date()
    if end_date - start_date != timedelta(days=14):
        raise ValueError(f"El calendario no cubre 15 días: {path}")

    copies = {}
    sections = re.finditer(r"^## Día (\d+)\b(?P<body>.*?)(?=^## Día \d+\b|\Z)", source, re.MULTILINE | re.DOTALL)
    marker = "**Texto de la publicación (copiar y pegar):**"
    for section in sections:
        day = int(section.group(1))
        body = section.group("body")
        if marker not in body:
            raise ValueError(f"Día {day} sin texto de publicación en {path}")
        lines = body.split(marker, 1)[1].splitlines()
        quote, started = [], False
        for line in lines:
            if line.startswith(">"):
                started = True
                quote.append(line[1:].lstrip())
            elif started and not line.strip():
                quote.append("")
            elif started:
                break
        while quote and not quote[-1]:
            quote.pop()
        copies[day] = "\n".join(quote)
    if set(copies) != set(range(1, 16)):
        raise ValueError(f"El calendario debe contener copys para los días 1 al 15: {path}")
    return start_date, copies


def load_agent(agent_dir):
    agent_dir = agent_dir.resolve()
    records_path = agent_dir.parent / "agentes.json"
    records = json.loads(records_path.read_text(encoding="utf8"))
    matches = [record for record in records if record.get("id") == agent_dir.name]
    if len(matches) != 1:
        raise ValueError(f"No existe un registro único para {agent_dir.name}")
    record = matches[0]
    required = ("id", "nombre", "telefono", "wa")
    if any(not record.get(field) for field in required):
        raise ValueError(f"Registro incompleto para {agent_dir.name}")
    portrait = agent_dir / "foto_recorte.png"
    original = agent_dir / "foto_original.jpeg"
    calendar_path = agent_dir / f"calendario_{record['id']}.md"
    for path in (portrait, original, calendar_path):
        if not path.is_file():
            raise ValueError(f"Falta entrada del agente: {path}")
    start_date, copies = parse_agent_calendar(calendar_path)
    signature = f"{record['nombre']} · RE/MAX Eleva · WhatsApp {record['telefono']}"
    whatsapp = f"https://wa.me/{record['wa']}"
    for day, copy in copies.items():
        if signature not in copy or whatsapp not in copy:
            raise ValueError(f"El copy del día {day} no coincide con agentes.json")
    return {
        **record,
        "directory": agent_dir,
        "records_path": records_path,
        "portrait_path": portrait,
        "original_path": original,
        "calendar_path": calendar_path,
        "start_date": start_date,
        "copies": copies,
    }


def split_display_name(name):
    words = name.upper().split()
    if len(words) < 2:
        return words
    splits = [(words[:index], words[index:]) for index in range(1, len(words))]
    first, second = min(splits, key=lambda pair: abs(len(" ".join(pair[0])) - len(" ".join(pair[1]))))
    return [" ".join(first), " ".join(second)]


class Artist:
    def __init__(self, source, project, kit_path, brand_assets=None, agent=None):
        self.source, self.project = source, project
        self.kit = json.loads(kit_path.read_text(encoding="utf8"))
        self.palette = json.loads((REPO/"brands/santa-isabel/palette.json").read_text(encoding="utf8"))
        self.yellow = self.palette["colors"]["yellow"]
        self.cream = self.palette["colors"]["white"]
        self.brand_assets = brand_assets
        self.agent = agent
        self.used = {}
        self.bounds = []
        self.fonts = {"impact": "impact.ttf", "serif": "georgiai.ttf", "body": "segoeui.ttf", "bold": "seguibl.ttf"}

    def font(self, name, size):
        return ImageFont.truetype(str(FONT / self.fonts[name]), int(size))

    def asset(self, path):
        path = Path(path)
        if path not in self.used:
            self.used[path] = sha(path)
        return Image.open(path).convert("RGBA")

    def photo(self, stem, size, anchor=(0.5, 0.5)):
        if stem == "calles-internas":
            raise ValueError("Foto descartada por Nixon")
        return ImageOps.fit(self.asset(self.source / f"SI_FOTO_{stem}_v01.jpg"), size,
                            Image.Resampling.LANCZOS, centering=anchor)

    def tint(self, image, stops):
        width, height = image.size
        a = np.interp(np.arange(height), [x[0] for x in stops], [x[1] for x in stops]).astype(np.uint8)
        overlay = Image.new("RGBA", image.size, NAVY + (0,))
        overlay.putalpha(Image.fromarray(np.broadcast_to(a[:, None], (height, width)).copy()))
        return Image.alpha_composite(image, overlay)

    def text(self, image, text, x, y, size, font="body", color=WHITE, max_width=960,
             anchor="mt", shadow=True, min_size=20):
        draw = ImageDraw.Draw(image)
        while size >= min_size:
            f = self.font(font, size)
            box = draw.textbbox((x, y), text, font=f, anchor=anchor, stroke_width=0)
            if box[2]-box[0] <= max_width:
                break
            size -= 1
        if size < min_size:
            raise ValueError(f"Texto demasiado largo: {text}")
        if box[0] < self.safe_left or box[2] > self.safe_right or box[1] < self.safe_top or box[3] > self.safe_bottom:
            raise ValueError(f"Texto fuera de zona segura: {text} {box}")
        self.bounds.append({"type":"text","text":text,"bbox":box,"font_px":size})
        if shadow:
            layer = Image.new("RGBA", image.size)
            ImageDraw.Draw(layer).text((x+1, y+4), text, font=f, anchor=anchor, fill=(0,0,0,220), stroke_width=2)
            image.alpha_composite(layer.filter(ImageFilter.GaussianBlur(5)))
        draw = ImageDraw.Draw(image)
        draw.text((x,y), text, font=f, anchor=anchor, fill=color,
                  stroke_width=1 if font=="impact" else 0, stroke_fill=(0,0,0,150))
        return box

    def logo(self, image, path, x, y, width):
        asset = self.asset(path)
        asset = asset.crop(asset.getbbox())
        asset = asset.resize((width, round(width * asset.height / asset.width)), Image.Resampling.LANCZOS)
        if x < self.safe_left or x + asset.width > self.safe_right or y < self.safe_top or y + asset.height > self.safe_bottom:
            raise ValueError(f"Logo fuera de zona segura: {path}")
        self.bounds.append({"type":"logo","text":Path(path).name,"bbox":(x,y,x+asset.width,y+asset.height)})
        shadow = Image.new("RGBA", asset.size, (0,0,0,0))
        shadow.putalpha(asset.getchannel("A"))
        image.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(3)), (x,y+3))
        image.alpha_composite(asset, (x,y))

    def photo_grid(self, image, photos, box, duo=False):
        x,y,w,h = box
        gap = 10
        if duo:
            slots = [(x,y,(w-gap)//2,h), (x+(w+gap)//2,y,(w-gap)//2,h)]
        else:
            large = round(w*0.59)
            slots = [(x,y,large,h), (x+large+gap,y,w-large-gap,(h-gap)//2),
                     (x+large+gap,y+(h+gap)//2,w-large-gap,(h-gap)//2)]
        for photo, (xx,yy,ww,hh) in zip(photos, slots):
            tile = self.photo(photo, (ww,hh), (0.54,0.5))
            # Narrow borders separate actual photographs without changing their contents.
            ImageDraw.Draw(image).rectangle((xx-2,yy-2,xx+ww+2,yy+hh+2), fill=self.cream)
            image.alpha_composite(tile,(xx,yy))

    def footer(self, image, tall, advisor=False):
        phone = self.agent["telefono"] if self.agent else self.kit["cierre"]["telefono"]["texto"]
        name = self.agent["nombre"] if self.agent else "Nixon Hernández"
        cta_y, phone_y = (1260,1314) if tall else (860,910)
        self.text(image,self.kit["cierre"]["frase"],540,cta_y,39 if tall else 36,font="bold")
        self.text(image,phone,540,phone_y,101 if tall else 88,font="impact",color=self.yellow)
        logo_y = 1408 if tall else 1018
        self.logo(image,self.kit["logos"]["remax_abajo_centro"]["archivo"],70,logo_y,310)
        self.logo(image,self.project/"assets/logo_bi_blanco.png",425,logo_y+5,220)
        self.text(image,name,825,logo_y+18,29,font="serif",max_width=290)
        self.text(image,"Asesor RE/MAX",825,logo_y+58,22,max_width=270)
        legal_y = 1515 if tall else 1134
        self.text(image,"*Financiamiento con Banco Industrial sujeto a evaluación del banco.",540,legal_y,23,max_width=950,shadow=False)
        self.text(image,"Sujeto a disponibilidad.",540,legal_y+29,23,shadow=False)

    def make(self, post, fmt):
        size = FORMATS[fmt]
        tall = fmt=="9x16"
        limits = self.kit["plataformas"]["master_9x16" if tall else "post_4x5"]["zona_segura_px"]
        self.safe_top, self.safe_bottom = limits["arriba"], size[1]-limits["abajo"]
        self.safe_left, self.safe_right = limits["izquierda"], size[0]-limits["derecha"]
        self.bounds = []
        if self.agent and post.get("layout") == "advisor":
            post = dict(post)
            post["title"] = split_display_name(self.agent["nombre"])
        anchor = (0.58,0.5) if post["photos"][0]=="calles-desde-arriba" else (0.78,0.5)
        image = self.photo(post["photos"][0], size, anchor)
        if tall:
            stops=[(0,205),(400,180),(800,25),(1180,65),(1250,205),(1530,250),(1920,240)]
        else:
            stops=[(0,205),(300,185),(540,65),(800,60),(855,205),(1125,250),(1350,240)]
        image=self.tint(image,stops)
        compact = not tall and post.get("layout")=="collage"
        self.logo(image,(self.brand_assets/"logo_si_horizontal_claro.png") if self.brand_assets else self.project/"assets/logo_si_horizontal.png",310 if compact else 270,270 if tall else 135,460 if compact else 540)
        self.text(image,"Comacarán, San Miguel",540,405 if tall else (255 if compact else 270),29,font="body",color=self.cream)
        self.text(image,post["kicker"],540,465 if tall else (300 if compact else 322),44 if tall else 38,font="serif",color=self.cream)
        lines = post["title"]
        top = 530 if tall else (350 if compact else 380)
        max_size = (143 if tall else (112 if compact else 135)) if len(lines)==1 else (108 if tall else 80)
        heights = (130 if tall else 86) if len(lines)>1 else 0
        for i,line in enumerate(lines):
            color = self.yellow if any(s in line for s in ("US$","v²","VISITA")) else WHITE
            self.text(image,line,540,top+i*heights,max_size,font="impact",color=color,min_size=55)
        support_y = (810 if tall else 570) if len(lines)>1 else (755 if tall else (482 if compact else 535))
        self.text(image,post["support"],540,support_y,33 if tall else 29,font="bold",color=self.cream)
        layout=post.get("layout","hero")
        if layout in ("collage","duo"):
            grid_y = (880 if tall else 622) if len(lines)>1 else (840 if tall else 588)
            grid_h = (320 if tall else 186) if len(lines)>1 else (360 if tall else 220)
            if compact:
                grid_y,grid_h=534,274
            self.photo_grid(image,post["photos"],(64,grid_y,952,grid_h),duo=layout=="duo")
        if layout=="advisor":
            portrait_path = self.agent["portrait_path"] if self.agent else self.project/"assets/nixon_recorte.png"
            portrait=self.asset(portrait_path)
            portrait=portrait.crop(portrait.getbbox()) if self.agent else portrait.crop((100,173,960,1220))
            ph=350 if tall else 225
            portrait=portrait.resize((round(portrait.width*ph/portrait.height),ph),Image.Resampling.LANCZOS)
            alpha=np.asarray(portrait.getchannel("A"),dtype=np.float32)
            fade=np.minimum(1,(ph-1-np.arange(ph))/30)[:,None]
            portrait.putalpha(Image.fromarray((alpha*fade).astype(np.uint8)))
            px,py=(1080-portrait.width)//2,870 if tall else 605
            portrait_box=(px,py,px+portrait.width,py+ph)
            if px < self.safe_left or px + portrait.width > self.safe_right or py < self.safe_top or py + ph > self.safe_bottom:
                raise ValueError(f"Retrato fuera de zona segura: {portrait_box}")
            self.bounds.append({"type":"portrait","text":self.agent["nombre"] if self.agent else "Nixon","bbox":portrait_box})
            image.alpha_composite(portrait,(px,py))
        self.footer(image,tall)
        for i,a in enumerate(self.bounds):
            for b in self.bounds[i+1:]:
                x0,y0,x1,y1=a["bbox"]; u0,v0,u1,v1=b["bbox"]
                if min(x1,u1)>max(x0,u0) and min(y1,v1)>max(y0,v0):
                    raise ValueError(f"Elementos superpuestos: {a['text']} / {b['text']}")
        return image.convert("RGB"), list(self.bounds)


def write_json(path, data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf8")


def caption(post, kit, approved_copy=None):
    if approved_copy is not None:
        return approved_copy
    tags="#SantaIsabel #Comacaran #SanMiguel #ElSalvador #Terrenos #VentaDeTerrenos #Lotes #BienesRaices #NixonHernandez #REMAX"
    return (post["copy"]+"\n\n• Terrenos desde US$24,500\n• Desde 286 v²\n• Con escritura\n• Agua conectada\n\n"
            +kit["cierre"]["frase"]+".\n+503 7956 4399\nhttps://wa.me/50379564399\n\n"
            +kit["cierre"]["banco_asterisco"]+"\nSujeto a disponibilidad.\n\n"+tags)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--photos",type=Path,required=True)
    ap.add_argument("--project",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--brand-assets",type=Path,help="Carpeta del kit azul/amarillo generado por codex_identidad_santa_isabel.py")
    ap.add_argument("--agente",type=Path,help="Carpeta del agente; lee agentes.json, foto_recorte.png y calendario_<id>.md")
    ap.add_argument("--pilot",action="store_true")
    args=ap.parse_args()
    if args.output.exists():
        raise ValueError("Elija una carpeta nueva para conservar las versiones anteriores")
    plan_path=REPO/"brands/nixon-remax/codex_campana_15_dias.json"
    kit_path=REPO/"brands/nixon-remax/motion_kit/kit_nixon_remax.json"
    plan=json.loads(plan_path.read_text(encoding="utf8"))
    snapshot_path=REPO/"brands/santa-isabel/contenido_v03/property_snapshot.json"
    snapshot=json.loads(snapshot_path.read_text(encoding="utf8"))
    project_snapshot=json.loads((args.project/"property_snapshot.json").read_text(encoding="utf8"))
    if project_snapshot["public_facts"] != snapshot["public_facts"]:
        raise ValueError("El snapshot del proyecto no coincide con la fuente canónica de Santa Isabel")
    facts=snapshot["public_facts"]
    assert snapshot["status"].startswith("VERIFIED")
    assert (facts["price_from_usd"],facts["min_lot_size_varas2"],facts["water_connected"],facts["with_deed"])==(24500,286,True,True)
    agent=load_agent(args.agente) if args.agente else None
    if not agent:
        assert snapshot["contact"]=="+503 7956 4399"
    artist=Artist(args.photos,args.project,kit_path,args.brand_assets,agent)
    artist.used[snapshot_path] = sha(snapshot_path)
    if agent:
        for path in (agent["records_path"], agent["original_path"], agent["calendar_path"]):
            artist.used[path] = sha(path)
    args.output.mkdir(parents=True)
    folders=["feed_4x5","historias_9x16","copys","revision"]
    if not agent:
        folders.append("pauta_inicial")
    for folder in folders:
        (args.output/folder).mkdir()
    posts=plan["posts"][:1] if args.pilot else plan["posts"]
    exports=[]
    calendar=[]
    for post in posts:
        day=post["day"]
        campaign_start = agent["start_date"] if agent else date.fromisoformat(plan["start_date"])
        dt=campaign_start+timedelta(days=day-1)
        prefix=(f"{agent['id']}_" if agent else "")+f"D{day:02d}_{post['id']}"
        text=caption(post,artist.kit,agent["copies"][day] if agent else None)
        (args.output/"copys"/f"{prefix}.md").write_text(f"# {dt.isoformat()} · {post['angle']}\n\n## Instagram\n\n{text}\n\n## Facebook\n\n{text}\n",encoding="utf8")
        calendar.append({"day":day,"date":dt.isoformat(),"id":prefix,"angle":post["angle"],"caption":text,"carousel":len(post.get("slides",[]))+1})
        pages=[post]+[dict(slide,layout="hero",id=post["id"]) for slide in post.get("slides",[])]
        for index,page in enumerate(pages,1):
            for fmt in (FORMATS if index==1 else ["4x5"]):
                img,bounds=artist.make(page,fmt)
                folder="feed_4x5" if fmt=="4x5" else "historias_9x16"
                name=f"{prefix}_{index:02d}_{fmt}.jpg"
                relative=f"{folder}/{name}"
                img.save(args.output/relative,quality=96,subsampling=0)
                thumb=ImageOps.contain(img,(320,420))
                thumb.save(args.output/"revision"/name,quality=85)
                exports.append({"day":day,"file":relative,"format":fmt,"page":index,"bounds":bounds,"sha256":sha(args.output/relative)})
                if day==1 and not agent:
                    shutil.copy2(args.output/relative,args.output/"pauta_inicial"/f"A_precio_{fmt}.jpg")
                print("OK",relative,flush=True)
    for variant in ([] if agent else plan["paid_variants"]):
        for fmt in FORMATS:
            img,bounds=artist.make(variant,fmt)
            relative=f"pauta_inicial/{variant['id']}_{fmt}.jpg"
            img.save(args.output/relative,quality=96,subsampling=0)
            ImageOps.contain(img,(320,420)).save(args.output/"revision"/Path(relative).name,quality=85)
            exports.append({"day":1,"file":relative,"format":fmt,"page":1,"bounds":bounds,"sha256":sha(args.output/relative)})
            print("OK",relative,flush=True)
    write_json(args.output/"plan_editable.json",plan)
    write_json(args.output/"calendario.json",calendar)
    public_contact = agent["telefono"] if agent else snapshot["contact"]
    write_json(args.output/"ficha_publica.json",{"source":snapshot["source"],"public_facts":facts,"contact":public_contact})
    manifest={"creado_por":"codex / NBS publicabot CHATGPT","agente_id":agent["id"] if agent else None,
              "agente_nombre":agent["nombre"] if agent else "Nixon Hernández","agente_telefono":public_contact,
              "fecha_hora":datetime.now(timezone(timedelta(hours=-6))).isoformat(),
              "palette":artist.palette,"brand_assets":str(args.brand_assets) if args.brand_assets else None,
              "script":"scripts/codex_artes_15d.py","estado":"borrador","inputs":[{"path":str(x),"sha256":artist.used[x]} for x in sorted(artist.used)],
              "design_read":{"kind":"campaña inmobiliaria personalizada","energy":3,"rhythm":3,"motion":1},
              "design_decisions":{
                  "color":"Navy dominante y amarillo como foco, según la paleta confirmada de Santa Isabel.",
                  "layout":"Se conservan las composiciones aprobadas para que solo cambie la identidad del agente.",
                  "typography":"Se conserva la combinación serif y sans del kit para mantener continuidad editorial.",
                  "spacing":"Las zonas seguras separan contenido y controles de las interfaces de Meta.",
                  "imagery":"Solo se usan fotos reales aprobadas y el recorte entregado por el agente."
              },
              "safe_zones_px":{"4x5":{"top":120,"bottom":160},"9x16":{"top":250,"bottom":350}},
              "outputs":exports,"publish_authorized":False,"drive_upload_authorized":False,"ad_spend_authorized":False}
    write_json(args.output/"manifest.json",manifest)
    unchanged=all(sha(path)==digest for path,digest in artist.used.items())
    assert unchanged, "Un archivo de entrada cambió durante la producción"
    assert all(Image.open(args.output/e["file"]).size==FORMATS[e["format"]] for e in exports)
    expected = 37 if agent and not args.pilot else len(exports)
    assert len(exports) == expected, f"Cantidad inesperada de diseños: {len(exports)} != {expected}"
    write_json(args.output/"qa_report.json",{"status":"DRAFT_FOR_USER_REVIEW","facts_match_snapshot":True,
              "contact_matches_agent":bool(agent),"dimensions_verified":True,"source_unchanged":unchanged,
              "safe_text_bounds_verified":True,"elements_no_overlap_verified":True,"visual_review":"PENDING",
              "publication_approved":False,"drive_upload_approved":False,"designs":len(exports)})
    period_text=f"{campaign_start.strftime('%d/%m/%Y')} al {(campaign_start+timedelta(days=14)).strftime('%d/%m/%Y')}"
    owner_text=agent["nombre"] if agent else "Nixon Hernández"
    paid_line="" if agent else "- La carpeta de pauta contiene tres alternativas; no son campañas activadas.\n"
    (args.output/"LEEME.md").write_text(f"# Santa Isabel · artes de 15 días · {owner_text}\n\nPaquete local del {period_text}. Fechas solo en el calendario.\n\n- Feed: JPG de 1080×1350. Historias: JPG de 1080×1920.\n- Carruseles: mantener el orden 01, 02, 03, 04 de cada día.\n{paid_line}- Copys para Instagram y Facebook en la carpeta copys.\n- Las fotos provienen de la carpeta de fotos limpias indicada por Nixon. Se conservan sus ediciones previas.\n- Los datos corresponden al snapshot verificado por el usuario el 12 de noviembre. Revalidar precio y disponibilidad antes de publicar cada pieza.\n- No se agregó voz, imagen sintética ni servicios no verificados.\n- Editable: plan_editable.json + script del repositorio; fuentes, colores y logos del kit.\n\nEstado: borradores pendientes de selección y aprobación de Nixon. No hay publicación, carga a Drive ni gasto activados.\n",encoding="utf8")
    create_readme_html(args.output)
    create_gallery(args.output,calendar,exports,agent)
    create_sheets(args.output,exports)
    if not args.pilot and not agent:
        files=list(args.output.rglob("*"))
        with zipfile.ZipFile(args.output/"SANTA_ISABEL_15_DIAS.zip","w",zipfile.ZIP_DEFLATED) as archive:
            for file in files:
                if file.is_file():
                    archive.write(file,file.relative_to(args.output))
    print("DONE",len(exports),args.output,flush=True)


def create_sheets(out,exports):
    for fmt in FORMATS:
        items=[e for e in exports if e["format"]==fmt]
        tw,th=(216,270) if fmt=="4x5" else (180,320)
        cols=5
        sheet=Image.new("RGB",(cols*(tw+14)+14,((len(items)+cols-1)//cols)*(th+42)+14),NAVY)
        draw=ImageDraw.Draw(sheet)
        font=ImageFont.truetype(str(FONT/"segoeui.ttf"),14)
        for i,item in enumerate(items):
            x=14+(i%cols)*(tw+14); y=14+(i//cols)*(th+42)
            image=Image.open(out/item["file"])
            sheet.paste(image.resize((tw,th),Image.Resampling.LANCZOS),(x,y))
            draw.text((x,y+th+5),Path(item["file"]).stem[:27],font=font,fill=WHITE)
        sheet.save(out/f"revision/hoja_{fmt}.jpg",quality=92)


def create_readme_html(out):
    content=html.escape((out/"LEEME.md").read_text(encoding="utf8"))
    page='<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Instrucciones · Santa Isabel</title><style>body{margin:0;background:#101927;color:#fff;font:17px/1.65 system-ui}main{max-width:840px;margin:auto;padding:40px 24px}pre{white-space:pre-wrap;font:inherit}a{color:#ecd628}a:focus{outline:3px solid #ecd628;outline-offset:3px}</style><main><p><a href="index.html">Volver a la galería</a></p><pre>'+content+'</pre></main></html>'
    (out/"LEEME.html").write_text(page,encoding="utf8")


def create_gallery(out,calendar,exports,agent=None):
    chunks=[]
    for item in calendar:
        elements=[e for e in exports if e["day"]==item["day"] and not e["file"].startswith("pauta")]
        photos="".join(f'<a href="{e["file"]}" target="_blank"><img loading="lazy" src="revision/{Path(e["file"]).name}" alt="{html.escape(item["angle"])}"><span>{e["format"]} · {e["page"]}</span></a>' for e in elements)
        chunks.append(f'<section><h2>Día {item["day"]} · {item["date"]} · {html.escape(item["angle"])}</h2><div class="images">{photos}</div><details><summary>Copy para Instagram / Facebook</summary><pre>{html.escape(item["caption"])}</pre></details></section>')
    paid="".join(f'<a href="pauta_inicial/{p.name}" target="_blank"><img src="pauta_inicial/{p.name}" alt="Alternativa de pauta"><span>{p.stem}</span></a>' for p in sorted((out/"pauta_inicial").glob("*.jpg"))) if not agent else ""
    owner=html.escape(agent["nombre"] if agent else "Nixon Hernández")
    paid_section='' if agent else '<section><h2>Pauta inicial · tres alternativas</h2><div class="images">'+paid+'</div></section>'
    zip_link='' if agent else '<a href="SANTA_ISABEL_15_DIAS.zip">Descargar paquete completo</a> · '
    page='<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NBS publicabot CHATGPT · Santa Isabel</title><style>body{margin:0;background:#101927;color:#fff;font:16px system-ui}header,main{max-width:1280px;margin:auto;padding:24px}h1{font-size:38px}p{line-height:1.6;color:#dedee3}section{padding:24px 0;border-top:1px solid #445066}h2{font-size:20px}a{color:#ecd628;text-decoration:none}a:focus,summary:focus{outline:3px solid #ecd628;outline-offset:3px}img{width:100%;max-height:380px;object-fit:contain;background:#182742}span{display:block;font-size:13px;padding:8px}.images{display:flex;gap:14px;overflow:auto}.images a{flex:0 0 220px}pre{white-space:pre-wrap;font:16px system-ui;line-height:1.6}summary{cursor:pointer;margin-top:16px}.tag{color:#ecd628}</style><header><p class="tag">NBS PUBLICABOT CHATGPT</p><h1>Santa Isabel · 15 días · '+owner+'</h1><p>Collages, carruseles y artes individuales. Borradores para revisión. Abra cada imagen para verla completa.</p><p>'+zip_link+'<a href="LEEME.html">Instrucciones</a></p></header><main>'+paid_section+''.join(chunks)+'</main></html>'
    (out/"index.html").write_text(page,encoding="utf8")


if __name__=="__main__":
    main()
