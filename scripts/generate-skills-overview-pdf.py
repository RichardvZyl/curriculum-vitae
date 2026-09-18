#!/usr/bin/env python3
"""Generate downloads/Richard-van-Zyl-Skills-Overview.pdf from SKILLS-OVERVIEW.md.

Canonical Skills Overview PDF pipeline. Style lives in
scripts/skills-overview-print.css — content changes in SKILLS-OVERVIEW.md must
not alter layout; only edit the CSS (or this script's markdown→HTML mapping)
to change appearance.

  python3 scripts/generate-skills-overview-pdf.py

Requires: pip install -r scripts/requirements-pdf.txt
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "SKILLS-OVERVIEW.md"
OUTPUT = ROOT / "downloads" / "Richard-van-Zyl-Skills-Overview.pdf"
SHARED_CSS = ROOT / "pdf" / "print-shared.css"
CSS_PATH = Path(__file__).resolve().parent / "skills-overview-print.css"


def combined_css() -> str:
    return SHARED_CSS.read_text(encoding="utf-8") + "\n" + CSS_PATH.read_text(encoding="utf-8")


def markdown_to_body(md: str) -> str:
    # Local repo links become plain names in the PDF.
    md = md.replace("[`SKILLSMATRIX.md`](./SKILLSMATRIX.md)", "SKILLSMATRIX.md")
    md = md.replace("[`CV.md`](./CV.md)", "CV.md")
    md = md.replace("[`LICENSE`](./LICENSE)", "LICENSE")
    md = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1", md)

    body = markdown.markdown(
        md,
        extensions=["tables", "fenced_code", "sane_lists"],
    )
    body = body.replace("<th>Years</th>", '<th class="yrs">Years</th>')
    body = body.replace("<th>Skill</th>", '<th class="skill">Skill</th>')
    body = re.sub(
        r"<table>\s*<thead>\s*<tr>\s*<th class=\"skill\">Skill</th>\s*<th class=\"yrs\">Years</th>",
        '<table class="skills">\n<thead>\n<tr>\n'
        '<th class="skill">Skill</th>\n<th class="yrs">Years</th>',
        body,
    )
    body = re.sub(
        r"(<h2>[\s\S]*?</h2>\s*(?:<p>[\s\S]*?</p>)?)",
        r'<div class="keep">\1</div>',
        body,
    )
    return body


def build_html(md: str, css: str) -> str:
    body = markdown_to_body(md)
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en"><head><meta charset="utf-8"/>'
        "<title>Richard van Zyl — Skills Overview</title>"
        f"<style>{css}</style></head><body>\n{body}\n</body></html>"
    )


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing source: {SOURCE}", file=sys.stderr)
        return 1
    if not SHARED_CSS.is_file():
        print(f"missing stylesheet: {SHARED_CSS}", file=sys.stderr)
        return 1
    if not CSS_PATH.is_file():
        print(f"missing stylesheet: {CSS_PATH}", file=sys.stderr)
        return 1

    css = combined_css()
    html = build_html(SOURCE.read_text(encoding="utf-8"), css)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(ROOT)).write_pdf(str(OUTPUT))
    print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")
    print(f"style: {SHARED_CSS.relative_to(ROOT)} + {CSS_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
