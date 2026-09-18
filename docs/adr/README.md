# Architecture decision records

Records are numbered sequentially and **never renumbered, reused or deleted**. A superseded
record stays, marked `Superseded by`, because the reasoning it captured is evidence about what
was known at the time.

Format and the "when is one required" test follow
[`engineering-standards` `standards/05-decision-records.md`](https://github.com/RichardvZyl/engineering-standards/blob/main/standards/05-decision-records.md)
(local Template Repository path: `…/Template Repository/standards`). Short version: required when
the decision is **hard to reverse**, not when it feels important — anything rated above
`Reversible` needs a record. Session rulings below include one `Reversible` record kept on
purpose so agents stop re-deriving it.

**This index is updated in the same commit that adds a record.**

| # | Title | Status | Cost to reverse | Date |
|---|---|---|---|---|
| [0001](./0001-weasyprint-canonical-pdf-pipeline.md) | WeasyPrint + committed CSS as the canonical PDF pipeline | Accepted | Costly | 2026-09-17 |
| [0002](./0002-canonical-download-home.md) | curriculum-vitae owns published PDF downloads; site links out | Accepted | Costly | 2026-09-17 |
| [0003](./0003-pdf-only-public-downloads.md) | Public downloads are PDF-only; DOCX unpublished | Accepted | Costly | 2026-09-17 |
| [0004](./0004-exclude-personality-frameworks-from-public-cv.md) | Exclude personality frameworks from the public CV pack | Accepted | Reversible | 2026-09-17 |
| [0005](./0005-dual-skills-pdfs.md) | Publish condensed and full skills PDFs (no MD for humans) | Accepted | Costly | 2026-09-18 |

<!-- Add newest at the bottom. Status: Proposed | Accepted | Superseded by NNNN | Deprecated.
     Cost to reverse: Reversible | Costly | One-way — must match the record header. -->

**Read the `Costly` / `One-way` rows first.** They are the constraints this pack has already
committed to.

## Creating one

1. Copy the shape from any existing record (or the upstream example in engineering-standards
   `templates/docs/adr/0001-example.md`) to the next number.
2. Fill Context, Options considered, Decision, Consequences.
3. Rate cost to reverse of the **chosen** option in the header, with a clause — matching that
   option's row in the table.
4. Add the index row above in the same commit.

**Options considered is not optional.** A record with one option is a note.
