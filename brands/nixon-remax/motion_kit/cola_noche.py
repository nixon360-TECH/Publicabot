# -*- coding: utf-8 -*-
"""Cola nocturna (se ejecuta una tarea detras de otra, con registro y estado).
1) espera a que termine el render de las 3 versiones «venta» de 30 s (parts/fin4.txt)
2) crea proxies SDR 9:16 de las tomas de SAN MIGUEL que usaran los videos 3-6 (originales intactos)
Mantiene la PC despierta mientras corre (SetThreadExecutionState; no cambia ajustes del sistema).
Estado: build/cola_estado.json · Registro: build/cola_log.txt"""
import os, sys, time, json, glob, subprocess, ctypes, datetime

FF = r'C:\Users\Usuario\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe'
ROOT = r'E:\NIXON360_CONTENTOPS'
PID = 'N360-20261112-0001'
BUILD = ROOT + rf'\04_PROJECTS_EDITABLE\{PID}\build'
PROX = ROOT + rf'\02_PROXIES\{PID}'
SM = r'E:\SAN MIGUEL'
LOG = BUILD + r'\cola_log.txt'
EST = BUILD + r'\cola_estado.json'
ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

estado = {'inicio': str(datetime.datetime.now()), 'tareas': []}


def log(m):
    line = f'[{datetime.datetime.now():%H:%M:%S}] {m}'
    print(line, flush=True)
    open(LOG, 'a', encoding='utf-8').write(line + '\n')


def guardar():
    json.dump(estado, open(EST, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


# 1) esperar el render de las versiones de 30 s
fin = BUILD + r'\parts\fin4.txt'
log('esperando fin del render venta A/B/C (30 s)')
t0 = time.time()
while not os.path.exists(fin) and time.time() - t0 < 3 * 3600:
    time.sleep(20)
estado['tareas'].append({'tarea': 'venta_30s', 'ok': os.path.exists(fin)})
guardar()
log('venta 30 s: ' + ('lista' if os.path.exists(fin) else 'NO termino (revisar)'))

# 2) proxies SDR 9:16 (HDR 4K horizontal -> recorte central vertical; verticales 1080p -> copia reescalada)
HDR = ['0558', '0559', '0555', '0557', '0554', '0560', '0570', '0574', '0575', '0576', '0578']
VER = ['0064', '0065', '0066', '0068']
os.makedirs(PROX, exist_ok=True)
vf_hdr = ('fps=25,zscale=t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=mobius,'
          'zscale=t=bt709:m=bt709:r=tv,format=yuv420p,scale=-2:1920,crop=1080:1920')
vf_ver = 'fps=25,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,format=yuv420p'
for n in HDR + VER:
    src = [f for f in glob.glob(SM + rf'\DJI_*_{n}_D.MP4') if 'copia' not in f]
    if not src:
        log(f'{n}: sin archivo'); estado['tareas'].append({'tarea': 'proxy_' + n, 'ok': False}); continue
    out = PROX + rf'\sm_{n}_sdr_9x16.mp4'
    if os.path.exists(out) and os.path.getsize(out) > 100000:
        log(f'{n}: ya existe'); continue
    t = time.time()
    r = subprocess.run([FF, '-y', '-v', 'error', '-i', src[0], '-t', '30', '-vf', vf_hdr if n in HDR else vf_ver,
                        '-an', '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p',
                        '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', out], capture_output=True, text=True)
    ok = r.returncode == 0 and os.path.exists(out)
    estado['tareas'].append({'tarea': 'proxy_' + n, 'ok': ok, 'seg': round(time.time() - t), 'err': r.stderr[-200:] if not ok else ''})
    guardar()
    log(f'{n}: {"ok" if ok else "ERROR"} ({round(time.time() - t)} s)')

estado['fin'] = str(datetime.datetime.now())
guardar()
log('COLA TERMINADA')
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
