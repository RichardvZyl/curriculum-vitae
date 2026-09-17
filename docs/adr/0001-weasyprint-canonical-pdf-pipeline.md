# 0001 — WeasyPrint + committed CSS as the canonical PDF pipeline

- **Status:** Accepted
- **Date:** 2026-09-17
- **Cost to reverse:** Costly — regenerating every published PDF with a different engine, updating
  generators / CSS / AGENTS.md / CI expectations, and re-checking visual sign-off; no data migration,
  but the public download artefacts and agent runbooks all move together

## Context

Two PDF engines produced different looks for the same markdown:

- **pandoc → xelatex** produced the first published CV and Skills Overview (serif / LaTeX;
  metadata `Creator: LaTeX via pandoc`, `Producer: xdvipdfmx`).
- **WeasyPrint** was used later for Skills Overview formatting and for CV layout spacing
  (sans-serif HTML print; metadata `Producer: WeasyPrint 70.0`).

Side-by-side review chose **WeasyPrint (style B)** for the CV. Skills Overview was already on
WeasyPrint with equal page margins. Without a recorded pipeline, agents reintroduced pandoc or
one-off print HTML and the published files drifted within days.

Upstream decision-record rules live in engineering-standards
[`standards/05-decision-records.md`](https://github.com/RichardvZyl/engineering-standards/blob/main/standards/05-decision-records.md).

## Options considered

| Option | Upside | Downside | Cost to reverse |
|---|---|---|---|
| Do nothing (ad-hoc regen) | No process work | Drift between site, release, and `downloads/`; agents invent pipelines | Reversible — none until drift ships |
| pandoc + xelatex as canonical | Matches first release look; one CLI | Heavier TeX install; Skills Overview tables and CV spacing were signed off on WeasyPrint | Costly — reinstall TeX, rewrite scripts/CSS, regenerate both PDFs |
| WeasyPrint + committed CSS *(chosen)* | Matches signed-off CV and Skills Overview; CSS is diffable; Python deps are light | Not the original LaTeX look; needs `weasyprint` + `markdown` | Costly — change CSS/scripts and regenerate both published PDFs |
| Chrome headless print-to-PDF | Familiar | Flaky in CI/agents; no checked-in stylesheet of record | Costly — same as adopting any new pipeline |

## Decision

Published PDFs are generated only with **WeasyPrint**, driven by **committed CSS** and the
checked-in generators:

| Artefact | Content | Stylesheet | Generator |
|---|---|---|---|
| `downloads/Richard-van-Zyl-CV.pdf` | `CV.md` | `pdf/cv-print.css` | `scripts/generate-cv-pdf.py` |
| `downloads/Richard-van-Zyl-Skills-Overview.pdf` | `SKILLS-OVERVIEW.md` | `scripts/skills-overview-print.css` | `scripts/generate-skills-overview-pdf.py` |

Deps: `scripts/requirements-pdf.txt`. Rebuild notes and tool links: [`pdf/README.md`](../../pdf/README.md).

**pandoc + xelatex remains a documented historical / comparison path** so the original look can be
reproduced; it is not allowed to overwrite `downloads/` unless a new ADR supersedes this one.

## Consequences

- Agents must not invent pandoc / Chrome / inline one-off CSS for published downloads.
- Visual changes go through the CSS files (and the markdown→HTML mapping in the generators), then
  regenerate into `downloads/`.
- Skills Overview CSS keeps **equal left/right page margins** (`14mm`) and `box-sizing: border-box`
  so table borders do not eat the right margin.
- Content-guard scans published PDF text (`pdftotext`); CI installs `poppler-utils`.
