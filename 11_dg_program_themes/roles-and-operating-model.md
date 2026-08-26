---
theme: roles-and-operating-model
type: dg-program-theme
frames:
  - "3458764611453525295" # DG Role Structure
  - "3458764611453525317" # Organizational Model of DG (CDO Office)
  - "3458764612005175528" # Comparison of 5 operational models
  - "3458764611929480210" # Data Teams Modeling template
  - "3458764611929480215" # Scorecard: Fully Centralized
  - "3458764611929480216" # Scorecard: Centralized + matrix
  - "3458764611929480217" # Scorecard: Federated analytics
  - "3458764611929480214" # Scorecard: Fully Federated (data mesh)
  - "3458764611929480213" # BI org model 5: Hybrid + cross-functional team
  - "3458764611929480212" # D&A capability matrix (as-is / to-be)
---
# Roles and Operating Model

## What the board teaches
The DG role model splits into central DG Office roles (CDO, DG Lead, Coordinating Data Steward, tools development team) and business-side roles (Executive Sponsor, Data Owner, Business Data Steward, Data Custodian). The Executive Sponsor is a senior *business* leader with ultimate accountability for a domain; the Data Custodian is the technical counterpart (DBAs, data engineers, BI professionals) — and, notably, custodian duties largely mirror what those teams already do day-to-day, which is why (per the board's DG Kitchen research) custodianship adopts far more easily than business stewardship. Above the roles sits the organizational design question: the board compares five operational models for data/analytics teams — from Complete Centralization to Full Federation (Data Mesh) — scoring each on ~13 criteria across Process Efficiency, User Experience, and Business Value. The consistent pattern: centralized models win on consistency, cost balancing, security, one-version-of-truth, and people development but bottleneck the business; federated models invert this; matrix and hybrid-with-core-team models buy business proximity while retaining most central benefits at the price of High implementation complexity. A capability matrix template (org units × 10 BI/data capabilities, done/in-progress/to-be) turns the model choice into a transformation roadmap.

## Key objects
- DG Office roles: CDO, Data Governance Lead, Coordinating Data Steward, Tools Development Team (data catalog, DQ tool)
- Business roles: Executive Sponsor (domain accountability, policy approval, arbitration between domains), Data Owner, Business Data Steward, Data Custodian (access control, integrity, DQ resolution with steward, technical protection, master data versioning, change management)
- OCDO org chart: CDO → Technical Team / DG Officers → Data Scientists, Data Engineers, Business Areas, Developers, Trainers
- Five operational models: 1) Complete Centralization (complexity Low); 2) Hybrid Centralization with Matrix Management (High); 3) Hybrid Federation with a Core / Cross-Functional Analytics Team (High); 4) Partial Federation — data engineering stays central (Medium); 5) Full Federation / Data Mesh (Medium) — plus fit ratings for large enterprise, SME, digital product company (100+ data pros), startup
- Scorecard criteria ("how easy is to provide"): capacity balancing, content/data governance, security, one-version-of-truth, cross-functional reporting, navigation/UX, quality and standardization, dedup of effort, people development/retention; vs business alignment, request throughput, time-to-market, high-context insights
- Scorecard results: Fully Centralized — consistency easy, business proximity hard; Centralized + matrix — proximity improves to medium, keeps central benefits; Federated analytics — proximity easy, consistency degrades; Fully Federated (mesh) — proximity easy, nearly all consistency criteria hard
- BI org model 5 (hybrid + cross-functional analytics team): strong on governance and TTM simultaneously; amber on capacity balancing, standardization, people development
- Data Teams Modeling template: org-chart prototypes with Managing vs Contributing roles and shared-service blocks (infrastructure, core data model, golden layer, glossary/metric store, metadata, DG/DQ framework, security)
- Capability matrix: units (Finance, Service Lines, Business Lines) × 10 capabilities (self-service BI/ETL, own governed layer, harmonized landscape, DQ tooling, catalog, data products, ...) with done/in-progress/to-be statuses
- Related workshop template (Data Teams Modeling) — see [templates.md](../12_templates/templates.md)

## Frames on the board
- [DG Role Structure](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525295)
- [Organizational Model of DG](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525317)
- [Comparison of Operational Models for Data Analytics Teams](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764612005175528)
- [Template — Data Teams Modeling (centralization vs self-service)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480210)
- [Scorecard — 1. Fully Centralized](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480215)
- [Scorecard — 2. Centralized with matrix management](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480216)
- [Scorecard — 3. Federated analytics](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480217)
- [Scorecard — 4. Fully Federated (data mesh)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480214)
- [BI org model 5: Hybrid + cross-functional analytics team](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480213)
- [D&A operating model capability matrix (as-is / to-be)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480212)

## Links
- https://data-nature.com (source attribution on the comparison matrix)
