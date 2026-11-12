---
name: design-dna
description: Ingeniería inversa de un diseño de referencia (web, Reel, imagen) a un sistema reutilizable: colores, tipografías, espaciado, jerarquía y layout. Usar cuando Nixon manda una foto/ejemplo de "así me gusta" para replicar el estilo.
---

# design-dna

Escrita por Claude desde conocimiento general. Estado: OBSERVADO.

## Flujo
1. Recibir la referencia (imagen/video). Guardarla en `brands/<marca>/refs/` con su fuente.
2. Extraer, midiendo (no a ojo): paleta (hex, 5–7 colores y rol), tipografías (familia/peso/tamaño relativo; si es de pago, buscar equivalente libre), escala de espaciado, radios, sombras, alineación, relación texto/fondo, tratamiento de color y movimiento (duración, easing).
3. Escribir el "ADN" en `brands/<marca>/design_dna_<nombre>.md` y como tokens (`json`/CSS variables).
4. Hacer un mock de un fotograma y compararlo lado a lado con la referencia; ajustar hasta que Nixon diga "exacto".
5. No copiar logos ni material con derechos de terceros; solo el estilo.

## Salida
Documento de ADN + tokens + mock. Lo usan `gsap-motion`, `motion-design` y `property-reel`.
