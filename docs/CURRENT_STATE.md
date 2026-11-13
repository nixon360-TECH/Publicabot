# CURRENT_STATE — 2026-11-12

| Elemento | Estado | Evidencia |
|---|---|---|
| Repo `nixon360-TECH/Publicabot` | OBSERVADO 2026-11-12: conector GitHub y Git local autenticados; remoto accesible | PR #4: `feature/N360-024-motion-skills`; worktree Codex: `feature/N360-025-santa-isabel-videos-codex`, basado en `9a4fdd7` |
| Master v1.0 | OBSERVADO | `NIXON360_CONTEXT_MASTER.md` |
| Decisiones de estilo | CONFIRMADO_USUARIO | `docs/style/` |
| Skills de Claude (4) | OBSERVADO: escritas, no probadas con medios reales | `.claude/skills/` |
| Código / pipeline | OBSERVADO: scripts de mocks, paneo y render de fotos limpias por lotes | `brands/nixon-remax/motion_kit/`, `scripts/render_fotos_limpias.py`, `docs/tools/FOTOS_LIMPIAS_MOTION.md` |
| PC Windows (specs) | OBSERVADO 2026-11-11 | Windows 11 Home 10.0.26300; i5-1135G7 (8 hilos); 7.7 GB RAM; GPU Intel Iris Xe (sin NVIDIA/CUDA). **C: 237 GB, solo ~8 GB libres** (riesgo para renders) |
| MEDIA_ROOT | CONFIRMADO_USUARIO: `E:\` (raíz) | Disco USB "Nixon", exFAT, 931 GB, ~698 GB libres. Contiene: ~9.3k JPG, 4.4k JPEG, 1.1k MP4, 168 MOV, 331 DNG (conteo a 3 niveles). Raíz mezcla material personal y de trabajo; sin estructura INBOX/OUTPUT aún. `.env` local creado (no versionado) |
| Claude Desktop + Dispatch | OBSERVADO: Claude Desktop/Code funcionando; Dispatch NO VERIFICADO | Claude Code 2.1.321 |
| Git / Node.js | OBSERVADO | Git 2.56.0, Node v24.11.1 |
| FFmpeg | OBSERVADO: instalado 2026-11-11 vía winget (`Gyan.FFmpeg` 9.0.2 full) | `ffmpeg -version`; ffprobe disponible |
| FilmCraft | OBSERVADO: v0.20.1 (MSI x64, SHA256 verificado y firma Authenticode válida) | `%LOCALAPPDATA%\Programs\ArtCraft\FilmCraft\filmcraft-cli.exe` |
| MCP `filmcraft` | OBSERVADO: registrado (scope local del proyecto) y `Connected` en `claude mcp list` | No probado aún con un clip real |
| Whisper / Auto-Editor | NO INSTALADOS (no hay Python real; solo alias de Microsoft Store) | FilmCraft trae Whisper integrado; ver OPEN_QUESTIONS #10 |
| DaVinci Resolve | NO INSTALADO | — |
| REconnect | NO CONECTADO | export/API PENDIENTE |
| Meta Business Suite | Lo usa Nixon para programar | — |
| Meta Marketing API / Google Ads API | NO CONECTADO | Fase 4 |
| Repos hermanos: Buscabot-NBS, santa-isabel-sitio, santa-isabel-media-ops | HISTÓRICO (vistos el 8-nov) | no auditados aún |
| Sitio `lotificacionsantaisabel.com` | PUBLICADO 2026-11-13: ChatGPT Sites versión 19, identidad azul/amarilla N360-027 | Dominio responde 200; nuevo CSS, favicon y catálogo confirmados; 20 pruebas pasan |
| Corrección logo Santa Isabel N360-028 | LISTA_LOCAL: logo verde original restaurado en encabezado, pie y favicon; paleta azul/amarilla conservada; despliegue pendiente de autorización específica | 20 pruebas pasan; revisión visual aprobada; campaña v03 no modificada |
| Chat previo «PublicaBOT» | NO ENCONTRADO | Nixon lo traerá |
