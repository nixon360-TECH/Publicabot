# Reglas para trabajar en paralelo (Claude Code · Codex · ChatGPT)

Objetivo: que cualquiera pueda **leer lo que otro creó** y continuar sin pisarlo. Aplica a Santa Isabel (`N360-20261112-0001`) y a los proyectos siguientes.

## 1. Orden de lectura obligatorio (al empezar)
1. `AGENTS.md` y `NIXON360_CONTEXT_MASTER.md` (sección 0 y §11).
2. `docs/context/SANTA_ISABEL_CONTEXTO_2026-11-12.md` (estado, reglas, cierres, material).
3. `docs/plan/PLAN_8_VIDEOS_SANTA_ISABEL.md` (qué toca a quién).
4. `brands/nixon-remax/motion_kit/kit_nixon_remax.json` (el kit único) y `brands/nixon-remax/design_dna_texto_viral.md`.
5. `E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001\puntos_confirmados.json` y `property_snapshot.json` (datos verificados).

## 2. Quién escribe dónde
| Agente | Prefijo de archivos y carpetas | Carpetas propias |
|---|---|---|
| Claude Code | `claude_` (o nombres ya existentes en `build\` y `_KIT\`) | `…\N360-…\build\`, `…\_KIT\`, renders `…_v0X.mp4` |
| Codex | `codex_` | `05_RENDERS_DRAFT\N360-…\codex_*`, ramas `codex/…` |
| ChatGPT | `chatgpt_` | solo texto: guiones, copy, prompts; Nixon los pega en `coordination\` o `docs\` |

- **Nunca** editar, mover ni borrar un archivo de otro agente. Si hay que cambiarlo, pedirlo en `coordination/HANDOFF_LATEST.md`.
- Originales (`E:\Lotificación Alvarez`, `E:\SAN MIGUEL`): solo lectura para todos.
- Nunca en `main`: rama `feature/N360-XXX-…` (Claude), `codex/N360-XXX-…` (Codex) y PR.

## 3. Manifiesto de producción
Cada agente deja, junto a lo que produce, un `manifest.json` (o lo agrega a uno existente) con: `agente`, `fecha_hora`, `entrada(s)`, `script`, `salida(s)`, `estado` (`borrador|en_revision|aprobado`), `notas`. Así se sabe quién hizo qué sin adivinar por el nombre.

## 4. Reglas de contenido que no se negocian
Ver sección 2 del documento de contexto: solo datos del snapshot, usted, sin fechas, Banco Industrial con asterisco, sin reserva ni electricidad, artes solo con calles limpias, nombres de calles y puntos solo los de `puntos_confirmados.json`, zona segura, nada se publica sin aprobación de Nixon.

## 5. Estilo
El estilo (texto en capas, pines, contorno, logos, cierre) sale **siempre** del kit. Ningún agente inventa variantes. Para cambiar el kit: proponerlo, que Nixon apruebe, y se versiona (`version` del JSON).

## 6. Qué puede cada uno (honesto)
- **Claude Code / Codex (en la PC):** leen `E:\`, renderizan, mezclan audio.
- **ChatGPT (navegador):** no ve `E:\`; no renderiza. Solo texto, ideas y artes a partir de imágenes que Nixon suba.
