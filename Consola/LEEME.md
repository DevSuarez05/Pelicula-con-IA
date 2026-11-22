# Consola de la función · Corazón de Pulpa

`consola.html` es el archivo que se proyecta el día de la sustentación. Reproduce los capítulos en orden, abre las votaciones con temporizador, mueve los indicadores y decide el final. **No necesita internet**: basta con abrirlo en Chrome o Edge.

## 1. Cómo se arma

```
Consola/
├── consola.html
├── LEEME.md
└── videos/
    ├── intro.mp4
    ├── prologo.mp4
    └── … (los 21 archivos de la tabla)
```

Los 21 videos ya están en `videos/`, copiados desde `Produccion/con-voz/`. Si se rehace un clip:

1. Vuelvan a armar el bloque.
2. Cópienlo encima con el nombre de la tabla, en minúsculas y sin tildes.
3. Abran `consola.html` (doble clic) y opriman **Revisar videos**. Cada archivo debe salir con ✓ y su duración.

**No pongan los números de los indicadores dentro de los videos.** La consola los muestra con los valores reales de cada función.

Si falta un video, la consola muestra una tarjeta con su título, el archivo esperado y un resumen, y se puede seguir.

## 2. Los 21 videos

| # | Archivo | Clips | Cuándo se proyecta |
|---|---|---|---|
| 1 | `intro.mp4` | Póster con el equipo + C1 a C4 + Don Lulo | Siempre, después de "Apaguen las luces" |
| 2 | `prologo.mp4` | P1 a P3 + "Tres meses antes…" | Siempre |
| 3 | `cap01.mp4` | 1.1, J1 a J4, 1.7, 1.8 | Siempre |
| 4 | `cap01-duplicar.mp4` | 1D | Si el salón vota DUPLICAR en D1 |
| 5 | `cap01-adaptar.mp4` | 1A | Si el salón vota ADAPTAR en D1 |
| 6 | `cap02.mp4` | 2.1 a 2.10 + G3 | Siempre |
| 7 | `comercial.mp4` | CM1 a CM3 | Siempre |
| 8 | `cap03.mp4` | 3.1 a 3.4 | Siempre |
| 9 | `cap03-r.mp4` | 3R | Siempre, después de votar R |
| 10 | `cap03-i.mp4` | 3I | Siempre, después de votar I |
| 11 | `cap03-fin.mp4` | 3F | Siempre |
| 12 | `cap04.mp4` | 4.1 a 4.4 | Siempre |
| 13 | `cap04-planta-duplicar.mp4` | 4AD | D3a = DUPLICAR |
| 14 | `cap04-planta-adaptar.mp4` | 4AA | D3a = ADAPTAR |
| 15 | `cap04-diciembre-duplicar.mp4` | 4BD | D3b = DUPLICAR |
| 16 | `cap04-diciembre-adaptar.mp4` | 4BA | D3b = ADAPTAR |
| 17 | `cap04-fin.mp4` | 4F | Siempre |
| 18 | `final-con-pulpa.mp4` | FA1 a FA5 | Si el promedio final es 55 o más |
| 19 | `final-pura-cascara.mp4` | FB1 a FB5 | Si el promedio final es menor que 55 |
| 20 | `final-extracto.mp4` | FA1 + FA4 | Solo si salió "Pura cáscara" y el salón pide ver el otro final |
| 21 | `creditos.mp4` | CR2 + créditos + CR1 | Siempre |

## 3. Lo que hace la consola en cada parada

| Parada | Qué muestra | Qué cambia |
|---|---|---|
| Apaguen las luces | Pantalla negra con latido | Nada |
| Ensayo del grito | "¡Así lo hace Frugle!" → "¡Pero nosotros no somos Frugle!" | Nada |
| D1 (45 s) | Pregunta y dos paneles: verde DUPLICAR y roja ADAPTAR | ADAPTAR suma +10 al criterio del salón. Don Harold envía igual |
| Fin del cap. 1 | Barras grandes | Clima 76, Cultura 78, VRIO 60 |
| Fin del Acto 1 (después del cap. 2) | Barras grandes | Clima 45, Cultura 50, VRIO 42 |
| D2 · prueba VRIO (2 preguntas de 15 s) | SÍ (verde) o NO (roja), luego responde la Piña | Por acierto: +3 de VRIO y +5 de criterio |
| Capital de confianza | El criterio dividido entre 5 | Se suma a cada indicador (máximo +4) |
| Grito nuevo | "¿Y cómo lo hacemos aquí?" → "¡Con pulpa!" | Nada |
| D3a planta y D3b diciembre (30 s) | Ahora sí se ejecuta | ADAPTAR: Clima +8, Cultura +7, VRIO +6 · DUPLICAR: Clima −4, Cultura −4, VRIO −3 |
| Indicadores finales | Las barras suben desde cero, aparece el promedio contra la línea de 55 y un destello | Elige el final |
| ¿Ver el otro final? | Solo si salió "Pura cáscara" | Proyecta o no `final-extracto.mp4` |
| Resumen | Tabla con todo lo que votó el salón | Nada |

Con estos números el final depende del salón:

| Votos en D3 | Criterio | Promedio | Final |
|---|---|---|---|
| ADAPTAR + ADAPTAR | Cualquiera | 60 a 66 | "Con pulpa" |
| Uno y uno | Perfecto (20) | 55 | "Con pulpa" por un pelo |
| Uno y uno | Bajo | 49 | "Pura cáscara" |
| DUPLICAR + DUPLICAR | Cualquiera | 38 a 44 | "Pura cáscara" |

En las votaciones con temporizador, cuando llega a cero aparece **¡TIEMPO!** y la consola espera a que el presentador marque la tarjeta que ganó. Si el salón termina antes, se puede marcar antes.

## 4. Teclas

| Tecla | Qué hace |
|---|---|
| `Espacio` o `Enter` | Continuar. Durante un video: pausar o reanudar |
| `AvPág` o `→` | Continuar. Durante un video: saltarlo |
| `RePág`, `←` o `Retroceso` | Volver al paso anterior. Deshace la votación y los indicadores |
| `V` o `1` | Ganó la tarjeta verde |
| `R` o `2` | Ganó la tarjeta roja |
| `F` | Pantalla completa |
| `H` | Mostrar u ocultar los indicadores encima de los videos |
| `M` | Menú: saltar a cualquier paso, ajustar indicadores a mano, volver al inicio |
| `S` | Silenciar los sonidos de la consola (no afecta el audio de los videos) |
| `?` | Ayuda |
| `Esc` | Cerrar el menú o la ayuda |

Un control de diapositivas (de los que pasan con AvPág y RePág) sirve para manejar la función desde el frente del salón. Las votaciones se marcan desde el teclado o con el mouse.

## 5. Si algo sale mal

- **Se cerró el navegador o se apagó el computador.** Al abrir de nuevo `consola.html` aparece el botón *Continuar en…* con los indicadores tal como estaban.
- **Se marcó la tarjeta equivocada.** `RePág` vuelve a la votación y deshace su efecto.
- **Un video no carga.** La consola muestra su tarjeta de resumen. El presentador lo cuenta en voz alta y sigue con `Espacio`.
- **Hay que saltar un capítulo por tiempo.** `M` → elegir el paso. Si se salta una votación del Acto 2, corrijan los indicadores en el mismo menú.
- **El video no arranca solo** (pasa en algunos navegadores la primera vez). Aparece un botón *Reproducir*: un clic y sigue.

## 6. Modo ensayo

En la pantalla de inicio, *Modo ensayo* reemplaza todos los videos por sus tarjetas. Sirve para que el presentador practique las votaciones, los gritos y los tiempos sin proyectar la película, y para probar los dos finales.

## 7. Antes de la función

1. Copien la carpeta `Consola/` completa al computador del salón (o llévenla en una USB y ábranla desde ahí).
2. Abran `consola.html` en Chrome o Edge y revisen los 21 videos con **Revisar videos**.
3. Prueben el audio y la pantalla completa (`F`) con el proyector.
4. Repartan las tarjetas: una verde y una roja por estudiante.
5. Tengan a mano el MP4 de respaldo (sección 8) por si el computador del salón no deja abrir la consola.

El plan completo del ensayo (roles, guion del presentador, cronograma y simulacros) está en `Produccion/05-Ensayo-y-Plan-B.md`.

## 8. Video de respaldo (plan B)

`plan-b/` arma un solo MP4 con toda la función, para proyectar en VLC si la consola falla. Donde la consola abriría una votación, el video muestra una tarjeta con la pregunta y la deja en pantalla el tiempo de la votación. El salón vota igual con las tarjetas físicas, pero la historia sigue siempre el camino ADAPTAR y termina en "Con pulpa".

```
plan-b/
├── armar-respaldo.bat      ← doble clic aquí
├── armar-respaldo.ps1
├── generar-tarjetas.ps1    ← solo si cambian textos de las tarjetas
├── tarjetas/               ← 13 tarjetas de 1920×1080 ya generadas
├── montaje/                ← las mismas tarjetas numeradas en orden (las crea el .bat)
└── LISTA-DE-MONTAJE.csv    ← el orden completo, con duraciones (lo crea el .bat)
```

**Con ffmpeg (automático).** Cuando estén los videos en `videos/`, doble clic en `armar-respaldo.bat`. Arma `plan-b/respaldo.mp4` (unos 14 minutos) con capítulos para saltar en VLC desde *Reproducción → Capítulo*. En el computador de Daniel ya está instalado y probado (con videos de prueba armó 12 minutos en 2 minutos, con imagen, sonido y capítulos correctos). En otro computador sin ffmpeg, se instala con este comando en una terminal y luego se vuelve a correr el .bat:

```bash
winget install Gyan.FFmpeg
```

**Sin ffmpeg (en el editor).** El .bat igual deja `LISTA-DE-MONTAJE.csv` (se abre en Excel) y la carpeta `montaje/`. En CapCut, Clipchamp o DaVinci se ponen en la línea de tiempo los videos y las tarjetas en el orden de la lista, cada tarjeta con la duración que dice su nombre (por ejemplo `005 - tarjeta d1 (50 s).png`), y se exporta en 1080p.

El respaldo usa 16 de los 21 videos: las reacciones "-adaptar", el final "Con pulpa" y nada del final B ni del extracto.

## Consola v2 (`consola-v2.html`)

Versión más dinámica de la consola. La original (`consola.html`) sigue igual, como respaldo.

- **Aplausómetro:** en las votaciones DUPLICAR / ADAPTAR, al acabar el tiempo (o con Espacio) la consola escucha por el micrófono del portátil. Primero aplauden los de la opción verde y luego los de la roja, 5 s cada uno. Gana el aplauso más fuerte. Si queda parejo (menos de 4 puntos de diferencia) o no hay micrófono, el presentador elige con V o R. La prueba VRIO sigue con tarjetas.
- **Antes de empezar:** en la pantalla de inicio, oprimir **Activar** en "Micrófono" y aceptar el permiso del navegador. La barrita debe moverse al hablar. "Sonido → Probar" revisa los parlantes. "Videos" debe decir 21 de 21.
- **Show:** transiciones con destello, cuenta regresiva con latido y temblor, reacciones de los personajes (fotos en `img/`), barras que brillan al caer o subir, redoble en la revelación, confeti de frutas ("Con pulpa") o pantalla que se agrieta ("Pura cáscara"), línea de tiempo abajo.
- **P:** panel del presentador (qué sigue, qué decir, tiempo de función). Ojo: también lo ve el público.
- **B:** si un video no abre, reproduce ese tramo desde `plan-b/respaldo.mp4`.
- **Al final:** "Descargar resumen (Excel)" guarda un CSV con cada decisión, cómo se decidió y los indicadores.
