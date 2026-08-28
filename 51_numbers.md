---
type: cross-cutting
purpose: Every number in this KB with its source and how much to trust it
---
# Numbers registry

Every quantity that appears anywhere in this knowledge base, in one table set, with a reliability tag attached to each one. The point is speed: an agent building an argument should be able to find the right number *and* know in the same second whether it survives being challenged.

**The five reliability tags**

| Tag | Meaning |
|---|---|
| `measured` | Somebody actually counted it in a real company — the author's own platform, or a named/anonymized peer case from his interviews |
| `benchmark` | Published industry research: Gartner, Eckerson/RateMyData, DAMA, academic papers, public vendor-neutral benchmarks |
| `vendor` | A vendor or consultancy claim. Marketing. Copy the *logic*, discount the number |
| `author-estimate` | The author's judgement, design target, or rule of thumb — not a measurement |
| `disputed` | The author himself flags it as mythology, marketing, or "based on nothing". His words are kept in the row |

**Standing warning.** If you find a number in this KB that is not in this registry, it has no reliability tag — do not quote it in a board deck, a business case, or an argument with a sponsor until it is tagged here. An untagged number is an unattributed number.

## How to use a number in an argument

- **Pair `measured` with `benchmark`.** Lead with the thing somebody counted, corroborate with published research. One `measured` number from your own platform beats three benchmarks.
- **Never lead with `vendor`.** Collibra's 23% and Forrester's TEI are useful as *evaluation structures*, not as evidence. If you must cite one, cite it as "the vendor assumes X — we assume Y".
- **Always state the denominator.** "2% of DG programs deliver high business value" is N=59 on a vendor self-assessment site. "30% of objects have owners" is on an audience of 30 analysts. The denominator is usually the whole argument.
- **Say out loud when a number is a target, not an achievement.** The "what it says" column marks these. A 20% core-penetration target that delivered 2% is the single most useful cautionary row in this file.
- **When you quote a `disputed` number, quote the dispute with it.** These are trust narratives, not arithmetic; using them straight will cost you the room the moment someone checks.

## Text-to-SQL and AI accuracy

| Number | What it says | Reliability | Source |
|---|---|---|---|
| ~40% | Text-to-SQL accuracy on real enterprise schemas | `benchmark` | semantic-layer.md; semantic-metric-layer-v2.md (BI+AI Strategy, slides 49–64) |
| 6% vs 86% | GPT-4o on Spider 2.0 (enterprise) vs the academic benchmark — the gap *is* the argument | `benchmark` | Spider 2.0, spider2-sql.github.io; library.md |
| 85–95% | Text-to-SQL accuracy *with* a semantic layer; failure mode also changes — it declines instead of inventing | `author-estimate` | semantic-layer.md, "Numbers for arguing with optimists" (no primary citation attached) |
| 21% → 95%+ | Anthropic's agent evals without vs with the governed route + skills | `measured` | Anthropic blog, self-service analytics with Claude; cited in semantic-layer, skills-hub, domain-knowledge-base |
| 42.5% → 92.5% | Accuracy lift when the agent clarifies an ambiguous question instead of answering it | `benchmark` | arXiv 2508.15276; llm-assistant-architecture.md step 3 |
| 25% → 80% | Domain-assistant accuracy before vs after the domain knowledge base is filled | `author-estimate` | context-governance.md; domain-knowledge-base.md |
| 20% vs 80% | Agent accuracy without vs with grounding in certified sources | `author-estimate` | certified-core-layer.md, "Numbers for arguing" |
| ~75% | Accuracy of AI auto-documentation — "plausible enough to poison the layer if there is no gate" | `author-estimate` | context-governance.md |
| ≥70% verified share | **Target.** Health threshold for a context layer | `author-estimate` | context-governance.md |
| <5% false-accept | **Target.** Share of wrong atoms that slipped into verified; read only together with coverage | `author-estimate` | context-governance.md |
| 20k → 6k tokens | Context routing effect on simple queries | `author-estimate` | context-governance.md |
| 13 → 4 steps | Same routing effect, in agent steps; minutes → seconds | `author-estimate` | context-governance.md |
| ~95% | **Target/expectation.** Share of metric deviations eventually self-explained by metric notes | `author-estimate` | context-governance.md (course day 6, transcript) |
| ~61% of requests | Share of ad-hoc analytics requests automatable with SQL plus documentation | `benchmark` | domain-knowledge-base.md — field study of request threads |
| 2 198 threads | Denominator of the above field study | `benchmark` | domain-knowledge-base.md |
| ≥50% / ≥45% / ≥30% | **Targets.** AI-ready score thresholds: domain metrics healthy / dashboard views on certified / mart hits on certified | `author-estimate` | domain-knowledge-base.md |
| 100% | **Rule, not a measurement.** All machine-generated knowledge enters as `needs_review` — no exceptions | `author-estimate` | domain-knowledge-base.md |
| ~80% of a 10 000-term glossary | Captured by an AI prototype from public documents, against 9 months of manual work before (central-bank case) | `vendor` | ai-governance.md; domain-knowledge-base.md (course day 6, transcript — reported by a catalog vendor guest) |
| 9 months → prototype | The manual baseline the above replaced; "implementation TTM an order of magnitude faster" | `vendor` | dg-program-roadmap.md (course day 5–6, transcript) |
| up to 3 retries | Design parameter: text-to-SQL generation retries on error before giving up | `author-estimate` | llm-assistant-architecture.md step 5b |
| −7.7% junior employment | GenAI as seniority-biased technological change, over 6 quarters | `benchmark` | Hosseini & Lichtinger (Harvard), SSRN 5425555; library.md |
| ~50× | Growth in DQ-checker creation rate after an agent skill took over authoring, partners only approving | `measured` | skills-hub.md; data-quality.md (course day 3, transcript) |
| 160 datamarts in 1 day | Business-logic DQ checkers by one steward with one AI skill, against ~3 weeks by hand | `measured` | skills-hub.md; data-quality.md; ai-governance.md (course day 6, transcript) |
| ~3 weeks | The manual baseline for the same 160 marts | `measured` | data-quality.md (course day 6, transcript) |
| 28.5% → 60% | **Target.** Skills-hub penetration in one large tech company's pilot | `measured` (baseline) / target | skills-hub.md (BI+AI Strategy pilot) |
| 218 → 459+ of ~764 | Monthly active contributors, actual → target, against the audience in scope | `measured` (baseline) / target | skills-hub.md |
| 15 / 20 / 30 points, cap 60/mo | Design of the contribution point scheme: accepted trace / PR into a shared skill / published skill | `author-estimate` | skills-hub.md |

## BI content and scale

| Number | What it says | Reliability | Source |
|---|---|---|---|
| 100 / 70 / 25 / 10 / 5 % | The content funnel model: all dashboards → non-sandbox → in regular use → "healthy" → recommended key reports | `author-estimate` | bi-content-management.md (frame model) |
| ~13k dashboards | Order-of-magnitude funnel at a large marketplace: → ~90% outside sandboxes → roughly a third in use → a few hundred key reports | `measured` | bi-content-management.md (course day 3, slides p.103) |
| ~15k metrics | Same company: → ~30% important → ~10% in use | `measured` | bi-content-management.md (course day 3, slides p.103) |
| 12 800 → 11 500 → 4 100 → ~150 (now ~400) | The same dashboard funnel, exact counts: total → outside sandboxes → in use → key reports | `measured` | dg-program-roadmap.md (course day 3, slides p.103) |
| 15 182 → 4 604 → 1 464 | The same metric funnel, exact counts: total → important → in use | `measured` | dg-program-roadmap.md (course day 3, slides p.103) |
| 5 004 marts scored, 12 healthy | 0.2% — the health-dashboard baseline at programme start | `measured` | certified-core-layer.md (course day 3, slides p.115) |
| 780 tables / 21 fully described (3%) / 92 partial (12%) / 668 none (86%) | Metadata-completeness baseline at a large IT services company | `measured` | maturity-and-metrics.md (course day 6, slides p.33) |
| 24 807 columns, 3 363 described (14%) | Column-level half of the same baseline | `measured` | maturity-and-metrics.md (course day 6, slides p.33) |
| 0.12 to 0.59 | Per-domain metadata quality scores in that same scorecard; weights: columns described 0.8, four other criteria ~0.045 each | `measured` | maturity-and-metrics.md (course day 6, slides p.33) |
| 49% → 86% in a year | Table-description quality across ~7 000 tables after a "no description — no prod deploy" gate | `measured` | data-catalog.md; skills-hub.md (course day 4, slides p.48) |
| ~7 000 tables | Denominator of the above | `measured` | data-catalog.md (course day 4, slides p.48) |
| ≥300 chars | Auto-certification threshold for documentation length at a large tech company | `measured` | bi-content-management.md (course day 3, slides p.97–101) |
| 5 parameters / 3 simplified | Data-certification standard vs its simplified variant at the same company | `measured` | bi-content-management.md (course day 3, slides p.97–101) |
| once a year | Certification re-confirmation cadence, run during a cleanup event | `measured` | bi-content-management.md (course day 3, slides p.97–101) |
| ~1 year | Metadata age at which descriptions are auto-tasked for re-review | `measured` | data-catalog.md (course day 4, slides p.53) |
| 20% / 30% / −10% / 50% | **Targets.** Subbotnik goals: archive black-status objects / move grey-black out of prod folders / cut average open time for red-yellow reports / close spawned tech-debt tasks in 3 months | `author-estimate` | bi-content-management.md; getting-started.md (course day 3, slides p.104–109) |
| 36.6% (299/817), 97 certified | **Actual result** of one June subbotnik run — the reality against those targets | `measured` | bi-content-management.md; getting-started.md (course day 3, slides p.104–109) |
| 3 weeks light, ~10 h per BI developer | Real subbotnik format and per-person cost | `measured` | getting-started.md (course day 3, slides p.104–107) |
| 20% of a 4 PB Hadoop cluster | Cost saved by deleting data at a job-search platform — the one *direct* economy in the whole peer study | `measured` | maturity-and-metrics.md; dg-kitchen-research.md (course day 6, slides p.34) |
| ~7M RUB/month | Search-and-understanding losses attributable to the catalog use case at a large tech company — "not that much" at that scale | `measured` | data-catalog.md (course day 4, transcript) |
| ~3–4 hours → ~15 min | An ad-hoc's data communication today vs the **target** with a certified documented catalog plus assistant | `measured` (baseline) / target | data-catalog.md (course day 2, transcript) |
| ~100+ analysts | The scale at which the catalog case starts working | `author-estimate` | data-catalog.md; getting-started.md (course day 2, slides p.35) |
| an order of magnitude | **Prediction.** Growth in volume of code, dashboards and data artefacts in the AI era | `author-estimate` | skills-hub.md; ai-governance.md (course day 6, slides p.96) |
| thousands of tables, 15 000+ metrics | Real-company scale, stated as beyond any academic benchmark | `measured` | semantic-layer.md |

## Certification and the core layer

| Number | What it says | Reliability | Source |
|---|---|---|---|
| 20% target → 2% delivered | Core-layer penetration after a year without dedicated capacity and enforcement. The honest lesson of the whole theme | `measured` | certified-core-layer.md |
| 47% → 35% (2026) → 25% (2027) | Share of user queries with 2+ joins: **current, then targets** | `measured` (47%) / targets | certified-core-layer.md; domains-and-data-mesh.md (course day 3, slides p.114) |
| 1% → 15% → 40% | Share of analyst queries hitting core tables: **current, then targets** | `measured` (1%) / targets | certified-core-layer.md; domains-and-data-mesh.md (course day 3, slides p.114) |
| tbd | Total mart count in the mart schema — deliberately left blank on the goals slide rather than invented | `measured` (absence) | certified-core-layer.md (course day 3, slides p.114) |
| 2026 | Platform billing arrives — marts become resources domains pay for. A scheduled event, not a hope | `measured` | certified-core-layer.md (course day 3, slides p.114) |
| 3 badges | Candidate / Certified / Degraded — the maximum public status count before badge inflation | `author-estimate` | certified-core-layer.md (course day 3, slides p.119–120) |
| 4 criteria | Binary assurance criteria in health scoring: ready on time / can be trusted / convenient to use / resource-efficient | `author-estimate` | certified-core-layer.md (course day 3, slides p.115) |
| ~10th version | Number of health-scoring methodology revisions so far — "we keep changing it, hopefully for the last time" | `measured` | certified-core-layer.md; data-quality.md (course day 3, transcript) |
| 1 quarter | **Target** duration of a Core Data Deep Dive per domain, after which the platform data engineer leaves | `author-estimate` | certified-core-layer.md (course day 3, slides p.116) |
| ~80% of companies | Share where the core layer will be built by data engineers, "who by nature are not product people" | `author-estimate` | certified-core-layer.md; domains-and-data-mesh.md (course day 3, transcript) |
| 3 months | Dashboard certification shipped as the first visible DG win at a large marketplace | `measured` | getting-started.md; dg-program-roadmap.md (course day 6, transcript) |
| ~1 year | Time over which the certified layer was marked across reports, marts and metrics — "past the point of no return", done without a DG team | `measured` | certified-core-layer.md (course day 6, transcript) |
| 80% of the governance you need | Minimal viable version: an Excel registry of your most important marts with named tech and business owner, checkers and docs | `author-estimate` | certified-core-layer.md; getting-started.md; data-quality.md (course day 3, transcript) |

## Data quality

| Number | What it says | Reliability | Source |
|---|---|---|---|
| 3 automatic checkers | Coverage rule for the ENTIRE warehouse: record completeness, freshness/actuality, format (allowed range folds in) | `author-estimate` | data-quality.md (course day 4 and day 2, transcript) |
| 90% of checkers are basic | Complex business checkers are rare and built per critical entity — but carry outsized value | `author-estimate` | data-quality.md (course day 4, transcript) |
| ~30% of all data is critical | Criticality threshold reached at a large classifieds player | `measured` | data-quality.md (course day 4, slides p.99, 146) |
| ~80% of critical data | **Target ceiling, stated as a refusal of 100%:** "you can't properly manage even critical data to 100%, and I don't need 100%" | `author-estimate` | data-quality.md; dg-frameworks.md; dg-kitchen-research.md (course day 6, transcript) |
| 2-day SLA | Super-critical fix **and recalculation**, under an automatic criticality classification built as a zero-bug-policy analogue | `measured` | data-quality.md (course day 4, slides p.145) |
| 3 / 3 / 2 / 1, threshold >10 | CDE Factor Rating Method weights — Regulatory / Compliance / Accounting / Operational — and the CDE score cut-off | `author-estimate` | data-quality.md (course day 3, slides p.33) |
| 3 levels | Autonomous validation levels: ingestion, storage, presentation — each with its own go/no-go and saved status | `author-estimate` | data-quality.md (course day 1, slides p.75) |
| 7 layers | DQM test pyramid: contracts → unit tests → pipeline checks → observability → DQ monitoring → functional tests → ad-hoc. "The lower, the cheaper and more reliable" | `author-estimate` | data-quality.md (course day 4, slides p.157) |
| 90% of DQ systems in the wild | Are a self-written checker engine plus incident dumping, and nothing else | `author-estimate` | data-quality.md (course day 4, transcript) |
| 10% of the sample | Companies monitoring DQ incident SLAs, out of 20 interviewed | `measured` | dg-kitchen-research.md (board frame 6) |
| ~10% of critical objects | Checker coverage at one peer, with technical checks only on the first layer and nothing business-level above it | `measured` | data-quality.md; dg-program-roadmap.md (course day 6, slides p.107) |
| 2 checks | The author's own DQ module at baseline — duplicates and nulls, analysts free to add their own. "The tool exists = the process doesn't" | `measured` | data-quality.md; dg-kitchen-research.md (course day 4, slides p.145) |
| 3 years | Time the author's own catalog has lived without a business glossary — "problematic, but we can't find a driver for it" | `measured` | data-catalog.md; getting-started.md (course day 4–5, transcript) |
| every check = money | No number, but the design constraint at a ride-hailing big-tech on pay-as-you-go compute: they deliberately do NOT blanket the warehouse | `measured` | data-quality.md (course day 4, slides p.145) |

## Data catalog

| Number | What it says | Reliability | Source |
|---|---|---|---|
| 4–45% with owners | Share of assets with an owner across domain collections in a Purview audit — "a typical starting picture worth showing to sponsors" | `measured` | data-catalog.md; roles-and-operating-model.md (course day 3, slides p.24) |
| 46–74% without classification | The other half of that same audit | `measured` | data-catalog.md (course day 3, slides p.24) |
| 30% of objects with owners | Custom catalog at a job-search platform, on an audience of 30 analysts — "a rather sad current situation" | `measured` | data-catalog.md (course day 4, slides p.87) |
| 30 analysts | The denominator that makes the 30% figure sting | `measured` | data-catalog.md (course day 4, slides p.87) |
| 900 power users vs 90 monthly actives | ~10% penetration at a delivery company's DataHub deployment, in prod and view-only | `measured` | data-catalog.md (course day 4, slides p.87) |
| 80% penetration | **Target.** Share of the target persona a catalog should reach; WAU is the right frequency, not DAU/MAU | `author-estimate` | data-catalog.md (course day 4, slides p.53) |
| 42.6 / 40.7 / 37.0 / 25.9 / 22.2 / 22.2 / 11.1 % | Eckerson catalog deployment challenges: tool complexity / lack of adoption / lack of integration / missing functionality / missing data or objects / no access to actual data / users don't trust the information | `benchmark` | data-catalog.md (course day 4, slides p.65) |
| ~70% | Share of the 20 interviewed companies on DataHub — but see the next row | `measured` | dg-kitchen-research.md (board frame 4) |
| 2 of 7 | DataHub share on the catalog *sub-sample* slide. The honest denominator when quoting the above | `measured` | data-catalog.md; dg-kitchen-research.md (course day 4, slides p.87) |
| <6 months, 3 part-time people | Fastest rollout in the peer set — a commercial catalog chosen on one decisive criterion (open push API) | `measured` | data-catalog.md; dg-kitchen-research.md (course day 4, slides p.87) |
| 1 quarter, 3 engineers → team of 10 | Custom open-source catalog MVP (1 front-end + 2 Go back-end), growing to a team of up to 10 by year two | `measured` | data-catalog.md (course day 4, slides p.87) |
| ~1.5–2M RUB per connector | RU catalog pricing beyond the base box's ~2 connectors; steward, admin seats and instances licensed separately | `measured` (practitioner report) | data-catalog.md (course day 4, transcript) |
| tens of millions RUB, >100M with implementation | Total RU catalog licence cost band; SaaS vs on-prem shifts it materially | `measured` (practitioner report) | data-catalog.md (course day 4, transcript) |
| 90% of companies | Share for which the boxed catalog solution is optimal | `author-estimate` | data-catalog.md (course day 4, transcript) |
| top 20% node objects | The curation rule: most-queried objects or those in the most-viewed reports; raise requirements there, lower them elsewhere | `author-estimate` | data-catalog.md (course day 4, slides p.47) |
| every 3–6 months | CSAT cadence, run out-of-band because in-product feedback gets tarnished by the latest bad experience | `author-estimate` | data-catalog.md (course day 4, slides p.53) |

## Roles and capacity

| Number | What it says | Reliability | Source |
|---|---|---|---|
| ~95% second hat | Share of steward/custodian roles that are a hat, not a position | `author-estimate` | roles-and-operating-model.md; dg-kitchen-research.md (course day 1, transcript) |
| ~5 people | Size of a whole-company dedicated steward team including catalog developers — already unusual | `measured` | roles-and-operating-model.md (course day 3, slides p.52–53) |
| 0.2–0.3 FTE per person | Ownership spread across teams when there is no budget | `author-estimate` | roles-and-operating-model.md; getting-started.md (course day 5, transcript) |
| ~70% of cases | Success rate of the "platform tax" — each domain committing a % of existing capacity — at the author's company | `measured` | roles-and-operating-model.md; getting-started.md (course day 2, transcript) |
| ~20% of time | Capacity reserved for governance by an administrative agreement that "tech debt includes data governance" | `measured` | roles-and-operating-model.md; domains-and-data-mesh.md (course day 2, transcript) |
| ~20 domains | Number with designated BI partners at a large tech company, with governance activity wired into the competency matrix | `measured` | roles-and-operating-model.md (course day 2, transcript) |
| 6 of 20 | People carved out of an overloaded DWH team for governance, zero new hires, overhead hidden inside product work | `measured` | roles-and-operating-model.md (course day 2, transcript) |
| 1 BI developer per 133 users | Density at a neobank with no formal BI function; 50+ person cross-data team acting informally as BI CoE; 10 000 MAU on the BI tool | `measured` | roles-and-operating-model.md; dg-kitchen-research.md (course day 3, slides p.62) |
| ~20 stewards, 3 VPs | A large telecom ecosystem's DG team before it "dissolved organizationally" — practice, methodology and platform reporting to three different executives | `measured` | dg-kitchen-research.md; roles-and-operating-model.md (course day 1, transcript) |
| 6-person standing DG team | One delivery platform: 2 tooling, 2 compliance, 1 AI/ML governance, 1 manager — the far end of the funding ladder | `measured` | roles-and-operating-model.md (course day 3, slides p.72) |
| 80–85% / <20% / <5% | **Benchmark for escalation design (DAMA):** conflicts resolved at business-unit stewardship level / reaching the DG Council / reaching the Steering Committee | `benchmark` | dg-frameworks.md; roles-and-operating-model.md (course day 5, slides p.65) |
| 65% | Share of the 20 interviewed companies where the Data Custodian role works, filled by systems analysts and data engineers | `measured` | dg-kitchen-research.md (board frame 3) |
| tech lead + 2–3 engineers | Standard shape of the platform team that builds the DQ tool; a dedicated DQ Engineer role only appears where data directly makes money | `author-estimate` | data-quality.md; roles-and-operating-model.md (course day 4, transcript) |
| 2–3 leads/seniors, 2+ years tenure | Prescribed MVP DG team profile. Tenure is a selection criterion, not a preference | `author-estimate` | getting-started.md; dg-program-roadmap.md (course day 6, slides p.100) |
| 2–3 of 10–20 domains | How many will be genuinely proactive without persuasion. Start there; the rest "get worn down by success posts" | `author-estimate` | roles-and-operating-model.md; domains-and-data-mesh.md (course day 3, slides p.88) |
| 1 / 1 / 3–10 / 3 / 3 | Lean DG sizing: one problem, one domain, 3–10 datasets, 3 minimum roles, 3 automated checks; plus 30-min weekly data office hours and quarterly expansion by 3 datasets | `benchmark` (Marcel Dybalski, endorsed) | dg-frameworks.md (course day 1, slides p.56, 119) |
| ~2 dozen companies max | Number in Russia at a scale where real DG committees genuinely emerge | `author-estimate` | dg-frameworks.md; roles-and-operating-model.md (course day 5, transcript) |
| 8 years | Time a large IT services company took to build fully controlled centralized executive reporting — "quality I have never met since" | `measured` | domains-and-data-mesh.md (course day 2, transcript) |
| 1 domain pair per year | Scoping discipline that made metric ownership work at a real-estate classified | `measured` | dg-program-roadmap.md; domains-and-data-mesh.md (course day 5, slides p.32–33) |
| 2 years | Time a real-estate classified took to reach an explicit Data Custodian role, after stewardship visibly failed | `measured` | roles-and-operating-model.md (course day 3, slides p.71) |

## Maturity and ROI

| Number | What it says | Reliability | Source |
|---|---|---|---|
| 2.88 / 5.0 | Average DG maturity, high end of "Initiating" | `benchmark` | maturity-and-metrics.md (Eckerson / RateMyData, course day 6, slides p.39–43) |
| N=59 | The sample behind every RateMyData number below. Quote it whenever someone waves the 2% figure | `benchmark` | maturity-and-metrics.md (course day 6, slides p.39–43) |
| 3.56 / 3.15 / 2.86 / 2.75 / 2.70 / 2.46 | Category scores: Culture / Data Management / Processes / Roles / Program / Technology | `benchmark` | maturity-and-metrics.md (course day 6, slides p.39–43) |
| 2% high / 39% moderate / 39% low / 22% none | Business value delivered by DG programs | `benchmark` | maturity-and-metrics.md; getting-started.md (course day 6, slides p.40–43) |
| 54 / 46 / 46 / 46 / 44 / 40 / 38 / 37 % | Top DG challenges: lack of stewards / conflicting priorities / lack of a plan / unclear responsibilities / lack of time / inadequate tools / resistance to change / no executive support | `benchmark` | maturity-and-metrics.md (course day 6, slides p.39–43) |
| 3.65 "Deploying" vs peer avg 3.0 | The author's own result on the same instrument — a short questionnaire producing a number precise to two decimals | `measured` | maturity-and-metrics.md (course day 6, slides p.39) |
| 80% of D&A governance initiatives fail by 2027 | Gartner. Shelfware catalogs are the default outcome. **⚠ URL unverified in `40_sources.md` — re-verify before public citation** | `benchmark` | context-governance.md; 40_sources.md |
| 10 topics, 97 criteria, 6 themes | UK Government Data Maturity Framework — the author's pick of open models; themes weighted Culture 24 / Data 22 / Leadership 17 / Tools 13 / Skills 12 / Uses 9, five levels per criterion | `benchmark` | maturity-and-metrics.md; dg-program-roadmap.md (course day 6, slides p.44–45) |
| 7 dimensions, 25 sub-areas, ~150 blocks | Size of the author's D&A Maturity Assessment map (Data informed → Driven → Led) | `author-estimate` | maturity-and-metrics.md; 00_index.md |
| 13 components, 26 metrics, weights = 1.00 | Data-Driven Index structure | `author-estimate` | maturity-and-metrics.md |
| 0.15 / 0.15 / 0.13 / 0.12 / 0.12 / 0.09 / 0.06 / 0.03×5 | DDI example weights: Data Literacy, Tools Adoption, Direct Business Value, Data Management, Data Accessibility, Organisational Model, Culture, then five components at 0.03 | `author-estimate` | maturity-and-metrics.md; data-literacy.md |
| 62.99 (dashboard 62.9, +11.1 YoY) | DDI worked example total | `author-estimate` (template example) | maturity-and-metrics.md |
| 10% / 14% / 99% / 95% | DDI worked example extremes: weakest = NPS improvement and cost reduction from data decisions; strongest = infrastructure uptime and ad-hoc duration | `author-estimate` (template example) | maturity-and-metrics.md |
| 5 of 12 | Threshold on the self-assessment test: 5+ relevant pain statements → a DG program likely pays for itself | `author-estimate` | getting-started.md (course day 2, slides p.24) |
| 1 of 4 → 2 of 4 | Sponsorship gates: one C-level (CDO/CTO/CFO/CEO) to start the MVP; two plus the MVP domain owner to scale to a program | `author-estimate` | getting-started.md; dg-program-roadmap.md (course day 6, slides p.100) |
| 20–30 use cases | Maximum size of the bottom-up business-case pile; individually small, collectively proof of a systemic problem | `author-estimate` | getting-started.md; maturity-and-metrics.md (course day 2, slides p.47–49) |
| 12 streams × 4 half-years, 61 tasks | Size of the roadmap deployment grid | `author-estimate` | dg-program-roadmap.md; 00_index.md |
| *(withheld)* | The author's own honest monthly money effect for his whole DG slice — deliberately not published in this repo. What survives is the shape: a truthful DG ROI looks small against product economics, and knowing that before a sponsor sets expectations is the useful part. | `measured` | author, withheld by request |
| 5–7% provable | What a productivity-improvement claim realistically survives to, against vendors' 23–26% | `author-estimate` | data-catalog.md; maturity-and-metrics.md (course day 4 and 6, transcript) |
| 60–70% | The author's own instrumented "share of analysts' target tasks" — his counter-datapoint to the 29–36% lost-time benchmarks | `measured` | maturity-and-metrics.md (course day 2, slides p.44; transcript) |
| 3 months → 2 months | Onboarding to full analyst productivity, with a well-described catalog. "The one multiplier worth stealing wholesale" | `author-estimate` | data-catalog.md (course day 4, transcript) |
| 92.29M RUB vs 35M RUB | Method 2 worked example — catalog labour savings vs cost (20M catalog TCO + 15M product team), built on 120×2.4M×23% + 45×2.0M×5% + 65×1.8M×15% + 10×2.0M×20% | `author-estimate` | maturity-and-metrics.md; data-catalog.md (course day 6, slides p.20) |
| 110M RUB vs 11.5M RUB | Method 1 worked example — cleaned-record economics: 100k duplicates × 100 RUB + 100k bad records × 1 000 RUB/yr profit, against 10M technical solution + 0.5M cleanup + 1M/yr upkeep. Guard printed under the formula: "one record is counted once" | `author-estimate` | maturity-and-metrics.md (course day 6, slides p.10, 23) |
| 320M records / 230M duplicates / 50% contact quality / >$300 acquisition / ~$300 per failed communication / >4B RUB effect | A large bank's published MDM business case — the reference for Method 1 | `vendor` | maturity-and-metrics.md (course day 6, slides p.11) |
| 30 years' payback | **The anti-case to memorise.** 10M direct-mail items/yr, ~10% wrong-address or duplicate, ~$500k/yr gross saved at 50c an item, only $100k net after $400k/yr new process upkeep, against $3M MDM investment | `vendor` | maturity-and-metrics.md; dg-program-roadmap.md (course day 6, slides p.16–18) |
| 9 → 6 business days | Month-end closing invoicing step at a mid-size company after a 2-FTE, one-quarter DG-as-a-service investigation | `measured` | getting-started.md; dg-program-roadmap.md; dg-kitchen-research.md (course day 2, slides p.41–43) |
| 2–3 excess workdays × 11 employees | The finance-team waste that funded a 3-person DG team off an Excel of small monetized cases; invoice deltas ran from 100€ to >100k€ | `measured` | getting-started.md; dg-kitchen-research.md (course day 2, slides p.41–43) |
| ~95% failure | Rate at which marching to business under the literal flag "Data Governance" fails | `author-estimate` | dg-frameworks.md; getting-started.md (course day 2, transcript) |
| 90% of projects | Share that never get a dedicated DG budget — which is why the no-budget branch is the *main* branch | `author-estimate` | dg-frameworks.md; getting-started.md; dg-program-roadmap.md (course day 5, transcript) |
| 20 companies, 5 countries, 3 000–100 000+ employees | Sample of the "DG Kitchen of the Tech Industry" (2024) interview research | `measured` | dg-kitchen-research.md |
| 40% | Share of that sample running no separate DG program at all — governance embedded in data-platform processes | `measured` | dg-kitchen-research.md (board frame 1) |
| 45% have a CDO / 30% bottom-up via infosec | Sponsorship shapes in the same sample | `measured` | dg-kitchen-research.md (board frame 1) |
| 2 of 20 | Companies with a consolidated business glossary plus metric tree — against metric divergence topping the pain list in the same interviews | `measured` | dg-kitchen-research.md (board frames 2 and 5) |
| 30% | Share of the sample scaling DG *back* after prolonged effort without visible results | `measured` | dg-kitchen-research.md (board frame 7) |
| 1 of 20 | Companies that ran an actual effectiveness analysis (chat search time vs catalog search stats × request volume × analyst FTE cost). It green-lit further investment | `measured` | maturity-and-metrics.md; dg-kitchen-research.md (course day 6, slides p.34) |
| 2–5 years | Anti-FOMO clause: how long laggard companies have before AI practices commoditize. "Nobody is late" | `author-estimate` | ai-governance.md; dg-program-roadmap.md (course day 6, slides p.97) |

## Industry mythology — cite only with the dispute attached

| Number | What it says | Reliability | Source |
|---|---|---|---|
| $1 prevent / $10 correct / $100 do-nothing | Per-record bad-data cost pyramid. Author's annotation, on the slide: **"$100 per bad data record — beautiful, but unrealistic"** | `disputed` | maturity-and-metrics.md (course day 6, slides p.12–15) |
| $8.495M three-year savings | The worked example built on that pyramid — "arithmetic on an invented constant" | `disputed` | maturity-and-metrics.md (course day 6, slides p.12–15) |
| 1x → 10 000x | Shift-left cost-by-finder chart. Author: **"frankly marketing, based on nothing"** — costing a CEO-found error means speculating about "fifteen minutes of his time and one un-made decision". Usable as a trust narrative, never as a business case | `disputed` | data-quality.md (course day 4, slides p.156) |
| ~40%/yr data growth; ~20% of a base is bad data | Bad-data rules of thumb carried on the same mythology slide | `disputed` | maturity-and-metrics.md (course day 6, slides p.12–15) |
| 30% of stored data used regularly; 33–70% of hardware IT spend on storage support | Data Management Institute. Labelled **"DG mythology"** on the slide itself | `disputed` | maturity-and-metrics.md (course day 1, slides p.43) |
| 70–80% of analyst time on data wrangling | Gartner. Same "DG mythology" slide | `disputed` | maturity-and-metrics.md (course day 1, slides p.43) |
| 15–35% of annual budget wasted due to poor DQ, up to 40% in services | Gartner. Same slide, same label | `disputed` | maturity-and-metrics.md (course day 1, slides p.43) |
| 29–36% unproductive time (finance worst at 36%), leaders at 5–10% | DIS Group. Counter-datapoint from the author's own instrumentation: his analysts' target-task share runs 60–70% — "the loss is real but a fraction of the claimed gap. Measure your own equivalent before quoting theirs" | `disputed` | maturity-and-metrics.md (course day 2, slides p.44; transcript) |
| up to 70% of cleansing effort wasted | McKinsey. Used approvingly as an anti-pattern warning, but it is a consultancy claim | `vendor` | data-quality.md; getting-started.md; dg-program-roadmap.md (course day 3, slides p.9) |
| hundreds of millions of dollars, 2+ years | One large company's failed enterprise-wide cleansing/data-lake initiative, "because nobody knew which data served which use cases". Same consultancy slide | `vendor` | getting-started.md; dg-program-roadmap.md (course day 3, slides p.9) |
| 23% / 5% / 26% / 27% | Collibra's assumed productivity gains: BI analysts and DS / report and app developers and architects / integration, DG and stewardship professionals / compliance professionals | `vendor` | data-catalog.md; maturity-and-metrics.md (course day 4, slides p.80–86) |
| $8.379M gain, 102 960 person-hours, 9.3× 3-year ROI vs $2.48M TCO | The output of that Collibra calculator on 120 + 120 + 45 people at $180k / $150k / $150k. Author: "you are simply asked to believe 23% and derive the rest" | `vendor` | data-catalog.md (course day 4, slides p.80–86) |
| $3.8M benefits PV vs $813K costs PV | Forrester TEI for Alation. Breakdown: $2.74M analyst productivity, $584K business self-service, $165K data engineers, $286K faster onboarding | `vendor` | data-catalog.md; maturity-and-metrics.md (course day 4, slides p.80–86) |
| 75 analysts / 70% of work affected / 70% time reduction / 50% capture / 10% risk adjustment / onboarding 2 months cut 50% | The visible assumption chain behind that TEI — "more instructive because the assumption chain is visible". Author's verdict: **"copy the evaluation logic, not the numbers"** | `vendor` | data-catalog.md; maturity-and-metrics.md (course day 4, slides p.80–86) |
| "replaces the data steward" / "design first, easy for business users" | The two 3rd-generation catalog claims the author personally question-marks on the vendor's own generations table | `disputed` | data-catalog.md (course day 4, slides p.89) |
| all vendor comparison quadrants | **"All available vendor comparisons are corrupt"** — made by vendors with dishonestly picked criteria; canonically, a vendor's own quadrant on which that vendor wins | `disputed` | data-catalog.md (course day 4, slides p.29) |
| "operational efficiency" and "innovation" as ROI petals | Crossed out by name on the classic six-petal ROI wheel: "a very shaky thing… in general it's air" and "also shaky". Data quality as a separate petal is also refused — "it always resolves into revenue or cost" | `disputed` | maturity-and-metrics.md; data-quality.md (course day 6, slides p.5) |
| decision-speed metrics | Closed topic. "Attempts to measure the acceleration of decision-making were worked over some ten years ago; it seems there are no fools left." Every company that went deep on it stopped | `disputed` | maturity-and-metrics.md; dg-program-roadmap.md (course day 6, transcript) |
| the indirect-benefit list | Multiplier on existing investments, faster onboarding, savings on audits and lawyers, fraud detection, accelerated decisions, easier self-service, problems fixed before they cost anything — eight items, one red X on the slide. "All plausible, all unbuyable" | `disputed` | maturity-and-metrics.md (course day 6, slides p.19) |
| the loss-vs-cost optimum curve | The textbook business-case curve. "We never managed to see a single such 'beautiful' curve of losses and costs built from several points" | `disputed` | getting-started.md; dg-program-roadmap.md (course day 1, slides p.44–45) |

## Numbers we do NOT have

The gaps an agent will hit. Do not fabricate around them — say the number does not exist and offer the nearest proxy.

- **Cost of a certification per object.** No number anywhere for what it costs to certify one mart, dashboard or metric — in hours, money or reviewer time. The nearest proxies are the subbotnik format (3 weeks light, ~10 h per BI developer, 97 objects certified in one run) and the 20%→2% core-penetration miss, which prices the *absence* of capacity rather than the presence of it.
- **Total mart count.** Deliberately left "tbd" on the core-layer goals slide rather than invented. The 5 004 scored marts is a health-dashboard scope, not a warehouse census.
- **Cost of one DQ check to run.** "Every check = money" is the constraint; the per-check figure is never stated. Nobody in the KB has published theirs.
- **Time-to-value effect of the catalog.** The peer study's own finding: TTM effect "impossible to assess because nobody tracks Jira properly". One company in twenty computed anything at all.
- **The denominator behind "~40% enterprise text-to-SQL accuracy".** Which schemas, which models, which query mix — not stated. Only the Spider 2.0 6%/86% pair has a published methodology.
- **Provenance of 85–95% with a semantic layer and of 25%→80% with a domain pack.** Both live in "numbers for arguing" lists without a primary citation. Treat as the author's working estimates.
- **Verification cost of AI-generated metadata.** The live, explicitly unresolved dispute: one camp says re-checking auto-generated docs costs about as much as doing the mapping by hand, the other says it doesn't make mistakes. No side has published a number. This is the single most useful measurement anyone reading this could go and take.
- **Net productivity after validation cost.** "The boost survives after subtracting validation costs, but it's smaller than the first emotions" — the net number is never given, only the gross (50×, 160 marts/day).
- **Cost of the human-in-the-loop burnout effect.** Named as a real hidden cost of agent-output review; unquantified.
- **Token economics of agent scenarios.** "After the 'Wild West' strategy comes the counting of burned tokens… there is not yet enough data to compare with the labour cost of doing it the old way."
- **Certified-object counts vs traffic.** The programme's declared key metric is *share of traffic* to core marts, yet the only published core-layer numbers are the join-share and query-share targets — no traffic baseline is stated.
- **Glossary cost.** Three years without one, "we can't find a driver" — no estimate of what building one would have cost.
- **Any ROI figure the author is willing to defend publicly.** His own number is withheld from this repo by request; treat the absence as the finding — nobody in the source material has a defensible public DG ROI.
