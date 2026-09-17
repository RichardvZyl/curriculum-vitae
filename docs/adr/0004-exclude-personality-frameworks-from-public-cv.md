# 0004 — Exclude personality frameworks from the public CV pack

- **Status:** Accepted
- **Date:** 2026-09-17
- **Cost to reverse:** Reversible — remove or narrow the content-guard `personality test` rule and
  add the line back to markdown; no published contract or download pipeline depends on it

## Context

`scripts/content-guard.py` carries a **`personality test`** forbid rule (labelled public-CV noise,
not secret). Exact tokens live only in that file so this record does not re-trigger the guard.
The question was why those labels should stay off the CV. This pack is built for falsifiable
hiring evidence (roles, systems, outcomes). Personality-framework labels are self-report, weak as
performance signal, and invite stereotype filters.

Rated `Reversible`, so standards would not *require* an ADR; it is recorded anyway so agents stop
re-litigating the guard and so the ruling sits with the other session decisions.

## Options considered

| Option | Upside | Downside | Cost to reverse |
|---|---|---|---|
| Publish personality-framework labels on CV/site | Personal colour | Low signal; crowds out density; stereotype risk | Reversible — delete the line |
| Keep off public pack; allow private notes *(chosen)* | Guard stays aligned with density rule | None for hiring outcomes | Reversible — drop the pattern |
| Do nothing / undocumented convention | — | Agents reintroduce it | Reversible |

## Decision

Personality-framework labels covered by the content-guard **`personality test`** rule stay off the
public CV, site, and published PDFs. See `scripts/content-guard.py` for the exact pattern (keep
word boundaries so identifiers such as `ArgumentParser` are not false positives). Private coaching
/ interview notes are a different surface.

## Consequences

- Hits on those tokens fail CI on tracked public files (including published PDF text).
- Narrowing the pattern needs an explicit reason in the same commit (per content-guard header).
- Do not paste the forbidden tokens into docs that the guard scans unless the pattern is updated
  in the same change.
