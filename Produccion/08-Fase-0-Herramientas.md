# Corazón de Pulpa · Fase 0: herramientas y plan de horas

El objetivo es producir la película sin ChatGPT, HeyGen ni Runway de pago, con herramientas gratuitas y sin marca de agua, conservando a los personajes de las imágenes originales. Este documento reemplaza la parte de herramientas de `06-Version-Sustentacion.md`. Las prioridades y los identificadores de fila siguen igual.

## 1. Lo que encontré en el PC

| Revisión | Resultado | Consecuencia |
|---|---|---|
| Tarjeta gráfica | AMD Radeon integrada, sin NVIDIA | La IA que anima caras no corre en este PC. Va en Google Colab, que presta GPU gratis |
| RAM | 15 GB | Suficiente para recortar personajes, generar voces y montar con ffmpeg |
| Python 3.14 y pip | Instalados | Probé la instalación en seco: `rembg` y `edge-tts` tienen paquetes listos para esta versión |
| ffmpeg | Instalado y probado | Hace todo el montaje |
| Imágenes originales | 4 PNG de 1312×1199 | Alcanzan para 1080p. Las caras tienen rasgos humanos con piel de fruta, lo que facilita que los detectores de cara las reconozcan |

## 2. Cómo se hace cada tipo de fila

| Método | Para qué filas | Con qué | Quién |
|---|---|---|---|
| **Cara que habla** | Un personaje diciendo su línea: confesionarios y planos de un personaje | Voz con `edge-tts` → SadTalker en Colab anima ojos, cabeza y boca desde la imagen del personaje. Si falla con las caras de fruta, se usa Wav2Lip | Yo preparo el cuaderno y los audios. Ustedes lo ejecutan en Colab |
| **Composición** | El personaje en otra locación (sala de juntas, planta, oficina de Harold) | `rembg` recorta al personaje de su imagen original y lo pongo sobre el plano de la locación. Después pasa por "cara que habla" si tiene diálogo | Yo |
| **Imagen con movimiento** | Narrador, planos sin diálogo, escenas de acción y de dos personajes | Imagen fija o composición con zoom, paneo, temblor y luz, hecha con ffmpeg. Si hay diálogo, la voz va encima con subtítulo | Yo |
| **Gráfico** | Filas FIJA y GRAF, textos académicos, cabezote | ffmpeg con las tipografías y la paleta de la biblia visual | Yo |
| **Saltar** | Las 13 filas de `06-Version-Sustentacion.md` | — | — |

Las imágenes nuevas son solo lo que no existe: **Don Lulo**, **los planos de las locaciones** (sin personajes) y algo de **utilería**. Son unas 30 imágenes en lugar de 188, y como ninguna tiene que copiar la cara de un personaje existente, sirve cualquier generador gratuito.

## 3. Lo que necesito de ustedes

Cada punto espera su aprobación. No instalo nada ni creo cuentas sin un sí.

| # | Qué | Para qué | Costo y riesgo |
|---|---|---|---|
| 1 | **Permiso para instalar `rembg[cpu]` y `edge-tts`** con pip en tu PC | Recortar personajes y generar voces | Gratis, unos 300 MB con el modelo de recorte, que se descarga la primera vez. Se desinstala con pip |
| 2 | **Aceptar que el texto de los diálogos va al servicio de voz de Microsoft Edge** | Así funciona `edge-tts`. Solo se envía el texto del guion, ningún dato personal | Si no quieren, la alternativa es grabar las voces ustedes |
| 3 | **Una cuenta de Google por persona** (las que ya tienen) | Ejecutar en Colab el cuaderno que anima las caras. La GPU gratis tiene un límite diario por cuenta, así que el trabajo se reparte entre los tres | Gratis. Cada uno abre el cuaderno con su cuenta; yo no entro a ninguna |
| 4 | **Una cuenta de Microsoft** para Microsoft Designer o Bing Image Creator | Don Lulo y los planos de las locaciones | Gratis, con un número de imágenes rápidas por día. Antes de producir en serie, revisen que no ponga marca visible |
| 5 | **Las voces:** ¿sintéticas o grabadas por ustedes? | Las sintéticas son más rápidas; las grabadas suenan más humanas | Pueden mezclar: narrador grabado y personajes sintéticos |

**No hace falta ninguna extensión del navegador.**

## 4. Voces propuestas

Una voz fija por personaje. La lista exacta se confirma después de instalar `edge-tts`, porque Microsoft cambia las voces disponibles.

| Personaje | Voz `edge-tts` | Ajuste |
|---|---|---|
| Don Harold | es-CO-GonzaloNeural | Tono más grave, un poco más lento |
| Valentina | es-CO-SalomeNeural | Natural |
| Daniel | Voz masculina joven latinoamericana (por ejemplo es-MX-JorgeNeural) | Un poco más agudo |
| Prof. Carlos Mario | Voz masculina madura distinta (por ejemplo es-US-AlonsoNeural) | Lento y pausado |
| Don Lulo | Otra voz masculina regional (por ejemplo es-VE-SebastianNeural) | — |
| Narrador | Voz grabada por el equipo, o una sintética con tono de telenovela | Lento |

## 5. Plan de horas

| Bloque | Qué se hace | Horas de ustedes | Horas de PC y Colab |
|---|---|---|---|
| **Martes 17, tarde** | Instalación (10 min). **Fase 1:** yo armo 1.20, 1.07 y 1.26 y el cuaderno de Colab; ustedes ejecutan la prueba de cara en Colab. Ustedes aprueban o ajustan | 1 h | 2 h |
| **Martes 17, noche** | Don Lulo y unos 20 planos de locación en el generador gratuito, repartidos entre los tres. **Fase 2:** actualizo `06` y la hoja de seguimiento | 2 h por persona | 1 h |
| **Miércoles 18** | Genero las ~150 voces. Colab anima las caras: capítulos 1 a 4 en la cuenta 1, 5 a 8 en la 2, finales y comerciales en la 3. Yo compongo y monto los capítulos 1 a 4 | 2 a 3 h por persona (casi todo esperar) | 6 a 8 h |
| **Jueves 19, mañana** | Capítulos 5 a 8, finales y créditos. Prioridad 2 hasta mediodía; lo que no alcance va como imagen con movimiento | 2 h por persona revisando | 4 h |
| **Jueves 19, tarde** | **Fase 4:** prueba completa en la consola, arreglos y respaldo. **Lista antes de las 6 p. m.** | 2 h | 2 h |
| **Jueves 19, noche** | Ensayo general | — | — |

**El riesgo principal** es que SadTalker y Wav2Lip están entrenados con caras humanas y pueden deformar las caras de fruta. Por eso la fase 1 empieza por ahí. Si fallan:

- Las caras se animan solo con parpadeo y movimiento suave de cabeza, sin boca.
- La voz queda encima con subtítulo, como un doblaje de telenovela.

La película se puede hacer igual, solo cambia cuánta vida tienen las caras.
