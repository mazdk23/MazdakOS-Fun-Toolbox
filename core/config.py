"""
Global configuration for MazdakOS Fun Toolbox.
"""

from pathlib import Path
import sys


PROJECT_NAME = "MazdakOS Fun Toolbox"
VERSION = "0.1.0"
AUTHOR = "mazdakproninja"


def get_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    return Path(__file__).resolve().parent.parent


ROOT_DIR = get_root()

APPS_DIR = ROOT_DIR / "apps"
TOOLS_DIR = ROOT_DIR / "tools"
PRANKS_DIR = ROOT_DIR / "pranks"

ASSETS_DIR = ROOT_DIR / "assets"
TESTS_DIR = ROOT_DIR / "tests"
DOCS_DIR = ROOT_DIR / "docs"


IGNORED_DIRECTORIES = {
    "__pycache__",
    "build",
    "dist",
    ".git",
    ".venv",
    "venv",
}


def get_path(*parts: str) -> Path:
    return ROOT_DIR.joinpath(*parts)