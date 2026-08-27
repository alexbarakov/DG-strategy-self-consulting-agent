---
theme: dg-program-roadmap
type: dg-program-theme
frames:
  - "3458764611453577668" # Data / AI Governance Program Map 3.0 (master map)
  - "3458764611453525287" # 12-stream x 4 half-year roadmap template
  - "3458764611802674402" # Land-and-expand roadmap, Stages 1-3
  - "3458764611825830326" # Reasonable way to start DG (staged flowchart)
  - "3458764611825791848" # Reasonable way to start DG (duplicate copy)
  - "3458764611453525277" # Section header: Basic Concepts of DG
  - "3458764611453561782" # Template cover: DG Implementation Plan
---
# DG Program Roadmap

## What the board teaches
The board's master artifact is the "Data / AI Governance Program Map 3.0": the whole DG journey staged 0-5, from Basic Concepts (0), through determining whether DG is needed at all (1), building a framework with goals and stakeholder buy-in (2, with sub-tracks 2.1 Common Sense DG and 2.2 DG MVP), launching the program (3), running projects in the most critical streams (4: catalog, certification/data products, DQ management, data operations, privacy/security, data literacy, stewardship), to developing the framework itself (5: operating model, cost-benefit model, maturity assessment, non-invasive DG, data strategy). Each stage carries explicit *fail branches* — "driver not found", "D&A maturity too low", "overestimating your determination", "pseudo DG: only a catalog with no business involvement". Two roadmap tools complement the map: a 12-stream × 4 half-year grid roadmap (61 task cards, recurring goal/domain-structure refinement checkpoints), and the "land and expand" roadmap that sequences initiatives into Stage 1 Essential Minimum → Stage 2 Reasonable Addition → Stage 3 Matured Focus, with sponsorship gates (C-level support 1/4 then 2/4) and a Budget Denial loop back to Common Sense DG + MVP restart. The philosophy throughout: stage order is a generalization, improvise, and return to your simplified framework when overwhelmed.

## Key objects
- Program Map 3.0 stages: 0 Basic Concepts → 1 Is DG necessary (drivers top-down, pain points bottom-up, barriers/risks; DG Drivers 1-3) → 2 Framework, goals, buy-in (DG Vision, ROI model, leader selection, 2.1 Common Sense DG, 2.2 DG MVP) → 3 Launch (policy, Data Office, roadmap, roles, comms/marketing) → 4 Critical stream projects (4.3 catalog, 4.4 certification/data products, 4.5 DQM, 4.6 data ops, 4.7 privacy & security, 4.8 data literacy, + stewardship program) → 5 Framework development (operating model, financials, maturity, active non-invasive DG, data monetization, data strategy)
- Fail branches: no driver / low maturity; insufficient value drivers for buy-in; insufficient determination against resistance; "pseudo DG" (catalog-only)
- 12 roadmap streams: preparation/goal-setting; own DG solution/framework; operational model; data catalog; data quality; data stewardship; privacy compliance; data access management; data certification; data literacy; data culture; other initiatives — each mapped across Stage 1-4 (half a year each)
- Recurring checkpoints: refine goals/roadmap; refine domain structure, role model, processes + audit of critical assets
- Land-and-expand stages: Stage 1 Essential Minimum (domain structure, metrics tree/ontology, lifecycle standardization, importance classification, roles, documentation by criticality, incident management, DQM coverage + public DQ status); Stage 2 Reasonable Addition (golden layer, PII classification, data contracts); Stage 3 Matured Focus (glossary, access automation, semantic layer and metric store)
- Budget Denial failure path → ongoing Common Sense DG + MVP restart; expansion triggers: MVP domain owner, interest from other domains, CDO/CTO/CFO/CEO support
- Author's manifesto of an effective DG leader: truly believe in DG; implement practically; explain DG concisely; never start without IT and business stakeholder support
- Data cleaning misconception: companies waste up to 70% of effort on cleaning (McKinsey); clean for critical use cases while building ontology and core data model
- Resource library: books (Seiner, Ladley, Eryurek, DMBOK2, ...), practitioner blogs, per-stage article cards, related boards and Excel template

## Frames on the board
- [Data / AI Governance Program Map 3.0 (master map)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453577668)
- [A (possible) roadmap for deploying a DG program — 12 streams x 4 stages](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525287)
- [Land and expand DG roadmap (Stages 1-3)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674402)
- [Reasonable way to start Data Governance](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611825830326)
- [Reasonable way to start Data Governance (copy)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611825791848)
- [Basic Concepts of Data Governance (section header)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525277)
- [Template - DG Implementation Plan (cover)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561782)

## From the course (Data Governance Fundamentals, 6 days)

### Selling the program to management
- Alfa-Bank DQ practice (Andrey Zavarzin, 2011): nobody has ever seen the textbook loss-vs-cost optimum curve in real life; top managers care about exactly two numbers — an agreed estimate of possible losses and the cost of works preventing them. "A positive start decision is always made when minimal losses exceed maximal costs." (course day 1, slides p.44-45)
- "Quality is free — what's expensive is poor-quality information": losses split into missed revenue and direct costs (fines, staff overload with unproductive work, idle equipment); most DQ costs are specialist salaries and tooling. (course day 1, slides p.44)
- Going to business under the literal flag "Data Governance" fails in ~95% of cases — the word itself evokes "distant and secondary"; package it under something else. (course day 2, transcript)
- Central thesis: "It is useless to explain DG to the business and wait for enthusiastic support... DG is a thing data/analytics leaders must arrive at themselves. The maturity of your own team in key positions decides." (course day 6, slides p.104)

### Business-case mechanics
- Map data & analytics use cases onto the company's value-adding process flows, score impact x feasibility; when ~20 cases each individually "doable without DG" accumulate, together they prove systemic problems worth a DG strategy. (course day 2, slides p.47-49)
- Attribution honesty: the only truly direct DG economy is infrastructure savings (hardware freed by deleting redundant datamarts); everything else is indirect — accepted if the logic is sound and numbers adequate. (course day 2, transcript)
- Read the company strategy and hang DG as the enabler under initiatives that already have money attached (e.g. a timber company's ~40% logistics-savings plan via route optimization, which needs many quality datamarts). (course day 2, transcript)
- Rostelecom (RT.DataGovernance): >1000 source systems, 10+ local DWHs; data search/assessment cut from ~23 person-days (sometimes infinite) to ~3.5 hours via catalog + lineage + unified business-term module. (course day 2, slides p.25)
- SOFTSWISS: a 2-FTE root-cause team investigated data & reports for one quarter; ISR invoice deltas ranged 100 EUR to >100k EUR, verification consumed 2-3 extra workdays of 11 finance employees monthly — a 3-person DG team was funded off an Excel of small monetized cases, with the Head of Internal Accounting as committee witness. (course day 2, slides p.41-43; day 6, slides p.108-110)

### Vision, goals, documentation
- DG Vision = a 4-6-page Amazon-style six-pager: problem analysis from drivers/pains, target framework concept, goals, metrics, projects, roadmap; refresh after each delivery cycle — "in the end it may be the only document you actually need." (course day 2, slides p.50; day 6, transcript)
- Goals come in three tiers: program goals (abstract, slogan-ish), DG team goals (SMART, annual), data steward goals (e.g. ">=98% of new product records accurate at entry"). Don't write goals you can't measure ("data transparency", "trust") — use reuse rate, DQ metrics, search speed. (course day 2, slides p.56-57)
- The framework's real function is focus retention "for boring but systematic movement over the course of a year", not control — "maybe a bit of bureaucracy won't hurt us now." (course day 5, slides p.64)

### Launching without a budget
- Packaging trick: relabel an existing stream of DQ projects as "DG working group + committee" and invite sponsors — "ordinary work, packaged so it can be tracked." (course day 5, slides p.64; transcript)
- Without a DG office you assemble the program piecemeal — e.g. extend dashboard certification into mart certification with Head of DWH and split the project between teams; documentation then exists per-component, not per-program, and that's fine. (course day 5, transcript)
- "Invisible / non-invasive DG": chain initiatives that pull each other (core layer pulls DQ checks, checks pull catalog, domains pull roles) — works, but "much slower than with a focused resource." (course day 6, transcript)
- Run an MVP even when approval is easy: it "knocks ideas against reality" and builds scaling themes; a large marketplace shipped dashboard certification in 3 months plus a data-cleanup event — both moved metrics AND worked emotionally, buying license for more expensive initiatives. (course day 6, slides p.104; transcript)
- Glossary heresy: the business glossary is "reserved for the mature" — there is never resource for it and physical/logical-level processes matter more; when you do reach it, it's a "nice suit", not the starting point. (course day 6, transcript)
- Data Strategy appears organically after DG start ("since we've already analyzed data structure, pains and value drivers"), not as a prerequisite — it is wider than DG and needs more business/IT involvement. (course day 6, slides p.121)

## Links
- https://docs.google.com/spreadsheets/d/1ZNnuGQrdlYCN6QgYwWb4ISFtcKl8gV-PvfyCtV3cGJE/edit?usp=sharing (Excel template of the guide)
- https://miro.com/app/board/o9J_lha8MnM= (D&A Maturity Assessment Tool by Data Nature)
- https://miro.com/app/board/uXjVOAch4J8= (Lords of the Boards)
- https://barakov.gumroad.com/l/BIAdoptionGuide ; https://barakov.gumroad.com/l/dataanalyticsmaturitymap
- https://data-nature.com/ ; https://t.me/datanature ; https://datanature.ru/datagovernance
- https://www.dama.org/cpages/home ; https://datamanagement.wiki/
