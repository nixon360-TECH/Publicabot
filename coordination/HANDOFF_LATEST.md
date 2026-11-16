# HANDOFF — 2026-11-16 — N360-029

- **Encargo completado:** tras aprobar el piloto, Nixon autorizó producir los cinco paquetes y crear en Google Drive `Publicidad Digital Remax Eleva`.
- **Entregado fuera de Git:** cinco paquetes en `<MEDIA_ROOT>/04_PROJECTS_EDITABLE/agentes/<id>/artes/`. Cada uno contiene 22 láminas de feed 1080×1350, 15 historias 1080×1920, 15 copys, galería, manifiesto, calendario y QA. Total: 185 diseños.
- **Recursos nuevos:** cada paquete incluye `recursos_informacion_general/` con ficha pública, preguntas frecuentes y reglas de uso. `CONFIRMADO_USUARIO` 2026-11-16: “El agua es provista por la alcaldía (ANDA).” Electricidad se mantiene como dato no confirmado y no debe comunicarse.
- **Drive:** carpeta principal creada y verificada con cinco carpetas personales. A solicitud de Nixon, la vista de cada agente se simplificó a `01 FOTOS PARA PUBLICAR` (22 JPG), `02 HISTORIAS` (15 JPG) y `03 TEXTOS PARA COPIAR Y PEGAR` (15 TXT + una instrucción breve). Los nombres comparten el número D01–D15; carruseles conservan orden 01–04. No hay ZIP, JSON ni archivos técnicos en la vista de los agentes. Todo el respaldo técnico se movió a `00 ARCHIVO INTERNO - NIXON` sin borrar datos.
- **Autorevisión:** cinco paquetes en `READY_FOR_REVIEW`; 185/185 JPG decodifican, dimensiones, hashes, zonas seguras, avisos y estructura aprobados. Revisión visual de las diez hojas generales y de las piezas de asesor en ambos formatos. Cero errores en `scripts/qa_artes_agentes.py`.
- **Privacidad:** nombres, teléfonos, retratos, copys personalizados, salidas y vínculos de Drive permanecen fuera del repositorio público.
- **Estado:** `DONE`. La carga a Drive fue autorizada y ejecutada. No se publicó en redes, no se envió a agentes y no se activó pauta.
- **Evidencia Git:** rama `feature/N360-029-artes-agentes-santa-isabel`; `scripts/codex_artes_15d.py`; `scripts/qa_artes_agentes.py`; `tests/test_agent_art_campaign.py`.

---

## Handoff anterior — 2026-11-13 — N360-028

- **Corrección de Nixon:** conservar el logo original de Santa Isabel y su tono verde. Los artes ya aprobados quedan como están porque el logo transparente no contiene fondo de color.
- **Hecho localmente:** encabezado, pie y favicon del sitio restaurados al archivo aprobado `santa-isabel-logo-aprobado.jpg`; interfaz, mapa y catálogo siguen navy/amarillo. Perfil verde original copiado a `05_RENDERS_DRAFT/N360-20261112-0001/codex_identidad_logo_original_v02/` relativa a `E:\NIXON360_CONTENTOPS`.
- **Campaña:** `codex_artes_15d_azul_amarillo_v03/` no se modificó; el hash de su ZIP se conserva.
- **Probado:** 20/20 pruebas del sitio, chequeos de sintaxis y revisión visual de escritorio. El navegador cargó el logo aprobado y el favicon original con estado 200.
- **Publicación autorizada y ejecutada:** Nixon aprobó expresamente publicar la corrección. ChatGPT Sites versión 20, commit fuente `c73f4278d1da041fc9d44dd25b8192079b2e8264`, desplegada el 13 de noviembre de 2026.
- **Verificación pública:** `https://lotificacionsantaisabel.com` cargó correctamente y la revisión visual confirmó el logo verde original en el encabezado, con la interfaz navy/amarilla intacta.
- **Estado:** `DONE`. No se modificaron ni publicaron los 41 artes y no se activó pauta.
- **Evidencia:** rama `codex/N360-028-santa-isabel-logo-original`; despliegue `appgdep_6af71ae0bedc819181643a1409411e31`; versión 20.

---

## Handoff anterior — 2026-11-13 — N360-027

- **Confirmado por Nixon:** sustituir la paleta verde de Santa Isabel por azul y amarillo en artes, identidad y sitio web; conservar el contraste que le gustó en la campaña.
- **Paleta fuente:** navy `#1B2A4A`, azul oscuro `#111D35`, apoyo `#2F5286`, amarillo `#ECD628`, blanco `#FFFFFF`. Fotografías naturales; logos oficiales de RE/MAX y Banco Industrial intactos.
- **Identidad entregada:** logo horizontal, vertical e icono en versiones clara/oscura, perfil y portada de Facebook en `05_RENDERS_DRAFT/N360-20261112-0001/codex_identidad_azul_amarillo_v01/` relativa a `E:\NIXON360_CONTENTOPS`.
- **Campaña entregada:** 41 diseños regenerados en `codex_artes_15d_azul_amarillo_v03/`, con ZIP de 31.5 MB, calendario, copys, tres carruseles y tres variantes de pauta. QA: dimensiones, decodificación, zonas seguras, datos, hashes y revisión visual aprobados. Sin publicación ni gasto.
- **Sitio web:** código original de `lotificacionsantaisabel.com` recuperado desde ChatGPT Sites. Versión local azul/amarilla completa: UI, botones, favicon, logo derivado, mapa, plano SVG y catálogo PDF. Se preservaron inventario, contactos, fotografías, lógica de financiamiento y logos de terceros.
- **Probado:** 20/20 pruebas del sitio, chequeos de sintaxis, revisión móvil en navegador y render visual de las dos páginas del catálogo PDF. No quedan referencias principales a la antigua paleta verde en los recursos de interfaz actualizados.
- **Despliegue autorizado y ejecutado:** Nixon autorizó expresamente publicar N360-027. ChatGPT Sites versión 19, commit fuente `0387db36b66028fba7a707c8de4fe75b39b04410`, desplegada el 13 de noviembre de 2026.
- **Verificación pública:** `https://lotificacionsantaisabel.com` responde 200 y entrega `styles.css?v=20261112-azul-amarillo`, favicon azul, navy `#1B2A4A` y amarillo `#ECD628`; no entrega el antiguo verde primario. Revisión visual de escritorio aprobada.
- **Estado:** `DONE`. No se publicaron artes en redes ni se activó pauta; esos pasos mantienen aprobación separada.
- **Evidencia:** `brands/santa-isabel/palette.json`, `scripts/codex_identidad_santa_isabel.py`, `scripts/codex_artes_15d.py`, `docs/tools/SANTA_ISABEL_PALETA_AZUL.md`.

---

## Handoff anterior — 2026-11-12 — N360-026

- **Confirmado por Nixon:** solo Santa Isabel; ampliar el kit actual; incluir varias fotos en un solo arte. Producir los artes aquí y dejar los videos con Claude. Chat identificado como **NBS publicabot CHATGPT**.
- **Hecho:** 41 diseños para 15 días (12–26 nov.), con 15 publicaciones y sus historias, siete láminas adicionales para tres carruseles y dos variantes adicionales de pauta en ambos formatos. Collages con fotos limpias; logos oficiales; sin fechas dentro del arte. Copy IG/FB, calendario, galería y ZIP.
- **Entrega local vigente:** `05_RENDERS_DRAFT/N360-20261112-0001/codex_artes_15d_v02/`, relativa al MEDIA_ROOT de ContentOps. `pauta_inicial/` contiene A precio, B medidas y C visita. `index.html` reúne todos los diseños.
- **Probado:** render de los 41 diseños, datos contra snapshot, dimensiones 1080×1350 y 1080×1920, límites de zona segura, superposición de textos/logos/retrato y hashes de fuentes. Revisión visual de hojas y muestras a tamaño completo. v02 separa las leyendas de los logos y corrige el retrato en historias.
- **Editable:** `brands/nixon-remax/codex_campana_15_dias.json` + `scripts/codex_artes_15d.py`. Instrucciones y evidencia del proceso de video de Claude en `docs/tools/CODEX_ARTES_SANTA_ISABEL.md`.
- **Estado:** borradores para selección de Nixon; publicación y gasto sin activar. La pauta inicial es un paquete de archivos y copy, no una campaña configurada. Revalidar precio y disponibilidad antes de cada publicación.
- **Siguiente paso:** Nixon revisa el collage A y los demás diseños en la galería. Claude conserva la producción audiovisual. Los archivos activos de Claude no se editaron.

---

## Handoff anterior — 2026-11-12 — N360-025

- **Hecho:** workspace de Codex vinculado al repositorio real como worktree de la rama `feature/N360-025-santa-isabel-videos-codex`, desde `9a4fdd7`. Conexión con GitHub comprobada por conector y Git local. Por elección directa de Nixon, se produjeron clips con movimiento desde las fotos de calles limpias.
- **Entregado:** 12 clips silenciosos de 6 segundos (seis fotos en 1080x1350 y 1080x1920), previews por formato, galería local, plan editable y QA. Carpeta relativa a MEDIA_ROOT de ContentOps: `05_RENDERS_DRAFT/N360-20261112-0001/codex_fotos_limpias_v02/`. La foto `calles-internas` está excluida. La versión v02 desplaza cuatro encuadres hacia las curvas de las calles; v01 se conserva como historial.
- **Probado:** resolución, 150 frames por clip, duración, píxeles cuadrados, yuv420p, decodificación completa, presencia de movimiento; dos pruebas de geometría de recorte. Rango de color corregido tras la primera muestra. QA y hashes en la carpeta del lote.
- **Alcance:** movimiento 2D sobre fotos ya editadas. Son recursos de montaje sin voz, música, copy o logos. El 9:16 recorta más terreno y amplía la fuente horizontal de 1672x941. No se modifica la escena ni se genera un vuelo nuevo.
- **Coordinación:** archivos nuevos `scripts/render_fotos_limpias.py`, `brands/nixon-remax/motion_kit/fotos_limpias_motion.json`, `tests/test_photo_motion.py`; uso en `docs/tools/FOTOS_LIMPIAS_MOTION.md`. Los scripts y cierres que trabaja Claude no se modificaron.
- **Pendiente:** elección de clips por Nixon e integración en los montajes de Claude. El lote conserva estado `RENDERED_DRAFT` y `publish_authorized=false`.
- **Siguiente paso:** revisar `index.html`, seleccionar tomas e importar los MP4 del formato elegido al montaje. Medios, previews y QA local permanecen fuera de Git.
- **Compatibilidad:** el plan de ocho videos incorporado por Claude en `a9089e2` identifica este material como base del video 7. PR #5 compatible con esa actualización. Se deja `manifest.json` con agente, fecha, script, entradas/salidas y hashes. La rama N360-025 fue creada antes de la nueva convención `codex/`; los renders usan el directorio propio `codex_*`.

---

## Handoff anterior — 2026-11-11 — N360-001 (histórico)

- **Hecho:** instalación y auditoría de la PC. FFmpeg 9.0.2 instalado (winget); Git y Node ya existían; repo clonado en `C:\NBS\publicabot`; FilmCraft v0.20.1 instalado (hash SHA256 verificado); MCP `filmcraft` registrado. Specs, discos y MEDIA_ROOT documentados en `docs/CURRENT_STATE.md`. Rama `feature/N360-001-pc-audit` (sin commit ni push).
- **Probado:** `ffmpeg -version`; `claude mcp list` → `filmcraft ... Connected`. NO probado: edición real con FilmCraft, Dispatch.
- **Pendiente:** C: con ~8 GB libres (mover caches/renders a E:); carpeta de trabajo dentro de `E:\`; decidir Python/Whisper; DaVinci no instalado; commit, push y PR de esta rama.
- **Necesita aprobación de Nixon:** carpeta de trabajo en MEDIA_ROOT; commit/PR de esta rama; OPEN_QUESTIONS #9 y #10.
- **Evidencia:** `docs/CURRENT_STATE.md`, `docs/OPEN_QUESTIONS.md`, `coordination/TASK_BOARD.md`; `E:\` leído solo en modo lectura (nada creado ni modificado).
- **Siguiente paso:** clip de prueba (copia, no original) por FilmCraft MCP, luego N360-004/005.
