# CV PDF generation

Reproducible print layout for **`Richard-van-Zyl-CV.pdf`** only.

Skills Overview / skills-matrix PDFs are **out of scope** here — leave them alone unless deliberately regenerating that pipeline.

## Layout source of truth

| File | Role |
|---|---|
| [`../CV.md`](../CV.md) | Content |
| [`cv-print.css`](./cv-print.css) | Print spacing, alignment, typography |
| [`../scripts/generate-cv-pdf.py`](../scripts/generate-cv-pdf.py) | Markdown → HTML → WeasyPrint PDF |

## Regenerate

From the `curriculum-vitae` repo root:

```bash
pip install weasyprint markdown
python3 scripts/generate-cv-pdf.py
```

Output: `downloads/Richard-van-Zyl-CV.pdf`.

Optional debug HTML:

```bash
python3 scripts/generate-cv-pdf.py --keep-html /tmp/cv-print.html
```

Copy to the site repo root when publishing downloads:

```bash
cp downloads/Richard-van-Zyl-CV.pdf ../RichardvZyl.github.io/Richard-van-Zyl-CV.pdf
```

## Layout rules encoded in CSS

- Sub-headings (`h3` role titles, and content immediately under `h2`) have **no gap** before the following company line / body.
- Top margin on headings is **discarded after a page break** (`margin-break: discard`).
- Lists sit on the **left body edge** with a hanging indent (marker + wrapped lines align with the text column).
- Bold lead-ins inside list items stay **inline** — never `display: block` — so there is no blank band under the label.
