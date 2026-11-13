# -*- coding: utf-8 -*-
"""Prueba del alineador con una voz sintetica (Windows, Helena es-ES): lee el guion A con pausas de 1 s."""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
FF = r'C:\Users\Usuario\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe'
BASE = r'E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001'
TMP = BASE + r'\work\tts'
os.makedirs(TMP, exist_ok=True)
lineas = json.load(open(BASE + r'\guiones_voz.json', encoding='utf-8'))['A']['lineas']
ps = ['Add-Type -AssemblyName System.Speech', '$s = New-Object System.Speech.Synthesis.SpeechSynthesizer',
      '$s.SelectVoice("Microsoft Helena Desktop")', '$s.Rate = 1']
for i, (_, t) in enumerate(lineas):
    ps.append('$s.SetOutputToWaveFile("%s\\l%d.wav"); $s.Speak("%s"); $s.SetOutputToNull()' % (TMP, i, t.replace('"', '')))
open(TMP + r'\tts.ps1', 'w', encoding='utf-8-sig').write('\n'.join(ps))
subprocess.run(['powershell', '-NoProfile', '-File', TMP + r'\tts.ps1'], check=True)
args = [FF, '-y', '-v', 'error']
filt = []
for i in range(len(lineas)):
    args += ['-i', TMP + rf'\l{i}.wav']
for i in range(len(lineas)):
    filt.append(f'[{i}:a]aresample=48000,apad=pad_dur=1.0[a{i}]')
filt.append(''.join(f'[a{i}]' for i in range(len(lineas))) + f'concat=n={len(lineas)}:v=0:a=1[o]')
os.makedirs(r'E:\NIXON360_CONTENTOPS\00_INBOX\N360-20261112-0001\voces', exist_ok=True)
dest = r'E:\NIXON360_CONTENTOPS\00_INBOX\N360-20261112-0001\voces\PRUEBA_vo_A.wav'
subprocess.run(args + ['-filter_complex', ';'.join(filt), '-map', '[o]', dest], check=True)
print('voz de prueba:', dest)
import alinear_voz
alinear_voz.alinear('A', dest)
