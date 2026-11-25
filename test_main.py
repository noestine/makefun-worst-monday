"""Tests for main.py — Worst Monday One-Liners entry.

Written first from RULES.txt, before main.py exists.
Gate: /output/entry.txt must be UTF-8 text, 1-140 chars, not only whitespace.
The line must be one funny line about an AI agent's worst Monday, deterministic.
"""
import os
import subprocess
import sys
import unittest

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_PY = os.path.join(REPO_DIR, "main.py")
OUTPUT_PATH = "/output/entry.txt"


class TestLineValidation(unittest.TestCase):
    def test_line_length_within_gate(self):
        import main
        line = main.get_line()
        self.assertIsInstance(line, str)
        self.assertGreaterEqual(len(line), 1)
        self.assertLessEqual(len(line), 140)

    def test_line_is_single_line(self):
        import main
        self.assertNotIn("\n", main.get_line())
        self.assertNotIn("\r", main.get_line())

    def test_line_not_whitespace_only(self):
        import main
        self.assertTrue(main.get_line().strip())

    def test_line_is_utf8_encodable(self):
        import main
        main.get_line().encode("utf-8")

    def test_line_on_subject_concrete_detail(self):
        import main
        line = main.get_line().lower()
        # Concrete Monday detail required by the judge brief: stuck deploy,
        # flooded inbox, or a stand-up that should have been a message.
        self.assertTrue(
            any(word in line for word in ("deploy", "inbox", "stand-up")),
            "line names no concrete worst-Monday detail",
        )

    def test_validate_accepts_good_line(self):
        import main
        self.assertTrue(main.validate(main.get_line()))

    def test_validate_rejects_empty(self):
        import main
        self.assertFalse(main.validate(""))
        self.assertFalse(main.validate("   "))
        self.assertFalse(main.validate("\n"))

    def test_validate_rejects_too_long(self):
        import main
        self.assertFalse(main.validate("x" * 141))
        self.assertTrue(main.validate("x" * 140))

    def test_validate_rejects_embedded_newline(self):
        import main
        self.assertFalse(main.validate("one\ntwo"))

    def test_validate_rejects_padding(self):
        import main
        self.assertFalse(main.validate(" padded line "))
        self.assertFalse(main.validate("padded line "))
        self.assertFalse(main.validate(" padded line"))

    def test_validate_rejects_non_string(self):
        import main
        self.assertFalse(main.validate(None))
        self.assertFalse(main.validate(42))
        self.assertFalse(main.validate(b"bytes"))


class TestProgramRun(unittest.TestCase):
    def tearDown(self):
        # Never leave a stray artifact behind in /output.
        try:
            os.remove(OUTPUT_PATH)
        except FileNotFoundError:
            pass

    def _run_main(self, cwd):
        return subprocess.run(
            [sys.executable, MAIN_PY],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30,
        )

    def test_run_writes_exact_line_no_newline(self):
        import main
        result = self._run_main(REPO_DIR)
        self.assertEqual(result.returncode, 0, result.stderr)
        with open(OUTPUT_PATH, "rb") as f:
            content = f.read()
        self.assertEqual(content, main.get_line().encode("utf-8"))

    def test_run_is_deterministic(self):
        first = self._run_main(REPO_DIR)
        self.assertEqual(first.returncode, 0, first.stderr)
        with open(OUTPUT_PATH, "rb") as f:
            run1 = f.read()
        second = self._run_main("/tmp")
        self.assertEqual(second.returncode, 0, second.stderr)
        with open(OUTPUT_PATH, "rb") as f:
            run2 = f.read()
        self.assertEqual(run1, run2)

    def test_run_ignores_cwd(self):
        # main.py writes the absolute /output/entry.txt whatever the cwd is.
        result = self._run_main("/tmp")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(os.path.exists(OUTPUT_PATH))

    def test_output_passes_gate(self):
        import main
        result = self._run_main(REPO_DIR)
        self.assertEqual(result.returncode, 0, result.stderr)
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
            text = f.read()
        self.assertTrue(1 <= len(text) <= 140)
        self.assertTrue(text.strip())


if __name__ == "__main__":
    unittest.main()
