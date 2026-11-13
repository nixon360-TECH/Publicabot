# Handoff detallado — flujo completo de PublicaBOT (caso Santa Isabel)

**Para quién:** un desarrollador o un agente de IA que no ha usado la PC original ni los chats anteriores. Quiere entender el flujo, **replicarlo en otra máquina** o **escalarlo a una aplicación**.
**Fecha:** 13 nov. 2026 · **Rama:** `feature/N360-029-handoff-dev`

**Documentos relacionados:**
- `docs/HANDOFF_DESARROLLADOR.md`: resumen de los 12 pasos y guía de la app.
- Plan de producto y negocio: https://claude.ai/artifact/NUktM7NVQrHoSChQsYtmTn

**Este documento** baja todo a nivel operativo: qué entra, qué script corre, qué sale, dónde se guarda y qué falla.

Todas las rutas son **relativas al repo** o a `<MEDIA_ROOT>`, la carpeta de medios que se define en `.env` (ver `.env.example`).

---

## 0. Reglas que no se negocian
- **No se publica nada automáticamente** (modo HANDOFF). El sistema entrega un paquete; el dueño lo revisa y lo programa en Meta Business Suite. Publicar, enviar WhatsApp o gastar requiere aprobación explícita por versión. Ver `AGENTS.md` y `policies/publishing_policy.yaml`.
  - El dueño del proyecto anunció que quiere cambiar las reglas de distribución más adelante. Hasta que lo haga, rigen las actuales.
- **No se inventan datos.** Solo se usa lo que está en `brands/santa-isabel/contenido_v03/property_snapshot.json` y `puntos_confirmados.json`.
  - Prohibido: reserva o apartado, electricidad, mínimos de negociación, comisiones, cuotas, fechas, plusvalía, "lujo" y "exclusivo".
  - Avisos fijos: "\*Financiamiento con Banco Industrial sujeto a evaluación del banco." y "Sujeto a disponibilidad."
- **Tono:** a los clientes se les trata de usted. El segmento "hermano lejano" (salvadoreños en el exterior) va de tú, por decisión del dueño.
- **Medios fuera de Git.** Los originales en `<MEDIA_ROOT>/01_ORIGINALS_READONLY` son de solo lectura.
- **Este repo es público.** No subir medios, secretos ni datos de clientes.

## 1. Requisitos para replicarlo
| Componente | Uso |
|---|---|
| Python 3.12 | Todos los scripts |
| `numpy`, `Pillow`, `opencv-python` | Render de cuadros, trazos de calles con brillo, desenfoques |
| `rembg` (modelo `u2net_human_seg`) | Solo para recortar la foto del agente (`recorte.py`) |
| FFmpeg y ffprobe | Codificar (libx264 CRF 17, 25 fps, 1080×1920, bt709), unir partes, mezclar audio, cambiar tempo |
| Fuentes | Georgia, Segoe UI, Arial Nova Cond e Impact (de Windows). **No sirven para un producto comercial:** hay que cambiarlas por fuentes libres |
| Navegador | Para la página de grabación de voz |

No hace falta GPU: todo corre en CPU. Se probó generar video con IA local y se descartó porque la máquina no tenía GPU.

### Rutas fijas que hay que cambiar
Los scripts de `brands/nixon-remax/motion_kit/` se escribieron para una sola PC y tienen rutas absolutas de Windows en sus primeras líneas. Para correrlos en otra máquina hay que cambiar estas variables:

| Variable | Qué es | Dónde está |
|---|---|---|
| `FF` | Ruta del ejecutable de FFmpeg | `video_build_v05.py`, `alinear_voz.py`, `ensamblar_venta.py`, `mezclar_voces.py` |
| `ROOT`, `BASE`, `B` | `<MEDIA_ROOT>` y la carpeta del proyecto | Casi todos |
| `VOCES` | Carpeta de las voces | `alinear_voz.py`, `mezclar_voces.py` |
| `LOGOS`, `PHOTO`, `BG_CIERRE` | Logos, fotos limpias y fondo del cierre, en una carpeta de marca fuera de `<MEDIA_ROOT>` | `video_build_v05.py`, `video_venta*.py` |
| `sys.path.insert(... _KIT)` | En la PC original, `mock_kit.py` vivía en una carpeta `_KIT` aparte. **En el repo está en el mismo `brands/nixon-remax/motion_kit/`**, así que esa línea se puede borrar | `video_venta*.py`, `video2_fotos.py`, `mk_v06.py`, `video_build_v06.py` |
| `FONTS`, `SEG`, `SEGR`, `GEOB` | Rutas de las fuentes del sistema | `video_build_v05.py` |
| Rutas de entrada y salida | Foto del agente y destino del recorte | `recorte.py` |
| `SM`, `PROX` | Carpeta de las tomas originales y carpeta de los proxies | `cola_noche.py` |

**Primera tarea recomendada:** juntar todo en un `config.py` que lea `MEDIA_ROOT` del `.env`.

## 2. Estructura de `<MEDIA_ROOT>` (por proyecto)
El ID del proyecto piloto es `N360-20261112-0001`.

| Carpeta | Qué contiene |
|---|---|
| `00_INBOX/<ID>/` | Material que llega: pistas de música (.mp3) y `voces/` |
| `00_INBOX/<ID>/voces/` | `vo_<VIDEO>.<ext>` (voz cruda), `cortes_<VIDEO>.json` (cortes manuales opcionales) y `vo_<VIDEO>_alineada.wav` (resultado) |
| `01_ORIGINALS_READONLY/` | Tomas originales de dron y celular. Nunca se modifican |
| `02_PROXIES/` | Versiones livianas SDR 9:16 para trabajar rápido |
| `04_PROJECTS_EDITABLE/<ID>/` | Ficha, guiones y páginas HTML de grabación |
| `04_PROJECTS_EDITABLE/<ID>/build/` | Scripts en ejecución y `parts/` (ganchos y cuerpos mudos) |
| `05_RENDERS_DRAFT/<ID>/` | Videos en calidad completa: `N360_REMAX_PROPERTY_SANTAISABEL_REEL_9x16_venta_<VIDEO>_v03.mp4` |
| `06_REVIEW_PREVIEWS/<ID>/` | Versiones livianas para revisar: `preview_low_venta_<VIDEO>_v03.mp4` |
| `07_VIDEOS_FINALES/` | Finales con voz y nombre claro: `<VIDEO>_<gancho_corto>_CON_VOZ.mp4` |
| `10_DRIVE_<PROYECTO>/` | Copia que se sube a Google Drive, organizada por uso (ver paso 12) |

**Carpeta de marca** (fuera de `<MEDIA_ROOT>`, una por desarrollo inmobiliario):
- `01_logos/`
- `03_personas/`: foto del agente.
- `fotos_limpias/`: fotos aéreas editadas con las calles limpias, con nombres `SI_FOTO_<nombre>_v01.jpg`.

## 3. El flujo completo, paso a paso

### Paso 1 · Datos verificados (entrada obligatoria)
- **Entra:** la información del vendedor o del desarrollador.
- **Proceso:** se valida campo por campo. Lo que no está confirmado no se usa. Herramienta: skill `.claude/skills/property-fact-check/`.
- **Sale:**
  - `property_snapshot.json`: precio desde, tamaño desde, escritura, agua, financiamiento y contacto.
  - `puntos_confirmados.json`: nombres de calles, lugares cercanos, frases del dueño y segmentos.
  - Los dos están en `brands/santa-isabel/contenido_v03/`.
- **En la app:** un formulario con campos obligatorios y un **validador hecho con código**, no con LLM. Si falta un dato, se bloquea la exportación.

### Paso 2 · Tomas y proxies
- **Entra:** videos de dron y de celular, y fotos.
- **Proceso:** ffprobe para leer metadatos y hojas de contacto para elegir las tomas. Luego proxies SDR 9:16 en una cola nocturna: `brands/nixon-remax/motion_kit/cola_noche.py`.
  - Corre las tareas una tras otra y mantiene la PC despierta mientras trabaja.
  - Registra el estado en `cola_estado.json` y el registro en `cola_log.txt`.
- **Lección:** algunas tomas son HDR. La cola las convierte a SDR con un filtro aparte (`vf_hdr`) antes de trabajarlas.

### Paso 3 · Kit de marca
- **Archivo central:** `brands/nixon-remax/motion_kit/kit_nixon_remax.json`. Define colores, estilos de texto, tamaños por plataforma y zonas seguras.
  - 9:16: 250 px libres arriba y 350 px abajo.
  - 4:5: 120 px arriba y 160 px abajo.
- **Estilo "texto en capas"**, con cuatro roles:
  - `conn`: conector en cursiva (Georgia).
  - `light`: texto claro (Segoe UI Black).
  - `accent`: acento amarillo (Arial Nova Cond).
  - `protag`: protagonista con degradado azul y contorno (Impact).
- **Otros archivos:**
  - `brands/nixon-remax/design_dna_texto_viral.md`: de dónde sale el estilo.
  - `brands/santa-isabel/brand.yaml` y `brands/santa-isabel/palette.json`.
- **En la app:** un formulario de marca que produce un JSON con la misma forma.

### Paso 4 · Cierre (tarjeta final)
- `brands/nixon-remax/motion_kit/mock_kit.py`, función `cierre_v5`. Las versiones anteriores quedan en el mismo archivo como historial.
- **Contenido:** teléfono arriba, logo de RE/MAX centrado, logo del banco blanco con sombra a la izquierda, foto recortada del agente con su nombre a la derecha y la lotificación de fondo.
- **Recorte del agente:** `brands/nixon-remax/motion_kit/recorte.py`, con rembg `u2net_human_seg`.

### Paso 5 · Fotos limpias y ubicación
- **Regla:** nunca mostrar calles de tierra o sucias. Solo fotos editadas con calles limpias que no se vean falsas.
- **Ubicación:** el dueño marcó sobre cuadrículas dónde está cada calle y lugar. Con eso se trazaron a mano polilíneas con brillo amarillo (OpenCV `polylines` + `GaussianBlur`) y pines.
- **Archivos:**
  - `brands/nixon-remax/motion_kit/paneo_foto.py` y `brands/nixon-remax/motion_kit/fotos_limpias_motion.json`.
  - `scripts/render_fotos_limpias.py`, con su prueba en `tests/test_photo_motion.py`.
  - Documentación: `docs/tools/FOTOS_LIMPIAS_MOTION.md`.
- **Descartado:**
  - Detectar las calles por color (HSV): bordes irregulares.
  - Video con IA local: no había GPU.
  - Limpiar calles en FilmCraft: no tiene relleno generativo.
- **En la app:** el usuario hace clic sobre la foto para marcar pines y calles, y el resultado se guarda como JSON de puntos.

### Paso 6 · La regla del "video que vende"
- Todo video dice, en 30 s:
  - nombre del proyecto y ubicación;
  - precio **desde** y tamaño **desde**;
  - cercanía (instituto y parque);
  - escritura, agua y financiamiento*, con su aviso;
  - llamada a la acción con el WhatsApp.
- Se rechazaron versiones que solo decían "calles asfaltadas".
- **Motor base:** `brands/nixon-remax/motion_kit/video_build_v05.py`. Define fuentes, `Block`, `Counter`, `draw_style` y logos.
- **Plan:** `docs/plan/PLAN_8_VIDEOS_SANTA_ISABEL.md`.

### Paso 7 · Un cuerpo, muchos ganchos (12 videos)
**Estructura fija de 30 s:**

| Tiempo | Contenido |
|---|---|
| 0–4 s | Gancho |
| 4–11 s | Ubicación con pines |
| 11–19 s | Foto limpia con calles trazadas |
| 19–25 s | Contador de precio y aviso del banco |
| 25–30 s | Cierre |

**Render por partes mudas.** Cada parte es un MP4 sin audio en `build/parts/`:

```bash
python video_venta.py hookA        # -> parts/hookA_mudo.mp4   (también hookB, hookC, body)
python video_venta2.py hookD       # -> parts/v2_hookD_mudo.mp4 (hookE, hookF, hookG1, hookG4, hookH1, hookH2, hookH3, body2b)
python video_venta3.py hookG2      # -> parts/v3_hookG2_mudo.mp4 (y body)
```

- Los `video_venta*.py` leen `video_build_v05.py` hasta `def C(k` y lo ejecutan con `exec` para reutilizar sus funciones. **Es lo primero que hay que volver un módulo importable.**
- **Costos de tiempo:** cambiar un gancho obliga a renderizar solo esa parte (minutos). Cambiar la música o la voz es solo remezclar el audio (segundos).

**Los 12 videos:**

| Video | Gancho | Tipo de convencimiento | Partes |
|---|---|---|---|
| A | ¿Busca dónde construir su nueva casa en San Miguel? | C8 acción + C4 ubicación | hookA + body |
| B | Paz y tranquilidad, a minutos de la ciudad | C5 tranquilidad | hookB + body |
| C | Terrenos desde US$24,500 en Comacarán | C1 precio | hookC + body |
| D | ¿Sueña con su casa propia en San Miguel? | C5 | v2_hookD + v2_body2b |
| E | Terrenos desde 286 v² en Comacarán | C6 facilidad | v2_hookE + v2_body2b |
| F | Escritura · Agua conectada · Calles asfaltadas | C2 legal + C3 servicios | v2_hookF + v2_body2b |
| G1 | ¿Cuánto cuesta un terreno en Comacarán? | C1 | v2_hookG1 + v2_body2b |
| G2 | Tres preguntas antes de comprar un terreno | C2 + C3 + C1 | v3_hookG2 + v3_body |
| G4 | ¿Y al comprar me dan mi escritura? | C2 | v2_hookG4 + v2_body2b |
| H1 | Hermano lejano, tu terreno en San Miguel te espera | C7 pertenencia | v2_hookH1 + v2_body2b |
| H2 | ¿Vive fuera del país? Tu terreno en Comacarán, San Miguel, ¡te espera! | C7 | v2_hookH2 + v2_body2b |
| H3 | Hermano lejano, ¿qué haces con $24,500 en El Salvador? ¡Compras tu primer lote para tu casa! | C7 + C1 | v2_hookH3 + v2_body2b |

- La tabla de los tipos de convencimiento (C1–C9) está en `coordination/HANDOFF_CHATGPT_CONTENIDO_2.md`, sección 4.
- Los 8 tipos de cliente están en `brands/santa-isabel/contenido_v03/SEGMENTOS_DE_CLIENTE_propuesta.md`.
- Los ganchos aprobados están en `brands/nixon-remax/motion_kit/guiones_ganchos_propuestos_v1.md`.

### Paso 8 · Música
- Una pista distinta por video, de Pixabay. Ver el diccionario `V` en `brands/nixon-remax/motion_kit/mezclar_voces.py`: video → (gancho, cuerpo, pista, segundo de inicio).
- Las fuentes, los hashes y la licencia están en `brands/santa-isabel/contenido_v03/rights_and_sources.md`.
- **Licencia:** varias pistas tienen registro de Content ID, y la licencia de Pixabay **no sirve para un SaaS**. Hay que cambiarla por una biblioteca con licencia para apps.

### Paso 9 · Voz del agente (probado con 3 grabaciones reales)
1. **Guiones.** La única fuente es `brands/nixon-remax/motion_kit/guiones_voz.py`. Genera `guiones_voz.json` (12 guiones de 7 líneas cada uno, con el segundo en que entra cada línea), `GUIONES_PARA_LEER.md` y las dos páginas HTML a partir de sus plantillas.
   - Las copias en `brands/santa-isabel/contenido_v03/` se actualizan a mano.
2. **Grabación.**
   - **Página:** `guion_con_video_plantilla.html`, una vez generada. Reproduce la vista previa del video elegido y resalta la línea que toca.
   - **Video:** lo carga con una **ruta relativa** a `06_REVIEW_PREVIEWS/<ID>/preview_low_venta_<VIDEO>_v03.mp4`, así que no necesita servidor.
     - **Por qué:** una versión anterior dependía de `python -m http.server` y dejaba de cargar los videos al cerrarse el servidor.
     - **No probado:** el arreglo con ruta relativa no se ha probado en un navegador.
   - **El teleprompter con tiempos** (`teleprompter_plantilla.html`) no le sirvió al agente.
   - **Forma real de grabar:** el agente grabó una nota de voz con **WhatsApp** en el celular mientras veía el video y la descargó en la PC. El archivo llega como `.mp4` de audio. Para la app, la lección es dejar grabar desde el celular, de forma natural.
   - Instrucciones para quien graba: `brands/nixon-remax/motion_kit/COMO_GRABAR_LA_VOZ.md`.
3. **Ubicación del archivo.** El audio se copia como `<MEDIA_ROOT>/00_INBOX/<ID>/voces/vo_<VIDEO>.mp4`. Se acepta cualquier extensión, porque el script busca `vo_<VIDEO>.*`.
4. **Alineación** (`brands/nixon-remax/motion_kit/alinear_voz.py`, sin internet; solo numpy + FFmpeg).
   - **Detección de frases.** Divide el audio en bloques de 10 ms y calcula el RMS de cada uno. Un bloque es silencio si queda 30 dB por debajo del percentil 95. Una pausa de 0.12 s o más separa trozos.
   - **Si sobran trozos,** prueba combinaciones de cortes y elige la que mejor reparte la duración según el número de caracteres de cada línea del guion.
   - **Colocación.** Pone cada frase en su segundo del guion. Si no cabe, la acelera con `atempo` hasta ×1.30.
   - **Cortes manuales.** Si existe `voces/cortes_<VIDEO>.json`, usa esos cortes en vez de detectarlos. Es una lista de `[inicio, fin]` en segundos, **uno por línea del guion** (7). Ejemplo real: `[[0.5,3.3],[4.75,7.9],[8.3,11.75],[12.15,15.45],[16.2,19.1],[20.15,22.95],[25.85,28.0]]`.
   - **Resultado real:** en las 3 grabaciones hubo que fijar los cortes a mano. El agente agregó frases que no estaban en el guion (por ejemplo, "calles asfaltadas **listas para disfrutar**"), y el detector juntaba frases y aceleraba de más.
   - **Mejora propuesta:** Whisper con tiempos por palabra, comparado contra el texto del guion. No está instalado.
5. **Mezcla:** `python mezclar_voces.py <VIDEO> [<VIDEO> ...]`. Sin argumentos procesa los 12.
   - Une las dos partes con `ffmpeg concat -c copy`.
   - Recorta la música, le pone fundidos y baja su volumen mientras hay voz (sidechain).
   - Normaliza con `loudnorm I=-14 TP=-1.5` y codifica AAC a 192k.
   - **Sobrescribe** el render `_v03` y su vista previa. Si no hay voz, deja una versión solo con música.
6. **Final.** Se copia **a mano** a `07_VIDEOS_FINALES/` con un nombre claro, sin acentos ni signos; por ejemplo, `A_Busca_donde_construir_su_casa_CON_VOZ.mp4`. El script no hace este paso.
- **Pedido del dueño:** los archivos deben entenderse por su nombre; los nombres técnicos le resultan difíciles.
- **Regla:** no se usa voz ni avatar de IA de una persona sin su autorización escrita para cada pieza. `prueba_voz_sintetica.py` usa la voz TTS de Windows **solo para probar el alineador**.

### Paso 10 · Artes estáticos (Codex)
- **Qué hay:** 44 archivos en total: 22 de feed 4:5, 15 historias 9:16 y 7 alternativas de pauta. Los informes de Codex dicen "41 artes"; falta aclarar esa diferencia.
- **Calendario:** 15 días.
- **Carruseles:** D02_recorrido (4 láminas), D06_visita (3) y D11_preguntas (3). El resto son de una sola lámina.
- **Archivos:**
  - `scripts/codex_artes_15d.py` y `scripts/codex_identidad_santa_isabel.py`.
  - `brands/nixon-remax/codex_campana_15_dias.json`.
  - `docs/tools/CODEX_ARTES_SANTA_ISABEL.md` y `docs/tools/SANTA_ISABEL_PALETA_AZUL.md`.
- **Pendiente:** el calendario empezaba el 12 nov. 2026 y hay que mover las fechas.

### Paso 11 · Textos (ChatGPT)
- ChatGPT recibe un brief con los datos permitidos, lo prohibido, el tono y un **encabezado obligatorio de tipo de convencimiento** en cada pieza. Por ejemplo: `CONVENCIMIENTO: C4 UBICACIÓN · RED: IG+FB · FORMATO: carrusel 4:5 · NOMBRE: ...`.
- **Archivos:** `coordination/HANDOFF_CHATGPT_SANTA_ISABEL.md` (ronda 1) y `coordination/HANDOFF_CHATGPT_CONTENIDO_2.md` (ronda 2).
- **Revisión antes de usar un texto:** skill `antislop-copywriting`, contra frases genéricas de IA.

### Paso 12 · Entrega (HANDOFF)
- **Paquete por pieza:** video 9:16, versión 4:5, portada, copy de IG y de FB, hashtags, CTA y checklist.
- **Control de calidad:** antes de marcar una pieza `READY_FOR_REVIEW` es obligatorio pasar la skill `.claude/skills/prepublish-qa/`.
- **Carpeta de Drive** (`10_DRIVE_<PROYECTO>/`):
  - `00_Coordinacion/CALENDARIO.md`
  - `03_Videos/Reels_y_Stories_9x16/`
  - `04_Artes_y_disenos/`: `Feed_4x5_Instagram_y_Facebook`, `Historias_9x16_Instagram_y_Facebook` y `Pauta_alternativas`.
  - `05_Guiones_y_copys/`
  - `06_Listo_para_publicar/Facebook` e `/Instagram`.
- **Quién publica:** el dueño programa a mano en Meta Business Suite.

## 4. Estado al 13 nov. 2026
| Pieza | Estado |
|---|---|
| 12 videos 9:16 de 30 s | Renderizados con música |
| Voz real del agente | **A, B y C** listos, en `07_VIDEOS_FINALES`. El dueño aprobó A ("quedó perfecto"). Nadie ha escuchado completas las mezclas de B y C |
| Voz de D, E, F, G1, G2, G4, H1, H2 y H3 | Pendiente de grabación |
| Copia en Drive de A, B y C | Es la versión **sin voz**. Falta reemplazarla |
| Versiones 4:5, portadas, copy y hashtags por video | Pendiente |
| `prepublish-qa` de cada pieza | Pendiente |
| 44 artes de Codex | Hechos; falta mover las fechas del calendario |
| Datos por confirmar con el dueño | Enlaces actuales de Facebook e Instagram; paleta exacta del sitio web; si "listos para construir" se puede usar en pauta (por revalidar) |
| Whisper | Propuesto, sin aprobar |
| PR de esta rama a `main` | No creado |

## 5. Cómo escalarlo a una aplicación
Cada paso manual de arriba corresponde a un paso del producto:

| Paso manual | En la app |
|---|---|
| 1 Datos | Formulario de ficha + validador determinista que bloquea lo no verificado |
| 2 Tomas | Subida a S3/R2 + worker de proxies (ffprobe, SDR 9:16) |
| 3–4 Marca y cierre | Asistente de marca → `kit.json` + recorte automático del agente |
| 5 Ubicación | Editor de pines y calles con clics sobre la foto → JSON de puntos |
| 6–7 Video | Selector de tipo de cliente y de convencimiento → ganchos con Claude API (la ficha es la única fuente de datos) → render por partes en workers |
| 8 Música | Biblioteca con licencia comercial + mezcla automática |
| 9 Voz | Grabar en el navegador o el celular mientras corre el video → Whisper por palabra + la lógica de `alinear_voz.py` → vista previa para aprobar |
| 10–11 Artes y textos | Plantillas de 4:5 y 9:16 + copys generados y revisados contra el validador |
| 12 Entrega | Paquete descargable y checklist. Publicar por la API de Meta es una fase posterior y requiere autorización |

**Arquitectura sugerida:**
- PWA en Next.js → FastAPI (Python) → Postgres + Redis (cola) → workers de render y voz (Python + FFmpeg en contenedores, en CPU) → S3/Cloudflare R2.
- Lo que se puede resolver con código (validar datos, permisos, cobros) no usa un LLM.

**Orden de trabajo técnico:**
1. `config.py` con `MEDIA_ROOT` y sin rutas fijas (sección 1).
2. Convertir `video_build_v05.py` y `video_venta*.py` en un paquete importable, sin `exec`, que reciba JSON (marca + ficha + tomas + guion) y devuelva un MP4.
3. **Prueba de paridad:** reproducir A, B y C con el mismo resultado visual.
4. Cambiar fuentes y música por opciones con licencia comercial.
5. Whisper en la alineación, con la meta de cero cortes manuales en las 3 voces reales.
6. Mover el producto a un **repo privado**.

**Precios, costos y riesgos:** están en la página del plan.
- Los costos son estimados.
- **Pasarelas de pago para El Salvador:** Wompi, N1co o Serfinsa. Falta confirmar si cobran suscripciones.
