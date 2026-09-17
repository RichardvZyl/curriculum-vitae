# AGENTS.md

Canonical agent entry for the public CV/portfolio repo.

- How an AI should collaborate with Richard: `AI-CONTEXT.md`
- Public profile / CV / skills: `PROFILE.md`, `CV.md`, `SKILLSMATRIX.md`, `SKILLS-OVERVIEW.md`
- Public project list: `PROJECTS.md` (public remotes only)
- Private inventory: `PROJECTS.private.md` (git-ignored). Never copy private/client detail into public files.

This repository is PUBLIC. Other agent files in this folder (`CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`) reference this file rather than duplicating it.

## Downloadable PDFs (canonical style)

Both downloadable PDFs are **WeasyPrint + committed CSS**, not pandoc/xelatex and not ad-hoc print HTML. Shared deps: `scripts/requirements-pdf.txt`.

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

**Shared agent rules:** do not invent pandoc / Chrome print-to-PDF / one-off CSS. Sync site copies when `RichardvZyl.github.io` still hosts the PDFs locally.

## Memory and workspace context (Perseus)

- **Vault** (shared across clients on this machine): `perseus_vault_*` MCP tools. Session start: `perseus_vault_context`. Durable facts: `perseus_vault_remember`. No secrets. Never remember anything that cannot appear in a public repo.
- **Context Engine** (this repo only): `perseus` MCP tools and `.perseus/context.md`. Do not reuse another project's briefing.