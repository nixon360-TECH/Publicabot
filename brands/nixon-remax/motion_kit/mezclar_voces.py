# -*- coding: utf-8 -*-
"""Mezcla FINAL de los videos: une gancho + cuerpo, pone una musica distinta en cada uno y, si existe la voz de Nixon,
la alinea (quita el silencio inicial y la coloca a 0.2 s), baja la musica mientras habla y normaliza a -14 LUFS.
Sin voz tambien funciona (deja la musica sola = vista previa).

Voces: carpeta E:\\NIXON360_CONTENTOPS\\00_INBOX\\N360-20261112-0001\\voces\\ con archivos vo_A, vo_B, vo_G1, vo_G2, vo_G4, vo_H
(cualquier formato: .m4a .mp3 .wav .aac .ogg). Uso:  python mezclar_voces.py [IDs...]   ej.  python mezclar_voces.py A G2"""
import os, sys, glob, subprocess
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

# id -> (parte gancho, parte cuerpo, musica, segundo de inicio)
V = {
    'A':  ('hookA.mp4', 'body.mp4', 'atlasaudio-upbeat-documentary-621616.mp3', 0.0),
    'B':  ('hookB.mp4', 'body.mp4', 'cinematic-soul-upbeat-and-inspiring-corporate-music-inspire-motion-511448.mp3', 12.0),
    'G1': ('v2_hookG1.mp4', 'v2_body2b.mp4', 'kornevmusic-upbeat-happy-corporate-487426.mp3', 0.0),
    'G2': ('v3_hookG2.mp4', 'v3_body.mp4', 'danamusic-upbeat-acoustic-uplifting-238981.mp3', 0.0),
    'G4': ('v2_hookG4.mp4', 'v2_body2b.mp4', 'the_mountain-upbeat-acoustic-593084.mp3', 0.0),
    'H':  ('v2_hookH.mp4', 'v2_body2b.mp4', 'grand_project-simple-happy-life-353819.mp3', 0.0),
}
ids = [a.upper() for a in sys.argv[1:]] or list(V)


def parte(n):
    return PARTS + '\\' + n.replace('.mp4', '_mudo.mp4')


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
    voz = glob.glob(VOCES + rf'\vo_{i}.*')
    cmd = [FF, '-y', '-v', 'error', '-i', joined, '-i', INB + '\\' + mus]
    if voz:
        cmd += ['-i', voz[0]]
        fc = (m + ';[2:a]aresample=48000,silenceremove=start_periods=1:start_threshold=-38dB:start_silence=0.1,'
              'adelay=200|200,highpass=f=80,acompressor=threshold=-18dB:ratio=3:attack=5:release=120,asplit=2[vv][sc];'
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
