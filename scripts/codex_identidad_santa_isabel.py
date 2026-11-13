"""Extiende las plantillas del kit existente con la paleta azul/amarillo.
Conserva la silueta y transparencia de las piezas del logo, sin retocar fotografías.
"""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np
from codex_artes_15d import sha, REPO

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project',type=Path,required=True)
    ap.add_argument('--photos',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args()
    a.output.mkdir(parents=True,exist_ok=False)
    palette=json.loads((REPO/'brands/santa-isabel/palette.json').read_text(encoding='utf8'))
    def rgb(key): return tuple(bytes.fromhex(palette['colors'][key][1:]))
    inputs=[]
    for layout in ['horizontal','vertical','icono']:
        path=a.project/f'assets/logo_si_{layout}.png'
        inputs.append({'path':str(path),'sha256':sha(path)})
        src=Image.open(path).convert('RGBA')
        arr=np.asarray(src); h,w=arr.shape[:2]; yy,xx=np.indices((h,w))
        if layout=='horizontal': accent=(xx<500)|(yy<80)|((xx>=570)&(xx<720)&(yy>=325)&(yy<360))
        elif layout=='vertical': accent=(yy<380)|((yy>=645)&(yy<670))
        else: accent=np.ones((h,w),dtype=bool)
        for variant in ['claro','oscuro']:
            out=np.zeros_like(arr); out[:,:,:3]=rgb('white' if variant=='claro' else 'navy')
            out[accent,:3]=rgb('yellow' if variant=='claro' else 'blue')
            out[:,:,3]=arr[:,:,3]
            im=Image.fromarray(out); im.save(a.output/f'logo_si_{layout}_{variant}.png')
            assert np.array_equal(np.asarray(im)[:,:,3],arr[:,:,3])
    # Profile uses the existing wordmark cropped into its named elements.
    horiz=Image.open(a.output/'logo_si_horizontal_claro.png').convert('RGBA')
    avatar=Image.new('RGBA',(1080,1080),rgb('navy')+(255,))
    draw=ImageDraw.Draw(avatar)
    draw.ellipse((58,58,1022,1022),outline=rgb('blue'),width=3)
    icon=Image.open(a.output/'logo_si_icono_claro.png').convert('RGBA'); icon=ImageOps.contain(icon,(225,210),Image.Resampling.LANCZOS)
    avatar.alpha_composite(icon,((1080-icon.width)//2,185))
    # Compose approved word shapes, preserving their alpha and letterforms.
    parts=[(horiz.crop((575,0,1190,65)),(510,65),425),
           (horiz.crop((570,105,1192,292)),(585,175),530),
           (horiz.crop((1220,105,1896,292)),(585,162),710),
           (horiz.crop((750,300,1330,375)),(385,50),905)]
    for p,size,y in parts:
        p=ImageOps.contain(p,size,Image.Resampling.LANCZOS); avatar.alpha_composite(p,((1080-p.width)//2,y))
    avatar.convert('RGB').save(a.output/'perfil_santa_isabel_azul.jpg',quality=97,subsampling=0)
    # Cover: real project photograph, navy overlay, content inside centered crop.
    source=a.photos/'SI_FOTO_calles-desde-arriba_v01.jpg'
    inputs.append({'path':str(source),'sha256':sha(source)})
    cover=ImageOps.fit(Image.open(source).convert('RGBA'),(1640,720),centering=(.5,.5))
    alpha=np.broadcast_to(np.linspace(236,55,1640).astype(np.uint8),(720,1640)).copy()
    overlay=Image.new('RGBA',cover.size,rgb('navy')+(0,)); overlay.putalpha(Image.fromarray(alpha));cover=Image.alpha_composite(cover,overlay)
    logo=ImageOps.contain(horiz,(660,145),Image.Resampling.LANCZOS);cover.alpha_composite(logo,(350,55))
    d=ImageDraw.Draw(cover)
    def font(name,size):return ImageFont.truetype(str(Path('C:/Windows/Fonts')/name),size)
    d.text((350,225),'Un espacio',font=font('georgiab.ttf',76),fill=rgb('white'))
    d.text((350,310),'para sus planes.',font=font('georgiab.ttf',76),fill=rgb('white'))
    d.rounded_rectangle((350,427,1110,432),radius=2,fill=rgb('yellow'))
    d.text((350,460),'COMACARÁN, SAN MIGUEL',font=font('segoeuib.ttf',26),fill=rgb('white'))
    d.text((350,520),'Escríbanos para agendar su visita',font=font('segoeui.ttf',30),fill=rgb('white'))
    d.text((350,566),'+503 7956 4399',font=font('segoeuib.ttf',44),fill=rgb('yellow'))
    cover.convert('RGB').save(a.output/'portada_facebook_azul.jpg',quality=97,subsampling=0)
    (a.output/'palette.json').write_text(json.dumps(palette,ensure_ascii=False,indent=2),encoding='utf8')
    manifest={'agent':'codex','palette':palette['version'],'source_alpha_preserved':True,'inputs':inputs,'outputs':[{'file':p.name,'sha256':sha(p)} for p in a.output.glob('*.png')]+[{'file':p.name,'sha256':sha(p)} for p in a.output.glob('*.jpg')]}
    assert all(sha(Path(i['path']))==i['sha256'] for i in inputs)
    (a.output/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({'output':str(a.output),'files':len(manifest['outputs'])}))

if __name__=='__main__': main()
