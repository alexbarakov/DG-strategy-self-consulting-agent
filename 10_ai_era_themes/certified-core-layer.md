---
theme: Certified Core Layer
type: ai-era-theme
status: draft (child hexagons currently removed on the board — panel only)
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681730395308"
related:
  - "[[semantic-layer]] — stands on the certified core"
  - "[[bi-content-management]] — the content funnel that produces the certified layer"
  - "[[domain-knowledge-base]] — consumes the certified markup as one of its six checklist rows"
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
- 5 004 marts scored, 12 healthy — 0.2%. The health dashboard at the start of the programme; that is the real baseline behind any «we have a core layer» claim. (course day 3, slides p.115)
- Share of user queries with 2+ joins: 47% → 35% (2026) → 25% (2027). Share of analyst queries hitting core tables: 1% → 15% → 40%. (course day 3, slides p.114)
- 20% vs 80% — agent accuracy without vs with grounding in certified sources.
- Thousands of marts, a single-digit certified share — the default state of a mature multi-domain warehouse.
- What AI adds now: generated DQ checks and descriptions with human-approved thresholds — check 100% instead of a sample.

## From the course (Data Governance Fundamentals, 6 days)

### Why certification is the spine

- Author's core belief, stated as the course's spine: "Separating crap content from good content that is recommended for use is largely the key to solving many DG problems. Agent systems will demand exactly the same certification." (course day 1, transcript)
- Certification must run through the entire delivery chain, not one layer: certified marts → certified semantic-layer objects → certified dashboards/metrics → (soon) certified agents. "Trust sprawl happened inside the semantic layer too — many objects of low trust accumulated there and now need certification." (course day 5, transcript)
- DG budget defence in cost cuts runs through AI: "under all our agents there must be a core data layer, a semantic layer and certified reports — and certification can only be achieved communally" — AI-readiness of domains becomes the shield for DG budgets. (course day 3, transcript)
- Certification is also a DQ instrument in disguise: run custdev on what "data quality" means to the business and "very many will say that first of all they don't know which reports they use and which to trust" — plus that what they open doesn't arrive, doesn't refresh, or breaks with nobody responsible. All of that gets attributed to DQ in their heads. The badge is the consumer-facing surface of everything the DQ programme does underneath. (course day 3, transcript)

### The vision slide, verbatim in structure

- The project goal is one sentence with five checkmarks: create a layer of certified marts (the core layer) that is a trusted source for all consumers — **data ready on time / data can be trusted / data convenient to use / data usable by an AI assistant / resources spent efficiently**. Note that «usable by an AI assistant» is a first-class member of that list, not an appendix. (course day 3, slides p.112)
- Three beneficiaries, named separately so each can be sold to separately: **analysts** find provably accurate data faster, join less, get updates more reliably; the **company** saves on CPU and storage by capping object growth and raising reuse; **Gen-AI products** answer more accurately because the marts under the metrics and dashboards are healthier and their metadata better. (course day 3, slides p.112)
- Three declared outcomes: raise analytics-projects velocity; cut total cost — technical (CPU/RAM/storage) and human (search / ad-hoc / creation / support); raise the domain's readiness for AI analytics. (course day 3, slides p.112)
- "In two words, what we do": DWH and BI **together** carve out and mark the layer of trusted marts by key entities, build roadmaps and backlogs of improvements (to-be architecture, tasks), and assign responsibility for development and support, automating what can be automated. The joint DWH+BI framing is deliberate — neither function owns the layer alone. (course day 3, slides p.112)

### What the consumer actually gets

- Trust statuses visible in the catalog: **Candidate / Certified / Degraded**. Degraded = certified but currently failing health requirements — that is the fix queue, not a demotion. (course day 3, slides p.113, 120)
- Certified implies default guarantees: owner + contacts, freshness SLA, base DQ thresholds, lineage, change rules as a contract. In the author's words the object "is taken under platform warranty" — it gets an SLA and must comply on quality, on delivery time, and on how changes are introduced. (course day 3, transcript; slides p.113)
- **Reuse-first** is written into the design: new marts, dashboards and ad-hocs are built from Core, not from scratch. (course day 3, slides p.113)
- Badge design detail: blue Candidate (may be renamed Promoted), green Certified, red Degraded (may be renamed Deprecated) — three colours, no more. (course day 3, slides p.120)

### The target architecture the layer sits in

- Two flows drawn side by side. **New flow:** trusted BI content and services (metric store, dashboards, AI Analyst, SQL query, plus a ClickHouse dataset tier kept purely for dashboard performance) → semantic layer (metrics and data models as SQL+YAML) → **Core Data Layer**. **Current flow:** sandbox BI content over a sandbox layer — the user self-service zone. Both stand on the same base: a 6NF detail store plus clickstream. (course day 3, slides p.113)
- The core layer itself has two object types with explicit purposes on the slide: **Presentation datamarts** — "enriched wide tech datamarts exposed through views with consistent column naming, *for use in ad-hocs*"; **Tech datamarts, 3NF** — denormalizations of the 6NF detail store: fact tables, dimension tables, dictionaries, *for reuse in other datamarts*. The consistent column naming on the presentation tier is what makes wide marts safely joinable — and agent-readable. (course day 3, slides p.113)
- Honest self-assessment attached to the same picture: this is "a semi-target model — today most of the traffic from tools and applications goes *around* the semantic layer; the goal is to raise that share". (course day 5, transcript)

### Money and targets

- Operational goals with numbers on the slide: share of user queries with 2+ joins 47% → 35% (2026) → 25% (2027); share of analyst queries hitting core tables 1% → 15% → 40%; total mart count in the mart schema — deliberately left "tbd" rather than invented. (course day 3, slides p.114)
- The money case is a scheduled event, not a hope: **platform billing arrives in 2026** — marts become resources domains pay for, and the core layer is what cuts their cost of ownership. Business goal wording: cut total cost, technical (CPU/RAM/storage) and human (search / ad-hoc / creation / support of marts). (course day 3, slides p.114)
- The programme's key metric is **share of traffic** going to core marts, not the count of certified objects: "we need them to actually be used, and duplicates to gradually leave or be archived." (course day 3, transcript)
- Budget candour: "we are trying to find money for this — and the money is exactly here, beyond the operational metrics, because we are strict about money." (course day 3, transcript)

### Health scoring

- Principle: execute **binary, manageable assurance criteria** and watch the movement of **control metrics**. Four criteria, in the author's wording: **Ready on time** — the mart computes by the stated time, and fast; **Can be trusted** — data-contract coverage, no incidents; **Convenient to use** — you read the necessary minimum optimally, metadata filled; **Resource-efficient** — store only what is needed, use resources optimally. Architectural checks (storage structure, read patterns) sit inside the last two. (course day 3, slides p.115; transcript)
- Health score is deliberately distinct from a DQ score: DQ answers "is this column right", health answers "is this object fit to be relied on". (course day 6, transcript)
- Methodology humility worth quoting to your own team: "this is roughly the tenth version of the health-scoring methodology we have invented; we keep changing it — hopefully for the last time." (course day 3, transcript)

### Rollout mechanics

- Two per-domain tracks, chosen by how much central resource the domain gets. **Core Data Deep Dive:** a project team of domain BI + a platform data engineer audits the domain data model, analyses pains and processes, slices a backlog and a roadmap focused on business-value cases, picks the low-hanging fruit and drives it to effect; target one quarter, after which the data engineer leaves for the next domain and the BI developer finishes the block alone. **Core Data Preparation (light):** the domain BI partner — or the analytics team lead where there is no BI partner — validates the list of core candidates (usage signals plus manual judgement), runs them through health scoring, fixes what can be fixed unaided, analyses how well the current model reflects real analyst needs, and books resource for a future deep dive including migration. (course day 3, slides p.116; transcript)
- Quick win that makes the metric move early: pre-mark the objects that already qualify. "So the impact on our metric arrives faster." (course day 3, slides p.116; transcript)
- Build per horizontal domain first (marketing was first), with the explicit contract that vertical teams downstream reuse those data products instead of rebuilding them; L1/L2 marts by criticality. (course day 5, transcript)
- Sequencing lesson: certify **marts first, then reports, then metrics** — even though reports feel closer to the business and are the natural place a BI leader starts. (course day 3, transcript)
- Naming warning: the word "certification" itself "smells of bureaucracy" to some audiences — consider another term before you brand the programme with it. (course day 3, transcript)

### Making the status impossible to miss

- Design goal stated bluntly: the layer must "shout at you from every interface" — the catalog card, search results, and every surface where a person is about to create something new, where it should first ask "maybe use this mart instead of building another one." The author flags those nudge scenarios as still unbuilt: "we still have to work those through." (course day 3, transcript)
- Single source of truth for statuses: the catalog carries **Core / Certified / Degraded** badges in search and on the mart card, with status filtering and a click-through to the detail of *why* the status is what it is; the BI tool and the metric store show **the same status** on dashboards and metrics, so trust is one process rather than three. (course day 3, slides p.117)
- Semantic-layer objects are **certified by default** — one version of truth by construction rather than by review. (course day 3, slides p.117)
- Data contracts are folded into the health score, not run beside it: coverage of every field, plus subscription to upstream contracts, so a break arrives as a signal rather than as a surprise. (course day 3, slides p.117)
- Promotion surfaces that vendors already ship and are worth copying: the certification badge in the **dataset picker** at the moment a report is created, and certification as a **search filter** (`certificationStatus:certified`) rather than only a label on a card. (course day 3, slides p.121)

### Catalog badge best practices

- Few public badges (Promoted / Certified / Deprecated, or just Certified / Deprecated) so the user's cost of choosing a source stays minimal. (course day 3, slides p.119)
- The right to certify is strictly limited; candidates are usually marked by owners, but certification itself is not self-service. (course day 3, slides p.119)
- Certification must be continuously challenged and revoked on major changes, "otherwise the badge loses its meaning." (course day 3, slides p.119)
- Deprecation ships with a plan: reason, deadline, consumer notification. (course day 3, slides p.119)
- The catalog is the hub of the data portal: status and contract changes emit **events** consumed by other services. (course day 3, slides p.119)
- Separation of concerns: the catalog owns trusted-data signals and object search; **domain cabinets** own operational management — preparation, review, fixes. The public status lives in the catalog; the work lives in the domain. (course day 3, slides p.119)

### Lessons and war stories

- Staffing trap: in ~80% of companies the core layer will be built by data engineers, who "by nature are not product people" — expect product-ownership problems and plan for them. The author applies the diagnosis to his own mart team without flinching. (course day 3, transcript)
- Participant counterpoint worth keeping: "a BI developer differs from a BI developer" — how far a BI person can carry the core layer alone depends on the toolset; sometimes they can act as architect, sometimes not. (course day 3, transcript)
- Trust base at a large marketplace: over a year the certified layer was marked across reports, datamarts and metrics, with health scoring underpinned by processes, roles and monitoring — "we have passed the point of no return." Done **without a DG team**, with governance distributed across teams under named drivers and shared goals. (course day 6, transcript)
- Peer scorecard from a big-tech ride-hailing player, presented as a cautionary artefact: a dashboard of domain-data-partner metrics — share of certified objects, share of traffic reaching certified objects that meet requirements, % legacy objects, description quality — "which nobody looked at." Building the scorecard is the easy half. (course day 6, transcript)
- Data deletion is a governance project of its own: "deleting data sounds easy, but in any big platform it's several circles of hell" — owners are unreachable or don't themselves know whether the data can go; it needs auto-certification, archiving logic and bots that walk around asking. One big-tech player deleted enough to save 20% of a 4PB Hadoop cluster. (course day 6, transcript; slides p.34)
- Minimal viable version of all of the above, for a company that will never fund a programme: keep a registry — Excel is fine — of your most important marts, each with a named technical and business owner, wired with checkers and documentation, and watch that they "arrive intact every morning." For many companies that is 80% of the governance they actually need. (course day 3, transcript)

## Anti-patterns

- **Counting certified objects instead of traffic to them.** The badge is not the outcome; the share of consumption landing on guaranteed objects is. (course day 3, transcript)
- **Certifying reports before marts** because reports feel closer to the business. The report inherits the mart's trust, not the other way round. (course day 3, transcript)
- **Letting the badge age.** No re-challenge, no revocation on major change → the badge stops carrying information and users go back to asking a colleague. (course day 3, slides p.119)
- **Deprecating without a plan.** No reason, no deadline, no consumer notification turns deprecation into a silent outage. (course day 3, slides p.119)
- **Badge inflation.** Every extra public status raises the user's cost of choosing a source; three is already generous. (course day 3, slides p.119)
- **Running the operational process inside the catalog.** Preparation, review and fixes belong in domain cabinets; the catalog shows public status. Mixing them makes the catalog a workflow tool it was never designed to be. (course day 3, slides p.119)
- **Handing the layer to data engineers with no product owner.** The most likely staffing outcome and the most likely failure mode. (course day 3, transcript)
- **Branding the programme "certification" to an audience allergic to bureaucracy.** The word can cost you the buy-in before the content is heard. (course day 3, transcript)
- **A partner scorecard nobody opens.** Metrics without a ritual that forces people to look at them are decoration. (course day 6, transcript)
- **Leaving the reuse nudge unbuilt.** If nothing intercepts the person at the moment they create a new mart, reuse stays an aspiration. (course day 3, transcript)

## Questions to ask

- What share of today's traffic lands on objects you would personally be willing to guarantee? (course day 3, transcript)
- If a mart is Certified, who carries the warranty, and what exactly happens when it breaks — SLA, quality, change rules? (course day 3, transcript; slides p.113)
- Who will actually build this layer, and are they product people? If not, who supplies the product ownership? (course day 3, transcript)
- At the moment someone creates a new mart, does anything suggest an existing one? (course day 3, transcript)
- How many public badges does your catalog show, and can a user tell them apart in one second? (course day 3, slides p.119)
- When was a certification last revoked? If never, the badge is decorative. (course day 3, slides p.119)
- Does the same status appear on the mart, the dashboard and the metric — or does each tool have its own idea of trust? (course day 3, slides p.117)
- Are you certifying marts before reports, or the reverse because reports are closer to the customer? (course day 3, transcript)
- When domains start paying for their marts, does your core layer lower their bill or raise it? (course day 3, slides p.114)
- What is your health baseline today, honestly counted — total objects vs objects passing all criteria? (course day 3, slides p.115)

## Sources

- Anthropic — a canonical table alone saves nothing: near-copies get deleted, and data code lives in one governed repo: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Vendor certification/endorsement references cited on the course slides: Microsoft Fabric endorsement, Looker content certification, DataHub dataset entity, AWS DataZone publishing (course day 3, slides p.119).
- Author's course «Data Governance Fundamentals» (6 days), day 1, 3, 5, 6 — slides and transcript.
- Author's course «BI+AI Strategy 2026», core layer module; field notes: https://t.me/datanature (post of 21 Mar 2026)
