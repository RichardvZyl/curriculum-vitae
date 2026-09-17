#!/usr/bin/env python3
"""Generate Richard-van-Zyl-CV.pdf from CV.md with the checked-in print CSS.

Usage (from repo root):
  python3 scripts/generate-cv-pdf.py
  python3 scripts/generate-cv-pdf.py --out /path/to/Richard-van-Zyl-CV.pdf

Requires: weasyprint, markdown (see pdf/README.md).
Concatenates pdf/print-shared.css ahead of pdf/cv-print.css.
Does not touch the Skills Overview / skills-matrix PDF.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import markdown
    from weasyprint import HTML
except ImportError as exc:  # pragma: no cover
    sys.stderr.write(
        "Missing dependency: install with\n"
        "  pip install weasyprint markdown\n"
        f"({exc})\n"
    )
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MD = ROOT / "CV.md"
SHARED_CSS = ROOT / "pdf" / "print-shared.css"
DEFAULT_CSS = ROOT / "pdf" / "cv-print.css"
DEFAULT_OUT = ROOT / "downloads" / "Richard-van-Zyl-CV.pdf"


def combined_css(specific: Path) -> str:
    parts = []
    for path in (SHARED_CSS, specific):
        if not path.is_file():
            raise FileNotFoundError(path)
        parts.append(path.read_text(encoding="utf-8"))
    return "\n".join(parts)


def md_to_html(md_text: str) -> str:
    """Convert CV markdown to HTML body fragment."""
    # Drop the thematic break under the header — the print CSS already
    # separates the masthead from the first section.
    md_text = re.sub(r"\n---\n", "\n\n", md_text, count=1)
    return markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )


def build_document(body_html: str, css_text: str, title: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
{css_text}
</style>
</head>
<body>
{body_html}
</body>
</html>
"""


def generate(md_path: Path, css_path: Path, out_path: Path, keep_html: Path | None) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    css_text = combined_css(css_path)
    body = md_to_html(md_text)
    title = "Richard van Zyl — CV"
    document = build_document(body, css_text, title)

    if keep_html is not None:
        keep_html.write_text(document, encoding="utf-8")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=document, base_url=str(md_path.parent)).write_pdf(str(out_path))
    print(f"Wrote {out_path} ({out_path.stat().st_size} bytes)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD, help="Source markdown")
    parser.add_argument("--css", type=Path, default=DEFAULT_CSS, help="Print stylesheet")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="Output PDF path")
    parser.add_argument(
        "--keep-html",
        type=Path,
        default=None,
        help="Optional path to write the intermediate HTML for debugging",
    )
    args = parser.parse_args()

    for path, label in ((args.md, "markdown"), (SHARED_CSS, "shared css"), (args.css, "css")):
        if not path.is_file():
            sys.stderr.write(f"Missing {label} file: {path}\n")
            return 1

    generate(args.md, args.css, args.out, args.keep_html)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
