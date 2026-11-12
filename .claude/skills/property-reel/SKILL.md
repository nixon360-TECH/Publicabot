---
name: property-reel
description: Produce un Reel de propiedad para @nixon.remax / Facebook Page, desde la ficha verificada hasta el paquete HANDOFF con 3 variantes de gancho. Usar cuando Nixon pida un video o Reel de una propiedad.
---

# property-reel

## Precondiciones
- `property_snapshot.json` en estado `VERIFIED` (skill `property-fact-check`).
- Medios reales en `MEDIA_ROOT/00_INBOX` o `01_ORIGINALS_READONLY`.
- Leer `docs/style/STYLE_DECISIONS.md`. Manda sobre cualquier preferencia del agente.

## Reglas de estilo (resumen; la fuente es STYLE_DECISIONS)
- Duración por tipo: terreno 20–30 s · casa o apartamento 30–45 s · propiedad grande 45–60 s.
- Ritmo de 2–3 s por toma, gradación natural, navy dominante, rojo solo al cierre.
- Estructura: intro de Nixon a cámara → recorrido con voz en off → cierre de Nixon con CTA a WhatsApp.
- Apertura con dron si hay toma autorizada.
- Subtítulos palabra por palabra, dinámicos. Usar plantillas de R1–R4 cuando existan; mientras tanto, la plantilla base del repo.
- Texto en pantalla: precio + zona + logo pequeño. Datos solo del snapshot.

## Proceso
1. Copiar los originales a `02_PROXIES` con ffprobe y crear un manifiesto con hash SHA-256. Nunca tocar los originales.
2. Transcribir las tomas de Nixon (Whisper local) y revisar cifras y nombres de zonas.
3. Guion en el formato del master §19.2 con **3 ganchos A/B/C**: mismo cuerpo, cambian los 0–3 s y la portada. Rotar tipos de gancho e investigar ganchos actuales; ser creativo sin afirmar nada falso.
4. EDL en JSON con `asset_id` y rangos reales; prohibido inventar tomas.
5. Render con FFmpeg: master 1080×1920 por variante, preview liviano y portada 4:5.
6. Copy de IG y FB: tono profesional cercano de usted, viñetas de ficha, 10–15 hashtags, CTA wa.me rastreable (+503 7956 4399).
7. Ejecutar `prepublish-qa`.

## Salida (paquete por pieza, master §18)
`property_snapshot.json`, `media_authorizations.json`, `transcript_es.srt`, `edit_plan.json`, `variant_A|B|C_1080x1920.mp4`, `preview_low.mp4`, `cover_4x5.png`, `copy_instagram.md`, `copy_facebook.md`, `whatsapp_message_draft.md`, `rights_and_sources.md`, `qa_report.json`, `approval_status.json`.

## Prohibido
Publicar o programar. Usar voz IA sin autorización escrita para esa pieza. Amueblado virtual sin la etiqueta «Ambientación ilustrativa». Reemplazar el cielo sin preguntar.
