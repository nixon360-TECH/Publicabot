# HANDOFF — 2026-11-11 — N360-001

- **Hecho:** instalación y auditoría de la PC. FFmpeg 9.0.2 instalado (winget); Git y Node ya existían; repo clonado en `C:\NBS\publicabot`; FilmCraft v0.20.1 instalado (hash SHA256 verificado); MCP `filmcraft` registrado. Specs, discos y MEDIA_ROOT documentados en `docs/CURRENT_STATE.md`. Rama `feature/N360-001-pc-audit` (sin commit ni push).
- **Probado:** `ffmpeg -version`; `claude mcp list` → `filmcraft ... Connected`. NO probado: edición real con FilmCraft, Dispatch.
- **Pendiente:** C: con ~8 GB libres (mover caches/renders a E:); carpeta de trabajo dentro de `E:\`; decidir Python/Whisper; DaVinci no instalado; commit, push y PR de esta rama.
- **Necesita aprobación de Nixon:** carpeta de trabajo en MEDIA_ROOT; commit/PR de esta rama; OPEN_QUESTIONS #9 y #10.
- **Evidencia:** `docs/CURRENT_STATE.md`, `docs/OPEN_QUESTIONS.md`, `coordination/TASK_BOARD.md`; `E:\` leído solo en modo lectura (nada creado ni modificado).
- **Siguiente paso:** clip de prueba (copia, no original) por FilmCraft MCP, luego N360-004/005.
