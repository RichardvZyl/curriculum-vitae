# Richard van Zyl — Projects & Skills Matrix (2026)

Expanded technical skills matrix with years of experience, followed by a deep-dive on SQL
performance tuning and a full project-by-project breakdown per employer.

---

## Expanded Technical Skills Matrix

### Logical Languages
| Skill | Years |
|---|---|
| C#/.NET | 10 |
| T-SQL | 10 |
| PostgreSQL | 7 |
| TypeScript | 5 |
| JavaScript | 5 |
| KQL | 5 |
| Batch Script | 5 |
| Visual Basic .NET | 3 |
| Java | 2 |

### Design Languages / Data Formats
| Skill | Years |
|---|---|
| JSON | 10 |
| XML | 8 |
| XAML | 7 |
| YAML | 6 |
| HTML | 3 |

### Databases
| Skill | Years |
|---|---|
| Microsoft SQL Server Management Studio | 10 |
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
| Skill | Years |
|---|---|
| Clean Architecture | 10 |
| Microservices | 7 |
| Event-Driven Architecture | 5 |
| Idempotency / Exactly-Once Processing | 4 |

### Frameworks, Libraries & Methodologies
| Skill | Years |
|---|---|
| Entity Framework | 10 |
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
| Event Sourcing | 5 |
| Integration Testing (TestContainers) | 5 |
| Feature Flags (Azure App Configuration) | 4 |
| ASP.NET | 3 |
| Circuit Breaker (Polly) | 3 |
| SignalR / WebSockets | 3 |

### Development Tools, Cloud & DevOps
| Skill | Years |
|---|---|
| Visual Studio | 10 |
| GitHub | 10 |
| Azure DevOps (previously TFS) | 10 |
| VS Code | 10 |
| Postman | 10 |
| Swagger | 10 |
| Enterprise Architect (UML) | 8 |
| Azure CI/CD | 7 |
| Docker | 7 |
| Telerik | 6 |
| Message Queues (Azure Service Bus / RabbitMQ) | 6 |
| Microsoft Azure Insights | 5 |
| Node.js | 5 |
| MVC | 5 |
| Azure Monitor / Log Analytics / App Insights | 5 |
| API Gateway (Azure API Management) | 4 |
| Container Orchestration (AKS / Kubernetes) | 4 |
| Elastic Stack (ELK) / Serilog | 4 |
| DevExpress | 3 |

### Security & Compliance
| Skill | Years |
|---|---|
| Role-Based Access Control (RBAC) | 8 |
| Data-protection-aware design (POPIA / GDPR) | 5 |
| SOX-aligned data segregation | 4 |

---

## Deep Dive: SQL Performance Tuning (Execution Plans / Indexing / Locking)

**Years of experience:** 10 · **Context:** Built and optimised high-volume financial ledger
systems supporting millions of users and 150+ money processors.

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

### Raging River Trading (Pty) Ltd — *Current*
- **Industry:** Fintech / Financial Technology
- **Job title:** Technical Lead — Core Financial Systems
- **Period:** Dec 2022 – Apr 2026
- **Consulting clients:** No
- **Reason for leaving:** Seeking new challenges — open to opportunities

**Overall duties (Software Developer):**
- Product transformation: led the full-scale rewrite of a legacy banking platform into a white-label
  financial engine handling deposits & withdrawals for millions of users across Africa, supporting
  major brands including Betway and Jackpot City.
- High-volume architecture: engineered the system for horizontal and vertical scalability,
  supporting major gaming brands across multiple African markets.
- Integration layer: contributed to the layer abstracting the complexities of 150+ individual money
  processors, ensuring seamless connectivity and reliable transaction routing.

**Project 1 — Core Financial Systems** *(Software Developer / Architect · Team 1–4 · Backend)*
Full-scale rewrite of a legacy banking platform into a white-label financial engine handling
deposits & withdrawals for multiple brands across Africa. Architected for horizontal scalability
with APIs that safely interact with a concurrent financial ledger during high-volume operations.
_Tech: Azure SQL, C# .NET._

**Project 2 — Integration Layer & Back-Office APIs** *(Software Developer / Architect · Team 5 · Backend)*
Developed the robust integration layer abstracting 150+ individual money processors. Designed and
exposed the critical APIs allowing back-office tooling to interact safely and concurrently with the
financial ledger, ensuring data integrity during high-volume operations. _Tech: C# .NET, Azure SQL._

**Project 3 — High-Availability Architecture & Concurrency Design** *(Software Developer / Architect · Team 1 · Backend)*
Designed and implemented the high-availability architecture supporting concurrent financial
transactions across multiple brands and markets, ensuring data integrity, system resilience, and
reliable ledger operations at scale. _Tech: C# .NET, Azure SQL._

### Dotcom Software Solutions
- **Industry:** Consulting (Fintech) · **Consulting clients:** Yes
- **Job title:** Software Developer · **Period:** Jan 2022 – Dec 2022
- **Reason for leaving:** No longer remote / not a culture fit

**Duties:** Specialist problem-solver tackling complex development challenges other team members
could not resolve, delivering robust full-stack solutions in the fintech consulting space for major
clients including Nedbank and PSG Wealth. Business analysis: monetization design for Schemes Bot and
payment validations.

**Project 1 — Schemes Bot (Standard Bank client)** *(Software Developer · Team 5 · Backend · Jan–Feb 2022)*
Schemes (Stokvel / Chama) BotFramework backend upgrade to .NET 6, including package-dependency
updates and breaking-change fixes. Repository history showed this had been attempted and rolled
back; successfully completed the update — live in production with the changes/fixes. _Tech: Azure
SQL, BotFramework, C# .NET Standard, MediatR, Q&A Maker._

**Project 2 — PSG Wealth Website (PSG Wealth client)** *(Software Developer / Analyst / Architect · Team 6 · Backend · Feb–Mar 2022)*
Implemented Angular Universal for server-side rendering for SEO — Dotcom had struggled with this for
two years; solved it in a week. _Tech: Docker, Angular, Bootstrap, Material, Node.js, C# .NET
Standard, Umbraco CMS._

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
