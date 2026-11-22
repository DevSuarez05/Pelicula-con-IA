"""Intro tipo telenovela: póster con créditos y título, y luego C1-C4 + Don Lulo con su letrero.
Uso: python intro.py [CARPETA_C]   (carpeta con C1-C4; por defecto F6, los clips fuera de la oficina)
Fondo: Produccion/fotogramas/F5/INTRO.mp4 (clip de Grok con música) si existe;
       si no, Escenas/Tanda 5/INTRO.png con acercamiento lento y música provisional.
Salida: Produccion/con-voz/INTRO.mp4"""
import subprocess, pathlib, sys
import numpy as np
from scipy.io import wavfile
from PIL import Image, ImageDraw, ImageFont
from camara import FF, FP
import sonido as S
from armar import ENC, VF

P = pathlib.Path(__file__).parent; R = P.parent
TMP = P / "tmp_intro"; TMP.mkdir(exist_ok=True)
OUT = R / "Produccion/con-voz/INTRO.mp4"
F1 = R / "Produccion/fotogramas/F1"
CLIP_GROK = R / "Produccion/fotogramas/F5/INTRO.mp4"
POSTER = R / "Escenas/Tanda 5/INTRO.png"
LULO = R / "Imagenes/Don Lulo en la oficina frutera.png"
PLAY = str(P / "fuentes/PlayfairDisplay-Italic.ttf"); MONT = str(P / "fuentes/Montserrat.ttf")
CREMA = (245, 239, 227); ORO = (232, 190, 110)
T_POSTER = 17.0

def dur(f):
    return float(subprocess.run([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)],
                                capture_output=True, text=True).stdout)

def fuente(path, size, peso=None):
    f = ImageFont.truetype(path, size)
    if peso:
        try: f.set_variation_by_axes([peso])
        except Exception: pass
    return f

def lineas(png, items, oscuro=0, y0=None):
    """items: (texto, fuente, color, espacio_despues). Centrado horizontal; bloque centrado en y0 o en pantalla."""
    img = Image.new("RGBA", (1920, 1080), (0, 0, 0, oscuro)); d = ImageDraw.Draw(img)
    alto_de = lambda f: f.getmetrics()[0] + f.getmetrics()[1]
    alto = sum(alto_de(f) + esp for _, f, _, esp in items)
    y = (y0 if y0 is not None else (1080 - alto) / 2)
    for texto, f, color, esp in items:
        w = d.textlength(texto, font=f)
        d.text(((1920 - w) / 2 + 3, y + 3), texto, font=f, fill=(0, 0, 0, 220))
        d.text(((1920 - w) / 2, y), texto, font=f, fill=color + (255,))
        y += alto_de(f) + esp
    img.save(png)

def letrero(png, nombre, frase):
    """Letrero inferior izquierdo de telenovela."""
    img = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    fn, ff = fuente(PLAY, 92), fuente(MONT, 40, 500)
    w = max(d.textlength(nombre, font=fn), d.textlength(frase, font=ff)) + 140
    for x in range(int(w)):  # banda que se desvanece hacia la derecha
        a = int(190 * min(1, (w - x) / 260))
        d.line([(x, 820), (x, 1000)], fill=(20, 12, 8, a))
    d.line([(80, 935), (min(w - 120, 80 + d.textlength(nombre, font=fn)), 935)], fill=ORO + (255,), width=3)
    d.text((80, 825), nombre, font=fn, fill=CREMA + (255,))
    d.text((82, 948), frase, font=ff, fill=ORO + (255,))
    img.save(png)

def musica_provisional(T, wav):
    """Tema de telenovela sintetizado (solo mientras llega el clip de Grok con música)."""
    out = S.silencio(T)
    acordes = (("A2", "E3", "A3", "C4"), ("F2", "C3", "A3", "F4"), ("C3", "G3", "C4", "E4"), ("E2", "B2", "G#3", "E4"))
    for i in range(int(T // 2.2) + 1):
        t0 = 0.4 + i * 2.2
        if t0 > T - 0.5: break
        d = min(2.4, T - t0)
        for j, n in enumerate(acordes[i % 4]):
            x = S.lp(S.saw(S.N(n), d, 8, 0.003), 1400) * S.env(d, 0.3, 0.3, 0.8, 0.6)
            S.put(out, S.st(x * 0.06, -0.4 + 0.27 * j), t0)
        S.put(out, S.st(S.pizz(S.N(acordes[i % 4][0]) / 2, 0.6, 0.5)), t0)
    for t in (0.2, 11.4):
        S.put(out, S.golpe(2.0, 60, 30), t, 0.8)
        for k, (n, dd) in enumerate((("D4", 0.3), ("C#4", 0.3), ("A3", 2.4))):
            S.put(out, S.st(S.metales([S.N(n), S.N(n) / 2, S.N(n) * 1.5], dd, 0.5)), t + 0.1 + 0.32 * k)
    out = S.reverb(out, 2.4, 0.3)
    out *= 0.5 / max(1e-6, np.abs(out).max())
    fade = np.linspace(1, 0, int(1.5 * S.SR))[:, None]; out[-len(fade):] *= fade
    wavfile.write(wav, S.SR, out.astype(np.float32))

def poster(out):
    # tarjetas: (png, inicio, fin)
    fp_mid = fuente(PLAY, 76)
    fm, fm_s = fuente(MONT, 50, 500), fuente(MONT, 38, 400)
    lineas(TMP / "t1.png", [("Universidad Nacional de Colombia", fuente(PLAY, 96), CREMA, 10), ("Sede Manizales", fm, ORO, 60),
                            ("presenta", fuente(PLAY, 64), CREMA, 0)], oscuro=200)
    lineas(TMP / "t2.png", [("Una frutinovela de", fuente(PLAY, 60), ORO, 40),
                            ("Daniel Andrés Suárez Ramírez", fp_mid, CREMA, 4), ("creador de la trama", fm_s, ORO, 34),
                            ("Harold Yamid Arango", fp_mid, CREMA, 22), ("Valentina Constain", fp_mid, CREMA, 56),
                            ("Profesor  ·  Carlos Mario Tabares", fm, ORO, 0)], oscuro=210)
    lineas(TMP / "t3.png", [("Corazón de Pulpa", fuente(PLAY, 140), CREMA, 0), ("¿Duplicar o Adaptar?", fuente(MONT, 54, 600), ORO, 0)], y0=8)
    cards = [(TMP / "t1.png", 1.5, 5.6), (TMP / "t2.png", 6.0, 11.2), (TMP / "t3.png", 11.6, T_POSTER)]

    if CLIP_GROK.exists():
        fondo = ["-i", str(CLIP_GROK)]; v0 = f"[0:v:0]{VF},trim=0:{T_POSTER},setpts=PTS-STARTPTS"
        audio = ["-map", "0:a:0"]; af = f"atrim=0:{T_POSTER},afade=out:st={T_POSTER - 1.5}:d=1.5,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000"
        extra = 0
    else:
        musica_provisional(T_POSTER, TMP / "musica.wav")
        n = int(T_POSTER * 24)
        fondo = ["-loop", "1", "-i", str(POSTER), "-i", str(TMP / "musica.wav")]
        v0 = (f"[0:v]scale=3840:-2,zoompan=z='1.0+0.08*on/{n}':x='iw/2-(iw/zoom/2)':y=0:d={n}:s=1920x1080:fps=24,"
              f"trim=0:{T_POSTER},setpts=PTS-STARTPTS,format=yuv420p")
        audio = ["-map", "1:a"]; af = "aresample=48000"
        extra = 1
    entradas = fondo[:]
    filt = [v0 + f",fade=in:st=0:d=1.5[b0]"]
    for i, (png, a, b) in enumerate(cards):
        entradas += ["-loop", "1", "-t", str(T_POSTER), "-i", str(png)]
        k = i + 1 + extra
        fin = f",fade=out:st={b - 0.5}:d=0.5:alpha=1" if b < T_POSTER else ""
        filt.append(f"[{k}:v]format=rgba,fade=in:st={a}:d=0.6:alpha=1{fin}[c{i}]")
        filt.append(f"[b{i}][c{i}]overlay=0:0:enable='between(t,{a},{b})'[b{i + 1}]")
    filt.append(f"[b{len(cards)}]format=yuv420p,setsar=1[v]")
    subprocess.run([FF, "-y", "-v", "error", *entradas, "-filter_complex", ";".join(filt), "-map", "[v]", *audio,
                    "-af", af, "-t", str(T_POSTER), "-r", "24", *ENC, str(out)], check=True)

def con_letrero(src, nombre, frase, out):
    letrero(TMP / "l.png", nombre, frase); D = dur(src)
    filt = (f"[0:v:0]{VF}[v0];[1:v]format=rgba,fade=in:st=0.7:d=0.5:alpha=1,fade=out:st={D - 1.0}:d=0.5:alpha=1[l];"
            f"[v0][l]overlay=0:0:shortest=1,format=yuv420p[v]")
    subprocess.run([FF, "-y", "-v", "error", "-i", str(src), "-loop", "1", "-i", str(TMP / "l.png"), "-filter_complex", filt,
                    "-map", "[v]", "-map", "0:a:0", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000",
                    "-t", str(D), *ENC, str(out)], check=True)

def lulo(out, T=5.0):
    letrero(TMP / "l.png", "Don Lulo", "Veinte años en la planta"); n = int(T * 24)
    w = TMP / "lulo.wav"; x = S.silencio(T); S.put(x, S.golpe(1.6, 60, 30), 0.1, 0.6)
    for k, (nn, dd) in enumerate((("D4", 0.3), ("C#4", 0.3), ("A3", 2.4))):
        S.put(x, S.st(S.metales([S.N(nn), S.N(nn) / 2, S.N(nn) * 1.5], dd, 0.5)), 0.2 + 0.32 * k)
    x = S.reverb(x, 2.2, 0.3); x *= 0.45 / max(1e-6, np.abs(x).max()); wavfile.write(w, S.SR, x.astype(np.float32))
    filt = (f"[0:v]scale=3840:-2,crop=3840:2160,zoompan=z='1.0+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1920x1080:fps=24,"
            f"trim=0:{T},setpts=PTS-STARTPTS[b];[2:v]format=rgba,fade=in:st=0.5:d=0.5:alpha=1,fade=out:st={T - 0.9}:d=0.5:alpha=1[l];"
            f"[b][l]overlay=0:0,fade=out:st={T - 0.4}:d=0.4,format=yuv420p,setsar=1[v]")
    subprocess.run([FF, "-y", "-v", "error", "-loop", "1", "-i", str(LULO), "-i", str(w), "-loop", "1", "-i", str(TMP / "l.png"),
                    "-filter_complex", filt, "-map", "[v]", "-map", "1:a", "-af", "aresample=48000", "-t", str(T), "-r", "24",
                    *ENC, str(out)], check=True)

if __name__ == "__main__":
    CDIR = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else R / "Produccion/fotogramas/F6"
    partes = [TMP / f"{i}.mp4" for i in range(6)]
    poster(partes[0]); print("póster", "(clip de Grok)" if CLIP_GROK.exists() else "(imagen + música provisional)")
    for p, (cid, nombre, frase) in zip(partes[1:5], [
            ("C1", "Don Harold", "El gerente que todo lo copia"),
            ("C2", "Valentina", "La estratega que pide diagnóstico"),
            ("C3", "Daniel", "El analista que solo quiere preguntar"),
            ("C4", "La Piña", "El profesor que llega a su debido tiempo")]):
        con_letrero(CDIR / f"{cid}.mp4", nombre, frase, p)
    lulo(partes[5])
    lista = TMP / "lista.txt"; lista.write_text("".join(f"file '{p.as_posix()}'\n" for p in partes), encoding="utf-8")
    subprocess.run([FF, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lista), "-c", "copy", "-movflags", "+faststart", str(OUT)], check=True)
    print("listo", OUT, round(dur(OUT), 2), "s")
