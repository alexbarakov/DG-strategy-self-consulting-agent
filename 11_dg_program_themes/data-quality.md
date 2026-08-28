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

### What a DQMS actually is
- "DQ management is a lot of things — not just an engine with data checks." The house model: three walls — Ownership (owners, stewardship, shift-left to data engineers, consumer self-service validation, producer commitment expressed as contracts), Monitoring (assessment, KPIs, alerting, dashboards, automation), Improvement (standards, a reusable rule library for all CDEs, a cleansing escalation path, benchmarks between teams) — a DQ culture roof, and a tools floor (catalog, DQ platform, contracts, MDM). (course day 1, slides p.73)
- On the DAMA-NL DQMS map he circles exactly one band in red and labels it "every day hands-on work": metadata, DQ rules, CDEs, lineage, profiling, issues, monitoring, cleansing. Strategic layers exist — "but that's where the life is." (course day 1, slides p.74)
- Profiling is the gate, not a nice-to-have: you profile to decide which checks are needed and which aren't. Without a profiling tool inside the framework "it will be hard to move to the next step — creating checks, automating them and keeping them current, because this is a very changeable space." (course day 4, transcript)
- The strategic tier is one sentence for him: adopt a policy fixing what owners and stewards in domains must actually do — "and you can wire this to the mart certification project. Checkers must be a mandatory condition of certification." (course day 4, transcript)
- Minimal viable version of all of the above: a registry — Excel is fine — of your most important marts, each with a named tech owner and business owner, wired with checkers and documentation, and you watch that they "arrive intact every morning." For many companies that is 80% of the governance they actually need. (course day 3, transcript)

### Coverage: what to check and what deliberately not
- Coverage rule: cover the ENTIRE warehouse with three automatic checkers — record completeness, freshness/actuality, format (allowed range folds in here) — and treat everything else as business checkers required only from critical objects. That kit "may already be enough." (course day 4, transcript; day 2, transcript)
- The reason is economic: "ensuring quality is expensive," which is exactly why you classify first and right-size the framework. A smaller, cheaper frame is legitimate. (course day 2, transcript)
- "Don't try to boil the ocean hanging DQ checks on everything — the logic by which you define criticality is a core piece of any DG program." (course day 1, transcript)
- 90% of checkers are basic; complex ones are rare and built per critical entity — but they carry outsized value. An exec report holds many numbers, and when one breaks "trust is lost in all of them at once… it hits the reputation of the whole platform and the BI team," even if the fix ships within a week. So complex checkers still get built: "without them you won't catch these things." (course day 4, transcript)
- Requirements differ by layer and object type: focus checker requirements on the core model, treat everything else "by the sufficiency principle." (course day 4, transcript)
- Threshold from a large classifieds player: only ~30% of all data is critical; key metrics map to critical data; steward-custodian pairs under a data leader. Companion quote: "Under collective responsibility there must be leadership and a managing process, otherwise collective responsibility = irresponsibility." (course day 4, slides p.99, 146)

### The checker taxonomy he actually uses
- The working split is two-tier, not dimension-based: base/automatic checks (record completeness, freshness, format, allowed range) versus business checkers (logical checks, value ranges, time intervals, cross-period comparisons). (course day 4, transcript)
- He carries the full rule taxonomy on a slide — simple value comparison; accepted ranges (numeric, text length, hardcoded and dynamic date windows); aggregated-measure validation (min/max thresholds, aggregate range, median/percentile); change-detection (relative change since last value / yesterday / a week / a month); dictionary-values validation (values not in dictionary, unused entries, expected popular values); anomaly detection including seasonality- and holiday-aware ML variants — and then refuses to teach it: "I'll leave the classification here, I don't want to dig into it, it carries a very concrete applied idea." The coverage rule is what he argues for; the taxonomy is a shopping list you consult once. (course day 4, slides p.116; transcript)
- A third class most DQ frameworks miss: **architectural checkers**, used as certification criteria rather than data checks — contract coverage, no open incidents, column metadata filled, optimal storage structure, resources used correctly. "This is roughly the tenth version of the methodology." (course day 3, transcript; slides p.115)

### Criticality selection (CDE rating)
- Factor Rating Method: weights Regulatory 3, Compliance 3, Accounting 2, Operational 1; CDE threshold score >10. Simple alternative he treats as equally valid: the data owner just picks. (course day 3, slides p.33)
- The artifact that turns classification into action is a "critical data by domain" status table: criticality score, master-data-source coverage, key BI marts, current DQ status, plans per quarter. (course day 3, slides p.34)
- Master Data **Source** Management (explicitly NOT MDM): identify, optimize and own the master sources in the DWH, cut duplicate sources, focus ownership, checks and monitoring on those only. (course day 3, slides p.35)
- The industrialized version, from his own platform: automatic criticality classification built as "an analogue of a zero-bug policy," with a 2-day SLA for super-critical fix **and recalculation**. (course day 4, slides p.145)
- The honest ceiling: ~80% of critical data managed. "You can't properly manage even critical data to 100%, and I don't need 100%." (course day 6, transcript)

### Where validation runs
- At least three autonomous levels. Ingestion: go/no-go on the source's DQ status, ingest, validate schema against the contract, validate constraints (missing fields, invalid formats), measure freshness of the most recent record, save status. Storage: go/no-go, transform into a cleansing layer, detect anomalies (distribution, outliers, changes), verify categorical values against dictionary tables, run business checks, save status. Presentation: go/no-go, generate publishing datasets, verify published data against the publisher contract, detect anomalies, save status, notify the consumer. (course day 1, slides p.75)
- The same idea vertically as a DQM test pyramid with owners attached: data contracts (producers and owners) → unit tests (DE) → pipeline checks (DE) → observability (DataOps) → DQ monitoring (stewards) → functional tests (DQ testers) → ad-hoc tests (all data-literate users). "The lower, the cheaper and more reliable." The instruction is diagnostic: draw the pyramid and see which layers you actually have — "not all layers are mandatory, some you can check off depending on the complexity of your platform." (course day 4, slides p.157; transcript)
- Federated vs centralized DQ: "as everywhere, the hybrid approach rules" — but fix the responsibility boundary between the central DQ team and the domains **before** building tooling, "because these are two different approaches to the tool." (course day 4, slides p.159; transcript)
- Even in a data-mesh setup, keep base checker coverage and incident generation centralized: "delegating this to domains is a risky story — it just won't start." (course day 4, transcript)

### Issue, incident, and who owns which lane
- Issue vs incident: an issue affects data quality, is recurring, and keeps causing incidents until resolved; an incident is an unplanned event caused by an issue, tracked and resolved as a task in Jira/ServiceNow. The platform groups similar issues into incidents and then **filters** them — the slide carries an explicit "ignored incident" branch, the part homegrown engines skip. (course day 4, slides p.119)
- Four swimlanes, and the split matters: the Data Owner approves significant platform/application changes; the Business Data Steward's ONLY operation is reviewing incidents that require business knowledge; the Technical Data Steward / DataOps reviews and confirms the incident and manages the checks; the Data Engineer fixes or reloads and revalidates. Incidents, tickets and tasks must be linked. Don't merge the business and technical steward. (course day 4, slides p.120; transcript)
- Business's entire contribution to check design is the baseline: "can this metric fluctuate this much from week to week, or is that already an incident? Where should the baseline for detecting the problem be?" (course day 4, transcript)
- Staffing: a dedicated DQ Engineer role only emerges where data directly generates money (trading, banks); elsewhere it's a data engineer with a DQ focus. Standard shape — a platform team (tech lead + 2-3 broad-skilled engineers) builds the tool; technical stewards in domains either write checkers or "raise" the analysts and engineers who build the marts to write them. "No new role model arises." (course day 4, transcript)
- Practice at a large marketplace: on the top exec report a team KPI is "share of incidents discovered by business" — the team must announce incidents proactively in the channel with a fix ETA; business finding it first counts against the metric. (course day 4, transcript)

### Data contracts in practice
- Two distinct types: source contract (system→DWH) and data-product/publisher contract (mart→consumers). (course day 4, transcript; slides p.129-130)
- What's inside the YAML: asset identification, ownership (department + data steward), criticality (incident priority, resolution time), identity/primary keys, foreign keys and relations, privacy flags and security mode, SLOs (max delay days, availability %, minimum DQ KPI), per-column types, descriptions, unique/not-null constraints, formats, quality rules with ranges. Tooling named: dbt, Soda, Great Expectations. (course day 4, slides p.129)
- The end-to-end flow runs the contract at both ends of the pipe: revalidate_source_schema_contract → load_to_landing_zone → test_business_rules_landing → load_output_dataset → test_business_rules → validate_data_contract → publish. The contract is converted into DQ checks in both directions. (course day 4, slides p.130)
- The real power is the feedback loop, not the document — the producer commits to an SLA-fix on THEIR side when a column nulls out or a format drifts. Works when the source system and the data folks share one domain team and one goal ("we're all in one boat and we row"); nearly impossible when the system is detached from business domains. (course day 4, transcript)
- Behavior on breach belongs in the contract text: stop the load; load and alert; or pause and alert. "There are no universal answers" — it's a concrete business case each time. (course day 4, transcript)
- The check usually runs before the data lands in the platform; some source systems agreed to run it on their own side before sending, which needs a more custom interface but is doable. (course day 4, transcript)
- Contract metadata is catalog metadata: a contract "reflects all the meta you can then put into the data catalog" when the object lands — so contracts pay off twice. (course day 4, transcript)
- Contracts as YAML checked on every delivery; on breach alerts fire to both producer and consumer, so domain data people react before the problem reaches marts and reports. (course day 3, transcript)
- Sequencing: contracts are a Stage-2 "reasonable addition," not the opening move. (course day 6, slides p.100-101)

### The economics of checks
- Compute cost per check is a design constraint, not a footnote: at a ride-hailing big-tech on pay-as-you-go compute, "every check = money" — so they deliberately do NOT blanket the warehouse, lean on anomaly detection, and keep only single narrowly-targeted checks. Their own note: "trying to cover the critical layer of data — but it's a hard task." (course day 4, slides p.145)
- What checkers structurally cannot cover: data drift, gradual or sharp-then-vanishing — "you can't create that many checkers." That's the observability niche (Monte Carlo the reference leader, RU market barely served, most teams self-written). Observability matters for big platforms with large volumes and low ownership; compact centralized platforms get the same result from plain infra monitoring. War story: an attrition-prediction model fed on office-visit data, then lockdown. (course day 4, slides p.153-155; transcript)
- "Quality is free — what's expensive is poor-quality information": most DQ *costs* are specialist salaries and tooling. (course day 1, slides p.44)
- The 1x→10,000x shift-left cost-by-finder chart "is frankly marketing, based on nothing" — costing a CEO-found error means speculating about "fifteen minutes of his time and one un-made decision." Real accounting has two lines: direct losses and (hard) lost profit. "The chart is really about trust, not cost." The shift-left *practices* on the same slide he does endorse: DQ validation embedded in ETL scripts at development time, quality metrics wired into CI/CD to reject defective data immediately, schema contracts on every transfer. (course day 4, slides p.156; transcript)
- Program-level: financial ROI of DQ is nearly unmeasurable, and DQ shouldn't be its own petal on the ROI wheel — "it always resolves into revenue or cost." When money fails, operational metrics carry the communication, and the killer one is "days without incidents in critical reporting." Often business isn't asking for a number at all: "just rid me of this pain, make it not every day." (course day 6, slides p.4-5, 28-29; transcript)

### Measuring DQ itself
- Aggregating DQ upward is "quite debatable." Realistically two options: days without incidents per critical object summed upward, or weighted quality scores with field/object significance — and the second is where teams fail organizationally. (course day 4, transcript)
- Aggregation trap: the more checkers you create, the worse your apparent quality — you simply detect more events and "drown in red." Pair quality with coverage metrics so nobody games it by deleting checkers. (course day 4, transcript)
- But coverage is gameable too. Annotating a peer's DWH-metrics dashboard he writes: the checker-coverage metric is "easy to hack. You'd have to check the quality of the checkers themselves — and that's already overkill." Report both, and accept that neither is clean. (course day 4, slides p.143; transcript)
- "There are things in life more important than DQ dashboards": cross-role agreed processes for defining and updating DQ metrics; good slogans from authoritative management that focus teams on DQ; bad-data alerting aimed at data stewards plus shame lists; energy focused on important data — "otherwise you quickly drown in heavy DQ bureaucracy." The blunter version in the room: "DQ monitoring is a good thing, but in practice you can do more sensible things." (course day 4, slides p.144; transcript)
- Direction of travel, from an insurer's published shift: stop counting governance quantity (standards, stewards, glossary terms), start measuring business impact — % of call-center calls caused by data defects, % of manual processes with automated validations, % of reserves held due to data issues. (course day 6, slides p.30-31)

### AI-authored checkers, and the bottleneck right behind them
- An AI agent that authors checkers itself (data partners only approve — "they look at them with their eyes and agree") grew checker creation ~50x at a large marketplace; it studies the upstream lineage and proposes good, complex business checkers. (course day 3, transcript)
- The mechanism is profiling: the agent profiles the table upstream and proposes ready checkers across many columns — "just take them and accept." Consequence: "the time to create custom checkers will drop and making them will become more pleasant." (course day 4, transcript)
- War story with numbers: a domain data steward used an AI skill to create business-logic checkers for 160 datamarts in one day — normally ~3 weeks, and these were real per-mart business checkers, not templates. The next bottleneck appeared immediately: the checkers flooded incidents, which requires an incident-management agent, plus an eval-agent judging checker adequacy "because they can decidedly be fake — the level of business context may still be insufficient." (course day 6, transcript)
- The verdict: this "grows into a system that is expensive to support, which — if you believe in it and invest — probably gives a boost, but it's a luxury that not everyone can afford right now." And: "the boost survives after subtracting validation costs, but it's smaller than the first emotions everyone feels." (course day 6, transcript)
- Hidden human cost: the operator must verify everything the agent produced, and a full day of purely intellectually-loaded verification "hollows a person out much faster than when the operation was mixed with routine." (course day 6, transcript)

### DQ tooling vs DQ process
- "90% of DQ systems in the wild = a self-written checker engine + incident dumping." What follows: business checkers rarely get created, floods of false positives, incidents poorly triaged — "and then the feeling that you therefore have data quality management does not appear." (course day 4, transcript)
- Why the tool is not the variable: unlike catalogs, "these tools work — they never require complex social scenarios inside themselves. You just need a good checker library and a good performant engine. And that's it." Which is exactly why process, roles and criticality logic decide the outcome. (course day 4, transcript)
- The self-diagnosis on the peer benchmark slide, about the author's own platform: a DQ module with two checks (duplicates, nulls), analysts free to add their own — "the tool exists = the process doesn't." (course day 4, slides p.145)
- Catalog is not a DQM solution: "the catalog's role is not quality control, but maximum dissemination of the results of that control." Catalogs are bad DQM tools; DQM tools are mediocre, overcomplicated catalogs; simple integration between the two is the pragmatic strategy. A practitioner veto seals it — a catalog's engine is not built for high-performance DQ checks, which killed the "DQ inside the catalog" option in one enterprise evaluation. (course day 4, slides p.67; transcript)
- On the normative base: a DQ Policy is "the intention and direction of an organization regarding data quality, formally expressed by its management" — input to managing CDEs and suppliers, framework for DQ objectives, part of the DQMS. He ships a real bank policy as a reusable example, then deflates it: "in most companies this is generally an absent, unnecessary story. Maybe somewhere in vain." (course day 4, slides p.132-134; transcript)
- Cheapest process control available: a release manager's checklist that blocks pushing a datamart or dashboard to prod without a spec/description. Failure mode is social ("your release manager is on vacation — ship it anyway"); the whole game is the balance between blocking checks and post-hoc checks. (course day 2, transcript)

## Maturity signals
From the author's peer interviews across the tech industry (course day 4, slides p.145; course day 6, slides p.107) plus his commentary. The ladder is about *process* — every company on it already has an engine.

- **Stage 0 — tool without process.** A DQ module running two checks (duplicates, nulls); analysts may add their own if they feel like it; no criticality classification, no coverage target. Annotation: "the tool exists = the process doesn't." (course day 4, slides p.145)
- **Stage 1 — coverage exists, but voluntary.** A perfectly decent in-house DQ tool that is "used voluntarily, without control or goals" — flagged red on his slide. Adjacent variant: checker coverage at ~10% of critical objects, with technical checks only on the first layer (notifications, autotasks, source update-time comparison, comparison with yesterday) and nothing business-level above it. (course day 4, slides p.145; course day 6, slides p.107)
- **Stage 2 — mandatory basics, status visible.** A base set of obligatory checks covers most objects; per-table check status is surfaced in the catalog; table tiering exists so checks are enforced only on critical tables. The recurring open question here: "we want to show DQ in dynamics — will that even work?" (course day 4, slides p.145)
- **Stage 3 — criticality-driven with an SLA.** Automatic criticality classification (zero-bug-policy analogue), a 2-day SLA for super-critical fix *and recalculation*, and a metric controlling checker coverage. (course day 4, slides p.145)
- **Stage 4 — business-facing accountability.** Cross-checks on golden marts for the most-asked metrics; domain teams each owning collect / ETL / MDM / autochecks / DQ for data in and out; and a team KPI on the exec report of "share of incidents discovered by business," with proactive announcement and fix ETA. (course day 4, slides p.145; transcript)
- **Orthogonal signal — economics.** Once compute is charged per query, "every check = money" and the mature move flips: deliberately *not* blanketing, letting anomaly detection self-surface problems, keeping only narrowly-targeted manual checks. Maturity here looks like fewer checks, not more. (course day 4, slides p.145)
- **Governance signal.** Only ~30% of data declared critical; key metrics explicitly mapped to critical data; a steward↔custodian pair per area under a data leader. (course day 4, slides p.146)
- **Disqualifying signal at any stage.** Dev doesn't monitor event emission, QA rarely tests data events, data teams do have SLAs — and still "nobody in data teams can answer: is our data quality good, and how good, in metric terms?" (course day 4, slides p.99)
- **Industry trend worth citing.** From repeat interviews: the maturity level in quality management "has grown over the last three years — coverage of critical objects with checks has become higher," because companies accumulated their own experience, not because tooling improved. (course day 4, transcript)

## Anti-patterns
- **Engine-and-dump.** A self-written checker engine plus incident dumping and nothing else — 90% of what exists. Business checkers rarely created, false positives flooding, incidents badly triaged. (course day 4, transcript)
- **Voluntary DQ.** A good tool adopted without control and without goals — flagged red on the peer slide precisely because it looks like success from outside. (course day 4, slides p.145)
- **Checkers on columns instead of business rules.** The author's confessed anti-pattern from his own platform: checkers attached directly to core-layer tables and columns, skipping the business-term/business-rule layer — "a consequence of a high degree of freedom and a poor level of governance." You cannot see which business rules exist for a field; rules smear across many objects. Checkers hanging off glossary terms would make requirements-to-checks traceable. (course day 5, transcript)
- **The red wall.** Coverage rises, apparent quality falls, everything goes red — and the cheapest way to move the number becomes deleting checkers. (course day 4, transcript)
- **Coverage-metric theatre.** Reporting checker coverage as the headline DQ number when it is "easy to hack," and auditing checker quality to fix it is "already overkill." (course day 4, slides p.143)
- **Boiling the ocean.** Per McKinsey up to 70% of cleansing effort is wasted; one large company burned hundreds of millions of dollars and 2+ years on an enterprise-wide cleansing/data-lake initiative that largely failed because nobody knew which data served which use cases. (course day 3, slides p.9)
- **Merging the two steward roles.** Give the business steward checker maintenance or documentation instead of incident review, and the role quietly dies. (course day 4, slides p.119-120)
- **Premature delegation.** Handing base coverage and incident generation to domains in the name of mesh: "it just won't start." (course day 4, transcript)
- **The 1x→10,000x chart as a business case.** "Frankly marketing, based on nothing" — mythology, usable only as a trust narrative. (course day 4, slides p.156)
- **Gate bypass.** A release gate defeated by "your release manager is on vacation — ship it anyway." (course day 2, transcript)
- **AI checker flood.** 160 marts in a day, then an incident flood, then an incident agent, then an eval-agent to judge whether the checkers are fake — a support-expensive system arriving faster than the process to run it. (course day 6, transcript)
- **DQ bureaucracy.** Building dashboards, policy and a council while skipping the four things that actually move quality. (course day 4, slides p.144)

## Questions to ask when designing a DQ program
The author's own diagnostic pair, put to the room verbatim (course day 4, slides p.160):
- **"Do you have DQM as a process? What does it actually consist of?"**
- **"Who participates in it, and who drives it?"**

Derived from the rest of the material, roughly in the order he works through them:
- Is the absence of built-out DQ a *current constraint* for the company, or just background noise? (course day 2, slides p.23)
- What share of your data have you declared critical, and by what logic — a factor rating, or the owner just picking? Both are legitimate; neither is not. (course day 1, transcript; course day 3, slides p.33)
- Which layers of the test pyramid do you actually have — and which are you deliberately fine without? (course day 4, slides p.157)
- Where is the boundary between the central DQ team and the domain teams, and does your tool assume the same boundary? "These are two different approaches to the tool." (course day 4, transcript)
- On a contract breach: stop the load, load and alert, or pause and alert? Is that written into the contract? (course day 4, transcript)
- What fluctuation range is normal versus an incident, and which business person has actually said so? (course day 4, transcript)
- What does one check cost you to run, and should that change how many you have? (course day 4, slides p.145)
- Can your coverage metric be moved by writing trivial checks? If yes, what do you report alongside it? (course day 4, slides p.143)
- Who finds your incidents first — you, or the business? (course day 4, transcript)
- Are checkers a precondition of certification, or an optional extra? (course day 4, transcript)
- Can anyone on your data team answer, in metric terms, whether your data quality is good and how good? (course day 4, slides p.99)
- Which of the four things "more important than DQ dashboards" do you already have? (course day 4, slides p.144)

## Links
- https://datamanagement.wiki/
