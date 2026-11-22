"""Une clips de Grok (con su propia voz) en un solo video 1920x1080, con volumen nivelado y tarjetas de título.
Uso: python armar.py SALIDA.mp4 CARPETA ID ID "T:Tres meses antes…:4" ID ...
  ID          → CARPETA/ID.mp4
  T:texto:seg → tarjeta de título sobre el fondo de la película"""
import sys, subprocess, pathlib
from PIL import Image, ImageDraw, ImageFont
from camara import FF

P = pathlib.Path(__file__).parent
TMP = P / "tmp_armar"; TMP.mkdir(exist_ok=True)
VF = "scale=1920:1094:flags=lanczos,crop=1920:1080,fps=24,format=yuv420p,setsar=1"
ENC = ["-c:v", "libx264", "-crf", "17", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]

def clip(src, out):
    subprocess.run([FF, "-y", "-v", "error", "-i", str(src), "-map", "0:v:0", "-map", "0:a:0", "-vf", VF,
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000", *ENC, str(out)], check=True)

def tarjeta(texto, seg, out):
    img = Image.new("RGB", (1920, 1080), (26, 20, 16)); d = ImageDraw.Draw(img)
    f = ImageFont.truetype(str(P / "fuentes/PlayfairDisplay-Italic.ttf"), 110)
    w = d.textlength(texto, font=f); d.text(((1920 - w) / 2, 470), texto, font=f, fill=(245, 239, 227))
    png = TMP / "t.png"; img.save(png)
    subprocess.run([FF, "-y", "-v", "error", "-loop", "1", "-i", str(png), "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                    "-t", str(seg), "-vf", f"fade=in:st=0:d=0.6,fade=out:st={seg - 0.6}:d=0.6,format=yuv420p,setsar=1", "-r", "24",
                    *ENC, str(out)], check=True)

if __name__ == "__main__":
    salida, carpeta, *items = sys.argv[1:]
    partes = []
    for i, it in enumerate(items):
        out = TMP / f"{i:03d}.mp4"
        if it.startswith("T:"):
            _, texto, seg = it.split(":"); tarjeta(texto, float(seg), out)
        else:
            src = pathlib.Path(carpeta) / f"{it}.mp4"
            if not src.exists(): print("falta", it); continue
            clip(src, out)
        partes.append(out)
    lista = TMP / "lista.txt"; lista.write_text("".join(f"file '{p.as_posix()}'\n" for p in partes), encoding="utf-8")
    subprocess.run([FF, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lista), "-c", "copy", "-movflags", "+faststart", salida], check=True)
    print("listo", salida)
