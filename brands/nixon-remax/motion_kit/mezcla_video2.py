# -*- coding: utf-8 -*-
"""Mezcla del video 2: musica (bed) + espacio para la voz de Nixon.
Sin voz: musica a nivel de cama, loudnorm -14. Con voz (vo_video2.wav): la musica baja sola cuando Nixon habla (sidechain).
Uso: python mezcla_video2.py [ruta_voz.wav]"""
import os, sys, subprocess
FF = r'C:\Users\Usuario\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe'
B = r'E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001\build'
NAME = 'N360_REMAX_PROPERTY_SANTAISABEL_REEL_9x16_video2_calles_v01'
VIDEO = B + rf'\{NAME}_mudo.mp4'
MUSIC = r'E:\NIXON360_CONTENTOPS\00_INBOX\N360-20261112-0001\universfield-warm-acoustic-guitar-232912.mp3'
OUT = rf'E:\NIXON360_CONTENTOPS\05_RENDERS_DRAFT\N360-20261112-0001\{NAME}.mp4'
DUR = 16.8
vo = sys.argv[1] if len(sys.argv) > 1 else None

mus = f'[1:a]atrim=0:{DUR},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1.0,afade=t=out:st={DUR-2.0}:d=2.0,volume=0.55[m]'
if vo and os.path.exists(vo):
    fc = (mus + f';[2:a]aresample=48000,highpass=f=80,acompressor=threshold=-18dB:ratio=3:attack=5:release=120,asplit=2[v][sc];'
          '[m][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[md];[md][v]amix=inputs=2:normalize=0[mx];'
          '[mx]loudnorm=I=-14:TP=-1.5:LRA=9[a]')
    cmd = [FF, '-y', '-v', 'error', '-i', VIDEO, '-i', MUSIC, '-i', vo, '-filter_complex', fc]
else:
    fc = mus + ';[m]loudnorm=I=-14:TP=-1.5:LRA=9[a]'
    cmd = [FF, '-y', '-v', 'error', '-i', VIDEO, '-i', MUSIC, '-filter_complex', fc]
cmd += ['-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest', '-movflags', '+faststart', OUT]
subprocess.run(cmd, check=True)
print('FINAL', OUT, 'con voz' if (vo and os.path.exists(vo)) else 'sin voz (espacio reservado)')
