#!/usr/bin/env python3
"""Rebuild print artefacts.

Default: canonical WeasyPrint PDFs → downloads/
  --all: also historical pandoc PDFs + local DOCX → dist/

See pdf/README.md and docs/adr/0001–0003.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = Path(__file__).resolve().parent


def run(script: str) -> None:
    subprocess.run([sys.executable, str(SCRIPTS / script)], check=True, cwd=ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--all",
        action="store_true",
        help="Also write pandoc+xelatex PDFs and DOCX under dist/",
    )
    args = parser.parse_args()

    run("generate-cv-pdf.py")
    run("generate-skills-overview-pdf.py")
    if args.all:
        run("generate-historical-pandoc-pdfs.py")
        run("generate-local-docx.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
