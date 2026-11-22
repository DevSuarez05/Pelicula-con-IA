"""Fase 1: arma los clips de prueba 1.20, 1.07 y 1.26 con imagen + movimiento + voz + texto.
Uso: python armar_prueba.py   (salida en prueba/clips/)"""
import subprocess, json, pathlib, shutil, glob, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

R = pathlib.Path(__file__).parent
IMG = R.parent / "Imagenes"
OUT = R / "prueba" / "clips"; OUT.mkdir(parents=True, exist_ok=True)
CAP = R / "prueba" / "capas"; CAP.mkdir(parents=True, exist_ok=True)
AUD = R / "prueba" / "audio"
W, H, FPS = 1920, 1080, 24

def tool(name):
    p = shutil.which(name)
    if p: return p
    g = glob.glob(os.path.join(os.environ["LOCALAPPDATA"], r"Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin", name + ".exe"))
    return g[0]
FF, FP = tool("ffmpeg"), tool("ffprobe")

def dur(f):
    return float(subprocess.check_output([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))

def font(kind, size):
    f = ImageFont.truetype(str(R / "fuentes" / ("Montserrat.ttf" if kind != "titulo" else "PlayfairDisplay-Italic.ttf")), size)
    f.set_variation_by_name({"sub": "SemiBold", "cuerpo": "Regular", "rotulo": "SemiBold", "titulo": "Bold Italic"}[kind])
    return f

CREMA, DORADO, NEGRO = (245, 239, 227), (201, 162, 77), (26, 20, 16)

def subtitulo(texto, path):
    """Subtítulo según la biblia: Montserrat SemiBold blanco, contorno negro, tercio inferior."""
    im = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(im); f = font("sub", 46)
    words, lines, cur = texto.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > 1500: lines.append(cur); cur = w
        else: cur = t
    lines.append(cur)
    y = H - 50 - len(lines) * 60
    for ln in lines:
        x = (W - d.textlength(ln, font=f)) / 2
        d.text((x, y), ln, font=f, fill="white", stroke_width=3, stroke_fill="black"); y += 60
    im.save(path)

def run(args):
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error"] + args, check=True)

ENC = ["-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-movflags", "+faststart"]

# ---------- 1.20 · Confesionario de Don Harold ----------
def clip_120():
    a = AUD / "1.20.mp3"; T = max(8.0, round(dur(a) + 1.0, 2))
    src = Image.open(IMG / "Don Harold_ Jefe de Gestión Humana.png").convert("RGB")
    src.crop((0, 0, 1312, 738)).resize((W, H), Image.LANCZOS).save(CAP / "120-base.png")
    subtitulo("¿Yo, improvisar? Por favor. Yo no improviso: yo copio con seguridad.", CAP / "120-sub.png")
    # empuje lento hacia la cara (centro de la cara ≈ 47 % del ancho, 42 % del alto)
    z = f"(1+0.07*t/{T})"
    vf = (f"[0:v]scale=w='trunc({W}*{z}/2)*2':h='trunc({H}*{z}/2)*2':eval=frame:flags=bicubic,"
          f"crop={W}:{H}:x='{W}*0.07*t/{T}*0.47':y='{H}*0.07*t/{T}*0.42',vignette=PI/5,format=rgba[v];"
          f"[v][1:v]overlay=0:0:enable='between(t,0.4,{T-0.3})',format=yuv420p[vo];"
          f"[2:a]adelay=400|400,apad,atrim=0:{T},afade=t=out:st={T-0.4}:d=0.4[ao]")
    run(["-loop", "1", "-framerate", str(FPS), "-t", str(T), "-i", str(CAP / "120-base.png"),
         "-loop", "1", "-framerate", str(FPS), "-t", str(T), "-i", str(CAP / "120-sub.png"),
         "-i", str(a), "-filter_complex", vf, "-map", "[vo]", "-map", "[ao]", "-t", str(T)] + ENC + [str(OUT / "1.20.mp4")])

# ---------- 1.07 · Sala de juntas (composición provisional) ----------
def clip_107():
    a = AUD / "1.07.mp3"; T = round(dur(a) + 1.2, 2)
    src = Image.open(IMG / "Don Harold_ Jefe de Gestión Humana.png").convert("RGB")
    # Fondo provisional: el fondo original muy desenfocado y cálido, hasta tener el plano de la sala de juntas
    bg = src.resize((W, int(W * src.height / src.width))).crop((0, 0, W, H)).filter(ImageFilter.GaussianBlur(38))
    bg = ImageEnhance.Brightness(bg).enhance(0.55)
    bg = Image.blend(bg, Image.new("RGB", (W, H), (120, 80, 30)), 0.18)
    # Pantalla de la sala con el texto académico (se agrega en edición, como dice el guion)
    scr = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(scr)
    x0, y0, x1, y1 = 110, 170, 860, 640
    d.rounded_rectangle((x0, y0, x1, y1), 18, fill=(26, 20, 16, 235), outline=DORADO + (255,), width=4)
    d.text((x0 + 50, y0 + 45), "Modelo 3x2", font=font("titulo", 92), fill=DORADO)
    d.line((x0 + 50, y0 + 170, x1 - 50, y0 + 170), fill=DORADO, width=3)
    fb = font("cuerpo", 46); fs = font("rotulo", 46)
    d.text((x0 + 50, y0 + 205), "3 días", font=fs, fill=CREMA); d.text((x0 + 230, y0 + 205), "en la oficina", font=fb, fill=CREMA)
    d.text((x0 + 50, y0 + 285), "2 días", font=fs, fill=CREMA); d.text((x0 + 230, y0 + 285), "en la casa", font=fb, fill=CREMA)
    d.text((x0 + 50, y0 + 375), "«Así lo hace Frugle»", font=font("cuerpo", 36), fill=(201, 162, 77, 220))
    scr.save(CAP / "107-pantalla.png"); bg.save(CAP / "107-fondo.png")
    # Personaje: recorte a 1000 px de alto, anclado abajo a la derecha
    har = Image.open(R / "recortes" / "HAROLD.png"); har = har.crop(har.getchannel("A").getbbox())
    hh = 900; har = har.resize((int(har.width * hh / har.height), hh), Image.LANCZOS); har.save(CAP / "107-harold.png")
    subtitulo("Señores: Frugle lo hace. Netfrux lo hace. Y desde hoy, FrutiTech también: ¡el modelo tres por dos!", CAP / "107-sub.png")
    hx = W - har.width + 40
    t_scr = round(dur(a) * 0.62 + 0.4, 2)  # la pantalla aparece en "¡el modelo tres por dos!"
    vf = (f"[0:v]scale=w='trunc({W}*(1+0.04*t/{T})/2)*2':h=-2:eval=frame,crop={W}:{H}:x='{W}*0.04*t/{T}/2':y='{H}*0.04*t/{T}/2'[bg];"
          f"[2:v]format=rgba,fade=t=in:st={t_scr}:d=0.5:alpha=1[scr];"
          f"[bg][scr]overlay=x='-30*t/{T}':y=0[b2];"
          f"[1:v]scale=w='trunc(iw*(1+0.06*t/{T})/2)*2':h=-2:eval=frame[har];"
          f"[b2][har]overlay=x='{hx}-40*t/{T}':y='H-h+20':eval=frame[b3];"
          f"[b3]vignette=PI/5[b4];"
          f"[b4][3:v]overlay=0:0:enable='between(t,0.4,{T-0.3})',format=yuv420p[vo];"
          f"[4:a]adelay=400|400,apad,atrim=0:{T},afade=t=out:st={T-0.4}:d=0.4[ao]")
    run(["-loop", "1", "-framerate", str(FPS), "-t", str(T), "-i", str(CAP / "107-fondo.png"),
         "-loop", "1", "-framerate", str(FPS), "-t", str(T), "-i", str(CAP / "107-harold.png"),
         "-loop", "1", "-framerate", str(FPS), "-t", str(T), "-i", str(CAP / "107-pantalla.png"),
         "-loop", "1", "-framerate", str(FPS), "-t", str(T), "-i", str(CAP / "107-sub.png"),
         "-i", str(a), "-filter_complex", vf, "-map", "[vo]", "-map", "[ao]", "-t", str(T)] + ENC + [str(OUT / "1.07.mp4")])

# ---------- 1.26 · Decisión 1 (provisional: zoom a los ojos de Don Harold) ----------
def clip_126():
    a = AUD / "1.26.mp3"; dn = dur(a); T = round(dn + 3.2, 2); tf = round(dn + 0.6, 2)  # congelado y título
    src = Image.open(IMG / "Don Harold_ Jefe de Gestión Humana.png").convert("RGB")
    src.save(CAP / "126-big.png")
    t = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(t); f = font("titulo", 170)
    txt = "Decisión 1"; tw = d.textlength(txt, font=f)
    d.text(((W - tw) / 2, H / 2 - 130), txt, font=f, fill=DORADO, stroke_width=2, stroke_fill=NEGRO)
    fs = font("rotulo", 44); s = "¿Qué debe hacer Don Harold?"; d.text(((W - d.textlength(s, font=fs)) / 2, H / 2 + 90), s, font=fs, fill=CREMA)
    t.save(CAP / "126-titulo.png")
    BW, BH = src.size; ex, ey = 0.495, 0.26   # punto entre los ojos (fracción de la imagen)
    # zoom: la ventana visible pasa de 85 % a 40 % del ancho de la imagen, acelerando; temblor que crece; luego congelado
    zt = f"(min(t,{tf})/{tf})"
    s = f"({W}/({BW}*(0.85-0.45*pow({zt},2.2))))"          # factor de escala de la imagen en cada cuadro
    shake = f"(lt(t,{tf})*{zt}*18*(sin(t*53)+0.6*sin(t*31+1)))"
    vf = (f"[0:v]scale=w='trunc({BW}*{s}/2)*2':h='trunc({BH}*{s}/2)*2':eval=frame:flags=bicubic,"
          f"crop={W}:{H}:x='max(0,min({BW}*{s}-{W},{BW}*{s}*{ex}-{W}/2+{shake}))':y='max(0,min({BH}*{s}-{H},{BH}*{s}*{ey}-{H}/2+{shake}*0.7))',"
          f"setsar=1,"
          f"eq=saturation=0.75:contrast=1.15,colorbalance=rs=0.10:bs=0.06,vignette=PI/3.2[v];"
          f"[v]null[v2];"
          f"[1:v]format=rgba,fade=t=in:st={tf}:d=0.6:alpha=1[ti];"
          f"[v2]drawbox=c=black@0.55:t=fill:enable='gte(t,{tf})'[v3];"
          f"[v3][ti]overlay=0:0,format=yuv420p[vo];"
          f"aevalsrc='0.9*sin(2*PI*52*t)*exp(-14*mod(t,0.82))+0.6*sin(2*PI*48*t)*exp(-16*mod(t+0.6,0.82))':s=48000:d={T},"
          f"volume='0.35+0.4*t/{T}':eval=frame,pan=stereo|c0=c0|c1=c0[hb];"
          f"[2:a]adelay=300|300,apad,atrim=0:{T}[nar];[nar][hb]amix=inputs=2:duration=first:normalize=0,afade=t=out:st={T-0.5}:d=0.5[ao]")
    run(["-loop", "1", "-framerate", str(FPS), "-t", str(T), "-i", str(CAP / "126-big.png"),
         "-loop", "1", "-framerate", str(FPS), "-t", str(T), "-i", str(CAP / "126-titulo.png"),
         "-i", str(a), "-filter_complex", vf, "-map", "[vo]", "-map", "[ao]", "-t", str(T)] + ENC + [str(OUT / "1.26.mp4")])

if __name__ == "__main__":
    for fn in (clip_120, clip_107, clip_126):
        fn(); print("listo", fn.__name__)
    for f in sorted(OUT.glob("*.mp4")):
        info = json.loads(subprocess.check_output([FP, "-v", "error", "-show_entries", "stream=codec_type,width,height,r_frame_rate,channels:format=duration", "-of", "json", str(f)]))
        print(f.name, round(float(info["format"]["duration"]), 2), [(s["codec_type"], s.get("width"), s.get("height"), s.get("r_frame_rate"), s.get("channels")) for s in info["streams"]])
