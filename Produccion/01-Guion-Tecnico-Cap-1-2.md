# Corazón de Pulpa — Guion técnico
## Prólogo, cabezote, capítulo 1 y capítulo 2

Duración de este tramo: unos 8 minutos de película y 2 pausas de votación.

---

## Cómo leer y usar las tablas

- **Cada fila es un clip de 8 segundos**, salvo que diga otra cosa.
- **Tipo de fila:** `IA` = clip generado con IA de video · `FIJA` = imagen fija con zoom lento hecho en edición · `GRAF` = gráfico o montaje hecho en edición.
- **Los prompts van en inglés** porque los generadores de video los siguen mejor así. El diálogo va en español entre comillas.
- **El texto en pantalla se agrega en edición.** No se le pide a la IA.
- **Las líneas del NARRADOR no van en el prompt.** Se graban aparte con una sola voz y se montan encima.

### Fórmula para armar cada prompt

```
[ESTILO] + [PERSONAJE] + [LOCACIÓN] + prompt de movimiento de la fila
+ He/She says in Colombian Spanish, [VOZ]: "diálogo de la fila"
+ No subtitles, no on-screen text.
```

Si la fila no tiene diálogo del personaje, se reemplaza la línea de voz por: `No dialogue, ambient office sound only.`

### Bloques fijos (se copian idénticos en todos los prompts)

**[ESTILO]**
`Hyperrealistic 3D animated film, cinematic warm lighting, shallow depth of field, anthropomorphic fruit characters with human faces and bodies in business attire, 16:9.`

**[HAROLD]**
`Don Harold, an anthropomorphic avocado man in his fifties: large bumpy green avocado-skin head with a human face, small brown stem on top, thin black hair on the sides, tortoiseshell rectangular glasses, charcoal pinstripe suit, black shirt, royal-blue tie, green avocado-skin hands.`
Voz: `a loud, deep, pompous middle-aged male voice`

**[VALENTINA]**
`Valentina, an anthropomorphic strawberry woman in her late twenties: glossy red strawberry-skin face with small yellow seeds, green leafy crown on top of long straight dark-brown hair, braces on her teeth, large gold hoop earrings, lilac blazer over a white blouse, pearl bracelet, red strawberry-skin hands.`
Voz: `a warm, clear, confident young female voice`

**[DANIEL]**
`Daniel, an anthropomorphic mango young man in his mid-twenties: large rounded mango head with red-to-yellow gradient skin and dew drops, short black hair, a green leaf and small brown stem on top, navy blazer, light-blue shirt, no tie, mango-skin hands.`
Voz: `a young, friendly, slightly shy male voice`
Su "luz": cuando está inspirado, `a soft golden glow radiates from his skin`; cuando lo apagan, `his skin looks dull and matte, no glow`.

**[LOC-LOBBY]** `FrutiTech lobby: double-height modern lobby, dark wood walls, gold accents, big green plants, glass doors, morning light, a large empty wall mural frame behind the reception.`

**[LOC-OFICINA]** `FrutiTech open office: rows of desks with laptops, dark wood and gold details, hanging plants, large windows with a city and green mountains behind.`

**[LOC-JUNTAS]** `FrutiTech boardroom: long dark wooden table, black leather chairs, a large blank screen on the wall, floor-to-ceiling windows with city and mountains.`

**[LOC-HAROLD]** `Don Harold's office: dark wood panelled executive office, big leather chair, desk with a laptop and an avocado mug, window with city view at dusk.`

**[LOC-GALA]** `A cold grey hotel conference room with blue-white lighting, bare walls, a blank white banner, a single small table with identical grey snacks.`

---

## PRÓLOGO · "Lo tenía todo" (0:50)

Adelanto del capítulo 5. Sirve de gancho y deja sembrada la fiesta sin alma que se contrasta al final con la de los buñuelos.

| # | Escena | Personaje | Prompt de movimiento | Diálogo exacto | Texto en pantalla |
|---|---|---|---|---|---|
| P-01 · IA | Fiesta corporativa helada. Frutas de traje gris idéntico, quietas, cada una con el mismo vaso. | Narrador | `Wide shot of [LOC-GALA]. A crowd of anthropomorphic fruits in identical grey suits stand motionless holding identical paper cups, nobody talks. Very slow push-in. Faint elevator music.` | NARRADOR: "FrutiTech lo tenía todo: política híbrida, evaluación trescientos sesenta… y hasta mesa de ping-pong." | *Fiesta de fin de año · FrutiTech S.A.S.* |
| P-02 · IA | Una fruta aplaude una sola vez. Nadie la sigue. | Narrador | `Medium shot in [LOC-GALA]. One fruit in a grey suit claps once, slowly, looks around, stops. The others stare at the floor. Static camera.` | NARRADOR: "Lo tenía todo… menos alma." | — |
| P-03 · IA | Daniel en un rincón, sin brillo, con un sobre blanco en la mano. | Narrador | `Close-up of [DANIEL] standing alone in a corner of [LOC-GALA], his skin looks dull and matte, no glow, sad eyes, holding a plain white envelope against his chest. Slow dolly-in.` | NARRADOR: "Y en un rincón, el talento más brillante de la empresa… se estaba apagando." | — |
| P-04 · IA | Don Harold brinda solo. Silencio. | Don Harold | `Medium shot of [HAROLD] in the centre of [LOC-GALA], raising a paper cup with a forced smile, nobody toasts back, his smile slowly fades. Static camera.` | "¡Salud por… la modernidad!" | — |
| P-05 · GRAF | Los cuatro clips anteriores en reversa acelerada, con sonido de cinta. | Narrador | *(Efecto de rebobinado en edición.)* | NARRADOR: "¿Cómo llegó aquí una empresa que solo quería verse moderna? Hay que volver al día en que un aguacate regresó de un congreso." | **Tres meses antes** |

**Ensayo del grito (en vivo, 20 segundos):** antes de seguir, el presentador le enseña al salón la respuesta: cuando Don Harold diga *"¡Así lo hace Frugle!"*, todos contestan *"¡Pero nosotros no somos Frugle!"*.

---

## CABEZOTE · Canción "Corazón de Pulpa" (0:40)

Cinco clips en cámara lenta, estilo presentación de telenovela, con la canción encima.

| # | Escena | Personaje | Prompt de movimiento | Texto en pantalla |
|---|---|---|---|---|
| C-01 · IA | Don Harold gira hacia cámara y se quita las gafas. | Don Harold | `Slow motion close-up of [HAROLD] in [LOC-HAROLD], turning dramatically to camera and taking off his glasses, golden backlight, soap-opera intro style. No dialogue, no sound.` | **Don Harold** es *El Aguacate* |
| C-02 · IA | Valentina se voltea con el pelo al viento. | Valentina | `Slow motion close-up of [VALENTINA] in [LOC-OFICINA], turning to camera, hair moving in the wind, confident smile showing braces, pink backlight. No dialogue, no sound.` | **Valentina** es *La Fresa* |
| C-03 · IA | Daniel levanta la mirada y brilla. | Daniel | `Slow motion close-up of [DANIEL] in [LOC-OFICINA], looking up from a notebook to camera, a soft golden glow radiates from his skin. No dialogue, no sound.` | **Daniel** es *El Mango* |
| C-04 · IA | Silueta misteriosa con corona de hojas, a contraluz. No se le ve la cara. | Prof. Carlos Mario | `Slow motion silhouette of a man with a pineapple-leaf crown on his head, seen from behind against a bright window in a library office, face not visible, mysterious. No dialogue, no sound.` | *…y la participación especial de* **La Piña** |
| C-05 · GRAF | Título sobre fondo de pulpa de frutas. | — | *(Título animado en edición.)* | **CORAZÓN DE PULPA** · *¿Duplicar o adaptar?* |

**Letra (original, para generar la canción con una IA de música; estilo: balada pop dramática de telenovela latina de los 2000, voz femenina, 40 segundos):**

> Copiaste un modelo que no era pa' ti,
> brillaba por fuera, vacío por dentro.
> Corazón de pulpa, no te dejes clonar,
> que lo que viene de afuera se debe adaptar.
> ¿Duplicar o adaptar? ¡Adaptar!
> Corazón de pulpa… con alma hay que liderar.

---

## CAPÍTULO 1 · "El atajo" (3:45)

**Cubre del artículo:** Introducción. El benchmarking como herramienta, el "camino más corto", la pregunta de investigación y el objetivo general.

| # | Escena | Personaje | Prompt de movimiento | Diálogo exacto | Texto en pantalla |
|---|---|---|---|---|---|
| 1.01 · FIJA | Fachada de la torre FrutiTech al amanecer, montañas al fondo. | Narrador | *(Imagen fija de la torre, zoom lento.)* | NARRADOR: "FrutiTech S.A.S. Trescientos colaboradores, una torre, una planta… y una cultura con sabor propio." | **Capítulo 1: El atajo** · *"Aquí todo se hace con pulpa"* |
| 1.02 · IA | Daniel entra al lobby radiante, con una libreta llena de notas adhesivas. | Daniel | `Medium tracking shot of [DANIEL] walking into [LOC-LOBBY], a soft golden glow radiates from his skin, hugging a notebook full of colourful sticky notes, waving happily at people off-screen.` | "¡Buenos días! Hoy sí le muestro mi propuesta al jefe. Llevo tres semanas escuchando a la gente de planta." | *Daniel · Analista de Talento* |
| 1.03 · IA | Valentina revisa su tableta en la oficina abierta. | Valentina | `Medium shot of [VALENTINA] standing in [LOC-OFICINA], checking a tablet, nodding satisfied, then looking up with a thoughtful expression. Slow push-in.` | "Clima laboral en ochenta y dos por ciento. Nada mal… pero ojo con la planta, Daniel: ahí hay algo que escuchar." | *Valentina · Estratega VRIO* · Clima laboral: 82 % |
| 1.04 · IA | Se abren las puertas de golpe. Don Harold entra con maleta llena de calcomanías, gafas oscuras y la escarapela del congreso todavía colgada. | Don Harold | `Wide shot of [LOC-LOBBY]. Glass doors burst open and [HAROLD] strides in wearing sunglasses and a conference lanyard, dragging a suitcase covered in travel stickers, arms wide open. Camera dollies back.` | "¡Paren todo! ¡Suelten esos computadores! Vengo de Sili-Coco Valley… ¡y vengo del futuro!" | *Don Harold · Director de Talento Humano* |
| 1.05 · IA | Valentina cierra los ojos y respira hondo. | Valentina | `Close-up of [VALENTINA] in [LOC-OFICINA], closing her eyes, sighing deeply, then whispering sideways. Static camera.` | "Ay, no. Cada vez que vuelve de un congreso, nos cambia la empresa." | — |
| 1.06 · IA | **Confesionario** de Daniel, sentado en su escritorio mirando a cámara. *(Usar su imagen original como imagen inicial.)* | Daniel | `[DANIEL] sitting at his desk looking straight at the camera, documentary interview style, rubbing his knee with a pained smile. Static camera.` | "La última vez nos puso a hacer las reuniones de pie. Duró dos días. Mis rodillas todavía se acuerdan." | — |
| 1.07 · IA | Sala de juntas. Don Harold a la cabeza de la mesa, control remoto en mano. | Don Harold | `Medium shot of [HAROLD] standing at the head of the table in [LOC-JUNTAS], pointing a remote at the screen like a showman, chest out.` | "Señores: Frugle lo hace. Netfrux lo hace. Y desde hoy, FrutiTech también: ¡el modelo tres por dos!" | **Modelo 3x2:** tres días en oficina, dos en casa |
| 1.08 · IA | Don Harold camina orgulloso frente a la ventana. | Don Harold | `Tracking shot of [HAROLD] pacing proudly in front of the windows of [LOC-JUNTAS], hands behind his back, chin up.` | "Tres días en la oficina, dos en la casa. ¡Así lo hace Frugle! Y así nos vamos a ver modernos." *(Aquí responde el salón.)* | — |
| 1.09 · IA | Valentina levanta la mano con calma. | Valentina | `Medium shot of [VALENTINA] seated at the table in [LOC-JUNTAS], calmly raising her hand, polite but firm. Static camera.` | "Don Harold, una pregunta: ¿ese modelo qué problema nuestro viene a resolver?" | — |
| 1.10 · IA | Don Harold, desconcertado, se acomoda las gafas. | Don Harold | `Close-up of [HAROLD] in [LOC-JUNTAS], confused, adjusting his glasses with one hand, then throwing both hands up.` | "¿Problema? Valentina, el problema es que no lo tenemos. ¡Todo el mundo lo tiene menos nosotros!" | Copiar para "verse moderno": se busca **legitimidad**, no eficiencia (DiMaggio y Powell, 1983) |
| 1.11 · IA | Daniel abre su libreta, brillando. | Daniel | `Medium shot of [DANIEL] seated in [LOC-JUNTAS], a soft golden glow radiates from his skin, opening his notebook eagerly and leaning forward.` | "Jefe, yo hablé con la gente de planta. Tengo datos, tengo ideas… hasta hice una encuestica." | — |
| 1.12 · IA | Don Harold le da palmaditas en la hoja de la cabeza. El brillo de Daniel parpadea. | Don Harold | `Two-shot in [LOC-JUNTAS]. [HAROLD] pats the leaf on top of [DANIEL]'s head condescendingly. Daniel's golden glow flickers and dims a little.` | "Daniel, mijo, usted todavía está biche. Cuando madure, opina. Mientras tanto, tome nota." | — |
| 1.13 · IA | Valentina se pone de pie. | Valentina | `Medium shot of [VALENTINA] standing up in [LOC-JUNTAS], gesturing with open hands, a soft purple holographic chart floating beside her.` | "Benchmarking no es calcar, Don Harold. Es mirar a los mejores para aprender… y después hacerlo a nuestra manera." | **Benchmarking:** identificar y tomar como referencia las mejores prácticas del mercado |
| 1.14 · IA | Don Harold saca una memoria USB como si fuera una reliquia. Luz dorada. | Don Harold | `Close-up of [HAROLD] in [LOC-JUNTAS] slowly raising a small USB drive above his head like a sacred relic, a golden beam of light falls on it, his face in awe.` | "¿Diagnóstico? Eso se demora. Yo ya traje la política lista. Solo hay que cambiarle el logo." | **"El camino más corto":** duplicar sin crítica modelos que le funcionaron a otros |
| 1.15 · IA | Daniel lee el archivo en el portátil, confundido. | Daniel | `Medium shot of [DANIEL] in [LOC-JUNTAS] reading a laptop screen, squinting, confused, raising a finger.` | "Don Harold… aquí dice que aplica para las sedes de California y Dublín." | — |
| 1.16 · IA | Don Harold lo resuelve con un gesto de la mano. | Don Harold | `Medium shot of [HAROLD] in [LOC-JUNTAS] waving his hand dismissively, then snapping his fingers, very pleased with himself.` | "Pues busque y reemplace, mijo: donde diga California, ponga 'torre'; donde diga Dublín, ponga 'planta'. ¡Listo, adaptado!" | — |
| 1.17 · IA | Daniel sigue leyendo. | Daniel | `Close-up of [DANIEL] in [LOC-JUNTAS] pointing at the laptop screen, looking up worried.` | "¿Y donde dice 'traiga su perro a la oficina'?" | — |
| 1.18 · IA | Don Harold lo piensa tres segundos largos y asiente. | Don Harold | `Close-up of [HAROLD] in [LOC-JUNTAS] thinking hard for a long beat, eyes to the ceiling, then nodding solemnly.` | "Eso déjelo. Se ve moderno." | — |
| 1.19 · IA | **Confesionario** de Valentina. *(Usar su imagen original.)* | Valentina | `[VALENTINA] sitting at her desk looking straight at the camera, documentary interview style, raising one eyebrow, calm and ironic. Static camera.` | "Copiar es fácil. Lo difícil es explicarle a la gente por qué, de un día para otro, somos otra empresa." | Replicar sin considerar la idiosincrasia propia = empresas **"sin alma y sin corazón"** |
| 1.20 · IA | **Confesionario** de Don Harold. *(Usar su imagen original.)* | Don Harold | `[HAROLD] sitting at his desk looking straight at the camera, documentary interview style, offended, hand on chest. Static camera.` | "¿Yo, improvisar? Por favor. Yo no improviso: yo copio con seguridad." | — |
| 1.21 · IA | Pasillo. Daniel camina apagado. | Daniel | `Medium shot of [DANIEL] walking slowly down a corridor of [LOC-OFICINA], shoulders down, his glow weak, hugging his notebook.` | "Valentina… ¿será que sí estoy muy biche para opinar?" | — |
| 1.22 · IA | Valentina le pone la mano en el hombro. El brillo vuelve un poco. | Valentina | `Two-shot in a corridor of [LOC-OFICINA]. [VALENTINA] puts a hand on [DANIEL]'s shoulder, warm smile. Daniel's glow slowly comes back a little.` | "Biche no, Daniel. A usted no le falta madurar: le falta un jefe que escuche." | — |
| 1.23 · FIJA | Oficina de Don Harold al atardecer. Mira una foto enmarcada de un campus futurista. | Narrador | *(Imagen fija de Don Harold de espaldas mirando el cuadro, zoom lento.)* | NARRADOR: "Esa noche, Don Harold tomó una decisión. O mejor dicho: tomó la decisión de otro." | **Objetivo:** evaluar el impacto estratégico del benchmarking en la gestión humana, argumentando la primacía de la adaptación cultural sobre la duplicación mimética |
| 1.24 · IA | Don Harold frente al portátil, hablando solo. | Don Harold | `Medium shot of [HAROLD] at his desk in [LOC-HAROLD] at dusk, face lit by the laptop, talking to himself, convincing himself.` | "Si a Frugle le funcionó, a nosotros también. Al fin y al cabo, todas las frutas somos iguales." | **Pregunta de investigación:** ¿duplicar o adaptar? ¿Cuál es la estrategia correcta? |
| 1.25 · IA | Valentina entra corriendo. | Valentina | `Medium shot of [VALENTINA] rushing through the door of [LOC-HAROLD], one hand stretched forward, urgent.` | "¡Don Harold, espere! Deme dos semanas. Hagamos un diagnóstico antes de enviar eso." | — |
| 1.26 · IA | Primerísimo plano del dedo de aguacate temblando sobre la tecla ENTER. Zoom dramático. Imagen congelada. | Narrador | `Extreme close-up of a green avocado-skin finger trembling one centimetre above a laptop Enter key, dramatic fast zoom-in, tense lighting. No dialogue, dramatic silence.` | NARRADOR: "Un clic. Trescientos colaboradores. Una cultura en juego. ¿Qué debe hacer Don Harold?" | **DECISIÓN 1** |

### PAUSA INTERACTIVA 1 (60 segundos)

> **¿Qué debe hacer Don Harold con la política 3x2?**
> **DUPLICAR** (tarjeta verde): enviarla hoy, tal cual llegó.
> **ADAPTAR** (tarjeta roja): frenar y hacer primero un diagnóstico.

Se cuentan las tarjetas y se reproduce la reacción que corresponda. En ambos casos Don Harold envía el correo: en el Acto 1 el jefe no escucha.

| # | Escena | Personaje | Prompt de movimiento | Diálogo exacto | Texto en pantalla |
|---|---|---|---|---|---|
| 1.27-A · IA | **Si gana DUPLICAR.** Don Harold mira a cámara, feliz, y oprime la tecla. | Don Harold | `Medium shot of [HAROLD] at his desk in [LOC-HAROLD], looking straight at camera, delighted, pointing at the audience, then pressing a key triumphantly.` | "¡Eso! Este salón sí sabe de modernidad. ¡Enviado!" | Criterio gerencial del salón: **+0** |
| 1.27-B · IA | **Si gana ADAPTAR.** Don Harold baja las gafas, mira a cámara, y oprime la tecla de todos modos. | Don Harold | `Medium shot of [HAROLD] at his desk in [LOC-HAROLD], lowering his glasses, looking straight at camera with a patronising smile, then pressing a key anyway.` | "Muy bonita su opinión, muy participativos todos… pero aquí el jefe soy yo. ¡Enviado!" | Criterio gerencial del salón: **+10** |
| 1.28 · IA | El correo llega a toda la oficina. Vibran los celulares. Caras de desconcierto. | Narrador | `Wide shot of [LOC-OFICINA]. Dozens of phones light up and buzz at the same time, fruit employees look at their screens, then at each other, puzzled. Slow crane up.` | NARRADOR *(tras 1.27-A)*: "Y así, con un clic… empezó a dañarse la fruta." / *(tras 1.27-B)*: "El salón tenía razón. Pero a un liderazgo que no escucha… ni el salón lo salva." | *Asunto: Bienvenidos al futuro* · Clima 82 → **76** · Cultura 85 → **78** · VRIO 70 → **60** · **Continuará…** |

---

## CAPÍTULO 2 · "Lo que no se negocia" (3:00)

**Cubre del artículo:** la excepción normativa. En lo legal, regulatorio y de seguridad se estandariza por obligación; en lo cultural, de desarrollo y de experiencia del colaborador, se adapta (Introducción y Conclusión 7.1).

**La idea cómica:** Don Harold lo hace exactamente al revés. Copia lo que debería adaptar y quiere "adaptar" lo que debería cumplir.

| # | Escena | Personaje | Prompt de movimiento | Diálogo exacto | Texto en pantalla |
|---|---|---|---|---|---|
| 2.00 · GRAF | Resumen con los clips 1.07, 1.14 y 1.26. | Narrador | *(Montaje en edición, 10 s.)* | NARRADOR: "Anteriormente, en Corazón de Pulpa…" | **Capítulo 2: Lo que no se negocia** |
| 2.01 · IA | Mañana siguiente. Frutas cuchicheando junto a la cafetera, mirando el celular. | Narrador | `Medium shot near a coffee machine in [LOC-OFICINA]. Three fruit employees whisper and show each other their phones, glancing nervously over their shoulders.` | NARRADOR: "A la mañana siguiente, en FrutiTech nadie hablaba de otra cosa." | — |
| 2.02 · IA | Don Harold cruza la oficina eufórico, con su pocillo de aguacate. | Don Harold | `Tracking shot of [HAROLD] walking through [LOC-OFICINA] holding a black mug, euphoric, greeting employees who avoid eye contact.` | "¿Vieron? Nadie se ha quejado. Bueno, nadie me ha contestado. ¡Que es lo mismo!" | — |
| 2.03 · IA | Sala de juntas. Don Harold se frota las manos. | Don Harold | `Medium shot of [HAROLD] seated in [LOC-JUNTAS], rubbing his hands together, leaning forward with a mischievous grin.` | "Y ya entrados en gastos de modernidad… adaptemos también lo aburrido: la seguridad, la nómina, todo eso." | — |
| 2.04 · IA | Don Harold enumera con los dedos, cada vez más emocionado. | Don Harold | `Close-up of [HAROLD] in [LOC-JUNTAS] counting on his fingers, more excited with each one, ending with both arms up.` | "Simulacro de evacuación: opcional. Casco en planta: según el outfit. Y las horas extras… ¡se pagan con pizza, como en las startups!" | — |
| 2.05 · IA | Valentina deja la tableta sobre la mesa, muy despacio. | Valentina | `Medium shot of [VALENTINA] in [LOC-JUNTAS] slowly putting her tablet down on the table, deadpan expression, folding her hands.` | "Eso no es innovación, Don Harold. Eso es una demanda laboral con pepperoni." | — |
| 2.06 · IA | Daniel levanta la mano con timidez. | Daniel | `Medium shot of [DANIEL] in [LOC-JUNTAS] timidly raising his hand halfway, apologetic smile.` | "Y una visita del Ministerio, jefe. Con multa incluida." | — |
| 2.07 · IA | Valentina se levanta. Aparece un holograma dividido en dos columnas vacías. Señala la izquierda. | Valentina | `Medium shot of [VALENTINA] standing in [LOC-JUNTAS] next to a purple hologram split into two blank columns, pointing firmly at the left column.` | "Mire: hay cosas que se cumplen igual que todo el mundo. La ley no se adapta al gusto: se cumple." | **SE CUMPLE** · Ámbito normativo, regulatorio y de seguridad: un deber ser estandarizado, aplicable por sector |
| 2.08 · IA | Valentina señala la columna derecha. | Valentina | `Medium shot of [VALENTINA] in [LOC-JUNTAS] moving to the right column of the purple hologram, opening her hand toward it, warm tone.` | "Y hay otras que nadie nos puede dictar: la cultura, el desarrollo, la experiencia de nuestra gente. Eso se diseña en casa." | **SE DISEÑA** · Dimensión cultural, de desarrollo y de experiencia del colaborador: adaptar con identidad propia |
| 2.09 · IA | Don Harold se rasca el tallito de la cabeza. | Don Harold | `Close-up of [HAROLD] in [LOC-JUNTAS] scratching the small stem on top of his head, frowning, lost.` | "No entiendo. ¿Entonces copiar es bueno o es malo? ¡Decídase, Valentina!" | — |
| 2.10 · IA | Valentina toma una botella de jugo de la mesa y la muestra. | Valentina | `Medium shot of [VALENTINA] in [LOC-JUNTAS] picking up a small unlabelled glass bottle of orange juice, showing its back, then holding it close to her heart.` | "Piénselo como un jugo: el registro sanitario es igual para todos. La receta… esa es de la casa." | Registro sanitario → **se estandariza** · Receta → **se adapta** |
| 2.11 · IA | A Daniel se le prende el brillo. | Daniel | `Close-up of [DANIEL] in [LOC-JUNTAS], eyes widening, a soft golden glow growing on his skin, raising a finger as he gets the idea.` | "O sea: en lo legal, todos iguales. En lo cultural, nadie igual." | *"En lo legal, todos iguales. En lo cultural, nadie igual."* |
| 2.12 · IA | Valentina mira a Don Harold de frente. | Valentina | `Close-up of [VALENTINA] in [LOC-JUNTAS], looking straight ahead, respectful but firm, slow push-in.` | "Y usted, con todo respeto, lo está haciendo al revés: copia lo que debería adaptar… y adapta lo que debería copiar." | — |
| 2.13 · IA | Don Harold se lleva la mano al pecho. Zoom de telenovela. | Don Harold | `Close-up of [HAROLD] in [LOC-JUNTAS] gasping, hand on chest, mouth open, sudden dramatic soap-opera zoom-in.` | "¡¿Al revés, yo?! ¡Me ofende, Valentina! ¡Me ofende… y me confunde!" | — |
| 2.14 · IA | Cambian las luces a concurso de televisión. Valentina con tarjetas de presentadora. | Valentina | `Medium shot of [VALENTINA] in [LOC-JUNTAS], lights switch to colourful game-show lighting, she holds a stack of cue cards like a TV host and gestures to the camera.` | "Tranquilo, lo vamos a practicar. Juguemos a '¡Se Cumple o Se Diseña!'. Y que el salón le ayude." | **DECISIÓN 2 · RÁFAGA** |

### PAUSA INTERACTIVA 2 · Ráfaga "¿Se cumple o se diseña?" (unos 90 segundos)

Cuatro casos, 10 segundos cada uno. El salón responde primero con las tarjetas (**verde = se cumple, es estándar** · **roja = se diseña, se adapta**). Después se reproduce la respuesta de Don Harold y aparece la correcta. Cada acierto del salón suma 5 puntos de criterio.

| # | Caso | Personaje | Prompt de movimiento | Diálogo exacto | Texto en pantalla (respuesta) |
|---|---|---|---|---|---|
| 2.15 · IA | **Pago de nómina y seguridad social** | Don Harold | `Medium shot of [HAROLD] behind a game-show podium in [LOC-JUNTAS] under colourful lights, slamming a big red buzzer, overconfident.` | "¡Se diseña! Que cada cual cobre cuando le nazca." | ✗ **SE CUMPLE.** Es obligación legal: igual para todos. |
| 2.16 · IA | **Programa de reconocimiento a colaboradores** | Don Harold | `Medium shot of [HAROLD] behind the game-show podium, slamming the buzzer again, winking at the camera.` | "¡Se copia! Frugle regala patinetas eléctricas." | ✗ **SE DISEÑA.** Lo que motiva en California no es lo que motiva en nuestra planta. |
| 2.17 · IA | **Protocolos de seguridad y salud en el trabajo** | Don Harold | `Close-up of [HAROLD] behind the podium, sweating, hesitating, pressing the buzzer softly, then celebrating wildly with both fists up.` | "Se… ¿cumple? ¡Se cumple! ¡Lo sabía! ¡Soy un genio de la gestión humana!" | ✓ **SE CUMPLE.** La seguridad no es opcional ni "según el outfit". |
| 2.18 · IA | **Modelo de trabajo híbrido** | Don Harold | `Medium shot of [HAROLD] behind the podium, relaxed, leaning on it, smug smile, pressing the buzzer with one finger.` | "¡Se copia! Esa es fácil: esa ya la copié." | ✗ **SE DISEÑA.** Y de eso se trata esta historia. |

| # | Escena | Personaje | Prompt de movimiento | Diálogo exacto | Texto en pantalla |
|---|---|---|---|---|---|
| 2.19 · IA | **Confesionario** de Valentina. *(Usar su imagen original.)* | Valentina | `[VALENTINA] sitting at her desk looking straight at the camera, documentary interview style, amused, shaking her head slightly. Static camera.` | "El salón lo tiene clarísimo. Don Harold acertó una… y fue por descarte." | — |
| 2.20 · IA | Don Harold en su oficina, enfurruñado. De pronto se anima. | Don Harold | `Medium shot of [HAROLD] slumped in his leather chair in [LOC-HAROLD], sulking with arms crossed, then suddenly sitting up with a stubborn grin.` | "Bueno. La ley se cumple. Pero mi tres por dos se queda tal cual. ¡Eso sí es estrategia!" | **Conclusión 7.1:** fuera de lo normativo, duplicar por el camino corto priva a la organización de su ventaja competitiva |
| 2.21 · IA | Don Harold abre una caja negra con un ojo brillante en la tapa. | Don Harold | `Medium shot of [HAROLD] at his desk in [LOC-HAROLD] opening a black box with a glowing red eye symbol on the lid, red light on his delighted face.` | "Y para que funcione, traje esto: 'Ojo de Aguacate Pro'. Yo confío plenamente en mi gente…" | — |
| 2.22 · IA | Primerísimo plano. La luz roja se refleja en las gafas. Sonrisa siniestra. | Don Harold | `Extreme close-up of [HAROLD]'s face in the dark, red light reflecting on his glasses, slow sinister smile, slow push-in.` | "…por eso los voy a vigilar cada cinco minutos." Luego, NARRADOR: "¿Trabajo moderno… con jefe antiguo? No se pierda el próximo capítulo." | **Continuará…** |

---

## Notas de dirección para este tramo

- **El brillo de Daniel es el termómetro emocional de toda la película.** Sube cuando lo escuchan (1.02, 1.11, 2.11) y baja cuando lo aplastan (1.12, 1.21). En el capítulo 5 se apaga del todo; es la imagen literal de "apagar la luz de los colaboradores más talentosos" (sección 5.4.1 del artículo).
- **"Biche" y "madurar"** vuelven en el capítulo 7, cuando el que resulta no haber madurado es Don Harold: madurez digital y madurez de liderazgo.
- **Frugle y Netfrux** son nombres inventados a propósito. El artículo menciona empresas reales; en pantalla es más seguro y más gracioso parodiarlas.
- **Filas que más se prestan para fallar:** 1.12 y 1.22 (dos personajes en el mismo plano) y 1.26 (primerísimo plano de la mano). Si no salen en tres intentos, 1.12 y 1.22 se resuelven con dos planos separados.
