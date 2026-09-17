# AGENTS.md

Canonical agent entry for the public CV/portfolio repo.

- How an AI should collaborate with Richard: `AI-CONTEXT.md`
- Public profile / CV / skills: `PROFILE.md`, `CV.md`, `SKILLSMATRIX.md`, `SKILLS-OVERVIEW.md`
- Public project list: `PROJECTS.md` (public remotes only)
- Private inventory: `PROJECTS.private.md` (git-ignored). Never copy private/client detail into public files.

This repository is PUBLIC. Other agent files in this folder (`CLAUDE.md`, `.cursorrules`, `.github/copilot-instructions.md`) reference this file rather than duplicating it.

## Skills Overview PDF (canonical style)

The downloadable Skills Overview look is **WeasyPrint + committed CSS**, not pandoc/xelatex and not an ad-hoc print HTML.

| Piece | Path |
|---|---|
| Content source | `SKILLS-OVERVIEW.md` |
| Print stylesheet (layout, fonts, margins, tables) | `scripts/skills-overview-print.css` |
| Generator | `scripts/generate-skills-overview-pdf.py` |
| Python deps | `scripts/requirements-pdf.txt` |
| Output | `downloads/Richard-van-Zyl-Skills-Overview.pdf` |

**Rules for agents**

- After editing `SKILLS-OVERVIEW.md`, regenerate with:
  `pip install -r scripts/requirements-pdf.txt && python3 scripts/generate-skills-overview-pdf.py`
- **Do not** invent a new pipeline (pandoc, Chrome print-to-PDF, inline one-off CSS). Style must come from `skills-overview-print.css` so regenerations stay visually identical when only markdown content changes.
- Change appearance only by editing `scripts/skills-overview-print.css` (and the markdown→HTML mapping in the generator if structure requires it). Keep **equal left/right page margins** (currently `14mm` all sides); table borders must not eat the right margin (`box-sizing: border-box` is required).
- Sync the site copy of the PDF when `RichardvZyl.github.io` still hosts it locally.

## Memory and workspace context (Perseus)

- **Vault** (shared across clients on this machine): `perseus_vault_*` MCP tools. Session start: `perseus_vault_context`. Durable facts: `perseus_vault_remember`. No secrets. Never remember anything that cannot appear in a public repo.
- **Context Engine** (this repo only): `perseus` MCP tools and `.perseus/context.md`. Do not reuse another project's briefing.