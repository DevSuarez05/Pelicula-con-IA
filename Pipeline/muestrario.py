"""Muestrario de voces: cada voz se presenta y actúa una línea. Uso: python muestrario.py"""
import asyncio, json, pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import actuar
R = pathlib.Path(__file__).parent; OUT = R / "prueba" / "muestrario"; OUT.mkdir(parents=True, exist_ok=True)
HOMBRES = ["es-CO-GonzaloNeural","es-MX-JorgeNeural","es-US-AlonsoNeural","es-VE-SebastianNeural","es-PE-AlexNeural",
  "es-AR-TomasNeural","es-CL-LorenzoNeural","es-CU-ManuelNeural","es-DO-EmilioNeural","es-UY-MateoNeural","es-EC-LuisNeural",
  "es-CR-JuanNeural","es-GT-AndresNeural","es-PA-RobertoNeural","es-PR-VictorNeural","es-ES-AlvaroNeural",
  "en-US-AndrewMultilingualNeural","en-US-BrianMultilingualNeural","fr-FR-RemyMultilingualNeural","it-IT-GiuseppeMultilingualNeural"]
MUJERES = ["es-CO-SalomeNeural","es-MX-DaliaNeural","es-US-PalomaNeural","es-VE-PaolaNeural","es-PE-CamilaNeural","es-AR-ElenaNeural",
  "es-CL-CatalinaNeural","es-CU-BelkysNeural","es-DO-RamonaNeural","es-UY-ValentinaNeural","es-EC-AndreaNeural","es-PR-KarinaNeural",
  "es-ES-XimenaNeural","en-US-AvaMultilingualNeural","en-US-EmmaMultilingualNeural","fr-FR-VivienneMultilingualNeural","pt-BR-ThalitaMultilingualNeural"]
PAIS = {"CO":"Colombia","MX":"México","US":"Estados Unidos","VE":"Venezuela","PE":"Perú","AR":"Argentina","CL":"Chile","CU":"Cuba",
  "DO":"República Dominicana","UY":"Uruguay","EC":"Ecuador","CR":"Costa Rica","GT":"Guatemala","PA":"Panamá","PR":"Puerto Rico","ES":"España"}
def etiqueta(v):
    p = v.split("-"); nombre = p[2].replace("MultilingualNeural","").replace("Neural","")
    return f"{nombre}, multilingüe." if "Multilingual" in v else f"{nombre}, de {PAIS[p[1]]}."
async def main():
    for grupo, voces, fila in (("hombres", HOMBRES, "1.07"), ("mujeres", MUJERES, "1.19")):
        spec = json.loads((R / "actuaciones" / f"{fila}.json").read_text(encoding="utf-8"))
        lista = []
        for i, v in enumerate(voces, 1):
            s = {"personaje": spec["personaje"], "frases": [{"t": f"Voz {i}. {etiqueta(v)}", "rate": "+0%", "pausa": 500}] + spec["frases"]}
            f = OUT / f"{grupo}-{i:02d}-{v.replace('Neural','')}.wav"
            await actuar.actuar(s, f, v); lista.append(f); print(f.name)
        txt = OUT / f"{grupo}.txt"; txt.write_text("".join(f"file '{f.as_posix()}'\nfile '{(OUT/'_silencio.wav').as_posix()}'\n" for f in lista), encoding="utf-8")
        subprocess.run([actuar.FF, "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", "1", "-c:a", "pcm_s16le", str(OUT / "_silencio.wav")], check=True)
        subprocess.run([actuar.FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(txt), "-c:a", "libmp3lame", "-q:a", "3", str(R / "prueba" / f"MUESTRARIO-VOCES-{grupo.upper()}.mp3")], check=True)
asyncio.run(main())
