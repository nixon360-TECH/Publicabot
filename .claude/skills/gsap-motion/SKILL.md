---
name: gsap-motion
description: Animación con GSAP (timelines, text reveals, ScrollTrigger, React) para títulos, subtítulos animados y gráficos de PublicaBOT, renderizados a video. Usar para texto cinético y tarjetas finales.
---

# gsap-motion

Escrita por Claude desde conocimiento general. Estado: OBSERVADO, sin probar con medios reales.

## Cuándo
Subtítulos palabra por palabra, contadores (286 v², precio), placas finales, lower-thirds. Alternativa al render con Python (`build/video_build.py` de N360-20261112-0001).

## Flujo
1. Página HTML 1080×1920 con fondo transparente; GSAP con versión fijada.
2. Un `gsap.timeline({paused:true})` maestro. Control por `timeline.time(t)` para render determinista; nada de animación en tiempo real.
3. Texto: separar por palabras/letras (SplitText o `<span>` propios); entrada con `y`, `scale`, `autoAlpha`, `ease: "back.out(1.7)"`; palabra activa resaltada según los tiempos del audio (transcripción Whisper).
4. Contadores: `gsap.to(obj,{val:286,roundProps:"val",onUpdate})`.
5. Render: captura por cuadro con Playwright (PNG con alfa) → FFmpeg `overlay` sobre el video base. Mantener fps = fps del proyecto.
6. ScrollTrigger solo aplica a páginas web, no a video; no usarlo para Reels.

## Reglas
Estilo de subtítulos: el que Nixon aprobó (ver `docs/STYLE_DECISIONS` y la imagen de referencia). Contraste mínimo garantizado sobre cualquier fondo. Tildes siempre UTF-8.
