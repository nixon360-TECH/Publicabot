# Handoff para desarrolladores — PublicaBOT

**Para quién:** un desarrollador que no ha usado la PC de Nixon ni los chats con los agentes. Aquí está qué se hizo, con qué herramienta, en qué archivo del repo vive y cómo se propone convertirlo en una aplicación.

**Plan de producto y negocio (página web):** https://claude.ai/artifact/NUktM7NVQrHoSChQsYtmTn
Se abre con el enlace. Si no puede abrirla, pídale acceso a Nixon. Este archivo trae lo esencial.

**Fecha:** 13 nov. 2026 · **Rama:** `feature/N360-029-handoff-dev`

---

## 1. Qué es PublicaBOT, en una frase
Un flujo que convierte tomas reales (dron, celular, fotos) y datos verificados de una propiedad en videos y artes listos para Instagram, Facebook y WhatsApp. El caso piloto es la **Lotificación Santa Isabel** (Comacarán, San Miguel, El Salvador). Hoy funciona como un conjunto de scripts que operan agentes de IA. La meta es una webapp de autoservicio.

## 2. Leer primero
| Archivo | Para qué |
|---|---|
| `AGENTS.md` | Límites duros: no publicar sin aprobación, no inventar datos, no subir medios ni secretos, trabajar en ramas |
| `NIXON360_CONTEXT_MASTER.md` | Contexto completo del negocio (sección 0 obligatoria; §11 lista los datos que no se publican) |
| `docs/style/STYLE_DECISIONS.md` | Cómo se ve, suena y se edita todo |
| `docs/tools/VIDEO_STACK.md` | Herramientas de video evaluadas (FilmCraft, Remotion, FFmpeg) y por qué |
| `coordination/MULTI_AGENTE_REGLAS.md` | Cómo se reparte el trabajo entre Claude Code, Codex y ChatGPT |
| `docs/context/SANTA_ISABEL_CONTEXTO_2026-11-12.md` | Contexto del proyecto piloto |
| `policies/publishing_policy.yaml`, `policies/cost_budget.yaml` | Reglas de publicación y de gasto |

**Importante:** los medios (videos originales, fotos, música, renders) **no están en el repo**, por regla. Viven en un disco externo definido como `MEDIA_ROOT` (ver `.env.example`). Los scripts tienen rutas absolutas de la PC original en sus primeras líneas (`BASE`, `FF`, `VOCES`, etc.); para correrlos en otra máquina hay que cambiarlas.

## 3. Cómo se fue dando el proceso (y con qué herramienta)

### Paso 1 · Reglas y datos verificados
- Antes de producir nada se fijaron los datos que **sí** se pueden decir: desde US$24,500, desde 286 v², con escritura, agua conectada, frente al Instituto Nacional de Comacarán, cerca del parque central, financiamiento Banco Industrial* (con aviso). Se fijaron también los que **no**: reserva, luz, negociación, comisiones.
- **Herramienta:** skill `property-fact-check` (`.claude/skills/property-fact-check/`).
- **Archivos:** `brands/santa-isabel/contenido_v03/property_snapshot.json` (ficha), `brands/santa-isabel/contenido_v03/puntos_confirmados.json` (calles, lugares, frases confirmadas por Nixon, segmentos).

### Paso 2 · Revisión de tomas
- Se revisaron las tomas de dron de dos vuelos (julio y octubre) y de un tercer día de grabación. Se hicieron hojas de contacto y proxies SDR 9:16 para trabajar rápido sin tocar los originales.
- **Herramientas:** FFmpeg/ffprobe, Python. La cola nocturna de proxies es `brands/nixon-remax/motion_kit/cola_noche.py`.
- **Lección:** los originales son de solo lectura. Nunca se renombran ni se sobrescriben.

### Paso 3 · Kit de marca y movimiento único
- Todos los videos debían verse idénticos: mismo estilo de texto, pines, contornos, logos y cierre. Se definió un solo kit.
- Estilo "texto en capas" con cuatro roles: conector en cursiva, texto claro, acento amarillo y protagonista con degradado azul y contorno. Se aclararon los azules porque se veían negros.
- **Archivos:** `brands/nixon-remax/motion_kit/kit_nixon_remax.json` (colores, estilos, medidas por plataforma, zonas seguras), `brands/nixon-remax/design_dna_texto_viral.md` (de dónde sale el estilo), `brands/santa-isabel/brand.yaml`, `brands/santa-isabel/palette.json`.
- **Herramientas:** skills `design-dna` y `motion-design`.

### Paso 4 · Cierre del video (tarjeta final)
- Hubo cinco iteraciones con Nixon. La aprobada (v5): teléfono arriba, logo de RE/MAX grande y centrado, logo de Banco Industrial blanco con sombra a la izquierda, foto recortada del agente con su nombre pequeño a la derecha, y la lotificación de fondo.
- **Archivos:** `brands/nixon-remax/motion_kit/mock_kit.py` (función `cierre_v5`; las versiones anteriores siguen ahí como historial), `brands/nixon-remax/motion_kit/recorte.py` (recorte de la foto con **rembg**, modelo `u2net_human_seg`).

### Paso 5 · Fotos limpias y ubicación
- Regla de Nixon: **nunca usar fotos con calles de tierra o sucias en artes**, solo las editadas con calles limpias (y nunca una que se vea falsa).
- Nixon marcó sobre cuadrículas dónde está cada cosa: calles de la lotificación (Isabel Poniente, Los Colibríes, Isabel Sur, Isabel Oriente), camino al río, calle al Jicaral, parque central e instituto. Con eso se trazaron a mano las calles (polilíneas con brillo amarillo) y los pines.
- Se intentó detectar las calles por color (HSV) y falló: bordes irregulares y poca cobertura. Por eso se usa el trazo manual.
- **Archivos:** `brands/nixon-remax/motion_kit/paneo_foto.py`, `brands/nixon-remax/motion_kit/video2_fotos.py`, `brands/nixon-remax/motion_kit/fotos_limpias_motion.json`, `scripts/render_fotos_limpias.py`, `docs/tools/FOTOS_LIMPIAS_MOTION.md`, `tests/test_photo_motion.py`.
- **Investigado y descartado:** generar video con IA local (WanGP) porque la PC no tiene GPU, y limpiar calles en video con FilmCraft porque no tiene relleno generativo.

### Paso 6 · Primer video bueno y la regla de "video que vende"
- El primer video aceptable fue el de 30 s con tomas de julio. Nixon rechazó las versiones que solo decían "calles asfaltadas". La regla quedó así: **todo video dice nombre, ubicación, precio desde, tamaño desde, cercanía al instituto y al parque, escritura, agua, financiamiento* y llamada a la acción.**
- Otras correcciones: más tiempo en pantalla (30 s), quitar el logo de la lotificación del cuerpo porque tapaba los pines, y en las escenas de pines mostrar solo pines.
- **Archivos:** `brands/nixon-remax/motion_kit/video_build_v05.py` (el original; define fuentes, `Block`, `Counter`, `draw_style`, logos), `video_build_v06.py`, `mk_v06.py`, `docs/plan/PLAN_8_VIDEOS_SANTA_ISABEL.md`.

### Paso 7 · Un cuerpo, muchos ganchos (12 videos)
- Estructura fija de 30 s: gancho 0–4 s · ubicación con pines 4–11 · foto limpia con calles trazadas 11–19 · contador de precio y aviso del banco 19–25 · cierre 25–30.
- Se renderiza por partes (gancho y cuerpo) y se unen con `ffmpeg -c copy`. Cambiar la música es solo remezclar el audio (segundos). Cambiar un gancho obliga a renderizar solo esa parte (minutos).
- Ganchos por tipo de cliente y por "convencimiento" (C1 precio … C9 prueba visual). Resultaron 12 versiones: A, B, C, D, E, F, G1, G2, G4, H1, H2 y H3. Las H son del segmento "hermano lejano" (salvadoreños en el exterior, en tú).
- **Archivos:**
  - `brands/nixon-remax/motion_kit/video_venta.py`: set 1 (A, B, C).
  - `brands/nixon-remax/motion_kit/video_venta2.py`: D, E, F, G1, G4, H1–H3, con tomas distintas y "listos para construir".
  - `brands/nixon-remax/motion_kit/video_venta3.py`: G2, "Tres preguntas".
  - `brands/nixon-remax/motion_kit/guiones_ganchos_propuestos_v1.md`: ganchos propuestos y aprobados.
  - `brands/santa-isabel/contenido_v03/SEGMENTOS_DE_CLIENTE_propuesta.md`: 8 tipos de cliente.
- **Detalle técnico:** los `video_venta*.py` leen `video_build_v05.py` hasta `def C(k` y lo ejecutan con `exec` para reutilizar fuentes y bloques. Funciona, pero es lo primero que hay que convertir en un módulo importable.
- **Herramientas:** Python 3.12, numpy, Pillow, OpenCV, FFmpeg (libx264 CRF 17, 25 fps, 1080×1920, bt709).

### Paso 8 · Música
- Una pista distinta por versión, de Pixabay (licencia Pixabay Content License). Varias pistas tienen registro de Content ID. Las fuentes, hashes y licencias están en `brands/santa-isabel/contenido_v03/rights_and_sources.md`.
- Mezcla: recorte y fundidos, voz con ducking por sidechain, loudnorm I=−14 TP=−1.5 y AAC 192k.
- **Archivos:** `brands/nixon-remax/motion_kit/ensamblar_venta.py` (sets 1 y 2), `mezclar_voces.py` (ensamblador final de los 12), `mezcla_video2.py`.

### Paso 9 · Voz de Nixon
- La idea: Nixon lee **viendo el video**, con la frase actual resaltada, y un programa coloca cada frase en su segundo.
- **Intentos:**
  1. El teleprompter con tiempos no le sirvió.
  2. La página "ver y leer" dependía de un servidor local y al cerrarlo dejaba de cargar los videos. Se cambió a rutas relativas que abren sin servidor.
  3. Nixon terminó grabando con WhatsApp en el celular (.mp4 de audio), que es lo más natural para él.
- **Alineación** (`alinear_voz.py`): detecta frases por silencios con numpy y FFmpeg, sin internet, y elige los cortes cuyo largo se parece más al del texto. Coloca cada frase en su segundo y acelera hasta ×1.30 si no cabe. Si la detección falla, acepta un archivo `cortes_<ID>.json` con los cortes a mano. **En 2 de 3 tomas hubo que fijar los cortes a mano**, porque Nixon agrega frases que no están en el guion ("listas para disfrutar"). La mejora pendiente es usar Whisper con tiempos por palabra; su instalación quedó sin aprobar.
- **Archivos:**
  - `brands/nixon-remax/motion_kit/guiones_voz.py`: única fuente de los 12 guiones. Genera `brands/santa-isabel/contenido_v03/guiones_voz.json` y `GUIONES_PARA_LEER.md`.
  - `teleprompter_plantilla.html` y `guion_con_video_plantilla.html`.
  - `alinear_voz.py`, `prueba_voz_sintetica.py` (prueba con la voz TTS de Windows) y `COMO_GRABAR_LA_VOZ.md`.
- **Resultado:** A, B y C ya tienen la voz de Nixon y quedaron como finales. Los otros 9 solo tienen música.

### Paso 10 · Artes (Codex)
- Codex hizo 41 artes (22 de feed 4:5, 15 historias 9:16 y 7 de pauta) con calendario de 15 días, la paleta azul y amarilla del sitio web, y el logo original.
- Los carruseles son D02_recorrido (4 láminas), D06_visita (3) y D11_preguntas (3). El resto son de una lámina.
- **Archivos:** `scripts/codex_artes_15d.py`, `scripts/codex_identidad_santa_isabel.py`, `brands/nixon-remax/codex_campana_15_dias.json`, `docs/tools/CODEX_ARTES_SANTA_ISABEL.md`, `docs/tools/SANTA_ISABEL_PALETA_AZUL.md`.

### Paso 11 · Textos (ChatGPT)
- ChatGPT recibe instrucciones con los datos permitidos, el tono (de usted; en tú solo para hermano lejano) y un encabezado obligatorio de "tipo de convencimiento". Con eso produce carruseles, posts, historias, ganchos y respuestas de WhatsApp.
- **Archivos:** `coordination/HANDOFF_CHATGPT_SANTA_ISABEL.md` (ronda 1), `coordination/HANDOFF_CHATGPT_CONTENIDO_2.md` (ronda 2, con la taxonomía C1–C9).

### Paso 12 · Entrega (modo HANDOFF)
- Nada se publica automáticamente. El sistema entrega el paquete (video, portada, copy, hashtags y checklist) y Nixon lo programa en Meta Business Suite. Se organizó una carpeta de Drive por red social (Reels/Historias 9:16, Feed 4:5, Pauta) con un índice.
- **Herramientas:** skill `prepublish-qa` (obligatoria antes de `READY_FOR_REVIEW`).

### Herramientas de agentes (no son parte del producto)
- **Skills** en `.claude/skills/`: `property-fact-check`, `property-reel`, `prepublish-qa`, `organic-reel-edit`, `filmcraft-edit`, `threejs-scenes`, `gsap-motion`, `design-dna`, `motion-design`, `genjutsu-polish` y `antislop` (MIT; su origen está en `.claude/skills/antislop/ORIGEN.md`).
- **Fuera del repo:** claude-mem, memoria persistente para Claude Code, instalada en la PC de Nixon.

## 4. Estado al 13 nov. 2026
| Pieza | Estado |
|---|---|
| 12 videos 9:16 de 30 s | Renderizados. A, B y C con voz y aprobados; los demás esperan voz y revisión |
| 41 artes | Hechos por Codex. Las fechas del calendario hay que correrlas |
| Versiones 4:5 de los videos, portadas y copy por video | Pendiente |
| Whisper para alinear voz | Propuesto, sin aprobar |
| Nueva paleta del sitio web | Aplicada en artes. Falta adaptar el kit de video si cambia |

## 5. Guía breve: cómo implementar la app a partir de este flujo
La propuesta completa (precios, plan de 6 meses, riesgos) está en la página del plan. Lo técnico, resumido:

**Flujo del usuario = los pasos de arriba, automatizados**
1. **Marca** (paso 3–4) → formulario que produce un `kit.json` con la forma de `kit_nixon_remax.json` + recorte automático de la foto (rembg).
2. **Ficha** (paso 1) → formulario con campos obligatorios. Se valida con código, no con IA, como en `property_snapshot.json`. Si falta un dato, se bloquea la exportación.
3. **Tomas** (paso 2) → subida a almacenamiento de objetos. Un worker hace los proxies SDR 9:16, como `cola_noche.py`.
4. **Cliente y convencimiento** (paso 7) → selectores con los 8 segmentos y C1–C9.
5. **Ganchos y guion** (paso 7, 11) → Claude API con la ficha como única fuente de datos. El texto pasa por el validador.
6. **Render** (pasos 5–8) → workers Python + FFmpeg en contenedores. Gancho y cuerpo por separado, para reutilizar el cuerpo.
7. **Voz** (paso 9) → grabar en el navegador o en el celular mientras corre el video, y alinear en el servidor (Whisper por palabra + la lógica de `alinear_voz.py`).
8. **Paquete** (paso 12) → 9:16, 4:5, portada, copy y checklist `prepublish-qa`. Se publica a mano; la API de Meta viene después.

**Arquitectura sugerida:** Next.js (PWA) → FastAPI (Python) → Postgres + Redis (cola) → workers de render y voz → S3/Cloudflare R2. Claude API para textos.

**Primer trabajo técnico (semanas 1–6):**
1. Convertir `video_build_v05.py` + `video_venta*.py` en un paquete importable, sin `exec` ni rutas fijas, que reciba JSON (marca + ficha + tomas + guion) y devuelva un MP4.
2. Prueba de paridad: reproducir A, B y C desde la API con el mismo resultado visual.
3. Reemplazar lo que no se puede usar en un servicio comercial: fuentes de Microsoft (Georgia, Segoe UI, Impact) por fuentes libres, y música de Pixabay por una biblioteca con licencia para apps. Revisar también la licencia de Remotion si se usa con más de 3 personas.
4. Alineación de voz con Whisper, con la meta de cero cortes manuales en las 3 voces reales.
5. Mover el producto a un **repo privado**. Este repo es público.

## 6. Reglas que no cambian en la app
- No inventar datos y omitir lo no verificado.
- Avisos legales fijos (financiamiento sujeto a evaluación del banco, sujeto a disponibilidad).
- Nada se publica ni se gasta sin aprobación del usuario.
- No usar voz ni avatar de una persona sin su autorización.
- Nunca se suben al repo medios originales, secretos ni datos de clientes.
