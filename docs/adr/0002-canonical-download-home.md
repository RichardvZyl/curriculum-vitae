# 0002 — curriculum-vitae owns published PDF downloads; site links out

- **Status:** Accepted
- **Date:** 2026-09-17
- **Cost to reverse:** Costly — putting PDF copies back on the site (or pointing elsewhere)
  requires coordinated README / `index.html` / release changes; old
  `https://richardvzyl.github.io/*.pdf` URLs already 404 after the hygiene change

## Context

Three copies of the CV PDF disagreed within 48 hours: `downloads/` here, a dated GitHub release,
and a copy on `RichardvZyl.github.io`. The README pointed at the frozen release, so readers got
builds that later PRs had already replaced. A second copy on the site is what made silent drift
possible.

## Options considered

| Option | Upside | Downside | Cost to reverse |
|---|---|---|---|
| Do nothing | No URL churn | Drift continues | Reversible until the next wrong download ships |
| Keep PDFs on the site only | Simple Pages hosting | Source markdown lives here; site copy falls behind regenerations | Costly — sync chore forever |
| Dated GitHub releases as canonical | Immutable snapshots | Every regen needs a new tag + README edit; already failed once | Costly — tagging discipline |
| This repo's `downloads/` on `master` as canonical; site links via raw URLs *(chosen)* | One file next to the markdown that generates it; site cannot drift from a second blob | Breaking change for anyone who bookmarked site-root PDF paths | Costly — restore site copies and rewrite links |

## Decision

**Canonical published PDFs live only in this repository:**

- `downloads/Richard-van-Zyl-CV.pdf`
- `downloads/Richard-van-Zyl-Skills-Overview.pdf` (condensed)
- `downloads/Richard-van-Zyl-Skills-Matrix.pdf` (full) — see [0005](./0005-dual-skills-pdfs.md)

Served as:

- `https://raw.githubusercontent.com/RichardvZyl/curriculum-vitae/master/downloads/Richard-van-Zyl-CV.pdf`
- `https://raw.githubusercontent.com/RichardvZyl/curriculum-vitae/master/downloads/Richard-van-Zyl-Skills-Overview.pdf`
- `https://raw.githubusercontent.com/RichardvZyl/curriculum-vitae/master/downloads/Richard-van-Zyl-Skills-Matrix.pdf`

The site (`RichardvZyl.github.io`) **does not** keep local PDF copies. Its hero/contact buttons
use the URLs above. GitHub serves them as `application/octet-stream` with `nosniff`, so they still
download.

The release tag `cv-downloads-2026-09-14` is **stale** and must not receive new README or site
links. Deleting that release (and leftover remote branches that held superseded PDF blobs) is
cleanup, not a change to this decision.

## Consequences

- After regenerating a PDF, commit it under `downloads/` on `master` — that is what the site
  serves.
- Do not re-add `Richard-van-Zyl-*.pdf` to the site repo.
- External bookmarks to `https://richardvzyl.github.io/Richard-van-Zyl-*.pdf` break by design.
