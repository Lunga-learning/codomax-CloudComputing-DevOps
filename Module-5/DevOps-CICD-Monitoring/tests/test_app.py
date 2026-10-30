from pathlib import Path
import unittest

HTML_FILE = Path(__file__).resolve().parent.parent / "index.html"


class TestModule5Application(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML_FILE.read_text(encoding="utf-8")

    def test_page_title(self):
        self.assertIn("<title>Module 5 - DevOps CI/CD</title>", self.html)

    def test_main_heading(self):
        self.assertIn(
            "<h1>Module 5: DevOps, CI/CD & Monitoring</h1>",
            self.html,
        )

    def test_application_status(self):
        self.assertIn(
            "Application status: Running successfully!",
            self.html,
        )


if __name__ == "__main__":
    unittest.main()
