"""Motor de cámara cuadro por cuadro.
- Capas (imagen o video) en un "mundo" de 1920×1080 a zoom 1, con posición, escala, giro, opacidad y paralaje animables.
- Cámara con zoom, centro, giro y temblor de cámara en mano, todo con curvas de aceleración.
- Desenfoque de movimiento automático en los movimientos rápidos.
- Respiración y vaivén suaves para que un personaje fijo no se vea congelado.
Los cuadros se envían por tubería a ffmpeg junto con el audio ya mezclado."""
import math, subprocess, shutil, glob, os
import numpy as np
from PIL import Image

W, H, FPS = 1920, 1080, 24

def tool(name):
    return shutil.which(name) or glob.glob(os.path.join(os.environ["LOCALAPPDATA"], r"Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin", name + ".exe"))[0]
FF, FP = tool("ffmpeg"), tool("ffprobe")

# ---------- curvas ----------
EASE = {
    "lineal": lambda u: u,
    "suave": lambda u: u * u * (3 - 2 * u),
    "golpe": lambda u: 1 - (1 - u) ** 4,          # arranca rápido y se asienta (golpe de zoom)
    "entra": lambda u: u ** 3,                     # arranca lento y acelera
    "sale": lambda u: 1 - (1 - u) ** 2,
}
def kf(*pts):
    """kf((t, valor), (t, valor, 'curva'), ...): la curva indica cómo se llega a ese punto."""
    return [(p[0], p[1], p[2] if len(p) > 2 else "suave") for p in pts]
def val(k, t):
    if not isinstance(k, list): return k
    if t <= k[0][0]: return k[0][1]
    for (t0, v0, _), (t1, v1, e) in zip(k, k[1:]):
        if t <= t1:
            u = (t - t0) / (t1 - t0) if t1 > t0 else 1
            return v0 + (v1 - v0) * EASE[e](u)
    return k[-1][1]

# ---------- matrices 3x3 ----------
def T_(x, y): return np.array([[1, 0, x], [0, 1, y], [0, 0, 1]], float)
def S_(s): return np.array([[s, 0, 0], [0, s, 0], [0, 0, 1]], float)
def R_(deg):
    a = math.radians(deg); c, s = math.cos(a), math.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]], float)

class Video:
    """Lee un video cuadro a cuadro (en orden) para usarlo como capa."""
    def __init__(self, path, llave=None, tol=90):
        """llave=(r,g,b): color de fondo que se vuelve transparente (p. ej. magenta en los recortes animados)."""
        info = subprocess.check_output([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", path]).decode().strip().split(",")
        self.w, self.h = int(info[0]), int(info[1]); self.llave, self.tol = llave, tol
        self.p = subprocess.Popen([FF, "-loglevel", "error", "-i", path, "-vf", f"fps={FPS}", "-f", "rawvideo", "-pix_fmt", "rgba", "-"], stdout=subprocess.PIPE)
        self.last = None; self.i = -1
    def frame(self, t):
        want = int(round(t * FPS))
        while self.i < want:
            b = self.p.stdout.read(self.w * self.h * 4)
            if len(b) < self.w * self.h * 4: break
            if self.llave is not None:
                a = np.frombuffer(b, np.uint8).reshape(self.h, self.w, 4).copy()
                dist = np.abs(a[..., :3].astype(np.int16) - np.array(self.llave, np.int16)).sum(-1)
                a[..., 3] = np.clip((dist - self.tol) * 4, 0, 255).astype(np.uint8)
                self.last = Image.fromarray(a, "RGBA")
            else:
                self.last = Image.frombuffer("RGBA", (self.w, self.h), b, "raw", "RGBA", 0, 1)
            self.i += 1
        return self.last

class Capa:
    def __init__(self, src, x=W / 2, y=H / 2, escala=1.0, rot=0.0, opac=1.0, ancla=(0.5, 0.5), fija=False, paralaje=1.0,
                 respira=0.0, vaiven=0.0, desde=0.0, hasta=1e9):
        self.src = src if isinstance(src, Video) else (src.convert("RGBA") if isinstance(src, Image.Image) else Image.open(src).convert("RGBA"))
        self.x, self.y, self.escala, self.rot, self.opac = x, y, escala, rot, opac
        self.ancla, self.fija, self.paralaje, self.respira, self.vaiven = ancla, fija, paralaje, respira, vaiven
        self.desde, self.hasta = desde, hasta
    def imagen(self, t):
        return self.src.frame(t) if isinstance(self.src, Video) else self.src
    def matriz(self, t, img, cam_dx=0.0, cam_dy=0.0):
        s = val(self.escala, t) * (1 + self.respira * math.sin(2 * math.pi * t / 3.7))
        r = val(self.rot, t) + self.vaiven * math.sin(2 * math.pi * t / 5.3 + 1.1)
        x = val(self.x, t) + (1 - self.paralaje) * cam_dx; y = val(self.y, t) + (1 - self.paralaje) * cam_dy
        return T_(x, y) @ R_(r) @ S_(s) @ T_(-self.ancla[0] * img.width, -self.ancla[1] * img.height)

class Camara:
    def __init__(self, zoom=1.0, cx=W / 2, cy=H / 2, rot=0.0, temblor=0.0):
        self.zoom, self.cx, self.cy, self.rot, self.temblor = zoom, cx, cy, rot, temblor
        self.cx0, self.cy0 = val(cx, 0), val(cy, 0)
    def estado(self, t):
        a = val(self.temblor, t)
        sx = a * (math.sin(t * 2.1) * 0.6 + math.sin(t * 5.3 + 1) * 0.3 + math.sin(t * 11.7 + 2) * 0.1)
        sy = a * (math.sin(t * 1.7 + 3) * 0.6 + math.sin(t * 4.1 + 2) * 0.3 + math.sin(t * 9.9) * 0.1)
        sr = a * 0.025 * math.sin(t * 1.3 + 0.5)
        return val(self.zoom, t), val(self.cx, t) + sx, val(self.cy, t) + sy, val(self.rot, t) + sr
    def matriz(self, t):
        z, cx, cy, r = self.estado(t)
        return T_(W / 2, H / 2) @ S_(z) @ R_(-r) @ T_(-cx, -cy), cx - self.cx0, cy - self.cy0

def _componer(t, capas, cam):
    lienzo = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    C, dx, dy = cam.matriz(t)
    for c in capas:
        if not (c.desde <= t < c.hasta): continue
        op = val(c.opac, t)
        if op <= 0.003: continue
        img = c.imagen(t)
        if img is None: continue
        M = c.matriz(t, img, dx, dy)
        if not c.fija: M = C @ M
        Mi = np.linalg.inv(M)
        capa = img.transform((W, H), Image.AFFINE, tuple(Mi[:2].ravel()), resample=Image.BICUBIC)
        if op < 0.997:
            a = capa.getchannel("A").point(lambda v, op=op: int(v * op)); capa.putalpha(a)
        lienzo.alpha_composite(capa)
    return lienzo

def _velocidad(cam, t):
    """Cuántos píxeles se mueve la imagen entre este cuadro y medio cuadro después (para el desenfoque de movimiento)."""
    a, b = cam.matriz(t)[0], cam.matriz(t + 0.5 / FPS)[0]
    pts = np.array([[0, 0, 1], [W, 0, 1], [0, H, 1], [W, H, 1], [W / 2, H / 2, 1]], float).T
    pa, pb = np.linalg.inv(a) @ pts, np.linalg.inv(b) @ pts
    return float(np.abs((a @ pb) - pts)[:2].max())

def render(T, capas, cam, audio_wav, salida, post="", crf=18):
    n = int(round(T * FPS))
    vf = "format=yuv420p" if not post else post + ",format=yuv420p"
    p = subprocess.Popen([FF, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-i", str(audio_wav), "-vf", vf, "-map", "0:v", "-map", "1:a", "-t", f"{T:.3f}",
                          "-c:v", "libx264", "-preset", "medium", "-crf", str(crf), "-pix_fmt", "yuv420p",
                          "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-movflags", "+faststart", str(salida)], stdin=subprocess.PIPE)
    for i in range(n):
        t = i / FPS
        v = _velocidad(cam, t)
        if v > 6:   # movimiento rápido: obturador de 180° con varias submuestras
            k = int(min(8, 2 + v // 8))
            acc = sum(np.asarray(_componer(t + j / k * 0.5 / FPS, capas, cam).convert("RGB"), np.float32) for j in range(k)) / k
            frame = acc.astype(np.uint8).tobytes()
        else:
            frame = _componer(t, capas, cam).convert("RGB").tobytes()
        p.stdin.write(frame)
    p.stdin.close(); p.wait()
    if p.returncode: raise RuntimeError("ffmpeg falló")
