# HANDOFF — 2026-11-12 — N360-026

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
