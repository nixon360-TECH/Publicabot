---
document_id: NIXON360-CONTENTOPS-MASTER
version: 1.0
updated_at: 2026-11-08
locale: es-SV
timezone: America/El_Salvador
classification: INTERNAL_MASTER_CONTEXT
owner: Nixon Hernández
status: READY_FOR_DISCOVERY_AND_MVP
intended_readers:
  - Claude
  - Claude Code
  - ChatGPT
  - Codex
  - Ingenieros y colaboradores autorizados
primary_objective: Ventas inmobiliarias verificables mediante contenido multicanal; fortalecer marca personal y escalar negocios secundarios
source_of_truth: El repositorio privado que se confirme en fase de descubrimiento; este documento es el handoff inicial, no una instalación ejecutada
publication_policy: HUMAN_APPROVAL_REQUIRED
---

# NIXON 360 / CONTENTOPS — CONTEXTO MAESTRO, ARQUITECTURA Y PLAN DE EJECUCIÓN

> **LEER PRIMERO — PARA CUALQUIER LLM O AGENTE.** Este documento consolida la conversación de trabajo del 8 de noviembre de 2026 y materiales históricos recuperados de ContentOps, BuscaBot, Nixon RE/MAX, Higgsfield y Santa Isabel. **No significa que se hayan instalado programas, conectado REconnect/WhatsApp, desplegado servidores, creado este repositorio o activado publicaciones automáticas.** Separar siempre `CONFIRMADO_USUARIO`, `OBSERVADO_EN_HERRAMIENTA`, `HISTÓRICO`, `PROPUESTO`, `PENDIENTE`, `SUPERADO` y `BLOQUEADO`.

## 0. Instrucción de arranque y reglas de precedencia

**Primera instrucción a Claude, Claude Code, Codex o ChatGPT:**

1. Leer íntegro este archivo antes de desarrollar, publicar o crear otro plan de ContentOps.
2. Recuperar el estado ACTUAL de los repositorios, ramas, aplicaciones conectadas, carpetas Drive, credenciales **sin exponerlas**, inventario aprobado y decisiones. No asumir que una descripción histórica representa la versión desplegada.
3. Leer `AGENTS.md`, `CLAUDE.md`, `docs/engineering/STACK_RULES.md` y otros archivos de instrucciones del repositorio **relevante** antes de modificar código. Respetar las reglas locales de cada repo.
4. Identificar las contradicciones entre fuentes. Orden de prioridad: (a) instrucción directa más reciente del usuario, (b) ficha comercial vigente aprobada, (c) estado técnico comprobado, (d) documentos históricos, (e) propuesta de un agente. Una discrepancia comercial impide publicar la afirmación dudosa; no impide avanzar en otras tareas.
5. Hacer inventario `YA EXISTE / FALTA / NO CONECTADO / NO VERIFICADO`. **No crear repositorios ni sistemas paralelos hasta auditar lo existente.**
6. Preparar una primera pieza real, editable, revisable y entregable antes de invertir días en una plataforma sofisticada.
7. Toda decisión de costo, acceso, integración externa, publicación, pauta, despliegue, envío a clientes o modificación del sitio requiere autorización específica y verificable de Nixon.
8. Si no se dispone de acceso a chats de otros asistentes, discos, cuentas, herramientas o archivos, declararlo; no fingir sincronización de memorias ni ejecución.
9. No trabajar directamente en `main`; usar ramas, PR, pruebas y aprobación. No sobrescribir silenciosamente decisiones existentes.
10. Mantener documentos de continuidad legibles para humanos y LLMs; cada tarea acaba con evidencia, archivos concretos, estado, bloqueo y siguiente paso.

**Actualización estratégica que supera restricciones históricas:** el handoff educativo de septiembre 2026 ordenaba no vender propiedades ni hacer CTA. Eso correspondía a una etapa educativa concreta y **queda SUPERADO para este programa multimarca de noviembre**: ahora la venta y captación inmobiliaria son prioritarias, manteniendo investigación rigurosa y separación entre contenidos educativos y promociones.

**Nombre operativo de este programa:** `NIXON 360 / CONTENTOPS`. No es necesariamente el nombre comercial público.

---

## 1. Resumen ejecutivo — qué vamos a construir y por qué

### 1.1 Resultado de negocio esperado

Operación ligera, local-first, asistida por IA, capaz de convertir material auténtico de Nixon y fichas inmobiliarias verificadas en publicaciones de gran calidad para Instagram, Facebook y WhatsApp, con evaluación, aprobación desde computadora o teléfono, seguimiento de clientes y medición de ventas.

**Prioridad 1:** vender propiedades, captar nuevos inmuebles, generar consultas calificadas, visitas, ofertas y cierres. **Prioridad 2:** consolidar marca personal creíble. **Prioridad 3:** captar alumnos para Nova Aquatics y clientes empresariales para NBS sin convertir la cuenta principal en una sucesión de anuncios.

Éxito inicial no significa «tengo un panel sofisticado»; significa: un video propio + una propiedad verificada → dos publicaciones acabadas → aprobadas → publicadas o preparadas para publicación → contactos trazables.

### 1.2 Identidad de Nixon

- Nadador olímpico salvadoreño, participante de París 2024.
- Asesor inmobiliario RE/MAX; cuenta especializada `@nixon.remax` y presencia en Facebook.
- Emprendedor / fundador de Next Bot Solutions (NBS), tecnología, automatizaciones y agentes.
- Entrenador de natación y creador de Nova Aquatics.
- Cuenta personal principal de Instagram: `@nixonhernandez_` / Nixon Hernández OLY; referencia comunicada de ~4,500 seguidores (revalidar mediante Insights).
- Regreso a entrenamientos a partir del **18 de noviembre de 2026**.
- Preparación del lanzamiento de **Nova Aquatics** y `nova-aquatics.com` en **enero de 2027**, sujeto a validación de sitio, instalaciones, programa y operación.
- Equipo de captura declarado: iPhone 15 Pro Max, DJI Osmo Pocket 3, DJI Air 3S y micrófonos.
- Contacto personal para anuncios inmobiliarios en este programa: **+503 7956 4399**. No publicar otros teléfonos personales sin verificación/autorización.
- Tono: español natural salvadoreño, profesional, humano, directo. **A los clientes dirigirlos de usted**. En reels orgánicos puede sonar conversacional; no fingir un personaje motivacional.

### 1.3 Tesis de posicionamiento

**«La disciplina no termina en la piscina».** Esta puede ser una idea narrativa, no un eslogan obligatorio en cada video. Las cuatro facetas se conectan mediante disciplina, mejora continua, desarrollo de personas y toma de decisiones; no deben parecer cuatro campañas comerciales independientes.

- `@nixonhernandez_` es la **fuente de alcance, identidad y confianza**, centrada en vida cotidiana, deporte, empresario, asesor y entrenador.
- `@nixon.remax` es el **canal especializado de inventario, educación inmobiliaria, ventas y captación**.
- Página Facebook de Nixon RE/MAX: difusión comercial, información, anuncios, mensajes y conversiones.
- Facebook personal Nixon: confianza y contenido seleccionado, no duplicado automático.
- Nova Aquatics: futura marca especializada de entrenamiento/programas educativos acuáticos.
- NBS: presencia de proyectos/innovación y canal B2B independiente.

**No convertir @nixonhernandez_ en catálogo inmobiliario.** Usar Reels colaborativos y menciones selectivas cuando aportan valor. No repetir idénticas historias o el mismo post en todas las cuentas.

### 1.4 Tiempo y principio operativo

**120 minutos diarios de Nixon, aproximadamente 14 horas semanales como máximo si trabaja los 7 días.** Se incluye guion, captura, control de edición, revisión, publicación y gestión de consultas. El procesamiento de IA puede continuar como trabajo automatizado en su equipo **solo si se configura un servicio local y la computadora está encendida y disponible**; ningún chat de IA hace trabajo de fondo por sí solo.

Distribución de referencia para un día de producción:

| Etapa | Minutos | Entrega |
|---|---:|---|
| Elegir asunto, validar datos y preparar guion | 15 | Brief aprobado para rodaje |
| Grabar 1 intervención y 5–8 clips útiles | 30 | Originales transferidos |
| Edición automatizada + control final | 35 | Vista previa y variantes básicas |
| Revisar y programar/publicar | 15 | Decisión registrada |
| WhatsApp/CRM: consultas, seguimiento, visitas | 25 | Leads y próximas acciones |
| **Total** | **120** | |

**Restricción:** un video premium complejo no está garantizado en 35 minutos. Agrupar grabaciones por lotes y producir piezas premium en varios días. Limitar experimentos de herramientas cuando estorben las ventas.

---

## 2. Audiencias, marcas y funciones de cada plataforma

| Identidad/canal | Prioridad editorial | Ritmo inicial | CTA dominante | Fuente de medición |
|---|---|---|---|---|
| Instagram `@nixonhernandez_` | Lifestyle auténtico: atleta, asesor, startup builder, entrenador | 2–3 Reels orgánicos por semana; historias útiles, no forzadas | Seguir, conocer proyectos, colaboraciones puntuales | Instagram Insights |
| Instagram `@nixon.remax` | Propiedades, recorridos, educativos, mercado y captación | 4–6 publicaciones/semana según medios aprobados | Consultar propiedad / agendar visita por WhatsApp | Instagram Insights + CRM |
| Facebook personal Nixon | Resumen personal y publicaciones relevantes | 1–2 seleccionadas/semana | Conversación y referencia | Insights disponibles |
| Página Facebook Nixon RE/MAX | Listados, videos, educación y anuncios | 4–6 adaptadas/semana | Mensajes y WhatsApp | Meta Business Suite / Ads Manager |
| WhatsApp Business inmobiliario | Calificación, fichas, citas, ofertas y poscontacto | Respuesta por necesidad; estados 2–3/semana | Agendar visita / siguiente paso | Registro CRM + trazabilidad |
| Nova Aquatics | Natación, metodología, captación de interesados | Preparación noviembre-diciembre; lanzamiento enero | Registro/interés cuando programa operativo confirmado | Formulario / CRM Nova |
| NBS | Casos reales de automatización y tecnología | Menciones orgánicas y contenidos B2B separados | Contacto empresarial | CRM NBS |

**Cuenta personal vs profesional:** verificar configuración real, permisos y elegibilidad de cada perfil antes de prometer publicación por API. Instagram Graph/API no ofrece las mismas capacidades para cuentas personales normales que para cuentas profesionales. Si la API no soporta un formato/cuenta, activar modo `HANDOFF` (revisión y publicación manual) sin automatizar clics evasivos.

### 2.1 Mezcla editorial: cuentas separadas, misma historia

- Línea Nixon OLY: `Un día en mi vida`, `De vuelta al agua`, `Construyendo`, `Detrás de cada nadador`.
- Línea Nixon RE/MAX: `Propiedad destacada`, `Nixon explica`, `Nixon Data`, `Nixon Radar`, `Guía del comprador`, `Propietarios: vender con criterio`.
- No sobrecargar OLY con historias: medir alcance en la primera historia, porcentaje de abandono, respuestas, DMs y alcance único, no creer que hay una penalización algorítmica fija por cantidad.
- Crear distintas versiones del mismo master cuando cambien intención, encuadre, CTA y audiencia. No publicar copia mecánica.
- Priorizar grabaciones originales de Nixon y voz real; no clonar rostro o voz sin autorización expresa.

### 2.2 Calendario semanal de referencia

| Día | Pieza maestra | Principal | Secundarios | Negocio |
|---|---|---|---|---|
| Lunes | Reel de inmueble vigente, con precio/estado revisados | IG RE/MAX | Facebook Page, historia/WhatsApp | Solicitudes |
| Martes | Vida real: atleta + asesor + empresario | IG OLY | Facebook personal, mención ocasional RE/MAX | Confianza |
| Miércoles | Carrusel o Reel con datos BCR/SSF/CNR/OPAMSS | IG RE/MAX | Facebook Page | Educación y leads |
| Jueves | Segundo inmueble / recorrido / captación de propietarios | IG RE/MAX | Facebook Page, historia/WhatsApp | Visitas y captaciones |
| Viernes | Lotificación Santa Isabel | IG RE/MAX | Facebook Page, WhatsApp y OLY solo selectivo | Proyecto destacado |
| Sábado | Natación, entrenamiento, Nova, NBS o microdocumental | IG OLY | Facebook personal | Audiencia, futuros alumnos |
| Domingo | CRM, métricas, plan, pruebas y mantenimiento | Interno | Solo publicación si existe pieza excelente | Eficiencia |

Horas exactas a optimizar con Insights. Este calendario es **propuesto**, no programación ya aplicada.

### 2.3 Fechas operativas clave

- **Domingo 8 nov. 2026:** consolidación del contexto y arquitectura.
- **Lunes 9 nov. 2026:** comenzar publicaciones con materiales comprobados; primera pieza comercial o educativa según disponibilidad.
- **18 nov. 2026:** regreso a entrenamiento; episodio `De vuelta al agua — 01` con imágenes auténticas después del entrenamiento.
- **Diciembre 2026:** construir interés por Nova y documentar progresión; comprobar operación real antes de anunciar cupos.
- **Enero 2027:** lanzamiento propuesto de Nova Aquatics, con sitio y servicios confirmados; campaña colaborativa OLY↔Nova.

---

## 3. Fuentes disponibles y antecedentes recuperados — conservar contexto sin confundir fechas

### 3.1 Documentos MD localizados en la Library de ChatGPT (archivos históricos)

Se localizaron en la biblioteca accesible, entre otros:

1. `Nixon Remax Bots/ContentOps_Continuity_Master_Context.md` y copia `(1).md`, fecha base 21 ago. 2026.
2. `Nixon Remax Bots/NIXON_REMAX_RESEARCH_CONTENT_HANDOFF_v2.md`, 14 sep. 2026.
3. `Nixon Remax Bots/CONTENTOPS_HIGGSFIELD_HANDOFF_NIXON_REMAX_v1.md`, 14 sep. 2026.
4. `Nixon Remax Bots/Higgsfield_ContentOps_costos_y_proceso.md`, 19 sep. 2026.
5. `Nixon Remax Bots/BUSCABOT_PARTNER_HANDOFF_v0_1.md`.
6. `Nixon Remax Bots/BuscaBot_resumen_proceso.md` y otra copia en raíz.
7. `Santa_Isabel_CONTEXTO_MAESTRO_LLM.md`, versión histórica 20 oct. 2026.
8. `Santa Isabel/SANTA_ISABEL_CENTRO_DE_TRABAJO.md`, actualización 2 nov. 2026.
9. `Santa Isabel/SI_REGLAS_COLABORACION_IA_v01.md`, 2 nov. 2026.
10. `Santa Isabel/SI_UPDATE_CHATGPT_EXPORTAR-SITIO_v01.md`.
11. `Santa Isabel/SI_UPDATE_CHATGPT_FOTOS-CAMINO_v01.md`.
12. Otros archivos `Pasted markdown*.md`, algunos relativos a búsquedas inmobiliarias específicas (no normas de ContentOps).

También se localizó el documento `ContentOps_System_Design_Roadmap_v0_2.docx` y referencias a `ContentOps_System_Design_Document_v1_1_BuscaBot_CNR.pdf`; las especificaciones son **históricas y no necesariamente código implementado**.

**Los documentos originales deberán importarse/leerlos desde una ubicación autorizada cuando Claude tenga acceso.** No se garantiza lectura del historial íntegro de todos los chats privados ni de todos los adjuntos antiguos. Este master no sustituye documentos fuente cuando deba verificarse una regla técnica o comercial.

### 3.2 Decisiones canónicas que sí se deben preservar

- **Graph 001 — BuscaBot:** descubre propiedades de portales, normaliza, deduplica, verifica y crea `SearchResultBundle`. No añadirle edición de video ni Facebook publishing en su MVP.
- **Graph 002 — ContentOps:** ingesta de medios/datos → plan → dirección creativa → selección de assets → copy → render → QA → revisión humana → content lock → distribución → verificación → analítica → CRM.
- **Graph 003 — Market & Content Intelligence:** fuentes públicas, tendencias, evidence ledger, scoring, investigación y briefs educativos. Puede alimentar Graph 002.
- Jerarquía creativa: **MEDIOS REALES → SISTEMA DE DISEÑO → TEMPLATES APROBADOS → RENDER PROGRAMÁTICO → IA DE APOYO → GENERACIÓN TOTAL**.
- `Creative Director/Router` elige entre REUSE / CANVA / LOCAL-REMOTION-FFMPEG / HIGGSFIELD según calidad, riesgo y costo.
- `Quality Gate`, aprobación humana, bloqueo inmutable del master aprobado, trazabilidad e idempotencia antes de publicar.
- Modos de distribución: `AUTO` (API oficial y permiso), `DRAFT` (borrador compatible), `HANDOFF` (usuario publica).
- No presentar anuncios de portales como precios de cierre; distinguir `ASKING`, `REGISTERED_TRANSFER`, `APPRAISAL`, `ESTIMATE`.
- No inventar datos físicos, legales, registrales o financieros.
- Auditoría creativa inicial de Canva: seleccionar 10–12 piezas, clasificar A/B/C/D, extraer `Creative DNA`, validar 3 direcciones, crear tres templates de alto nivel — no 100 plantillas.
- Auditar presupuesto y licencias de IA antes de generar por lotes.

### 3.3 Estado de Higgsfield — históricos no equivalen a saldo actual

- Un registro de agosto describía plan Pro de 600 créditos; **no asumir que continúa igual**.
- El informe de septiembre reconstruyó un lote de **79 clips de 5 segundos, 395 segundos de bruto, 528.75 créditos estimados**. Reportó **3.45 créditos de saldo observado al 19 sep. 2026**, no saldo verificado al 8 nov.
- Ese lote era **biblioteca de clips**, no 79 Reels terminados; buscar sus archivos/orígenes antes de volver a gastar.
- Regla: estimate → comprobar presupuesto/saldo → aprobación → generar → registrar consumo y resultado. No gastar créditos de forma indiscriminada.

### 3.4 Canva histórico

- Brand Kit `Nixon.Remax`, ID histórico `kAGRDHJKvZM` — verificar que sigue accesible/adecuado.
- Carpeta `ContentOps` con `00_INBOX`, `01_BRAND_SYSTEM`, `02_TEMPLATE_LAB`, `03_TEMPLATES_APPROVED`, `04_PROPERTIES`, `05_EDUCATIONAL_CONTENT`, `06_REELS_VIDEO`, `07_PRESENTATIONS`, `08_PUBLISHED`, `90_REFERENCES`, `99_ARCHIVE`.
- **No mover, borrar ni sobrescribir diseños antiguos automáticamente**.

### 3.5 Repositorios existentes observados en GitHub

Cuenta: `nixon360-TECH`. Repositorios visibles al 8 nov. 2026:

| Repo | Propósito observado | Acción correcta |
|---|---|---|
| `Buscabot-NBS` | BuscaBot Graph 001 — búsqueda/inteligencia de inmuebles | Respetar sus reglas; definir contrato de exportación hacia ContentOps |
| `santa-isabel-sitio` | Sitio web del proyecto | NO modificar para construir ContentOps |
| `santa-isabel-media-ops` | Scripts de arte/video/edición para Santa Isabel (README mínimo observado) | Auditar código, recursos y uso potencial; no presumir que ya tiene pipeline multimarca |

**ATENCIÓN CON ARQUITECTURA BUSCABOT:** su `AGENTS.md` actual describe `Next.js 16` para web, `Fastify`, `Prisma/PostGIS`, `pg-boss`, `pnpm` y un monorepo TypeScript. Eso es más reciente y específico que el diseño histórico de BuscaBot en Python/SQLite. **No sustituir ni «migrar de vuelta» esa pila.** Contenido y búsqueda son productos hermanos; interoperan por contratos y no por edición directa de código ajeno.

Reglas confirmadas de BuscaBot incluyen: no main, no CAPTCHAs/2FA bypass, RE/MAX y Encuentra24 como fuentes prioritarias, pruebas específicas por cambio y **V1 sin envíos automáticos de WhatsApp**.

Para cualquier repo: antes de trabajar, leer archivo real `AGENTS.md`, `CLAUDE.md` y reglas técnicas del repo; **nunca asumir que reglas copiadas aquí reemplazan las actuales**.

### 3.6 Coordinación Santa Isabel existente

Drive de proyecto histórico, confirmado en documentos anteriores:

- Centro de trabajo: `https://drive.google.com/drive/folders/1Lg8G0JsT1sexalJTVLpT8YPI945mx4Jm`
- Carpeta `00_Coordinacion`: `https://drive.google.com/drive/folders/1ztDafrCTkEg77-y_B_sh_00avx8fMd2v`
- Sitio: `https://lotificacionsantaisabel.com`
- Videos: `https://drive.google.com/drive/folders/1Ct_JmZAAGEK3QyU2IhX_wbSuXnl4Kdvj`
- Artes y diseños: `https://drive.google.com/drive/folders/1Z34EHCnuHDQv3PNVXLtYpP2gOJSHDr5s`
- Guiones/copys: `https://drive.google.com/drive/folders/14BGLwPlYjga0oNxHc2yMc_upCSeD_Kha`
- `06_Listo_para_publicar`: `https://drive.google.com/drive/folders/1fkLjVT2rFW8iZam0Jwb5LXNUAMe3LCej`

No asumir permisos de acceso actual hasta comprobarlos; estas carpetas son específicas de Santa Isabel. No hacer a Santa Isabel dueña del ContentOps multimarca: el programa debe tener una raíz de coordinación independiente, y enlazar hacia Santa Isabel donde corresponda.

---

## 4. Decisiones técnicas: sistema local-first con revisión desde teléfono

### 4.1 Principios

1. Código versionado en **GitHub privado**.
2. Originales de foto/video en **disco externo de Nixon** y/o almacenamiento Drive autorizado. GitHub no es repositorio de videos originales.
3. Procesamiento pesado donde estén los archivos y recursos: **PC Windows**, CPU/GPU según disponibilidad real.
4. Cola de trabajos persistente para que, tras una carga, el sistema prepare borradores sin intervención continua.
5. Interfaz web local/responsiva (`Review Inbox`) para aprobar/rechazar desde PC o celular.
6. Acceso remoto PRIVADO y autenticado; evitar abrir un puerto sin seguridad o usar túneles públicos indiscriminados.
7. ChatGPT, Claude Code y Codex pueden colaborar sobre **archivos y Git**, no compartir mágicamente memorias, sesión o tokens.
8. Publicación autorizada con APIs oficiales solo si se confirman cuentas, alcances, formatos y permisos; en caso contrario, **handoff manual**.
9. Mantener separado el plano técnico del plano comercial: la automatización sirve a las ventas, no viceversa.

### 4.2 Arquitectura lógica

```text
  NIXON (teléfono/cámara)                  REconnect export autorizado
           │                                         │
           ▼                                         ▼
  Originals / INBOX Drive ───► Media Intake     Property Intake
           │                       │                 │
           └──────────────┬────────┴─────────────────┘
                          ▼
               CONTENTOPS ORCHESTRATOR
               Planner + Research + Policy
                          │
       ┌──────────────────┼──────────────────┐
       ▼                  ▼                  ▼
  Organic Video       Property Reel     Educational Research
  Transcript          Fact Snapshot     Evidence Ledger
  Auto-cut            Real Media        Storyboard / Data
       │                  │                  │
       └──────────────────┼──────────────────┘
                          ▼
           Creative Router / Editing Stack
          FFmpeg + Auto-Editor + Whisper
        Remotion/Canva + optional DaVinci/Higgsfield
                          ▼
                   QUALITY GATE
                          ▼
             REVIEW INBOX (PC + móvil)
              Nixon: aprobar/rechazar
                          ▼
                   CONTENT LOCK
                          ▼
    API oficial (autorizada) / DRAFT / HANDOFF
                          ▼
               Instagram / Facebook
                          ▼
         WhatsApp → CRM → Visitas → Ofertas
                          ▼
                Analytics + Attribution
                          ▼
                 Planner / Feedback
```

**No introducir un «agente IA» donde basta una función determinista.** Clasificar cada pieza como agent, task, tool, adapter, policy, loop, executor o estado. El LLM puede planificar y ayudar a editar, pero una validación de precio, checksum, permiso y publicación debe implementarse con lógica verificable.

### 4.3 Propuesta de pila tecnológica (sujeta a auditoría de reutilización)

| Capa | V1 pragmática | Nota |
|---|---|---|
| Directorio/servicios | Windows, Python y/o Node LTS según estado recuperado | No forzar instalación si ya existe base funcional |
| API local | FastAPI **si** se reutiliza el diseño previo; o servicio TS si conviene al repo auditado | Decidir por ADR, no por preferencia de modelo |
| Base de datos de estado | SQLite con migraciones en V1 de un solo operador | Migrar a PostgreSQL solo si escala/colaboración lo justifican |
| Worker local | Proceso supervisado + cola persistente, lease/retries y estados | Evitar procesos efímeros de chat como scheduler |
| Edición base | FFmpeg, ffprobe, Auto-Editor, Whisper local | Comprobar instaladores, recursos y licencias |
| Motion/templates | Remotion + TypeScript/React, Canva | Remotion es source-available con licencia propia, NO tratar como OSS sin condiciones |
| Acabado premium | DaVinci Resolve, edición manual cuando valga la pena | Proyecto especial, no paso forzoso diario |
| Generación opcional | Higgsfield con `Credit Governor` y autorización | No generar inmueble ficticio |
| Panel móvil | Web responsiva/PWA con auth | Servida desde PC al comienzo |
| Red privada móvil | Tailscale Serve (tailnet, HTTPS, ACL), si se elige | No habilitar Funnel público para datos privados |
| Cloud / Drive | Sincronización de briefs, proxys o archivos aprobados | No poner tokens ni datos personales en carpeta pública |
| Programación social | Meta Business Suite y/o API oficial / gestor conectado | Ver permisos reales, sin depender de hacks |
| CRM | Registro sencillo inicial + REconnect donde aplique | Nunca enviar información privada al LLM sin autorización |

**Requisito del modo móvil:** PC encendida, servicio activo, Tailscale en celular y PC (o servicio web autenticado desplegado de forma segura). Cuando PC esté apagada, el V1 local no renderiza ni sirve nuevos borradores. Un servicio en nube puede añadirse en una fase posterior con criterios de seguridad y costo.

**No programar accesos públicos inseguros** a localhost, puertos, carpetas SMB o API. Proteger sesión de aprobación con credenciales propias, expiración, MFA si es viable, verificación de identidad y controles de cambio de estado.

---

## 5. Arquitectura de información: fuente de verdad, carpetas y normas

### 5.1 Separar tres superficies de información

| Superficie | Guarda | NO guarda |
|---|---|---|
| GitHub repo técnico | Código, configuración sin secretos, schemas, prompts, skills, instrucciones, changelog, templates como código, tests | Videos grandes, contraseñas, DUI, clientes, contratos privados |
| Drive de coordinación | Briefs, fuentes, aprobaciones exportadas, guiones, entregables, proxies/exports según permisos | Claves en texto plano, datos comerciales internos dentro de carpetas públicas |
| PC + disco externo | Originales multimedia, cachés, proxies, renders pesados, backup/working data | Único respaldo de activos importantes |

**No confundir:** una carpeta de archivos aprobados no reemplaza un evento explícito de aprobación en el registro con identidad, versión, hora y alcance de canal.

### 5.2 Estructura de repositorio propuesta

**No crear automáticamente el repo antes de auditar si existe `contentops` en otro lugar.** Si no existe y Nixon lo autoriza, proponer repo privado `nixon360-TECH/nixon-contentops` (nombre provisional). Usar la siguiente estructura de referencia, adaptable a tecnologías comprobadas:

```text
nixon-contentops/
├── README.md                         # Qué es, arranque rápido, límites
├── NIXON360_CONTEXT_MASTER.md        # Este documento como baseline inicial
├── AGENTS.md                         # Reglas transversales para Codex/otros
├── CLAUDE.md                         # Importa AGENTS + notas Claude Code
├── .gitignore
├── .env.example                      # Variables vacías; sin tokens
├── docs/
│   ├── CURRENT_STATE.md              # Realidad observada, no expectativas
│   ├── DECISIONS.md                  # Registro de decisiones/ADR
│   ├── OPEN_QUESTIONS.md
│   ├── CONNECTORS.md                 # Herramientas, permisos, estado, dueño
│   ├── SKILLS_REGISTRY.md            # Skills, fuente, licencia, fecha de revisión
│   ├── SECURITY.md
│   ├── MEDIA_PIPELINE.md
│   ├── EDITORIAL_CALENDAR.md
│   ├── BRAND_SYSTEM.md
│   ├── SALES_CRM.md
│   ├── PUBLICATION_POLICY.md
│   ├── DATA_DICTIONARY.md
│   ├── RUNBOOK.md
│   ├── architecture/
│   └── adr/
├── coordination/
│   ├── TASK_BOARD.md
│   ├── DECISION_LOG.md
│   ├── HANDOFF_LATEST.md
│   ├── CHANGELOG.md
│   ├── source-manifests/
│   └── handoffs/
├── brands/
│   ├── nixon-oly/brand.yaml
│   ├── nixon-remax/brand.yaml
│   ├── nova-aquatics/brand.yaml
│   ├── nbs/brand.yaml
│   └── santa-isabel/brand.yaml
├── policies/
│   ├── fact_policy.yaml
│   ├── brand_rules.yaml
│   ├── privacy_policy.yaml
│   ├── publishing_policy.yaml
│   ├── cost_budget.yaml
│   └── creative_router.yaml
├── schemas/
│   ├── property_creative_snapshot.schema.json
│   ├── asset_manifest.schema.json
│   ├── content_item.schema.json
│   ├── approval.schema.json
│   ├── publication_job.schema.json
│   └── lead.schema.json
├── apps/
│   ├── api/                           # Backend y auth
│   └── review-web/                    # Revisión PC/móvil
├── services/
│   ├── intake/
│   ├── research/
│   ├── planning/
│   ├── creative/
│   ├── video-edit/
│   ├── qa/
│   ├── approvals/
│   ├── publishing/
│   ├── attribution/
│   └── analytics/
├── providers/
│   ├── reconnect-export/
│   ├── buscabot-export/
│   ├── google-drive/
│   ├── canva/
│   ├── higgsfield/
│   ├── remotion/
│   ├── meta/
│   └── whatsapp/
├── templates/
│   ├── organic-daily-reel/
│   ├── property-reel/
│   ├── educational-data-reel/
│   ├── carousel/
│   ├── captions/
│   └── review-card/
├── .claude/
│   ├── skills/
│   │   ├── ingest-and-proxy/SKILL.md
│   │   ├── property-fact-check/SKILL.md
│   │   ├── organic-reel-edit/SKILL.md
│   │   ├── property-reel/SKILL.md
│   │   ├── research-to-carousel/SKILL.md
│   │   ├── prepublish-qa/SKILL.md
│   │   └── postmortem-analytics/SKILL.md
│   └── agents/
│       ├── content-researcher.md
│       ├── creative-director.md
│       ├── editor-qa.md
│       └── sales-analyst.md
├── tasks/
├── tests/
├── scripts/
└── fixtures/                         # Datos sintéticos; nunca PII real
```

**Ruta externa del disco, por ejemplo `D:\\NIXON_CONTENTOPS\\`, es ILUSTRATIVA, NO ubicación descubierta.** Durante instalación preguntar o detectar rutas con consentimiento. Guardar rutas reales en `.env` local o configuración cifrada. No comprometer rutas privadas en documentación pública.

### 5.3 Carpeta de medios local propuesta

```text
MEDIA_ROOT/                              # SSD / HDD — fuera de Git
├── 00_INBOX/                            # Carga desde teléfono/cámara/Drive
├── 01_ORIGINALS_READONLY/               # Copia original, hash/metadata
├── 02_PROXIES/                          # Copias livianas para previsualizar
├── 03_AUDIO_TRANSCRIPTS/
├── 04_PROJECTS_EDITABLE/                # EDL, proyecto Remotion/DaVinci
├── 05_RENDERS_DRAFT/
├── 06_REVIEW_PREVIEWS/
├── 07_APPROVED_LOCKED/
├── 08_PUBLISHED_EXPORTS/
├── 90_ARCHIVE/
└── 99_FAILED_QUARANTINE/
```

Cada clip debe tener: `asset_id`, `source_device`, `filmed_at` si se conoce, `ingested_at`, hash SHA-256, archivo original, tipo de contenido, propiedad vinculada si aplica, permisos, autor, resolución, duración, orientation, tags/escenas, derechos y estado. No asignar propiedad por coincidencia de nombres solamente.

### 5.4 Convenciones de nombres

- ID de contenido: `N360-20261109-0001` (ejemplo), estable y único.
- Archivo de exportación: `N360_REMAX_PROPERTY_[PROPERTY_ID]_REEL_9x16_v01.mp4`.
- Gráfico: `N360_DATA_CENSO24_CAROUSEL_4x5_v01.png`.
- Original: conservar nombre de cámara + `asset_id` en manifiesto, sin renombrarlo destructivamente.
- Handoff: `HANDOFF_2026-11-09_CLAUDE_TASK-001.md`.
- Branch: `feature/N360-001-intake`, `fix/N360-023-captions`.

### 5.5 Fuente de verdad y sincronización entre LLMs

- GitHub contiene el estado versionado de código/config/políticas.
- Drive contiene archivos y documentos colaborativos; registrar IDs y URLs reales en el estado.
- La base de datos local guarda objetos runtime, estado de aprobación, jobs y eventos auditables.
- `docs/CURRENT_STATE.md` y `coordination/HANDOFF_LATEST.md` explican situación para cualquier asistente.
- Un agente toma una tarea, declara `owner`, branch y estado; otro no edita los mismos archivos a la vez.
- Actualizar `TASK_BOARD.md`, `DECISIONS.md` y un handoff por entrega; no sincronizar conversaciones enteras ni asumir memoria compartida.
- Una copia de un documento no es una fuente de verdad automática: incluir hash, versión, fecha, provenance y enlace al original.

---

## 6. Modos de trabajo: humano, Claude Code, Codex y ChatGPT

| Participante | Responsabilidad principal | Lo que NO se le permite asumir |
|---|---|---|
| Nixon | Filmar, dirección personal, gustos, decisión comercial, leads, aprobar presupuestos/contenido/publicación | No debe editar manualmente seis versiones cada día |
| Claude Code local | Orquestar procesos locales, leer carpeta autorizada, scripts, generación/editing, jobs, panel | No puede acceder al disco sin permisos/ejecución real ni correr si no está configurado |
| Codex/GitHub | Cambios de código bien delimitados, tests, CI, PR, revisión, refactor | No publicar automáticamente ni tocar otra rama sin coordinación |
| ChatGPT | Investigación, estrategia, guiones, crítica creativa, QA conceptual, analítica y handoff estructurado | No accede al PC/Claude ni ejecuta cron local por simple conversación |
| Canva | Editables de artes, carruseles, redimensionado y Brand Kit | No suplanta fotografía real ni verifica inventario |
| Higgsfield | Generación de B-roll/animaciones opcionales | No inventa características de inmuebles ni consume créditos sin preflight |
| Meta Business Suite / API | Programación/publicación donde se soporte y autorice | No saltar restricciones de cuenta, plataforma, CAPTCHA o 2FA |
| WhatsApp Business | Conversación comercial y seguimiento consentido | No spam ni mensajes automáticos fuera de permisos y políticas |

### 6.1 Protocolo de handoff obligatorio

```yaml
task_id: N360-001
title: "Primer Reel orgánico"
owner: claude-code
state: IN_PROGRESS  # TODO/IN_PROGRESS/IN_REVIEW/APPROVED/DONE/BLOCKED
started_at: "2026-11-09T09:00:00-06:00"
base_repo: "[repo_verificado]"
branch: "feature/N360-001-first-reel"
inputs:
  - "asset_id_123"
outputs:
  - "[ruta_o_enlace_verificado]"
checks:
  - "transcripción revisada"
  - "derechos de música confirmados"
  - "render 1080x1920 reproducido"
risks: []
blocking_questions: []
approval_required: true
next_action: "Presentar preview a Nixon"
```

**Regla de fin de trabajo:** enviar siempre qué está realmente hecho, qué se probó, qué está pendiente, qué necesita aprobación y evidencia de links/archivos/commit. «Se planeó» ≠ «se ejecutó».

### 6.2 Plantillas de instrucciones para agentes

**`AGENTS.md` (a generar después de auditoría):** incluir misión, límites, estructura, comandos que REALMENTE funcionan en ese repo, coding standard, tests, no secrets, publicación y aprobación, source hierarchy y estado de handoffs. Si el repo incluye reglas previas, combinar sin perder reglas de seguridad.

**`CLAUDE.md`:** incluir import de `AGENTS.md` (si la versión instalada de Claude Code acepta esa sintaxis, conforme a documentación oficial), referencias a `NIXON360_CONTEXT_MASTER.md` y solo notas particulares de Claude Code. No mantener dos copias contradictorias del mismo reglamento.

**Claude Code skills:** procedimientos repetidos y acotados. Ejemplos: `/ingest-and-proxy`, `/organic-reel-edit`, `/property-fact-check`, `/prepublish-qa`, `/review-pack`, `/postmortem-analytics`. Cada `SKILL.md` con entrada, salida, permisos, preconditions, comandos reales, prohibiciones, control de errores y tests.

**Subagentes Claude:** especialistas con lectura/escritura estrictamente limitada y salida estructurada (research, creative, editor QA, sales analyst). Ningún subagente puede autoaprobar una publicación, gasto, contrato o acceso a datos confidenciales.

**Codex:** leer `AGENTS.md`, trabajar en issue y branch propios, correr tests y hacer PR. No forzar merge ni rebases destructivos; no cambiar código simultáneamente sobre el mismo módulo que Claude Code.

---

## 7. Pipeline de producción audiovisual: original → Reel revisable

### 7.1 Qué graba Nixon

- Una intervención orgánica a cámara de 20–45 s con audio limpio y luz utilizable.
- Cinco a ocho clips B-roll de 5–8 s de trabajo, piscina, reuniones, propiedad o trayecto autorizados.
- Priorizar **9:16** para Reels/Stories, master 1080×1920 final. Grabación 4K/30fps cuando sea práctica y el hardware lo soporte; 60fps solo si se desea cámara lenta.
- Evitar textos importantes demasiado cerca de zonas tapadas por controles de la app.
- Evitar datos de clientes, pantallas con credenciales, matrículas privadas y menores sin consentimientos.
- Nunca usar WhatsApp para transferir el master si comprime los archivos; preferir carpeta Drive de alta calidad o transferencia directa.
- Las filmaciones de clientes/propiedades requieren autorización del propietario/fuente según corresponda; grabaciones de niños requieren consentimiento del representante legal.

### 7.2 Rutina de importación y edición

1. `INBOX`: detectar nueva carga, validar integridad/tamaño, calcular checksum, guardar original inmutable.
2. `MEDIA METADATA`: ejecutar `ffprobe`, identificar formato, duración, FPS, orientación, audio, rotación; error → cuarentena con diagnóstico.
3. `PROXY`: generar preview de bajo peso para móvil y/o clips seleccionables.
4. `TRANSCRIPT`: aplicar Whisper u otro ASR comprobado, devolver SRT/JSON con palabras/tiempos/confianza, idioma español. Revisar nombres, cifras, zonas y precio (ASR puede equivocarse).
5. `AUTO-CUT`: sugerir cortes de silencio/repetición con Auto-Editor y/o EDL; no eliminar contexto esencial ni dejar saltos no naturales.
6. `STORY EDIT`: LLM propone hook, secuencia, B-roll y subtítulos en JSON **validado**, con referencias a `asset_id` y rangos temporales reales. No alucinar tomas inexistentes.
7. `RENDER`: plantilla Remotion/FFmpeg, edición de audio, mezcla musical autorizada, subtítulos legibles, lower-thirds, logo oficial y CTA adecuado.
8. `QA AUTOMÁTICA`: formato, sonido, duración, frame negro, título legible, audio clipping, subtítulos truncados, archivo playable, consistencia de datos, marca, derechos.
9. `QA EDITORIAL`: humano/LLM revisor, verificar hechos, autenticidad y objetivo de venta o relación.
10. `PREVIEW`: crear versión watermark/bajo peso para panel y export editable.
11. `REVISION`: Nixon elige aprobar, pedir cambios (comentario/tiempo exacto), rechazar o guardar como borrador.
12. `LOCK`: congelar assets, audio, copy, CTA, precio y versión con hash de contenido.
13. `PUBLISH`: disparar únicamente el flujo autorizado para la cuenta/formato; verificar resultado/URL.
14. `ANALYTICS`: registrar métricas al periodo correspondiente y relacionar leads.

**No afirmar que Auto-Editor o Whisper sustituyen al editor de forma perfecta.** Son etapas de automatización asistida. DaVinci Resolve entra en piezas premium, corrección fina y color.

### 7.3 Herramientas candidatas y validaciones

| Herramienta | Función | Naturaleza / validación |
|---|---|---|
| FFmpeg/ffprobe | Cortar, mezclar, sonorizar, exportar, inspeccionar | Software abierto; confirmar build y licencias de codecs |
| Auto-Editor (`WyattBlue/auto-editor`) | Detectar ritmo/silencios y generar edición base/EDL | Revisar versión, licencia y opciones de exportación |
| Whisper (`openai/whisper`) | Speech-to-text, subtítulos | Revisar versión y recursos GPU/CPU |
| Remotion (`remotion-dev/remotion`) | Video determinístico programado en React | **Source-available/licencia propia**; verificar elegibilidad y modalidad comercial |
| Remotion AI Skills | Procedimientos de construcción de videos con agentes | Evaluar repositorio oficial de skills y versiones |
| Motion Canvas | Motion graphics procedimental | Alternativa evaluable, no instalar por duplicación |
| DaVinci Resolve | Edición premium/color/audio | Herramienta comercial con licencia según uso; instalación separada |
| Canva | Carruseles y artes editables con Brand Kit | Usar marca aprobada, no replicar logos por IA |
| Higgsfield | B-roll conceptual y clips experimentales | Solo si añade valor y pasa Credit Governor |
| LosslessCut | Recorte rápido sin recomprimir cuando es posible | Herramienta opcional; no es core |

Regla de dependencia: instalar solo lo necesario para producir **(A) un Reel orgánico, (B) un Reel de propiedad, (C) un carrusel basado en datos**. El resto queda bajo evaluación.

### 7.4 Tres familias creativas v1

**ORGANIC01 — Nixon un día normal**
- Fuente: Nixon grabado, clips personales auténticos, voz real.
- Tono: natural, ágil, sobrio, no excesivamente producido.
- Entrega: Reel 25–60 s, portada 4:5, variante historia, texto/hashtags medidos.
- Ejemplo: `Soy nadador olímpico y este es un martes normal`; incluye asesoría, NBS, natación cuando aplique.

**PROPERTY01 — Propiedad verificable**
- Fuente: ficha/estado actual de REconnect export autorizada + fotos reales + autorización.
- Formatos: Reel 20–35s, 4:5 carrusel, Facebook, 9:16 historia, ficha WhatsApp.
- Campo obligatorio: `property_id`, status, ubicación pública apropiada, precio/moneda, medidas/unidades, features confirmadas, origen de imágenes, CTA.
- No incluir metrajes, características o precios no verificados. Si falta, omitir o bloquear según importancia.

**DATA01 — Datos inmobiliarios**
- Fuente: BCR/ONEC/SSF/CNR/OPAMSS, metodología y fecha.
- Formatos: carrusel 4:5, Reel motion 20–45s, copy con fuentes.
- Ejemplos: Censo 2024, tenencia/condiciones de vivienda, precios anunciados vs cierres, financiamiento.
- El Censo 2024 no prueba automáticamente las causas de variación del precio inmobiliario. Distinguir observación, hipótesis y causalidad.

### 7.5 Dirección visual / Creative DNA

- Editorial, moderno, humano, preciso, accesible, buen tratamiento de fotografías reales.
- Evitar gold/luxury genérico, neón, halos IA, mansiones inexistentes, HDR exagerado, música sin licencia, texto ilegible, gráficas sin fuente.
- RE/MAX debe respetar sus logos oficiales y uso de marca; no hacer que `Nixon OLY` parezca comunicación corporativa de una franquicia.
- Santa Isabel: marca inmobiliaria **accesible, no premium**. Imágenes reales, cercanía, ubicación, servicios verificados.
- Seleccionar 10–12 diseños previos Canva, clasificar `A me gusta / B con cambios / C solo elementos / D no me gusta`, registrar preferencias y producir tres direcciones para Nixon aprobar.
- Nunca generar fotografías de inmuebles reales con habitaciones, vías, amenidades, servicios o entornos inventados.

---

## 8. Datos y contratos: no inventar, no mezclar clientes e inventario

### 8.1 Inventario REconnect — acceso PENDIENTE

El usuario tiene base de datos en REconnect. **No está confirmada aquí una conexión activa y autorizada con REconnect ni API de lectura.** Antes de automatizar:

1. Revisar términos de uso, permisos profesionales y si existe exportación CSV/XLSX o API oficial.
2. Importar SOLO registros autorizados para marketing; no extraer campos privados de clientes/propietarios por scraping de área restringida.
3. Identificar `external_id`, fecha de verificación, estatus, precio, divisa, tipo, ubicación pública, metraje, derechos de imagen, link y agente responsable.
4. Preparar `PropertyCreativeSnapshot` inmutable por contenido, con fuente/hash/fecha.
5. Revalidar estado/precio antes de revisión y nuevamente antes de publicación.
6. Si se revocan permisos o cambia disponibilidad, cancelar publicación y notificar. Nunca inferir disponible por simplemente estar en un Excel viejo.

### 8.2 Ejemplo `PropertyCreativeSnapshot` (NO datos reales)

```json
{
  "schema_version": "1.0",
  "property_id": "PROP-DEMO-001",
  "source_system": "RECONNECT_EXPORT_AUTHORIZED",
  "source_record_id": "DEMO-ID",
  "source_verified_at": "2026-11-09T09:00:00-06:00",
  "listing_status": "ACTIVE_VERIFIED",
  "transaction": "SALE",
  "type": "HOUSE",
  "asking_price_usd": null,
  "public_location": "[UBICACION_PUBLICABLE_AUTORIZADA]",
  "area_m2": null,
  "features_verified": [],
  "public_contact": "+50379564399",
  "media_asset_ids": [],
  "marketing_permission": false,
  "notes": "EJEMPLO; BLOQUEAR PUBLICACIÓN HASTA COMPLETAR DATOS REALES"
}
```

### 8.3 Evidence Ledger de investigación pública

```yaml
claim_id: CENSO24-EXAMPLE-001
claim: "El Censo 2024 registró 6,029,976 personas en El Salvador"
source_name: "BCR / Censo de Población y Vivienda 2024"
source_url: "https://censo2024.bcr.gob.sv/"
source_publication_date: "[verificar documento exacto]"
accessed_at: "[fecha real de consulta]"
period: "2024"
geography: "El Salvador"
evidence_level: PRIMARY_OFFICIAL
caveats: "Cifra demográfica, no evidencia de causalidad sobre precios inmobiliarios"
```

Fuente oficial relevante: `https://poblacion.bcr.gob.sv/`; Segundo informe de resultados: `https://censo2024.bcr.gob.sv/wp-content/uploads/tablas-geoportal/informe-de-resultados-censo-de-poblacion-y-vivienda-el-salvador-2024-segunda-entrega.pdf?download=1`. Cifras reportadas oficialmente: 6,029,976 habitantes, 2,270,170 viviendas, 1,920,668 hogares. Revalidar definiciones y tablas antes de publicar porcentajes u otras derivaciones.

**Precisión:** distinguir tenencia de vivienda, cantidad de viviendas, hogares, déficit cualitativo y déficit cuantitativo. No afirmar que 1.48 millones «no tienen casa» si la cifra incluye viviendas necesitadas de mejoras. Fuentes sobre deuda, tasas, remesas o vivienda requieren fecha/serie correcta y, cuando aplica, advertencias metodológicas.

### 8.4 CRM / leads y privacidad

El CRM de marketing inmobiliario tendrá como mínimo:

```yaml
lead_id: "UUID"
created_at: "timestamp"
source_channel: "instagram_oly | instagram_remax | facebook_personal | facebook_page | whatsapp | referral | other"
source_post_id: "nullable"
campaign_id: "nullable"
property_id: "nullable"
consent_status: "UNKNOWN | OPTED_IN | OPTED_OUT"
name: "private"
phone: "private"
budget_range: "private"
zone_interest: "private"
transaction: "BUY | SELL | RENT | INVEST"
stage: "NEW | QUALIFIED | DETAILS_SENT | VISIT_SCHEDULED | VISIT_DONE | OFFER | CLOSED | LOST"
owner: "Nixon"
next_followup_at: "nullable"
last_contact_at: "nullable"
notes: "private, access restricted"
```

- Proteger PII. El código, prompts públicos y artefactos de diseño no deben incluir teléfono, DUI, presupuesto individual o mensajes privados de los clientes.
- Los agentes solo pueden consultar datos personales mínimos para el flujo autorizado, con trazabilidad de acceso.
- Preparar borradores de mensajes y tareas de seguimiento; **no enviar WhatsApp masivo ni mensajes sin consentimiento**.
- Para WhatsApp Business Platform/API: revisar políticas de templates aprobados y ventana de servicio, permisos y facturación actuales. La app WhatsApp Business y WhatsApp Cloud API **no son la misma integración**.
- Puede habilitarse un enlace de contacto verificable desde contenido; no prometer un chatbot automático sin conexión legal y técnica aprobada.
- Leads de Nova deben separarse de compradores inmobiliarios: finalidades distintas y permisos diferenciados.

### 8.5 Modelo lógico mínimo

Entidades sugeridas: `brands`, `social_accounts`, `properties`, `property_snapshots`, `assets`, `asset_rights`, `topics`, `evidence_claims`, `campaigns`, `content_items`, `content_versions`, `script_versions`, `render_jobs`, `quality_checks`, `approvals`, `publication_jobs`, `publication_attempts`, `published_posts`, `analytics_snapshots`, `leads`, `lead_interactions`, `followup_tasks`, `ai_runs`, `provider_costs`, `activity_log`.

**Objetivo relacional:** `propiedad → contenido → post → clic/mensaje → lead → visita → oferta → cierre`.

**`activity_log` append-only**; cuando algo cambia, se agrega evento, no se reescribe el historial. Registrar timestamps con offset y almacenar UTC internamente para comparación, mostrando hora El Salvador al usuario.

---

## 9. Máquina de estados y aprobación: lo más importante del sistema

### 9.1 Estados

```text
IDEA
  → RESEARCHING
  → BRIEF_READY
  → MEDIA_READY
  → SCRIPT_READY
  → EDITING
  → RENDERED_DRAFT
  → QA_PENDING
  → READY_FOR_REVIEW
      ├─ NEEDS_CHANGES → EDITING (nueva versión)
      ├─ REJECTED → ARCHIVED
      └─ APPROVED_LOCKED
             → SCHEDULED
             → READY_TO_POST
             → PUBLISHING
             → PUBLISHED
             → VERIFIED
             → ANALYTICS_RUNNING
             → COMPLETED
```

Ramas de error: `BLOCKED_FACTS`, `BLOCKED_RIGHTS`, `BLOCKED_BUDGET`, `FAILED_RENDER`, `FAILED_PUBLISH`, `STALE_PROPERTY`, `OFFLINE`, `PAUSED`, `CANCELLED`.

### 9.2 Contrato de aprobación

```json
{
  "approval_id": "UUID",
  "content_item_id": "N360-20261109-0001",
  "content_version": 3,
  "preview_sha256": "[sha256_del_video_o_arte_y_copy]",
  "platform_targets": ["instagram_remax", "facebook_page"],
  "caption_sha256": "[hash_del_copy_final]",
  "property_snapshot_id": "[si_aplica]",
  "approved_by": "Nixon",
  "approved_at": "2026-11-09T11:15:00-06:00",
  "approval_scope": "CONTENT_ONLY",
  "publish_authorization": false,
  "ad_budget_authorized_usd": 0,
  "expires_at": null
}
```

**Dos decisiones separadas:** aprobar el contenido **no** significa autorizar un gasto publicitario ni publicar instantáneamente. El panel debe indicar claramente: `Aprobar contenido`, `Programar publicación` y, si aplica, `Autorizar campaña/presupuesto`.

- Aprobar contenido bloquea `file hash + copy + CTA + cuenta destino + precio + property_snapshot`.
- Modificar cualquiera exige nueva versión y nueva aprobación.
- El servidor debe autenticar al usuario, registrar acción y evitar aprobaciones anónimas por URL.
- Prevención de duplicados: `idempotency_key = platform + account + content_version + scheduled_slot`.
- Antes de ejecución verificar `APPROVED_LOCKED`, modo de publicación disponible, permisos/token, no duplicado, presupuesto autorizado y datos comerciales todavía vigentes.
- Si Meta/API falla, cambiar a `FAILED_PUBLISH` con motivo; no afirmar publicación hasta tener ID/URL verificada.
- `DRAFT/HANDOFF` debe presentar archivo, copy, link y checklist para publicación manual; después Nixon confirma enlace/estado.

### 9.3 Panel de revisión desde teléfono

**MVP visual propuesto:** interfaz privada de uso propio, con tarjetas de material:

- Miniatura + reproductor con proxy optimizado.
- Marca, serie, objetivo, cuenta/canal destino, fecha propuesta.
- Hook y guion; copy y CTA; fuentes verificadas; propiedad/precio/estatus.
- Versiones A/B/C (cuando sea útil), historial de cambios.
- Notas con timestamp: «cambiar toma 0:08», «usar titular 2», «subir volumen», «no me gusta color».
- Acciones: `Aprobar contenido`, `Pedir cambios`, `Rechazar`, `Guardar borrador`.
- Publicación: pantalla de autorización separada con cuenta, fecha, contenido inmutable y modalidad `AUTO / DRAFT / HANDOFF`.
- Estado de procesamiento y alertas de bloqueo: `PC offline`, `No se pudo renderizar`, `Precio sin confirmar`, `Falta licencia musical`.
- Dashboard simple: «Hoy por revisar», «Programados», «Publicados», «Consultas», «Visitas».

**Modelo de acceso:** PWA responsive + HTTPS/identidad, inicialmente por red privada tailnet usando Tailscale Serve; no suponer que Tailscale está instalado. Diseño sin exposición pública de archivos ni links de aprobación de un clic no autenticados.

### 9.4 Automatizaciones programadas

Eventos que pueden ejecutarse después de configurar un worker real:

- `file_ingested` → crear proxy/transcripción / sugerir briefing.
- `property_snapshot_verified` → ofrecer concepto de anuncio, nunca publicar automáticamente.
- `daily_planner` → generar propuestas de tres temas y borradores útiles.
- `review_requested` → mostrar notificación en el panel (push/email/aviso opcional solo si conectado y autorizado).
- `approved_for_render` → crear export final de calidad.
- `approved_for_publish` → encolar con guardas e idempotencia.
- `post_verified` → registrar métricas y links; crear tareas de seguimiento, sin invadir WhatsApp.
- `property_status_changed` → bloquear posts futuros vinculados a un inmueble inactivo.
- `analytics_weekly` → resumen comercial y propuestas de mejora.

El job debe persistir y reintentar con backoff, límite y auditoría. **Nunca «prometer» ejecución futura desde un chat si no hay scheduler y conexión funcionando.**

---

## 10. Ventas inmobiliarias — Instagram/Facebook → WhatsApp → operación

### 10.1 Funnel y objetivos

```text
Contenido de calidad/propiedad real
           ↓
Alcance + confianza + claridad
           ↓
Instagram / Facebook (orgánico o anuncio autorizado)
           ↓
CTA medible por fuente y propiedad
           ↓
WhatsApp Business / mensaje / formulario autorizado
           ↓
Calificación (zona, presupuesto, plazo, necesidad)
           ↓
Ficha verificable + agenda de visita
           ↓
Visita → oferta → negociación → cierre
           ↓
Medición de valor por fuente / campaña
```

**Ritmo de seguimiento:** reservar 25 minutos diarios para mensajes reales, citas y pipeline, no convertir toda la sesión en edición estética. Cada lead tiene `next_action` y fecha, o se marca cerrado/perdido con motivo.

### 10.2 Estados comerciales y mensajes

- `NEW`: saludo y clasificación sin presión.
- `QUALIFIED`: presupuesto/rango, necesidad, zona, fecha estimada, financiamiento cuando proceda.
- `DETAILS_SENT`: ficha, enlace/planos autorizados, preguntas abiertas.
- `VISIT_SCHEDULED`: cita clara y confirmación.
- `VISIT_DONE`: feedback y próxima acción.
- `OFFER`: solicitud/oferta y negociación documentada.
- `CLOSED` / `LOST`: resultado, motivo, fuente; no borrar lead.

**Mensaje de primera respuesta propuesto al cliente, trato de usted:**

> ¡Hola! Mucho gusto, gracias por escribirme. Con gusto le ayudo. ¿Qué zona tiene en mente y un presupuesto aproximado? Así puedo compartirle opciones que realmente le funcionen.

No presentar scripts como envío ya ejecutado. Nunca reenviar listas sin consentimiento. Verificar requisitos actuales de WhatsApp antes de automatizar comunicaciones.

### 10.3 Publicidad de Meta

- Pautar selectivamente: inmueble atractivo y vigente, Santa Isabel con condiciones actuales, contenido educativo de alto valor si tiene sentido comercial.
- Primera ronda con presupuesto controlado y objetivo explícito (mensajes, leads, visita), no «likes» por sí solos.
- Separar alcance orgánico de performance pagado.
- Usar políticas de anuncios inmobiliarios/categorías especiales aplicables, privacidad, autorizaciones de marca.
- Guardar costo por lead calificado, costo por visita, visitas a cierre, inversión, ventas atribuibles cuando sea justificable.
- **Ningún agente sube presupuesto o activa campaña sin autorización explícita.**

### 10.4 Investigación de competencia continua

Auditoría cualitativa de RE/MAX (oficinas/asesores), Propi, Vivo Latam, CityMax y otros asesores relevantes: últimos 20 posts públicos por cuenta, temas, hooks, engagement visible, anuncios visibles, ofertas, estilos, vacíos educativos, sin inventar métricas privadas. Priorizar análisis que derive en experimentos accionables, no informes decorativos.

### 10.5 KPIs del tablero

| Nivel | KPIs | Fuente |
|---|---|---|
| Producción | piezas/semana, tiempo por pieza, tasa aprobación, retrabajo | ContentOps |
| Alcance | reach no seguidor, retención/tiempo de visualización, shares, saves | IG/FB Insights |
| Conversión | clic a WhatsApp, conversaciones, leads calificados, visitas | Meta/UTM/CRM |
| Comercial | propiedades captadas, ofertas, cierres, ingresos atribuidos con confianza | CRM / registros comerciales |
| Costos | horas, créditos IA, herramientas, pauta autorizada | Cost ledger |
| Riesgo | posts bloqueados, errores de precio/estado, duplicados, copyright | QA/incident log |

No fijar cifras «meta» sin línea base real. Las 4,500 personas seguidoras de OLY son un dato de referencia aportado, no una estadística de panel verificada.

---

## 11. Santa Isabel — contenido semanal obligatorio, reglas comerciales especiales

**Proyecto:** Lotificación Santa Isabel, Comacarán, San Miguel, El Salvador. Tratarlo como una propiedad/proyecto de segmento accesible, sin lenguaje de lujo/exclusividad. Reservar un contenido RE/MAX los **viernes**, rotando enfoque: ubicación, proceso de compra, financiamiento, recorrido real, avance/FAQ verificado.

### 11.1 Datos públicos de referencia según conversación reciente

- Precio público: **desde US$24,500 por lote**, sujeto a disponibilidad.
- Mensaje: **«Consulte nuestras condiciones especiales de compra al contado».**
- Financiamiento Banco Industrial: **compra de 2 lotes o más**, con **monto mínimo del crédito de US$40,000**, sujeto a evaluación y aprobación. **US$40,000 es el crédito mínimo**, no automáticamente el valor mínimo de una compra.
- Reservas, planes de pago, estado de servicios, ofertas y lotes disponibles: **revalidar antes de mencionar**.
- Sitio existente: `https://lotificacionsantaisabel.com`. Su actualización web se informó previamente completa. **No asignar una nueva tarea de modificar el sitio sin solicitud específica.**
- Contacto de este sistema para piezas inmobiliarias de Nixon: **+503 7956 4399**, salvo ficha comercial aprobada específica que estipule otra representación.

### 11.2 Datos INTERNOS — PROHIBIDO PUBLICAR AUTOMÁTICAMENTE

Existen referencias históricas a un mínimo interno de negociación al contado de US$22,000 para 10 lotes elegibles, comisiones y condiciones de corredores. Este material es **uso restringido para asesores autorizados, nunca un CTA/publicación pública**. No volcarlo a copys, formularios, metadata pública, logs compartidos, miniaturas, dashboards públicos ni respuestas automatizadas a clientes.

### 11.3 Contradicciones pendientes que requieren bloquear afirmación concreta

- **Reserva:** hubo referencias históricas a US$2,000 y una actualización posterior del usuario a US$500. El centro de trabajo antiguo todavía muestra US$2,000. **No publicar monto de reserva hasta verificar condiciones comerciales vigentes con Nixon/ventas**.
- **Servicios:** documentos de distinta fecha discrepan sobre electricidad/conexión. **No afirmar que un servicio está instalado o listo sin validación actual**.
- **Contacto del sitio:** diferentes archivos históricos nombran a Erika y a Nixon en posiciones distintas. La ficha/representación actual del canal que vaya a publicar debe establecer contacto responsable. No cambiar sitio sin petición expresa.
- **Inventario/financiamiento/tasas:** cualquier cálculo de crédito, tasa o cuota requiere versión actual y aprobación bancaria; no heredar simulaciones antiguas como promesa.

### 11.4 Reglas audiovisuales Santa Isabel

- Mantener fotos originales y fuentes. Si se editan caminos, el acceso es concreto gris claro, calles interiores asfalto gris oscuro, sin inventar servicios, edificios, calles ni geografía.
- Los retoques son mejoras visuales, no alteraciones de condiciones del inmueble.
- El plano/representación 3D esquemática no sustituye levantamiento topográfico ni linderos.
- Las fotografías deben pertenecer realmente al proyecto; evitar visuales IA que aparenten ser tomas actuales.
- Reutilizar `santa-isabel-media-ops` sin mezclar políticas internas sensibles con material exportable.

---

## 12. Nova Aquatics + marca atleta — lanzamiento gradual

### 12.1 Cronología editorial

- 9–17 noviembre: reactivación lifestyle de `@nixonhernandez_`, trabajo real como asesor/empresario, preparación deportiva; no exagerar anuncio de regreso.
- Desde 18 noviembre: serie **«De vuelta al agua»**, seguimiento de entrenamientos, sensaciones, hábitos, técnica y progresión.
- Diciembre: vida de atleta y entrenador, filosofía del club y proyecto de enseñanza; lista de interés opcional cuando se tengan permisos y oferta consistente.
- Enero 2027: presentar **Nova Aquatics** y `nova-aquatics.com` si el sitio, programas, instalaciones, seguridad, capacidad, precios y operación están confirmados.

### 12.2 Programas en consideración — NO oferta comercial confirmada

- Aprender a nadar en aproximadamente un mes (niños/adultos): formular como **programa objetivo**, no garantía de aprendizaje igual para todas las personas.
- Programa PRO personalizado según necesidades del nadador: técnica, natación, dryland/gimnasio, posible nutrición profesional donde sea apropiado y autorizado.
- Entrenamiento y metodología de natación orientados a rendimiento, educación y seguimiento.
- Costeo operativo del club, piscina de FSN, entrenador, equipos y profesionales: línea de trabajo separada que necesita cotizaciones, acuerdos y permisos. No inventar tarifas o instalaciones confirmadas.

### 12.3 Natación y privacidad

El contenido del usuario como deportista puede ser filmado libremente por él donde tenga permiso, pero la imagen, datos, resultados deportivos y testimonios de menores/alumnos requieren autorización del padre/madre/tutor y acceso restringido. No publicar datos de niños desde una base deportiva privada por el simple hecho de existir registros internos.

### 12.4 NBS en contenido personal

Documentar proyectos, problemas resueltos, vida de fundador y automatización útil. No divulgar información de clientes, código propietario, contratos, credenciales ni pantallas con datos empresariales. Evitar confundir marketing NBS con ventas de inmuebles; CTA a negocio separado cuando sea pertinente.

---

## 13. Plan de implementación por etapas — negocio primero

> La automatización no debe desplazar la producción comercial. Cada fase tiene entregable verificable y condición para pasar a la siguiente. Las duraciones son secuencia relativa, no promesas de trabajo asíncrono.

### FASE 0 — Discovery, auditoría y reconciliación (primer bloque)

**Tareas:**

1. Leer este master y `.md` históricos, `AGENTS.md`, `CLAUDE.md` en repos actuales, ramas y docs.
2. Confirmar equipo de Windows (RAM, GPU, CPU, espacio libre, versiones Python/Node, FFmpeg, DaVinci si instalado), disco externo y ruta real, sin escribir/renombrar originales.
3. Inspeccionar `santa-isabel-media-ops`, restos de ContentOps, otras carpetas locales y repos; detectar scripts funcionales, errores e incompatibilidades.
4. Confirmar Canva/Drive/Higgsfield/GitHub como conectados o no, sin suponer permisos. Confirmar Meta y WhatsApp Business **por separado**.
5. Revisar propiedad verificada de REconnect, permiso para marketing y material de muestra.
6. Clasificar `CONFIRMADO / EXISTENTE / HISTÓRICO / NO VERIFICADO / BLOQUEADO`.
7. Registrar ADR si se sustituye una decisión técnica antigua.

**Entregables:** `docs/CURRENT_STATE.md`, `docs/CONNECTORS.md`, `docs/OPEN_QUESTIONS.md`, `docs/DECISIONS.md` y primer tablero de tareas.

**Criterio de salida:** sabemos dónde está el código real, qué contenido se puede usar y qué faltaría para la primera publicación.

### FASE 1 — Primer contenido real (MVP editorial)

1. Seleccionar un clip real de Nixon y una propiedad vigente autorizada.
2. Importar originales sin pérdida; generar proxy, transcripción y EDL.
3. Renderizar un Reel orgánico v1 y un Reel/ficha de inmueble v1.
4. Generar portada, copy adaptado IG/FB, CTA WA y formatos de revisión.
5. Aplicar QA factual y creativo. Nixon elige aprobar/pedir cambios.
6. Dejar lista publicación `HANDOFF` aunque no exista API social.
7. Registrar minutos reales y costos.

**Criterio de salida:** dos contenidos completos y revisables; al menos una publicación manual completada y verificada si Nixon la autoriza.

### FASE 2 — Pipeline local reproducible

1. Watcher/sync de INBOX y manifiesto.
2. Auto-Editor/Whisper/FFmpeg integrados con tests y fallback.
3. Plantillas Remotion/Canva para `ORGANIC01`, `PROPERTY01`, `DATA01`.
4. SQLite/job ledger, render retries y logs, backups.
5. Creative router y presupuesto por proveedor.

**Criterio:** nuevos clips generan un borrador sin rehacer manualmente el proyecto de edición.

### FASE 3 — Review Inbox PC + celular

1. Interfaz web responsive con auth.
2. Preview + copy + variantes + notas por timestamp.
3. Aprobación versionada con content lock.
4. Tailscale Serve o equivalente privado, probado desde su teléfono con PC en línea.
5. Notificaciones de borrador listo (solo canal conectado y autorizado).
6. Recuperación de errores, offline y bloqueo.

**Criterio:** Nixon puede revisar y decidir desde teléfono sin exponer el sistema público.

### FASE 4 — Distribución y control comercial

1. Manual `HANDOFF` como modo seguro por defecto.
2. Confirmar cuentas profesionales, API Meta y permisos reales.
3. `AUTO` solo por API oficial con job aprobado y publicación verificada.
4. Registrar posts, links, métricas y leads por fuente.
5. Crear WhatsApp respuestas rápidas/flujo consentido, CRM y seguimientos.
6. Importación REconnect autorizada, refresh y caducidad de snapshots.

**Criterio:** post publicado/verificado se liga a consultas/visitas, sin duplicados ni envíos no autorizados.

### FASE 5 — Calidad avanzada y escala controlada

1. Presets por marca y campañas.
2. Edición premium con DaVinci y corrección de color cuando tenga ROI.
3. Automatización de analítica/costeos, detección de fatiga creativa.
4. Variaciones A/B de hooks, CTA y formatos.
5. Segundo canal de captación Nova; roll-out enero si está operativo.
6. Considerar nube/postgres/multiusuario solo si hay carga real que lo justifique.

**Criterio:** estabilidad, buenas métricas comerciales, costos controlados y decisiones documentadas.

---

## 14. Backlog priorizado para Jira/GitHub Issues

| ID | Prioridad | Tarea | Responsable propuesto | Criterio de aceptación |
|---|---|---|---|---|
| N360-001 | P0 | Auditoría de repos y MD heredados | Claude Code + ChatGPT | Inventario verificado con links y conflictos |
| N360-002 | P0 | Contratos, conexiones, legalidad de medios y REconnect | Nixon + agente auditor | Matríz CONNECTORS con permisos concretos |
| N360-003 | P0 | Elegir propiedad piloto vigente | Nixon / REconnect | Precio, estado, medios y derecho verificables |
| N360-004 | P0 | Elegir y transferir primer Reel orgánico | Nixon | Original intacto + manifiesto |
| N360-005 | P0 | Editar/QA Reel orgánico v1 | Claude Code | MP4, subtítulos, editable, preview |
| N360-006 | P0 | Editar/QA propiedad v1 | Claude Code + ChatGPT | Reel, portada, copy y CTA correctos |
| N360-007 | P0 | Flujo aprobación manual por carpeta/manifest | Claude Code | Nixon decide y queda registro de versión |
| N360-008 | P0 | Primer handoff para publicación y verificación | Nixon + agente | URL/resultado confirmado, nunca simulado |
| N360-009 | P1 | Montar cola local, observabilidad, backups | Codex / Claude Code | Reanudar tras corte/errores y sin duplicados |
| N360-010 | P1 | Plantillas ORGANIC01/PROPERTY01/DATA01 | Equipo creativo | 3 masters editables aprobados |
| N360-011 | P1 | Review Inbox móvil autenticado | Codex | Prueba real desde teléfono en red privada |
| N360-012 | P1 | CRM/lead attribution | Claude + equipo | Lead ligado a campaña, propiedad y siguiente acción |
| N360-013 | P1 | Integración Meta autorizada | Integrador | Cuenta elegible + formato/permiso probado |
| N360-014 | P1 | Integra Santa Isabel semanal | ContentOps | Publicación con hechos comerciales vigentes |
| N360-015 | P1 | Serie regreso al agua 18 nov | Nixon + editor | Primer episodio aprobado y publicado según permiso |
| N360-016 | P2 | Creative DNA + Canva Audit | ChatGPT + Nixon | 3 direcciones y selección de un sistema |
| N360-017 | P2 | Analítica semanal + competidores | ChatGPT | Informe con fuentes, insights y 3 experimentos |
| N360-018 | P2 | Nova Aquatics lanzamiento | Nixon / Nova | Sitio, oferta, permisos, campaña y medición |

**No abrir simultáneamente múltiples PR para el mismo módulo.** Cada issue necesita scope, archivos permitidos, dependencias y tests.

---

## 15. Métricas operativas y presupuesto

### 15.1 Objetivos de producción iniciales

- 2–3 Reels/semana en OLY, sin obligación de publicar todas las facetas cada día.
- Aproximadamente 4 publicaciones inmobiliarias/semana en RE/MAX y adaptaciones a Facebook (ajustar a material auténtico y ventas activas).
- 1 publicación Santa Isabel los viernes, datos comerciales verificados.
- 25 minutos diarios para leads y visitas.
- Primera revisión semanal con métricas de Instagram/Meta y resultados comerciales.
- Si la carga supera 120 min/día, reducir volumen, agrupar rodajes y mejorar templates antes de añadir software.

### 15.2 Presupuestos que NO son autorizaciones

- Herramientas (Higgsfield, Canva, Remotion en caso de licencia de compañía, servidor, almacenamiento), música y pauta: **pendientes de costos reales y autorización**.
- Cualquier propuesta de US$30–100 de test Ads en chats previos era ilustrativa, **no un gasto aprobado**.
- Crear `cost_budget.yaml` con `max_cost_per_render`, `max_daily_spend`, `max_monthly_spend` y `approval_threshold`; valores se eligen con Nixon, no se inventan.
- Un cambio de herramienta debe justificar tiempo ahorrado, mejora de calidad, licencia, GPU/RAM, costo y sostenibilidad.

---

## 16. Seguridad, ética comercial y controles

**Bloqueos obligatorios:**

- No publicar ni programar sin aprobación humana real ligada a versión.
- No contratar, gastar créditos, activar anuncios, comprar licencias, desplegar sitios o modificar cuentas sin autorización apropiada.
- No consultar credenciales ni hacer login automatizado mediante bypass de captcha/2FA; usuario resuelve autorizaciones normales.
- No subir secretos, bases de clientes, DUI, fichas privadas, contratos, correos internos ni tokens al repo o a prompts no autorizados.
- No publicar por plataformas no oficiales cuando ello viole términos de servicio.
- No presentar edición IA como evidencia fotográfica de características que no existen.
- No fabricar testimonios, compradores, cierres, premios, resultados deportivos o rentabilidades.
- No prometer resultados de inversión, financiación, aprendizaje de natación ni el status legal de propiedades.
- No reutilizar imagen de niños sin consentimiento verificable y específico.
- No usar música, fotos o metraje ajeno sin licencia compatible con publicidad y plataformas.
- No conectar bases de RE/MAX y Nova con marketing cruzado sin base legal/consentimiento.
- No publicar lotes inactivos, precios no vigentes ni servicios dudosos.
- No abrir revisión remota a Internet público sin auth y modelo de amenazas.

**Recomendado:** cifrado de discos/secret manager, backup 3-2-1, control por roles, MFA, rotación y revocación de tokens, variables de entorno, logs de acceso, mínimo privilegio, limpieza de EXIF/metadatos personales en exports públicos, prueba de restore, políticas de retención y borrado seguro de PII.

---

## 17. Fallos y recuperación — acciones deterministas

| Código | Problema | Control / respuesta |
|---|---|---|
| F001 | Precio viejo | Caducidad de snapshot, bloquea y revalida |
| F002 | Propiedad vendida | Cancelar programación y avisar |
| F003 | Fotos mezcladas | IDs/hashes; vínculo property/media; bloquea |
| F004 | Alucinación de copy | Fact checker + evidence ledger |
| F005 | Publicación duplicada | Idempotency key y verificación remota |
| F006 | Estética IA genérica | Creative DNA y auditoría humana |
| F007 | Desvío de marca | Brand rules, calidad y rotación templates |
| F008 | Gasto excesivo de créditos | Credit Governor y presupuesto aprobado |
| F009 | Cola de aprobaciones saturada | Dashboard priorizado por valor/tiempo |
| F010 | API externa cae | Reintentos/fallback HANDOFF, sin mentir |
| F011 | PC apagada | Estado OFFLINE y reanudación posterior; no promesas |
| F012 | Publicar versión antigua | Content hash + lock + pointer immutable |
| F013 | Repetición excesiva | Historial uso de templates y cooldown |
| F014 | Pérdida de archivos | Hash + backups + restore test |
| F015 | Carrera entre agentes | Leases, branches, PR y task owner |
| F016 | Métricas mal atribuidas | Fuente/periodo/definición y confidence |
| F017 | Licencia ausente | Bloqueo por derechos sin evidencia |
| F018 | Video IA confundido con propiedad real | Disclosure y QA factual |
| F019 | Dato registral interpretado mal | Nivel de evidencia, revisión profesional |
| F020 | Notificación/aprobación desde móvil comprometida | Login fuerte, audit log, expiración, revoke |
| F021 | Niño o cliente identificable sin permiso | Contenido bloqueado y eliminación controlada |

---

## 18. Definición de entregables de la primera prueba

**El agente NO termina únicamente con una propuesta; cuando tenga materiales y conexiones debe crear archivos reales verificables.**

Paquete mínimo de un video orgánico:

```text
content_id/
├── original_manifest.json
├── transcript_es.srt
├── edit_plan.json
├── preview_low.mp4
├── master_1080x1920.mp4
├── cover_4x5.png
├── copy_instagram.md
├── copy_facebook.md
├── rights_and_sources.md
├── qa_report.json
└── approval_status.json
```

Paquete mínimo de video inmueble: mismo esquema + `property_snapshot.json` + `media_authorizations.json` + `whatsapp_message_draft.md` y, de ser posible, ficha PDF opcional autorizada.

Condiciones de aceptación:

1. Render se abre, sin cortes defectuosos/títulos cortados y audio entendible.
2. Los archivos fuente originales se mantienen intactos.
3. Hay una forma de editar texto, clips y precio sin rehacerlo todo.
4. Precio, disponibilidad y rasgos del inmueble corresponden a la fuente autorizada actual.
5. Se puede revisar desde el teléfono de manera segura, o existe procedimiento HANDOFF claro mientras se termina el panel.
6. Sin aprobación no existe job de publicación habilitado.
7. La publicación real, si ocurre, incluye URL/ID verificable.
8. Se registra tiempo empleado y costos de proveedores.

---

## 19. Formatos de scripts y briefs que deben generar los agentes

### 19.1 Brief editorial

```yaml
content_id: "N360-20261109-0001"
brand: nixon-remax
account: instagram_remax
objective: "qualified_whatsapp_leads"
series: "property-feature"
format: "reel_9x16"
primary_audience: "buyer"
property_id: "[verified ID]"
problem_or_insight: "[problema real del comprador]"
hook: "[frase breve]"
key_claims: []
evidence_ids: []
asset_ids: []
required_shots: []
video_duration_target_sec: 25
cta: "Consultar por WhatsApp"
constraints:
  - "Real media only for property"
  - "No unverified specs"
  - "Commercial information must be current"
status: "DRAFT"
```

### 19.2 Guion con shots

```text
CONTENIDO:
OBJETIVO:
CANAL:
HOOK (0-2s):
CUERPO (2-20s):
DEMO / IMAGEN REAL:
CIERRE (20-30s):
CTA:
REQUIERE GRABACIÓN DE NIXON: SÍ/NO
SHOT LIST (5-8 clips):
FUENTES Y DATOS A VALIDAR:
EDICIÓN PROPUESTA:
MÚSICA: licencia verificada / ninguna
ESTILO: editorial / documental / cinematográfico
```

### 19.3 QA editorial

```yaml
facts_verified: false
property_active_verified: false
media_rights_verified: false
music_rights_verified: false
phone_and_links_verified: false
brand_reviewed: false
caption_readable: false
video_playback_verified: false
kid_or_client_privacy_checked: false
approval_by_nixon: false
publish_authorized: false
publish_mode: HANDOFF
warnings: []
blocking_issues: []
```

Si una condición obligatoria es falsa, el agente crea un borrador y señala el bloqueo, no da el contenido por publicable.

---

## 20. Instrucciones listas para iniciar a Claude Code (PRIMER COMANDO DE TRABAJO)

**Copiar este bloque como instrucción de arranque después de cargar el archivo `.md`.**

```text
Eres el arquitecto y ejecutor local de NIXON 360 / CONTENTOPS. Lee COMPLETO el archivo NIXON360_CONTENTOPS_MASTER_2026-11-08.md y trata su sección 0 como reglas obligatorias. No escribas código todavía.

1. Inspecciona los repositorios, archivos MD, AGENTS.md/CLAUDE.md existentes y la estructura accesible del equipo/Drive. No confundas BuscaBot con ContentOps; conserva la arquitectura actual de BuscaBot.
2. Produce un CURRENT_STATE real con evidencia (repos, carpetas, herramientas instaladas, conexiones autorizadas, material existente), distinguiendo HISTÓRICO, OBSERVADO, PROPUESTO y BLOQUEADO.
3. Enumera las discrepancias comerciales y de privacidad que impiden publicar datos sin revalidar.
4. Propón una decisión de arquitectura MVP local-first compatible con Windows, publicación HANDOFF inicial, Review Inbox móvil privado futuro y conexiones oficiales.
5. Define backlog P0 y las dos primeras pruebas reales: Reel orgánico Nixon y Reel de propiedad verificada.
6. Revisa las licencias y dependencias antes de instalar software; especial atención a Remotion.
7. Entrega la ruta del repositorio auditado, la rama propuesta, pruebas y una propuesta de PR, sin modificar main ni publicar nada.
8. Al terminar deja HANDOFF_LATEST.md y TASK_BOARD.md; asigna a Codex módulos bien delimitados, no trabajo duplicado.

No pidas de nuevo información ya documentada. Si hay bloqueo verdadero, continúa con las tareas independientes.
```

### 20.1 Instrucción recurrente a ChatGPT

```text
Actúa como estrategia/QA editorial de NIXON 360. Lee CURRENT_STATE, HANDOFF_LATEST, las reglas de marca y el brief de contenido. Investiga fuentes públicas, escribe guion y CTA orientado a negocio cuando corresponda, verifica claims e identifica contradicciones. No afirmes disponer de accesos que no están conectados ni publiques. Deja brief, evidence ledger, propuesta de mejoras y estado claro para Claude Code/Codex.
```

### 20.2 Instrucción recurrente a Codex

```text
Trabaja exclusivamente en [ISSUE] del repo verificado y rama feature/[ISSUE]. Lee AGENTS.md, CLAUDE.md solo si aplica, y reglas locales. Implementa [MODULO] con tests, idempotencia, observabilidad y seguridad. No toques publicación, datos privados, main ni funciones fuera del alcance. Corre pruebas disponibles y entrega PR + handoff para que Claude Code pueda integrar sin conflictos.
```

### 20.3 Instrucción recurrente a Claude para producción audiovisual

```text
Lee el brief/content_id y sus media assets autorizados. Usa primero originales reales. Transcribe, propone EDL, genera una edición que respete ritmo natural y datos, pasa QA técnico y factual, exporta preview y master editable. Presenta al usuario la versión y dos opciones SOLO si mejora la decisión. No publiques, no cambies precios ni gastes créditos de Higgsfield sin autorización. Si la grabación requiere regrabar una frase, identifícala con timestamp y texto preciso.
```

---

## 21. Matriz de conexiones — estado inicial SIN suposiciones

| Servicio | Disponibilidad observada en conversaciones previas / herramientas | Lo pendiente |
|---|---|---|
| GitHub | Conector de ChatGPT disponible; tres repos observados | Comprobar repo definitivo, ramas, permisos y código |
| Google Drive | Conector disponible; carpeta Santa Isabel referenciada | Crear/definir raíz multimarca sin duplicar y validar permisos de Claude |
| Canva | Conector disponible; Brand Kit histórico identificado | Confirmar kit, templates y uso actual |
| Higgsfield | Conector disponible y historial de producción previo | Balance actual, licencias/costos, assets existentes |
| REconnect | Usuario indica base RE/MAX | Export/API/consentimiento; **NO confirmada conexión directa** |
| Disco externo | Usuario indica biblioteca física | Ruta, acceso, permisos y capacidad; **NO visible desde ChatGPT cloud** |
| Claude/Claude Code | Usuario lo utiliza | Verificar instalaciones locales, versión, acceso a repos y disco |
| Codex | Disponible como colaborador técnico propuesto | Cuenta/entorno, archivos y flujo PR efectivo |
| Instagram OLY | Cuenta identificada por usuario | Tipo de cuenta, permisos, Insights, formato API |
| Instagram Nixon RE/MAX | Cuenta identificada por usuario | Cuenta profesional/permisos y autorización de publicación |
| Facebook personal/Page | Cuentas referidas por usuario | Identificadores, roles y capacidades reales |
| WhatsApp Business | Canal deseado | Confirmar app/Business Platform, catálogo, permisos y consentimiento |
| Metricool | Sugerido anteriormente | No asumir instalado/conectado |
| Tailscale Serve | Arquitectura propuesta | No asumir instalado; configurar y testear si se aprueba |
| Nova site | Dominio/objetivo declarado por usuario | Verificar DNS, web, oferta y lanzamiento real |

---

## 22. Investigación de tecnologías y referencias oficiales

Las siguientes referencias se deben volver a comprobar al momento de instalar, por cambios de versiones/licencias/API:

**Claude Code / instrucciones:**
- Anthropic, skills/AGENTS/rules/subagents: `https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more`
- Claude Code power user tips: `https://support.claude.com/en/articles/14554000-claude-code-power-user-tips`

**Codex:**
- Documentación AGENTS: `https://learn.chatgpt.com/docs/agent-configuration/agents-md`
- Receta de flujo con Codex: `https://github.com/openai/openai-cookbook/blob/main/examples/codex/iterating-development-workflows-with-codex.md`

**Video:**
- Remotion repo: `https://github.com/remotion-dev/remotion`
- Remotion AI Skills: `https://www.remotion.dev/docs/ai/skills`
- Remotion licenciamiento: `https://www.remotion.dev/docs/license/pricing` y `https://www.remotion.dev/docs/terms`
- Auto-Editor: `https://github.com/WyattBlue/auto-editor`
- Whisper: `https://github.com/openai/whisper`
- FFmpeg: `https://ffmpeg.org/`
- Motion Canvas: `https://github.com/motion-canvas/motion-canvas`
- LosslessCut: `https://github.com/mifi/lossless-cut`

**Red y publicación:**
- Tailscale Serve (privado): `https://tailscale.com/docs/features/tailscale-serve`
- Meta Instagram content publishing: `https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/content-publishing`
- Instagram API oficial de Meta (Postman): `https://www.postman.com/meta/instagram/documentation/6yqw8pt/instagram-api`
- Política WhatsApp Business: `https://whatsappbusiness.com/policy/`

**Datos oficiales El Salvador:**
- Geoportal Censo 2024: `https://poblacion.bcr.gob.sv/`
- Resultados Censo 2024: `https://censo2024.bcr.gob.sv/`
- BCR descargas: `https://www.bcr.gob.sv/descargas/`
- CNR: `https://www.cnr.gob.sv/`
- OPAMSS: `https://opamss.org.sv/` (comprobar vigencia de URL/servicios)

**No copiar instrucciones de repositorios desconocidos a ciegas.** Una skill pública de GitHub puede contener comandos peligrosos o licencias incompatibles. Auditoría mínima: reputación, mantenimiento, código, permisos, tráfico de datos, dependencias, licencia y sandbox de ejecución. Nunca instalar scripts con secretos habilitados sin revisión.

---

## 23. Criterios para decidir si la arquitectura realmente funciona

**Prueba E2E A — Reel orgánico:**
1. Nixon sube vídeo de prueba.
2. INBOX registra original e integridad.
3. Worker transcribe y propone edición.
4. Preview aparece en panel/Drive autorizado.
5. Nixon pide un cambio en el segundo 8 y recibe versión nueva.
6. Nixon aprueba versión exacta.
7. Sale `HANDOFF` a Instagram OLY; publicación manual verificada si procede.
8. Se registran minutos y feedback.

**Prueba E2E B — Propiedad inmobiliaria:**
1. Snapshot vigente de una propiedad y fotos autorizadas.
2. Guion solo utiliza campos verificados.
3. Render y QA detectan precio/propiedad/fotos correctos.
4. Nixon aprueba contenido y, separadamente, la publicación.
5. Enlace WhatsApp o mensaje preparado lleva `property_id`/`campaign_id` cuando técnicamente compatible.
6. Una consulta de prueba llega a CRM con fuente y siguiente paso (sin exponer PII en logs públicos).
7. Si cambia el estatus antes de postear, publicación se bloquea.

**Prueba E2E C — Móvil:**
1. Conexión privada autenticada desde celular.
2. Puede reproducir preview, ver detalles, pedir cambio y aprobar.
3. Un tercero sin acceso no puede verlo ni aprobar.
4. PC fuera de línea se muestra como fuera de línea, sin simular tareas terminadas.

**Prueba E2E D — Resiliencia:**
1. Cortar/reiniciar worker durante render.
2. Recuperar trabajo sin publicar doble.
3. Rechazar una versión vieja aprobada si se altera precio/copy.
4. Restaurar desde respaldo de prueba.

---

## 24. Lo que se solicita ahora y lo que NO está hecho

**Solicitado en esta conversación:** crear un `.md` maestro legible para Claude, Claude Code, Codex, ChatGPT y otros LLMs, incorporando todo el contexto de marca/ventas/ContentOps y un flujo de creación, revisión y aprobación automatizable desde computadora o teléfono.

**Estado al generar este documento:** documento maestro redactado, fuente histórica consultada en Library/Drive y repositorios observados con conector GitHub. **NO se ha instalado el stack local, desplegado panel, conectado REconnect, montado Tailscale ni publicado en redes.** Son fases de ejecución posteriores que requieren acceso al entorno local y permisos reales.

**Próxima acción inmediata para Claude:** ejecutar `FASE 0`, comparar archivos históricos y repos actuales, producir CURRENT_STATE y probar el primer Reel/propiedad. Mantener 2h de Nixon como límite real y priorizar ventas sobre infraestructura.

---

## 25. Cierre — regla de producto

> **Nixon pone la historia, el criterio y la aprobación. ContentOps convierte material auténtico y datos verificables en piezas de calidad. Instagram/Facebook generan interés. WhatsApp y CRM convierten ese interés en visitas y ventas. Nova y NBS aprovechan la confianza sin diluir el objetivo inmobiliario.**

La excelencia del sistema se medirá por: **contenido real publicable, control humano, tiempo ahorrado, calidad, continuidad de marca, leads calificados y oportunidades comerciales concretas**. No por cuántos modelos, skills o agentes aparecen en su arquitectura.

**FIN — NIXON360-CONTENTOPS-MASTER v1.0**
