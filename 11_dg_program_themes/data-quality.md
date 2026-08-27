---
theme: data-quality
type: dg-program-theme
frames:
  - "3458764611490421980" # DQMS concept map [WIP]
  - "3458764611453525293" # Data quality tools taxonomy
  - "3458764612153156400" # Data Contracts (title-only placeholder)
---
# Data Quality

## What the board teaches
The core artifact is a concept map of a Data Quality Management System (inspired by datamanagement.wiki): 20 concepts and 33 labeled relations organized around a single center — *Data Issues* (non-fulfilment of data quality requirements). Everything else is defined by its relation to issues: Data Profiling identifies them, Data Quality Rules prevent them, Data Cleansing resolves them, DQ Monitoring detects and reports them, an Incident Tracking System tracks them, and Data Lineage investigates their root causes. Governance concepts (DQ Policy, Stakeholder Analysis, DQ Objectives) and structural concepts (Critical Data Elements, Roles and Responsibilities, Data Suppliers/Consumers, Data Delivery Agreements) frame that operational core — a compact way to explain what a DQMS actually consists of. A companion taxonomy splits the DQ tooling landscape into open-source DQ tools, proprietary DQ software, and ETL tools with strong built-in DQ. Data contracts appear as a named topic (currently a placeholder frame) and recur across the board as a Stage-2 "Reasonable Addition" initiative and an MVP project ("data contracts with systems teams"); the practitioner findings on 3-level DQ and tooling live in the DG Kitchen research (see [dg-kitchen-research.md](dg-kitchen-research.md)).

## Key objects
- Central concept: Data Issues (synonyms: anomalies, errors, DQ incidents, defects, nonconformities)
- Process concepts: Data Cleansing, Data Profiling, DQ Monitoring, DQ Rules, DQ Dimensions, Incident Tracking System, Data Lineage, Data Delivery Agreement (DDA), Defining Metadata
- Governance concepts: Data Quality Policy, Stakeholder Analysis, DQ Objectives
- Reference concepts: Critical Data Elements (CDEs); Roles and Responsibilities (owners, stewards, consumers, producers, analysts, custodians); Data Suppliers
- Relation vocabulary: "identified by", "can be prevented by", "can be resolved by", "are input for", "is assigned to", ...
- DQ tool taxonomy: open source DQ tools / proprietary DQ software / ETL tools with strong DQ
- Data Contracts: placeholder section on the board; positioned in roadmaps as embedded quality + documentation as code, contracts with backend systems and DWH/DL teams
- Related roadmap content: DQM stream (4.5) in Program Map 3.0 — DQMS scope, operational DQ processes (profiling, cleansing, assessment, monitoring), metrics/checks library, DQ in pipelines, DQ statuses in the catalog, criticality-driven coverage, DQ monitoring → data observability

## Frames on the board
- [Data Quality Management System (DQMS) concept map](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611490421980)
- [Data quality tools taxonomy](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525293)
- [Data Contracts (placeholder)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764612153156400)

## From the course (Data Governance Fundamentals, 6 days)

### Coverage strategy
- Author's coverage rule: cover the ENTIRE warehouse with 3 automatic checkers (record completeness, freshness/actuality, format) and treat everything else as business checkers required only from critical objects — that minimal kit "may already be enough." (course day 4, transcript; day 2, transcript)
- 90% of checkers are basic; complex ones are rare and built per specific critical entity — but they carry outsized value: one broken exec report destroys trust in the whole platform at once, even if fixed within a week. (course day 4, transcript)
- CDE selection via Factor Rating Method: weights Regulatory 3, Compliance 3, Accounting 2, Operational 1; CDE threshold score >10. Simple alternative: the data owner just picks. (course day 3, slides p.33)
- Threshold from a large classifieds player: only ~30% of all data is critical; steward-custodian pairs overseen by a data leader. Companion quote: "Under collective responsibility there must be leadership and a managing process, otherwise collective responsibility = irresponsibility." (course day 4, slides p.99, 146)
- DQ validation runs on at least 3 autonomous levels: ingestion (contract/schema/freshness gates), storage (anomalies, dictionary and business checks), presentation (published-data contract verification, consumer notification). (course day 1, slides p.75)

### Incident workflow and metrics
- Issue vs incident: an issue is a recurring problem from a checker; an incident is grouped issues processed as a Jira-like task. The business data steward's ONLY lane is reviewing incidents for business-logic adequacy; the technical steward does the actual work — don't merge the roles. (course day 4, slides p.119-120)
- Even in a data-mesh setup, keep base checker coverage + incident generation centralized: "delegating this to domains is a risky story — it just won't start." (course day 4, transcript)
- Aggregation trap: the more checkers you create, the worse your apparent quality (more detections). Weight events/objects/columns, report % days without incidents on critical objects — and pair with coverage metrics so nobody games it by deleting checkers. (course day 4, transcript)
- Practice at a large marketplace: on the top exec report a team KPI is "share of incidents discovered by business" — the team must announce incidents proactively in the channel with fix ETA; business finding it first counts against the metric. (course day 4, transcript)

### Data contracts in practice
- Two distinct contract types: source contract (system→DWH) and data-product/publisher contract (mart→consumers). The real power is the feedback loop — the producer commits to SLA-fix on THEIR side when a column nulls out or format drifts; works when source system and data folks share one domain team, nearly impossible when the system is detached from business domains. Behavior on breach (stop load vs load+alert) belongs in the contract text. (course day 4, transcript; slides p.129-130)
- Contracts as YAML: every delivery is checked against the contract; on breach alerts fire to both producer and consumer, so domain data people react before the problem reaches marts and reports. (course day 3, transcript)

### Anti-patterns and honest numbers
- 90% of DQ systems in the wild = a self-written checker engine + incident dumping. Typical failures: business checkers rarely get created, floods of false positives, incidents poorly triaged. (course day 4, transcript)
- Anti-pattern the author confesses from his own platform: checkers attached directly to core-layer tables/columns, skipping the business-term/business-rule layer — you cannot see which business rules exist for a field; rules smear across many objects. Checkers hanging off glossary terms would make requirements-to-checks traceable. (course day 5, transcript)
- The famous 1x→10,000x shift-left cost-by-finder chart "is frankly marketing, based on nothing" — the chart is really about trust, not cost. (course day 4, slides p.156; transcript)
- "There are things in life more important than DQ dashboards": cross-role agreed processes for defining DQ metrics, good slogans from authoritative management, bad-data alerting and shame lists, energy focused on important data — otherwise you drown in heavy DQ bureaucracy. (course day 4, slides p.144)
- Release-gate pattern: a release manager's checklist blocks pushing a datamart/dashboard to prod without a spec/description. Failure mode: business pressure to bypass ("your release manager is on vacation — ship it anyway"); the whole game is the balance between blocking checks and post-hoc checks. (course day 2, transcript)

### AI leverage
- An AI agent that authors DQ checkers itself (data partners only approve) grew checker creation ~50x at a large marketplace — it studies upstream lineage and proposes good, complex business checkers. (course day 3, transcript)
- War story: a domain data steward used an AI skill to create business-logic checkers for 160 datamarts in one day (normally ~3 weeks); the next bottleneck appeared immediately — checker-generated incident floods requiring an incident-management agent plus an eval-agent judging checker adequacy. "The boost survives after subtracting validation costs, but it's smaller than the first emotions." (course day 6, transcript)

## Links
- https://datamanagement.wiki/
