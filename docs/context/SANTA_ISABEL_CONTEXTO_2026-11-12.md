# Santa Isabel — contexto de producción (para Codex, ChatGPT y Claude)

Proyecto: `N360-20261112-0001` · Lotificación Santa Isabel, Comacarán, San Miguel · Asesor: Nixon Hernández (RE/MAX).
Estado: **borrador, modo HANDOFF. Nada se publica sin aprobación explícita de Nixon.**

## 1. Dónde está cada cosa
| Qué | Dónde | En GitHub |
|---|---|---|
| Reglas, skills, estilo | este repo (`AGENTS.md`, `.claude/skills/`, `brands/nixon-remax/`) | Sí |
| Kit único de marca y motion | `brands/nixon-remax/motion_kit/kit_nixon_remax.json` | Sí |
| Script de mocks / paneo desde foto | `brands/nixon-remax/motion_kit/` | Sí |
| Originales, proxies, renders, fotos | `E:\NIXON360_CONTENTOPS`, `E:\Lotificación Alvarez`, `E:\SAN MIGUEL` | **No** (disco externo) |
| Datos verificados | `E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001\property_snapshot.json` | No (pegar si se necesita) |

## 2. Reglas duras (acumuladas)
1. Solo datos del snapshot: desde **US$24,500**, desde **286 v²**, **con escritura**, **agua conectada**, Comacarán, San Miguel, +503 7956 4399.
2. Banco Industrial: solo con asterisco «*Financiamiento con Banco Industrial sujeto a evaluación del banco.» y «Sujeto a disponibilidad.»
3. Sin fechas en pantalla. Sin reserva, electricidad, negociación, comisiones ni cuotas.
4. Clientes de usted. Cierre: «Escríbanos para agendar su visita» y solo el número.
5. **Artes y piezas fijas: nunca usar fotos con calles sucias.** Usar las editadas de `E:\Lotificación Alvarez\_marca\fotos_limpias\` (7 fotos `SI_FOTO_*_v01.jpg`, 1672×941) u otras editadas nuevas.
6. Logo Banco Industrial: **sin placa de color**; versión monocroma blanca con sombra sobre fondos oscuros (el original azul marino no se lee sobre el terreno). Logo RE/MAX sin recolorear (el oficial blanco/color).
7. Estilo de texto «en capas» (ver `brands/nixon-remax/design_dna_texto_viral.md`). Los pines, el contorno, los logos y el cierre salen **siempre** del kit; no inventar variantes por video.
8. Zona segura 9:16 (1080×1920): 250 px arriba, 350 abajo, 60 laterales. 4:5 (1080×1350): 120/160/50. No es medida oficial de Meta: validar en el teléfono.
9. Música solo de bibliotecas gratuitas con licencia registrada. Originales en solo lectura. Trabajar en rama, nunca en `main`.

### ⚠ Material antiguo que contradice lo anterior
`E:\Lotificación Alvarez\_marca\kit_chatgpt\*` y `LEEME.txt` traen datos **obsoletos o restringidos**: precio US$24,000, reserva US$500, «luz en proceso», tope negociable, contacto de Erika. **No usar nada de eso en pantalla.** Manda el snapshot.

## 3. Cierre estándar (editable) — v2 aprobado en mocks
- La lotificación es la protagonista: fondo a pantalla completa, solo sombras para leer, sin placas.
- Arriba: logo Santa Isabel. Frase «Escríbanos para agendar su visita». Teléfono grande en amarillo `#ECD628` (Impact).
- Fila inferior: foto de Nixon recortada (pequeña, a la izquierda) · RE/MAX + Banco Industrial (centro) · firma «Nixon Hernández» en cursiva (derecha). Leyendas legales dentro de la zona segura.
- Animación: la foto entra con zoom in y termina con zoom out (valores en el kit).
- Para **RE/MAX Eleva**: copiar el kit, cambiar foto, firma, teléfono y logo. El resto no se toca.

## 4. Material nuevo: `E:\SAN MIGUEL` (9 de octubre de 2026, misma lotificación, GPS 13.527, -88.062)
- 23 videos únicos (las «- copia» son duplicados). 4K HDR horizontales (0554–0560, 0569, 0570, 0574–0578), 1080p verticales (0064–0069), 1080p horizontales (0060–0063). Sin audio. 20 fotos JPG de dron.
- Cenitales útiles para contorno/pines: 0558, 0559. Generales: 0554, 0555, 0556, 0557, 0560. Calle a nivel del suelo: 0060–0063, 0065, 0066. Nixon en cámara: 0064, 0574–0578, 0068. Ascensos: 0570, 0574, 0575, 0578. Descartar: 0067, 0069 (pasto de cerca).
- Plan de 6 videos con ganchos y tomas distintas pero coherentes: (1) desde el aire, (2) contorno y pines, (3) calles y accesos, (4) asesor presenta, (5) entorno, (6) ascenso.

## 5. Videos con calles limpias — qué se puede hacer
- **Desde fotos limpias (recomendado, gratis):** `brands/nixon-remax/motion_kit/paneo_foto.py` genera push-in, pull-out, panorámicas y «reveal» con FFmpeg. Probado con `SI_FOTO_calles-internas_v01.jpg` (4:5): se ve bien. En 9:16 las fotos de 941 px de alto se ven suaves; preferir 4:5/16:9 o ampliar antes.
- **Dentro de FilmCraft:** tiene máscaras con seguimiento (`masks.add`, `masks.track`) y efectos de color. Sirve para oscurecer/neutralizar el polvo de la calle en tomas estables. **No tiene relleno generativo**: no borra tierra ni huellas. Es experimental y puede verse falso. No verificado en este proyecto.
- **IA imagen-a-video (estilo Higgsfield):** requiere créditos y subir fotos a un servicio externo. Solo con permiso de Nixon. Las piezas con IA llevan la leyenda «Imagen ilustrativa — se vende el terreno, no incluye construcción.»

## 6. Cómo repartir la carga
| Herramienta | Hace | No hace |
|---|---|---|
| **Claude Code (PC de Nixon)** | Render, recorte de foto (rembg), seguimiento de contorno (OpenCV), motor del kit, exportes | — |
| **Codex (en la PC o el repo)** | Scripts del repo, refactor del motor para que lea el kit, pruebas, documentación, `paneo_foto.py` en lote | No ve el disco externo si corre en la nube |
| **ChatGPT (navegador)** | Ganchos, copy IG/FB, hashtags, CTA wa.me, calendario, ideas de artes y prompts | No renderiza ni lee `E:\` |

## 7. Plantillas de prompt
**Codex:** «Lee `AGENTS.md`, `docs/context/SANTA_ISABEL_CONTEXTO_2026-11-12.md` y `brands/nixon-remax/motion_kit/kit_nixon_remax.json`. En una rama `feature/N360-0XX-...` convierte `mock_kit.py` en un módulo que reciba `kit.json` y un `guion.json` y produzca fotogramas por formato (9x16 y 4x5). No toques `main`. Entrega PR con pruebas.»

**ChatGPT:** «Con estos datos verificados [pegar snapshot] escribe 3 ganchos de 3 segundos (de usted, sin fechas) para el video 2 (contorno y pines) y el copy de IG (máx. 150 palabras) con 12 hashtags y CTA a wa.me/50379564399. Lista de qué campo sale cada dato.»

**ChatGPT (artes):** «Usa solo fotos con calles limpias. Propón 5 artes 4:5 con el estilo en capas del kit; texto de usted; Banco Industrial con asterisco.»

## 8. Pendiente
- Voz de Nixon (los clips de dron no tienen audio); retemporizar subtítulos.
- Confirmar con Nixon dónde marcar pines (alcaldía, carretera principal, otros).
- Decidir si las fotos de calles limpias editadas llevan la leyenda «Imagen ilustrativa».
- Motor del kit + video 2 con vista previa; luego los otros 5 y las versiones 4:5.
- `prepublish-qa` y aprobación explícita antes de cualquier publicación.
