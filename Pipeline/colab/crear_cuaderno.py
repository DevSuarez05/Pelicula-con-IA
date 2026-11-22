"""Crea los dos cuadernos de Colab y el paquete entrada.zip.
  sadtalker.ipynb    → anima boca, ojos y cabeza a partir de la IMAGEN + el AUDIO (voz edge-tts actuada).
  liveportrait.ipynb → copia la actuación de una persona real a partir de la IMAGEN + un VIDEO grabado con el celular.
Uso: python crear_cuaderno.py [FILA ...]   (por defecto: 1.20 1.07)"""
import json, sys, pathlib, zipfile, shutil, subprocess
from PIL import Image
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from camara import FF

R = pathlib.Path(__file__).parent; P = R.parent
filas = sys.argv[1:] or ["1.20", "1.07"]

def md(*l): return {"cell_type": "markdown", "metadata": {}, "source": "\n".join(l)}
def code(*l): return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": "\n".join(l)}
def guardar(nombre, cells):
    nb = {"cells": cells, "metadata": {"accelerator": "GPU", "colab": {"gpuType": "T4", "provenance": []},
          "kernelspec": {"name": "python3", "display_name": "Python 3"}}, "nbformat": 4, "nbformat_minor": 0}
    (R / nombre).write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")

SUBIR = [code("# Subir entrada.zip",
              "from google.colab import files",
              "import zipfile, os, shutil",
              "shutil.rmtree('/content/entrada', ignore_errors=True)",
              "up = files.upload()",
              "for n in up: zipfile.ZipFile(n).extractall('/content/entrada')",
              "print(sorted(os.listdir('/content/entrada')))")]
BAJAR = [code("# Descargar salida.zip",
              "!cd /content/salida && zip -q -r /content/salida.zip . && ls -la /content/salida",
              "from google.colab import files",
              "files.download('/content/salida.zip')")]

# ---------------- SadTalker ----------------
guardar("sadtalker.ipynb", [
md("# Corazón de Pulpa · Caras que hablan con SadTalker (imagen + audio)",
   "",
   "1. **Entorno de ejecución → Cambiar tipo de entorno → GPU T4 → Guardar.**",
   "2. **Entorno de ejecución → Ejecutar todo.**",
   "3. Cuando salga **Elegir archivos**, suban `entrada.zip`.",
   "4. Al final se descarga `salida.zip`. Pónganlo en `Pipeline/colab/` y avísenle a Claude.",
   "",
   "La instalación tarda unos 10 minutos; después, 1 o 2 minutos por clip. Si una celda muestra un error, cópienlo completo y péguenlo en el chat."),
code("# 1. GPU", "!nvidia-smi --query-gpu=name,memory.total --format=csv"),
code("# 2. Instalar SadTalker con arreglos para las versiones actuales de Colab",
     "%cd /content",
     "!rm -rf SadTalker && git clone -q https://github.com/OpenTalker/SadTalker.git",
     "%cd /content/SadTalker",
     "!pip -q install face_alignment==1.3.5 yacs pydub kornia gfpgan basicsr facexlib safetensors imageio-ffmpeg librosa",
     "!sed -i 's/from torchvision.transforms.functional_tensor import rgb_to_grayscale/from torchvision.transforms.functional import rgb_to_grayscale/' $(python -c 'import basicsr,os;print(os.path.dirname(basicsr.__file__))')/data/degradations.py",
     "!grep -rl 'np\\.float\\b' src | xargs -r sed -i 's/np\\.float\\b/float/g'",
     "!sed -i 's/np.array(\\[w0, h0, s, t\\[0\\], t\\[1\\]\\])/np.array([w0, h0, s, float(t[0]), float(t[1])])/' src/face3d/util/preprocess.py",
     "!sed -i 's/warnings.filterwarnings(\"ignore\", category=np.VisibleDeprecationWarning)//' src/face3d/util/preprocess.py",
     "!sed -i 's/librosa.filters.mel(hp.sample_rate, hp.n_fft,/librosa.filters.mel(sr=hp.sample_rate, n_fft=hp.n_fft,/' src/utils/audio.py",
     "!bash scripts/download_models.sh > /dev/null 2>&1; ls checkpoints gfpgan/weights"),
*SUBIR,
code("# 4. Animar: --still y --preprocess full conservan la imagen completa; expression_scale da más gesto",
     "import glob, subprocess, os, shutil",
     "os.makedirs('/content/salida', exist_ok=True)",
     "for img in sorted(glob.glob('/content/entrada/*.png')):",
     "    fila = os.path.basename(img)[:-4]; wav = f'/content/entrada/{fila}.wav'",
     "    if not os.path.exists(wav): print('sin audio:', fila); continue",
     "    for modo, extra in (('still', ['--still']), ('vivo', [])):     # dos versiones: cabeza quieta y cabeza con más movimiento",
     "        out = f'/content/tmp/{fila}-{modo}'; shutil.rmtree(out, ignore_errors=True)",
     "        print('animando', fila, modo)",
     "        r = subprocess.run(['python', 'inference.py', '--driven_audio', wav, '--source_image', img, '--result_dir', out,",
     "                            '--preprocess', 'full', '--enhancer', 'gfpgan', '--expression_scale', '1.3'] + extra,",
     "                           capture_output=True, text=True)",
     "        vids = glob.glob(out + '/**/*.mp4', recursive=True)",
     "        if vids: shutil.copy(max(vids, key=os.path.getsize), f'/content/salida/{fila}-{modo}.mp4'); print('  listo')",
     "        else: print('  ERROR\\n', r.stdout[-1500:], r.stderr[-3000:])"),
*BAJAR])

# ---------------- LivePortrait ----------------
guardar("liveportrait.ipynb", [
md("# Corazón de Pulpa · Actuación real con LivePortrait (imagen + video del celular)",
   "",
   "LivePortrait copia en Don Harold los gestos de una persona: boca, ojos, cejas y cabeza. Es la opción más expresiva, y además la voz puede ser la de ustedes.",
   "",
   "**Cómo grabar cada línea** (una por video, con el nombre de su fila: `1.20.mp4`, `1.07.mp4`):",
   "- Celular **en horizontal** y quieto (apoyado), cara **de frente**, a unos 50 cm, con buena luz de frente y fondo liso.",
   "- Empiecen **un segundo con la cara neutra y la boca cerrada**; después digan la línea **exagerando como en telenovela**.",
   "- No tapen la cara con las manos y giren la cabeza solo un poco.",
   "",
   "1. **Entorno de ejecución → Cambiar tipo de entorno → GPU T4 → Guardar** y luego **Ejecutar todo**.",
   "2. Primero suban `entrada.zip` (imágenes) y después sus videos (pueden elegir varios a la vez).",
   "3. Al final se descarga `salida.zip`. Pónganlo en `Pipeline/colab/` y avísenle a Claude."),
code("# 1. GPU", "!nvidia-smi --query-gpu=name,memory.total --format=csv"),
code("# 2. Instalar LivePortrait y descargar sus pesos",
     "%cd /content",
     "!rm -rf LivePortrait && git clone -q https://github.com/KwaiVGI/LivePortrait.git",
     "%cd /content/LivePortrait",
     "!pip -q install tyro onnxruntime-gpu pykalman lmdb imageio-ffmpeg 'huggingface_hub[cli]' rich",
     "!pip -q install -r requirements_base.txt --no-deps 2>/dev/null; true",
     "!huggingface-cli download KwaiVGI/LivePortrait --local-dir pretrained_weights --exclude '*.git*' 'README.md' 'docs' > /dev/null",
     "!ls pretrained_weights"),
*SUBIR,
code("# 4. Subir los videos de actuación (1.20.mp4, 1.07.mp4…)",
     "os.makedirs('/content/actuacion', exist_ok=True)",
     "for n, b in files.upload().items(): open('/content/actuacion/' + n, 'wb').write(b)",
     "print(sorted(os.listdir('/content/actuacion')))"),
code("# 5. Transferir la actuación a cada personaje",
     "import glob, subprocess, shutil",
     "os.makedirs('/content/salida', exist_ok=True)",
     "for vid in sorted(glob.glob('/content/actuacion/*.mp4')):",
     "    fila = os.path.basename(vid)[:-4]; img = f'/content/entrada/{fila}.png'",
     "    if not os.path.exists(img): print('no hay imagen para', fila); continue",
     "    out = f'/content/tmp/{fila}'; shutil.rmtree(out, ignore_errors=True)",
     "    print('animando', fila)",
     "    r = subprocess.run(['python', 'inference.py', '-s', img, '-d', vid, '-o', out, '--flag_crop_driving_video'], capture_output=True, text=True)",
     "    vids = [v for v in glob.glob(out + '/*.mp4') if 'concat' not in v]",
     "    if vids:",
     "        shutil.copy(vids[0], f'/content/salida/{fila}.mp4')",
     "        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', vid, '-vn', '-ac', '2', '-ar', '48000', f'/content/salida/{fila}-voz.wav'])",
     "        print('  listo')",
     "    else: print('  ERROR\\n', r.stdout[-1500:], r.stderr[-3000:])"),
*BAJAR])

# ---------------- paquete de entrada ----------------
ent = R / "entrada"; shutil.rmtree(ent, ignore_errors=True); ent.mkdir()
for f in filas:
    if f == "1.20":     # imagen original completa: el confesionario
        shutil.copy(P.parent / "Imagenes" / "Don Harold_ Jefe de Gestión Humana.png", ent / "1.20.png")
    elif f == "1.07":   # recorte sobre magenta: después se quita el magenta y se compone en la sala de juntas
        har = Image.open(P / "recortes" / "HAROLD.png"); har = har.crop(har.getchannel("A").getbbox())
        lienzo = Image.new("RGBA", (har.width + 80, har.height + 40), (255, 0, 255, 255)); lienzo.alpha_composite(har, (40, 40))
        lienzo.convert("RGB").save(ent / "1.07.png")
    wav = P / "prueba" / "audio" / f"{f}.wav"
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(wav), "-ar", "16000", "-ac", "1", str(ent / f"{f}.wav")], check=True)
with zipfile.ZipFile(R / "entrada.zip", "w") as z:
    for p in sorted(ent.iterdir()): z.write(p, p.name)
old = R / "caras-que-hablan.ipynb"
if old.exists(): old.unlink()
print("ok", sorted(p.name for p in ent.iterdir()))
