---
name: prepublish-qa
description: Control de calidad técnico, factual y de derechos obligatorio antes de marcar cualquier pieza de PublicaBOT como READY_FOR_REVIEW.
---

# prepublish-qa

Genera `qa_report.json` con el checklist del master §19.3, ampliado:

## Técnico (automático con ffprobe/ffmpeg)
- Resolución 1080×1920 (o 1080×1350 en portada), con duración dentro del rango del tipo de pieza.
- Sin frames negros iniciales; audio sin clipping (picos < -1 dBFS); el archivo se reproduce.
- Subtítulos dentro de la zona segura y sin cortes.

## Factual
- Cada cifra en pantalla o en el copy coincide con `property_snapshot.json` o con el evidence ledger.
- Teléfono = +50379564399 y el link wa.me funciona.
- No aparece ningún dato interno de Santa Isabel (master §11.2).

## Derechos y privacidad
- Licencia de la música registrada; fotos con origen.
- Amueblado virtual etiquetado; cielo reemplazado solo con aprobación registrada.
- Voz o avatar IA: autorización escrita para esta pieza.
- Sin menores, clientes ni placas identificables sin consentimiento.

## Marca
- Navy dominante, rojo solo al cierre, logo oficial sin alterar.
- Copy de usted; ninguna palabra de la lista prohibida (`STYLE_DECISIONS §F`).

## Resultado
- Todo OK → estado `READY_FOR_REVIEW`.
- Cualquier fallo obligatorio → `BLOCKED_*` con la razón exacta y cómo arreglarlo. Nunca se marca como publicable con fallos.
