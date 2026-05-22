"""Optional dependency loading for local scripts."""

import subprocess

from .paths import VENV_PIP


def ensure_openpyxl():
    try:
        import openpyxl
    except ImportError:
        subprocess.check_call([str(VENV_PIP), "install", "openpyxl"])
        import openpyxl
    return openpyxl
