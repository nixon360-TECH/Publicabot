# -*- coding: utf-8 -*-
"""Guiones de voz de los 12 videos (una sola fuente). Genera guiones_voz.json y el teleprompter.
Cada linea: [segundo en que debe EMPEZAR, texto]. Los tiempos coinciden con los textos en pantalla."""
import json, os
BASE = r'E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001'
CIERRE = 'Escríbanos para agendar su visita.'
CUERPO_A = [
    [4.2, 'Lotificación Santa Isabel, en Comacarán, San Miguel.'],
    [7.6, 'Frente al Instituto Nacional de Comacarán y cerca del parque central.'],
    [11.2, 'Terrenos desde doscientas ochenta y seis varas cuadradas, con escritura y agua conectada.'],
    [15.6, 'Calles asfaltadas dentro de la lotificación.'],
    [19.2, 'Desde veinticuatro mil quinientos dólares, con financiamiento con Banco Industrial.'],
    [25.4, CIERRE],
]
CUERPO_G = [
    [4.2, 'Lotificación Santa Isabel, en Comacarán, San Miguel.'],
    [7.6, 'Frente al Instituto Nacional de Comacarán y cerca del parque central.'],
    [11.2, 'Terrenos desde doscientas ochenta y seis varas cuadradas, con escritura y agua conectada, listos para construir.'],
    [16.0, 'Con calles asfaltadas dentro de la lotificación.'],
    [19.2, 'Desde veinticuatro mil quinientos dólares, con financiamiento con Banco Industrial.'],
    [25.4, CIERRE],
]
G = {
    'A': ('¿Busca dónde construir su nueva casa en San Miguel?', CUERPO_A),
    'B': ('Paz y tranquilidad, a minutos de la ciudad.', CUERPO_A),
    'C': ('Terrenos desde veinticuatro mil quinientos dólares, en Comacarán, San Miguel.', CUERPO_A),
    'D': ('¿Sueña con su casa propia en San Miguel?', CUERPO_G),
    'E': ('Terrenos desde doscientas ochenta y seis varas cuadradas, en Comacarán.', CUERPO_G),
    'F': ('Escritura, agua conectada y calles asfaltadas, en Comacarán, San Miguel.', CUERPO_G),
    'G1': ('¿Cuánto cuesta un terreno en Comacarán? Desde veinticuatro mil quinientos dólares.', CUERPO_G),
    'G4': ('¿Y al comprar me dan mi escritura? Sí: con escritura.', CUERPO_G),
    'H1': ('Hermano lejano, tu terreno en San Miguel te espera.', CUERPO_G),
    'H2': ('¿Vive fuera del país? Tu terreno en Comacarán, San Miguel, ¡te espera!', CUERPO_G),
    'H3': ('Hermano lejano, ¿qué haces con veinticuatro mil quinientos dólares en El Salvador? ¡Compras tu primer lote para tu casa!', CUERPO_G),
}
TITULOS = {
    'A': '¿Busca dónde construir su nueva casa?', 'B': 'Paz y tranquilidad', 'C': 'Terrenos desde US$24,500',
    'D': '¿Sueña con su casa propia?', 'E': 'Terrenos desde 286 v²', 'F': 'Escritura, agua y calles',
    'G1': '¿Cuánto cuesta un terreno en Comacarán?', 'G2': 'Tres preguntas', 'G4': '¿Y al comprar me dan mi escritura?',
    'H1': 'Hermano lejano · tu terreno te espera', 'H2': 'Hermano lejano · ¿vive fuera del país?', 'H3': 'Hermano lejano · ¿qué haces con $24,500?',
}
out = {k: [[0.2, h]] + body for k, (h, body) in G.items()}
out['G2'] = [
    [0.2, 'Tres preguntas antes de comprar un terreno.'],
    [4.2, 'Uno. ¿Dónde queda? Frente al Instituto Nacional de Comacarán.'],
    [8.2, 'Lotificación Santa Isabel, en Comacarán, San Miguel, cerca del parque central.'],
    [12.2, 'Dos. ¿Qué trae? Escritura, agua conectada y calles asfaltadas.'],
    [16.4, 'Terrenos listos para construir.'],
    [19.4, 'Tres. ¿Cuánto cuesta? Desde veinticuatro mil quinientos dólares, en terrenos desde doscientas ochenta y seis varas cuadradas.'],
    [25.4, CIERRE],
]
orden = ['A', 'B', 'C', 'D', 'E', 'F', 'G1', 'G2', 'G4', 'H1', 'H2', 'H3']
data = {k: {'titulo': TITULOS[k], 'lineas': out[k]} for k in orden}
json.dump(data, open(BASE + r'\guiones_voz.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# guion legible (para leer sin teleprompter)
md = ['# Guiones de voz — 12 videos', '', 'Lea cada línea con calma y **haga una pausa de un segundo entre línea y línea**: así el programa coloca su voz exactamente donde va.', '']
for k in orden:
    md.append(f'## {k} · {TITULOS[k]}')
    for t, s in data[k]['lineas']:
        md.append(f'{len(md) and ""}- **{t:.1f} s** — {s}')
    md.append('')
open(BASE + r'\GUIONES_PARA_LEER.md', 'w', encoding='utf-8').write('\n'.join(md))

# teleprompter: pagina unica con los guiones incrustados
html = open(BASE + r'\teleprompter_plantilla.html', encoding='utf-8').read()
html = html.replace('/*DATOS*/', 'const DATOS = ' + json.dumps(data, ensure_ascii=False) + ';')
open(BASE + r'\teleprompter_venta.html', 'w', encoding='utf-8').write(html)
print('ok', len(data), 'guiones')

# pagina para leer VIENDO el video
plant = open(BASE + r'\guion_con_video_plantilla.html', encoding='utf-8').read()
open(BASE + r'\guion_con_video.html', 'w', encoding='utf-8').write(plant.replace('/*DATOS*/', 'const DATOS = ' + json.dumps(data, ensure_ascii=False) + ';'))
print('guion_con_video.html listo')
