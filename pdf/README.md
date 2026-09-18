# PDF / DOCX rebuild guide

Canonical decisions: [`docs/adr/0001`](../docs/adr/0001-weasyprint-canonical-pdf-pipeline.md),
[`0002`](../docs/adr/0002-canonical-download-home.md),
[`0003`](../docs/adr/0003-pdf-only-public-downloads.md).

## Tools (links)

| Tool | Role here | Link |
|---|---|---|
| **WeasyPrint** | **Canonical** PDF engine for published downloads | https://doc.courtbouillon.org/weasyprint/stable/ |
| **Python `markdown`** | MD → HTML before WeasyPrint | https://python-markdown.github.io/ |
| **Pandoc** | Historical PDF comparison (xelatex) + local DOCX export | https://pandoc.org/ |
| **TeX Live / XeLaTeX** | PDF engine for the historical pandoc path | https://tug.org/texlive/ · https://www.tug.org/xetex/ |
| **Poppler `pdftotext`** | Content-guard reads published PDFs | https://poppler.freedesktop.org/ |

Python pins for the canonical path: [`../scripts/requirements-pdf.txt`](../scripts/requirements-pdf.txt).

```bash
pip install -r scripts/requirements-pdf.txt
```

## Canonical publish path (WeasyPrint) — writes `downloads/`

These are the only commands that may update published PDFs. Prefer the one-shot helper below
(it also writes local DOCX under `dist/`).

```bash
# From curriculum-vitae repo root
python3 scripts/generate-cv-pdf.py
python3 scripts/generate-skills-overview-pdf.py
# Local Word (unpublished): python3 scripts/generate-local-docx.py
```

| Output | Stylesheet | Generator |
|---|---|---|
| `downloads/Richard-van-Zyl-CV.pdf` | [`cv-print.css`](./cv-print.css) | `scripts/generate-cv-pdf.py` |
| `downloads/Richard-van-Zyl-Skills-Overview.pdf` | `scripts/skills-overview-print.css` | `scripts/generate-skills-overview-pdf.py` |

Optional HTML debug for the CV:

```bash
python3 scripts/generate-cv-pdf.py --keep-html /tmp/cv-print.html
```

Layout rules encoded in `cv-print.css` (see also ADR 0001):

- Sub-headings sit tight above company / body lines.
- Top margin on headings is discarded after a page break (`margin-break: discard`).
- Lists use a hanging indent on the body column.
- Bold lead-ins in list items stay inline.

Skills Overview CSS keeps **equal 14mm** page margins and border-box tables.

## Historical / comparison path (pandoc + xelatex) — do not overwrite `downloads/` casually

Reproduces the original LaTeX look (`Creator: LaTeX via pandoc`). Output goes under gitignored
`dist/` unless you deliberately promote it via a new ADR.

```bash
# Install (Debian/Ubuntu example)
sudo apt-get install -y pandoc texlive-xetex texlive-fonts-recommended texlive-plain-generic

mkdir -p dist

pandoc CV.md -o dist/Richard-van-Zyl-CV.pandoc-xelatex.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=10pt \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue

pandoc SKILLS-OVERVIEW.md -o dist/Richard-van-Zyl-Skills-Overview.pandoc-xelatex.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=10pt \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V urlcolor=blue
```

Or: `python3 scripts/generate-historical-pandoc-pdfs.py` (same flags; writes `dist/`).

## Local Word / DOCX — unpublished (always with default rebuild)

Per ADR 0003, DOCX is **not** a public download. Output is under gitignored `dist/` for editing
or on-request sends only.

**Install pandoc** (once): https://pandoc.org/ — e.g. `sudo apt-get install -y pandoc`.

```bash
# Preferred: same one-shot as published PDFs (DOCX is included by default)
python3 scripts/rebuild-print-artefacts.py

# DOCX only
python3 scripts/generate-local-docx.py

# Equivalent manual commands
mkdir -p dist
pandoc CV.md -o dist/Richard-van-Zyl-CV.docx
pandoc SKILLS-OVERVIEW.md -o dist/Richard-van-Zyl-Skills-Overview.docx
```

| Output | Generator |
|---|---|
| `dist/Richard-van-Zyl-CV.docx` | `scripts/generate-local-docx.py` |
| `dist/Richard-van-Zyl-Skills-Overview.docx` | same |

Do **not** commit these files (`*.docx` is gitignored) and do **not** link them from the site.

## One-shot helper

```bash
python3 scripts/rebuild-print-artefacts.py              # WeasyPrint → downloads/ + DOCX → dist/
python3 scripts/rebuild-print-artefacts.py --skip-docx  # PDFs only
python3 scripts/rebuild-print-artefacts.py --all        # also historical pandoc PDFs → dist/
```
