# Projects & Portfolio — Richard van Zyl

> Public, open-source personal projects that showcase Richard's engineering approach.
>
> **Note to reviewers:** what you can see on this GitHub account is only part of the
> picture. Several repositories are **private** (proprietary, client, or pre-release work)
> and are **deliberately excluded** — see ["What's not shown here"](#whats-not-shown-here).
> Commercial work is described at a high, non-confidential level in [`CV.md`](./CV.md) and
> [`SKILLSMATRIX.md`](./SKILLSMATRIX.md).
>
> _Last updated: 2026-09-04._

---

## Active public projects

### CombinatorialOptimiser
**Repo:** https://github.com/RichardvZyl/CombinatorialOptimiser · **Stack:** .NET 10, C#, xUnit

A **dependency-free .NET combinatorial-optimisation library** plus a demo CLI, solving
problems across three domains — **Permutation** (TSP-style ordering), **SubsetSelection**
(0/1 knapsack), and **ConstraintAssignment** (graph colouring) — with **20+ solvers**
spanning four paradigms (Exact, Construction, Improvement, Reduction).

Highlights:
- Clean `ISolver<TProblem, TResult>` core abstraction; sync and `SolveAsync` (cancellable) APIs.
- A `SolverRegistry` that *recommends* a solver based on problem size, and enumerates
  all applicable solvers at a given size.
- Shared metaheuristic base classes (Simulated Annealing / Genetic Algorithm / ILS).
- Zero third-party dependencies in the library.
- The library project is **packable as NuGet**; it is **not** published to nuget.org.
- Solvers span Brute Force and Held–Karp (exact) through nearest-neighbour,
  2-opt/Or-opt improvement, and metaheuristics — a tour of the accuracy vs. runtime
  trade-off space.

Demonstrates: algorithm design, clean library architecture, paradigm breadth, and the
"pick the right tool for the size of the problem" thinking Richard applies to system design.

### engineering-standards
**Repo:** https://github.com/RichardvZyl/engineering-standards · **Stack:** PowerShell, Markdown

Engineering conventions in a form a repository can actually **consume** rather than merely
document. The `standards/` tree is vendored into downstream repositories and kept current by
an automated sync PR, so conventions propagate instead of drifting.

Demonstrates: treating standards as a versioned, distributable artefact — the same discipline
applied to code applied to the rules about code.

### pseudo-random-guaranteed-unique
**Repo:** https://github.com/RichardvZyl/pseudo-random-guaranteed-unique · **Stack:** T-SQL

A pseudo-random, **guaranteed-unique** encrypted code generator for SQL Server and PostgreSQL —
collision-free *by construction* via a keyed Feistel permutation, rather than by retry-on-collision.
Public for evaluation; proprietary licensing.

Demonstrates: reaching for a correctness guarantee from the structure of the algorithm instead of
defending against collisions at runtime — the same instinct behind the idempotency and
concurrency work described in `CV.md`.

### RichardvZyl.github.io
**Repo:** https://github.com/RichardvZyl/RichardvZyl.github.io · **Stack:** HTML, CSS, JS

Personal site — positioning, problems solved, capabilities, credentials, approach, ventures and
contact. GitHub Pages at https://richardvzyl.github.io/.

### curriculum-vitae *(this repo)*
**Repo:** https://github.com/RichardvZyl/curriculum-vitae

A human- **and** AI-consumable CV: structured profile, narrative CV, skills matrix, and
an AI-collaboration context file. Built so an assistant can do role-matching,
cover-letter generation, and interview prep without re-deriving context.

---

## Archived / historical

Kept public for continuity, but **not representative of current work** — they predate the
standards applied in the projects above. Do not treat these as strengths.

| Repo | Status |
|---|---|
| [`Abstractions_Deprecated`](https://github.com/RichardvZyl/Abstractions_Deprecated) | Archived. An early .NET abstractions library, superseded by a private successor. |
| [`ProgressiveTaxDemoApplication`](https://github.com/RichardvZyl/ProgressiveTaxDemoApplication) | Archived. 2022 demo. |
| [`DemoApplication`](https://github.com/RichardvZyl/DemoApplication) | Archived. Early interview demo. |

---

## What's not shown here

This public account is intentionally a **subset** of Richard's work. There are additional
private repositories not listed here because they are proprietary, client-owned, or
pre-release. Without exposing anything confidential, that private body of work currently
includes, at a high level:

- A **provider-agnostic EF Core data-access SDK** (repository / unit-of-work /
  specification contracts with strict CQRS read/write separation), built as a family
  of responsibility-scoped packages.
- A **schema-discovery + auto-API generator** producing GraphQL / gRPC / Swagger surfaces.
- A **quantitative trading / backtesting engine** (signal, Markov, execution, and
  backtester components).
- A **capabilities / orchestration runtime**.
- A **multi-tenant white-label banking core** (domain, core, API).
- Applied **routing optimisation** (weighted / prize-collecting / periodic TSP for
  field-rep scheduling), plus custom Roslyn analyzers and internal tooling.
- A **versioned AI engineering toolkit** — skills, agents, commands and hooks with a
  two-layer publish/capture model, of which `engineering-standards` is the public slice.

If you're an employer or collaborator and want to see more, Richard can **walk you
through the private repositories on request** or under NDA. The public projects above are
representative of the engineering standard applied across all of them.

> For the commercial systems (multi-tenant financial engine, integration layer over
> 150+ money processors, concurrency/ledger design), see `CV.md` §Experience.
