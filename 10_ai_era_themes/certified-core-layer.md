---
theme: Certified Core Layer
type: ai-era-theme
status: draft (child hexagons currently removed on the board — panel only)
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681730395308"
related:
  - "[[semantic-layer]] — stands on the certified core"
  - "[[bi-content-management]] — the content funnel that produces the certified layer"
---

# Certified Core Layer

**Tagline:** The trusted middle of the warehouse: marts with a declared, guaranteed trust status. The healthy diet of an AI analyst — and of everyone else.

## What is it

The core layer is the set of data marts with a declared, guaranteed trust status — an owner, an SLA, quality checks and metadata — plus active promotion of reuse instead of «I'll just build another mart». It is the trusted middle of the warehouse the semantic layer stands on.

Two mart profiles serve two needs: wide denormalized marts for exploration and ad-hoc, normalized ones for building derivatives. Both sit on one logical and conceptual model, and the layer starts from the most reused cross-domain entities — not from the sickest marts, where a project dies on the first hard case.

Why it needs governance muscle: cheaper production means more objects — the Jevons paradox — and complexity eats the gains. An AI analyst fed from thousands of uncertified marts produces plausible garbage. The dependency chain is core → certified metrics → agent accuracy → self-service.

## Key terms

- **Certified** — declared trust: owner, SLA, DQ coverage, metadata; the status is visible where the object is consumed.
- **Core mart** — governed and reused; wide profile for ad-hoc, normalized profile for derivatives.
- **Cross-domain entity** — an object every domain touches: customer, listing, order; the starting point of the layer.
- **Conceptual and logical model** — business entities and relations, and their table-level shape.
- **Health score** — penalties for no owner, staleness, no usage, duplicates; multipliers for wide and decision-level consumption.
- **Upstream check** — derived objects must stand on certified sources; checked at build, not discovered later.
- **Jevons paradox** — cheaper production → more objects → complexity eats the gains.

## Numbers for arguing with optimists

- The honest lesson: a 20% core-penetration target delivered 2% in a year — without dedicated capacity and enforcement the layer does not build itself.
- 20% vs 80% — agent accuracy without vs with grounding in certified sources.
- Thousands of marts, a single-digit certified share — the default state of a mature multi-domain warehouse.
- What AI adds now: generated DQ checks and descriptions with human-approved thresholds — check 100% instead of a sample.

## From the course (Data Governance Fundamentals, 6 days)

**Why certification is the spine**
- Author's core belief, stated as the course's spine: "Separating crap content from good content that is recommended for use is largely the key to solving many DG problems. Agent systems will demand exactly the same certification." (course day 1, transcript)
- Certification must run through the entire delivery chain, not one layer: certified marts → certified semantic-layer objects → certified dashboards/metrics → (soon) certified agents. "Trust sprawl happened inside the semantic layer too — many objects of low trust accumulated there and now need certification." (course day 5, transcript)
- DG budget defense in cost cuts runs through AI: "under all our agents there must be a core data layer, a semantic layer and certified reports — and certification can only be achieved communally" — AI-readiness of domains becomes the shield for DG budgets. (course day 3, transcript)

**Trust statuses and targets**
- Trust statuses: Candidate / Certified / Degraded (certified but currently failing health requirements — the fix queue). Certified implies default guarantees: owner + contacts, freshness SLA, base DQ thresholds, lineage, change rules as a contract. (course day 3, slides p.113, 120)
- Operational targets with numbers: share of user queries with 2+ joins 47% → 35% (2026) → 25% (2027); share of analyst queries hitting core tables 1% → 15% → 40%. Money case: platform billing arrives in 2026 — marts become resources domains pay for, the core layer cuts ownership cost. (course day 3, slides p.114)
- Health scoring = binary, manageable assurance criteria plus monitored control metrics (on time; can trust; convenient; resource-efficient); the author admits this is roughly the 10th version of the methodology. (course day 3, slides p.115; transcript)

**Rollout mechanics**
- Two per-domain tracks: Core Data Deep Dive (BI+DE project team audits the domain data model, backlog + roadmap on business-value cases, one quarter, then the DE leaves) vs Core Data Preparation (light: the domain BI partner runs core candidates through health scoring alone). Quick win: pre-mark objects that already qualify so the metric moves early. (course day 3, slides p.116)
- Build per horizontal domain (marketing first), with the explicit contract that vertical teams downstream reuse those data products instead of rebuilding; L1/L2 marts by criticality. (course day 5, transcript)
- Sequencing lesson: certify marts first, then reports, then metrics — even though reports feel closer. And the word "certification" itself "smells of bureaucracy" to some audiences — consider another term. (course day 3, transcript)
- Catalog badge best practices: few public badges (Promoted/Certified/Deprecated) to keep the user's cost of choice minimal; the right to certify strictly limited; certification continuously challenged and revoked on major changes; deprecation ships with a plan; operational management lives in domain cabinets, the catalog only shows public status. (course day 3, slides p.119)

**Lessons and war stories**
- Staffing trap: in ~80% of companies the core layer will be built by data engineers, who "by nature are not product people" — expect product-ownership problems and plan for them. (course day 3, transcript)
- Trust base at a large marketplace: over a year the certified layer was marked across reports, datamarts and metrics, with health scoring (distinct from DQ score) underpinned by processes, roles and monitoring — "we passed the point of no return." Done without a DG team. (course day 6, transcript)
- Data deletion is a governance project of its own: "deleting data sounds easy, but in any big platform it's several circles of hell" — it needs auto-certification, archiving logic and bots that go around asking owners; one big-tech player deleted enough to save 20% of a 4PB Hadoop. (course day 6, transcript; slides p.34)

## Sources

- Anthropic — a canonical table alone saves nothing: near-copies get deleted, and data code lives in one governed repo: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Author's course «BI+AI Strategy 2026», core layer module; field notes: https://t.me/datanature (post of 21 Mar 2026)
