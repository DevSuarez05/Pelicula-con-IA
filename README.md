# Corazón de Pulpa: ¿Duplicar o Adaptar?

Frutinovela interactiva hecha con inteligencia artificial para la asignatura de Gerencia Estratégica del Talento Humano, Universidad Nacional de Colombia, Sede Manizales (2026).

FrutiTech copia el modelo de trabajo de su competidor ("¡Así lo hace Frugle!") y se va quedando *pura cáscara*. Durante la función el público vota: en el Acto 1 Don Harold no escucha; en el Acto 2 las decisiones del salón se ejecutan y definen el final: **"Con pulpa"** o **"Pura cáscara"**.

Basada en el artículo *Benchmarking en gestión humana* (isomorfismo institucional, teoría de recursos y capacidades, VRIO y trabajo híbrido).

## Equipo

- Daniel Andrés Suárez Ramírez (creador de la trama)
- Harold Yamid Arango
- Valentina Constain

Profesor: Carlos Mario Tabares.

## Contenido del repositorio

| Carpeta | Qué hay |
|---|---|
| `Consola/` | La consola de la función (`consola-v2.html`, con aplausómetro; `consola.html`, versión original), fotos de las reacciones, plan B y su `LEEME.md` |
| `Produccion/` | Guiones, guion técnico y los prompts de imagen (ChatGPT) y de video con voz (Grok) |
| `Imagenes/` | Imágenes de referencia de los personajes |
| `Escenas/` | Fotogramas iniciales de cada escena |
| `Pipeline/` | Scripts en Python para transcribir, montar capítulos, intro y créditos (ffmpeg) |

## Videos

Los videos (~4 GB) **no están en el repositorio** porque GitHub no acepta archivos de más de 100 MB. Para usar la consola hay que poner los 21 videos en `Consola/videos/` (la lista está en `Consola/LEEME.md`).

## Cómo correr la función

1. Copiar la carpeta `Consola` completa, con `videos/`, `img/` y `plan-b/`.
2. Abrir `Consola/consola-v2.html` con doble clic en Chrome o Edge. No necesita internet.
3. En la pantalla de inicio: revisar que diga **Videos 21 de 21**, activar el micrófono y probar el sonido.
4. **Iniciar función.** Ayuda con la tecla `?`.

## Uso de inteligencia artificial

- Imágenes de las escenas: ChatGPT (OpenAI)
- Video, actuación y voces: Grok Imagine (xAI)
- Guion, prompts, montaje y consola: Claude (Anthropic)
- Apoyo en el artículo: Gemini (Google)

La trama, las decisiones y la revisión final son del equipo.
