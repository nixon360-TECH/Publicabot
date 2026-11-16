import tempfile
import unittest
from pathlib import Path

from scripts.codex_artes_15d import Artist, caption, create_agent_resources, create_gallery, create_readme_html, office_caption, parse_agent_calendar, split_display_name


class AgentArtCampaignTests(unittest.TestCase):
    def test_calendar_extracts_fifteen_approved_copies(self):
        sections = [
            f"## Día {day} · fecha\n\n**Texto de la publicación (copiar y pegar):**\n\n> Texto aprobado {day}\n"
            for day in range(1, 16)
        ]
        source = "**Periodo:** 16/11/2026 al 30/11/2026\n\n" + "\n".join(sections)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "calendario.md"
            path.write_text(source, encoding="utf8")
            start, copies = parse_agent_calendar(path)
        self.assertEqual(start.isoformat(), "2026-11-16")
        self.assertEqual(len(copies), 15)
        self.assertEqual(copies[10], "Texto aprobado 10")

    def test_approved_copy_is_not_rewritten(self):
        approved = "Texto aprobado sin cambios."
        self.assertEqual(caption({}, {}, approved), approved)

    def test_advisor_name_keeps_two_line_composition(self):
        self.assertEqual(split_display_name("NOMBRE APELLIDO"), ["NOMBRE", "APELLIDO"])
        self.assertEqual(split_display_name("NOMBRE DE APELLIDO"), ["NOMBRE DE", "APELLIDO"])

    def test_readme_has_browser_friendly_html(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            (output / "LEEME.md").write_text("# Instrucciones", encoding="utf8")
            create_readme_html(output)
            page = (output / "LEEME.html").read_text(encoding="utf8")
        self.assertIn('<html lang="es">', page)
        self.assertIn('href="index.html"', page)

    def test_gallery_reserves_thumbnail_space(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            calendar = [{"day": 1, "date": "2026-11-16", "angle": "Ángulo", "caption": "Copy"}]
            exports = [{"day": 1, "file": "feed_4x5/muestra.jpg", "format": "4x5", "page": 1}]
            create_gallery(output, calendar, exports, {"nombre": "NOMBRE"})
            page = (output / "index.html").read_text(encoding="utf8")
        self.assertIn('width="320" height="420"', page)
        self.assertIn('a,summary{cursor:pointer}', page)

    def test_agent_resources_use_confirmed_water_provider_and_block_electricity(self):
        snapshot = {
            "location": "UBICACIÓN",
            "public_facts": {
                "price_text": "PRECIO",
                "min_lot_size_varas2": 286,
                "water_provider_text": "El agua es provista por la alcaldía (ANDA).",
            },
        }
        agent = {"nombre": "NOMBRE", "telefono": "+503 0000 0000"}
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            create_agent_resources(output, snapshot, agent)
            faq = (output / "recursos_informacion_general" / "02_PREGUNTAS_FRECUENTES.md").read_text(encoding="utf8")
        self.assertIn("alcaldía (ANDA)", faq)
        self.assertIn("No hay una confirmación pública vigente", faq)

    def test_minimal_style_routes_to_minimal_renderer(self):
        artist = object.__new__(Artist)
        artist.style = "minimal"
        artist.make_minimal = lambda post, fmt: (post, fmt)
        self.assertEqual(artist.make({"id": "sample"}, "4x5"), ({"id": "sample"}, "4x5"))

    def test_office_caption_uses_office_contact(self):
        post = {"copy": "Texto"}
        kit = {"cierre": {"frase": "Agende", "banco_asterisco": "Aviso"}}
        result = office_caption(post, kit, "+503 0000 0000", "50300000000")
        self.assertIn("+503 0000 0000", result)
        self.assertIn("wa.me/50300000000", result)


if __name__ == "__main__":
    unittest.main()
