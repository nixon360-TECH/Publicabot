# -*- coding: utf-8 -*-
"""Mezcla FINAL de los 12 videos: une gancho + cuerpo, pone una musica distinta en cada uno y, si existe la voz de Nixon,
la alinea (alinear_voz.py), baja la musica mientras habla y normaliza a -14 LUFS. Sin voz = musica sola (vista previa).
Voces: E:\\NIXON360_CONTENTOPS\\00_INBOX\\N360-20261112-0001\\voces\\vo_<ID>.(m4a|mp3|wav|aac|ogg)
Uso: python mezclar_voces.py [IDs...]   ej.: python mezclar_voces.py A G2   (sin IDs = todos los que tengan video)"""
import os, sys, glob, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
FF = r'C:\Users\Usuario\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe'
ROOT = r'E:\NIXON360_CONTENTOPS'
PID = 'N360-20261112-0001'
PARTS = ROOT + rf'\04_PROJECTS_EDITABLE\{PID}\build\parts'
INB = ROOT + rf'\00_INBOX\{PID}'
VOCES = INB + r'\voces'
OUT = ROOT + rf'\05_RENDERS_DRAFT\{PID}'
PREV = ROOT + rf'\06_REVIEW_PREVIEWS\{PID}'
DUR = 30.0
SUF = 'v03'

DOC = 'atlasaudio-upbeat-documentary-621616.mp3'
INSP = 'cinematic-soul-upbeat-and-inspiring-corporate-music-inspire-motion-511448.mp3'
KORN = 'kornevmusic-upbeat-happy-corporate-487426.mp3'
DANA = 'danamusic-upbeat-acoustic-uplifting-238981.mp3'
MONT = 'the_mountain-upbeat-acoustic-593084.mp3'
HAPPY = 'grand_project-simple-happy-life-353819.mp3'
# id -> (gancho, cuerpo, musica, segundo de inicio de la musica)
V = {
    'A':  ('hookA', 'body', DOC, 0.0),
    'B':  ('hookB', 'body', INSP, 12.0),
    'C':  ('hookC', 'body', KORN, 0.0),
    'D':  ('v2_hookD', 'v2_body2b', DANA, 0.0),
    'E':  ('v2_hookE', 'v2_body2b', MONT, 0.0),
    'F':  ('v2_hookF', 'v2_body2b', HAPPY, 0.0),
    'G1': ('v2_hookG1', 'v2_body2b', INSP, 40.0),
    'G2': ('v3_hookG2', 'v3_body', DOC, 30.0),
    'G4': ('v2_hookG4', 'v2_body2b', KORN, 30.0),
    'H1': ('v2_hookH1', 'v2_body2b', DANA, 40.0),
    'H2': ('v2_hookH2', 'v2_body2b', MONT, 25.0),
    'H3': ('v2_hookH3', 'v2_body2b', HAPPY, 30.0),
}
ids = [a.upper() for a in sys.argv[1:]] or list(V)


def parte(n):
    return PARTS + '\\' + n + '_mudo.mp4'


for i in ids:
    hook, body, mus, off = V[i]
    if not (os.path.exists(parte(hook)) and os.path.exists(parte(body))):
        print('FALTA parte de video para', i, '-> se omite'); continue
    lst = PARTS + rf'\lista_{i}_{SUF}.txt'
    open(lst, 'w', encoding='utf-8').write(f"file '{parte(hook)}'\nfile '{parte(body)}'\n".replace('\\', '/'))
    joined = PARTS + rf'\unido_{i}.mp4'
    subprocess.run([FF, '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', joined], check=True)
    m = (f'[1:a]atrim={off}:{off + DUR},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1.0,'
         f'afade=t=out:st={DUR - 2.0}:d=2.0,volume=0.55[m]')
    crudas = [f for f in glob.glob(VOCES + rf'\vo_{i}.*') if '_alineada' not in f]
    voz = None
    if crudas:
        try:
            import alinear_voz
            voz = alinear_voz.alinear(i, crudas[0])
        except SystemExit as e:
            print(e)
        except Exception as e:
            print('No se pudo alinear', i, '->', e)
    cmd = [FF, '-y', '-v', 'error', '-i', joined, '-i', INB + '\\' + mus]
    if voz:
        cmd += ['-i', voz]
        fc = (m + ';[2:a]aresample=48000,highpass=f=80,acompressor=threshold=-18dB:ratio=3:attack=5:release=120,asplit=2[vv][sc];'
              '[m][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[md];'
              '[md][vv]amix=inputs=2:normalize=0:duration=first[mx];[mx]loudnorm=I=-14:TP=-1.5:LRA=9[a]')
    else:
        fc = m + ';[m]loudnorm=I=-14:TP=-1.5:LRA=9[a]'
    name = f'N360_REMAX_PROPERTY_SANTAISABEL_REEL_9x16_venta_{i}_{SUF}'
    final = OUT + rf'\{name}.mp4'
    cmd += ['-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
            '-t', str(DUR), '-movflags', '+faststart', final]
    subprocess.run(cmd, check=True)
    subprocess.run([FF, '-y', '-v', 'error', '-i', final, '-vf', 'scale=540:-2', '-c:v', 'libx264', '-crf', '27', '-preset', 'veryfast',
                    '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart', PREV + rf'\preview_low_venta_{i}_{SUF}.mp4'], check=True)
    print('OK', i, 'con voz' if voz else 'SIN voz (musica sola)', '->', final)
