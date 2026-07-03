# Richard van Zyl
### Solutions Architect / Technical Lead — Backend & Data-Intensive Systems

Pretoria, Gauteng, South Africa · richardvzyl@gmail.com · [linkedin.com/in/richard-van-zyl](https://www.linkedin.com/in/richard-van-zyl) · [github.com/RichardvZyl](https://github.com/RichardvZyl)

---

## Professional Summary

Solutions Architect and Technical Lead with **9+ years** architecting high-throughput,
multi-tenant financial systems where data integrity is non-negotiable — backed by a decade of
hands-on C#/.NET and T-SQL. Deep specialist in backend engineering and relational data:
execution-plan tuning, concurrency control, partitioning, and idempotent transaction design for
ledgers processing millions of transactions daily across Africa.

I own architecture end-to-end — from concurrency and multi-tenancy strategy through to CI/CD and
production telemetry — while leading delivery teams and bridging engineering with business
stakeholders. A problem solver at heart; languages and frameworks are simply tools. Regularly
handed the challenges others could not solve, from turning around failed legacy migrations to
designing the financial engine that replaced a legacy banking platform.

---

## Core Competencies

**Architecture & Design** — Domain-Driven Design (DDD), CQRS, Event Sourcing, Event-Driven
Architecture, Microservices, Multi-tenancy & Tenant Isolation, Idempotency / Exactly-Once
Processing, RESTful API design, Clean Architecture.

**Databases & Data** — Microsoft SQL Server, Azure SQL, T-SQL, SQL Performance Tuning (execution
plans, indexing, locking & isolation levels, deadlock resolution), Table Partitioning & Archiving,
In-Memory OLTP, PostgreSQL, MySQL, Redis (distributed caching), MongoDB, Entity Framework.

**Backend & Languages** — C# (.NET Core, .NET 6+, ASP.NET Core, ASP.NET Web API), MediatR,
FluentValidation, AutoMapper, Polly; SQL / T-SQL; TypeScript, JavaScript, Node.js.

**Messaging & Integration** — Azure Service Bus, RabbitMQ, API Gateway (Azure API Management),
SignalR / WebSockets.

**Cloud, DevOps & Observability** — Microsoft Azure, Azure DevOps, Docker, AKS / Kubernetes, Azure
CI/CD, GitHub, Trunk-based & GitFlow branching, Feature Flags, Azure Monitor / Application Insights
/ Log Analytics, Elastic Stack (ELK) / Serilog.

**Security & Compliance** — OAuth2 / OpenID Connect / JWT, Role-Based Access Control (RBAC), KYC /
AML domains, SOX-aligned data segregation, data-protection-aware design (POPIA / GDPR).

**Testing & Tooling** — xUnit, NUnit, Moq, Integration Testing (TestContainers); Enterprise
Architect (UML), Swagger, Postman, SSRS; Angular, Angular Material; Agile, Scrum.

---

## Selected Achievements

- **Architected a multi-tenant, white-label financial engine** serving two separate legal entities
  (Betway and Jackpot City) from a single, configuration-driven codebase — with per-entity database
  isolation and per-brand schema separation to satisfy SOX-aligned segregation.
- **Sustained deposit volumes in excess of €10M on peak trading days**, absorbing both steady
  casino throughput and large spikes during live sporting events — transaction volumes that
  exceeded those of conventional banking workloads.
- **Eliminated double-spend race conditions** under heavy contention by designing idempotent,
  exactly-once withdrawal processing with rowversion-based optimistic concurrency on the ledger.
- **Solved problems others had abandoned:** completed a .NET 6 migration that had been attempted
  and rolled back by previous developers, and resolved a 2-year Angular Universal SEO blocker in
  one week.
- **IKM C# Assessment:** 73rd percentile of all test takers (assessed twice, six months apart).

---

## Professional Experience

### Solutions Architect / Technical Lead — Core Financial Systems
**Raging River Trading (Pty) Ltd** · Fintech / Gaming · Dec 2022 – Apr 2026

Led the architectural transformation of core financial systems, replacing a legacy banking
platform with a modern, white-label engine handling high-volume transactions across Africa's
largest gaming brands. Architecturally responsible for the processing flow, multi-tenancy
strategy, and concurrency design, working in close partnership with the Enterprise Architect.

- **Multi-tenancy & data segregation:** Designed a configuration-driven engine serving multiple
  legal entities from one codebase. Each legal entity held its own database, and every brand (by
  country) lived in its own schema sharing a common structural design; the correct database and
  schema were resolved per request via a brand identifier, behind load-balanced, round-robin
  instances with health checks — purpose-built for SOX-aligned separation.
- **Concurrency & ledger integrity:** Designed exactly-once, idempotent withdrawal processing to
  prevent double spends. Each request created an attempt record keyed to a unique identifier; on
  confirmation that identifier drove the ledger deduction, guarded by a rowversion (SQL timestamp)
  optimistic-concurrency check so updates only succeeded if the row was unchanged since read.
  Supported both back-office-reviewed and automated "auto-cash-in" approval flows.
- **High-throughput scaling:** Engineered for sustained throughput and live-event spikes using
  hash-partitioned work queues (partitioning by account so the running-balance constraint could be
  validated against a subset), with multiple consumers converging on a single source of truth at a
  controlled write rate.
- **Performance & storage strategy:** Applied in-memory tables with non-sequential keys and tuned
  fill factors on high-contention paths, and implemented tiered partitioning with progressive
  cold-archiving (detaching yearly partitions into separate databases on colder servers) to meet
  multi-year regulatory retention while keeping hot ledger tables performant.
- **Resilience:** Used exponential backoff with retries, circuit breakers, and dead-letter queues
  to prevent thundering-herd failures, on high-availability clusters with redundant storage.
- **Integration layer:** Contributed to the layer abstracting 150+ individual money processors,
  routing online (callback/polling) and offline (e.g. USSD-reconciled) deposit and withdrawal
  flows reliably.
- **Delivery & operations:** Practised trunk-based development with feature flags; defined build
  pipelines and shipped to production several times daily via automated CI/CD, with canary
  releases, health checks, and early-warning telemetry.
- **Stakeholders:** Acted as the bridge between engineering and the business (product owners,
  business analysts, marketing, client retention), translating feature needs into a sustainable
  architecture without sacrificing long-term integrity for short-term wins.

### Software Developer (Specialist Problem-Solver)
**Dotcom Software Solutions** · Fintech consulting · Jan 2022 – Dec 2022

Specialist problem-solver for complex challenges other team members could not resolve, within the
fintech consulting space for clients including Nedbank, Standard Bank, and PSG Wealth.

- **Legacy upgrade (Standard Bank – Schemes Bot):** Upgraded the Schemes (Stokvel / Chama)
  BotFramework backend from .NET Standard to .NET 6, resolving critical breaking changes and
  package dependencies — previously attempted and rolled back by others. Live and stable in
  production since February 2022. Also handled monetization design and payment validations.
  _(Azure SQL, BotFramework, C# .NET Standard, MediatR, Q&A Maker.)_
- **Angular Universal SSR (PSG Wealth):** Implemented server-side rendering to resolve a 2-year SEO
  bottleneck in one week. _(C# .NET 6, Angular, Azure SQL, BotFramework, Docker, Node.js, Umbraco
  CMS, MediatR, Bootstrap / Material.)_

### Senior Developer / Business Analyst / Team Lead
**Payteq (Pty) Ltd** · Fintech · Apr 2020 – Jan 2022

- **GoTrips (Team Lead | Full Rewrite):** Led the ground-up rewrite of a struggling platform,
  eliminating years of technical debt and introducing proper coding standards, design principles,
  and performance optimisations. _(C# .NET Core API, PostgreSQL, Angular, Azure CI/CD,
  FluentValidation, Azure Functions.)_
- **Veriseal (Solo Migration):** Single-handedly migrated a critical compliance platform (KYC,
  AML, mass payments, bank-account verification) from legacy ASP.NET to .NET Core API with Angular
  8, with meticulous attention to data integrity and security. _(.NET Core, SQL, SSRS,
  FluentValidation, AutoMapper.)_
- **GoBills (Team Lead):** Led development of a scalable business-management solution (inventory,
  POS, financials) with a sophisticated RBAC system governing permissions and client access.
  _(.NET Core API, Angular 8, Identity Framework, Dependency Injection, custom CMS, Bootstrap /
  Angular Material.)_
- **Interchange IDE & Insight Server:** Go-to consultant for a highly scalable messaging-middleware
  integration platform with RBAC, providing ongoing support and maintenance on a SaaS basis.

### Software Developer / Business Analyst
**iPlan Global** · Supply Chain / Manufacturing / Mining / Industrial / Automation · Oct 2017 – Apr 2020

Delivered tailored solutions across Supply Chain, Manufacturing, Mining, and Industrial sectors as
both developer and analyst, including solution-architecture design.

- **Consolidated Job Dashboard:** Automated a previously manual, error-prone supply-chain
  consolidation process. _(VBScript, SQL.)_
- **Espresso Quote Application:** Solo full-stack mobile quoting app with integrated email delivery
  and manager-approval workflows. _(C# .NET, Entity Framework, MVC, jQuery, AJAX, JavaScript, SQL.)_
- **ASP.NET Food Portal:** Distributed compliance/tracking system for farmers to log deliveries and
  track poison-testing results, enforcing user security across multiple locations. _(ASP.NET, C#
  .NET, XAML/MVVM.)_
- **Espresso RepCheckIn:** Rep-tracking and route-optimisation system with tiered priority visit
  lists. _(JavaScript, C# .NET, jQuery, MVC, AJAX.)_

### Software Developer (C# .NET)
**Novigo (Pty) Ltd** · Recruitment · Apr 2017 – Oct 2017

Sole developer and IT administrator for a recruitment firm: designed, built, and deployed a
complete ERP from the ground up, including Linux server setup, domain hosting, and general IT
support. _(C# .NET WinForms, MySQL, Linux.)_

---

## Notable Clients Engaged (Across Consulting Roles)

Bankserv (now PayInc), Standard Bank, Nedbank, PSG Wealth, Libstar Holdings, Translution.

---

## Certifications, Education & Profile

- **IKM C# Assessment:** 73rd percentile of all test takers (assessed twice, six months apart).
- **National Diploma — IT: Software Development:** Varsity College, 2014–2016.
- **DISC & Values Index:** High D (decisive, results-driven) / High I (communicative) / Low S
  (adaptable, thrives in change) / Moderate C. Motivators: Very High Theoretical and Political;
  pragmatic and results-focused.
