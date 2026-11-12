---
name: filmcraft-edit
description: Edita video con FilmCraft (editor open-source tipo Premiere) a través de su servidor MCP: importar tomas, armar secuencia vertical 1080×1920, cortar, color, audio y exportar MP4. Usar cuando una pieza de PublicaBOT necesite montaje de clips reales (Nixon, dron, recorridos, Santa Isabel).
---

# filmcraft-edit

FilmCraft (`storytold/filmcraft`, Apache-2.0/MIT) está en **alpha**. Úsalo con respaldo FFmpeg para entregas con fecha.

## Precondiciones
- MCP registrado (ver `docs/setup/WINDOWS_SETUP.md`):
  `claude mcp add filmcraft -- "%LOCALAPPDATA%\Programs\ArtCraft\FilmCraft\filmcraft-cli.exe" mcp`
  - Sin `--bridge`: modo headless, sin ventana. Es el modo que se usa con Dispatch o en procesos nocturnos.
  - Con `--bridge 127.0.0.1:9876`: maneja la app abierta (`filmcraft --control 9876`). Nixon ve la edición en vivo.
- Brief y `edit_plan.json` aprobados (skills property-reel / organic-reel-edit).
- Originales en `MEDIA_ROOT/01_ORIGINALS_READONLY`. **Trabajar sobre proxies o copias; nunca sobrescribir originales.**
- **El servidor MCP no limita carpetas: puede leer y escribir donde pueda el usuario.** Usar solo rutas dentro de `MEDIA_ROOT` y `04_PROJECTS_EDITABLE` / `05_RENDERS_DRAFT`.

## Ciclo de trabajo (según docs/agents.md de FilmCraft)
1. `command_list` con filtro (ej. `sequence`, `export`, `color`): descubrir los IDs de comando reales. **No inventar IDs.**
2. `media_import` con rutas absolutas → `project_inspect` para obtener los IDs.
3. Crear la secuencia 1080×1920 al frame rate de las tomas (preset vertical).
4. Armar el EDL con `command_batch` (`stop_on_error: true`).
5. Revisar con `sequence_inspect` y `render_frame` en puntos clave (0 s, gancho, cierre). Si algo está mal, usar `edit.undo`.
6. Color natural neutro, nivel de diálogo constante y música por debajo de la voz (STYLE_DECISIONS §C/§E).
7. Guardar el proyecto `.fcproj` en `04_PROJECTS_EDITABLE/<content_id>/`, para que Nixon pueda abrirlo y retocarlo.
8. Exportar con `file.exportMedia` (`wait: true`, `range: "entire"`) a `05_RENDERS_DRAFT/<content_id>/`. Revisar `warnings` y `offlineMedia`.
9. Validar con ffprobe y pasar a `prepublish-qa`.

## Límites
- Los subtítulos virales animados **no** se hacen aquí: van en la capa de diseño (Remotion o ASS, ver `docs/tools/VIDEO_STACK.md`).
- El TTS de FilmCraft (Kokoro) **no es la voz de Nixon**. No usarlo en piezas publicables sin aprobación.
- Si FilmCraft falla o se cuelga: registrar el error en el handoff y producir con FFmpeg. No reintentar indefinidamente.
