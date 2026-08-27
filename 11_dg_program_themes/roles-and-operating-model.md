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

## From the course (Data Governance Fundamentals, 6 days)

### Which role actually carries the load
- "The Data Custodian / Data Partner / Domain Curator role is probably MORE important than the Data Steward role" — and at minimum it comes first. (course day 2, slides p.53; course day 6, slides p.99)
- Business data stewards are a common delusion: business people will never do hands-on steward work in any workflow you design — at best they answer questions, approve the glossary, and state DQ requirements. Actual steward work must land on a data person in the domain (power user / analyst / BI partner) — "nowhere does it work otherwise." (course day 2, transcript)
- Exec-level "Data Owner" is a near-useless concept; the useful one is "data object owner" — the specific engineer/analyst who created the object. On the classic Data Owner responsibility wheel, "more than half of this is in fact done by the DS, not the DO." (course day 3, transcript)
- Naming adapts to culture: large tech companies call custodians "data partners" or "BI partners"; a timber company consciously renamed stewards "data foresters" — renaming the roles for the industry is a worthwhile brainstorm. (course day 1, transcript)

### Staffing and motivation
- In ~95% of cases data steward is a second hat; whole-company dedicated steward teams are ~5 people including catalog developers. "Everyone who gets to formalizing stewards realizes the global problem was not defining them but motivating them." (course day 1, transcript)
- Practical hiring rule: every domain running on common sense already has a person instinctively tending content (archiving, certifying, documenting) — find them and confer the role, don't invent a new one. (course day 1, transcript)
- Enforcement mechanism at a large tech company: ~20 domains with designated BI partners; governance activities are hard-wired into the competency matrix (can't pass calibration without them), with ~20% of partner time reserved via an agreed "tech-debt includes governance" rule. (course day 2, transcript)
- Tom Sawyer engagement in practice: gamified BI cleanup marathons whose participants are told afterwards they were doing data stewardship — that's how the BI-partner program was bootstrapped. (course day 3, slides p.85; transcript)
- Top-down alternative: adopt a 5-level DG maturity model and give each top manager an annual goal "function reaches level X" — steward duties cascade by themselves. (course day 3, transcript)

### Funding the operating model
- Funding models: business pays, platform pays, or a negotiated "platform tax" — each domain commits a % of existing capacity to governance (works in ~70% of cases, no extra headcount). One big-tech variant: 6 people carved out of a 20-person DWH team, zero new hires, overhead hidden inside product work. (course day 2, transcript)
- With no budget, governance ownership spreads at 0.2-0.3 FTE per person across teams; per-slice centers of expertise form naturally — but someone must be the visionary coordinating the pieces, or the fragments never converge. (course day 5, transcript)
- The DG leader must be an "authoritative old-timer" of the company: hire from the market and you wait years — "nobody lets a newcomer seriously change their processes; you get sabotage and imitation." (course day 6, slides p.104)

### Bodies, escalation, rituals
- Real DG committees only emerge at very large scale — "maybe two dozen companies max" in Russia; call it a "data management sync" instead, it works the same with less bureaucratic smell. (course day 5, transcript)
- DAMA escalation benchmark: 80-85% of data conflicts resolved at business-unit stewardship level, <20% reach the DG Council, <5% reach the Steering Committee. (course day 5, slides p.65)
- Council hygiene: expect stewards to ask "should I keep attending?" after the very first meeting — have a ready answer and repeat it every session; never meet for meeting's sake; close by listing the day's achievements. (course day 3, slides p.86-87)
- Monthly ritual that works: show domain stewards dashboards with per-steward metrics — peer dynamics alone motivates even before you have the right to set targets. (course day 5, transcript)
- Operating-model war story from a large telecom ecosystem: DG elevated to ecosystem level with ~20 stewards, then it "dissolved organizationally" — practice, methodology and platform reported to three different VPs, internal centers of power competed for budgets. (course day 1, transcript)
- Shift-left is the endgame chain: dashboard certification → mart quality → raw-layer quality → data contracts → product thinking on source-system owners. For backend teams "data is exhaust — they need to ship features"; breaking that paradigm is a CDO's real job. (course day 2, transcript)

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
