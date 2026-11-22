# Corazón de Pulpa · Mini película interactiva (8 minutos)

> **Actualización:** las voces ahora las hace Grok. Los prompts definitivos de cada escena, con diálogo y voz, están en `10-Guion-Grok-con-Voz.md`. Ese documento reemplaza las columnas "Voz" y "Grok" de este.

Esta versión reemplaza los 30 minutos. Usa la misma historia, los mismos personajes y la misma consola, pero condensada.

- **Película:** 8:06 de video.
- **Función completa:** unos 12 minutos, contando las votaciones.
- **Votaciones:** 3 paradas, con 5 votos en total.
- **Movimiento:** Grok Imagine (imagen → video, clips de 6 o 10 s).
- **Imágenes iniciales:** las 4 de `Imagenes/` tal cual, o fotogramas nuevos hechos con ChatGPT o Grok usando esas imágenes como referencia.
- **Voz, música, subtítulos y textos académicos:** los ponemos nosotros en edición con el pipeline (`Pipeline/`).

---

## 1. La historia en una página

FrutiTech vive con una regla: *"Aquí todo se hace con pulpa"*.

1. **Prólogo.** Diciembre. Una gala moderna, fría y vacía. Don Harold brinda solo y grita *"¡Así lo hace Frugle!"*. Daniel guarda un sobre de renuncia. *"Tres meses antes…"*
2. **El atajo.** Don Harold vuelve del congreso con el modelo 3x2 de Frugle y quiere copiarlo tal cual, "solo cambiándole el logo". Valentina pide diagnóstico y Daniel pregunta por la planta. Valentina recuerda que la seguridad y la nómina no se adaptan: se cumplen. El dedo de Harold queda sobre ENTER. **El salón vota (D1), pero Harold envía igual.**
3. **Pura cáscara.** Se instala el modelo:
   - vigilancia cada 5 minutos ("¡Pensar no mueve el mouse, mijo!");
   - viernes flexible para la torre y un fondo de pantalla de playa para la planta;
   - Don Lulo: "Veinte años aquí y nadie vino a preguntarnos";
   - la novena con buñuelos cambiada por una gala importada.

   Daniel escribe su renuncia. Una mano de piña detiene el sobre.
4. **Comercial: Isomorfina Forte.** "¿Su empresa sufre de incertidumbre? ¡Copie al líder!"
5. **La Piña ha hablado.** El Prof. Carlos Mario explica el isomorfismo mimético (DiMaggio y Powell) y VRIO (Barney). Rompe la cuarta pared y le pide ayuda a la junta. **D2 es una prueba VRIO de 2 preguntas.** Luego le entrega el mando al salón: *"¿Y cómo lo hacemos aquí?" → "¡Con pulpa!"*
6. **Diagnóstico con alma.** Esta vez sí se pregunta, a la torre y a la planta. Don Harold aprende a soltar: "El que no había madurado era yo". **D3 son 2 decisiones que ahora sí se ejecutan:** qué se le da a la planta y qué fiesta se hace en diciembre.
7. **Final.** La consola revela los indicadores. Con promedio ≥ 55 se proyecta **"Con pulpa"** (novena, buñuelos, Daniel se queda). Si no, **"Pura cáscara"** (FrutiTech sobrevive, idéntica a todas).

Cobertura del artículo:

| Parte del artículo | Dónde aparece |
|---|---|
| Camino corto e introducción | Cap. 1 |
| Excepción normativa (7.1) | Valentina, 1.6 |
| Fractura 1, liderazgo que no escucha (5.4.1) | D1 ignorada, vigilancia |
| Fractura 2, falsa equidad (5.4.2) | Planta y Don Lulo |
| Fractura 3, miopía de TH (5.4.3) y costo en cultura (5.4.4) | Gala y renuncia |
| Isomorfismo (4.1) | Comercial y cap. 3 |
| VRIO (4.2) y Wright et al. (2001) | Cap. 3 |
| Adaptar como tamiz (5.4.4) y Gratton (2021) | Cap. 4 |
| Conclusiones | Finales y créditos |

---

## 2. Cómo se hace cada clip

### Ruta A · Imagen original directa (la más consistente)

Se sube a Grok la imagen de `Imagenes/` tal cual y se anima. Sirve para los confesionarios: el personaje en su escritorio, hablándole a la cámara. **21 clips** usan esta ruta.

### Ruta B · Fotograma nuevo y después Grok

1. **Fotograma (keyframe).** En ChatGPT o en Grok Imagine (modo imagen), suban la(s) imagen(es) original(es) del personaje y peguen el prompt **K** de la sección 4. Pidan formato 16:9.
2. **Revisen.** La cara, la fruta y la ropa tienen que ser las mismas del original. Si no, repitan.
3. **Animación.** Suban ese fotograma a Grok Imagine → **Video** → peguen el prompt de la columna "Grok".

### Ajustes de Grok Imagine

| Ajuste | Valor |
|---|---|
| Modo | Video |
| Proporción | 16:9; si no aparece, 3:2 y yo recorto |
| Resolución | La más alta disponible (720p si la hay); yo escalo a 1080p |
| Duración | La que dice la tabla (6 s o 10 s) |

Guarden cada video con el nombre de su ID, por ejemplo `1.2.mp4`, en `Produccion/grok/`.

### Voces

Grok puede generar audio, pero la voz cambia de un clip a otro.

- **Grok mueve la boca.** Por eso el prompt incluye la línea entre comillas: así el movimiento de boca dura lo mismo que la frase.
- **La voz final la pongo yo**, con edge-tts actuada (`Pipeline/actuar.py`), para que cada personaje suene igual toda la película.
- **Prueba primero.** Generen el clip **1.2**. Si el español de Grok suena bien y la boca va con la frase, podemos dejar la voz de Grok en algunos clips.

### Reglas para que Grok no se equivoque

- Un solo personaje habla por clip. Máximo unas 20 palabras en 10 s, o 10 palabras en 6 s.
- Una sola acción y un solo movimiento de cámara por clip.
- **Nada de texto dentro del video.** Letreros, títulos, citas APA y subtítulos van en edición. Por eso los prompts terminan con *no text*.
- Todos los prompts cierran con el **candado de personaje**: *keep the character's face, fruit head and clothes exactly as in the reference image*.

---

## 3. Fichas de personaje (para pegar en los prompts)

Están en inglés porque Grok y los generadores de imagen las siguen mejor. Los diálogos van en español.

| Clave | Ficha |
|---|---|
| **HAROLD** | anthropomorphic avocado man: his whole head is a bumpy green avocado with a small brown stem on top, real middle-aged Latino man's face, brown tortoiseshell glasses, black hair on the sides, green avocado-skin hands, dark pinstripe suit, black shirt, navy blue tie |
| **VALENTINA** | strawberry woman: bright red strawberry skin with tiny yellow seeds on face, neck and hands, crown of green strawberry leaves, long straight dark brown hair, big gold hoop earrings, braces, lilac blazer, white shirt, pearl bracelet |
| **DANIEL** | mango young man: his head is a ripe red-orange-yellow mango with dew drops, a green leaf and stem on top, short black hair, mango-skin hands, navy blazer, light blue shirt |
| **PIÑA** | pineapple man (Prof. Carlos Mario): his head is a golden pineapple with a tall spiky green crown, curly black hair, short dark beard, pineapple-textured hands, dark pinstripe suit, white shirt, red tie, red pocket square |
| **LULO** | lulo man (Colombian naranjilla): round orange lulo fruit head with fine fuzz and a small green star-shaped calyx on top, real 55-year-old Colombian man's face, grey mustache, kind tired eyes, navy blue work overalls, white hairnet, rubber apron |

**Estilo común (va en todos los K):** *photorealistic cinematic 3D, fruit-people telenovela, warm golden lighting, shallow depth of field, 16:9, same art style as the reference images, no text.*

---

## 4. Fotogramas nuevos (prompts K para ChatGPT o Grok imagen)

Cada prompt empieza igual: **"Using the uploaded image(s) as exact character reference (same face, same fruit head, same clothes):"**, seguido del texto de la tabla y del estilo común.

| K | Suban | Prompt |
|---|---|---|
| **K00 · Don Lulo (referencia)** | La imagen de Harold, solo como referencia de estilo | Create a NEW character in exactly the same art style: LULO [ficha]. He sits at a worn wooden table inside a fruit processing plant, steel peeling machine and crates of fruit behind him, looking at the camera with a gentle half smile. Same framing as the reference: chest-up, desk in front. |
| **K01 · Gala vacía** | Harold | HAROLD stands alone in the middle of a huge corporate gala inside a factory hall, cold blue LED lights, glossy black tables, empty dance floor, he raises a champagne glass with a forced proud smile. Wide shot. |
| **K02 · Daniel con el sobre** | Daniel | DANIEL sits alone at a corner table of the same cold blue gala, holding a sealed white envelope, sad eyes. Medium shot. |
| **K03 · Llegada del congreso** | Harold | HAROLD walks into a modern office lobby pulling a carry-on suitcase, wearing a conference lanyard, energized grin, green plants and warm wood walls. Wide shot, he walks toward camera. |
| **K04 · Sala de juntas** | Harold + Valentina + Daniel | Boardroom with a large blank screen. HAROLD stands presenting with arms wide open; VALENTINA and DANIEL sit at the table looking skeptical. Warm office light. Medium-wide shot. |
| **K05 · El dedo y el ENTER** | Harold | Extreme close-up of HAROLD's green avocado finger hovering one centimeter above the ENTER key of a laptop, his blurred face and glasses in the background, dramatic side light. |
| **K06 · Oficina "moderna"** | (ninguna) | Modern open office with an unused ping-pong table, colorful beanbags, a nap pod, and a ceiling security camera; fruit-people employees typing stiffly at desks. Cold light. Wide shot. |
| **K07 · Daniel vigilado** | Daniel | DANIEL at his desk with his hand on his chin thinking; the webcam on his monitor glows red. Medium close-up. |
| **K08 · La planta** | La imagen K00 de Lulo | LULO works at a steel fruit peeling machine inside the plant, steam, crates of mangoes and lulos; on a shelf next to him a small monitor shows a tropical beach wallpaper. Medium shot. |
| **K09 · Cambio de afiche** | Harold | HAROLD in a hallway peeling off a handmade colorful paper poster with drawings of buñuelos and Christmas lights, and replacing it with a glossy black and silver corporate poster. Medium shot. |
| **K10 · La renuncia** | Daniel | DANIEL at home at night typing on a laptop, face lit only by the screen, a white envelope next to the keyboard. Close-up. |
| **K11 · La mano de piña** | Daniel + Piña | At the cold blue gala, DANIEL slides a white envelope across a table; a golden pineapple-textured hand with a pinstripe sleeve and red cuff enters the frame and presses the envelope down. Close-up on the hands. |
| **K12 · La Piña entra** | Piña | PIÑA walks into the dark gala hall under a single spotlight, the music has stopped, the guests turn to look at him. Wide shot, low angle. |
| **K13 · La Piña al salón** | Piña | PIÑA stands center frame looking straight into the camera, pointing at the viewer with a confident half smile, dark background with a warm rim light. Medium shot. |
| **K14 · Isomorfina Forte** | Harold | TV commercial set: HAROLD in a white lab coat over his suit, overly bright smile, holding up a large unlabeled pill bottle, pastel studio background. Medium shot. |
| **K15 · Oficinas clonadas** | (ninguna) | A row of six identical glass office buildings, identical gray logos, identical gray people walking in sync, overcast sky. Wide shot. |
| **K16 · Mesa de diagnóstico** | Valentina + Daniel + Lulo + Harold | Long table inside the fruit plant: VALENTINA, DANIEL, LULO and several plant workers and office workers sit together with sticky notes and coffee; HAROLD sits next to LULO listening. Warm light. Wide shot. |
| **K17 · Turnos** | Lulo | LULO and three plant workers in front of a whiteboard with a colorful shift grid of sticky notes, smiling. Medium shot. |
| **K18 · Novena** | Todos + Lulo | The fruit plant decorated for a Colombian Christmas novena: paper garlands, warm string lights, a big pan of hot oil with golden buñuelos; LULO frying buñuelos, HAROLD with an apron next to him, VALENTINA, DANIEL, PIÑA and workers around laughing. Wide shot. |
| **K19 · Gala final** | Harold | Same cold blue gala as K01, perfect decoration, almost empty; HAROLD alone at a long table checking his phone. Wide shot. |
| **K20 · Escritorio vacío** | Daniel | DANIEL's office desk empty: no nameplate, a cardboard box, his mango mug left behind, gray light. |
| **K21 · Puerta de la planta** | Harold | December evening, HAROLD walks nervously toward the big metal door of the fruit plant, warm light leaking under the door. Medium shot from behind. |

---

## 5. Escaleta con prompts para Grok

**Columnas:**

- **Imagen:** `ORIG-X` es la imagen original del personaje X; `K..` es un fotograma de la sección 4; `L` es un gráfico que hago yo en el PC, sin Grok.
- **Grok:** el prompt de movimiento. A todos agréguenle al final: *Keep the character's face, fruit head and clothes exactly as in the image. No text, no subtitles.*
- **Origen:** la fila del guion largo de donde sale la escena.

### `prologo.mp4` · 0:28

| ID | s | Imagen | Grok | Voz | En pantalla (edición) | Origen |
|---|---|---|---|---|---|---|
| P1 | 10 | K01 | Slow dolly-in. Harold raises his champagne glass toward an empty dance floor; silver confetti falls slowly; his proud smile fades into loneliness. | NARRADOR: "Diciembre. FrutiTech tenía la fiesta más moderna de su historia… y nadie quería estar ahí." | — | P-01 |
| P2 | 6 | K02 | Slow push-in to the envelope. Daniel looks at the envelope, sighs, and slides it into his inner jacket pocket. | — | — | P-03 |
| P3 | 6 | ORIG-HAROLD | Quick zoom-in. Harold lowers the paper, raises his fist proudly and shouts: "¡Así lo hace Frugle!" | HAROLD: "¡Así lo hace Frugle!" | — | P-04 |
| P4 | 6 | L | — | NARRADOR: "Tres meses antes…" | Título sobre negro | P-05 |

→ **Consola:** ensayo del grito.

### `cabezote.mp4` · 0:30 (presentación de telenovela)

| ID | s | Imagen | Grok | Voz | En pantalla | Origen |
|---|---|---|---|---|---|---|
| C1 | 6 | ORIG-HAROLD | Dramatic slow orbit. Harold adjusts his glasses and raises one eyebrow at the camera like a telenovela villain. | Canción | "Don Harold · Director de Talento Humano" | C-01 |
| C2 | 6 | ORIG-VALENTINA | Slow push-in. Valentina turns from the hologram to the camera and gives a confident smile. | Canción | "Valentina · Estratega VRIO" | C-02 |
| C3 | 6 | ORIG-DANIEL | Slow push-in. Daniel lifts his eyes from his laptop, looks at the camera, and gives a shy half smile. | Canción | "Daniel · Analista de Talento" | C-03 |
| C4 | 6 | ORIG-PIÑA | The scene is in silhouette, backlit. Piña slowly lowers his hand from his chin; only his eyes catch the light. | Canción | "¿…?" | C-04 |
| C5 | 6 | L | — | Canción | Logo "Corazón de Pulpa" | C-05 |

### `cap01.mp4` · El atajo · 1:12

| ID | s | Imagen | Grok | Voz | En pantalla | Origen |
|---|---|---|---|---|---|---|
| 1.1 | 10 | K03 | Tracking shot backward. Harold strides toward the camera pulling his suitcase, waving at people off screen, full of energy. | NARRADOR: "Don Harold volvió del congreso con una idea brillante… y sin ninguna gana de esperar." | Letrero "Aquí todo se hace con pulpa" | 1.01 |
| 1.2 | 10 | K04 | Slow push-in on Harold. Harold opens his arms wide and speaks excitedly to the table: "¡Señores! Frugle trabaja tres días en casa y dos en la oficina. Lo copiamos tal cual." Valentina and Daniel exchange a look. | HAROLD (la misma línea) | Pantalla: "Modelo 3x2" | 1.07 |
| 1.3 | 6 | K04 | Snap zoom to Harold's face. He winks and says: "Solo hay que cambiarle el logo." | HAROLD: "Solo hay que cambiarle el logo." | — | 1.08 |
| 1.4 | 10 | ORIG-VALENTINA | Static camera, slight handheld feel. Valentina turns from the hologram to the camera and says calmly but firmly: "Don Harold, primero hay que preguntarle a la gente. Eso se llama diagnóstico." | VALENTINA (la misma línea) | — | 1.19 |
| 1.5 | 10 | ORIG-DANIEL | Slow push-in. Daniel takes his hand off his chin, frowns and says: "¿Y la planta? Los de la planta no pueden trabajar desde la casa." | DANIEL (la misma línea) | — | 1.15 |
| 1.6 | 10 | ORIG-VALENTINA | Valentina taps the hologram and counts on her fingers while saying: "Y ojo: la seguridad y la nómina no se adaptan. Se cumplen." | VALENTINA (la misma línea) | "Se cumple ≠ se diseña" | 2.05 |
| 1.7 | 10 | ORIG-HAROLD | Snap zoom-in. Harold takes off his glasses, laughs arrogantly and says: "¿Yo? ¿Improvisar? Por favor. Lo que funciona en Frugle funciona en todas partes." | HAROLD (la misma línea) | — | 1.20 |
| 1.8 | 6 | K05 | Very slow push-in. The avocado finger trembles above the ENTER key; tension; a drop of sweat falls. | Latido (efecto) | Correo "Implementar Modelo 3x2" | 1.26 |

→ **Consola: D1 · ¿Don Harold envía el 3x2 tal cual o primero diagnostica?** Verde DUPLICAR = enviar; roja ADAPTAR = diagnosticar.

| Video | s | Imagen | Grok | Voz |
|---|---|---|---|---|
| `cap01-duplicar.mp4` | 10 | K05 | Pull back to reveal Harold; he presses ENTER triumphantly and throws his arms up: "¡Hasta la junta está de acuerdo! ¡Enviado!" | HAROLD (la misma línea) |
| `cap01-adaptar.mp4` | 10 | K05 | Pull back to reveal Harold; he looks at the camera with a condescending smile, says "Muy bonito, junta… pero así lo hace Frugle", and presses ENTER. | HAROLD (la misma línea) → grito del salón |

### `cap02.mp4` · Pura cáscara · 1:30

| ID | s | Imagen | Grok | Voz | En pantalla | Origen |
|---|---|---|---|---|---|---|
| 2.1 | 6 | K06 | Slow lateral pan across the office; nobody uses the ping-pong table or the beanbags; the security camera turns toward the lens. | NARRADOR: "El 3x2 llegó completo…" | Letrero "PROHIBIDO" en el ping-pong | 3.03 |
| 2.2 | 10 | K07 | Daniel is thinking calmly; the webcam light flashes red; he jumps, startled, and frantically shakes his mouse. | HAROLD (en off): "¡Pensar no mueve el mouse, mijo!" | Ventana "Inactivo 5 min" | 3.12 |
| 2.3 | 6 | ORIG-HAROLD | Quick zoom-in. Harold points at the camera, annoyed, and shouts: "¡Pensar no mueve el mouse, mijo!" | (la voz va sobre 2.2 y 2.3) | — | 3.13 |
| 2.4 | 10 | K08 | Slow push-in. Lulo peels fruit at the machine, pauses, glances at the beach wallpaper on the monitor, and shakes his head with a tired smile. | NARRADOR: "Para la torre, viernes flexible. Para la planta… un fondo de pantalla de playa." | — | 4.08 |
| 2.5 | 10 | K00 | Static camera. Lulo looks at the camera and says softly: "Veinte años aquí… y nadie vino a preguntarnos nada." | LULO (la misma línea) | — | 4.14 |
| 2.6 | 6 | K08 | Daniel (mango man, navy blazer) enters the frame, listens to Lulo, and nods while writing in a notebook. | — | — | 4.18 |
| 2.7 | 10 | ORIG-VALENTINA | Slow push-in. Valentina lowers the tablet, sad, and says: "Copiaron la cáscara. La pulpa se quedó afuera." | VALENTINA (la misma línea) | — | 4.22 |
| 2.8 | 10 | K09 | Harold rips off the colorful handmade poster, crumples it, and sticks up the glossy corporate poster, satisfied. | NARRADOR: "Y para diciembre… la fiesta también vino importada." | Afiches "Novena con buñuelos" → "Gala FrutiVerso" | 5.12 |
| 2.9 | 10 | K10 | Slow push-in. Daniel types slowly, stops, closes his eyes, and presses one last key. | DANIEL (en off): "Querido Don Harold: aquí ya no hay pulpa." | Carta en la pantalla | 5.24 |
| 2.10 | 6 | K11 | The pineapple hand presses the envelope down firmly; Daniel's hand freezes. | Golpe musical | — | 5.30 |
| 2.11 | 6 | K02 | Daniel looks up, surprised, at someone standing beside him. | — | — | 6.00 |

→ **Consola:** indicadores (fin del Acto 1).

### `comerciales.mp4` · Isomorfina Forte · 0:30

| ID | s | Imagen | Grok | Voz | En pantalla | Origen |
|---|---|---|---|---|---|---|
| CM1 | 10 | K14 | Cheesy commercial zoom-in. Harold shakes the pill bottle next to his face and says with a salesman smile: "¿Su empresa sufre de incertidumbre? ¡Copie al líder!" | HAROLD (la misma línea) | Etiqueta "ISOMORFINA FORTE" | CM1-01 |
| CM2 | 10 | K15 | Slow aerial push over the identical buildings; the gray people walk perfectly in sync. | NARRADOR: "Isomorfina Forte: ¡todas las empresas iguales, en una sola toma!" | — | CM1-03 |
| CM3 | 10 | ORIG-DANIEL | Daniel reads very fast with a deadpan face, like the legal disclaimer at the end of a commercial. | DANIEL (rapidísimo): "Efectos secundarios: pérdida de identidad, mal clima y empresas pura cáscara. Consulte a su Piña de confianza." | Letra pequeña | CM1-05 |

### `cap03.mp4` · La Piña ha hablado · 0:40 + reacciones

| ID | s | Imagen | Grok | Voz | En pantalla | Origen |
|---|---|---|---|---|---|---|
| 3.1 | 10 | K12 | Low-angle slow push-in. Piña walks into the spotlight, stops, and says calmly: "Un momento. Esto no es un error de presupuesto. Es un error de estrategia." | PIÑA (la misma línea) | — | 6.02 |
| 3.2 | 10 | ORIG-PIÑA | Slow push-in. Piña lowers his hand from his chin and explains: "Cuando una empresa duda, copia al líder. Eso se llama isomorfismo mimético." | PIÑA (la misma línea) | "DiMaggio y Powell (1983)" | 6.06 |
| 3.3 | 10 | ORIG-PIÑA | The hologram pulses; Piña counts on his fingers: "Pero lo que todos copian no es ventaja. Valioso, raro, inimitable y organizado." | PIÑA (la misma línea) | "V · R · I · O — Barney (1991)" | 6.10 |
| 3.4 | 10 | K13 | Snap zoom-in. Piña points at the viewer and smiles: "Ustedes, la junta. Ayúdenme a probarlo." | PIÑA (la misma línea) | — | 6.19 |

→ **Consola: D2 · Prueba VRIO** (verde SÍ / roja NO, 15 s cada una).

| Pregunta | Correcta | Video | s | Imagen | Grok | Voz |
|---|---|---|---|---|---|---|
| ¿El 3x2 de Frugle es **RARO**? | NO | `cap03-r.mp4` | 10 | ORIG-PIÑA | Piña shakes his head slowly with a knowing smile and says: "No. Lo tiene medio mundo. Valioso pero común: eso es empate, no ventaja." | PIÑA (la misma línea) |
| ¿La novena con buñuelos de Don Lulo es **DIFÍCIL DE IMITAR**? | SÍ | `cap03-i.mp4` | 10 | ORIG-PIÑA | Piña nods, touches his chest, and says warmly: "Sí. Veinte años de historia no se descargan de internet. Eso es pulpa." | PIÑA (la misma línea) + "Wright et al. (2001)" |

| Video | s | Imagen | Grok | Voz |
|---|---|---|---|---|
| `cap03-fin.mp4` | 10 | K13 | Piña extends his open hand toward the camera as if handing over a key, and says solemnly: "Desde ahora, las decisiones las toman ustedes." | PIÑA (la misma línea) |

→ **Consola:** capital de confianza y grito nuevo: *"¿Y cómo lo hacemos aquí?" → "¡Con pulpa!"*

### `cap04.mp4` · Diagnóstico con alma · 0:40 + reacciones

| ID | s | Imagen | Grok | Voz | En pantalla | Origen |
|---|---|---|---|---|---|---|
| 4.1 | 10 | K16 | Slow lateral dolly along the table; people talk, laugh, and stick notes; Lulo speaks while Harold listens and nods. | NARRADOR: "Esta vez sí preguntaron. A la torre… y a la planta." | — | 7.02 |
| 4.2 | 10 | ORIG-VALENTINA | Valentina points at the hologram, then at the camera: "Adaptar es pasar la buena práctica por el tamiz de lo que somos." | VALENTINA (la misma línea) | "Arango, Constain y Suárez (2026)" | 7.08 |
| 4.3 | 10 | K16 | Push-in on Harold. He takes off his glasses, looks at Lulo, and says humbly: "El que no había madurado era yo." | HAROLD (la misma línea) | — | 7.15 |
| 4.4 | 10 | ORIG-PIÑA | Slow push-in. Piña speaks with a gentle smile: "El trabajo híbrido no se importa. Se diseña con la gente." | PIÑA (la misma línea) | "Gratton (2021)" | 7.17 |

→ **Consola: D3 · Ahora sí se ejecuta** (30 s cada una).

| Decisión | Verde DUPLICAR | Roja ADAPTAR |
|---|---|---|
| **D3a · Para la planta** | Copiar el viernes flexible de la torre | Diseñar turnos con Don Lulo |
| **D3b · Para diciembre** | Gala FrutiVerso importada | Novena con buñuelos |

| Video | s | Imagen | Grok | Voz |
|---|---|---|---|---|
| `cap04-a-duplicar.mp4` | 10 | K08 | Lulo reads a printed memo in front of the machine, scratches his head, and shrugs: "¿Viernes flexible? ¿Y quién pela la fruta los viernes?" | LULO (la misma línea) |
| `cap04-a-adaptar.mp4` | 10 | K17 | Lulo sticks the last note on the shift board, and the workers clap: "Turnos que armamos nosotros mismos. Así sí." | LULO (la misma línea) |
| `cap04-b-duplicar.mp4` | 10 | K09 | Harold hesitates in front of the glossy poster, then straightens it and walks away; the camera stays on the poster. | NARRADOR: "Y diciembre volvió a llegar en plantilla." |
| `cap04-b-adaptar.mp4` | 10 | K16 | Harold stands, picks up a white apron, and offers it to Lulo with a shy smile: "Don Lulo… ¿me enseña a hacer buñuelos?" | HAROLD (la misma línea) |
| `cap04-fin.mp4` | 10 | K21 | Tracking from behind. Harold walks slowly toward the plant door, stops, takes a deep breath, and puts his hand on the handle. | NARRADOR: "Veintiuno de diciembre. Lo que hay detrás de esa puerta… lo decidieron ustedes." |

→ **Consola:** revelación de los indicadores y elección del final.

### `final-con-pulpa.mp4` · 0:56

| ID | s | Imagen | Grok | Voz |
|---|---|---|---|---|
| FA1 | 10 | K18 | The plant door opens to warm light; slow push into the novena; Lulo flips the first golden buñuelo and everybody cheers. | Música alegre |
| FA2 | 10 | K18 | Close-up on Harold: he bites a hot buñuelo, burns his tongue, laughs, and his eyes get teary. | HAROLD: "¡Esto sí es nuestro!" |
| FA3 | 10 | K02 | Daniel takes the envelope out of his pocket, smiles, and tears it in half. | NARRADOR: "Daniel se quedó." |
| FA4 | 10 | K18 | Everyone raises cups of hot chocolate in a toast; string lights twinkle. | VALENTINA: "¡Por FrutiTech, con pulpa!" |
| FA5 | 10 | ORIG-PIÑA | Piña looks at the camera, nods, and smiles: "Benchmarking sí. Pero con pulpa." | PIÑA (la misma línea) |
| FA6 | 6 | L | — | Título "Con pulpa" |

### `final-pura-cascara.mp4` · 0:56

| ID | s | Imagen | Grok | Voz |
|---|---|---|---|---|
| FB1 | 10 | K21 | Harold opens the door: behind it is the cold blue gala instead of the plant; his face falls. | Música fría |
| FB2 | 10 | K19 | Slow pull-back. Harold sits alone at the long table and stops scrolling his phone. | NARRADOR: "La gala salió perfecta. Como en Frugle." |
| FB3 | 10 | K20 | Slow push-in on the abandoned mango mug; dust in a beam of gray light. | NARRADOR: "Daniel no volvió." |
| FB4 | 10 | K08 | Lulo turns off the machine, hangs his hairnet on a hook, and walks out without looking back. | — |
| FB5 | 10 | ORIG-PIÑA | Piña looks at the camera, serious: "FrutiTech sobrevivió… idéntica a todas las demás. Pura cáscara." | PIÑA (la misma línea) |
| FB6 | 6 | L | — | Título "Pura cáscara" |

### `creditos.mp4` · 0:30

| ID | s | Imagen | Grok / contenido |
|---|---|---|---|
| CR1 | 6 | ORIG-HAROLD | Blooper: Harold sneezes and his glasses fly off; he laughs at the camera. |
| CR2 | 24 | L | Referencias APA, nombres del equipo y declaración de uso de IA (Grok Imagine, ChatGPT, Claude, edge-tts). |

### Resumen de tiempos

| Bloque | Duración |
|---|---|
| Prólogo | 0:28 |
| Cabezote | 0:30 |
| Cap. 1 + reacción | 1:22 |
| Cap. 2 | 1:30 |
| Comercial | 0:30 |
| Cap. 3 + 2 respuestas + cierre | 1:10 |
| Cap. 4 + 2 reacciones + cierre | 1:10 |
| Final | 0:56 |
| Créditos | 0:30 |
| **Película vista** | **8:06** |
| Votaciones y pantallas de la consola | unos 4:00 |
| **Función** | **unos 12 minutos** |

**Trabajo en Grok:**

- 58 clips en total, contando las reacciones y los dos finales.
- Unas 120 generaciones si cada clip necesita 2 intentos.
- Grok gratis tiene un límite diario. Repártanse los clips entre las cuentas del equipo.

**Fotogramas:** 22 (K00 a K21).

---

## 6. Orden de trabajo sugerido

| Día | Qué |
|---|---|
| **Mar 17** | Prueba de 3 clips en Grok: **1.2** (fotograma K04), **1.7** (ORIG-HAROLD) y **3.2** (ORIG-PIÑA). Con eso confirmamos proporción, calidad y si sirve la voz de Grok. Además, el fotograma **K00 · Don Lulo**. |
| **Mié 18** | Todos los fotogramas K. Clips del prólogo, el cabezote y los caps. 1 y 2. Yo armo voces, música y montaje a medida que lleguen. |
| **Jue 19 (mañana)** | Caps. 3 y 4, reacciones, finales y créditos. |
| **Jue 19 (tarde)** | Consola adaptada y ensayo completo. Plan B listo. |
| **Vie 20** | Sustentación. |

---

## 7. Cambios en la consola (después de revisar los prompts)

La consola se reutiliza casi entera: votación, temporizador, indicadores, revelación, menú, teclas y recuperación. Cambia la secuencia.

### Videos

Pasan de 43 a 20:

`prologo` · `cabezote` · `cap01` · `cap01-duplicar` · `cap01-adaptar` · `cap02` · `comerciales` · `cap03` · `cap03-r` · `cap03-i` · `cap03-fin` · `cap04` · `cap04-a-duplicar` · `cap04-a-adaptar` · `cap04-b-duplicar` · `cap04-b-adaptar` · `cap04-fin` · `final-con-pulpa` · `final-pura-cascara` · `creditos`

### Paradas

| Parada | Cambio |
|---|---|
| D1 | Igual que antes: ADAPTAR suma +10 al criterio y Harold envía igual. Temporizador de 45 s. |
| Ráfaga D2 (4 casos), D4, D5, Comerciales 2, cap. 8 y puerta | Se quitan. La excepción normativa queda dentro del clip 1.6. |
| Indicadores | Solo 2 pantallas. Fin del cap. 1: 76/78/60. Fin del Acto 1, después del cap. 2: **45/50/42**. |
| D2 VRIO | 2 preguntas (R e I) en lugar de 4. Cada acierto da +3 VRIO y +5 de criterio. |
| Capital de confianza | Criterio ÷ 5. El criterio máximo es 20, así que el bono máximo es +4. |
| D3a y D3b | Mismo efecto que el D7 actual. ADAPTAR: +8/+7/+6. DUPLICAR: −4/−4/−3. |
| "¿Ver el otro final?" | Se mantiene, usando los primeros 30 s de `final-con-pulpa.mp4` en lugar de un video aparte. |

Con estos números el final depende del salón:

| Votos en D3 | Criterio | Promedio | Final |
|---|---|---|---|
| ADAPTAR + ADAPTAR | Cualquiera | 60 a 66 | "Con pulpa" |
| Uno y uno | Perfecto | 55 | "Con pulpa" por un pelo |
| Uno y uno | Bajo | 49 | "Pura cáscara" |
| DUPLICAR + DUPLICAR | Cualquiera | 38 a 44 | "Pura cáscara" |

Así los votos del Acto 1 sí pesan.

### Para que se sienta "vacano"

- Cuenta regresiva con latido.
- Las tarjetas se iluminan al marcar.
- Las barras de los indicadores caen con sonido.
- Un "flash" de telenovela al revelar el final.
- Una sola pantalla de inicio con el logo.

### Plan B

Hay que actualizar `plan-b/armar-respaldo.ps1`, las tarjetas de `generar-tarjetas.ps1` y el `LEEME.md`.
