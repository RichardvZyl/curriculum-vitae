# Richard van Zyl — Professional Profile & AI Context

> **Purpose of this document.** A single, comprehensive context file about Richard van Zyl,
> compiled from his CV, 2026 skills matrix, and job-application correspondence. It exists so an
> AI assistant can help with CV/cover-letter generation, role matching, interview prep, and
> general career assistance without re-deriving context each time. It is a *reference document*,
> not project code.
>
> _Last compiled: 2026-07-02._

---

## 1. Snapshot

| | |
|---|---|
| **Name** | Richard van Zyl |
| **Title** | Solutions Architect / Technical Lead — Backend & Data-Intensive Systems |
| **Experience** | 9+ years architecting systems; ~10 years hands-on C#/.NET and T-SQL |
| **Location** | Pretoria, Gauteng, South Africa |
| **Relocation** | Willing to relocate to Johannesburg if relocation costs are covered |
| **Email** | richardvzyl@gmail.com |
| **LinkedIn** | linkedin.com/in/richard-van-zyl (also referenced as /richardvzyl) |
| **GitHub** | https://github.com/RichardvZyl |
| **Citizenship** | South African citizen (no work permit / visa required) |
| **Availability** | Immediate notice period |
| **References** | Available upon formal offer (per SA labour-law norms) |

---

## 2. Professional Summary

Solutions Architect and Technical Lead with 9+ years architecting high-throughput, multi-tenant
financial systems where data integrity is non-negotiable — backed by roughly a decade of hands-on
C#/.NET and T-SQL. Deep specialist in backend engineering and relational data: execution-plan
tuning, concurrency control, partitioning, and idempotent transaction design for ledgers
processing millions of transactions daily across Africa.

Owns architecture end-to-end — from concurrency and multi-tenancy strategy through to CI/CD and
production telemetry — while leading delivery teams and bridging engineering with business
stakeholders. A problem solver at heart; languages and frameworks are treated as tools.
Regularly handed the challenges others could not solve, from turning around failed legacy
migrations to designing the financial engine that replaced a legacy banking platform.

---

## 3. Core Competencies

- **Architecture & Design:** Domain-Driven Design (DDD), CQRS, Event Sourcing, Event-Driven
  Architecture, Microservices, Multi-tenancy & Tenant Isolation, Idempotency / Exactly-Once
  Processing, RESTful API design, Clean Architecture, Layered Architecture, SAGA patterns.
- **Databases & Data:** Microsoft SQL Server, Azure SQL, T-SQL, SQL Performance Tuning
  (execution plans, indexing, locking & isolation levels, deadlock resolution), Table
  Partitioning & Archiving, In-Memory OLTP, PostgreSQL, MySQL, Redis (distributed caching),
  MongoDB, Entity Framework.
- **Backend & Languages:** C# (.NET Core, .NET 6+, ASP.NET Core, ASP.NET Web API), MediatR,
  FluentValidation, AutoMapper, Polly; SQL / T-SQL; TypeScript, JavaScript, Node.js.
- **Messaging & Integration:** Azure Service Bus, RabbitMQ, API Gateway (Azure API Management),
  SignalR / WebSockets, REST, gRPC, SOAP, GraphQL.
- **Cloud, DevOps & Observability:** Microsoft Azure, Azure DevOps, Docker, AKS / Kubernetes,
  Azure CI/CD, GitHub, Trunk-based & GitFlow branching, Feature Flags, Azure Monitor /
  Application Insights / Log Analytics, Elastic Stack (ELK) / Serilog.
- **Security & Compliance:** OAuth2 / OpenID Connect / JWT, Role-Based Access Control (RBAC),
  Maker-Checker workflows, Entitlement Management, KYC / AML domains, SOX-aligned data
  segregation, data-protection-aware design (POPIA / GDPR).
- **Testing & Tooling:** xUnit, NUnit, Moq, Integration Testing (TestContainers); Enterprise
  Architect (UML), Swagger, Postman, SSRS; Angular, Angular Material; Agile, Scrum.

---

## 4. Skills Matrix — Years of Experience

_From the 2026 Expanded Technical Skills Matrix. Where the CV framing and the matrix differ, see
the notes in §9. Full detail lives in `SKILLS-MATRIX.md`._

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

### Databases
| Skill | Years |
|---|---|
| SQL Server Management Studio | 10 |
| SQL Performance Tuning | 8 |
| Azure SQL | 7 |
| MySQL Workbench | 6 |
| Azure Data Studio | 6 |
| SSRS | 5 |
| Redis (distributed caching) | 5 |
| NoSQL (MongoDB) | 4 |
| Table Partitioning & Archiving | 4 |
| In-Memory OLTP | 4 |

### Architecture, Frameworks & Methodologies
| Skill | Years |
|---|---|
| Clean Architecture | 10 |
| Entity Framework | 10 |
| Domain-Driven Design (DDD) | 8 |
| Scrum | 8 |
| Microservices | 7 |
| MediatR | 7 |
| Multi-tenancy / Tenant Isolation | 7 |
| Angular / Angular Material | 6 |
| AutoMapper | 6 |
| FluentValidation | 6 |
| CQRS | 6 |
| Unit Testing (xUnit / NUnit / Moq) | 6 |
| OAuth2 / OpenID Connect / JWT | 6 |
| Event-Driven Architecture | 5 |
| Event Sourcing | 5 |
| Integration Testing (TestContainers) | 5 |
| Idempotency / Exactly-Once Processing | 4 |
| Feature Flags (Azure App Configuration) | 4 |
| Circuit Breaker (Polly) | 3 |
| SignalR / WebSockets | 3 |

### Cloud & DevOps
| Skill | Years |
|---|---|
| Visual Studio / GitHub / Azure DevOps / VS Code / Postman / Swagger | 10 |
| Enterprise Architect (UML) | 8 |
| Azure CI/CD | 7 |
| Docker | 7 |
| Message Queues (Azure Service Bus / RabbitMQ) | 6 |
| Azure Monitor / Log Analytics / App Insights | 5 |
| Node.js | 5 |
| API Gateway (Azure API Management) | 4 |
| Container Orchestration (AKS / Kubernetes) | 4 |
| Elastic Stack (ELK) / Serilog | 4 |

### Security & Compliance
| Skill | Years |
|---|---|
| Role-Based Access Control (RBAC) | 8 |
| Data-protection-aware design (POPIA / GDPR) | 5 |
| SOX-aligned data segregation | 4 |

---

## 5. Selected Achievements

- **Multi-tenant, white-label financial engine** serving two separate legal entities (Betway and
  Jackpot City) from a single, configuration-driven codebase — with per-entity database isolation
  and per-brand schema separation to satisfy SOX-aligned segregation.
- **Sustained deposit volumes in excess of €10M on peak trading days**, absorbing steady casino
  throughput plus large spikes during live sporting events — volumes exceeding conventional
  banking workloads.
- **Eliminated double-spend race conditions** under heavy contention via idempotent, exactly-once
  withdrawal processing with rowversion-based optimistic concurrency on the ledger.
- **Solved problems others had abandoned:** completed a .NET 6 migration previously attempted and
  rolled back; resolved a 2-year Angular Universal SEO blocker in one week.
- **IKM C# Assessment:** 73rd percentile of all test takers (assessed twice, six months apart).

---

## 6. Professional Experience (summary)

_Full detail in `CV.md`._

| Company | Role | Period |
|---|---|---|
| Raging River Trading (Pty) Ltd | Solutions Architect / Technical Lead — Core Financial Systems | Dec 2022 – Apr 2026 |
| Dotcom Software Solutions | Software Developer (Specialist Problem-Solver) | Jan 2022 – Dec 2022 |
| Payteq (Pty) Ltd | Senior Developer / Business Analyst / Team Lead | Apr 2020 – Jan 2022 |
| iPlan Global | Software Developer / Business Analyst | Oct 2017 – Apr 2020 |
| Novigo (Pty) Ltd | Software Developer (C# .NET) | Apr 2017 – Oct 2017 |

**Notable clients engaged across consulting roles:** Bankserv (now PayInc), Standard Bank,
Nedbank, PSG Wealth, Libstar Holdings, Translution.

---

## 7. Leadership & Ways of Working

- **Team leadership:** led teams of 1–5 developers; code reviews, coding standards, mentoring of
  junior/mid-level devs.
- **Stakeholder management:** translates business needs (product owners, BAs, marketing,
  retention) into sustainable architecture without trading long-term integrity for short-term wins.
- **Strategic input:** architecture review boards, solution assurance, technical design approvals.
- **Agile/Scrum:** sprint planning, technical estimation, backlog grooming.

---

## 8. Education, Certifications & Personal Profile

- **National Diploma — IT: Software Development**, Varsity College, 2014–2016.
- **IKM C# Assessment:** 73rd percentile (assessed twice, six months apart).
- **DISC & Values Index:** High D (decisive, results-driven) / High I (communicative) / Low S
  (adaptable, thrives in change) / Moderate C. Motivators: Very High Theoretical and Political;
  pragmatic and results-focused.

---

## 9. Honest Skill Boundaries & Framing Notes

Deliberate self-assessments and framing nuances — useful when tailoring applications so claims
stay defensible in interviews.

- **Front-end / full-stack:** primary focus is backend engineering, system architecture, and
  integration. Worked with Angular up to v8 and TypeScript, but **not actively maintaining**
  front-end skills; would need ramp-up for deep front-end leadership roles.
- **Docker / Kubernetes:** the CV/skills matrix list Docker (7 yrs) and AKS/K8s (4 yrs), but the
  candid framing is that deep hands-on cluster management is **limited** — comfortable with
  containerisation concepts and high-level AKS (deployments, scaling), would rely on operational
  support for deep cluster ops. Choose whichever framing matches the audience, but keep it
  consistent within a single application.
- **Go (GoLang):** no production experience; willing to upskill.
- **Java:** ~college-level / ~2 years exposure.
- **Reason for leaving current role:** framed on the 2026 skills matrix as "seeking new challenges
  – open to opportunities"; in later application correspondence framed as **retrenchment following
  a corporate takeover**. The retrenchment framing is the more current/accurate status.

---

## 10. Availability

- **Notice period:** immediate.
- **Open to:** permanent or contract opportunities.
- **Negotiable** where the package includes meaningful benefits (medical aid, provident fund, extra
  leave) or non-monetary perks (remote work, office close to home, autonomy).

> _Rate/CTC figures, phone number, and personal-background details are kept out of this public
> repository. They live in `PRIVATE-DETAILS.private.md`, which is git-ignored and not published —
> available on request or shared directly with recruiters._

---

## 11. Links

- **LinkedIn:** https://www.linkedin.com/in/richard-van-zyl (also seen as /richardvzyl)
- **GitHub:** https://github.com/RichardvZyl

---

_Compiled from CV, 2026 skills matrix, and job-application correspondence. Intended as
comprehensive context for an AI assistant to help with role matching, cover-letter generation, and
interview preparation._
