"""Pone voz, música y ambiente a los clips de Grok y los deja en 1920x1080.
Uso: python voz_clips.py            (todos los clips de CLIPS que existan)
     python voz_clips.py P1 P3      (solo esos)
Entrada:  Produccion/fotogramas/F1/<ID>.mp4   (o Produccion/grok/<ID>.mp4)
Salida:   Produccion/con-voz/<ID>.mp4 y Produccion/con-voz/PROLOGO-prueba.mp4"""
import json, sys, subprocess, pathlib
import numpy as np
from scipy.io import wavfile
from PIL import Image, ImageDraw, ImageFont
from camara import FF, FP
import sonido as S

P = pathlib.Path(__file__).parent; R = P.parent
ENTRADAS = [R / "Produccion/fotogramas/F1", R / "Produccion/grok"]
OUT = R / "Produccion/con-voz"; OUT.mkdir(exist_ok=True)
TMP = P / "tmp_voz"; TMP.mkdir(exist_ok=True)

# ---------- música ----------
def pad_frio(T, g=0.22):
    """Acorde menor sostenido, frío y triste (gala vacía)."""
    out = S.silencio(T)
    for n, pan in (("A2", -0.3), ("E3", 0.3), ("C4", -0.1), ("G4", 0.2)):
        x = S.lp(S.saw(S.N(n), T, 8, 0.002), 900) * S.env(T, 1.5, 0.5, 0.9, 1.5)
        S.put(out, S.st(x * g / 4, pan), 0)
    return S.reverb(out, 3.0, 0.4)

def campanita(T, t0=0.4, g=0.12):
    """Notas sueltas de celesta: tristeza navideña."""
    out = S.silencio(T)
    for i, n in enumerate(("E5", "C5", "A4", "B4")):
        f = S.N(n); x = (S.sine(f, 1.6) + 0.3 * S.sine(f * 2, 1.6)) * S.perc(1.6, 0.5)
        S.put(out, S.st(x * g, -0.3 + 0.2 * i), t0 + i * 1.3)
    return S.reverb(out, 2.5, 0.45)

def sting_telenovela(T, t0=0.2):
    out = S.silencio(T)
    S.put(out, S.golpe(2.0, 60, 30), t0, 0.8)
    for i, (n, d) in enumerate((("D4", 0.3), ("C#4", 0.3), ("A3", 2.4))):
        S.put(out, S.st(S.metales([S.N(n), S.N(n) / 2, S.N(n) * 1.5], d, 0.6)), t0 + 0.1 + 0.32 * i)
    return S.reverb(out, 2.2, 0.3)

def multitud(T, g=S.db(-34)):
    x = S.bp(S.ruido(T), 250, 2500); x = np.stack([x, np.roll(x, 3000)], 1)
    return (x * g).astype(np.float32)

# ---------- clips ----------
# voz: (personaje, frases, inicio_s); grok_db: volumen del audio original de Grok (None = silenciado)
CLIPS = {
 "P1": dict(voz=("NARRADOR", [
            {"t": "Diciembre.", "rate": "-10%", "pitch": "-4Hz", "pausa": 700},
            {"t": "FrutiTech tenía la fiesta más moderna de su historia...", "pausa": 650},
            {"t": "y nadie quería estar ahí.", "rate": "-18%", "pitch": "-8Hz", "pausa": 0}], 1.0),
            grok_db=+6, musica=lambda T: pad_frio(T) + campanita(T, 0.6), musica_db=-14),
 "P2": dict(voz=("NARRADOR", [
            {"t": "Y Daniel...", "rate": "-12%", "pausa": 500},
            {"t": "llevaba semanas cargando ese sobre.", "rate": "-10%", "pitch": "-6Hz", "pausa": 0}], 0.8),
            grok_db=+6, musica=lambda T: pad_frio(T), musica_db=-15),
 "P3": dict(voz=("HAROLD", [
            {"t": "¡Así lo hace Frúgol!", "rate": "-30%", "pitch": "+24Hz", "vol": "+20%", "pausa": 0}], 0.7),
            grok_db=None, musica=lambda T: multitud(T) + S.silencio(T), musica_db=-6, golpe=3.0),
 "C1": dict(voz=("NARRADOR", [
            {"t": "Don Harold.", "rate": "-8%", "pitch": "-6Hz", "pausa": 350},
            {"t": "El fan número uno de Frúgol.", "rate": "+2%", "pitch": "+4Hz", "pausa": 0}], 0.5),
            grok_db=0, musica=lambda T: sting_telenovela(T, 0.0), musica_db=-12),
}

def dur(path):
    return float(subprocess.check_output([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]))

def buscar(id_):
    for d in ENTRADAS:
        if (d / f"{id_}.mp4").exists(): return d / f"{id_}.mp4"

def voz(id_, personaje, frases):
    spec = TMP / f"{id_}.json"; wav = TMP / f"{id_}-voz.wav"
    spec.write_text(json.dumps({"personaje": personaje, "frases": frases}, ensure_ascii=False), encoding="utf-8")
    subprocess.run([sys.executable, str(P / "actuar.py"), str(spec), str(wav)], check=True, cwd=P)
    return wav

def audio_grok(src, T, gain_db):
    wav = TMP / "grok.wav"
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(src), "-vn", "-ac", "2", "-ar", str(S.SR), "-t", f"{T}", str(wav)], check=True)
    x = S.leer(wav); out = S.silencio(T); S.put(out, x[:len(out)], 0)
    return out * S.db(gain_db)

def hacer(id_):
    src = buscar(id_); c = CLIPS[id_]
    if not src: print("falta", id_); return None
    T = round(dur(src), 3)
    per, frases, ini = c["voz"]; vw = voz(id_, per, frases)
    vd = S.leer(vw).shape[0] / S.SR
    if ini + vd > T - 0.2: print(f"  ¡ojo! la voz de {id_} dura {vd:.1f}s y no cabe desde {ini}s")
    pistas = [c["musica"](T)]
    if c.get("golpe"): g = S.silencio(T); S.put(g, S.golpe(1.5), c["golpe"], 0.7); pistas.append(g * S.db(10))
    mezcla = TMP / f"{id_}-mezcla.wav"
    S.mezclar(T, vw, ini, pistas, mezcla, musica_db=c["musica_db"], ducking_db=-8)
    if c["grok_db"] is not None:   # ambiente original de Grok por debajo, sin ducking
        m = S.leer(mezcla) + audio_grok(src, T, c["grok_db"])[:len(S.leer(mezcla))]
        m *= min(1.0, S.db(-1) / max(1e-6, np.abs(m).max()))
        wavfile.write(mezcla, S.SR, (m * 32767).astype(np.int16))
    out = OUT / f"{id_}.mp4"
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(src), "-i", str(mezcla), "-map", "0:v:0", "-map", "1:a",
                    "-vf", "scale=1920:1094:flags=lanczos,crop=1920:1080,fps=24,format=yuv420p",
                    "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-t", f"{T}", "-movflags", "+faststart", str(out)], check=True)
    print("listo", out.name, f"{T:.1f}s")
    return out

def titulo(texto, T, voz_frases):
    """Tarjeta 'Tres meses antes…' con el narrador."""
    img = Image.new("RGB", (1920, 1080), (26, 20, 16)); d = ImageDraw.Draw(img)
    f = ImageFont.truetype(str(P / "fuentes/PlayfairDisplay-Italic.ttf"), 110)
    w = d.textlength(texto, font=f); d.text(((1920 - w) / 2, 470), texto, font=f, fill=(245, 239, 227))
    png = TMP / "titulo.png"; img.save(png)
    vw = voz("P4", "NARRADOR", voz_frases); mezcla = TMP / "P4-mezcla.wav"
    S.mezclar(T, vw, 0.8, [pad_frio(T, 0.15)], mezcla, musica_db=-16)
    out = OUT / "P4.mp4"
    subprocess.run([FF, "-y", "-loglevel", "error", "-loop", "1", "-i", str(png), "-i", str(mezcla), "-t", f"{T}",
                    "-vf", f"fade=in:st=0:d=0.8,fade=out:st={T - 0.8}:d=0.8,format=yuv420p", "-r", "24",
                    "-c:v", "libx264", "-crf", "17", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                    "-movflags", "+faststart", str(out)], check=True)
    return out

if __name__ == "__main__":
    ids = sys.argv[1:] or list(CLIPS)
    hechos = {i: hacer(i) for i in ids}
    if not sys.argv[1:]:
        p4 = titulo("Tres meses antes…", 4.0, [{"t": "Tres meses antes...", "rate": "-16%", "pitch": "-8Hz", "pausa": 0}])
        orden = [hechos.get("P1"), hechos.get("P2"), hechos.get("P3"), p4, hechos.get("C1")]
        lista = TMP / "lista.txt"
        lista.write_text("".join(f"file '{p.as_posix()}'\n" for p in orden if p), encoding="utf-8")
        subprocess.run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lista),
                        "-c:v", "libx264", "-crf", "17", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
                        str(OUT / "PROLOGO-prueba.mp4")], check=True)
        print("listo PROLOGO-prueba.mp4", f"{dur(OUT / 'PROLOGO-prueba.mp4'):.1f}s")
