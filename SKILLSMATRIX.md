# Richard van Zyl — Projects & Skills Matrix (2026)

Expanded technical skills matrix with years of experience, followed by a deep-dive on SQL
performance tuning and a full project-by-project breakdown per employer.

> **How to read the Years column.** Values are **professional years only**, counted from the
> start of paid work in **April 2017** — so nothing exceeds **9**. Formal study began in 2014
> (National Diploma in IT: Software Development, Varsity College, 2014–2016), during which
> development was hands-on; those years are deliberately *not* counted here. Skills tied to a
> specific engagement (PostgreSQL, Redis, MongoDB, Azure Functions) carry the span of that
> engagement, not the whole career.

---

## Expanded Technical Skills Matrix

### Logical Languages
| Skill | Years (professional) |
|---|---|
| C#/.NET | 9 |
| T-SQL | 9 |
| PostgreSQL | 7 |
| TypeScript | 5 |
| JavaScript | 5 |
| KQL | 5 |
| Batch Script | 5 |
| Visual Basic .NET | 3 |
| Java | 2 |

### Design Languages / Data Formats
| Skill | Years (professional) |
|---|---|
| JSON | 9 |
| XML | 8 |
| XAML | 7 |
| YAML | 6 |
| HTML | 3 |

### Databases
| Skill | Years (professional) |
|---|---|
| Microsoft SQL Server Management Studio | 9 |
| SQL Performance Tuning | 8 |
| Azure SQL | 7 |
| MySQL Workbench | 6 |
| Azure Data Studio | 6 |
| SSRS | 5 |
| Redis (Distributed Caching) | 5 |
| NoSQL (MongoDB) | 4 |
| Table Partitioning & Archiving | 4 |
| In-Memory OLTP | 4 |

### Architecture & Design
| Skill | Years (professional) |
|---|---|
| Clean Architecture | 9 |
| Microservices | 7 |
| Event-Driven Architecture | 5 |
| Idempotency / Exactly-Once Processing | 4 |

### Business Analysis & Solution Design
| Skill | Years (professional) |
|---|---|
| Business & Problem-Domain Analysis | 9 |
| Requirements Specification (BRS / URS / FRS / TRS) | 9 |
| Solution Design & Solution Architecture | 9 |
| Technical Documentation (audience-tailored) | 9 |
| Stakeholder Engagement & Translation | 8 |
| Process & System Modelling (UML) | 8 |

### Frameworks, Libraries & Methodologies
| Skill | Years (professional) |
|---|---|
| Entity Framework | 9 |
| Domain-Driven Design (DDD) | 8 |
| Scrum | 8 |
| MediatR | 7 |
| Multi-tenancy / Tenant Isolation | 7 |
| Angular | 6 |
| Angular Material | 6 |
| AutoMapper | 6 |
| FluentValidation | 6 |
| Ajax | 6 |
| CQRS | 6 |
| Unit Testing (xUnit / NUnit / Moq) | 6 |
| OAuth2 / OpenID Connect / JWT | 6 |
| Integration Testing (TestContainers) | 5 |
| Feature Flags (Azure App Configuration) | 4 |
| ASP.NET | 3 |
| Circuit Breaker (Polly) | 3 |
| SignalR / WebSockets | 3 |

### Development Tools, Cloud & DevOps
| Skill | Years (professional) |
|---|---|
| Visual Studio | 9 |
| GitHub | 9 |
| Azure DevOps (previously TFS) | 9 |
| VS Code | 9 |
| Postman | 9 |
| Swagger | 9 |
| Enterprise Architect (UML) | 8 |
| Azure CI/CD | 7 |
| Pipeline-as-code (Azure DevOps YAML) | 6 |
| Docker | 7 |
| Telerik | 6 |
| Message Queues (Azure Service Bus / RabbitMQ) | 6 |
| Microsoft Azure Insights | 5 |
| New Relic (APM, release tracking, alerting) | 4 |
| OpenTelemetry | 3 |
| Grafana | 3 |
| Graylog | 3 |
| Node.js | 5 |
| MVC | 5 |
| Azure Monitor / Log Analytics / App Insights | 5 |
| API Gateway (Azure API Management) | 4 |
| Container Orchestration (AKS / Kubernetes) | 4 |
| Elastic Stack (ELK) / Serilog | 4 |
| DevExpress | 3 |

### Security & Compliance
| Skill | Years (professional) |
|---|---|
| Role-Based Access Control (RBAC) | 8 |
| Data-protection-aware design (POPIA / GDPR) | 5 |
| SOX-aligned data segregation | 4 |

---

## Deep Dive: SQL Performance Tuning (Execution Plans / Indexing / Locking)

**Years of experience:** 8 · **Context:** Built and optimised high-volume financial ledger
systems integrating 150+ money processors across multiple African markets.

| Sub-skill | Description |
|---|---|
| **Execution Plan Analysis** | Reading and interpreting SHOWPLAN, `SET STATISTICS IO`, and `SET STATISTICS TIME` to identify table scans, key lookups, and high-cost operators. |
| **Indexing Strategy** | Designing clustered, non-clustered, filtered, and covering indexes; analysing index fragmentation and rebuild/reorganise decisions. |
| **Locking & Concurrency** | Managing transaction isolation levels (READ COMMITTED, REPEATABLE READ, SERIALIZABLE, SNAPSHOT); detecting and resolving deadlocks using SQL Server Profiler / Extended Events. |
| **Performance Tuning Patterns** | Rewriting correlated subqueries as joins; INNER JOIN vs EXISTS; optimising WHERE clauses with SARGable predicates; avoiding scalar UDFs. |
| **Database Design for Scale** | Partitioning tables by date/tenant; indexed and materialised views for pre-aggregation; designing for high-volume batch inserts (e.g. ledger entries). |
| **In-Memory OLTP** | Using memory-optimised tables and natively compiled stored procedures for high-contention financial operations. |
| **Query Store & Automatic Tuning** | Leveraging Query Store to track regression; using forced parameterization and plan forcing. |
| **Database Health Monitoring** | Regular `sys.dm_os_wait_stats`, `sys.dm_db_index_usage_stats`, and `sp_WhoIsActive` analysis to identify bottlenecks. |

---

## Employment & Project Profiles

### Yuno Technologies
- **Industry:** Digital consultancy
- **Job title:** Co-owner / Solutions Architect
- **Period:** Apr 2026 – present
- **Consulting clients:** Yes (client names held private)

**Overall duties:**
- Half-owner of a South African digital consultancy; leads technical delivery — architecture,
  backend engineering and security design across client platforms.
- Four-plane deployment topology with one-way initiation; BFF holding session rather than tokens;
  response-only identity plane on Keycloak; inter-plane trust specified (mTLS / SPIFFE/SPIRE as
  phase two behind a documented interim).
- Ledger-plane isolation under evaluation: KVM-backed microVM separation so a container escape in
  an adjacent workload cannot reach the ledger.
- Containerised platforms across four environments; ADRs with formal supersession.
_Tech: .NET, Vite / React, PostgreSQL, Redis, RabbitMQ, gRPC, Django / DRF, Azure Functions,
Blob Storage, Keycloak, Prometheus / Grafana / ELK._

### Raging River Trading (Pty) Ltd
- **Industry:** Fintech / Gaming
- **Job title:** Solutions Architect / Technical Lead — Core Financial Systems
  *(payroll title: Software Developer)*
- **Period:** Dec 2022 – Mar 2026
- **Consulting clients:** No
- **Reason for leaving:** Concluded via voluntary severance during a post-acquisition restructure.

**Overall duties:**
- Product transformation: led the full-scale rewrite of a legacy banking platform into a white-label
  financial engine handling deposits & withdrawals across multiple African markets, supporting
  major brands including Betway and Jackpot City.
- High-volume architecture: engineered the system for horizontal and vertical scalability,
  supporting major gaming brands across multiple African markets.
- Integration platform: worked on the platform where integrations are managed, routed and
  reconciled — abstracting 150+ individual money processors — and built integrations on it.
  Per-provider IronPython marshalling hosted in the .NET backend reshaped payloads to the core
  contract. Rewrote the engine that moves each integration into its own instance, preventing
  shared thread-pool and socket exhaustion.
- Large-scale migration: moved roughly 150 million records across a high-throughput Saturday at
  peak trading, with no drop in the New Relic Apdex score.

**Project 1 — Core Financial Systems** *(Solutions Architect / Technical Lead · Team 1–4 · Backend)*
Full-scale rewrite of a legacy banking platform into a white-label financial engine handling
deposits & withdrawals for multiple brands across Africa. Architected for horizontal scalability
with APIs that safely interact with a concurrent financial ledger during high-volume operations.
Schema-per-brand under one SQL Server (separate databases priced out); transactional outbox to
per-brand queues with dead-lettering.
_Tech: Azure SQL, C# .NET, Docker, RabbitMQ, EF Core._

**Project 2 — Integration Layer & Back-Office APIs** *(Solutions Architect / Technical Lead · Team 5 · Backend)*
Developed the robust integration layer abstracting 150+ individual money processors. Designed and
exposed the critical APIs allowing back-office tooling to interact safely and concurrently with the
financial ledger, ensuring data integrity during high-volume operations. _Tech: C# .NET, Azure SQL._

**Project 3 — High-Availability Architecture & Concurrency Design** *(Solutions Architect / Technical Lead · Team 1 · Backend)*
Designed and implemented the high-availability architecture supporting concurrent financial
transactions across multiple brands and markets — idempotent attempt records with rowversion
optimistic concurrency on the ledger — ensuring data integrity, system resilience, and reliable
ledger operations at scale. _Tech: C# .NET, Azure SQL._

### MeterMo
- **Industry:** Utilities — automated electricity, water and gas usage metering & reporting · **Consulting clients:** No
- **Job title:** Software Developer · **Period:** Apr 2022 – Dec 2022
- **Reason for leaving:** Mandate complete; sole developer — sought a larger engineering team with scope to learn and grow.

**Duties:** Platform development and modernisation across an automated utility-metering estate —
electricity, water and gas usage capture and reporting from field devices. Two APIs, two
cross-platform field apps (Xamarin, Cordova) and two websites. Device telemetry and usage
integrity: readings that must arrive, persist, and not be double-counted. Migrated six projects
from Team Foundation Server to Azure DevOps; upgraded projects to current frameworks and package
versions.
_Tech: C# .NET, ASP.NET, Angular, Xamarin, Cordova, Azure DevOps, TFS._

### Dotcom Software Solutions
- **Industry:** Consulting (Fintech) · **Consulting clients:** Yes
- **Job title:** Software Developer (Specialist Problem-Solver) · **Period:** Jan 2022 – Apr 2022
- **Reason for leaving:** No longer remote / not a culture fit

**Duties:** Specialist problem-solver tackling complex development challenges other team members
could not resolve, delivering robust full-stack solutions in the fintech consulting space for major
clients including Nedbank, Standard Bank and PSG Wealth. Business analysis: monetization design for Schemes Bot and
payment validations.

**Project 1 — Schemes Bot (Standard Bank client)** *(Software Developer · Team 5 · Backend · Jan–Feb 2022)*
Schemes (Stokvel / Chama) BotFramework backend upgrade **to .NET 6 from .NET Standard**, including
package-dependency updates and breaking-change fixes. Repository history showed this had been
attempted and rolled back; successfully completed the update — live in production with the
changes/fixes. _Tech: Azure SQL, BotFramework, C# .NET 6 (from .NET Standard), MediatR, Q&A Maker
(historical / retired Microsoft service)._

**Project 2 — PSG Wealth Website (PSG Wealth client)** *(Software Developer / Analyst / Architect · Team 6 · Backend · Feb–Mar 2022)*
Implemented Angular Universal for server-side rendering for SEO — Dotcom had struggled with this for
two years; solved it in a week. _Tech: Docker, Angular, Bootstrap, Material, Node.js, C# .NET 6,
Umbraco CMS._

### Payteq
- **Industry:** Fintech · **Consulting clients:** No
- **Job title:** Senior Developer / Business Analyst / Team Lead · **Period:** Apr 2020 – Jan 2022
- **Reason for leaving:** Career growth

**Duties:** Full-stack development on EDI, GoTrips, and Veriseal; business analysis with the BA team;
team lead on the GoTrips technical-debt rewrite, optimisation, and architecture.

**Project 1 — GoTrips** *(Software Developer / Analyst / Team Lead · Team 5 · Full Stack · Jan 2021 – Jan 2022)*
Led the ground-up rewrite of the GoTrips platform, eliminating years of accumulated technical debt;
implemented coding standards, design principles, and performance optimisations; built abstractions
and automation that transformed a struggling codebase into a maintainable, scalable system. _Tech:
C# .NET Core API, PostgreSQL, Azure CI/CD, FluentValidation, Angular, Azure Functions._

**Project 2 — Veriseal** *(Software Developer / Analyst / Architect · Team 1 · Full Stack · side project, migrated whenever there was opportunity)*
Single-handedly migrated a critical compliance platform from legacy ASP.NET to .NET Core API with
Angular 8. Handled mass payments, bank-account verification, KYC, and AML checks — with meticulous
attention to data integrity and security. _Tech: C# .NET Core (to), SQL, SSRS, Angular (to),
ASP.NET Core (from), C# .NET Framework (from), IP microservices/integrations, FluentValidation,
AutoMapper._

**Project 3 — GoBills** *(Team Lead · Team 2 · Full Stack · Apr 2020 – Jan 2021)*
Led development of a scalable business-management solution covering inventory, POS, and financials,
serving businesses from single stores to large chains. Implemented a sophisticated RBAC system
governing user permissions and client access control. _Tech: C# .NET Core API, Dependency
Injection, Identity Framework, custom CMS, Angular 8, Bootstrap, Angular Material._

**Project 4 — Interchange IDE & Insight Server** *(Development & maintenance · Team 2 · Support/Maintenance)*
Go-to consultant for a highly scalable integration platform functioning as messaging middleware with
an RBAC system governing user access; ongoing support and maintenance on a SaaS basis. _Tech: SQL,
C# .NET Core, various IP microservices/integrations._

### iPlan Global
- **Industry:** Supply Chain / Manufacturing / Farming / Industrial / Automation · **Consulting clients:** Yes
- **Job title:** Software Developer / Business Analyst · **Period:** Oct 2017 – Apr 2020
- **Reason for leaving:** Career growth

**Duties:** Team and individual project work; automation for business productivity; work across many
technologies and systems; occasional IT support. As BA: client needs analysis, business-domain
analysis, solution design across Mining, Industrial, Supply Chain, Manufacturing, Sales; solution
architecture.

**Project 1 — Consolidated Job Dashboard** *(Software Developer / Analyst / Architect · Team 1 · Full Stack · May–Jun 2019)*
Supply-chain solution consolidating job material requirements into new jobs, streamlining a
previously manual, error-prone process. _Tech: VBScript, SQL._

**Project 2 — Espresso Quote Application** *(Software Developer / Analyst / Architect · Team 1 · Full Stack · Feb–Apr 2019)*
Multi-platform mobile app empowering sales reps to work independently — on-the-spot quoting with
integrated email delivery and manager-approval workflows. _Tech: jQuery, SQL, C# .NET, JavaScript,
Entity Framework, MVC, Ajax._

**Project 3 — ASP.NET Food Portal** *(Development & maintenance · Team 2 · Full Stack · May–Sep 2019)*
Distributed food-processing system for farmers to log vegetable/fruit deliveries and track
poison-testing results, enforcing user security and compliance across multiple locations. _Tech:
ASP.NET, C# .NET, XAML, MVVM._

**Project 4 — Espresso RepCheckIn** *(Software Developer / Architect · Team 1 · Full Stack · May–Sep 2019)*
Representative-tracking system letting managers monitor rep locations and plan client visits by
tiered priority lists, ensuring reps followed optimised routes and improving field-team efficiency.
_Tech: JavaScript, C# .NET, jQuery, MVC, Ajax._

### Novigo (Pty) Ltd
- **Industry:** Recruitment · **Consulting clients:** Yes (the client was the company)
- **Job title:** Software Developer C# .NET · **Period:** Apr 2017 – Oct 2017
- **Reason for leaving:** Contract ended

**Duties:** Business-needs and problem-domain analysis; system solution planning; framework design;
system and server implementation; management-system maintenance; company server setup and
maintenance; general IT and domain/hosting support.

**Project 1 — Novigo Management System** *(Sole developer · Team 1 · Full Stack · Apr–Sep 2017)*
Sole developer: designed, built, and deployed a complete ERP solution from the ground up to support
all core business processes, including server setup, domain hosting, and general IT support. _Tech:
MySQL, C# .NET, Linux, WinForms._
