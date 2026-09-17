# 0003 — Public downloads are PDF-only; DOCX unpublished

- **Status:** Accepted
- **Date:** 2026-09-17
- **Cost to reverse:** Costly — adding a published DOCX means a regenerable pipeline, README/site
  links, ignore-rule exceptions, and a second artefact that must stay in lockstep with `CV.md`;
  not a one-file force-add

## Context

Word/DOCX was previously published, then removed (PDF-only downloads). `.gitignore` blocks
`*.docx` (and most `*.pdf`) so only the two published PDFs under `downloads/` can be committed.
DOCX may still exist on disk for local editing. The question returned: why not put DOCX back in
the public CV repo and on the site?

## Options considered

| Option | Upside | Downside | Cost to reverse |
|---|---|---|---|
| Do nothing / keep PDF-only *(chosen)* | One public artefact; regenerable; content-guard can scan PDF text | Recruiters who insist on Word need an on-request send | Reversible for a one-off email; Costly if we later publish DOCX properly |
| Commit DOCX under `downloads/` without a pipeline | Quick | Opaque binary; drifts from `CV.md`; guard cannot scan it; agents force-add stale files | Costly — remove links and re-teach ignore rules |
| Published DOCX via checked-in generator (e.g. pandoc) | Word available from the site | Second source of truth forever; doubles release surface | Costly — delete links, stop regenerating, update docs |

## Decision

**Public downloads are PDF only.** DOCX is allowed locally for editing or on-request sends; it is
**gitignored** and **not linked** from the site or README.

Local rebuild of a Word file for personal use is documented in [`pdf/README.md`](../../pdf/README.md)
(output under gitignored `dist/`). That path must not be treated as a published download unless a
new ADR supersedes this one.

## Consequences

- Do not add DOCX links to `RichardvZyl.github.io` or this README.
- Do not force-add `*.docx` to git.
- If a published Word download is required later, add a generator + ADR first — do not commit a
  one-off export as canonical.
