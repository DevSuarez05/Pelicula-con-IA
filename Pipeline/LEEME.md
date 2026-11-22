# Pipeline · Fase 1 (prueba, versión 2)

## Para ver

| Archivo | Qué es |
|---|---|
| `prueba/PRUEBA-FASE-1.mp4` | Los tres clips seguidos: 1.07, 1.20 y 1.26 |
| `prueba/MUESTRARIO-VOCES-HOMBRES.mp3` | 20 voces masculinas actuando la línea de 1.07; cada una dice primero su número y su nombre |
| `prueba/MUESTRARIO-VOCES-MUJERES.mp3` | 17 voces femeninas actuando la línea de Valentina (1.19) |

Para cambiar una voz, díganle a Claude, por ejemplo: "Don Harold = voz 8, narrador = voz 3".

## Probar la animación de la cara en Colab

Hay dos cuadernos. Prueben primero SadTalker, porque no hay que grabar nada.

### A. SadTalker: imagen + audio (`colab/sadtalker.ipynb`)

1. Entren a **colab.research.google.com** con su cuenta de Google, vayan a **Archivo → Subir cuaderno** y elijan `Pipeline/colab/sadtalker.ipynb`.
2. Vayan a **Entorno de ejecución → Cambiar tipo de entorno → GPU T4 → Guardar** y luego a **Ejecutar todo**.
3. Cuando aparezca **Elegir archivos**, suban **`Pipeline/colab/entrada.zip`**. Contiene:
   - `1.20.png`: la imagen original de Don Harold, para el confesionario.
   - `1.20.wav`: su voz actuada, "¿Yo? ¿Improvisar? Por favor…".
   - `1.07.png`: Don Harold recortado sobre fondo magenta. El magenta se quita después y lo pongo en la sala de juntas.
   - `1.07.wav`: su voz actuada, "¡Señores! Frugle lo hace…".
4. Por cada fila salen dos versiones: `-still` (cabeza quieta) y `-vivo` (más movimiento de cabeza). Al final se descarga **`salida.zip`**. Pónganlo en `Pipeline/colab/` y avísenle a Claude: escojo la mejor versión y la monto en el clip.

### B. LivePortrait: imagen + video actuado por ustedes (`colab/liveportrait.ipynb`)

Es la opción más expresiva: Don Harold hace exactamente los gestos de quien actúe y la voz puede ser la de ustedes.

1. **Graben** con el celular cada línea en un video aparte, con el nombre de su fila: `1.20.mp4` y `1.07.mp4`.
   - Celular en horizontal y apoyado, la cara de frente a unos 50 cm, buena luz y fondo liso.
   - Un segundo con la cara neutra y la boca cerrada. Después digan la línea exagerando como en telenovela.
2. Suban el cuaderno igual que el anterior, con GPU T4, y denle **Ejecutar todo**.
3. Primero suban **`entrada.zip`** y después sus dos videos.
4. Pongan **`salida.zip`** en `Pipeline/colab/` y avísenle a Claude.

**Ninguno de los dos cuadernos se ha probado en Colab**, porque este PC no tiene GPU. Si una celda falla, copien el error completo y péguenlo en el chat.

## Herramientas (para Claude)

| Archivo | Qué hace |
|---|---|
| `voces.json` | Voz fija y ajuste base de cada personaje |
| `actuar.py` + `actuaciones/*.json` | Voz actuada frase por frase: tono, velocidad, volumen y pausa en milisegundos. Escribe un `.json` con el tiempo de cada frase. edge-tts no acepta SSML propio, así que este es el reemplazo |
| `muestrario.py` | Genera los muestrarios de voces |
| `sonido.py` | Música y efectos sintetizados en el PC, sin licencias: tensión, comedia, confesionario, golpes, latido, barridos de aire. Mezcla con la voz y baja la música cuando alguien habla |
| `camara.py` | Motor de cámara: curvas de aceleración, golpes de zoom con desenfoque de movimiento, giros, cámara en mano, paralaje y respiración |
| `clips_prueba.py` | Arma 1.07, 1.20 y 1.26. Si existe `colab/salida/FILA.mp4`, usa la cara animada en lugar de la imagen fija |
| `recortar.py` | Recorta a un personaje de su imagen original |
| `colab/crear_cuaderno.py` | Genera los dos cuadernos y `entrada.zip` |
