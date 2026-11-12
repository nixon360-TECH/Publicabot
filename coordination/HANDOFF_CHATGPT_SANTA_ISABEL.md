# Instrucciones para ChatGPT / otro agente — Reel Santa Isabel (N360-20261112-0001)

Pega esto al inicio de la conversación y adjunta `AGENTS.md`, `NIXON360_CONTEXT_MASTER.md` (sección 0 y §11) y `brands/nixon-remax/design_dna_texto_viral.md`.

## Qué puede y qué no puede hacer ChatGPT aquí
- **Sí:** guiones y ganchos, copy IG/FB, hashtags, CTA de WhatsApp, calendario de contenido, prompts para artes/portadas, revisión de textos contra la ficha, ideas de ritmo.
- **No:** renderizar el video. El montaje corre en la PC de Nixon (FFmpeg + Python) y los originales están en un disco externo. ChatGPT en el navegador no puede leerlos. Todo render lo hace Claude Code en la PC o un agente con acceso local.
- Nunca publicar, programar ni enviar nada. Solo entregar el paquete (modo HANDOFF) para que Nixon apruebe.

## Reglas duras (de AGENTS.md y de esta sesión)
1. Solo datos de `property_snapshot.json` (VERIFIED_BY_USER_2026-11-12): precio **desde US$24,500**, **desde 286 varas cuadradas**, **con escritura**, **agua conectada**, ubicación Comacarán, San Miguel, contacto +503 7956 4399.
2. Banco Industrial solo con asterisco: «*Financiamiento con Banco Industrial sujeto a evaluación del banco.» y «Sujeto a disponibilidad.»
3. **Sin fechas** en pantalla ni en el copy. Nada de reserva, electricidad, mínimos de negociación, comisiones ni simulaciones de crédito.
4. Tratar a los clientes **de usted**. Hablar con Nixon en español y directo.
5. Música solo de bibliotecas gratuitas, con licencia registrada por pieza (`rights_and_sources.md`). Originales de video: solo lectura.
6. Trabajar en rama `feature/N360-XXX-...` con PR; nunca en `main`. No instalar software de pago.

## Reglas de video aprendidas (según guías de Reels; no hay medida oficial de Meta, validar en el teléfono)
- Zona segura 1080×1920: dejar libres ~250 px arriba, ~350 px abajo y ~60 px a la derecha. Nada importante ahí.
- Logos pequeños, sin placa que tape la imagen, con sombra doble. Mejor si aparecen intermitentes.
- Cortes cada 4 tiempos de la música (~100 BPM), 2–3 s por toma. Reel de terreno 20–30 s.
- Contraste mínimo garantizado en cada texto sobre cualquier fondo.
- Tildes siempre en UTF-8 (cuidado con scripts que conviertan «ó» en «?»).

## Estilo aprobado por Nixon: «texto en capas»
- Por bloque: conector en cursiva serif pequeña (Georgia Italic, crema) + palabra ligera (blanca) + **palabra protagonista** en Impact con degradado, textura de nubes y contorno negro fino (2 px) + acento amarillo `#ECD628` sin contorno fuerte (1 px).
- El color de la palabra protagonista se elige por contraste con el fondo (oscuro azul-verde sobre fondo claro; claro/plata/celeste sobre oscuro). No usar azul plano.
- Logo Santa Isabel arriba al centro (y≈270); logo RE/MAX abajo al centro, grande (≈270 px de ancho); logo oficial de RE/MAX sin recolorear.
- Gancho elegido: **C** «Antes de decidir, conózcalo desde el aire.» Variantes A y B pendientes.

## Estado y dónde está cada cosa
- Repo (GitHub): reglas, skills (`.claude/skills/`), estilo, guion. Ramas: PR #3 abierta (herramientas); `feature/N360-024-motion-skills` con las 5 skills nuevas (aún sin subir).
- **Disco externo `E:\NIXON360_CONTENTOPS` (NO está en GitHub):** originales, proxies, renders, `property_snapshot.json`, `guion_v1.md`, scripts `build/*.py`, mocks y logos. Si ChatGPT necesita algo de ahí, Nixon debe pegarlo.
- Borrador v04 listo (sin voz). v05 con el estilo nuevo en render. Falta: voz en off de Nixon, variantes de gancho, portada 4:5, copy, hashtags, `prepublish-qa`, aprobación de Nixon.

## Cómo pedirle cosas a ChatGPT (plantillas)
- «Con estos datos verificados [pegar snapshot], escribe 3 variantes de gancho de 3 segundos tratando de usted, sin fechas, sin datos no listados.»
- «Escribe el copy de IG (150 palabras máx) + 12 hashtags + CTA a wa.me/50379564399 para este Reel. Lista los datos usados y de qué campo salen.»
- «Revisa este texto contra el snapshot y marca cualquier dato que no esté ahí.»
