# VIDEO_STACK — herramientas de edición (investigación 2026-11-12)

Estado: **CONFIRMADO_USUARIO (2026-11-12)**: Nixon aprueba FilmCraft + Remotion + FFmpeg y produce como individuo (licencia gratuita de Remotion). Todas las herramientas son gratuitas. Ninguna está instalada todavía.

## Hallazgo principal: ArtCraft "Crafting Apps" (storytold)
Es una suite open-source escrita en Rust, con licencia dual Apache-2.0 + MIT. Corre en Windows, macOS, Linux y navegador.
**Todas las apps exponen un servidor MCP**: Claude Code las maneja con comandos, igual que un editor humano, sin necesidad de clics.

| App | Equivale a | Uso en PublicaBOT | MCP / CLI |
|---|---|---|---|
| **FilmCraft** (`storytold/filmcraft`) | Premiere | Corte, armado, color, audio y export H.264 1080×1920 | ✓ `filmcraft-cli mcp` (headless o bridge) |
| **EffectCraft** | After Effects | Texto animado y motion graphics (efectos tipo R2/R4) | ✓ `.mcp.json` + CLI |
| **LightCraft** | Lightroom | Revelado y retoque natural de fotos de propiedades | ✓ CLI + MCP |
| **PhotoCraft** | Photoshop | Portadas, carruseles, etiquetas «Ambientación ilustrativa» | ✓ CLI + MCP |

**FilmCraft, observado en su repo (commit del 2026-11-11):**
- Tiene Whisper integrado (Rust puro, CPU), con transcripción palabra por palabra y etiquetado de quién habla.
- Tiene TTS integrado (voces Kokoro-82M, locales). **No clona voces.**
- Subtítulos: importa y exporta SRT y VTT, con quemado en el video. **No trae subtítulos animados palabra por palabra estilo TikTok.**
- Exporta H.264 y AAC en MP4 con codificador propio, con preset vertical 1080×1920.
- **Estado: ALPHA.** Su propio roadmap dice que la beta está a unas 400–700 h de trabajo. Lo usamos con plan B (FFmpeg) para cualquier pieza con fecha.
- La IA generativa en la nube de ArtCraft es **de pago** y queda fuera. Los editores son gratis.

## Las tres maneras de editar (y cuándo usar cada una)

| Vía | Cómo funciona | Fuerte en | Débil en | Costo |
|---|---|---|---|---|
| **A. FilmCraft/EffectCraft por MCP** | El agente opera el editor: importa, corta, aplica color y exporta | Clips reales de Nixon, dron, ajustes finos que Nixon puede abrir y retocar a mano | Alpha; subtítulos virales limitados | Gratis (Apache/MIT) |
| **B. Remotion** (React → video) | El agente escribe la plantilla como código y la renderiza | Plantillas repetibles de propiedad, **subtítulos animados**, texto que cambia con el fondo (`mix-blend-mode`) | Hay que programar la plantilla la primera vez | **Gratis para individuos y empresas de hasta 3 personas**; si no, licencia de empresa |
| **C. FFmpeg + subtítulos ASS** | Cortes y subtítulos karaoke por línea de comandos | Robusto, rápido, sirve de respaldo y para QA | Menos flexible en diseño | Gratis (LGPL/GPL) |

## Recomendación (PROPUESTO)
1. **FilmCraft** como editor principal del material de Nixon y del dron: corte, color y audio, siempre con un proyecto `.fcproj` editable.
2. **Remotion** para la capa de diseño: subtítulos dinámicos palabra por palabra, texto con mezcla (ref R2), precio/zona y CTA. Plantillas fijas `PROPERTY01` y `ORGANIC01`.
3. **FFmpeg** como respaldo si FilmCraft falla, y para el QA técnico (ffprobe).
4. **LightCraft o PhotoCraft** para fotos y portadas.
5. Piloto: **Lotificación Santa Isabel** (tomas de dron y fotos reales), aplicando las restricciones del master §11.

## Riesgos y bloqueos
- Licencia de Remotion: Nixon califica como individuo. **Si la pieza la produce o paga una empresa de más de 3 personas, se requiere licencia de empresa.** CONFIRMAR antes de producir para terceros.
- FilmCraft en alpha: probar primero con un clip de prueba. Nunca editar sobre originales.
- Skills de terceros: el repo `remotion-dev/skills` no tenía archivo de licencia (según una fuente del 2-nov-2026). Se instalan con su comando oficial en la PC y no se copian dentro de este repo.

## Descartado
| Herramienta | Motivo |
|---|---|
| Higgsfield, ArtCraft Cloud AI | De pago |
| CapCut | Términos comerciales a revisar; no es open-source |
| SaaS de subtítulos (Submagic, etc.) | De pago; Remotion o FFmpeg hacen lo mismo localmente |

## Fuentes
- github.com/storytold/filmcraft: README, ROADMAP.md, docs/agents.md, crates/speech, crates/tts, crates/captions
- github.com/storytold/{effectcraft,lightcraft,photocraft}: AGENTS.md, .mcp.json, CLI
- remotion.dev/docs/license/faq y remotion.dev/docs/terms
- remotion.dev/templates/tiktok (subtítulos palabra por palabra con Whisper.cpp)
