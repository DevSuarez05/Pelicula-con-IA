"""Fase 1 (versión 2): 1.07, 1.20 y 1.26 con voz actuada, cámara cinematográfica, música y efectos.
Uso: python clips_prueba.py [1.07 1.20 1.26]
Si existe colab/salida/FILA.mp4 (cara animada por SadTalker o LivePortrait), se usa en lugar de la imagen fija."""
import json, sys, pathlib, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import camara as C, sonido as S
from camara import kf, Capa, Camara, W, H

R = pathlib.Path(__file__).parent
IMG = R.parent / "Imagenes"; AUD = R / "prueba" / "audio"; ACT = R / "actuaciones"
OUT = R / "prueba" / "clips"; TMP = R / "prueba" / "capas"; COLAB = R / "colab" / "salida"
OUT.mkdir(parents=True, exist_ok=True); TMP.mkdir(parents=True, exist_ok=True)
HAROLD = IMG / "Don Harold_ Jefe de Gestión Humana.png"
CREMA, DORADO, NEGRO = (245, 239, 227), (201, 162, 77), (26, 20, 16)
POST = "unsharp=5:5:0.5,vignette=PI/4.5,noise=alls=4:allf=t"

def font(kind, size):
    f = ImageFont.truetype(str(R / "fuentes" / ("PlayfairDisplay-Italic.ttf" if kind == "titulo" else "Montserrat.ttf")), size)
    f.set_variation_by_name({"sub": "SemiBold", "cuerpo": "Regular", "rotulo": "SemiBold", "titulo": "Bold Italic"}[kind]); return f

def tiempos(fila):
    t = json.loads((AUD / f"{fila}.json").read_text(encoding="utf-8"))
    spec = json.loads((ACT / f"{fila}.json").read_text(encoding="utf-8"))
    for a, b in zip(t["frases"], spec["frases"]): a["sub"] = b.get("sub", b["t"])
    return t

def img_sub(texto):
    im = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(im); f = font("sub", 46)
    words, lines, cur = texto.split(), [], ""
    for w in words:
        c = (cur + " " + w).strip()
        if d.textlength(c, font=f) > 1400: lines.append(cur); cur = w
        else: cur = c
    lines.append(cur); y = H - 60 - len(lines) * 60
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill="white", stroke_width=3, stroke_fill="black"); y += 60
    return im

def subtitulos(t, v0, max_chars=48):
    """Agrupa frases en subtítulos de hasta ~48 caracteres; cada uno aparece con su frase."""
    grupos, cur = [], []
    for f in t["frases"]:
        if cur and len(" ".join(x["sub"] for x in cur + [f])) > max_chars: grupos.append(cur); cur = []
        cur.append(f)
    if cur: grupos.append(cur)
    capas = []
    for i, g in enumerate(grupos):
        a = v0 + g[0]["ini"]; b = v0 + (grupos[i + 1][0]["ini"] if i + 1 < len(grupos) else g[-1]["fin"] + 0.6)
        capas.append(Capa(img_sub(" ".join(x["sub"] for x in g)), fija=True, opac=kf((a - 0.08, 0), (a, 1, "lineal"), (b - 0.06, 1), (b, 0, "lineal"))))
    return capas

def capa_colab(fila, defecto):
    v = COLAB / f"{fila}.mp4"
    return (C.Video(str(v)), True) if v.exists() else (defecto, False)

# ---------------- 1.26 · Decisión 1 ----------------
def clip_126():
    t = tiempos("1.26"); v0 = 0.6; F = [(v0 + f["ini"], v0 + f["fin"]) for f in t["frases"]]
    tf = F[-1][1] + 0.45; T = tf + 3.4
    s = 1920 / 1312                                    # la imagen ocupa el ancho del cuadro a zoom 1
    ojo = (960 + (0.495 * 1312 - 656) * s, 540 + (0.26 * 1199 - 599.5) * s)
    cara = (960, 540 + (0.36 * 1199 - 599.5) * s)
    harold = Capa(HAROLD, escala=s)
    cam = Camara(
        zoom=kf((0, 1.0), (F[0][1] + 0.05, 1.07, "lineal"), (F[0][1] + 0.33, 1.65, "golpe"), (F[2][0] - 0.25, 1.78, "suave"),
                (F[2][0] + 0.05, 2.55, "golpe"), (F[3][0], 2.7, "suave"), (tf, 3.05, "entra")),
        cx=kf((0, 960), (F[0][1] + 0.33, cara[0] - 25, "golpe"), (F[2][0] - 0.25, cara[0] + 55, "suave"), (F[2][0] + 0.05, ojo[0] - 10, "golpe"),
              (F[3][0], ojo[0] + 18, "suave"), (tf, ojo[0], "entra")),
        cy=kf((0, cara[1] + 60), (F[0][1] + 0.05, cara[1] + 40, "lineal"), (F[0][1] + 0.33, cara[1] - 30, "golpe"), (F[2][0] - 0.25, cara[1] - 45),
              (F[2][0] + 0.05, ojo[1] + 25, "golpe"), (F[3][0], ojo[1] + 15), (tf, ojo[1] + 10, "entra")),
        rot=kf((0, -2.5), (F[0][1] + 0.33, -1.0, "golpe"), (F[2][0] - 0.25, 1.6), (F[2][0] + 0.05, -0.8, "golpe"), (tf, 0.0, "entra")),
        temblor=kf((0, 2.5), (tf - 0.05, 9.0, "entra"), (tf, 0, "lineal")))
    # congelado: velo oscuro, destello blanco y título
    velo = Capa(Image.new("RGBA", (W, H), (0, 0, 0, 150)), fija=True, opac=kf((tf, 0), (tf + 0.5, 1, "lineal")))
    flash = Capa(Image.new("RGBA", (W, H), (255, 250, 235, 255)), fija=True, opac=kf((tf - 0.01, 0), (tf, 0.85, "lineal"), (tf + 0.18, 0, "sale")))
    tit = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(tit); f = font("titulo", 180); x = "Decisión 1"
    d.text(((W - d.textlength(x, font=f)) / 2, H / 2 - 150), x, font=f, fill=DORADO, stroke_width=2, stroke_fill=NEGRO)
    fs = font("rotulo", 46); q = "¿Qué debe hacer Don Harold?"; d.text(((W - d.textlength(q, font=fs)) / 2, H / 2 + 80), q, font=fs, fill=CREMA)
    titulo = Capa(tit, fija=True, escala=kf((tf + 0.1, 1.08), (tf + 1.2, 1.0, "sale")), opac=kf((tf + 0.1, 0), (tf + 0.7, 1, "lineal")))
    mus = [S.pista_tension(T, tf, golpes=[F[0][1] + 0.3, F[2][0] + 0.02]), S.latido(T, 0.82, 0.2, tf, 0.30)]
    S.mezclar(T, AUD / "1.26.wav", v0, mus, TMP / "1.26-mezcla.wav", musica_db=-12, ducking_db=-6)
    C.render(T, [harold, velo, flash, titulo], cam, TMP / "1.26-mezcla.wav", OUT / "1.26.mp4",
             post="eq=saturation=0.78:contrast=1.14,colorbalance=rs=0.08:bs=0.05:rh=0.04," + POST.replace("PI/4.5", "PI/3.4"))

# ---------------- 1.20 · Confesionario ----------------
def clip_120():
    t = tiempos("1.20"); v0 = 0.5; F = [(v0 + f["ini"], v0 + f["fin"]) for f in t["frases"]]
    T = round(F[-1][1] + 1.6, 2); pf = F[2][0]              # "Por favor."
    fuente, animada = capa_colab("1.20", HAROLD)
    if animada:   # el video de Colab ya trae la cara viva; se ubica igual que la imagen
        s = 1920 / fuente.w; harold = Capa(fuente, escala=s, y=540 + (fuente.h * s - 1080) / 2 - 40)
    else:
        s = 1920 / 1312; harold = Capa(HAROLD, escala=s, y=540 + (1199 * s - 1080) / 2 - 40, respira=0.004, vaiven=0.25, ancla=(0.5, 0.5))
    # encuadre: el tallito siempre dentro del cuadro (biblia visual)
    cam = Camara(zoom=kf((0, 1.02), (pf - 0.02, 1.04, "lineal"), (pf + 0.22, 1.15, "golpe"), (F[4][0], 1.16), (T, 1.22, "suave")),
                 cx=kf((0, 960), (pf - 0.02, 960), (pf + 0.22, 940, "golpe"), (T, 950)),
                 cy=kf((0, 515), (pf - 0.02, 510, "lineal"), (pf + 0.22, 445, "golpe"), (T, 430)),
                 rot=kf((0, 0.0), (pf + 0.22, -0.8, "golpe"), (T, -0.4)), temblor=2.0)
    S.mezclar(T, AUD / "1.20.wav", v0, [S.pista_confesionario(T, golpe_t=pf + 0.05, remate=F[-1][1] + 0.12)], TMP / "1.20-mezcla.wav", musica_db=-10)
    C.render(T, [harold] + subtitulos(t, v0), cam, TMP / "1.20-mezcla.wav", OUT / "1.20.mp4", post="eq=saturation=1.05," + POST)

# ---------------- 1.07 · Sala de juntas ----------------
def clip_107():
    t = tiempos("1.07"); v0 = 0.6; F = [(v0 + f["ini"], v0 + f["fin"]) for f in t["frases"]]
    wp = F[5][0] + 0.15; T = round(F[-1][1] + 1.8, 2)      # el paneo rápido a la pantalla cae en "¡el modelo tres por dos!"
    src = Image.open(HAROLD).convert("RGB")
    fondo = src.resize((2900, int(2900 * src.height / src.width))).filter(ImageFilter.GaussianBlur(45))
    fondo = Image.blend(ImageEnhance.Brightness(fondo).enhance(0.5), Image.new("RGB", fondo.size, (120, 80, 30)), 0.2)
    # pantalla de la sala con el texto académico, en el mundo a la izquierda
    pan = Image.new("RGBA", (820, 520)); d = ImageDraw.Draw(pan)
    d.rounded_rectangle((0, 0, 819, 519), 22, fill=(26, 20, 16, 240), outline=DORADO + (255,), width=5)
    d.text((55, 40), "Modelo 3x2", font=font("titulo", 100), fill=DORADO); d.line((55, 180, 765, 180), fill=DORADO, width=3)
    fb, fs = font("cuerpo", 50), font("rotulo", 50)
    d.text((55, 220), "3 días", font=fs, fill=CREMA); d.text((250, 220), "en la oficina", font=fb, fill=CREMA)
    d.text((55, 305), "2 días", font=fs, fill=CREMA); d.text((250, 305), "en la casa", font=fb, fill=CREMA)
    d.text((55, 410), "«Así lo hace Frugle»", font=font("cuerpo", 38), fill=DORADO)
    animado = (COLAB / "1.07.mp4").exists()
    if animado:
        v = C.Video(str(COLAB / "1.07.mp4"), llave=(255, 0, 255)); hcapa = Capa(v, escala=920 / v.h, x=1560, y=1100, ancla=(0.5, 1.0))
    else:
        har = Image.open(R / "recortes" / "HAROLD.png"); har = har.crop(har.getchannel("A").getbbox())
        har = har.resize((int(har.width * 920 / har.height), 920), Image.LANCZOS)
        hcapa = Capa(har, x=1560, y=1100, ancla=(0.5, 1.0), respira=0.006, vaiven=0.35)
    capas = [Capa(fondo, x=1200, y=540, paralaje=0.55),
             Capa(pan, x=560, y=470, opac=kf((wp - 0.1, 0), (wp + 0.15, 1, "lineal")), escala=kf((wp - 0.1, 0.92), (wp + 0.5, 1.0, "sale"))),
             hcapa]
    cam = Camara(
        zoom=kf((0, 1.0), (F[0][1], 1.05), (F[1][0] + 0.12, 1.10, "golpe"), (F[2][0] + 0.12, 1.16, "golpe"), (F[4][1], 1.22, "suave"),
                (wp + 0.38, 1.0, "golpe"), (T, 1.04, "lineal")),
        cx=kf((0, 1380), (F[2][0] + 0.12, 1430, "golpe"), (wp, 1440), (wp + 0.38, 620, "golpe"), (T, 600, "lineal")),
        cy=kf((0, 560), (F[4][1], 470, "suave"), (wp + 0.38, 480, "golpe"), (T, 470)),
        rot=kf((0, 0), (wp, 0.6), (wp + 0.38, -0.5, "golpe"), (T, 0)), temblor=kf((0, 1.5), (wp, 2.5), (T, 1.5)))
    golpes = [F[1][0] + 0.1, F[2][0] + 0.1]
    mus = [S.pista_showman(T, golpes=golpes, final=wp + 0.3)]
    wh = S.silencio(T); S.put(wh, S.whoosh(0.45), wp - 0.12, 0.9); mus.append(wh)
    S.mezclar(T, AUD / "1.07.wav", v0, mus, TMP / "1.07-mezcla.wav", musica_db=-13)
    C.render(T, capas + subtitulos(t, v0), cam, TMP / "1.07-mezcla.wav", OUT / "1.07.mp4", post=POST)

if __name__ == "__main__":
    pedidos = sys.argv[1:] or ["1.07", "1.20", "1.26"]
    for fila in pedidos:
        {"1.07": clip_107, "1.20": clip_120, "1.26": clip_126}[fila](); print("listo", fila)
