import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "photo_motion", Path(__file__).resolve().parents[1] / "scripts" / "render_fotos_limpias.py")
motion = importlib.util.module_from_spec(spec)
spec.loader.exec_module(motion)


class PhotoMotionGeometryTests(unittest.TestCase):
    def test_landscape_to_portrait_preserves_ratio_and_stays_inside_source(self):
        for target in [(1080, 1350), (1080, 1920)]:
            for anchor in [(0, 0), (0.54, 0.5), (1, 1)]:
                with self.subTest(target=target, anchor=anchor):
                    w, h, x, y = motion.geometry((1672, 941), target, anchor)
                    self.assertLess(abs(w / h - target[0] / target[1]), 0.003)
                    self.assertGreaterEqual(min(x, y), 0)
                    self.assertLessEqual(x + w, 1672)
                    self.assertLessEqual(y + h, 941)

    def test_portrait_to_landscape_and_square_sources(self):
        for source, target in [((900, 1600), (1920, 1080)), ((1024, 1024), (1080, 1350))]:
            w, h, x, y = motion.geometry(source, target, (1, 1))
            self.assertLess(abs(w / h - target[0] / target[1]), 0.005)
            self.assertLessEqual(x + w, source[0])
            self.assertLessEqual(y + h, source[1])


if __name__ == "__main__":
    unittest.main()
