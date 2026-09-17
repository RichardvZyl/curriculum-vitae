# Richard van Zyl — Curriculum Vitae

**[⬇ CV (PDF)](https://raw.githubusercontent.com/RichardvZyl/curriculum-vitae/master/downloads/Richard-van-Zyl-CV.pdf)** ·
**[Skills overview (PDF)](https://raw.githubusercontent.com/RichardvZyl/curriculum-vitae/master/downloads/Richard-van-Zyl-Skills-Overview.pdf)** ·
**[richardvzyl.github.io](https://richardvzyl.github.io/)**

Human- and AI-consumable CV for a Solutions Architect / Technical Lead specialising in
high-throughput, multi-tenant financial systems (C#/.NET, SQL Server, Azure).

This is a **public repository for employers, recruiters, and collaborators** — structured so
both humans and AI assistants can do role matching, cover-letter generation, and interview prep
without re-deriving context.

> **Note:** what's public here is a **subset** of Richard's work. Additional repositories and
> packages are private (proprietary, client, or pre-release) and are deliberately not shown —
> see [`PROJECTS.md`](./PROJECTS.md). Detail available on request or under NDA.

## Contents

| File | What it is |
|---|---|
| [`PROFILE.md`](./PROFILE.md) | **Start here.** Structured profile and AI context — snapshot, summary, skills matrix, achievements, experience overview, honest skill boundaries. |
| [`CV.md`](./CV.md) | The CV in narrative form (summary, competencies, achievements, full role history, open source, education). |
| [`SKILLS-OVERVIEW.md`](./SKILLS-OVERVIEW.md) | Human-readable skills summary — source for the Skills Overview PDF. Canonical style: `scripts/skills-overview-print.css` via `scripts/generate-skills-overview-pdf.py` (see `AGENTS.md`). |
| [`SKILLSMATRIX.md`](./SKILLSMATRIX.md) | Full 2026 skills matrix with years of experience, a SQL performance-tuning deep-dive, and a project-by-project breakdown per employer. |
| [`AI-CONTEXT.md`](./AI-CONTEXT.md) | **For AI assistants.** How to work with Richard on engineering tasks — stack, coding & database standards, architectural defaults, and a self-update rule. |
| [`PROJECTS.md`](./PROJECTS.md) | Open-source portfolio, with an explicit note that additional **private** repos/packages exist and are excluded. |
| [`LICENSE`](./LICENSE) | All rights reserved — read for evaluation; do not republish as your own. |
| [`docs/adr/`](./docs/adr/) | Architecture decision records for this pack (WeasyPrint pipeline, download home, PDF-only, personality-framework rule). |
| [`pdf/`](./pdf/) | Print CSS + **rebuild guide** (WeasyPrint canonical, pandoc comparison, local DOCX) and [tool links](./pdf/README.md). |

## Regenerating print artefacts

**Canonical (publishes to `downloads/`):**

```bash
pip install -r scripts/requirements-pdf.txt
python3 scripts/rebuild-print-artefacts.py
```

**Also historical pandoc PDFs + local DOCX → `dist/` (gitignored, not published):**

```bash
python3 scripts/rebuild-print-artefacts.py --all
```

Full commands, stylesheet map, and tool links (WeasyPrint, Pandoc, XeLaTeX, Poppler):
[`pdf/README.md`](./pdf/README.md). Rulings: [`docs/adr/`](./docs/adr/).

## Contact

- **Email:** richardvzyl@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/richardvzyl
- **GitHub:** https://github.com/RichardvZyl
- **Site:** https://richardvzyl.github.io/

> Rate/CTC, phone number, and personal-background details are kept private and are available on
> request.
