@AGENTS.md

# Notas específicas de Claude (Claude Code / Dispatch)

- Las reglas de `AGENTS.md` aplican completas; este archivo no las repite ni las contradice.
- Las skills del proyecto están en `.claude/skills/`. Úsalas cuando la tarea coincida:
  - `property-fact-check`: antes de cualquier pieza de propiedad.
  - `property-reel`: Reel de propiedad, de la ficha verificada al paquete HANDOFF.
  - `organic-reel-edit`: Reel personal de @nixonhernandez_.
  - `prepublish-qa`: obligatoria antes de marcar una pieza como `READY_FOR_REVIEW`.
  - `filmcraft-edit`: montaje de clips reales con FilmCraft por MCP (alpha, con respaldo FFmpeg).
  - `threejs-scenes`: escenas 3D (maquetas, fondos) renderizadas a video.
  - `gsap-motion`: subtítulos animados, contadores y placas con GSAP.
  - `design-dna`: extraer el estilo de una imagen de referencia a tokens y mock.
  - `motion-design`: ritmo, easing y SFX de cada elemento.
  - `genjutsu-polish`: pasada final de dirección creativa antes de revisión.
- Instalación en la PC: `docs/setup/WINDOWS_SETUP.md`. Stack de video: `docs/tools/VIDEO_STACK.md`.
- Si se trabaja desde Dispatch (celular → PC): la PC debe estar encendida y la app abierta. Si falta acceso a `MEDIA_ROOT`, dilo en lugar de suponer.
- Al cerrar una sesión de trabajo, entrega el resumen en este formato: hecho / probado / pendiente / necesita aprobación / evidencia.
- Habla con Nixon en español y de forma directa. A los clientes, en los textos, siempre se les trata **de usted**.
