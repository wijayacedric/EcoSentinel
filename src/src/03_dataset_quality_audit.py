"""Backward-compatible wrapper. Canonical script: src/quality_audit.py"""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parents[1] / "quality_audit.py"), run_name="__main__")
