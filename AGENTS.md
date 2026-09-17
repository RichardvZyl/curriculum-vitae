# AGENTS.md

Canonical agent entry for the public CV/portfolio repo.

- How an AI should collaborate with Richard: `AI-CONTEXT.md`
- Public profile / CV / skills: `PROFILE.md`, `CV.md`, `SKILLSMATRIX.md`, `SKILLS-OVERVIEW.md`
- Public project list: `PROJECTS.md` (public remotes only)
- Private inventory: `PROJECTS.private.md` (git-ignored). Never copy private/client detail into public files.
- **Session / pack rulings (ADRs):** [`docs/adr/`](./docs/adr/) — format per [engineering-standards `05-decision-records`](https://github.com/RichardvZyl/engineering-standards/blob/main/standards/05-decision-records.md) (Template Repository `standards/`).
- **Rebuild PDFs / local DOCX:** [`pdf/README.md`](./pdf/README.md) (tool links + WeasyPrint / pandoc / DOCX commands).

This repository is PUBLIC. Other agent files in this folder (`CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`) reference this file rather than duplicating it.

## Downloadable artefacts (canonical source)

**This repo (`curriculum-vitae`) owns the published downloads.** The site (`RichardvZyl.github.io`) does **not** keep local PDF copies — its hero/contact buttons link here:

- CV: `https://raw.githubusercontent.com/RichardvZyl/curriculum-vitae/master/downloads/Richard-van-Zyl-CV.pdf`
- Skills Overview: `https://raw.githubusercontent.com/RichardvZyl/curriculum-vitae/master/downloads/Richard-van-Zyl-Skills-Overview.pdf`

Same URLs are used from this repo’s README. After regenerating a PDF, commit it under `downloads/` on `master` — that is what the site serves. Do not re-add PDFs to the site repo.

| Published | Path | On the website? |
|---|---|---|
| CV PDF | `downloads/Richard-van-Zyl-CV.pdf` | Linked (points here) |
| Skills Overview PDF | `downloads/Richard-van-Zyl-Skills-Overview.pdf` | Linked (points here) |
| Word / DOCX | May exist locally for editing; `*.docx` is gitignored | **Not linked** — deliberately unpublished |

Word/DOCX is not a public download. Do not add DOCX links to the site or README. The dated GitHub release `cv-downloads-2026-09-14` is stale; do not point new links at it.

## Downloadable PDFs (canonical style)

Both published PDFs are **WeasyPrint + committed CSS**, not pandoc/xelatex and not ad-hoc print HTML. Shared deps: `scripts/requirements-pdf.txt`.

### CV PDF

| Piece | Path |
|---|---|
| Content source | `CV.md` |
| Print stylesheet | `pdf/cv-print.css` |
| Generator | `scripts/generate-cv-pdf.py` |
| Notes | `pdf/README.md` |
| Output | `downloads/Richard-van-Zyl-CV.pdf` |

- After editing `CV.md`, regenerate with:
  `pip install -r scripts/requirements-pdf.txt && python3 scripts/generate-cv-pdf.py`
- Change appearance only via `pdf/cv-print.css` (tight heading→content gaps, hanging list indents, `margin-break: discard` after page breaks). Do not invent a parallel pipeline.

### Skills Overview PDF

| Piece | Path |
|---|---|
| Content source | `SKILLS-OVERVIEW.md` |
| Print stylesheet | `scripts/skills-overview-print.css` |
| Generator | `scripts/generate-skills-overview-pdf.py` |
| Output | `downloads/Richard-van-Zyl-Skills-Overview.pdf` |

- After editing `SKILLS-OVERVIEW.md`, regenerate with:
  `pip install -r scripts/requirements-pdf.txt && python3 scripts/generate-skills-overview-pdf.py`
- Change appearance only via `scripts/skills-overview-print.css`. Keep **equal left/right page margins** (currently `14mm` all sides); table borders must not eat the right margin (`box-sizing: border-box` is required).

**Shared agent rules:** do not invent pandoc / Chrome print-to-PDF / one-off CSS for *published*
downloads. Never copy published PDFs back onto the site repo. Historical pandoc and local DOCX
rebuilds are documented in `pdf/README.md` and must not silently overwrite `downloads/`.

## Memory and workspace context (Perseus)

- **Vault** (shared across clients on this machine): `perseus_vault_*` MCP tools. Session start: `perseus_vault_context`. Durable facts: `perseus_vault_remember`. No secrets. Never remember anything that cannot appear in a public repo.
- **Context Engine** (this repo only): `perseus` MCP tools and `.perseus/context.md`. Do not reuse another project's briefing.