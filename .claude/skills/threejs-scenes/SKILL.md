---
name: threejs-scenes
description: Escenas 3D con Three.js (modelos GLTF, luces, cámaras, partículas) para piezas de PublicaBOT, p. ej. maqueta de lote, plano animado o fondo 3D. Usar solo si la pieza pide 3D; para video normal usar filmcraft-edit.
---

# threejs-scenes

Escrita por Claude desde conocimiento general (no es copia de ninguna skill externa). Marcar como OBSERVADO hasta probarla con una pieza real.

## Cuándo
Maquetas de lotificación, extrusión de polígonos de lote, recorridos virtuales, fondos con partículas. **No** para sustituir tomas reales de dron.

## Flujo
1. Proyecto HTML aislado en `MEDIA_ROOT/04_PROJECTS_EDITABLE/<content_id>/web3d/` (Vite o un solo `index.html`, Three.js con versión fijada, sin CDN desconocidos).
2. Escena: `WebGLRenderer({antialias:true, preserveDrawingBuffer:true})`, `PerspectiveCamera`, luz direccional con sombras + `HemisphereLight`, `tone mapping ACESFilmic`.
3. Modelos GLTF/GLB: solo con licencia registrada en `rights_and_sources.md`. Comprimir con Draco/meshopt.
4. Animación determinista por tiempo `t` (no por `requestAnimationFrame` libre) para poder renderizar cuadro a cuadro.
5. Exportar: capturar PNG por cuadro con navegador headless (Playwright) a 1080×1920, 25 fps, y unir con FFmpeg. Mezclar con el resto en `filmcraft-edit`.
6. Datos del lote (medidas, precio) salen de `property_snapshot.json`; nunca inventar cifras en la escena.

## Reglas
Zona segura (nada importante en el 15 % inferior ni en la franja derecha). Sin fechas en pantalla. Pasar `prepublish-qa`.
