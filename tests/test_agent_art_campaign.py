import tempfile
import unittest
from pathlib import Path

from scripts.codex_artes_15d import caption, parse_agent_calendar, split_display_name


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


if __name__ == "__main__":
    unittest.main()
