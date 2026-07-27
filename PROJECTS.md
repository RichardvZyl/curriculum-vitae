# Projects & Portfolio — Richard van Zyl

> Public, open-source personal projects that showcase Richard's engineering approach.
>
> **Note to reviewers:** what you can see on this GitHub account is only part of the
> picture. Several repositories and NuGet packages are **private** (proprietary,
> client, or pre-release work) and are **deliberately excluded** from this public list —
> see ["What's not shown here"](#whats-not-shown-here) below. Commercial work is
> described at a high, non-confidential level in [`CV.md`](./CV.md) and
> [`SKILLSMATRIX.md`](./SKILLSMATRIX.md).
>
> _Last updated: 2026-07-08._

---

## Open-source projects (publicly visible)

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
- Zero third-party dependencies in the library; packable as a NuGet package.
- Solvers span Brute Force and Held–Karp (exact) through nearest-neighbour,
  2-opt/Or-opt improvement, and metaheuristics — a tour of the accuracy vs. runtime
  trade-off space.

Demonstrates: algorithm design, clean library architecture, paradigm breadth, and the
"pick the right tool for the size of the problem" thinking Richard applies to system design.

### curriculum-vitae *(this repo)*
**Repo:** https://github.com/RichardvZyl/curriculum-vitae

A human- **and** AI-consumable CV: structured profile, narrative CV, skills matrix, and
an AI-collaboration context file. Built so an assistant can do role-matching,
cover-letter generation, and interview prep without re-deriving context.

---

## What's not shown here

This public account is intentionally a **subset** of Richard's work. There are
**additional private repositories and published-but-private NuGet packages** that are
not listed here because they are proprietary, client-owned, or pre-release. Without
exposing anything confidential, that private body of work currently includes, at a
high level:

- A **provider-agnostic EF Core data-access SDK** (repository / unit-of-work /
  specification contracts with strict CQRS read/write separation), shipped as a family
  of responsibility-scoped NuGet packages.
- A **schema-discovery + auto-API generator** producing GraphQL / gRPC / Swagger surfaces.
- A **quantitative trading / backtesting engine** (signal, Markov, execution, and
  backtester components).
- A **capabilities / orchestration runtime**.
- A **multi-tenant white-label banking core** (domain, core, API).
- Applied **routing optimisation** (weighted / prize-collecting / periodic TSP for
  field-rep scheduling), plus custom Roslyn analyzers and internal tooling.

If you're an employer or collaborator and want to see more, Richard can **walk you
through the private repositories and packages on request** or under NDA. The public
projects above are representative of the engineering standard applied across all of them.

> For the commercial systems (multi-tenant financial engine, integration layer over
> 150+ money processors, concurrency/ledger design), see `CV.md` §Experience.
