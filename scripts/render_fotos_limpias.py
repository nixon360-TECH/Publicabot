"""Render local photo motion clips. Python stdlib + FFmpeg/ffprobe; no uploads.

Inputs remain read-only. A new output directory is required for each version.
This creates silent editing footage, not a finished property advertisement.
"""
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import html
import json
import math
from pathlib import Path
import subprocess


def run(command):
    result = subprocess.run([str(x) for x in command], capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode:
        raise RuntimeError(result.stderr[-6000:])
    return result.stdout


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def probe(ffprobe, path, frames=False):
    args = [ffprobe, "-v", "error"]
    if frames:
        args += ["-count_frames"]
    return json.loads(run(args + ["-show_streams", "-show_format", "-of", "json", path]))


def geometry(source_size, target_size, anchor):
    iw, ih = source_size
    ow, oh = target_size
    # Match the output aspect ratio BEFORE zoompan, which otherwise stretches photos.
    cw = min(iw, ih * ow / oh)
    ch = cw * oh / ow
    cw, ch = int(cw) // 2 * 2, int(ch) // 2 * 2
    x = round((iw - cw) * anchor[0]) // 2 * 2
    y = round((ih - ch) * anchor[1]) // 2 * 2
    return cw, ch, x, y


def motion_filter(source_size, target_size, shot, duration, fps):
    n = round(duration * fps)
    if n < 2:
        raise ValueError("At least two frames required")
    cw, ch, cx, cy = geometry(source_size, target_size, shot["crop_anchor"])
    ow, oh = target_size
    ease = f"(1-cos(PI*on/{n-1}))/2"
    motions = {
        "push_in": (f"1+0.12*{ease}", "0.5", "0.5"),
        "pull_out": (f"1.12-0.12*{ease}", "0.5", "0.5"),
        "pan_right": ("1.12", f"0.10+0.80*{ease}", "0.5"),
        "pan_left": ("1.12", f"0.90-0.80*{ease}", "0.5"),
        "reveal_up": ("1.12", "0.5", f"0.85-0.70*{ease}"),
    }
    z, x, y = motions[shot["motion"]]
    return (f"crop={cw}:{ch}:{cx}:{cy},scale={ow*2}:{oh*2}:flags=lanczos:in_range=full:out_range=limited:out_color_matrix=bt709,"
            f"zoompan=z='{z}':x='(iw-iw/zoom)*({x})':y='(ih-ih/zoom)*({y})'"
            f":d={n}:s={ow}x{oh}:fps={fps},setsar=1,format=yuv420p,setrange=limited")


def encode_options():
    return ["-an", "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-threads", "2", "-maxrate", "12M", "-bufsize", "24M",
            "-pix_fmt", "yuv420p", "-color_range", "tv", "-colorspace", "bt709",
            "-movflags", "+faststart", "-map_metadata", "-1"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--ffmpeg", default="ffmpeg")
    parser.add_argument("--ffprobe", default="ffprobe")
    parser.add_argument("--only", help="Render a single shot id for a pilot")
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    source, output = args.source.resolve(strict=True), args.output.resolve()
    if output == source or source in output.parents:
        raise ValueError("Output must be outside the input photo directory")
    shots = [s for s in plan["shots"] if not args.only or s["id"] == args.only]
    if not shots:
        raise ValueError("No matching shots")
    duration, fps = plan["duration_seconds"], plan["fps"]
    if not (math.isfinite(duration) and 1 <= duration <= 30 and 1 <= fps <= 60):
        raise ValueError("Invalid duration/fps")
    inputs = []
    for shot in shots:
        path = (source / shot["file"]).resolve(strict=True)
        if path.parent != source or shot["file"] in plan.get("excluded", []):
            raise ValueError("Unexpected or excluded source")
        if any(not 0 <= a <= 1 for a in shot["crop_anchor"]):
            raise ValueError("Crop anchors must be between zero and one")
        stream = probe(args.ffprobe, path)["streams"][0]
        inputs.append({"shot": shot, "path": path, "sha256": sha256(path),
                       "size": [stream["width"], stream["height"]]})
    output.mkdir(parents=True, exist_ok=False)
    (output / "edit_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    records = []
    base = [args.ffmpeg, "-hide_banner", "-loglevel", "error", "-nostdin", "-n", "-filter_threads", "2"]
    for fmt, size in plan["formats"].items():
        folder = output / fmt
        folder.mkdir()
        for item in inputs:
            shot = item["shot"]
            target = folder / f"SI_{shot['id']}_{fmt}_{plan['version']}.mp4"
            print(f"RENDER {target.name}", flush=True)
            vf = motion_filter(item["size"], size, shot, duration, fps)
            run(base + ["-i", item["path"], "-vf", vf, "-frames:v", str(round(duration*fps))]
                + encode_options() + [target])
            data = probe(args.ffprobe, target, frames=True)
            stream = data["streams"][0]
            checks = {
                "resolution": [stream["width"], stream["height"]] == size,
                "frames": int(stream["nb_read_frames"]) == round(duration*fps),
                "duration": abs(float(data["format"]["duration"]) - duration) < 1/fps,
                "pixel_format": stream["pix_fmt"] == "yuv420p",
                "square_pixels": stream.get("sample_aspect_ratio") == "1:1",
                "silent": all(s["codec_type"] != "audio" for s in data["streams"]),
            }
            run([args.ffmpeg, "-v", "error", "-xerror", "-i", target, "-f", "null", "-"])
            checks["decode"] = True
            frame_hashes = run([args.ffmpeg, "-v", "error", "-i", target,
                               "-vf", "fps=1,scale=64:-2", "-f", "framemd5", "-"])
            hashes = [line.rsplit(",", 1)[-1].strip() for line in frame_hashes.splitlines()
                      if line and not line.startswith("#")]
            checks["motion_present"] = len(set(hashes)) >= min(3, len(hashes)) and len(hashes) > 1
            if not all(checks.values()):
                raise RuntimeError(f"QA failed: {target.name}: {checks}")
            stills = []
            for label, sec in [("start", 0), ("mid", duration/2), ("end", duration-1/fps)]:
                still = folder / f"{target.stem}_{label}.jpg"
                run(base + ["-ss", str(sec), "-i", target, "-vf", "scale=320:-2",
                            "-frames:v", "1", "-update", "1", still])
                stills.append(still.relative_to(output).as_posix())
            records.append({"file": target.relative_to(output).as_posix(),
                            "source": shot["file"], "source_sha256": item["sha256"],
                            "source_size": item["size"], "format": fmt,
                            "motion": shot["motion"], "sha256": sha256(target),
                            "filter": vf, "checks": checks, "stills": stills})
            print(f"OK {target.name}", flush=True)
        concat = folder / "concat.txt"
        concat.write_text("\n".join(f"file '{Path(r['file']).name}'" for r in records if r["format"] == fmt), encoding="utf-8")
        preview = output / f"preview_{fmt}.mp4"
        run(base + ["-f", "concat", "-safe", "1", "-i", concat,
                    "-vf", "scale=432:-2", "-an", "-c:v", "libx264", "-preset", "fast",
                    "-crf", "22", "-threads", "2", "-movflags", "+faststart", preview])
    unchanged = all(sha256(x["path"]) == x["sha256"] for x in inputs)
    report = {"state": "RENDERED_DRAFT", "type": "silent_motion_footage",
              "source_unchanged": unchanged, "publish_authorized": False,
              "visual_review": "PENDING", "outputs": records,
              "notes": ["Movimiento 2D sobre fotos ya editadas; sin generación IA adicional.",
                        "Vertical: recorte de fotos horizontales de 1672x941; no es detalle 4K nativo.",
                        "Clips para montaje: sin voz, música, texto ni aprobación de publicación."]}
    (output / "qa_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest = {
        "agente": "codex", "fecha_hora": datetime.now(timezone(timedelta(hours=-6))).isoformat(),
        "script": "scripts/render_fotos_limpias.py", "estado": "borrador",
        "entradas": [{"archivo": x["shot"]["file"], "sha256": x["sha256"]} for x in inputs],
        "salidas": [{"archivo": r["file"], "sha256": r["sha256"]} for r in records],
        "notas": report["notes"],
    }
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (output / "approval_status.json").write_text(json.dumps({"status": "DRAFT", "publish_authorized": False}, indent=2), encoding="utf-8")
    cards = []
    for record in records:
        cards.append(f'<article><h2>{html.escape(Path(record["file"]).stem)}</h2>'
                     f'<video controls preload="none" poster="{record["stills"][1]}" src="{record["file"]}"></video>'
                     f'<p>{html.escape(record["motion"])} · {duration:g} segundos · sin audio</p>'
                     f'<a href="{record["file"]}" download>Descargar MP4</a></article>')
    page = '<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Santa Isabel · movimiento desde fotos</title><style>body{background:#101927;color:#f7f7f7;font:16px system-ui;margin:30px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px}article{background:#1b2a4a;padding:18px;border-radius:12px}h2{font-size:16px}video{width:100%;max-height:480px}a{color:#ecd628}</style><h1>Santa Isabel · fotos en movimiento</h1><p>Borradores para montaje · 4:5 y 9:16 · originales intactos</p><main>' + ''.join(cards) + '</main></html>'
    (output / "index.html").write_text(page, encoding="utf-8")
    if not unchanged:
        raise RuntimeError("Source changed during render")
    print(f"DONE {len(records)} clips: {output}", flush=True)


if __name__ == "__main__":
    main()
