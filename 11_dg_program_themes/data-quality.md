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

## Links
- https://datamanagement.wiki/
