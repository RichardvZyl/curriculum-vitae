#!/usr/bin/env python3
"""Generate downloads/Richard-van-Zyl-Skills-Matrix.pdf from SKILLSMATRIX.md.

Full / uncondensed skills artefact (companion to the condensed Skills Overview).
Style: scripts/skills-matrix-print.css.

  python3 scripts/generate-skills-matrix-pdf.py

Requires: pip install -r scripts/requirements-pdf.txt
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "SKILLSMATRIX.md"
OUTPUT = ROOT / "downloads" / "Richard-van-Zyl-Skills-Matrix.pdf"
SHARED_CSS = ROOT / "pdf" / "print-shared.css"
CSS_PATH = Path(__file__).resolve().parent / "skills-matrix-print.css"

# Rows marked for CV/site omission must not appear in the published PDF.
_OMIT_LEAVING = re.compile(
    r"^\| Leaving \|[^\n]*omit from CV/site[^\n]*\|\s*$",
    re.MULTILINE | re.IGNORECASE,
)


def prepare_markdown(md: str) -> str:
    """Human-facing PDF: no repo markdown paths; strip interview-only rows."""
    md = _OMIT_LEAVING.sub("", md)
    # Drop links that point at local markdown (keep link text only if useful).
    md = re.sub(r"\[`([^`]+)`\]\(\./[^)]+\.md\)", r"\1", md)
    md = re.sub(r"\[([^\]]+)\]\(\./[^)]+\.md\)", r"\1", md)
    # External URLs: keep visible label only (no raw URL noise in print).
    md = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1", md)
    return md


def markdown_to_body(md: str) -> str:
    md = prepare_markdown(md)
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
    # Employer metadata tables: first header cell is Field.
    body = re.sub(
        r"<table>\s*<thead>\s*<tr>\s*<th>Field</th>\s*<th>Detail</th>",
        '<table class="meta">\n<thead>\n<tr>\n<th>Field</th>\n<th>Detail</th>',
        body,
    )
    return body


def build_html(md: str, css: str) -> str:
    body = markdown_to_body(md)
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en"><head><meta charset="utf-8"/>'
        "<title>Richard van Zyl — Skills Matrix</title>"
        f"<style>{css}</style></head><body>\n{body}\n</body></html>"
    )


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing source: {SOURCE}", file=sys.stderr)
        return 1
    if not CSS_PATH.is_file():
        print(f"missing stylesheet: {CSS_PATH}", file=sys.stderr)
        return 1

    css = SHARED_CSS.read_text(encoding="utf-8") + "\n" + CSS_PATH.read_text(encoding="utf-8")
    html = build_html(SOURCE.read_text(encoding="utf-8"), css)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(ROOT)).write_pdf(str(OUTPUT))
    print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")
    print(f"style: {SHARED_CSS.relative_to(ROOT)} + {CSS_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
