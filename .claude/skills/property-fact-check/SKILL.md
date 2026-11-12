---
name: property-fact-check
description: Verifica la ficha de una propiedad (precio, estado, medidas, rasgos, derechos de fotos) antes de crear cualquier contenido inmobiliario de PublicaBOT. Usar siempre antes de property-reel o de un carrusel de propiedad.
---

# property-fact-check

## Entrada
- Fuente de la propiedad: export autorizado de REconnect, ficha que Nixon confirma en el chat o link del listado.
- Fotos y videos con su origen.

## Proceso
1. Construir `property_snapshot.json` con el esquema del master §8.2: `property_id`, `source_system`, `source_verified_at`, `listing_status`, `transaction`, `type`, `asking_price_usd`, `public_location`, `area_m2`, `features_verified[]`, `public_contact`, `media_asset_ids[]`, `marketing_permission`.
2. Cada campo lleva su origen. Si un dato viene de un portal, es precio de **lista** (`ASKING`), no de cierre.
3. Los campos sin fuente se dejan en `null`. **Nunca se rellenan por inferencia.**
4. Preguntar a Nixon **en un solo mensaje** todo lo que falte y bloquee la pieza (precio, estado, permiso de marketing).
5. Santa Isabel: aplicar master §11. Prohibido usar datos internos, y el monto de reserva no se usa sin revalidar.

## Salida
- `property_snapshot.json` con estado `VERIFIED` o `BLOCKED_FACTS` y la lista de faltantes.

## Bloquea si
- Falta precio, estado activo o permiso de marketing.
- Las fotos no tienen origen o derechos claros.
