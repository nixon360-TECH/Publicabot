# Fotos limpias de Santa Isabel con movimiento

N360-025: clips de apoyo para el montaje, a partir de las seis fotos editadas
seleccionadas por Nixon. No son anuncios completos ni tomas nuevas de dron.

## Entradas y salidas

- Plan editable: `brands/nixon-remax/motion_kit/fotos_limpias_motion.json`.
- Entrada: directorio de fotos limpias ya existentes. `calles-internas` está excluida.
- Salida: carpeta nueva fuera de las fotos, con seis MP4 de seis segundos por formato
  (1080x1350 y 1080x1920), previews de 36 segundos, galería HTML, plan y reporte QA.
- Paneos, acercamientos, alejamiento y ascenso del encuadre con inicio/final suaves.
- Sin sonido, texto, logos o IA generativa adicional; aptos como material para editar.
- H.264, 25 fps, yuv420p, rango limitado, píxeles cuadrados y faststart.

Las fotos fuente son horizontales de 1672x941. Cada formato recorta el encuadre
antes del movimiento para mantener la proporción, con ancla configurable por foto.
El vertical muestra menos terreno y amplía la imagen; no añade detalle fotográfico.
No se modifican las calles, el cielo ni otros elementos de las fotos de entrada.

## Ejecución

Python 3.12 y FFmpeg/ffprobe ya instalados; sin paquetes Python adicionales.
Sustituir los argumentos por las rutas locales del equipo. El directorio de salida
no debe existir; usar otra versión para repetir, conservando los renders anteriores.

```powershell
python scripts/render_fotos_limpias.py --source RUTA_FOTOS --output RUTA_BORRADOR_NUEVO --plan brands/nixon-remax/motion_kit/fotos_limpias_motion.json --ffmpeg RUTA_FFMPEG --ffprobe RUTA_FFPROBE
```

`--only 01_calles-desde-arriba` permite una muestra en ambos formatos.
El programa no sube archivos ni requiere servicios externos.

## Comprobaciones

Cada MP4 pasa comprobación de resolución, duración, 150 fotogramas, formato de píxel,
ausencia de audio, decodificación completa y cambio de imagen durante el movimiento.
Los hashes SHA-256 de las fotos se comparan al inicio y al final. Se guardan muestras
del inicio, centro y final para inspección visual. Un fallo detiene el lote.

```powershell
python -m unittest discover -s tests -v
```

Las pruebas comprueban que los recortes permanecen dentro de las fotos y conservan
su proporción en diferentes orientaciones. `qa_report.json` conserva estado de
borrador: la inspección técnica no representa aprobación comercial ni de publicación.

## Coordinación

Rama `feature/N360-025-santa-isabel-videos-codex`, basada en la rama de motion de Claude.
Se añaden un renderizador y un plan independientes; `mock_kit.py`, `paneo_foto.py`,
los cierres y el kit compartido continúan bajo el trabajo de Claude.
Los medios y los reportes con rutas/datos locales quedan fuera de Git.
