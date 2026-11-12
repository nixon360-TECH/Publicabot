# AGENTS.md — PublicaBOT

Reglas para cualquier agente: Claude Code, Claude por Dispatch, Codex o ChatGPT con acceso al repo.

## Leer antes de trabajar
1. `NIXON360_CONTEXT_MASTER.md`: contexto completo. Su **sección 0 es obligatoria**.
2. `docs/style/STYLE_DECISIONS.md`: cómo se ve, suena y se edita todo.
3. `docs/CURRENT_STATE.md` y `coordination/HANDOFF_LATEST.md`: qué existe hoy de verdad.
4. `coordination/TASK_BOARD.md`: tomar una tarea, poner `owner` y rama antes de editar.

## Misión
Convertir material real de Nixon y propiedades verificadas en piezas listas para IG/FB/WhatsApp que generen **consultas, visitas y cierres**. La automatización sirve a las ventas, no al revés. Nixon dedica como máximo 120 min al día.

## Límites duros (nunca)
- Publicar, programar, enviar WhatsApp, activar anuncios o gastar dinero o créditos sin aprobación explícita de Nixon ligada a una versión concreta.
- Inventar precio, metraje, servicios, estado legal o características de una propiedad. Si un dato no está verificado, se omite o la pieza se bloquea (`BLOCKED_FACTS`).
- Publicar datos internos de Santa Isabel (mínimos de negociación, comisiones) ni montos de reserva sin revalidar (master §11).
- Subir a Git secretos, tokens, PII de clientes, DUI, contratos o videos originales.
- Saltarse CAPTCHAs o 2FA, usar APIs no oficiales o automatizar clics que violen términos de servicio.
- Usar voz o avatar IA de Nixon sin autorización escrita **por pieza**.
- Instalar software de pago. Solo ChatGPT y Claude son de pago; todo lo demás debe ser gratis u open-source, auditado antes de instalar (licencia, mantenimiento, permisos).
- Trabajar en `main`. Todo cambio va en rama `feature/N360-XXX-...` con PR.

## Forma de trabajo
- Las etiquetas de estado son `CONFIRMADO_USUARIO`, `OBSERVADO`, `HISTÓRICO`, `PROPUESTO`, `PENDIENTE` y `BLOQUEADO`. No mezclarlas.
- Si una función determinista resuelve el problema (validar precio, checksum, permisos), se programa así y no se usa un LLM.
- Si hay un bloqueo real, continuar con las tareas independientes y dejarlo escrito en `docs/OPEN_QUESTIONS.md`.
- Al terminar cada tarea, actualizar `coordination/HANDOFF_LATEST.md` y `TASK_BOARD.md` con lo hecho, lo probado, lo pendiente, la evidencia (archivos y commits) y el siguiente paso. Planear no cuenta como ejecutar.
- Dos agentes no editan el mismo módulo a la vez.

## Medios
- Los originales viven en `MEDIA_ROOT` (disco externo o carpeta definida en `.env`) y se tratan como **solo lectura**. Nunca se renombran ni se sobrescriben.
- Estructura de carpetas: master §5.3. Paquete de entrega por pieza: master §18.
- Formato final: 1080×1920 (9:16) para Reels e Historias; 1080×1350 (4:5) para portada y carrusel.

## Publicación
El modo por defecto es **HANDOFF**: el sistema entrega el paquete (video, portada, copy IG/FB, hashtags, CTA y checklist) y Nixon lo programa en Meta Business Suite. La publicación por API es de la Fase 4 y requiere autorización aparte.

## Comandos
Todavía no hay código. Cuando exista, documentar aquí **solo comandos probados**.
