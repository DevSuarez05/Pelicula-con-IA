"""Recorta un personaje de su imagen original. Uso: python recortar.py entrada.png salida.png [corte_inferior]
corte_inferior (0-1): fracción de altura desde la que se descarta (el escritorio)."""
import sys, numpy as np
from PIL import Image, ImageFilter
from rembg import remove, new_session
from scipy import ndimage
src, out = sys.argv[1], sys.argv[2]
corte = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
im = Image.open(src).convert("RGB")
a = np.array(remove(im, session=new_session("isnet-general-use"), only_mask=True)).astype(np.float32)
m = a > 25                                   # silueta
m = ndimage.binary_closing(m, iterations=6)
m = ndimage.binary_fill_holes(m)             # rellena camisa negra y manos semitransparentes
lab, n = ndimage.label(m)                    # solo la pieza más grande (el personaje)
if n > 1:
    sizes = ndimage.sum(m, lab, range(1, n + 1)); m = lab == (np.argmax(sizes) + 1)
inner = ndimage.binary_erosion(m, iterations=3)
alpha = np.maximum(a, inner * 255.0) * m
h = alpha.shape[0]; cut = int(h * corte)
if cut < h:                                  # desvanece el borde inferior en 40 px
    alpha[cut:] = 0
    ramp = np.linspace(1, 0, 40)[:, None]; alpha[cut-40:cut] *= ramp
rgba = im.convert("RGBA"); rgba.putalpha(Image.fromarray(alpha.clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8)))
rgba.save(out); print(out, rgba.getchannel("A").getbbox())
