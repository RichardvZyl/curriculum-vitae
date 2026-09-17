#!/usr/bin/env python3
"""Write historical pandoc+xelatex PDFs to dist/ (comparison only).

Does NOT overwrite downloads/. Canonical publish path is generate-cv-pdf.py /
generate-skills-overview-pdf.py (WeasyPrint). See pdf/README.md and docs/adr/0001.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

PANDOC_FLAGS = [
    "--pdf-engine=xelatex",
    "-V",
    "geometry:margin=1in",
    "-V",
    "fontsize=10pt",
    "-V",
    "colorlinks=true",
    "-V",
    "linkcolor=blue",
    "-V",
    "urlcolor=blue",
]

JOBS = [
    (ROOT / "CV.md", DIST / "Richard-van-Zyl-CV.pandoc-xelatex.pdf"),
    (ROOT / "SKILLS-OVERVIEW.md", DIST / "Richard-van-Zyl-Skills-Overview.pandoc-xelatex.pdf"),
]


def main() -> int:
    if shutil.which("pandoc") is None:
        sys.stderr.write("pandoc not found — see https://pandoc.org/\n")
        return 1
    if shutil.which("xelatex") is None:
        sys.stderr.write(
            "xelatex not found — install TeX Live / texlive-xetex "
            "(https://tug.org/texlive/)\n"
        )
        return 1

    DIST.mkdir(parents=True, exist_ok=True)
    for src, out in JOBS:
        if not src.is_file():
            sys.stderr.write(f"missing {src}\n")
            return 1
        cmd = ["pandoc", str(src), "-o", str(out), *PANDOC_FLAGS]
        print(" ".join(cmd))
        subprocess.run(cmd, check=True, cwd=ROOT)
        print(f"wrote {out} ({out.stat().st_size} bytes)")
    print("Historical only — do not copy to downloads/ without a new ADR.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
