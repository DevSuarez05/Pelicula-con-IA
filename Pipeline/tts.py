"""Genera una línea de voz con la voz fija del personaje (voces.json).
Uso: python tts.py PERSONAJE "texto" salida.mp3
Reintenta si el audio sale cortado (el servicio a veces devuelve solo un pedazo)."""
import asyncio, json, sys, pathlib
import edge_tts
VOCES = json.loads((pathlib.Path(__file__).parent / "voces.json").read_text(encoding="utf-8"))

async def main(p, texto, out):
    v = VOCES[p]
    minimo = len(texto) * 250   # una voz normal da ~550 bytes por carácter (48 kbps); un audio cortado queda muy por debajo
    for intento in range(4):
        await edge_tts.Communicate(texto, v["voz"], rate=v["rate"], pitch=v["pitch"]).save(out)
        if pathlib.Path(out).stat().st_size >= minimo:
            return
    print("AVISO: el audio pudo salir cortado:", out)

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2], sys.argv[3]))
