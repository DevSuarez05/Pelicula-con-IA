"""Transcribe el audio de los clips de Grok para revisar que digan la línea del guion.
Uso: python transcribir.py CARPETA [modelo]   (modelo por defecto: small)"""
import sys, glob, os, re, subprocess
import numpy as np
from camara import FF
from faster_whisper import WhisperModel

carpeta = sys.argv[1]; modelo = sys.argv[2] if len(sys.argv) > 2 else "small"
m = WhisperModel(modelo, device="cpu", compute_type="int8")
for f in sorted(glob.glob(os.path.join(carpeta, "*.mp4")), key=lambda p: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", os.path.basename(p))]):
    pcm = subprocess.run([FF, "-v", "error", "-i", f, "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
    segs, _ = m.transcribe(audio, language="es", vad_filter=False, beam_size=5)
    texto = " ".join(f"[{s.start:.1f}-{s.end:.1f}] {s.text.strip()}" for s in segs)
    print(f"{os.path.basename(f)}: {texto or '(sin voz)'}", flush=True)
