# -*- coding: utf-8 -*-
"""Une gancho + cuerpo y mezcla la musica (una pista distinta por version) con espacio para la voz.
Cambiar SOLO la musica no obliga a renderizar el video: se reutiliza el video ya hecho (-c:v copy), tarda segundos.
Uso: python ensamblar_venta.py [set 1|2] [sufijo] [carpeta_con_voces]
  set 1 = versiones A/B/C (partes hookA/B/C + body) · set 2 = versiones D/E/F (partes v2_hookD/E/F + v2_body)
  sufijo por defecto v02 (v01 queda intacto). Voces opcionales: vo_venta_<letra>.wav"""
import os, sys, subprocess
FF = r'C:\Users\Usuario\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe'
ROOT = r'E:\NIXON360_CONTENTOPS'
PID = 'N360-20261112-0001'
B = ROOT + rf'\04_PROJECTS_EDITABLE\{PID}\build'
PARTS = B + r'\parts'
INB = ROOT + rf'\00_INBOX\{PID}'
OUT = ROOT + rf'\05_RENDERS_DRAFT\{PID}'
PREV = ROOT + rf'\06_REVIEW_PREVIEWS\{PID}'
DUR = 30.0

# letra -> (archivo de musica, segundo donde empieza)
MUSICA = {
    'A': (INB + r'\atlasaudio-upbeat-documentary-621616.mp3', 0.0),
    'B': (INB + r'\cinematic-soul-upbeat-and-inspiring-corporate-music-inspire-motion-511448.mp3', 12.0),
    'C': (INB + r'\kornevmusic-upbeat-happy-corporate-487426.mp3', 0.0),
    'D': (INB + r'\danamusic-upbeat-acoustic-uplifting-238981.mp3', 0.0),
    'E': (INB + r'\the_mountain-upbeat-acoustic-593084.mp3', 0.0),
    'F': (INB + r'\grand_project-simple-happy-life-353819.mp3', 0.0),
}
SET = int(sys.argv[1]) if len(sys.argv) > 1 else 1
SUF = sys.argv[2] if len(sys.argv) > 2 else 'v02'
vodir = sys.argv[3] if len(sys.argv) > 3 else None
letras = 'ABC' if SET == 1 else 'DEF'
pref = '' if SET == 1 else 'v2_'

for v in letras:
    name = f'N360_REMAX_PROPERTY_SANTAISABEL_REEL_9x16_venta_{v}_{SUF}'
    lst = PARTS + rf'\lista_{v}_{SUF}.txt'
    open(lst, 'w', encoding='utf-8').write(
        f"file '{PARTS}\\{pref}hook{v}_mudo.mp4'\nfile '{PARTS}\\{pref}body_mudo.mp4'\n".replace('\\', '/'))
    joined = PARTS + rf'\venta_{v}_mudo.mp4'
    subprocess.run([FF, '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', joined], check=True)
    musica, off = MUSICA[v]
    mus = (f'[1:a]atrim={off}:{off + DUR},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1.0,'
           f'afade=t=out:st={DUR - 2.0}:d=2.0,volume=0.55[m]')
    vo = os.path.join(vodir, f'vo_venta_{v}.wav') if vodir else None
    if vo and os.path.exists(vo):
        fc = (mus + ';[2:a]aresample=48000,highpass=f=80,acompressor=threshold=-18dB:ratio=3:attack=5:release=120,asplit=2[vv][sc];'
              '[m][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[md];[md][vv]amix=inputs=2:normalize=0[mx];'
              '[mx]loudnorm=I=-14:TP=-1.5:LRA=9[a]')
        cmd = [FF, '-y', '-v', 'error', '-i', joined, '-i', musica, '-i', vo, '-filter_complex', fc]
    else:
        cmd = [FF, '-y', '-v', 'error', '-i', joined, '-i', musica, '-filter_complex', mus + ';[m]loudnorm=I=-14:TP=-1.5:LRA=9[a]']
    final = OUT + rf'\{name}.mp4'
    cmd += ['-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest',
            '-movflags', '+faststart', final]
    subprocess.run(cmd, check=True)
    subprocess.run([FF, '-y', '-v', 'error', '-i', final, '-vf', 'scale=540:-2', '-c:v', 'libx264', '-crf', '27', '-preset', 'veryfast',
                    '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart', PREV + rf'\preview_low_venta_{v}_{SUF}.mp4'], check=True)
    print('OK', v, os.path.basename(musica), 'con voz' if (vo and os.path.exists(vo)) else 'sin voz')
