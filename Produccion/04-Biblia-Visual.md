# Corazón de Pulpa — Biblia visual

Este documento existe para que el clip 1 y el clip 250 parezcan de la misma película. Tiene seis partes:

1. Cómo mantener la coherencia (el flujo de trabajo)
2. El guion de color: cómo cambia la luz según el alma de FrutiTech
3. Hojas de personaje
4. Locaciones y planos de fondo
5. Utilería, hologramas y planos secundarios
6. Paquete gráfico para la edición

Los prompts van en inglés, igual que en el guion. Los bloques `[HAROLD]`, `[LOC-OFICINA]`, etc. son los mismos de los guiones técnicos; aquí se agregan variantes y modificadores que se pegan **al final** de esos bloques.

---

## 1. Cómo mantener la coherencia

### El flujo para cada clip

| Paso | Qué se hace | Con qué |
|---|---|---|
| 1 | Se elige la **imagen de referencia del personaje** | Su imagen original o su hoja de personaje (parte 3) |
| 2 | Se elige el **plano de fondo** de la locación | Los planos de la parte 4, generados una sola vez |
| 3 | Se genera la **imagen inicial** del clip combinando las dos referencias con el prompt de la fila | Herramienta de imagen |
| 4 | Se revisa la imagen con la **lista de chequeo** (abajo) | — |
| 5 | Se anima la imagen inicial con el prompt de movimiento y el diálogo | Herramienta de video |

La regla de oro: **nunca se genera un clip de video desde cero, solo con texto.** Siempre se parte de una imagen inicial que ya pasó la lista de chequeo. Es la diferencia entre personajes que se parecen y personajes que cambian de cara en cada plano.

### Orden de producción de las referencias

Antes de generar un solo clip del guion, se produce esto, en este orden:

1. Imagen de referencia de **Don Lulo** (prompt en `02-Guion-Tecnico-Cap-3-5.md`).
2. **Hojas de personaje** de los cinco (parte 3): giro de cuerpo completo y expresiones.
3. **Foto de grupo** con los cinco juntos, para fijar estaturas (parte 3).
4. **Planos de fondo** de todas las locaciones (parte 4).
5. **Utilería principal** (parte 5).

Se guardan en carpetas así:

```
Imagenes/
  Personajes/   (originales + hojas + foto de grupo)
  Locaciones/   (un plano por locación y variante)
  Utileria/
Clips/
  Cap01/  Cap02/  …  (un archivo por fila: 1.07.mp4, 1.08.mp4…)
```

Nombrar cada clip con el número de su fila ahorra horas en la edición.

### Formato técnico fijo

- **Relación de aspecto:** 16:9 siempre, incluso en confesionarios.
- **Resolución de entrega:** 1080p.
- **Cuadros por segundo:** 24 en toda la película.
- **Duración por clip:** 8 segundos (si la herramienta genera más, se recorta en edición).

### Prompt negativo

Si la herramienta tiene un campo de prompt negativo, siempre se pega este:

`text, letters, words, subtitles, watermark, logo, signature, deformed hands, extra fingers, extra limbs, duplicated character, human ears, human skin on head, blurry face, 2D cartoon, anime, flat illustration`

Si no tiene ese campo, se agrega al final del prompt: `No text or letters anywhere in the image.`

### Lista de chequeo de la imagen inicial

Antes de animar, la imagen tiene que pasar las cinco:

- [ ] **Identidad:** el personaje tiene sus rasgos fijos (tabla "lo que no cambia nunca" de su hoja).
- [ ] **Manos:** cinco dedos, con la piel de su fruta.
- [ ] **Sin texto deformado:** ni letreros, ni pantallas, ni papeles con letras raras. Si aparecen, se regenera o se tapa en edición.
- [ ] **Luz del capítulo:** coincide con el guion de color (parte 2).
- [ ] **Estado de la historia:** el brillo de Daniel, las plantas de la oficina y el vestuario corresponden al momento de la historia.

### Problemas frecuentes

| Problema | Solución |
|---|---|
| El personaje cambia de cara a mitad del clip | Acortar el clip, reducir el movimiento de cámara y subir el peso de la imagen de referencia si la herramienta lo permite |
| Aparecen orejas o pelo humano donde no van | Agregar `fruit-skin head, no human ears` y regenerar la imagen inicial |
| Las manos salen humanas | Agregar `[fruta]-skin hands with the texture of the fruit` y mostrar menos las manos en el encuadre |
| Dos personajes se mezclan en uno | Separar el plano en dos clips (plano y contraplano) |
| El texto en pantallas o papeles sale deformado | Pedir `blurred screen` o `blank paper` y agregar el texto en edición |
| El labio no coincide con el diálogo | Revisar que el diálogo tenga máximo 20 palabras; si no basta, plano más abierto o de perfil |
| El personaje habla aunque el clip es de narrador | Agregar `mouth closed, not speaking` |

---

## 2. El guion de color

La luz cuenta la historia: **mientras FrutiTech pierde la pulpa, la imagen se enfría y se apaga; cuando la recupera, vuelve el calor.** Así el salón siente la caída aunque no lea los indicadores.

Se logra en dos lugares: con una frase de luz al final de cada prompt y con una corrección de color pareja por capítulo en la edición.

| Bloque | Temperatura y saturación | Frase de luz para el prompt `[LUZ]` | Corrección en edición |
|---|---|---|---|
| Prólogo (gala) | Fría, gris azulada, muy apagada | `cold blue-grey fluorescent light, desaturated, lifeless` | Saturación −40 %, tinte azul |
| Cap. 1 y 2 | Cálida, dorada, colores plenos | `warm golden morning light, rich saturated colours` | Neutra, leve calidez |
| Cap. 3 | Cálida pero invadida: rojo del ojo, azul de pantallas | `warm light contaminated by cold blue screen glow and red accents` | Saturación −10 % |
| Cap. 4 | Planta en blanco industrial; torre vacía fría; la playa de la pantalla en cian falso | `flat white industrial light` · torre: `cold empty light` | Saturación −15 % |
| Cap. 5 | Fría y gris, una Navidad sin calor | `cold grey winter light, weak Christmas lights, muted colours` | Saturación −30 %, tinte azul |
| Cap. 6 | De negro a reflector, y luego dorado | `single spotlight in darkness` → `golden warm light returning` | Contraste alto al inicio, después calidez |
| Cap. 7 | El calor vuelve poco a poco, luz de mañana | `soft warm morning light, colours coming back to life` | Saturación −5 % → neutra |
| Final A | El más cálido de la película: ámbar de faroles | `glowing amber light from paper lanterns, festive, very warm` | Calidez alta, saturación +10 % |
| Final B | Blanco clínico y azul | `clinical white light, cold, sterile, perfectly ordered` | Saturación −35 % |
| Comerciales | Colores chillones de televisión de los 90 | `saturated cheesy 1990s TV commercial lighting` | Filtro de VHS, formato 4:3 dentro del 16:9 |
| Confesionarios | La de su imagen original | *(no se agrega)* | Viñeta suave |

### Las plantas de la oficina

Las plantas colgantes de FrutiTech se marchitan con la cultura y reviven con ella. Es un detalle que casi nadie nota conscientemente, pero que se siente. Se agrega la frase al final de `[LOC-OFICINA]`, `[LOC-JUNTAS]` o `[LOC-HAROLD]`:

| Momento | Frase `[PLANTAS]` |
|---|---|
| Cap. 1 y 2 · Final A | `lush, healthy green plants` |
| Cap. 3 y 4 | `some plants have yellowing leaves` |
| Cap. 5 y 6 · Final B | `the plants are wilted and brown` |
| Cap. 7 | `wilted plants with small fresh green sprouts` |

### El brillo de Daniel

Es el termómetro emocional de la película. Cuatro niveles, cada uno con su frase exacta:

| Nivel | Frase para el prompt | Clips |
|---|---|---|
| **3 · Brillante** | `a soft golden glow radiates from his skin` | 1.02, 1.11, C-03, 3.09, 7.12, 7.15, 7.21-B, FB-08 |
| **3+ · Máximo** | `a bright golden glow radiates fully from his skin` | FA-06, FA-11 |
| **2 · Normal** | *(no se agrega nada)* | 1.15, 1.17, 2.06, 3.11, 3.13 |
| **1 · Débil** | `his glow is weak, slightly dull skin` | 1.21, 3.15, 4.07, 7.28 |
| **0 · Apagado** | `his skin looks dull and matte, no glow, slightly greyish` | P-03, 3.21, 3.22, 4.21, 5.06, 5.21, 5.23, 5.29, 6.16 |
| **Subiendo** | `a soft golden glow slowly returning to his skin` | 1.22, 2.11, 4.10, 6.17, 7.09 |

---

## 3. Hojas de personaje

Para cada personaje se generan dos imágenes de referencia **usando su imagen original como referencia**: un giro de cuerpo completo y una hoja de expresiones. Las imágenes originales solo muestran del pecho para arriba; sin el giro de cuerpo completo, la IA inventa piernas y zapatos distintos en cada plano.

### Plantillas

**Giro de cuerpo completo:**
`Character reference sheet for a hyperrealistic 3D animated film. [PERSONAJE] [PERSONAJE-CUERPO]. The same character shown four times side by side on a plain light-grey studio background: front view, three-quarter view, side profile and back view. Full body, standing in a relaxed neutral pose, soft even studio lighting. No text, no labels.`

**Hoja de expresiones:**
`Expression sheet for a hyperrealistic 3D animated film. [PERSONAJE]. Six head-and-shoulders portraits of the same character in a 3x2 grid on a plain light-grey background: happy, angry, surprised, sad, thinking, laughing. Identical lighting in all six. No text, no labels.`

### Don Harold · El Aguacate

**Bloque:** `[HAROLD]` (en `01-Guion-Tecnico-Cap-1-2.md`)

**[HAROLD-CUERPO]** `Short and round build with a big belly, charcoal pinstripe trousers, black leather belt, polished black leather shoes, walks with his chest puffed out.`

| Lo que no cambia nunca | Por qué importa |
|---|---|
| Tallito café en la punta de la cabeza | Es su silueta; sin él parece una pera |
| Gafas de carey rectangulares | Solo se las quita en C-01 y 7.16 |
| Corbata azul rey sobre camisa negra | Lo distingue a distancia en planos generales |
| Piel de aguacate rugosa, verde amarillento | — |

| Variante de vestuario | Frase que se agrega | Clips |
|---|---|---|
| Recién llegado del congreso | `wearing dark sunglasses and a conference lanyard around his neck` | 1.04 |
| Con gafas de realidad virtual | `wearing a white VR headset over his glasses` | 5.04, 5.07, CR-01 |
| Con bigote postizo | `wearing an obviously fake black moustache` | CM2-01 a CM2-03 |
| Con gafas oscuras de comercial | `wearing cheap sunglasses` | CM1-02, CM1-03 |
| Con gorra de FrutiTech | `wearing a cap with a small fruit logo` | FA-10 |

**Lenguaje corporal:** Acto 1, pecho afuera, brazos abiertos, señala con el dedo. Desde 6.08, hombros más bajos, manos juntas, mira a los ojos.

### Valentina · La Fresa

**Bloque:** `[VALENTINA]`

**[VALENTINA-CUERPO]** `Slim build, lilac blazer over a white blouse, white tailored trousers, nude low heels, a slim tablet usually in one hand, walks with a confident upright posture.`

| Lo que no cambia nunca | Por qué importa |
|---|---|
| Corona de hojas verdes sobre el pelo largo castaño oscuro | Su silueta |
| Brackets en los dientes | Rasgo propio que la hace reconocible |
| Argollas doradas grandes | — |
| Blazer lila | Es "su" color; el morado es también el de sus hologramas y el de VRIO en pantalla |

| Variante de vestuario | Frase que se agrega | Clips |
|---|---|---|
| En la planta | `wearing a white hairnet stretched over her leafy crown` | 4.16 a 4.19 |
| Presentadora de concurso | `holding a stack of cue cards like a TV host, colourful game-show lighting` | 2.14 |

**Lenguaje corporal:** manos abiertas al explicar, nunca levanta la voz, ceja levantada para la ironía.

### Daniel · El Mango

**Bloque:** `[DANIEL]`

**[DANIEL-CUERPO]** `Medium-tall slim build, navy blazer, light-blue shirt, grey chinos, brown leather shoes, often hugging a notebook full of colourful sticky notes.`

| Lo que no cambia nunca | Por qué importa |
|---|---|
| Hoja verde y tallito café en la cabeza | Su silueta; es la hoja que se le cae en CR-03 |
| Degradado de piel: rojo arriba, amarillo abajo | La IA tiende a volverlo todo naranja; hay que insistir en el degradado |
| Gotitas de rocío sobre la piel | Lo hacen ver "fresco"; se quitan cuando está apagado |
| La libreta con notas adhesivas | Su objeto: aparece en casi todas sus escenas |

| Variante de vestuario | Frase que se agrega | Clips |
|---|---|---|
| En casa | `blazer off, light-blue shirt with sleeves rolled up` | 3.09 a 3.22, 5.06, 5.21 |
| En la planta | `wearing a white hairnet stretched comically over the leaf on his head` | 4.07 a 4.10 |
| Con gafas de realidad virtual | `a white VR headset pushed up on his forehead` | 5.06 |

**Lenguaje corporal:** se inclina hacia adelante cuando tiene una idea; se encorva y abraza la libreta cuando lo apagan.

### Prof. Carlos Mario · La Piña

**Bloque:** `[PIÑA]` (en `03-Guion-Tecnico-Cap-6-8-Finales.md`) y `[PIÑA-SOMBRA]` para antes de la revelación (en `02-Guion-Tecnico-Cap-3-5.md`)

**[PIÑA-CUERPO]** `The tallest of the cast, broad shoulders, navy pinstripe suit trousers, black leather shoes, moves slowly and calmly, often with one hand on his chin.`

| Lo que no cambia nunca | Por qué importa |
|---|---|
| Corona alta de hojas de piña | Lo hace el más alto; es lo único que se ve en su silueta del cabezote |
| Barba y bigote oscuros, pelo crespo corto | — |
| Corbata roja con pañuelo rojo | Contrasta con la corbata azul de Don Harold: los dos líderes opuestos |
| Libreta de cuero café | Su objeto, desde el capítulo 3 |

**Regla de la revelación:** antes del clip 6.01 **nunca** se le ve la cara. Solo mano, manga, silueta a contraluz o voz.

**Lenguaje corporal:** quieto, pausado, mira a cámara. Es el único que rompe la cuarta pared.

### Don Lulo · El Lulo

**Bloque:** `[LULO]` (en `02-Guion-Tecnico-Cap-3-5.md`)

**[LULO-CUERPO]** `Short stocky build, white work apron over a light-blue work shirt, dark work trousers, white rubber boots, slightly bent posture from years of work.`

| Lo que no cambia nunca | Por qué importa |
|---|---|
| Cáliz verde en forma de estrella en la cabeza | Su silueta |
| Pelusa aterciopelada de la piel de lulo | Lo distingue de una naranja |
| Bigote gris grueso | — |
| Gorra con el logo de FrutiTech | Símbolo de pertenencia: se la quita en 4.20 y vuelve en FA-02 |

| Variante de vestuario | Frase que se agrega | Clips |
|---|---|---|
| De trabajo con gorra (base) | `white hairnet, white apron, navy cap with a small fruit logo` | 4.02 a 4.20 |
| Sin gorra | `no cap, white hairnet, white apron` | Desde el final de 4.20: 4.26, 5.14, todo el cap. 7, FB-02. La gorra solo vuelve en FA-02 |
| Su mejor camisa | `no hairnet or apron, wearing his best ironed short-sleeve shirt` | 5.26, FB-10 |
| En la novena | `cap with a small fruit logo, festive red scarf, no hairnet` | FA-02, FA-10, FA-11 |

### Extras

**Bloque:** `[EXTRAS]` (en `02-Guion-Tecnico-Cap-3-5.md`)

Para que no se confundan con los protagonistas, los extras **nunca** son aguacate, fresa, mango, piña ni lulo. Se usan banano, naranja, guayaba, maracuyá, guanábana, uva y kiwi. En la torre visten ropa de oficina en grises y beige; en la planta, delantal y malla blancos.

### Foto de grupo

Fija las estaturas y sirve de referencia para los planos con varios personajes.

`Group reference image for a hyperrealistic 3D animated film. Five anthropomorphic fruit characters standing in a row on a plain light-grey studio background, full body, front view, soft even studio lighting. From left to right: [LULO] [LULO-CUERPO]; [HAROLD] [HAROLD-CUERPO]; [VALENTINA] [VALENTINA-CUERPO]; [DANIEL] [DANIEL-CUERPO]; [PIÑA] [PIÑA-CUERPO]. Height order from shortest to tallest: Lulo, Harold, Valentina, Daniel, Pineapple professor (his crown makes him the tallest). No text, no labels.`

Si la imagen sale con los personajes mezclados, se generan de a dos y se comparan las estaturas en la edición.

---

## 4. Locaciones y planos de fondo

Para cada locación se genera **un plano vacío, sin personajes**, en el ángulo principal. Ese plano se usa como referencia de fondo en todas las imágenes iniciales de esa locación.

**Plantilla del plano de fondo:**
`Empty background plate for a hyperrealistic 3D animated film, no characters. [LOCACIÓN]. [LUZ]. [PLANTAS si aplica]. Eye-level wide shot, 16:9, cinematic, shallow depth of field. No text or letters anywhere.`

**El mundo de FrutiTech.** Una empresa colombiana mediana de jugos y pulpas, con una torre administrativa y una planta de producción a dos cuadras, en una ciudad andina rodeada de montañas verdes. Tiene un estilo propio: madera oscura, detalles dorados, plantas por todas partes. Ese "sabor propio" es el que se pierde cuando todo se vuelve gris y blanco.

**El letrero de Gestión Humana.** Las cuatro imágenes originales tienen un cuadro negro con el ícono de tres personas y el texto "Gestión Humana". En las imágenes nuevas se pide `a dark framed wall sign with a simple white icon of three people` sin texto. Si en algún plano importa que se lea, el texto se agrega en edición.

### Torre FrutiTech

| Locación | Bloque | Escenas | Variantes |
|---|---|---|---|
| **Lobby** | `[LOC-LOBBY]` | 1.02, 1.04, 3.02 a 3.05, CR-01 | **Transformado** (cap. 3): agregar `now filled with a ping-pong table, colourful bean bags and a futuristic white sleeping pod`. **Clonado** (final B): `[LOC-LOBBY-CLON]` |
| **Oficina abierta** | `[LOC-OFICINA]` | 1.03, 1.05, 1.28, 2.01, 2.02, 3.29, 4.05, 5.05, 5.07, 5.08, 7.05, 7.09 | **Pasillo:** `a corridor of the open office with glass walls on one side` (1.21, 1.22). **Cafetera:** `a coffee corner with a dark wood counter and a steel coffee machine` (2.01). **Vacía de viernes:** `lights off, nobody there` (4.05) |
| **Sala de juntas** | `[LOC-JUNTAS]` | Casi todo el cap. 1 y 2, 3.17 a 3.28, 4.23 a 4.25, 5.02 a 5.04, cap. 7 | **Concurso** (2.14 a 2.18): agregar `colourful game-show lighting, a small glossy podium with a big red buzzer` |
| **Oficina de Don Harold** | `[LOC-HAROLD]` | 1.23 a 1.27, 2.20 a 2.22, 3.08, 3.12, 3.14, 3.16, 4.11, 4.12, 5.09 a 5.20, 7.17, 7.19, FB-07, FB-11 | **De noche:** `at night, lit only by the desk lamp`. **Pared de pantallas** (3.16): `a wall of many small video screens behind the desk` |
| **Taller de liderazgo** | `[LOC-TALLER]` | 7.07, 7.08 | — |

**Regla de cámara para la oficina de Don Harold:** la ventana con la ciudad y las montañas queda **siempre a la derecha** del encuadre, como en su imagen original. Si cambia de lado, el salón siente que es otra oficina.

### Planta FrutiTech

| Locación | Bloque | Escenas | Variantes |
|---|---|---|---|
| **Planta** | `[LOC-PLANTA]` | Cap. 4, 5.14, 7.20, 7.23 a 7.26, FB-10 | **Con playa** (desde 4.13): agregar `the large screen above the peeling machine shows a bright tropical beach wallpaper`. **Casilleros** (4.20): `a row of grey metal lockers at the end of the plant` |
| **Novena** | `[LOC-NOVENA]` | Final A | — |
| **Planta vacía** | `[LOC-PLANTA-VACIA]` | Final B | — |

### Otras locaciones

| Locación | Bloque | Escenas | Notas |
|---|---|---|---|
| **Apartamento de Daniel** | `[LOC-CASA-DANIEL]` | Cap. 3, 5.06, 5.21, 5.22, 7.28, CR-03 | De día en el cap. 3; de noche en el 5 (`at night, lit only by the laptop screen`); al atardecer en el 7. Las notas adhesivas de la nevera van desapareciendo (3.21) |
| **Salón de la gala** | `[LOC-GALA]` | Prólogo, 5.24 a 5.30, cap. 6 | En el cap. 6 se transforma: primero un solo reflector, luego `the lights come up warmly and a large golden hologram glows in the centre` |
| **Biblioteca de la Piña** | `[LOC-BIBLIOTECA]` | 3.23, 4.22, 5.17, 7.27, CON-01 a CON-04, FB-12, CR-04 | Debe parecerse al fondo de su imagen original: estantes de libros, globo terráqueo dorado. Para sus confesionarios se usa directamente esa imagen |
| **Set de infomercial** | `[LOC-INFOMERCIAL]` | Comerciales 1 y 2 | — |
| **Oficina de Banco Papaya** | `[LOC-PAPAYA]` | FB-08 | Tiene que verse más cálida que la FrutiTech del final B: ahí está el contraste |

### Exteriores y planos fijos

Son las filas `FIJA` del guion. Se generan como imagen fija y se animan en edición con un zoom lento (efecto Ken Burns).

| Fila | Prompt completo |
|---|---|
| **1.01** Fachada al amanecer | `Hyperrealistic 3D animated film still. Exterior of the FrutiTech headquarters at sunrise: a modern twelve-storey tower of glass and dark wood with vertical gardens on its balconies, in a Colombian Andean city surrounded by green mountains. Warm golden sunrise light, a few people walking in. Wide establishing shot, 16:9. No text or letters.` |
| **1.23** Don Harold y el cuadro | `Hyperrealistic 3D animated film still. [LOC-HAROLD] at dusk. [HAROLD] seen from behind, standing still, looking at a framed photograph on the wall of a futuristic glass tech campus. Warm orange dusk light from the window. Medium shot, 16:9. No text.` |
| **3.01** Torre con pendón | `Hyperrealistic 3D animated film still. Exterior of the FrutiTech headquarters (modern glass and dark wood tower with vertical gardens) on an early Monday morning; a huge blank white banner hangs down the front of the building. Green mountains behind. Wide shot, 16:9. No text on the banner.` |
| **4.01** Planta de madrugada | `Hyperrealistic 3D animated film still. Exterior of the FrutiTech fruit-processing plant before dawn: a large industrial building with a saw-tooth roof, trucks loaded with colourful fresh fruit at the loading dock, workers in white aprons arriving under orange street lights. Green mountains in silhouette. Wide shot, 16:9. No text.` |
| **5.01** Ciudad de Navidad | `Hyperrealistic 3D animated film still. A Colombian Andean city at night decorated with Christmas street lights, the FrutiTech glass tower in the background with few lit windows. Cold, slightly muted colours. Wide shot, 16:9. No text.` |
| **5.11** Novena de 2006 | *(Prompt en el guion, fila 5.11.)* Agregar al final: `old photograph texture, slight grain, soft vignette.` |
| **7.01** Calendario | `Hyperrealistic 3D animated film still. Close-up of a paper wall calendar for December hanging on a dark wood office wall, one day circled in red marker, a small plant beside it with new green sprouts. Soft morning light, 16:9. The numbers are blurred.` |
| **7.22** Torre de noche | `Hyperrealistic 3D animated film still. Exterior of the FrutiTech glass and dark wood tower at night, several windows warmly lit, Christmas lights on a few balconies, green mountains in the dark background. Wide shot, 16:9. No text.` |
| **8.01** Puerta de la planta | `Hyperrealistic 3D animated film still. The big closed metal sliding door of the FrutiTech fruit-processing plant at dusk, a faint warm light leaking under the door, a path leading to it. Medium-wide shot, 16:9. No text.` |
| **FB-05** Lobby clonado | Plano de fondo de `[LOC-LOBBY-CLON]` con la luz del final B. |

---

## 5. Utilería, hologramas y planos secundarios

### Utilería principal

Cada objeto se genera una vez como imagen de referencia y se describe **siempre con la misma frase**.

| Objeto | Frase fija | Aparece en |
|---|---|---|
| Pocillo de Don Harold | `a black mug with a gold avocado symbol` | Su oficina, 2.02 |
| Pocillo de Valentina | `a white mug with a red strawberry outline` | 5.18, FB-09 |
| Pocillo de Daniel | `a black mug with a mango symbol` (en la torre) · `a mango-shaped mug` (en casa) | Cap. 3, CR-03 |
| Pocillo de la Piña | `a black mug with a gold pineapple symbol` | Biblioteca |
| Libreta de Daniel | `a notebook full of colourful sticky notes` | Casi todas sus escenas |
| Libreta de la Piña | `a worn brown leather notebook` | 3.23, 4.22, 5.17, cap. 6, FB-12 |
| Memoria USB "sagrada" | `a small silver USB drive` | 1.14, CM2-02 |
| Maleta del congreso | `a hard-shell suitcase covered in travel stickers` | 1.04 |
| Ojo de Aguacate Pro | `a black box with a glowing red eye symbol on the lid` | 2.21, 7.17, 7.19 |
| Ventana del software | `a pop-up window with a big glowing red eye` | 3.10 |
| Cámaras de vigilancia | `a small webcam with a red light` | 3.29 |
| Formato F-27 | `a printed form, blurred` | 3.17, 7.19-B |
| Mesa de ping-pong, puffs y cápsula | `a ping-pong table, colourful bean bags and a futuristic white sleeping pod` | 3.02 a 3.05, CM1-03, FB-06 |
| Gafas de realidad virtual | `a white VR headset` | Cap. 5, CR-01 |
| Gorra de FrutiTech | `a navy cap with a small fruit logo` | Don Lulo, FA-10, FB-10 |
| Sobre de la renuncia | `a plain white envelope` | P-03, 5.22 en adelante, FA-06 |
| Invitaciones | `one sleek grey minimal card` · `one handmade card with a hand-drawn golden buñuelo` | 5.19, 5.20 |
| Paila de buñuelos | `a huge black frying pan full of golden round buñuelos` | 5.14 (vacía), 7.24, FA-02 |
| Pasabocas grises | `identical small grey snacks on a plain tray` | Gala, FB-03, FB-13 |
| Foto de la novena de 2006 | `a framed sepia photograph` | FB-11 |
| Botella de jugo | `a small unlabelled glass bottle of orange juice` | 2.10 |

### Código de color de los hologramas

Los hologramas dicen quién está pensando:

| Color | De quién | Frase | Uso |
|---|---|---|---|
| **Morado** `#9B6BFF` | Valentina | `a soft purple hologram` | Diagnóstico, columnas, balanza, auditorías |
| **Dorado** `#E8B04A` | La Piña | `a large golden hologram` | VRIO, fracturas, cap. 6 |
| **Azul** `#3D9BE9` | Daniel | `a soft blue hologram` | Si se quiere uno para él en el cap. 7; es el color de su imagen original |
| **Rojo** `#E5322D` | El Ojo de Aguacate Pro | `glowing red` | Vigilancia y control |

Don Harold **no tiene holograma**: todo lo suyo es impreso, en USB o en una caja. Es la persona del papel y el control remoto.

### Planos secundarios para la edición

Estos clips no están en el guion como filas, pero salvan la edición: sirven de transición, tapan un corte feo o dan aire entre escenas. Se generan **4 segundos** cada uno y se usan donde haga falta.

| Plano | Prompt |
|---|---|
| Pulpa para títulos | `Macro slow-motion shot of fresh fruit pulp — strawberry, mango, pineapple and avocado — splashing and swirling together on a dark background, juicy, vibrant, cinematic. No text.` |
| Pulpa que se seca (antes de "Continuará" en cap. 3 a 5) | `Macro time-lapse of bright fruit pulp slowly drying, cracking and turning grey on a dark background. No text.` |
| Fachada, paso del tiempo | `Time-lapse of the FrutiTech glass tower from day to night, clouds moving fast over green mountains. No text.` |
| Cafetera | `Close-up of a steel coffee machine in a dark wood office pouring a black coffee, steam rising. No text.` |
| Celulares que vibran | `Close-up of several phones on office desks lighting up and vibrating at the same time. Screens blurred.` |
| Banda de la planta | `Close-up of fresh lulos, mangos and strawberries moving along a stainless-steel conveyor belt. No text.` |
| Buñuelos friéndose | `Close-up of golden buñuelos frying and turning in hot oil in a big black pan, warm light, festive. No text.` |
| Faroles | `Slow upward shot of colourful paper Christmas lanterns glowing under the steel beams of a factory. No text.` |
| Escritorio vacío de Daniel | `A tidy empty office desk with a black mango mug and a closed laptop, sticky notes on the monitor edge, cold light. No text.` |
| Silueta de la corona (CM2-05) | `Silhouette of a man with a tall pineapple-leaf crown on his head against a soft golden backlight, completely black figure. No text.` |

---

## 6. Paquete gráfico para la edición

Todo lo que lleva texto se hace en el editor de video, nunca con la IA.

### Paleta de la película

| Uso | Color | Hex |
|---|---|---|
| Fondo de tarjetas | Negro café | `#1A1410` |
| Línea y detalles | Dorado FrutiTech | `#C9A24D` |
| Texto | Crema | `#F5EFE3` |
| **DUPLICAR** (tarjeta y botón) | Verde aguacate | `#6B8E23` |
| **ADAPTAR** (tarjeta y botón) | Rojo fresa | `#E63946` |
| Indicador **Clima laboral** | Azul | `#3D9BE9` |
| Indicador **Cultura / Alma** | Naranja mango | `#FF9F1C` |
| Indicador **Ventaja VRIO** | Morado Valentina | `#9B6BFF` |
| Indicador **Criterio del salón** | Dorado piña | `#E8B04A` |

Los indicadores usan colores distintos al verde y al rojo de las tarjetas para que el salón no confunda "voté verde" con "subió el verde".

### Tipografías

Las tres son gratuitas en Google Fonts:

- **Títulos de telenovela** (cabezote, nombres de capítulo, "Continuará…"): *Playfair Display*, cursiva negrita.
- **Textos académicos, rótulos e indicadores:** *Montserrat* (SemiBold para títulos, Regular para el cuerpo).
- **Subtítulos:** *Montserrat* SemiBold, blanco con contorno negro de 2 px, en el tercio inferior.

### Piezas gráficas

| Pieza | Cómo se ve | Cuándo |
|---|---|---|
| **Rótulo de personaje** | Barra negra café con línea dorada a la izquierda. Nombre en Montserrat SemiBold; debajo, el cargo en cursiva | La primera vez que aparece cada uno |
| **Texto académico** | Tarjeta semitransparente (negro café al 80 %) en la esquina inferior izquierda. Concepto en dorado, explicación en crema, cita entre paréntesis en cursiva | Columna "Texto en pantalla" del guion |
| **Confesionario** | Rótulo pequeño "CONFESIONARIO" en la esquina superior izquierda y viñeta suave | Todos los confesionarios |
| **Indicadores** | Tres barras horizontales en la esquina superior derecha con número y flecha. Al cambiar, la barra se anima y aparece "−6" o "+8" | Fin de cada capítulo y decisiones del Acto 2 |
| **Tarjeta de decisión** | Pantalla completa: pregunta arriba, dos bloques grandes abajo (DUPLICAR verde a la izquierda, ADAPTAR rojo a la derecha), temporizador circular dorado | Las 7 decisiones |
| **"Anteriormente…"** | Franjas negras arriba y abajo, título en Playfair cursiva | Inicio de cada capítulo |
| **"Continuará…"** | Imagen congelada que se desatura, zoom lento, Playfair cursiva dorada grande, acorde dramático | Fin de cada capítulo |
| **Comerciales** | Formato 4:3 dentro del 16:9, ruido de VHS, fecha de grabadora en una esquina | Comerciales 1 y 2 |
| **Cuarta pared** (6.18) | Breve parpadeo de la imagen, como si se fuera la señal | La Piña mira a cámara |

### Tarjetas físicas para el salón

Imprimir una tarjeta por estudiante, tamaño media carta, a dos caras:

- **Cara verde** `#6B8E23`: un aguacate y la palabra **DUPLICAR**.
- **Cara roja** `#E63946`: una fresa y la palabra **ADAPTAR**.

En la prueba VRIO (decisión 6) la misma tarjeta sirve: verde = **SÍ**, roja = **NO**. Conviene decirlo en voz alta antes de empezar, porque es la única decisión donde el verde no significa duplicar.
