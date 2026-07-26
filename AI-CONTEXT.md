# AI Collaboration Context — Working with Richard van Zyl

> **Purpose.** This is the operational companion to `PROFILE.md`. Where `PROFILE.md`
> frames Richard for recruiters and role-matching, this file tells an AI assistant
> *how to actually work with him* on engineering tasks — his stack, standards,
> architectural defaults, and the way he likes help delivered. Load this before
> writing code, reviewing designs, or reasoning about his systems.
>
> _Public, non-proprietary. No client data, credentials, or private project internals._
> _Last updated: 2026-07-08._

---
## 1. Who I'm assisting

Richard is a **Solutions Architect / Technical Lead** specialising in **high-throughput,
multi-tenant financial systems** (ledgers, payments, gaming/fintech) where **data
integrity is non-negotiable**. He thinks in terms of concurrency, consistency,
contention, and correctness first — features second. Treat him as a senior engineer:
he wants the *right tool for the job* and the reasoning behind a recommendation, not
a beginner walkthrough.

## 2. How to respond to me

- **Be concise and direct.** Cut filler. If a sentence can be removed without losing
  meaning, remove it. He has explicitly asked for this.
- **Lead with the answer / recommendation,** then justify. Don't bury the conclusion.
- **Show trade-offs.** For any non-trivial choice (library, pattern, index strategy,
  isolation level) give the pros/cons and name the winner for *his* context.
- **Assume depth.** Skip 101-level explanations of C#, SQL, DDD, CQRS, etc. unless asked.
- **Push back when warranted.** He values honest technical disagreement over agreement.
- **Prefer correctness under concurrency** over cleverness or brevity of code.

## 3. Primary stack

| Layer | Tools / versions |
|---|---|
| Language | **C# .NET**, T-SQL; some TypeScript/Node |
| Data | **SQL Server / Azure SQL** (primary), **PostgreSQL**, Redis, MongoDB |
| ORM / access | **Entity Framework Core**; custom repository/UoW/specification SDK (`Bedrock.*`) |
| Patterns | DDD, CQRS, Event Sourcing/EDA, SAGA, Clean Architecture, Result types |
| Messaging | Azure Service Bus, RabbitMQ; gRPC, REST, SignalR |
| Cloud/DevOps | Azure, Azure DevOps + GitHub, Docker, AKS, CI/CD, feature flags |
| Testing | xUnit, NUnit, Moq, TestContainers (integration) |
| Observability | Serilog, App Insights / Log Analytics (KQL), ELK |

## 4. Architecture & design defaults

- **Multi-tenancy is a first-class concern.** Assume tenant isolation / data
  segregation is required (per-DB or per-schema). Never let a query cross tenants.
- **CQRS read/write separation** — reference the read side only where a component
  must be physically incapable of writing.
- **Result/outcome types over exceptions** for expected failures (see `Bedrock.Results`).
- **Idempotency / exactly-once** for anything touching money: attempt records keyed to
  a unique id, guarded by **rowversion optimistic concurrency** on the ledger row.
- **Design for contention:** hash/partition work by account so running-balance
  invariants validate against a subset; converge on a single source of truth at a
  controlled write rate.
- Favour **composition, small responsibility-scoped packages, and explicit contracts**
  over large god-services.

## 5. Database standards (he cares deeply here)

- **Money is `decimal`, never `double`/`float`.**
- **SARGable predicates**; avoid scalar UDFs in hot paths; rewrite correlated
  subqueries as joins; prefer `EXISTS` over `IN` where appropriate.
- **Indexing:** clustered/non-clustered/filtered/covering chosen deliberately; watch
  last-page insert contention (avoid sequential hot keys on high-insert tables — use
  non-sequential keys / tuned fill factors).
- **Concurrency:** choose isolation levels consciously (READ COMMITTED SNAPSHOT vs
  SERIALIZABLE); design to *avoid* deadlocks, not just catch them.
- **Scale:** table partitioning by date/tenant, progressive cold-archiving for
  regulatory retention, In-Memory OLTP for high-contention paths.
- **Verify with the plan:** reason from execution plans, `SET STATISTICS IO/TIME`,
  wait stats — not guesses.

## 6. Engineering hygiene

- **Coding style** follows the repo `.editorconfig`: 4-space indent, CRLF, `System.*`
  usings first, no unnecessary usings (IDE0005 = warning), no final newline.
- **Git:** trunk-based / GitFlow, feature flags, small reviewable commits, build +
  test green before commit. Respect any repo `AGENTS.md` / `CLAUDE.md` / `.sixth/skills`.
- **Compliance-aware:** POPIA / GDPR / SOX-aligned segregation. Never suggest logging
  PII, secrets, or cross-tenant data.
- **Tests matter:** prefer xUnit + TestContainers for anything touching the DB.

## 7. Do / Don't

**Do:** recommend the right tool with trade-offs · reason about concurrency and query
plans · keep tenant isolation intact · use `decimal` for money · keep answers tight.

**Don't:** expose client/proprietary details in public artifacts · invent numbers or
benchmarks · hand-wave over race conditions · pad responses · assume a single-tenant
happy path.

## 8. Keeping this current — **update rule**

This file, `PROFILE.md`, `PROJECTS.md`, and the git-ignored `PROJECTS.private.md`
are living context. Refresh them whenever the facts change:

1. **Trigger a refresh when** a project is added/removed/renamed in the linked
   `Repos/` directory, a repo flips public⇄private, the stack or standards change, or
   Richard states a new preference/decision worth remembering.
2. **Keep public files public.** Only name a project by its real repo in `PROJECTS.md`
   if its GitHub/remote is **public**. Anything private, local-only, or client-related
   goes in `PROJECTS.private.md` (matches the `*.private.md` gitignore — never
   committed) or is omitted entirely.
3. **Verify before writing.** Confirm a repo's public/private status (e.g.
   `git ls-remote` anonymously, or the remote host) before promoting it to a public file.
4. **Stamp the date** (`Last updated:`) on any file you edit, and mirror new files into
   the `README.md` contents table.
5. **Don't duplicate** — update the existing file rather than creating parallel copies.

_An AI assistant asked to "update my context" should re-scan `Repos/`, re-check
public/private status, and apply the rules above._
