"""Regression tests for repository tooling."""

from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parent.parent


class ToolingTests(unittest.TestCase):
    """Verify checked-in tooling stays compatible with supported Python."""

    def test_ci_does_not_use_nose(self) -> None:
        """The CI workflow uses the stdlib test runner instead of nose."""
        ci_workflow = (REPO_ROOT / ".github/workflows/ci.yml").read_text()

        self.assertNotIn("nosetests", ci_workflow)
        self.assertIn("python -m unittest -v tests/test_app.py", ci_workflow)

    def test_pipfile_does_not_declare_nose(self) -> None:
        """The service no longer declares nose as a dev dependency."""
        pipfile = (REPO_ROOT / "Pipfile").read_text()

        self.assertNotIn("nose", pipfile)
