# NBS publicabot CHATGPT · campaña Santa Isabel

## Encargo confirmado

Nixon pidió artes para los 15 días del 12 al 26 de noviembre de 2026, exclusivamente
de Santa Isabel, ampliando las plantillas del kit existente. Solicitó collages con
varias fotos en un mismo arte para mostrar el proyecto. Los videos continúan con
Claude por instrucción posterior; los clips silenciosos N360-025 no se presentan
como anuncios terminados.

## Contenido

- 15 publicaciones principales, cada una con versión 4:5 y 9:16.
- Carruseles en los días 2, 6 y 11: siete láminas adicionales 4:5.
- Dos alternativas adicionales para pauta, cada una en ambos formatos.
- Total: 41 diseños JPG. La carpeta de pauta también incluye copias del arte A.
- Copy de Instagram/Facebook, calendario, galería local, manifiesto y QA.
- Editable mediante `brands/nixon-remax/codex_campana_15_dias.json` y
  `scripts/codex_artes_15d.py` (Pillow y NumPy del runtime ya disponible).

Se conserva la fotografía existente, se recorta para maquetar y se usan los logos
oficiales sin recolorear. Se excluye `calles-internas`. No hay generación de escena
inmobiliaria ni nuevas afirmaciones comerciales. El kit aporta colores, contacto,
tipografías y leyendas; las composiciones amplían sus plantillas según el encargo.

## Render

Con un intérprete Python que tenga Pillow y NumPy:

```powershell
python scripts/codex_artes_15d.py --photos RUTA_FOTOS_LIMPIAS --project RUTA_PROYECTO_N360 --output RUTA_NUEVA
```

`--pilot` limita el paquete al primer día y las alternativas de pauta. La salida
debe ser nueva. Nunca se sobrescriben originales. Los PNG/JPG, manifests con rutas
locales y ZIP permanecen en el disco de medios, fuera de Git.

Se comprueba el snapshot antes de producir; se miden los textos y logos dentro de
las zonas seguras del kit; se revisan dimensiones y hashes de entrada. La selección
y aprobación final pertenecen a Nixon. Las fechas aparecen en calendario y archivos,
no en las imágenes ni en el copy público.

## Evidencia del proceso de video de Claude

La implementación local de Claude documenta pasos reproducibles:

1. Datos: `property_snapshot.json` y `puntos_confirmados.json` del proyecto.
2. Estilo: `brands/nixon-remax/motion_kit/kit_nixon_remax.json`,
   `brands/nixon-remax/design_dna_texto_viral.md` y contexto de Santa Isabel.
3. Montaje y títulos: `video_build_v06.py`, `mk_v06.py`, `video2_fotos.py`.
   El segundo usa cámara por keyframes, calles trazadas con coordenadas, pines,
   bloques tipográficos del núcleo v05 y cierre v5.
4. Cierre: `mock_kit.py`, variante vigente y parámetros de animación de la foto.
5. Audio: `mezcla_video2.py` y `rights_and_sources.md`; la voz real se incorpora
   cuando está disponible. No se fabrica voz de Nixon.
6. QA: skill `prepublish-qa`, reporte técnico y revisión visual.

Los scripts de referencia dependen de rutas y módulos del disco externo, incluido
el núcleo `video_build_v05.py` y `_KIT/mock_kit.py`. Hay que inspeccionar la versión
que realmente se ejecuta y sus assets antes de reutilizarlos. La copia del repo y
el núcleo del disco no siempre tienen las mismas firmas de funciones. Esto explica
por qué leer solo el guion no equivale a reconstruir un render terminado.

Esta tarea produce únicamente los artes. Una reproducción futura del video debe
seguir el montaje, títulos, audio y cierre, con muestras comprobadas, en carpeta
propia y sin editar archivos activos de Claude.
