"""Música y efectos sintetizados (sin licencias) que se ajustan a los tiempos de cada clip, y mezcla con la voz.
Todo a 48 kHz estéreo en float32 (-1..1)."""
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
rng = np.random.default_rng(7)

# ---------- utilidades ----------
def silencio(T): return np.zeros((int(T * SR), 2), np.float32)
def tt(d): return np.arange(int(d * SR)) / SR
def env(d, a=0.01, dcy=0.1, s=0.7, r=0.2):
    n = int(d * SR); e = np.full(n, s, np.float32)
    na, nd, nr = int(a * SR), int(dcy * SR), int(r * SR)
    e[:na] = np.linspace(0, 1, na) if na else e[:na]
    e[na:na + nd] = np.linspace(1, s, len(e[na:na + nd]))
    if nr: e[-nr:] *= np.linspace(1, 0, min(nr, n))
    return e
def perc(d, decay): return np.exp(-tt(d) / decay).astype(np.float32)
def saw(f, d, k=14, det=0.0):
    t = tt(d); x = np.zeros_like(t)
    for h in range(1, k + 1):
        if f * h > SR / 2.2: break
        x += np.sin(2 * np.pi * f * h * (1 + det) * t) / h
    return (x * 0.55).astype(np.float32)
def sine(f, d): return np.sin(2 * np.pi * f * tt(d)).astype(np.float32)
def lp(x, fc, o=2): return signal.sosfilt(signal.butter(o, fc, "low", fs=SR, output="sos"), x, axis=0).astype(np.float32)
def hp(x, fc, o=2): return signal.sosfilt(signal.butter(o, fc, "high", fs=SR, output="sos"), x, axis=0).astype(np.float32)
def bp(x, lo, hi): return signal.sosfilt(signal.butter(2, [lo, hi], "band", fs=SR, output="sos"), x, axis=0).astype(np.float32)
def ruido(d): return rng.standard_normal(int(d * SR)).astype(np.float32)
def st(x, pan=0.0):
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    return np.stack([x * l, x * r], 1).astype(np.float32)
def put(buf, x, t0, g=1.0):
    i = int(t0 * SR)
    if i >= len(buf): return
    x = x if x.ndim == 2 else st(x)
    n = min(len(x), len(buf) - i); buf[i:i + n] += x[:n] * g
def reverb(x, dec=1.8, wet=0.25):
    ir_t = tt(dec); ir = rng.standard_normal((len(ir_t), 2)).astype(np.float32) * np.exp(-ir_t * 4.5 / dec)[:, None]
    ir[:, 0] = lp(ir[:, 0], 6000); ir[:, 1] = lp(ir[:, 1], 6000); ir /= np.sqrt((ir ** 2).sum(0))
    w = np.stack([signal.fftconvolve(x[:, c], ir[:, c])[:len(x)] for c in (0, 1)], 1)
    return (x * (1 - wet) + w * wet).astype(np.float32)
def db(g): return 10 ** (g / 20)
N = lambda name: 440 * 2 ** ((("C C# D D# E F F# G G# A A# B".split().index(name[:-1])) - 9) / 12 + int(name[-1]) - 4)

# ---------- efectos ----------
def whoosh(d=0.5, up=True):
    n = ruido(d); a = lp(n, 1200); b = hp(n, 2500)
    k = np.linspace(0, 1, len(n)) if up else np.linspace(1, 0, len(n))
    x = a * (1 - k) + b * k
    e = np.sin(np.pi * np.linspace(0, 1, len(n))) ** 2
    return st(x * e * 0.5, 0)
def golpe(d=1.6, f0=58, f1=32):
    t = tt(d); f = f1 + (f0 - f1) * np.exp(-t * 6)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.6)
    x += lp(ruido(d), 900) * np.exp(-t * 16) * 0.6
    return st(x.astype(np.float32) * 0.9)
def latido(T, periodo=0.85, desde=0.0, hasta=None, g=0.35):
    out = silencio(T); hasta = hasta or T; t = desde
    while t < hasta:
        b = sine(52, 0.25) * perc(0.25, 0.06); put(out, b, t, g); put(out, sine(46, 0.2) * perc(0.2, 0.05), t + 0.24, g * 0.7)
        t += periodo
    return out
def ambiente_oficina(T, g=db(-44)):
    x = lp(ruido(T), 450) + 0.3 * lp(ruido(T), 120); x = np.stack([x, np.roll(x, 2400)], 1)
    return (x * g).astype(np.float32)
def pizz(f, d=0.5, g=0.5):
    x = sum(sine(f * h, d) / h ** 1.6 for h in range(1, 6)) * perc(d, 0.09)
    return lp(x, 3500) * g
def metales(freqs, d, g=0.35):
    x = sum(saw(f, d, 18, det) for f in freqs for det in (-0.003, 0.003))
    e = env(d, 0.03, 0.15, 0.75, min(0.35, d * 0.4))
    return lp(x * e, 2200) * g / len(freqs)

# ---------- pistas ----------
def pista_tension(T, tf, golpes=()):
    """Drama: bordón grave que crece, ostinato de cuerdas, subida al congelado, golpe y "tan tan taaan"."""
    out = silencio(T)
    d = tf
    dron = (saw(N("D2"), d, 10) + saw(N("A2"), d, 10, 0.002) * 0.8 + saw(N("F3"), d, 8, -0.002) * 0.45)
    dron = lp(dron, 700) * np.linspace(0.25, 0.9, len(dron)) ** 1.3 * (1 + 0.08 * np.sin(2 * np.pi * 4.5 * tt(d)))
    put(out, st(dron * 0.28, -0.15), 0)
    t, paso = 1.5, 60 / 104 / 2      # corcheas a 104 pulsos por minuto
    while t < tf - 0.1:
        k = (t / tf) ** 1.5
        put(out, st(lp(saw(N("D2"), 0.22, 12) * env(0.22, 0.005, 0.05, 0.6, 0.08), 1400) * (0.10 + 0.25 * k), 0.2), t)
        t += paso
    sub = tt(3.0); riser = hp(ruido(3.0), 1500) * (sub / 3) ** 3 * 0.25 + np.sin(2 * np.pi * np.cumsum(200 + 1000 * (sub / 3) ** 2) / SR) * (sub / 3) ** 2 * 0.06
    put(out, st(riser.astype(np.float32)), tf - 3.0)
    for g in golpes: put(out, golpe(1.4), g, 0.6); put(out, whoosh(0.35), g - 0.33, 0.7)
    put(out, golpe(2.2, 62, 28), tf, 1.0)
    for i, (n, dur) in enumerate((("A3", 0.26), ("G#3", 0.26), ("E3", 1.7))):
        put(out, st(metales([N(n), N(n) / 2], dur, 0.55)), tf + 0.12 + 0.3 * i)
    return reverb(out, 2.2, 0.28)

def pista_showman(T, golpes=(), final=None):
    """Comedia corporativa: bajo saltarín, pizzicato y un golpe de metales en el remate."""
    out = silencio(T); beat = 60 / 126
    bajo = ["C2", "C2", "G2", "A2", "F2", "F2", "G2", "G2"]; acordes = [("E4", "G4", "C5"), ("D4", "F4", "B4")]
    i, t = 0, 0.0
    while t < (final or T) - 0.05:
        put(out, st(pizz(N(bajo[i % 8]), 0.45, 0.55), -0.2), t)
        if i % 2 == 1:
            for n in acordes[(i // 4) % 2]: put(out, st(pizz(N(n), 0.3, 0.13), 0.35), t)
        put(out, st(hp(ruido(0.06), 7000) * perc(0.06, 0.012) * 0.10, 0.5), t + beat / 2)
        t += beat; i += 1
    for g in golpes: put(out, st(pizz(N("G4"), 0.3, 0.35)), g)
    if final is not None:
        put(out, st(metales([N("C4"), N("E4"), N("G4"), N("C3")], 1.2, 0.7)), final)
        put(out, st(hp(ruido(1.5), 4000) * perc(1.5, 0.35) * 0.18, 0.2), final)
    return reverb(out, 1.4, 0.18)

def pista_confesionario(T, golpe_t=None, remate=None):
    """Confesionario de comedia: cuarto en silencio, pasos de bajo tímidos y un "ta-tán" al final."""
    out = ambiente_oficina(T) * 1.0
    t = 0.3
    while t < (remate or T) - 0.3:
        put(out, st(pizz(N("E2"), 0.35, 0.16)), t); t += 1.2
    if golpe_t is not None: put(out, whoosh(0.3), golpe_t - 0.28, 0.5)
    if remate is not None:
        put(out, st(pizz(N("G3"), 0.35, 0.5)), remate); put(out, st(pizz(N("C3"), 0.9, 0.6)), remate + 0.28)
    return reverb(out, 1.2, 0.15)

# ---------- mezcla ----------
def leer(path):
    sr, x = wavfile.read(path); x = x.astype(np.float32) / (32768 if x.dtype == np.int16 else 1)
    if x.ndim == 1: x = np.stack([x, x], 1)
    assert sr == SR, sr
    return x
def mezclar(T, voz_wav, voz_ini, pistas, out_wav, musica_db=-17, ducking_db=-9):
    voz = silencio(T); put(voz, leer(voz_wav), voz_ini)
    mus = sum(pistas) if pistas else silencio(T)
    envv = np.abs(voz[:, 0]); envv = signal.sosfilt(signal.butter(1, 4, fs=SR, output="sos"), envv)
    k = np.clip(envv / 0.03, 0, 1)
    gain = db(musica_db) * (1 - k * (1 - db(ducking_db)))
    mix = voz + mus * gain[:, None]
    fade = int(0.25 * SR); mix[-fade:] *= np.linspace(1, 0, fade)[:, None]
    mix *= min(1.0, db(-1) / max(1e-6, np.abs(mix).max()))
    wavfile.write(out_wav, SR, (mix * 32767).astype(np.int16))
