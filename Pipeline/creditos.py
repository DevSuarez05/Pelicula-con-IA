"""Créditos: CR2 (despedida) → créditos que suben sobre el escenario desenfocado → CR1 (blooper).
Uso: python creditos.py CARPETA   (CARPETA con CR1.mp4 y CR2.mp4)
Salida: Produccion/con-voz/CREDITOS.mp4"""
import sys, subprocess, pathlib, textwrap
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from intro import fuente, musica_provisional, dur, PLAY, MONT, CREMA, ORO, TMP, R
from armar import clip, ENC

OUT = R / "Produccion/con-voz/CREDITOS.mp4"
VEL = 135  # píxeles por segundo

REFS = [
    "Barney, J. (1991). Firm resources and sustained competitive advantage. Journal of Management, 17(1), 99-120.",
    "DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. American Sociological Review, 48(2), 147-160.",
    "Google. (2026). Gemini (Versión 2026) [Modelo de lenguaje de gran tamaño]. https://gemini.google.com/",
    "Gratton, L. (2021). How to do hybrid right. Harvard Business Review, 99(3), 66-74.",
    "Snyder, H. (2019). Literature review as a research methodology: An overview and guidelines. Journal of Business Research, 104, 333-339.",
    "Wright, P. M., Dunford, B. B., & Snell, S. A. (2001). Human resources and the resource based view of the firm. Journal of Management, 27(6), 701-721.",
]

def rodillo(png):
    tit, sub = fuente(PLAY, 120), fuente(MONT, 48, 600)
    sec, nom, rol, txt = fuente(MONT, 40, 700), fuente(PLAY, 66), fuente(MONT, 36, 400), fuente(MONT, 30, 400)
    items = [("Corazón de Pulpa", tit, CREMA, 0), ("¿Duplicar o Adaptar?", sub, ORO, 140),
             ("REPARTO", sec, ORO, 30)]
    for n, r in [("Don Harold", "el gerente que todo lo copia"), ("Valentina", "la estratega"), ("Daniel", "el analista"),
                 ("La Piña", "el profesor"), ("Don Lulo", "veinte años en la planta")]:
        items += [(n, nom, CREMA, 0), (r, rol, ORO, 26)]
    items[-1] = items[-1][:3] + (130,)
    items += [("UN TRABAJO DE", sec, ORO, 30),
              ("Daniel Andrés Suárez Ramírez", nom, CREMA, 0), ("creador de la trama", rol, ORO, 26),
              ("Harold Yamid Arango", nom, CREMA, 26), ("Valentina Constain", nom, CREMA, 130),
              ("PROFESOR", sec, ORO, 30), ("Carlos Mario Tabares", nom, CREMA, 130),
              ("BASADA EN EL ARTÍCULO", sec, ORO, 30), ("Benchmarking en gestión humana", nom, CREMA, 130),
              ("REFERENCIAS", sec, ORO, 40)]
    for ref in REFS:
        lin = textwrap.wrap(ref, 78)
        for k, l in enumerate(lin):
            items.append((l, txt, CREMA, 30 if k == len(lin) - 1 else 6))
    items[-1] = items[-1][:3] + (130,)
    items += [("USO DE INTELIGENCIA ARTIFICIAL", sec, ORO, 30)]
    for l in ["Imágenes de las escenas: ChatGPT (OpenAI)", "Video, actuación y voces: Grok Imagine (xAI)",
              "Guion, prompts, montaje y consola: Claude (Anthropic)", "Apoyo en el artículo: Gemini (Google)",
              "La trama, las decisiones y la revisión final son del equipo."]:
        items.append((l, fuente(MONT, 34, 400), CREMA, 14))
    items[-1] = items[-1][:3] + (160,)
    items += [("Universidad Nacional de Colombia", fuente(PLAY, 80), CREMA, 6), ("Sede Manizales · 2026", sub, ORO, 0)]

    alto_de = lambda f: f.getmetrics()[0] + f.getmetrics()[1]
    H = int(sum(alto_de(f) + e for _, f, _, e in items)) + 20
    img = Image.new("RGBA", (1920, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img); y = 0
    for t, f, c, e in items:
        w = d.textlength(t, font=f)
        d.text(((1920 - w) / 2 + 3, y + 3), t, font=f, fill=(0, 0, 0, 230))
        d.text(((1920 - w) / 2, y), t, font=f, fill=c + (255,))
        y += alto_de(f) + e
    img.save(png); return H

def roll(cr2, out):
    from intro import FF
    fondo = TMP / "fondo.png"
    subprocess.run([FF, "-y", "-v", "error", "-sseof", "-0.2", "-i", str(cr2), "-map", "0:v:0", "-frames:v", "1",
                    "-vf", "scale=1920:1094,crop=1920:1080", str(fondo)], check=True)
    im = Image.open(fondo).convert("RGB").filter(ImageFilter.GaussianBlur(18))
    ImageEnhance.Brightness(im).enhance(0.38).save(fondo)
    H = rodillo(TMP / "rodillo.png")
    T = round((H + 560) / VEL, 2)  # termina con la universidad centrada
    musica_provisional(T, TMP / "musica_cr.wav")
    filt = (f"[0:v]fade=in:st=0:d=1[b];[1:v]format=rgba[r];"
            f"[b][r]overlay=x=0:y='1080-t*{VEL}':shortest=0,fade=out:st={T - 1}:d=1,format=yuv420p,setsar=1[v]")
    subprocess.run([FF, "-y", "-v", "error", "-loop", "1", "-t", str(T), "-i", str(fondo), "-loop", "1", "-t", str(T),
                    "-i", str(TMP / "rodillo.png"), "-i", str(TMP / "musica_cr.wav"), "-filter_complex", filt,
                    "-map", "[v]", "-map", "2:a", "-af", "aresample=48000", "-t", str(T), "-r", "24", *ENC, str(out)], check=True)
    return T

if __name__ == "__main__":
    from intro import FF
    C = pathlib.Path(sys.argv[1])
    partes = [TMP / "cr_a.mp4", TMP / "cr_b.mp4", TMP / "cr_c.mp4"]
    clip(C / "CR2.mp4", partes[0])
    print("rodillo", roll(C / "CR2.mp4", partes[1]), "s")
    clip(C / "CR1.mp4", partes[2])
    lista = TMP / "lista_cr.txt"; lista.write_text("".join(f"file '{p.as_posix()}'\n" for p in partes), encoding="utf-8")
    subprocess.run([FF, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lista), "-c", "copy", "-movflags", "+faststart", str(OUT)], check=True)
    print("listo", OUT, round(dur(OUT), 2), "s")
