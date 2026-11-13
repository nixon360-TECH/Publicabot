"""Paneo/zoom (Ken Burns) a partir de una FOTO LIMPIA, solo FFmpeg (gratis, local).
Uso: python paneo_foto.py foto.jpg salida.mp4 --preset push_in --formato 4x5 --seg 6
Presets: push_in, pull_out, pan_der, pan_izq, reveal_arriba.
Limite: fotos de 1672x941 ampliadas a vertical se ven suaves; preferir 4x5 o 16:9, o ampliar antes con un escalador gratuito."""
import argparse, subprocess, shutil
ap = argparse.ArgumentParser()
ap.add_argument("foto"); ap.add_argument("salida")
ap.add_argument("--preset", default="push_in", choices=["push_in", "pull_out", "pan_der", "pan_izq", "reveal_arriba"])
ap.add_argument("--formato", default="4x5", choices=["9x16", "4x5", "1x1"])
ap.add_argument("--seg", type=float, default=6.0)
ap.add_argument("--fps", type=int, default=25)
a = ap.parse_args()
size = {"9x16": "1080x1920", "4x5": "1080x1350", "1x1": "1080x1080"}[a.formato]
n = int(a.seg * a.fps)
t = f"on/{n}"
z, x, y = {
    "push_in": (f"1.0+0.30*{t}", "(iw-iw/zoom)*0.5", "(ih-ih/zoom)*0.5"),
    "pull_out": (f"1.30-0.30*{t}", "(iw-iw/zoom)*0.5", "(ih-ih/zoom)*0.5"),
    "pan_der": ("1.25", f"(iw-iw/zoom)*{t}", "(ih-ih/zoom)*0.5"),
    "pan_izq": ("1.25", f"(iw-iw/zoom)*(1-{t})", "(ih-ih/zoom)*0.5"),
    "reveal_arriba": (f"1.0+0.25*{t}", "(iw-iw/zoom)*0.5", f"(ih-ih/zoom)*(1-{t})"),
}[a.preset]
ff = shutil.which("ffmpeg") or r"C:\Users\Usuario\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"
vf = f"scale=6688:-1:flags=lanczos,zoompan=z='{z}':x='{x}':y='{y}':d={n}:s={size}:fps={a.fps},format=yuv420p"
subprocess.run([ff, "-y", "-loop", "1", "-t", str(a.seg), "-i", a.foto, "-vf", vf, "-c:v", "libx264", "-crf", "18", "-maxrate", "12M", "-bufsize", "24M", "-movflags", "+faststart", a.salida], check=True)
