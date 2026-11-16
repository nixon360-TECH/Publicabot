"""Valida paquetes de artes por agente sin copiar datos personales al repositorio."""

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image


FORMATS = {"4x5": (1080, 1350), "9x16": (1080, 1920)}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate(package, visual_reviewed=False, require_drive_authorization=False):
    manifest = json.loads((package / "manifest.json").read_text(encoding="utf8"))
    outputs = manifest["outputs"]
    errors = []
    if len(outputs) != 37:
        errors.append(f"cantidad de diseños: {len(outputs)}")
    if len(list((package / "feed_4x5").glob("*.jpg"))) != 22:
        errors.append("cantidad de feed distinta de 22")
    if len(list((package / "historias_9x16").glob("*.jpg"))) != 15:
        errors.append("cantidad de historias distinta de 15")
    if len(list((package / "copys").glob("*.md"))) != 15:
        errors.append("cantidad de copys distinta de 15")
    for item in outputs:
        path = package / item["file"]
        try:
            with Image.open(path) as image:
                image.load()
                if image.size != FORMATS[item["format"]]:
                    errors.append(f"medidas incorrectas: {item['file']}")
        except Exception as exc:
            errors.append(f"no decodifica: {item['file']}: {exc}")
            continue
        if sha256(path) != item["sha256"]:
            errors.append(f"hash incorrecto: {item['file']}")
        width, height = FORMATS[item["format"]]
        safe = manifest["safe_zones_px"][item["format"]]
        for bound in item["bounds"]:
            x0, y0, x1, y1 = bound["bbox"]
            if x0 < 0 or x1 > width or y0 < safe["top"] or y1 > height - safe["bottom"]:
                errors.append(f"zona segura: {item['file']}: {bound['text']}")
    resources = package / "recursos_informacion_general"
    expected_resources = {
        "01_INFORMACION_GENERAL.md",
        "02_PREGUNTAS_FRECUENTES.md",
        "03_REGLAS_DE_USO.md",
    }
    if not resources.is_dir() or {p.name for p in resources.glob("*.md")} != expected_resources:
        errors.append("recursos generales incompletos")
    else:
        faq = (resources / "02_PREGUNTAS_FRECUENTES.md").read_text(encoding="utf8")
        if "El agua es provista por la alcaldía (ANDA)." not in faq:
            errors.append("respuesta de agua ausente")
        if "No hay una confirmación pública vigente" not in faq:
            errors.append("electricidad no está bloqueada")
    if require_drive_authorization and not manifest.get("drive_upload_authorized"):
        errors.append("autorización de Drive ausente")
    report = json.loads((package / "qa_report.json").read_text(encoding="utf8"))
    report.update(
        {
            "status": "READY_FOR_REVIEW" if not errors and visual_reviewed else "BLOCKED_QA" if errors else "DRAFT_FOR_USER_REVIEW",
            "visual_review": "PASSED" if visual_reviewed else "PENDING",
            "technical_review": "PASSED" if not errors else "FAILED",
            "resources_verified": not errors,
            "errors": errors,
        }
    )
    (package / "qa_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agents-root", type=Path, required=True)
    parser.add_argument("--agent", action="append", required=True)
    parser.add_argument("--package-name", default="artes")
    parser.add_argument("--visual-reviewed", action="store_true")
    parser.add_argument(
        "--require-drive-authorization",
        action="store_true",
        help="Bloquea la validación si el paquete aún no fue autorizado para subir a Drive.",
    )
    args = parser.parse_args()
    failed = False
    for agent_id in args.agent:
        report = validate(
            args.agents_root / agent_id / args.package_name,
            args.visual_reviewed,
            args.require_drive_authorization,
        )
        print(agent_id, report["status"], len(report["errors"]), flush=True)
        failed = failed or bool(report["errors"])
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
