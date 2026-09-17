# Richard van Zyl — Skills Matrix (2026)

Professional years of experience, a SQL performance deep-dive, and a project-by-project breakdown
per employer.

> **Years column.** Professional years only, counted from paid work starting **April 2017** — nothing
> exceeds **9**. Formal study (Varsity College, 2014–2016) is not counted. Engagement-tied skills
> (PostgreSQL, Redis, MongoDB, Azure Functions) use that engagement’s span, not the whole career.

| Section | What’s in it |
|---|---|
| [Skills by area](#skills-by-area) | Grouped tables, strongest first within each group |
| [SQL performance deep-dive](#deep-dive-sql-performance-tuning) | Execution plans, indexing, locking, scale patterns |
| [Employment & projects](#employment--projects) | Employer metadata, duties, and project cards |

---

## Skills by area

Within each table, rows are ordered by years (highest first).

### Languages

| Skill | Years |
|---|---:|
| C# / .NET | 9 |
| T-SQL | 9 |
| PostgreSQL | 7 |
| TypeScript | 5 |
| JavaScript | 5 |
| KQL | 5 |
| Batch Script | 5 |
| Visual Basic .NET | 3 |
| Java | 2 |

### Data formats

| Skill | Years |
|---|---:|
| JSON | 9 |
| XML | 8 |
| XAML | 7 |
| YAML | 6 |
| HTML | 3 |

### Databases & data engineering

| Skill | Years |
|---|---:|
| SQL Server / SSMS | 9 |
| SQL performance tuning | 8 |
| Azure SQL | 7 |
| MySQL Workbench | 6 |
| Azure Data Studio | 6 |
| Redis (distributed caching) | 5 |
| SSRS | 5 |
| MongoDB | 4 |
| Table partitioning & archiving | 4 |
| In-Memory OLTP | 4 |

### Architecture & design

| Skill | Years |
|---|---:|
| Clean Architecture | 9 |
| Domain-Driven Design (DDD) | 8 |
| Microservices | 7 |
| Multi-tenancy / tenant isolation | 7 |
| CQRS | 6 |
| Event-driven architecture | 5 |
| Idempotency / exactly-once processing | 4 |

### Business analysis & solution design

| Skill | Years |
|---|---:|
| Business & problem-domain analysis | 9 |
| Requirements specification (BRS / URS / FRS / TRS) | 9 |
| Solution design & solution architecture | 9 |
| Technical documentation (audience-tailored) | 9 |
| Stakeholder engagement & translation | 8 |
| Process & system modelling (UML) | 8 |

### Backend frameworks & libraries

| Skill | Years |
|---|---:|
| Entity Framework | 9 |
| MediatR | 7 |
| AutoMapper | 6 |
| FluentValidation | 6 |
| ASP.NET | 3 |
| Circuit breaker (Polly) | 3 |
| SignalR / WebSockets | 3 |

### Frontend & UI

| Skill | Years |
|---|---:|
| Angular | 6 |
| Angular Material | 6 |
| Ajax | 6 |
| MVC | 5 |
| Node.js | 5 |

### Delivery practices

| Skill | Years |
|---|---:|
| Scrum | 8 |
| Unit testing (xUnit / NUnit / Moq) | 6 |
| OAuth2 / OpenID Connect / JWT | 6 |
| Integration testing (TestContainers) | 5 |
| Feature flags (Azure App Configuration) | 4 |

### Cloud, DevOps & tooling

| Skill | Years |
|---|---:|
| Visual Studio | 9 |
| VS Code | 9 |
| GitHub | 9 |
| Azure DevOps (previously TFS) | 9 |
| Postman | 9 |
| Swagger | 9 |
| Enterprise Architect (UML) | 8 |
| Azure CI/CD | 7 |
| Docker | 7 |
| Pipeline-as-code (Azure DevOps YAML) | 6 |
| Message queues (Azure Service Bus / RabbitMQ) | 6 |
| Telerik | 6 |
| Azure Monitor / Log Analytics / App Insights | 5 |
| Microsoft Azure Insights | 5 |
| New Relic (APM, release tracking, alerting) | 4 |
| API Gateway (Azure API Management) | 4 |
| Elastic Stack (ELK) / Serilog | 4 |
| OpenTelemetry | 3 |
| Grafana | 3 |
| Graylog | 3 |
| DevExpress | 3 |

### Security & compliance

| Skill | Years |
|---|---:|
| Role-based access control (RBAC) | 8 |
| Data-protection-aware design (POPIA / GDPR) | 5 |
| SOX-aligned data segregation | 4 |

---

## Deep dive: SQL performance tuning

**8 years** · High-volume financial ledger systems integrating 150+ money processors across African markets.

| Sub-skill | Focus |
|---|---|
| Execution plan analysis | SHOWPLAN, `SET STATISTICS IO` / `TIME`; spotting scans, key lookups, and high-cost operators |
| Indexing strategy | Clustered, non-clustered, filtered, and covering indexes; fragmentation and rebuild / reorganise decisions |
| Locking & concurrency | Isolation levels (READ COMMITTED → SNAPSHOT); deadlock detection via Profiler / Extended Events |
| Tuning patterns | Correlated subqueries → joins; INNER JOIN vs EXISTS; SARGable predicates; avoiding scalar UDFs |
| Design for scale | Date/tenant partitioning; indexed / materialised views; high-volume batch inserts (ledger entries) |
| In-Memory OLTP | Memory-optimised tables and natively compiled procedures on high-contention paths |
| Query Store | Regression tracking, forced parameterization, plan forcing |
| Health monitoring | `sys.dm_os_wait_stats`, `sys.dm_db_index_usage_stats`, `sp_WhoIsActive` |

---

## Employment & projects

Each employer block uses the same shape: metadata → duties → projects (role line, summary, tech).

### Yuno Technologies

| Field | Detail |
|---|---|
| Industry | Digital consultancy |
| Role | Co-owner / Solutions Architect |
| Period | Apr 2026 – present |
| Consulting | Yes (client names held private) |

**Duties**
- Half-owner; leads technical delivery — architecture, backend engineering, and security design across client platforms.
- **Current production:** four-plane deployment topology with one-way initiation; BFF holding session rather than tokens; response-only identity plane on Keycloak; containerised platform across environments.
- **Phase 2 / planned:** inter-plane trust via mTLS / SPIFFE/SPIRE behind a documented interim.
- **Under evaluation:** ledger-plane isolation via KVM-backed microVM separation so a container escape in an adjacent workload cannot reach the ledger.
- ADRs with formal supersession across topology changes.

**Tech:** .NET · Vite / React · PostgreSQL · Redis · RabbitMQ · gRPC · Django / DRF · Azure Functions · Blob Storage · Keycloak · Prometheus / Grafana / ELK

---

### Raging River Trading (Pty) Ltd

| Field | Detail |
|---|---|
| Industry | Fintech / Gaming |
| Role | Solutions Architect / Technical Lead — Core Financial Systems *(payroll title: Software Developer)* |
| Period | Dec 2022 – Mar 2026 |
| Consulting | No |
| Leaving | Voluntary severance during a post-acquisition restructure *(interview context only — omit from CV/site)* |

**Duties**
- Led the rewrite of a legacy banking platform into a white-label financial engine for deposits & withdrawals across African markets (including Betway and Jackpot City).
- Engineered for horizontal and vertical scale under concurrent ledger load.
- Integration platform for 150+ money processors — IronPython marshalling in .NET; rewrote per-integration isolation to stop shared thread-pool / socket exhaustion.
- Migrated ~150 million records on a peak-trading Saturday with no New Relic Apdex drop.

#### Project — Core Financial Systems
**Solutions Architect / Technical Lead · Team 1–4 · Backend**

Full-scale rewrite to a white-label engine handling deposits & withdrawals for multiple brands. Horizontal scale with APIs that safely touch a concurrent ledger. Schema-per-brand under one SQL Server (separate databases priced out); transactional outbox to per-brand queues with dead-lettering.

**Tech:** Azure SQL · C# / .NET · Docker · RabbitMQ · EF Core

#### Project — Integration layer & back-office APIs
**Solutions Architect / Technical Lead · Team 5 · Backend**

Integration layer abstracting 150+ money processors. Back-office APIs for safe concurrent ledger access under high volume.

**Tech:** C# / .NET · Azure SQL

#### Project — High-availability & concurrency design
**Solutions Architect / Technical Lead · Team 1 · Backend**

HA architecture for concurrent financial transactions — idempotent attempt records with rowversion optimistic concurrency on the ledger.

**Tech:** C# / .NET · Azure SQL

---

### MeterMo

| Field | Detail |
|---|---|
| Industry | Utilities — automated electricity, water and gas metering & reporting |
| Role | Software Developer |
| Period | Apr 2022 – Dec 2022 |
| Consulting | No |
| Leaving | Mandate complete; sought a larger engineering team |

**Duties**

Platform modernisation across the metering estate. Migrated six projects from TFS to Azure DevOps and upgraded frameworks/packages; maintained two APIs, two cross-platform field apps (Xamarin, Cordova), and two websites.

**Tech:** C# / .NET · ASP.NET · Angular · Xamarin · Cordova · Azure DevOps · TFS

---

### Dotcom Software Solutions

| Field | Detail |
|---|---|
| Industry | Consulting (Fintech) |
| Role | Software Developer (Specialist Problem-Solver) |
| Period | Jan 2022 – Apr 2022 |
| Consulting | Yes |
| Leaving | No longer remote / not a culture fit |

**Duties**

Specialist problem-solver for challenges others could not resolve — full-stack fintech delivery for Nedbank, Standard Bank, and PSG Wealth. Business analysis including Schemes Bot monetisation design and payment validations.

#### Project — Schemes Bot (Standard Bank)
**Software Developer · Team 5 · Backend · Jan–Feb 2022**

BotFramework backend upgrade **to .NET 6 from .NET Standard**, including dependency updates and breaking-change fixes. Prior attempts had been rolled back; completed and live in production.

**Tech:** Azure SQL · BotFramework · C# / .NET 6 · MediatR · QnA Maker *(historical / retired)*

#### Project — PSG Wealth website
**Software Developer / Analyst / Architect · Team 6 · Backend · Feb–Mar 2022**

Angular Universal SSR for SEO — unblocked a two-year struggle in one week.

**Tech:** Docker · Angular · Bootstrap · Material · Node.js · C# / .NET 6 · Umbraco CMS

---

### Payteq

| Field | Detail |
|---|---|
| Industry | Fintech |
| Role | Senior Developer / Business Analyst / Team Lead |
| Period | Apr 2020 – Jan 2022 |
| Consulting | No |
| Leaving | Career growth |

**Duties**

Full-stack work on EDI, GoTrips, and Veriseal; business analysis with the BA team; team lead on the GoTrips rewrite, optimisation, and architecture.

#### Project — GoTrips
**Software Developer / Analyst / Team Lead · Team 5 · Full stack · Jan 2021 – Jan 2022**

Ground-up rewrite eliminating accumulated technical debt; coding standards, design principles, performance work, and automation for a maintainable system.

**Tech:** C# / .NET Core API · PostgreSQL · Azure CI/CD · FluentValidation · Angular · Azure Functions

#### Project — Veriseal
**Software Developer / Analyst / Architect · Team 1 · Full stack · side project, migrated opportunistically**

Independently migrated a critical compliance platform (KYC, AML, mass payments, bank-account verification) from legacy ASP.NET to .NET Core API with Angular 8.

**Tech:** C# / .NET Core · SQL · SSRS · Angular · ASP.NET · .NET Framework · FluentValidation · AutoMapper

#### Project — GoBills
**Team Lead · Team 2 · Full stack · Apr 2020 – Jan 2021**

Business-management solution (inventory, POS, financials) with sophisticated RBAC for permissions and client access.

**Tech:** C# / .NET Core API · Identity Framework · DI · custom CMS · Angular 8 · Bootstrap · Angular Material

#### Project — Interchange IDE & Insight Server
**Development & maintenance · Team 2 · Support**

Messaging-middleware integration platform with RBAC; ongoing SaaS support and maintenance.

**Tech:** SQL · C# / .NET Core · IP microservices / integrations

---

### iPlan Global

| Field | Detail |
|---|---|
| Industry | Supply chain / manufacturing / farming / industrial / automation |
| Role | Software Developer / Business Analyst |
| Period | Oct 2017 – Apr 2020 |
| Consulting | Yes |
| Leaving | Career growth |

**Duties**

Team and solo delivery; productivity automation; BA work across mining, industrial, supply chain, manufacturing, and sales — needs analysis, domain analysis, solution design and architecture.

#### Project — Consolidated Job Dashboard
**Software Developer / Analyst / Architect · Team 1 · Full stack · May–Jun 2019**

Supply-chain consolidation of job material requirements — replaced a manual, error-prone process.

**Tech:** VBScript · SQL

#### Project — Espresso Quote Application
**Software Developer / Analyst / Architect · Team 1 · Full stack · Feb–Apr 2019**

Multi-platform quoting for sales reps — on-the-spot quotes, email delivery, manager approval.

**Tech:** jQuery · SQL · C# / .NET · JavaScript · Entity Framework · MVC · Ajax

#### Project — ASP.NET Food Portal
**Development & maintenance · Team 2 · Full stack · May–Sep 2019**

Farmers log deliveries and poison-testing results with multi-location security and compliance.

**Tech:** ASP.NET · C# / .NET · XAML · MVVM

#### Project — Espresso RepCheckIn
**Software Developer / Architect · Team 1 · Full stack · May–Sep 2019**

Rep tracking and tiered priority visit lists for optimised field routes.

**Tech:** JavaScript · C# / .NET · jQuery · MVC · Ajax

---

### Novigo (Pty) Ltd

| Field | Detail |
|---|---|
| Industry | Recruitment |
| Role | Software Developer (C# / .NET) |
| Period | Apr 2017 – Oct 2017 |
| Consulting | Yes (the company was the client) |
| Leaving | Contract ended |

**Duties**

Business and problem-domain analysis; solution planning; framework design; system and server implementation; ERP maintenance; Linux server and domain/hosting support.

#### Project — Novigo Management System
**Sole developer · Team 1 · Full stack · Apr–Sep 2017**

Designed, built, and deployed a complete ERP from scratch, including server setup and IT support.

**Tech:** MySQL · C# / .NET · Linux · WinForms
