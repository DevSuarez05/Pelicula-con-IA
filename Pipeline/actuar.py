"""Voz actuada: cada frase con su propio tono, velocidad y volumen, y pausas dramáticas medidas entre frases.
(edge-tts no acepta SSML propio; esto logra el mismo efecto que <prosody> y <break> por frase.)

Uso:  python actuar.py actuaciones/1.20.json salida.wav [--voz es-MX-JorgeNeural]

Formato de la actuación (JSON):
{ "personaje": "HAROLD",
  "frases": [ {"t": "¿Yo?", "rate": "-5%", "pitch": "+25Hz", "vol": "+10%", "pausa": 350}, ... ] }
rate/pitch/vol se suman al ajuste base del personaje en voces.json. pausa = silencio después de la frase, en ms.
"""
import asyncio, json, sys, pathlib, subprocess, tempfile, shutil, glob, os, re
import edge_tts

R = pathlib.Path(__file__).parent
VOCES = json.loads((R / "voces.json").read_text(encoding="utf-8"))

def tool(name):
    return shutil.which(name) or glob.glob(os.path.join(os.environ["LOCALAPPDATA"], r"Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin", name + ".exe"))[0]
FF = tool("ffmpeg")

def suma(base, extra, unidad):
    n = lambda s: float(re.sub(r"[^\d.\-+]", "", s or "0") or 0)
    v = n(base) + n(extra)
    return f"{'+' if v >= 0 else ''}{int(round(v))}{unidad}"

async def frase(texto, voz, rate, pitch, vol, out):
    minimo = len(texto) * 250
    for _ in range(4):
        await edge_tts.Communicate(texto, voz, rate=rate, pitch=pitch, volume=vol).save(out)
        if pathlib.Path(out).stat().st_size >= minimo: return
    print("AVISO: frase posiblemente cortada:", texto)

# Cadena de efectos: quita graves sobrantes, comprime como en doblaje, da presencia y un cuarto pequeño; volumen -16 LUFS
FX = ("highpass=f=75,acompressor=threshold=0.08:ratio=3:attack=8:release=180:makeup=2,"
      "equalizer=f=180:t=q:w=1:g=2,equalizer=f=3200:t=q:w=1.2:g=3,"
      "aecho=0.85:0.6:28|47:0.10|0.06,loudnorm=I=-16:TP=-1.5:LRA=9,aresample=48000")

async def actuar(spec, out, voz=None):
    p = VOCES[spec["personaje"]]; voz = voz or p["voz"]
    tmp = pathlib.Path(tempfile.mkdtemp())
    partes = []
    for i, f in enumerate(spec["frases"]):
        mp3 = tmp / f"{i}.mp3"
        await frase(f["t"], voz, suma(p["rate"], f.get("rate"), "%"), suma(p["pitch"], f.get("pitch"), "Hz"), suma("+0%", f.get("vol"), "%"), mp3)
        partes.append((mp3, f.get("pausa", 250)))
    # recorta el silencio de cada frase, mide su duración y arma la línea con las pausas medidas
    TRIM = "silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.03"
    tiempos, t0, lista = [], 0.0, tmp / "lista.txt"
    with open(lista, "w", encoding="utf-8") as L:
        for i, (mp3, pausa) in enumerate(partes):
            wav = tmp / f"{i}.wav"
            subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(mp3), "-af",
                            f"aresample=48000,aformat=channel_layouts=mono,{TRIM},areverse,{TRIM},areverse,apad=pad_dur={pausa/1000}",
                            "-c:a", "pcm_s16le", str(wav)], check=True)
            d = (wav.stat().st_size - 44) / (48000 * 2)
            tiempos.append({"t": spec["frases"][i]["t"], "ini": round(t0, 3), "fin": round(t0 + d - pausa / 1000, 3)})
            t0 += d; L.write(f"file '{wav.as_posix()}'\n")
    subprocess.run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lista), "-af",
                    f"{FX},pan=stereo|c0=c0|c1=c0", "-c:a", "pcm_s16le", str(out)], check=True)
    pathlib.Path(out).with_suffix(".json").write_text(json.dumps({"voz": voz, "dur": round(t0, 3), "frases": tiempos}, ensure_ascii=False, indent=1), encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    a = sys.argv[1:]; voz = None
    if "--voz" in a: i = a.index("--voz"); voz = a[i + 1]; del a[i:i + 2]
    asyncio.run(actuar(json.loads(pathlib.Path(a[0]).read_text(encoding="utf-8")), a[1], voz))
