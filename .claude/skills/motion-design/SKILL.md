---
name: motion-design
description: Diseño de movimiento (Lottie/SVG, keyframes, estados interactivos, ritmo con la música) para Reels y gráficos de PublicaBOT. Usar al definir cómo entra, se mueve y sale cada elemento.
---

# motion-design

Escrita por Claude desde conocimiento general. Estado: OBSERVADO.

## Principios
- Mover con propósito: un elemento principal por momento; el resto quieto.
- Ritmo atado al pulso de la música (corte cada 4 tiempos; hits en tiempos fuertes).
- Easing: entradas `out`, salidas `in`, énfasis con overshoot corto (≤120 ms). Duraciones 150–450 ms.
- Escalonar (stagger) 40–90 ms entre palabras/letras.
- Nada importante en el 15 % inferior ni en la franja derecha.

## Herramientas
Lottie/SVG para iconos y logos animados (verificar licencia de cada animación); keyframes calculados en Python/GSAP para texto; SFX sincronizados (whoosh en corte, tick en contadores, impacto en precio).

## Entregable
Tabla de movimiento por elemento (inicio, duración, easing, SFX) en `edit_plan.json` o en el guion, antes de renderizar.
