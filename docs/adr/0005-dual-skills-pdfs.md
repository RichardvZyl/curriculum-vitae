# 0005 — Publish condensed and full skills PDFs (no MD for humans)

- **Status:** Accepted
- **Date:** 2026-09-18
- **Cost to reverse:** Costly — third published PDF, ignore-rule exception, site download
  chooser, and agent runbooks all move together; dropping the full matrix means re-teaching
  readers to open markdown again

## Context

Skills Overview was a condensed PDF that pointed hiring readers at `SKILLSMATRIX.md` for the
dense detail. Rule: humans must not be sent to markdown; condensed and full must both exist as
regenerable human-facing artefacts.

## Options considered

| Option | Upside | Downside | Cost to reverse |
|---|---|---|---|
| Keep one PDF; strip the MD pointer only | Small diff | Loses the dense matrix for humans; “fixes” by deletion | Costly — rebuild dual pack later |
| Full matrix PDF local-only under `dist/` | Fast for agents | Hiring readers still only get condensed | Costly — promote + site links |
| Publish both under `downloads/`; site chooser *(chosen)* | Condensed + full without MD; matches CV download pattern | One more committed binary + CSS/generator | Costly — remove PDF, links, exceptions |

## Decision

Two published skills PDFs (WeasyPrint + committed CSS):

| Artefact | Role | Source | Output |
|---|---|---|---|
| Skills Overview | **Condensed** | `SKILLS-OVERVIEW.md` | `downloads/Richard-van-Zyl-Skills-Overview.pdf` |
| Skills Matrix | **Full / uncondensed** | `SKILLSMATRIX.md` | `downloads/Richard-van-Zyl-Skills-Matrix.pdf` |

Generators: `scripts/generate-skills-overview-pdf.py`, `scripts/generate-skills-matrix-pdf.py`.
Local DOCX for both under gitignored `dist/` via `scripts/generate-local-docx.py`.

The site offers an explicit chooser (Overview condensed / Matrix full), linking raw `master`
`downloads/` URLs — no PDF copies on the site. Published PDF sources and generators must not
direct readers to `.md` files.

Amends the artefact lists in [0001](./0001-weasyprint-canonical-pdf-pipeline.md) and
[0002](./0002-canonical-download-home.md).

## Consequences

- After editing either skills markdown, regenerate the matching PDF (or run
  `rebuild-print-artefacts.py`) and commit under `downloads/`.
- Interview-only rows marked omit-from-CV/site are stripped in the matrix PDF generator, not
  left for the reader to ignore.
- Do not reintroduce “see SKILLSMATRIX.md” (or similar) into Overview source that prints.
