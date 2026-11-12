# CURRENT_STATE — 2026-11-12

| Elemento | Estado | Evidencia |
|---|---|---|
| Repo `nixon360-TECH/publicabot` | OBSERVADO: creado; base en PR | rama `feature/N360-000-repo-base` |
| Master v1.0 | OBSERVADO | `NIXON360_CONTEXT_MASTER.md` |
| Decisiones de estilo | CONFIRMADO_USUARIO | `docs/style/` |
| Skills de Claude (4) | OBSERVADO: escritas, no probadas con medios reales | `.claude/skills/` |
| Código / pipeline | NO EXISTE | — |
| PC Windows (specs) | OBSERVADO 2026-11-11 | Windows 11 Home 10.0.26300; i5-1135G7 (8 hilos); 7.7 GB RAM; GPU Intel Iris Xe (sin NVIDIA/CUDA). **C: 237 GB, solo ~8 GB libres** (riesgo para renders) |
| MEDIA_ROOT | CONFIRMADO_USUARIO (2026-11-12): `E:\NIXON360_CONTENTOPS` | Disco USB "Nixon", exFAT, 931 GB, ~698 GB libres. Carpeta creada con las 11 subcarpetas del master §5.3 (`00_INBOX` … `99_FAILED_QUARANTINE`). El resto de `E:\` (material personal y anterior) no se tocó. `.env` local apunta aquí (no versionado) |
| Claude Desktop + Dispatch | OBSERVADO: Claude Desktop/Code funcionando; Dispatch NO VERIFICADO | Claude Code 2.1.321 |
| Git / Node.js | OBSERVADO | Git 2.56.0, Node v24.11.1 |
| FFmpeg | OBSERVADO: instalado 2026-11-11 vía winget (`Gyan.FFmpeg` 9.0.2 full) | `ffmpeg -version`; ffprobe disponible |
| FilmCraft | OBSERVADO: v0.20.1 (MSI x64, SHA256 verificado y firma Authenticode válida) | `%LOCALAPPDATA%\Programs\ArtCraft\FilmCraft\filmcraft-cli.exe` |
| MCP `filmcraft` | OBSERVADO: registrado (scope local del proyecto) y `Connected` en `claude mcp list` | Prueba por CLI (2026-11-12): copia de clip en `00_INBOX` → import → secuencia → export preset "Social Vertical 1080×1920" → `05_RENDERS_DRAFT/TEST_filmcraft_9x16_v01.mp4` (H.264, 1080×1920, 25 fps, 5 s, verificado con ffprobe). Cada ejecución del CLI arranca un proyecto vacío: importar, editar y exportar van en un solo guion `run`. No probado: por MCP, con clip de propiedad real, con audio |
| Python | OBSERVADO: 3.12.10 instalado 2026-11-12 vía winget (`Python.Python.3.12`, scope usuario) | `python --version` |
| Auto-Editor | OBSERVADO: 29.3.1 (licencia Unlicense) instalado con pip; `Scripts` añadido al PATH de usuario | `auto-editor --version` |
| Whisper | Usar el integrado de FilmCraft (Rust, CPU). No se instaló `faster-whisper`/`openai-whisper` aparte (PyTorch pesa varios GB y C: tiene ~8 GB libres) | ver OPEN_QUESTIONS #10 |
| DaVinci Resolve | NO INSTALADO a propósito: gratis pero no open-source, exige GPU y espacio que C: no tiene; FilmCraft + FFmpeg cubren el stack aprobado | reconsiderar si se libera C: |
| REconnect | NO CONECTADO | export/API PENDIENTE |
| Meta Business Suite | Lo usa Nixon para programar | — |
| Meta Marketing API / Google Ads API | NO CONECTADO | Fase 4 |
| Repos hermanos: Buscabot-NBS, santa-isabel-sitio, santa-isabel-media-ops | HISTÓRICO (vistos el 8-nov) | no auditados aún |
| Chat previo «PublicaBOT» | NO ENCONTRADO | Nixon lo traerá |
