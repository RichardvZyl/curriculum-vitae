# Richard van Zyl — Skills Overview

**Solutions Architect / Technical Lead — Backend & Data-Intensive Systems**

Pretoria, Gauteng, South Africa · richardvzyl@gmail.com · [linkedin.com/in/richardvzyl](https://www.linkedin.com/in/richardvzyl) · [github.com/RichardvZyl](https://github.com/RichardvZyl) · [richardvzyl.github.io](https://richardvzyl.github.io/)

A human-readable skills summary for hiring conversations. For the full dense matrix with every row and project breakdown, see [`SKILLSMATRIX.md`](./SKILLSMATRIX.md). Narrative CV: [`CV.md`](./CV.md).

> **Years column.** Professional years only, counted from paid work starting **April 2017** — nothing exceeds **9**. Study years (2014–2016) are not counted.

---

## At a glance

| Area | Strength |
|---|---|
| Primary stack | C# / .NET, SQL Server / Azure SQL, T-SQL |
| Architecture | Multi-tenant financial systems, DDD, CQRS, idempotent ledger design |
| Cloud | **Microsoft Azure** in production (not AWS) |
| Delivery | Azure DevOps YAML pipelines, Docker on Azure hosts, trunk-based + feature flags |
| Leadership | ~5 years leading teams; ~3.5 as Solutions Architect / Technical Lead |
| Analysis | BRS / URS / FRS / TRS since 2017; stakeholder translation |

---

## Grouped skills (professional years)

### Languages & data formats

| Skill | Years |
|---|---|
| C# / .NET | 9 |
| T-SQL | 9 |
| PostgreSQL | 7 |
| TypeScript / JavaScript | 5 |
| JSON / XML | 9 / 8 |
| YAML | 6 |
| Visual Basic .NET | 3 |
| Java | 2 |

### Databases & data engineering

| Skill | Years |
|---|---|
| SQL Server / SSMS | 9 |
| SQL performance tuning | 8 |
| Azure SQL | 7 |
| Entity Framework | 9 |
| Redis (distributed caching) | 5 |
| Table partitioning & archiving | 4 |
| In-Memory OLTP | 4 |
| MongoDB | 4 |
| SSRS | 5 |

### Architecture & design

| Skill | Years |
|---|---|
| Clean Architecture | 9 |
| Domain-Driven Design | 8 |
| Microservices | 7 |
| CQRS | 6 |
| Event-driven architecture | 5 |
| Multi-tenancy / tenant isolation | 7 |
| Idempotency / exactly-once processing | 4 |

### Requirements & solution design

| Skill | Years |
|---|---|
| Business & problem-domain analysis | 9 |
| Requirements (BRS / URS / FRS / TRS) | 9 |
| Solution design & architecture | 9 |
| Technical documentation (audience-tailored) | 9 |
| Stakeholder engagement & translation | 8 |
| Process & system modelling (UML) | 8 |

### Backend frameworks & practices

| Skill | Years |
|---|---|
| MediatR / AutoMapper / FluentValidation | 7 / 6 / 6 |
| OAuth2 / OpenID Connect / JWT | 6 |
| Unit testing (xUnit / NUnit / Moq) | 6 |
| Integration testing (TestContainers) | 5 |
| Feature flags (Azure App Configuration) | 4 |
| Circuit breaker (Polly) | 3 |
| SignalR / WebSockets | 3 |
| Angular / Angular Material | 6 |

### Cloud, DevOps & observability

| Skill | Years |
|---|---|
| Azure DevOps (previously TFS) | 9 |
| Azure CI/CD | 7 |
| Pipeline-as-code (Azure DevOps YAML) | 6 |
| Docker | 7 |
| Message queues (Azure Service Bus / RabbitMQ) | 6 |
| Azure Monitor / App Insights / Log Analytics | 5 |
| New Relic | 4 |
| AKS / Kubernetes | 4 |
| API Gateway (Azure API Management) | 4 |
| OpenTelemetry / Grafana / Graylog | 3 |

### Security & compliance

| Skill | Years |
|---|---|
| Role-Based Access Control (RBAC) | 8 |
| Data-protection-aware design (POPIA / GDPR) | 5 |
| SOX-aligned data segregation | 4 |

---

## Honest boundaries

Keep these framing notes when matching roles — they are deliberate, not soft-pedalling.

- **No AWS experience.** Cloud depth is **Microsoft Azure**. Do not map skills to “AWS equivalents.”
- **Infrastructure as Code:** declarative work is **Azure DevOps YAML pipelines** (pipeline-as-code) and **Docker on Azure hosts** — not Terraform, Bicep, or ARM templates in anger. Roles that lead on cloud resource provisioning as code need ramp-up; that is not a current strength.
- **Python:** not a language to hire for. Production exposure is **IronPython hosted in a C# backend** for integration marshalling (pre-v3), plus limited contemporaneous Python at MeterMo. Treat as read-and-modify.
- **Front-end:** not primary. Angular up to v8 and TypeScript are on the record, but front-end skills are not actively maintained; deep front-end leadership would need ramp-up.
- **Docker / Kubernetes:** comfortable with containerisation and high-level AKS (deployments, scaling); deep hands-on cluster ops is limited — would rely on operational support for that layer.
- **ActiveXperts:** used in production observability prose; not given a years row here (no invented span).

---

## SQL performance tuning (condensed)

**~8 years** on high-volume financial ledger systems (150+ money processors across African markets).

| Focus | What it means in practice |
|---|---|
| Execution plans | SHOWPLAN, `STATISTICS IO` / `TIME`; spotting scans, lookups, high-cost operators |
| Indexing | Clustered / non-clustered / filtered / covering; fragmentation and rebuild choices |
| Locking & concurrency | Isolation levels; deadlock detection via Profiler / Extended Events |
| Tuning patterns | SARGable predicates; join vs EXISTS; avoiding scalar UDFs; subquery rewrites |
| Scale design | Date/tenant partitioning; indexed/materialised views; high-volume batch inserts |
| In-Memory OLTP | Memory-optimised tables and natively compiled procedures on hot paths |
| Health monitoring | Query Store, wait stats, index usage, `sp_WhoIsActive` |

---

## Career timeline (condensed)

Detail stays in [`CV.md`](./CV.md).

| Period | Role | Organisation |
|---|---|---|
| Apr 2026 – present | Co-owner / Solutions Architect | Yuno Technologies |
| Dec 2022 – Mar 2026 | Solutions Architect / Technical Lead — Core Financial Systems | Raging River Trading |
| Apr 2022 – Dec 2022 | Software Developer | MeterMo (utilities metering; six projects TFS→Azure DevOps; APIs, field apps, websites; platform-debt close) |
| Jan 2022 – Apr 2022 | Software Developer (Specialist Problem-Solver) | Dotcom Software Solutions |
| Apr 2020 – Jan 2022 | Senior Developer / Business Analyst / Team Lead | Payteq |
| Oct 2017 – Apr 2020 | Software Developer / Business Analyst | iPlan Global |
| Apr 2017 – Oct 2017 | Software Developer (C# .NET) | Novigo |

---

## Education & assessment

- **National Diploma — IT: Software Development**, Varsity College, 2014–2016
- **IKM C# Assessment:** 73rd percentile (assessed twice, six months apart)

---

*All rights reserved. For evaluation by employers and collaborators; do not republish as your own. See [`LICENSE`](./LICENSE).*
