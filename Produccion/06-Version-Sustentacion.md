# Corazón de Pulpa · Versión de sustentación

Plan para tener la función lista el **viernes 20 de noviembre de 2026**. Cada una de las 265 filas del guion queda asignada a una herramienta y a una prioridad. Los identificadores, la consola, el respaldo y el formato (1920×1080, 24 fps, audio estéreo) no cambian.

La hoja de seguimiento para repartir y marcar el trabajo está en `06-Seguimiento.csv` (se abre en Excel o Google Sheets).

## 1. Resumen

| Herramienta | Prioridad 1 | Prioridad 2 | Total |
|---|---|---|---|
| **HeyGen** (un personaje hablándole a cámara) | 84 | 49 | 133 |
| **Runway** (movimiento, dos personajes o momentos clave sin diálogo) | 34 | 21 | 55 |
| **Edición** (imagen fija con zoom, gráficos; no gasta créditos) | 45 | 13 | 58 |
| **Montaje** (reusos e inserción de clips ya hechos) | — | — | 6 |
| **Saltar** (no se produce) | — | — | 13 |
| **Clips que hay que generar** | **118** | **70** | **188** |

- **Prioridad 1** es lo mínimo para que la función tenga sentido: las reacciones de cada votación, las filas que llevan texto académico en pantalla, el capítulo 6 completo, los dos finales y el cierre de la Piña.
- **Prioridad 2** se hace solo si sobra tiempo. Si una fila de prioridad 2 no alcanza, se monta su fotograma inicial con zoom lento y, si tiene diálogo, la voz sola (el audio de HeyGen o la misma voz grabada). La película no pierde ninguna escena; solo pierde movimiento.
- **Saltar** son las 9 filas marcadas con ✂ y las 4 tomas falsas de los créditos. La película queda en unos 32 minutos, más las votaciones.

## 2. Reglas que se usaron

| Si la fila… | Va a |
|---|---|
| Es un confesionario (personaje en su escritorio mirando a cámara) | **HeyGen** con la imagen original de `Imagenes/`. No necesita fotograma |
| Tiene un solo personaje que habla, sin caminar ni manipular objetos | **HeyGen** con el fotograma inicial que hace ChatGPT |
| Tiene dos personajes en cuadro, alguien camina o entra, o hay mucha gente | **Runway** con el fotograma inicial. Si hay diálogo, se monta la voz en edición |
| Es del narrador y no es un momento clave | **Edición**: fotograma inicial con zoom lento y la voz del narrador encima |
| Es del narrador y es un momento clave (prólogo, dedo sobre ENTER, puertas de los finales, planos finales) | **Runway** |
| Es FIJA o GRAF en el guion | **Edición**, como ya decía el guion |
| El cabezote (C-01 a C-04) | **Edición**: las 4 imágenes originales con zoom sobre la canción |

**Las voces.** HeyGen da la voz con la boca sincronizada. Para que cada personaje suene igual en toda la película, usen la misma voz de HeyGen también en las filas de Runway: generen ahí el audio de la línea y móntenlo sobre el clip de Runway en la edición.

**Todas las filas de Runway y de Edición necesitan fotograma inicial de ChatGPT**, igual que las de HeyGen que no son confesionario. Los confesionarios son los únicos que salen directo de las imágenes originales.

## 3. Calendario

| Día | Mañana | Tarde | Noche |
|---|---|---|---|
| **Martes 17** | Prueba HeyGen contra Runway (filas 1.20, 1.07 y 1.26) | Fijar una voz por personaje. Empezar los confesionarios de prioridad 1 en HeyGen | ChatGPT: Don Lulo y fotogramas de los capítulos 1 a 4 |
| **Miércoles 18** | Prioridad 1 de los capítulos 1 a 4 | Prioridad 1 de los capítulos 5 a 8 y finales | Editar capítulos 1 a 4 y exportar sus videos con los nombres de `Consola/LEEME.md` |
| **Jueves 19** | Prioridad 2, lo que alcance hasta mediodía | Editar capítulos 5 a 8, finales y créditos. Exportar todo. Armar el respaldo | **Ensayo general** completo con la consola |
| **Viernes 20** | Ensayo técnico en el salón, si dejan entrar antes. Sustentación | | |

**Corte duro: jueves a mediodía se deja de generar.** Lo que no esté, va como fotograma con zoom. Un ensayo sin película completa vale más que una película completa sin ensayo.

**Reparto sugerido** para tres personas, por capítulos, para que cada quien edite lo que generó:

| Persona | Genera | Edita |
|---|---|---|
| 1 | HeyGen de prólogo a capítulo 4 | Capítulos 1 a 4 |
| 2 | HeyGen de capítulo 5 a créditos, comerciales | Capítulos 5 a 8, finales, créditos, comerciales |
| 3 | Todo Runway; recibe los fotogramas de ChatGPT | Las filas de Edición (zoom sobre fotograma) y el respaldo |

## 4. Fila por fila

Columnas: **Fila** (identificador del guion) · **Qué se ve** · **Quién** · **Herramienta** · **P** (prioridad) · **Nota**.

### PRÓLOGO · "Lo tenía todo" (0:50)

1 HeyGen · 3 Runway · 1 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| P-01 | Fiesta corporativa helada. Frutas de traje gris idéntico, quietas, cada una… | Narrador | **Runway** | 1 | Momento clave sin diálogo de personaje |
| P-02 | Una fruta aplaude una sola vez. Nadie la sigue. | Narrador | **Runway** | 2 | Momento clave sin diálogo de personaje. Si no alcanza: fotograma con zoom |
| P-03 | Daniel en un rincón, sin brillo, con un sobre blanco en la mano. | Narrador | **Runway** | 2 | Momento clave sin diálogo de personaje. Si no alcanza: fotograma con zoom |
| P-04 | Don Harold brinda solo. Silencio. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| P-05 | Los cuatro clips anteriores en reversa acelerada, con sonido de cinta. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |

### CABEZOTE · Canción "Corazón de Pulpa" (0:40)

0 HeyGen · 0 Runway · 5 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| C-01 | Don Harold gira hacia cámara y se quita las gafas. | Don Harold | **Edición** | 2 | Imagen original del personaje con zoom, sobre la canción |
| C-02 | Valentina se voltea con el pelo al viento. | Valentina | **Edición** | 2 | Imagen original del personaje con zoom, sobre la canción |
| C-03 | Daniel levanta la mirada y brilla. | Daniel | **Edición** | 2 | Imagen original del personaje con zoom, sobre la canción |
| C-04 | Silueta misteriosa con corona de hojas, a contraluz. No se le ve la cara. | Prof. Carlos Mario | **Edición** | 2 | Imagen original del personaje con zoom, sobre la canción |
| C-05 | Título sobre fondo de pulpa de frutas. | — | **Edición** | 2 | Gráfico o montaje en el editor |

### CAPÍTULO 1 · "El atajo" (3:45)

15 HeyGen · 9 Runway · 2 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 1.01 | Fachada de la torre FrutiTech al amanecer, montañas al fondo. | Narrador | **Edición** | 1 | Imagen fija con zoom lento |
| 1.02 | Daniel entra al lobby radiante, con una libreta llena de notas adhesivas. | Daniel | **Runway** | 1 | Movimiento |
| 1.03 | Valentina revisa su tableta en la oficina abierta. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 1.04 | Se abren las puertas de golpe. Don Harold entra con maleta llena de… | Don Harold | **Runway** | 1 | Movimiento |
| 1.05 | Valentina cierra los ojos y respira hondo. | Valentina | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 1.06 | Confesionario de Daniel, sentado en su escritorio mirando a cámara. (Usar su… | Daniel | **HeyGen** | 2 | Confesionario: imagen original. Si no alcanza: fotograma con zoom y la voz sola |
| 1.07 | Sala de juntas. Don Harold a la cabeza de la mesa, control remoto en mano. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 1.08 | Don Harold camina orgulloso frente a la ventana. | Don Harold | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 1.09 | Valentina levanta la mano con calma. | Valentina | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 1.10 | Don Harold, desconcertado, se acomoda las gafas. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 1.11 | Daniel abre su libreta, brillando. | Daniel | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 1.12 | Don Harold le da palmaditas en la hoja de la cabeza. El brillo de Daniel… | Don Harold | **Runway** | 2 | Dos personajes en cuadro. Si no alcanza: fotograma con zoom |
| 1.13 | Valentina se pone de pie. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 1.14 | Don Harold saca una memoria USB como si fuera una reliquia. Luz dorada. | Don Harold | **Runway** | 1 | Movimiento |
| 1.15 | Daniel lee el archivo en el portátil, confundido. | Daniel | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 1.16 | Don Harold lo resuelve con un gesto de la mano. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 1.17 | Daniel sigue leyendo. | Daniel | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 1.18 | Don Harold lo piensa tres segundos largos y asiente. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 1.19 | Confesionario de Valentina. (Usar su imagen original.) | Valentina | **HeyGen** | 1 | Confesionario: imagen original |
| 1.20 | Confesionario de Don Harold. (Usar su imagen original.) | Don Harold | **HeyGen** | 2 | Confesionario: imagen original. Si no alcanza: fotograma con zoom y la voz sola |
| 1.21 | Pasillo. Daniel camina apagado. | Daniel | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 1.22 | Valentina le pone la mano en el hombro. El brillo vuelve un poco. | Valentina | **Runway** | 2 | Dos personajes en cuadro. Si no alcanza: fotograma con zoom |
| 1.23 | Oficina de Don Harold al atardecer. Mira una foto enmarcada de un campus… | Narrador | **Edición** | 1 | Imagen fija con zoom lento |
| 1.24 | Don Harold frente al portátil, hablando solo. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 1.25 | Valentina entra corriendo. | Valentina | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 1.26 | Primerísimo plano del dedo de aguacate temblando sobre la tecla ENTER. Zoom… | Narrador | **Runway** | 1 | Momento clave sin diálogo de personaje |

### PAUSA INTERACTIVA 1 (60 segundos)

2 HeyGen · 0 Runway · 1 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 1.27-A | Si gana DUPLICAR. Don Harold mira a cámara, feliz, y oprime la tecla. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 1.27-B | Si gana ADAPTAR. Don Harold baja las gafas, mira a cámara, y oprime la tecla… | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 1.28 | El correo llega a toda la oficina. Vibran los celulares. Caras de desconcierto. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |

### CAPÍTULO 2 · "Lo que no se negocia" (3:00)

12 HeyGen · 1 Runway · 2 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 2.00 | Resumen con los clips 1.07, 1.14 y 1.26. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| 2.01 | Mañana siguiente. Frutas cuchicheando junto a la cafetera, mirando el celular. | Narrador | **Edición** | 2 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 2.02 | Don Harold cruza la oficina eufórico, con su pocillo de aguacate. | Don Harold | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 2.03 | Sala de juntas. Don Harold se frota las manos. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 2.04 | Don Harold enumera con los dedos, cada vez más emocionado. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 2.05 | Valentina deja la tableta sobre la mesa, muy despacio. | Valentina | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 2.06 | Daniel levanta la mano con timidez. | Daniel | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 2.07 | Valentina se levanta. Aparece un holograma dividido en dos columnas vacías.… | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 2.08 | Valentina señala la columna derecha. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 2.09 | Don Harold se rasca el tallito de la cabeza. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 2.10 | Valentina toma una botella de jugo de la mesa y la muestra. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 2.11 | A Daniel se le prende el brillo. | Daniel | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 2.12 | Valentina mira a Don Harold de frente. | Valentina | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 2.13 | Don Harold se lleva la mano al pecho. Zoom de telenovela. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 2.14 | Cambian las luces a concurso de televisión. Valentina con tarjetas de… | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |

### PAUSA INTERACTIVA 2 · Ráfaga "¿Se cumple o se diseña?" (unos 90 segundos)

8 HeyGen · 0 Runway · 0 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 2.15 | Pago de nómina y seguridad social | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 2.16 | Programa de reconocimiento a colaboradores | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 2.17 | Protocolos de seguridad y salud en el trabajo | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 2.18 | Modelo de trabajo híbrido | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 2.19 | Confesionario de Valentina. (Usar su imagen original.) | Valentina | **HeyGen** | 2 | Confesionario: imagen original. Si no alcanza: fotograma con zoom y la voz sola |
| 2.20 | Don Harold en su oficina, enfurruñado. De pronto se anima. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 2.21 | Don Harold abre una caja negra con un ojo brillante en la tapa. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 2.22 | Primerísimo plano. La luz roja se refleja en las gafas. Sonrisa siniestra. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |

### CAPÍTULO 3 · "Moderno de cáscara" (4:00)

17 HeyGen · 4 Runway · 7 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 3.00 | Resumen con los clips 2.07, 2.20 y 2.22. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| 3.01 | Torre FrutiTech un lunes temprano, con un pendón gigante en la fachada. | Narrador | **Edición** | 1 | Imagen fija con zoom lento |
| 3.02 | El lobby transformado de la noche a la mañana: mesa de ping-pong, puffs de… | Don Harold | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 3.03 | Valentina lee un letrero pegado en la mesa de ping-pong. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.04 | Don Harold acaricia la mesa con orgullo. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 3.05 | Don Harold abre la cápsula de siesta y saca de adentro una carpeta gruesa. | Don Harold | **Runway** | 1 | Movimiento |
| 3.06 | Confesionario de Valentina. (Usar su imagen original.) | Valentina | **HeyGen** | 1 | Confesionario: imagen original |
| 3.07 | Confesionario de Don Harold. (Usar su imagen original.) | Don Harold | **HeyGen** | 1 | Confesionario: imagen original |
| 3.08 ✂ | Don Harold en su oficina, deslizando el dedo en el celular, cada vez más… | Don Harold | **Saltar** | — | Prescindible (✂) |
| 3.09 | Martes. Daniel en su apartamento, radiante, con tinto y la libreta abierta. | Daniel | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.10 | En el portátil salta una ventana con un ojo rojo. Daniel se asusta. | Voz del software | **Runway** | 1 | Movimiento |
| 3.11 | Daniel mueve el mouse como loco. | Daniel | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 3.12 | Videollamada: Don Harold muy cerca de su cámara web. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 3.13 | Daniel le muestra la libreta a la cámara. | Daniel | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 3.14 | Don Harold en la videollamada, golpeando el escritorio. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.15 ✂ | Daniel escribe en la libreta y al mismo tiempo mueve el mouse con el pie,… | Narrador | **Saltar** | — | Prescindible (✂) |
| 3.16 | Don Harold frente a una pared de pantallas con decenas de cámaras de empleados… | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.17 | Miércoles, día de oficina. Don Harold presenta un formato impreso, orgulloso. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.18 | Valentina, incrédula, lo mira de frente. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.19 | Don Harold, ofendido, se pone la mano en el pecho. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 3.20 | Valentina se levanta. Holograma partido: a un lado una casa con portátil; al… | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.21 | Daniel, de nuevo en casa. Las notas adhesivas se caen de la nevera una por una. | Narrador | **Edición** | 2 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 3.22 | Confesionario de Daniel, apagado. (Usar su imagen original; en el prompt pedir… | Daniel | **HeyGen** | 1 | Confesionario: imagen original |
| 3.23 | Biblioteca en penumbra. La mano de piña escribe en la libreta. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 3.24 | Sala de juntas. Don Harold proyecta una gráfica que sube. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.25 | Valentina le contesta sin levantar la voz. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.26 | Valentina pone un documento sobre la mesa, junto al contrato del software. | Valentina | **Runway** | 2 | Dos personajes en cuadro. Si no alcanza: fotograma con zoom |
| 3.27 | Primerísimo plano de un bolígrafo de aguacate sobre la línea de firma. Zoom… | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |

### PAUSA INTERACTIVA 3 (60 segundos)

2 HeyGen · 0 Runway · 1 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 3.28-A | Si gana DUPLICAR. Don Harold firma feliz. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.28-B | Si gana ADAPTAR. Don Harold mete la propuesta de Valentina en un cajón y firma. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 3.29 | Oficina en silencio. Sobre cada escritorio, una pequeña cámara con luz roja… | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |

### COMERCIALES 1 · "Isomorfina Forte" (0:40)

0 HeyGen · 1 Runway · 4 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| CM1-01 | Don Harold angustiado, en blanco y negro, mirando el celular. | Narrador | **Edición** | 2 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| CM1-02 | Se toma una pastilla verde gigante y todo se llena de color y brillos. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| CM1-03 | Don Harold baila feliz frente a una mesa de ping-pong. | Don Harold | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| CM1-04 | Letra pequeña que sube a toda velocidad. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| CM1-05 | Imagen original de Valentina, zoom lento. | Narrador | **Edición** | 1 | Imagen fija con zoom lento |

### CAPÍTULO 4 · "Los de la torre y los de la planta" (3:30)

11 HeyGen · 5 Runway · 9 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 4.00 | Resumen con los clips 3.14, 3.20 y 3.27. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| 4.01 | La planta de FrutiTech de madrugada. Camiones llenos de fruta en la entrada. | Narrador | **Edición** | 1 | Imagen fija con zoom lento |
| 4.02 | Don Lulo revisa la fruta en la banda transportadora, orgulloso. | Don Lulo | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 4.03 | Vibran los celulares de los operarios. Don Lulo lee el suyo. | Don Lulo | **Runway** | 1 | Movimiento |
| 4.04 | Confesionario de Don Lulo junto a la banda. | Don Lulo | **HeyGen** | 2 | Confesionario: imagen original. Si no alcanza: fotograma con zoom y la voz sola |
| 4.05 | Viernes en la torre: oficina vacía, luces apagadas, una silla girando sola. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 4.06 | Pantalla dividida con dos chats de WhatsApp. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| 4.07 | Daniel llega a la planta con malla en el pelo (encima de su hoja de mango) y… | Daniel | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 4.08 | Don Lulo, sorprendido, se limpia las manos en el delantal. | Don Lulo | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 4.09 | Caminan juntos a lo largo de la banda. Don Lulo cuenta con los dedos. | Don Lulo | **Runway** | 1 | Dos personajes en cuadro |
| 4.10 | Daniel deja de escribir. Su brillo sube un poco. | Daniel | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 4.11 | Daniel entra a la oficina de Don Harold con la libreta llena. | Daniel | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 4.12 | Don Harold levanta la mano sin mirarlo. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 4.13 | En la planta, Don Harold descubre su solución: la pantalla grande sobre la… | Don Harold | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 4.14 | Don Lulo mira la playa, inexpresivo. Se oye una gaviota. | Don Lulo | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 4.15 ✂ | Don Harold sigue, entusiasmado. | Don Harold | **Saltar** | — | Prescindible (✂) |
| 4.16 | Valentina llega con malla en el pelo sobre su corona de hojas. | Valentina | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 4.17 | Valentina proyecta un holograma: una balanza. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 4.18 | Don Harold, acorralado, levanta los brazos. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 4.19 | Valentina, con calma total. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 4.20 | Fin del turno. Don Lulo se quita despacio la gorra con el logo de FrutiTech,… | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 4.21 ✂ | Confesionario de Daniel, apagado. | Daniel | **Saltar** | — | Prescindible (✂) |
| 4.22 | La mano de piña escribe en la libreta. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 4.23 | Sala de juntas. Valentina pone la libreta de Daniel frente a Don Harold. | Valentina | **Runway** | 2 | Dos personajes en cuadro. Si no alcanza: fotograma con zoom |
| 4.24 | Primerísimo plano: los ojos de Don Harold van de la libreta a la pantalla con… | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |

### PAUSA INTERACTIVA 4 (60 segundos)

2 HeyGen · 0 Runway · 1 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 4.25-A | Si gana DUPLICAR. Don Harold, feliz, sube el volumen con un control remoto. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 4.25-B | Si gana ADAPTAR. Don Harold cierra la libreta de Daniel y la devuelve. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 4.26 | La planta trabaja en silencio bajo la pantalla de la playa. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |

### CAPÍTULO 5 · "La fiesta sin alma" (4:00)

12 HeyGen · 1 Runway · 7 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 5.00 | Resumen con los clips 4.13, 4.18 y 4.20. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| 5.01 | La ciudad de noche con las primeras luces de Navidad. | Narrador | **Edición** | 2 | Imagen fija con zoom lento |
| 5.02 | Sala de juntas llena de cajas. Don Harold saca unas gafas de realidad virtual. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 5.03 | Valentina, con la tableta, hace tres preguntas contando con los dedos. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 5.04 | Don Harold se pone las gafas de realidad virtual. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 5.05 | Oficina: todos con gafas de realidad virtual, congelados a mitad de gesto. Un… | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 5.06 | Daniel en casa, se levanta las gafas, resignado. | Daniel | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 5.07 | Don Harold se arranca las gafas y grita por toda la oficina. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 5.08 ✂ | Don Harold recorre los escritorios con un cronómetro. | Narrador | **Saltar** | — | Prescindible (✂) |
| 5.09 | Valentina muestra la tableta con números en rojo. | Valentina | **Runway** | 1 | Dos personajes en cuadro |
| 5.10 | A Don Harold se le resbalan las gafas por la nariz. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 5.11 | Recuerdo en sepia: torre y planta revueltas alrededor de una paila de… | Narrador | **Edición** | 1 | Imagen fija con zoom lento |
| 5.12 | Don Harold se recompone y pone cara de visionario. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 5.13 | Don Harold enumera con desprecio. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 5.14 | En la planta, Don Lulo recibe la noticia por teléfono, con la paila y la… | Don Lulo | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 5.15 | Oficina de Don Harold. Valentina, conmovida, hace el último intento. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 5.16 | Don Harold gira la silla hacia la ventana y le da la espalda. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 5.17 | La mano de piña escribe en la libreta y la cierra. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 5.18 | Confesionario de Valentina, triste. | Valentina | **HeyGen** | 2 | Confesionario: imagen original. Si no alcanza: fotograma con zoom y la voz sola |
| 5.19 | Sobre el escritorio de Don Harold, dos invitaciones: una gris y elegante; otra… | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |

### PAUSA INTERACTIVA 5 (60 segundos)

3 HeyGen · 1 Runway · 8 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 5.20-A | Si gana DUPLICAR. Don Harold toma la tarjeta gris. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 5.20-B | Si gana ADAPTAR. Don Harold huele la tarjeta del buñuelo con nostalgia, la… | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 5.21 | De noche, en su apartamento, Daniel abre un documento en blanco. | Narrador | **Edición** | 2 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 5.22 | Las manos de Daniel doblan una carta y la meten en un sobre blanco. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 5.23 | Confesionario de Daniel, más apagado que nunca. | Daniel | **HeyGen** | 1 | Confesionario: imagen original |
| 5.24 | Clip P-01 del prólogo. | Narrador | **Montaje** | — | Reusa el clip del prólogo |
| 5.25 | Clip P-02 del prólogo. | Narrador | **Montaje** | — | Reusa el clip del prólogo |
| 5.26 | Don Lulo llega a la fiesta con su mejor camisa y una bolsita de papel con… | Don Lulo | **Edición** | 2 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 5.27 | Clip P-03 del prólogo: Daniel en el rincón con el sobre. | Narrador | **Montaje** | — | Reusa el clip del prólogo |
| 5.28 | Clip P-04 del prólogo: Don Harold brinda solo. | Don Harold | **Montaje** | — | Reusa el clip del prólogo |
| 5.29 | Daniel cruza la fiesta en cámara lenta hacia Don Harold y le extiende el… | Daniel | **Edición** | 2 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 5.30 | Se apagan las luces. Un solo reflector. Una mano de piña entra al cuadro y… | Prof. Carlos Mario… | **Runway** | 1 | Movimiento |

### COMERCIALES 2 · "Plantillas Don Copión" (0:40)

2 HeyGen · 1 Runway · 2 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| CM2-01 | Don Harold con bigote postizo, en un set de infomercial. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| CM2-02 | Mete una memoria USB en un portátil y cae confeti. | Don Harold | **Runway** | 1 | Movimiento |
| CM2-03 | Muestra tres documentos idénticos, lado a lado. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| CM2-04 | Número de teléfono parpadeante y letra pequeña. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| CM2-05 | Pantalla negra, letras blancas. Corona de piña en silueta al fondo. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |

### CAPÍTULO 6 · "La Piña ha hablado" (4:00)

14 HeyGen · 2 Runway · 4 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 6.00 | Resumen con los clips 5.15, 5.23 y 5.30. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| 6.01 | La revelación. La cámara sube despacio desde la mano de piña, que sostiene la… | Prof. Carlos Mario | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 6.02 | Don Harold, desconcertado y ofendido. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.03 | La Piña levanta la libreta de cuero. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.04 ✂ | Don Harold cambia de actitud de golpe y se acomoda las gafas, interesado. | Don Harold | **Saltar** | — | Prescindible (✂) |
| 6.05 ✂ | La Piña, sin inmutarse. | Prof. Carlos Mario | **Saltar** | — | Prescindible (✂) |
| 6.06 | La Piña abre la libreta y pasa las páginas. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.07 | Se encienden las luces. El salón de la gala se convierte en un aula: aparece… | Prof. Carlos Mario | **Runway** | 1 | Movimiento |
| 6.08 | Don Harold baja la mirada. Por primera vez, es honesto. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.09 | La Piña asiente con amabilidad. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.10 | La Piña se acerca a Don Harold. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.11 | En el holograma aparece una fruta con tres grietas, que se iluminan una a una. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.12 | Valentina levanta la mano. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.13 | La Piña niega con la cabeza. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.14 | En el holograma aparecen cuatro bloques dorados. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.15 | La Piña toca cada bloque y se ilumina. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.16 | Daniel, todavía apagado, levanta la mano con curiosidad. | Daniel | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.17 | La Piña se voltea hacia Daniel con calidez. Un destello casi imperceptible… | Prof. Carlos Mario | **Runway** | 1 | Dos personajes en cuadro |
| 6.18 | La Piña mira directo a la cámara. Rompe la cuarta pared. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.19 | La Piña, a cámara, señala el holograma. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |

### PAUSA INTERACTIVA 6 · Prueba VRIO (unos 90 segundos)

7 HeyGen · 3 Runway · 0 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 6.20 | V · ¿Es valioso? | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.21 | R · ¿Es raro? | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.22 | I · ¿Es difícil de imitar? | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.23 | O · ¿FrutiTech está organizada para aprovecharlo? | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.24 | La Piña da el veredicto. Solo un bloque sigue encendido. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.25 | Don Harold se sienta despacio en una silla. Se mira en el reflejo de una… | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.26 | La Piña le pone la mano en el hombro. | Prof. Carlos Mario | **Runway** | 1 | Dos personajes en cuadro |
| 6.27 | La Piña, a cámara, solemne. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 6.28 | La Piña, a cámara, sonríe y enseña un grito nuevo. | Prof. Carlos Mario | **Runway** | 1 | Movimiento |
| 6.29 | La Piña señala un calendario de pared a Valentina y Daniel. | Prof. Carlos Mario | **Runway** | 1 | Dos personajes en cuadro |

### CAPÍTULO 7 · "Diagnóstico con alma" (4:00)

8 HeyGen · 5 Runway · 6 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 7.00 | Resumen con los clips 6.11, 6.24 y 6.27. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| 7.01 | Calendario de pared con el 16 de diciembre marcado. | Narrador | **Edición** | 1 | Imagen fija con zoom lento |
| 7.02 | Sala de juntas. Valentina frente a un tablero, con energía. Don Harold y… | Valentina | **Runway** | 1 | Dos personajes en cuadro |
| 7.03 | Valentina proyecta un holograma con tres columnas. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 7.04 | Don Harold levanta la mano con timidez. Se arrepiente a mitad de camino. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 7.05 | Daniel abre un portátil viejo y le sale una nube de polvo. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 7.06 | Valentina mira la tableta, que ahora brilla en verde. Sonríe. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 7.07 | Auditoría tres: Don Harold, sentado en una silla de estudiante demasiado… | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 7.08 | La Piña, junto al rotafolio, le responde con paciencia. | Prof. Carlos Mario | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 7.09 | Montaje: Daniel escuchando a la gente en la torre y en la planta. Su brillo… | Narrador | **Edición** | 2 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| 7.10 | Mesa de trabajo: gente de la torre y de la planta en la misma mesa. Don Lulo… | Don Lulo | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 7.11 ✂ | Don Lulo, con una propuesta. | Don Lulo | **Saltar** | — | Prescindible (✂) |
| 7.12 | Daniel, brillando, pega notas adhesivas en el tablero, agrupadas por equipo. | Daniel | **Runway** | 1 | Movimiento |
| 7.13 | Valentina con los resultados en la tableta. | Valentina | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 7.14 | Don Harold se dirige a Daniel, algo apenado. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 7.15 | Daniel saca la libreta de septiembre. Su brillo sube. | Daniel | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 7.16 | Confesionario de Don Harold. (Usar su imagen original.) | Don Harold | **HeyGen** | 1 | Confesionario: imagen original |
| 7.17 | Don Harold mira la caja del Ojo de Aguacate Pro sobre su escritorio. La Piña,… | Prof. Carlos Mario | **Runway** | 2 | Dos personajes en cuadro. Si no alcanza: fotograma con zoom |
| 7.18 | Valentina mira a cámara. | Valentina | **HeyGen** | 1 | Fotograma inicial de ChatGPT |

### PAUSA INTERACTIVA 7 · Tres decisiones (unos 2 minutos)

5 HeyGen · 6 Runway · 2 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 7.19-A | DUPLICAR. Don Harold mantiene el ojo, pero "suavizado". El brillo de Daniel… | Don Harold | **Runway** | 1 | Dos personajes en cuadro |
| 7.19-B | ADAPTAR. Don Harold desconecta el ojo y rompe el formato F-27. Lluvia de… | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 7.20-A | DUPLICAR. Don Lulo lee el correo, incrédulo. | Don Lulo | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| 7.20-B | ADAPTAR. Don Lulo lee una cartelera nueva en la planta. Se emociona. | Don Lulo | **Runway** | 1 | Movimiento |
| 7.21-A | DUPLICAR. Valentina suspira frente al tablero. | Valentina | **Runway** | 1 | Movimiento |
| 7.21-B | ADAPTAR. Daniel, brillando, presenta el esquema y le pregunta al salón. | Daniel | **Runway** | 1 | Movimiento |
| 7.22 | La torre FrutiTech de noche, con algunas ventanas encendidas. | Narrador | **Edición** | 1 | Imagen fija con zoom lento |
| 7.23 | Don Harold llega a la planta. Don Lulo está limpiando la paila vacía. | Don Harold | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 7.24 | Don Lulo deja de limpiar y lo mira, sorprendido. | Don Lulo | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 7.25 | Don Harold sonríe por primera vez sin pose. | Don Harold | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |
| 7.26 | Don Lulo pasa la mano por la paila, pensativo. | Don Lulo | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 7.27 | Confesionario del Prof. Carlos Mario. (Usar su imagen original.) | Prof. Carlos Mario | **HeyGen** | 1 | Confesionario: imagen original |
| 7.28 | Daniel, en su casa, saca del cajón el sobre blanco. Lo mira. No lo abre. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |

### Tronco común

1 HeyGen · 2 Runway · 3 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| 8.00 | Resumen con los clips 6.27, 7.17 y 7.28. | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| 8.01 | La planta al atardecer, con la puerta grande cerrada. | Narrador | **Edición** | 1 | Imagen fija con zoom lento |
| 8.02 | Don Harold camina hacia la planta, nervioso, con una caja de natilla en las… | Don Harold | **Runway** | 2 | Movimiento. Si no alcanza: fotograma con zoom |
| 8.03 | Valentina y Daniel en la puerta de la planta. Daniel toca el sobre en el… | Valentina | **Runway** | 2 | Dos personajes en cuadro. Si no alcanza: fotograma con zoom |
| 8.04 | Revelación de los indicadores finales. | Narrador / presentador | **Edición** | 1 | Gráfico o montaje en el editor |
| 8.05 | La Piña pone la mano en la manija de la puerta y mira a cámara. | Prof. Carlos Mario | **HeyGen** | 2 | Fotograma inicial de ChatGPT. Si no alcanza: fotograma con zoom y la voz sola |

### Cierre académico · COMPARTIDO por los dos finales

4 HeyGen · 0 Runway · 0 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| CON-01 | La Piña en su escritorio, a cámara. | Prof. Carlos Mario | **HeyGen** | 1 | Confesionario: imagen original |
| CON-02 | La Piña se inclina hacia la cámara. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| CON-03 | La Piña levanta cuatro dedos y los va bajando. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| CON-04 | La Piña se lleva la mano al pecho. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |

### FINAL A · "Con pulpa" (2:00)

3 HeyGen · 7 Runway · 2 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| FA-01 | Se abre la puerta: la planta llena de faroles, luces y gente. Torre y planta… | Narrador | **Runway** | 1 | Momento clave sin diálogo de personaje |
| FA-02 | Don Lulo, con la gorra de FrutiTech puesta otra vez, revuelve una paila… | Don Lulo | **Runway** | 1 | Movimiento |
| FA-03 | Don Lulo le da el primer buñuelo a Don Harold. Don Harold lo muerde y cierra… | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| FA-04 | Don Harold levanta el buñuelo como en un brindis. Esta vez todos le responden. | Don Harold | **Runway** | 1 | Movimiento |
| FA-05 | Pantalla dividida: a la izquierda, el brindis solitario de la gala (P-04); a… | Narrador | **Edición** | 1 | Gráfico o montaje en el editor |
| FA-06 | Daniel saca el sobre de la renuncia, lo abre y mete dos buñuelos adentro. Su… | Daniel | **Runway** | 1 | Movimiento |
| FA-07 | Valentina le choca la mano a Daniel. | Valentina | **Runway** | 1 | Dos personajes en cuadro |
| FA-08 | Confesionario de Don Harold, con un buñuelo en la mano. | Don Harold | **HeyGen** | 1 | Confesionario: imagen original |
| CON-01 a CON-04 | Cierre académico de la Piña (32 s). | Prof. Carlos Mario | **Montaje** | — | Se insertan los clips CON-01 a CON-04 |
| FA-09 | La Piña, de vuelta en la novena, frente al pesebre, con un buñuelo, a cámara. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| FA-10 | Don Lulo le pone una gorra de FrutiTech a Don Harold. | Don Lulo | **Runway** | 1 | Dos personajes en cuadro |
| FA-11 | Plano general final: toda la novena cantando, la cámara sube hasta los faroles. | Narrador | **Runway** | 1 | Momento clave sin diálogo de personaje |

### FINAL B · "Pura cáscara" (2:15)

4 HeyGen · 4 Runway · 6 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| FB-01 | Se abre la puerta: la planta casi a oscuras, sillas apiladas, una paila fría. | Narrador | **Runway** | 1 | Momento clave sin diálogo de personaje |
| FB-02 | Don Lulo, solo, sentado en una caja frente a la paila fría. Sin gorra. | Don Lulo | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| FB-03 | Don Harold, con un pasabocas gris en la mano, mira alrededor. | Don Harold | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| FB-04 | La Piña, a su lado. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| FB-05 | El lobby de FrutiTech un año después: blanco, gris, idéntico a cualquier otro. | Narrador | **Edición** | 1 | Imagen fija con zoom lento |
| FB-06 | Don Harold les da el recorrido a empleados nuevos, con el mismo discurso de… | Don Harold | **Runway** | 1 | Movimiento |
| FB-07 | Don Harold enmarca una página de revista. | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| FB-08 | Daniel brillando, presentando ideas en otra empresa, ante un equipo que lo… | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| FB-09 ✂ | Confesionario de Valentina, guardando sus cosas en una caja. | Valentina | **Saltar** | — | Prescindible (✂) |
| FB-10 | Don Lulo se jubila. Le entrega su gorra a Don Harold. | Don Lulo | **Runway** | 1 | Dos personajes en cuadro |
| FB-11 | De noche, Don Harold, solo en su oficina, mira la foto enmarcada de la novena… | Narrador | **Edición** | 1 | Narrador sobre el fotograma inicial con zoom (sin generar video) |
| CON-01 a CON-04 | Cierre académico de la Piña (32 s). | Prof. Carlos Mario | **Montaje** | — | Se insertan los clips CON-01 a CON-04 |
| FB-12 | La Piña cierra la libreta, a cámara. | Prof. Carlos Mario | **HeyGen** | 1 | Fotograma inicial de ChatGPT |
| FB-13 | Don Harold, solo en el lobby clonado, se come el pasabocas gris. | Narrador | **Runway** | 1 | Momento clave sin diálogo de personaje |

### Tomas falsas (32 s)

0 HeyGen · 0 Runway · 4 sin generar

| Fila | Qué se ve | Quién | Herramienta | P | Nota |
|---|---|---|---|---|---|
| CR-01 | Don Harold, con gafas de realidad virtual, camina directo contra la puerta de… | Don Harold | **Saltar** | — | Tomas falsas: los créditos quedan solo con texto |
| CR-02 | Valentina no aguanta la risa en plena escena. | Valentina | **Saltar** | — | Tomas falsas: los créditos quedan solo con texto |
| CR-03 | A Daniel se le cae la hoja de la cabeza en el tinto. | Daniel | **Saltar** | — | Tomas falsas: los créditos quedan solo con texto |
| CR-04 | La corona de la Piña tumba la lámpara de la biblioteca. | Prof. Carlos Mario | **Saltar** | — | Tomas falsas: los créditos quedan solo con texto |
