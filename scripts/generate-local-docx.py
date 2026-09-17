#!/usr/bin/env python3
"""Generate local DOCX under dist/ (unpublished — see docs/adr/0003).

Requires pandoc: https://pandoc.org/
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

JOBS = [
    (ROOT / "CV.md", DIST / "Richard-van-Zyl-CV.docx"),
    (ROOT / "SKILLS-OVERVIEW.md", DIST / "Richard-van-Zyl-Skills-Overview.docx"),
]


def main() -> int:
    if shutil.which("pandoc") is None:
        sys.stderr.write("pandoc not found — see https://pandoc.org/\n")
        return 1

    DIST.mkdir(parents=True, exist_ok=True)
    for src, out in JOBS:
        if not src.is_file():
            sys.stderr.write(f"missing {src}\n")
            return 1
        cmd = ["pandoc", str(src), "-o", str(out)]
        print(" ".join(cmd))
        subprocess.run(cmd, check=True, cwd=ROOT)
        print(f"wrote {out} ({out.stat().st_size} bytes)")
    print("Local only — gitignored; do not link from the site.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
