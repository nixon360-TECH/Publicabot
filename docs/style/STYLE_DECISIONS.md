# STYLE_DECISIONS — PublicaBOT

- **Fuente:** cuestionario de estilo respondido por Nixon (`STYLE_ANSWERS_2026-11-12.yaml`, texto literal sin editar).
- **Estado:** `CONFIRMADO_USUARIO` salvo lo marcado como `PROPUESTO` (interpretación del agente, requiere visto bueno) o `PENDIENTE`.
- **Precedencia:** una instrucción directa más reciente de Nixon reemplaza este archivo. Para cambiar una regla: editar aquí y registrar la fecha en `docs/DECISIONS.md`.

---

## A. Identidad visual

| Regla | Valor | Estado |
|---|---|---|
| Sensación @nixon.remax | Editorial limpio y confiable: mucho aire, la foto real como protagonista, datos claros | CONFIRMADO |
| Color dominante (todas las marcas) | **Azul/navy siempre manda** ("quisiera que siempre mande el azul como mi color") | CONFIRMADO |
| Paleta @nixon.remax | Navy `#1B2A4A` + blanco `#FFFFFF` + hueso `#FAF7F2`; negro como apoyo; **rojo `#E2001A` opcional, solo al final** (CTA o cierre) | CONFIRMADO |
| Logo RE/MAX | Se usa el archivo oficial con sus colores originales; nunca se recolorea ni se recrea con IA | Regla del master |
| Paleta @nixonhernandez_ (OLY) | Azules/agua como firma (puente natural con Nova Aquatics) | CONFIRMADO |
| Tipografía | Serif editorial para titulares + sans para texto y subtítulos | CONFIRMADO |
| Fuentes concretas | Titulares: **Fraunces** o **Playfair Display**; texto: **Inter**. Todas son Google Fonts gratuitas | PROPUESTO: Nixon elige entre las dos serif |

### Referencias visuales (enviadas por Nixon)

| # | Link | Qué le gusta |
|---|---|---|
| R1 | tiktok.com/@melissaortarealtor/video/7591889708972543262 | Cómo muestra las propiedades |
| R2 | tiktok.com/@kelssie3/video/7589249524674071838 | Letras que **cambian con el fondo** (texto con máscara o mezcla según la imagen) |
| R3 | tiktok.com/@grupoinevita/video/7543702115584052500 | Estilo general (sin nota específica) |
| R4 | tiktok.com/@nacho.jauz/video/7446847131442253061 | Cómo hablan y cómo **aparecen los textos** |

**PENDIENTE (N360-019):** analizar R1–R4 cuadro por cuadro y convertirlos en plantillas.
- Los agentes en la nube no pueden reproducir TikTok de forma confiable. Nixon debe guardar una grabación de pantalla de cada video en `MEDIA_ROOT/90_REFERENCES/` (uso interno de análisis; no se republica).
- Por cada referencia se documenta: tipografía, animación de entrada y salida, posición, duración por palabra, transición y ritmo.
- No se copian marcas, logos ni música de esos videos: se replica la *técnica*, no el contenido.

---

## B. Fotografía de inmuebles

| Regla | Valor | Estado |
|---|---|---|
| Retoque | Natural: luz, color, enderezar líneas. Nunca alterar condiciones reales | CONFIRMADO |
| Reemplazo de cielo | Solo cuando haga falta y **preguntando a Nixon en cada caso**; si se aplica, la imagen queda registrada como `EDITED_SKY` en el manifiesto | CONFIRMADO |
| Texto sobre foto | Precio + zona + logo pequeño en esquina | CONFIRMADO |
| Amueblado virtual con IA | Permitido **con etiqueta visible «Ambientación ilustrativa»** dentro de la imagen | CONFIRMADO |
| Amueblado virtual: salvaguarda | En el mismo carrusel o Reel debe aparecer también la foto real del espacio sin amueblar | PROPUESTO |
| Dron (DJI Air 3S) | Apertura aérea cuando haya permiso y aporte valor | CONFIRMADO |

---

## C. Video y edición

| Regla | Valor | Estado |
|---|---|---|
| Duración del Reel de propiedad | **Según el tipo de propiedad**: terreno/lote 20–30 s · casa o apartamento 30–45 s · propiedad grande o con amenidades 45–60 s | CONFIRMADO (rangos propuestos según la nota de Nixon) |
| Ritmo | Medio: 2–3 s por toma | CONFIRMADO |
| Ganchos (hooks) | Los cuatro tipos, rotando: Nixon a cámara con dato clave · dron + precio en pantalla · pregunta al comprador · detalle visual llamativo | CONFIRMADO |
| Ganchos: investigación | Investigar qué ganchos y frases están funcionando ahora; se permiten ganchos virales poco convencionales y se pide **mucha creatividad**, sin afirmar nada falso sobre la propiedad | CONFIRMADO → tarea N360-020 |
| Presencia de Nixon | Intro y cierre a cámara; el recorrido va con voz en off | CONFIRMADO |
| Transiciones | Varían según la pieza | CONFIRMADO |
| Gradación de color | Natural neutra | CONFIRMADO |

---

## D. Subtítulos y texto en pantalla

| Regla | Valor | Estado |
|---|---|---|
| Modo | Palabra por palabra resaltada, **dinámicos**: cambian de fondo y de estilo, con estética viral de TikTok/IG | CONFIRMADO |
| Aspecto | Plantillas construidas a partir de R1–R4 | PENDIENTE (N360-019) |
| Zona segura | Nada importante en el 15 % inferior ni en la franja derecha de botones de IG/TikTok | Regla técnica |

---

## E. Audio y voz

| Regla | Valor | Estado |
|---|---|---|
| Música | Biblioteca libre de derechos (YouTube Audio Library, Pixabay Music) con licencia registrada por pieza | CONFIRMADO |
| Voz | **Se permite voz IA clonada de Nixon, con autorización escrita.** Por defecto se usa la voz real | CONFIRMADO |
| Voz IA: condiciones | Autorización registrada **por pieza** en `approval_status.json`; herramienta open-source local (por evaluar, N360-021); la voz de clientes o terceros nunca se clona; revisar las reglas de etiquetado de IA de Meta antes de publicar | PROPUESTO |
| Avatar o clon visual | Permitido con autorización explícita por pieza | CONFIRMADO |

---

## F. Copy y tono

| Regla | Valor | Estado |
|---|---|---|
| Tono @nixon.remax | Profesional cercano, **de usted** | CONFIRMADO |
| Largo del caption | Medio con viñetas de ficha; puede variar según la pieza | CONFIRMADO |
| Hashtags | 10–15, mezclando zona, tipo de propiedad y nicho | CONFIRMADO |
| CTA | «Escríbame por WhatsApp» con link wa.me rastreable (+503 7956 4399) | CONFIRMADO |
| Palabras prohibidas | — | PENDIENTE (Nixon) |

---

## G. Cuenta personal OLY

| Regla | Valor | Estado |
|---|---|---|
| Estilo | Documental tipo vlog: crudo pero cuidado | CONFIRMADO |
| Contenido inmobiliario en OLY | **Solo Reels colaborativos con propiedades top** | CONFIRMADO |

---

## H. IA generativa

| Regla | Valor | Estado |
|---|---|---|
| IA visual | Solo de apoyo: gráficos de datos, fondos, B-roll conceptual **no inmobiliario** | CONFIRMADO |
| Excepción | Amueblado virtual con etiqueta (sección B) | CONFIRMADO |

---

## I. Revisión y aprobación

| Regla | Valor | Estado |
|---|---|---|
| Variantes | 3 variantes A/B/C | CONFIRMADO |
| Variantes: alcance | Las tres comparten el cuerpo del video; **solo cambian el gancho (0–3 s) y el texto de portada**. Así la revisión no rompe el límite de 120 min/día | PROPUESTO |
| Dispositivo | Celular y PC por igual (el panel debe ser responsive) | CONFIRMADO |
| Ventana de revisión | **8:00 a. m.** (hora de El Salvador): los borradores deben estar listos antes | CONFIRMADO |
| Publicación | Nixon programa en **Meta Business Suite** (gratis). PublicaBOT entrega el paquete listo para programar. La API automática queda para la Fase 4 | CONFIRMADO |

---

## J. Herramientas y costo

| Regla | Valor | Estado |
|---|---|---|
| Presupuesto de software | **Solo ChatGPT + Claude.** Todo lo demás debe ser gratuito u open-source | CONFIRMADO |
| Editor premium | DaVinci Resolve (versión gratuita) | CONFIRMADO |
| Otros editores | El editor que mencionó Nixon es **FilmCraft** (`storytold/filmcraft`, suite ArtCraft, Apache-2.0/MIT, se maneja por MCP). Se usará como editor principal, por ahora en alpha. Ver `docs/tools/VIDEO_STACK.md` | CONFIRMADO_USUARIO (herramienta) / PROPUESTO (stack) |
| Motor de plantillas | FFmpeg + plantillas propias en código (100 % open-source) | CONFIRMADO |
| Capa de subtítulos y diseño | **Remotion** para subtítulos dinámicos y texto con mezcla. Es gratis para Nixon como individuo, pero no es open-source puro | PROPUESTO: requiere visto bueno |
| Higgsfield | Fuera del flujo por defecto (es de pago). Solo con autorización puntual | Derivado de la regla de costo |

---

## K. Publicidad

| Regla | Valor | Estado |
|---|---|---|
| Plataforma | Meta (IG + FB) primero; Google Ads después | CONFIRMADO |
| Objetivo | Mensajes a WhatsApp | CONFIRMADO |
| Acceso | APIs oficiales gratuitas (Meta Marketing API, Google Ads API) dentro de PublicaBOT | CONFIRMADO |
| Presupuesto | Nixon aprueba cada campaña con monto y fecha. Ningún agente activa gasto | CONFIRMADO |
