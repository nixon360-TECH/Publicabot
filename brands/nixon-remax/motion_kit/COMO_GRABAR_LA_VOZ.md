# Cómo grabar su voz (mañana) — 6 videos de 30 s

## Qué necesita
- La **grabadora de su teléfono** (Notas de voz en iPhone / Grabadora en Android). No hace falta nada más.
- La PC con el **teleprompter**: abra `teleprompter_venta.html` con doble clic (se abre en el navegador).

## Dónde
En un cuarto cerrado y callado: un clóset con ropa o un carro con las ventanas cerradas suena mejor que una sala vacía. Teléfono a un palmo (20 cm) de la boca, sin tocarlo. Sin ventilador ni aire acondicionado.

## Cómo, video por video
1. En el teleprompter elija el video (A, B, G1, G2, G4, H).
2. **Empiece a grabar el audio en el teléfono.**
3. Pulse **«Iniciar»** en la PC. Cuenta 3, 2, 1 y va mostrando cada frase justo cuando toca decirla.
4. Hable con calma y con la sonrisa que se oye. No corra: las frases ya están medidas para 30 s.
5. Al terminar, detenga la grabación. Si se equivocó, repita la toma completa (borre la mala).

## Nombres de los archivos
Guarde cada grabación así y cópiela a esta carpeta de la PC:

`E:\NIXON360_CONTENTOPS\00_INBOX\N360-20261112-0001\voces\`

| Video | Archivo |
|---|---|
| A · ¿Busca dónde construir su nueva casa? | `vo_A` |
| B · Paz y tranquilidad | `vo_B` |
| G1 · ¿Cuánto cuesta un terreno en Comacarán? | `vo_G1` |
| G2 · Tres preguntas | `vo_G2` |
| G4 · ¿Y al comprar me dan mi escritura? | `vo_G4` |
| H · Hermano lejano | `vo_H` |

Cualquier formato sirve (`.m4a`, `.mp3`, `.wav`).

## Después
Dígale a Claude «ya están las voces», o ejecute `python mezclar_voces.py` dentro de la carpeta `build`. El programa quita el silencio del inicio, alinea la voz, baja la música mientras usted habla, deja el sonido en -14 LUFS y entrega los 6 videos y sus vistas previas.

## Si algo no cuadra
- Si dice las frases más rápido o más lento, no se preocupe: el video no cambia; solo cuide que la primera frase empiece apenas pulse «Iniciar».
- Las partes que más se pueden desfasar son las frases largas (tamaño, escritura y agua; precio). Léalas sin pausas largas.
