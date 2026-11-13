# Plan: 8 videos de Santa Isabel (mínimo 2 versiones cada uno)

Estado: **borrador de plan**. Se ejecuta cuando Nixon apruebe los **dos primeros clips** (v06 del reel «desde el aire» y el video 2 «calles asfaltadas»). Nada se publica.

Supuesto a confirmar con Nixon: «8 videos, de 2 versiones mínimo» = 8 piezas distintas y cada una con ≥2 versiones (por ejemplo gancho A/B/C y formatos 9:16 y 4:5).

## 1. Material disponible
- **Vuelo 4 jul. 2026** (`E:\Lotificación Alvarez`): 10 videos (0192–0201 y «Video aéreo de frente de la calle»), 9 fotos, SRT con GPS. Tomas del pueblo (0199, 0192, 0198, 0197), lote (0193, 0196, 0201) y órbita.
- **Vuelo 9 oct. 2026** (`E:\SAN MIGUEL`): 23 videos únicos (4K HDR, 1080p vertical) + 20 fotos. Cenitales 0558/0559; generales 0554–0557, 0560; calle a nivel del suelo 0060–0063, 0065, 0066; **Nixon en cámara** 0064, 0068, 0574–0578; ascensos 0570, 0574, 0575, 0578. Descartar 0067, 0069. Sin audio.
- **Fotos limpias** (`_marca\fotos_limpias`, 7 fotos de calles sin tierra): única fuente para artes y paneos desde foto. No usar `calles-internas`.
- **Guiones:** `guion_v1.md` (ganchos A/B/C y cuerpo), `BRIEF_ChatGPT_Santa_Isabel.md` (**contiene datos obsoletos: no usar**).
- **Puntos confirmados:** `puntos_confirmados.json` (calles, parque central, instituto, Calle al Jicaral).

## 2. Los 8 videos
| # | Video | Gancho / idea | Tomas | Versiones mínimas |
|---|---|---|---|---|
| 1 | Desde el aire (v06) | «Antes de decidir, conózcalo desde el aire.» | Vuelo jul. + pines | A/B/C de gancho · 9:16 y 4:5 |
| 2 | Calles asfaltadas | «Paz y tranquilidad a minutos de la ciudad.» | Foto limpia + trazo | 9:16 y 4:5 · 2 cierres |
| 3 | Precio y condiciones | «Terrenos desde 24,500 dólares. Con escritura y agua conectada.» | Cenitales oct. + contadores | gancho B · con/sin voz |
| 4 | Su asesor presenta | Nixon en cámara en la calle | SAN MIGUEL 0064, 0068, 0574–0578 | 2 recortes de gancho |
| 5 | Junto al pueblo | Parque central, instituto, Calle al Jicaral | Vuelo jul. (0197–0199, 0192) + pines | 2 órdenes de pines |
| 6 | Ascenso | Del suelo al aire | 0570, 0575, 0578, 0574 | 2 ritmos de música |
| 7 | Recorrido desde foto limpia | Paneos sobre las 6 fotos limpias | `fotos_limpias` | 9:16 y 4:5 (Codex ya hizo un piloto) |
| 8 | Visita | «Escríbanos para agendar su visita» | Calle a nivel + Nixon | 2 llamadas a la acción |

## 3. Reparto por calidad
| Quién | Hace | Por qué |
|---|---|---|
| **Claude Code** | Motor del kit (config por video), videos con pines/trazos/contadores (1, 2, 3, 5), mezcla de audio y subtítulos tras la voz, verificación de datos, `prepublish-qa` | Tiene el contexto del estilo y renderiza en la PC |
| **Codex** | Videos 6 y 7 y los reexportes 4:5/variantes de todos, a partir de la plantilla ya aprobada; pruebas y documentación del repo | Tarea repetitiva sobre un molde ya fijado |
| **ChatGPT** | 3 ganchos y guion de voz por video, copy IG/FB, hashtags, CTA `wa.me/50379564399`, calendario, ideas de portada | Escribe bien y rápido; **no** ve `E:\` ni renderiza |
| **Nixon** | Graba las 8 voces de una sola sentada, elige entre versiones, aprueba | Decide |
| Video 4 y 8 | Claude (edición) con guion de ChatGPT | Requieren voz y subtítulos |

## 4. Ejecución (después de aprobar los dos primeros)
0. **Congelar el kit v1.0** (etiqueta en el repo). Sin cambios de estilo después.
1. **Motor por configuración** (Claude): un `video.json` por pieza (tomas, textos, pines, cierre, música). Codex y Claude lo usan.
2. **Paquete de textos** (ChatGPT): ganchos A/B/C, guion de voz y copy de los 8 videos; Claude revisa contra el snapshot.
3. **Producción en paralelo:** Claude → 1, 2, 3, 5; Codex → 6, 7; Claude → 4 y 8 cuando haya voz.
4. **Música:** una pista libre por video (registrada con hash y licencia); variantes de ritmo para el 6.
5. **QA:** `property-fact-check` y `prepublish-qa` a cada pieza; reporte por video.
6. **Sesión de voz:** Nixon graba los 8 guiones; se re-temporizan los subtítulos y se baja la música automáticamente al hablar.
7. **Revisión de Nixon** con vistas previas ligeras por pieza; ajustes; aprobación.
8. **Entrega en modo HANDOFF** (sin publicar): carpeta por video con 9:16, 4:5, portada, copy y manifiesto.

## 5. Riesgos
- Fotos limpias de 941 px de alto se ven suaves en 9:16 (preferir 4:5 o ampliarlas).
- Los pines sobre video en movimiento pueden desfasarse: se usan solo en tomas lentas y se revisan en la vista previa.
- Música con «Content ID registered»: puede haber reclamos en redes; elegir pistas sin esa marca cuando se pueda.
- Dos agentes pisándose: respetar `coordination/MULTI_AGENTE_REGLAS.md`.
