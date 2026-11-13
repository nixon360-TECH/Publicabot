# ADN de subtítulos "viral" (referencia de Nixon, 5 capturas)

Estado: BORRADOR para aprobar con Nixon. Mock en `04_PROJECTS_EDITABLE/N360-20261112-0001/mock_viral_AB.png`. Solo se imita el estilo; no se copian marcas ni textos de las referencias.

## Lo que tienen en común (medido en las 5 capturas)
1. **Mezcla de pesos en una misma frase**: palabra ligera condensada (SMART) sobre palabra pesada condensada (BUYERS). Contraste de grosor + tamaño, 1 palabra protagonista (~3x el tamaño de las demás).
2. **Cursiva serif pequeña** como "conector" (It, is, what, desde, con) junto a una palabra grande en sans pesada.
3. **Relleno en negativo**: la letra grande toma el color inverso del fondo detrás (degradado gris/blanco/negro, "THIS", "$400k", "The Location"); funciona como vidrio/negativo, no como color plano.
4. **Acento de color**: dorado/lima (Lehigh Acres) para una palabra clave; el resto blanco, crema o negativo.
5. **Letras que pasan por detrás de la persona** (capa de texto entre fondo y sujeto) cuando hay sujeto; en dron, texto sobre el terreno con sombra suave.
6. **Cifra gigante** (precio) con palabra pequeña en cursiva ("is what $1.18 million").
7. Centrado, 2–4 líneas, composición apilada; la palabra clave aparece primero y la frase se completa por capas.

## Molde (plantilla) por bloque de texto
| Capa | Fuente (libre/ya instalada) | Tamaño relativo | Relleno |
|---|---|---|---|
| Palabra protagonista | Impact / Bebas Neue (OFL) | 100 % | negativo del fondo (desenfoque 45 px, contraste empujado) |
| Palabra ligera | Arial Nova Cond Light | 55–70 % | blanco |
| Conector | Georgia Italic | 25–35 % | crema |
| Acento | Arial Nova Bold Italic o Cond Bold | 35–45 % | dorado `#ECD628` |

## Movimiento (para `gsap-motion` / `motion-design`)
Entrada por capas escalonadas 60–90 ms: conector → palabra ligera → protagonista con golpe de escala (1.12→1.0, 120 ms) + SFX tick/whoosh; salida con fundido corto. Máximo 1 bloque protagonista por toma.

## Reglas del proyecto que mandan sobre el estilo
Zona segura (15 % inferior, franja derecha), contraste mínimo garantizado (si el negativo queda gris medio, empujar a blanco/negro), UTF-8 con tildes, sin fechas, asterisco del banco, solo cifras de `property_snapshot.json`.

## Guion de bloques propuesto (hook C, sin voz aún)
1. «Antes de decidir,» (conector) / **CONÓZCALO** (protagonista) / «desde el aire» (acento)
2. «SANTA» (ligera) / **ISABEL** (protagonista) / «en Comacarán» (acento)
3. «Terrenos desde» / **286 v²**
4. «con escritura» / **AGUA CONECTADA**
5. «desde» / **$24,500** / «*Financiamiento con Banco Industrial sujeto a evaluación del banco.»
