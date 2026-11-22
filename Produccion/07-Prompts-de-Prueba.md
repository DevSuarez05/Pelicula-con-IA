# Corazón de Pulpa · Prompts de prueba (1.20, 1.07 y 1.26)

La prueba sirve para decidir qué hace cada herramienta antes de producir en serie. Son tres filas del capítulo 1, todas de Don Harold, y cada una pone a prueba algo distinto:

| Fila | Qué prueba | HeyGen | Runway |
|---|---|---|---|
| **1.20** Confesionario | Labios y cara desde la imagen original, sin fotograma nuevo | Sí | Sí, para comparar |
| **1.07** Sala de juntas | Fotograma de ChatGPT, gesto con el brazo y voz con la boca sincronizada | Sí | Sí, para comparar |
| **1.26** Dedo sobre ENTER | Movimiento sin diálogo, tensión y zoom | No aplica | Sí |

En total son **5 clips**: dos de HeyGen y tres de Runway. Cada uno dura 8 segundos, en 16:9.

**Orden de trabajo:**

1. ChatGPT hace los dos fotogramas (parte 1).
2. Se fija la voz de Don Harold en HeyGen (parte 2).
3. Se generan los 5 clips (partes 3 y 4).
4. Se graba el narrador de 1.26 (parte 5).
5. Se califica todo en la hoja de la parte 6.

Guarden los archivos así: `Clips/Prueba/1.20-heygen.mp4`, `1.20-runway.mp4`, `1.07-heygen.mp4`, `1.07-runway.mp4` y `1.26-runway.mp4`.

---

## 1. Fotogramas en ChatGPT

La fila 1.20 no necesita fotograma: se usa directo `Imagenes/Don Harold_ Jefe de Gestión Humana.png`.

Para 1.07 y 1.26, adjunten esa misma imagen original de Don Harold. Si ChatGPT ya tiene su hoja de personaje, adjunten también la hoja.

### 1.07 · Fotograma inicial

Adjuntar la imagen original de Don Harold y pegar:

```
Use the attached image as the exact identity reference for Don Harold. Keep his face, glasses, stem, skin texture, suit, shirt and tie identical.

Create the starting frame of a shot for a hyperrealistic 3D animated film, cinematic warm lighting, shallow depth of field, anthropomorphic fruit characters with human faces and bodies in business attire, 16:9.

Don Harold, an anthropomorphic avocado man in his fifties: large bumpy green avocado-skin head with a human face, small brown stem on top, thin black hair on the sides, tortoiseshell rectangular glasses, charcoal pinstripe suit, black shirt, royal-blue tie, green avocado-skin hands. Short and round build with a big belly.

Medium shot. He stands at the head of a long dark wooden table in the FrutiTech boardroom, black leather chairs, a large blank screen on the wall, floor-to-ceiling windows with a city and green mountains behind, lush healthy green plants. He points a small remote at the screen like a showman, chest out, proud confident smile, mouth slightly open as if starting to speak. His face is clearly visible, turned three-quarters toward the camera.

Warm golden morning light, rich saturated colours. Five fingers on each hand, with avocado skin. No text or letters anywhere in the image, the screen is blank.
```

**Revisen antes de animar:**

- Tiene el tallito, las gafas de carey y la corbata azul rey.
- Las manos tienen cinco dedos y piel de aguacate.
- La pantalla está en blanco.
- La cara se ve bien, porque HeyGen la necesita para mover la boca.

### 1.26 · Fotograma inicial

Adjuntar la imagen original de Don Harold (solo como referencia de la textura de la piel) y pegar:

```
Use the attached image only as a reference for the green avocado skin texture and the charcoal pinstripe suit sleeve.

Create the starting frame of a shot for a hyperrealistic 3D animated film, cinematic, shallow depth of field, 16:9.

Extreme close-up of a single green bumpy avocado-skin finger, with the cuff of a charcoal pinstripe sleeve and a black shirt cuff visible at the edge of frame, hovering one centimetre above the Enter key of a dark laptop keyboard on a dark wooden desk. Behind it, out of focus, a laptop screen glowing with soft white light and a black mug with a gold avocado symbol. Tense dramatic lighting: warm desk lamp from one side, cold screen glow on the finger, deep shadows.

The keyboard keys have no readable letters or symbols, only blank keys. No text or letters anywhere in the image.
```

**Revisen antes de animar:** el dedo tiene textura de aguacate (no es un dedo humano) y las teclas no tienen letras deformadas. La palabra ENTER no hace falta: el encuadre ya lo dice.

---

## 2. La voz de Don Harold (se fija una vez)

En HeyGen, elijan una voz masculina en **español latinoamericano, ojalá colombiano**: grave, fuerte, pomposa, de hombre de cincuenta años. Prueben 3 o 4 voces con esta frase, que tiene las palabras difíciles de la película:

```
Señores: Frugle lo hace. Netfrux lo hace. Y desde hoy, FrutiTech también.
```

Cuando elijan la voz, anoten su nombre en la parte 6. **Esa voz se usa para todo Don Harold**, también en sus clips de Runway.

**Pronunciación.** Si la voz lee mal los nombres de las marcas, escríbanlos como suenan **solo en el campo de texto de HeyGen**, no en el guion:

| En el guion | Escribir en HeyGen |
|---|---|
| Frugle | Frúgol |
| Netfrux | Netfrux (si falla: Net frucs) |
| FrutiTech | Fruti Tec |

---

## 3. HeyGen

### 1.20 · Confesionario

- **Imagen o avatar:** `Imagenes/Don Harold_ Jefe de Gestión Humana.png` (créenlo como avatar a partir de foto).
- **Formato:** 16:9, 1080p.
- **Voz:** la de Don Harold.
- **Texto que dice:**

```
¿Yo, improvisar? Por favor. Yo no improviso: yo copio con seguridad.
```

- **Prompt de movimiento o gestos** (si HeyGen muestra un campo para describir la actuación):

```
Offended and theatrical. He places one hand on his chest at "¿Yo, improvisar?", raises his eyebrows, then relaxes with a smug, proud smile at "yo copio con seguridad". Static camera, documentary interview style.
```

- **Tono:** ofendido al principio y orgulloso al final. Si HeyGen tiene control de emoción o estilo de la voz, elijan uno dramático o enérgico.
- **Pausa:** después de "Por favor", para que caiga el remate.

### 1.07 · Sala de juntas

- **Imagen:** el fotograma 1.07 de ChatGPT.
- **Formato:** 16:9, 1080p.
- **Voz:** la de Don Harold.
- **Texto que dice** (con la pronunciación corregida si hizo falta):

```
Señores: Frugle lo hace. Netfrux lo hace. Y desde hoy, Fruti Tec también: ¡el modelo tres por dos!
```

- **Prompt de movimiento o gestos:**

```
Showman energy. He points the remote at the screen at "el modelo tres por dos", chest out, big proud smile, slight nod on each brand name. Body and camera mostly still, no walking.
```

**Texto en pantalla** (se agrega en edición, no se le pide a HeyGen): **Modelo 3x2:** tres días en oficina, dos en casa.

---

## 4. Runway

Runway anima la imagen inicial. El prompt describe **solo el movimiento**, no a los personajes, porque la imagen ya los tiene. Usen el modelo de imagen a video más reciente de su plan, en 16:9, de 8 a 10 segundos.

Si Runway tiene campo de prompt negativo, peguen siempre este:

```
text, letters, words, subtitles, watermark, logo, deformed hands, extra fingers, duplicated character, human ears, morphing face, blurry face, 2D cartoon, anime
```

### 1.20 · Confesionario (comparación)

**Imagen inicial:** `Imagenes/Don Harold_ Jefe de Gestión Humana.png`

```
Static camera, documentary interview. The avocado man looks straight at the camera, offended, and slowly places his right hand on his chest, raises his eyebrows, then gives a smug proud smile. He speaks with natural mouth movement. Subtle natural head motion, his face and glasses stay consistent.
```

**Voz:** el clip sale sin la voz de Don Harold. Hay dos opciones:

- Si su plan tiene sincronización de labios (*Lip Sync*), súbanle el audio de 1.20 exportado desde HeyGen.
- Si no la tiene, móntenlo en edición y califiquen el clip solo por imagen.

### 1.07 · Sala de juntas (comparación)

**Imagen inicial:** el fotograma 1.07 de ChatGPT.

```
Medium shot, camera almost static with a very slow push-in. The avocado man proudly points the remote at the blank screen with a theatrical flourish, chest out, nodding with a big confident smile while talking enthusiastically. The plants and the city behind stay still. His face, glasses and tie stay consistent.
```

**Voz:** igual que en 1.20. Usen el audio de 1.07 de HeyGen, ya sea con la sincronización de labios de Runway o montado en edición.

### 1.26 · Dedo sobre ENTER

**Imagen inicial:** el fotograma 1.26 de ChatGPT.

```
Extreme close-up. The green avocado-skin finger trembles nervously one centimetre above the Enter key, hesitating, never pressing it. Dramatic fast zoom-in toward the finger, then the camera holds still. Tense lighting, the screen glow flickers softly on the skin. No people speaking, silence.
```

**Si el dedo presiona la tecla,** agreguen al prompt `the finger never touches the key` y regeneren. En edición, el último cuadro se congela, y sobre la imagen congelada entran el texto **DECISIÓN 1** y la consola con la votación.

---

## 5. Narrador de 1.26

El narrador no va en ningún prompt: se graba aparte y se monta encima. Definan **una sola voz de narrador para toda la película**:

- grabada por un integrante con buen micrófono y en silencio, o
- una voz de HeyGen grave, lenta y de tono de telenovela, distinta a la de Don Harold.

```
Un clic. Trescientos colaboradores. Una cultura en juego. ¿Qué debe hacer Don Harold?
```

Dejen pausas largas entre frase y frase. Debe durar más o menos lo mismo que el clip, unos 8 segundos.

---

## 6. Hoja de evaluación

Califiquen de 1 a 5 cada criterio en cada clip. Con un solo intento por clip basta; anoten si hubo que repetir.

| Criterio | 1.20 HeyGen | 1.20 Runway | 1.07 HeyGen | 1.07 Runway | 1.26 Runway |
|---|---|---|---|---|---|
| Se parece a Don Harold (gafas, tallito, corbata) | | | | | — |
| La cara no se deforma durante el clip | | | | | — |
| Labios sincronizados con la voz | | | | | — |
| El gesto o movimiento es el que se pidió | | | | | |
| Manos correctas (cinco dedos, piel de aguacate) | | | | | |
| Se ve como película 3D, no como dibujo ni foto | | | | | |
| **Total** | | | | | |
| Intentos | | | | | |
| Créditos gastados | | | | | |
| Minutos de espera | | | | | |

**Voz elegida para Don Harold:** ____________________ &nbsp;&nbsp; **Voz del narrador:** ____________________

### Cómo decidir

| Si pasa esto… | …se hace esto |
|---|---|
| HeyGen gana o empata en 1.20 y 1.07 | Se sigue el plan de `06-Version-Sustentacion.md` tal cual |
| Runway gana claramente en 1.07 y tiene sincronización de labios | Las filas con fotograma de ChatGPT pasan a Runway, con voz de HeyGen. Los confesionarios se quedan en HeyGen |
| HeyGen deforma la cara en el fotograma de ChatGPT, pero no en la imagen original | HeyGen solo para confesionarios. El resto, Runway con la voz montada en edición |
| Runway gasta más de 3 intentos en 1.26 | Bajar el movimiento: sin zoom en Runway; el zoom se hace en edición |
| Los créditos de una herramienta no alcanzan para su parte | Mover sus filas de prioridad 2 a fotograma con zoom (ver `06-Version-Sustentacion.md`) |

**Cuenta rápida de créditos.** Multipliquen los créditos que gastó cada clip por el número de filas de esa herramienta: 133 de HeyGen y 55 de Runway, contando 2 o 3 intentos por fila en Runway. Si el total pasa lo que tienen, empiecen solo con la prioridad 1: 84 de HeyGen y 34 de Runway.
