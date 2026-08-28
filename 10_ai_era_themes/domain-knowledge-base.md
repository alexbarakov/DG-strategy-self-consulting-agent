---
theme: Domain Knowledge Base
type: ai-era-theme
status: draft (child hexagons currently removed on the board — hub + panel only)
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681729697250"
related:
  - "[[context-governance]] — the governance process that keeps packs trustworthy"
  - "[[semantic-layer]] — layer 2 of the triad; the KB is layer 3 on top of it"
  - "[[enterprise-ontology]] — the relationship map a domain pack builds on"
  - "[[certified-core-layer]] — supplies row 2 of the AI-Ready Domain checklist"
---

# Domain Knowledge Base

**Tagline:** The agent answers from a curated domain pack, not from the model's memory. Layer three of the prerequisite triad, on top of the semantic layer and core data.

## What is it

A curated corpus of domain knowledge that grounds the agent: which metric to use and why, what the known traps are, where the boundaries of the domain lie. The semantic layer holds the formulas; the knowledge base holds the judgement around them.

It ships as a pack: a manifest, knowledge files — domain profile, glossary, key objects, FAQ — and an eval folder with a golden set. Everything machine-generated enters as needs_review and counts only after a human confirms it.

Filling ≠ trust ≠ effect: coverage can be gamed by weakening the gate, so coverage and false-accept are read only together, and the domain's value is measured by its AI-ready score, not by file count.

## Key terms

- **Knowledge pack** — manifest plus knowledge/ plus eval/; the versioned, deployable unit of domain knowledge.
- **Domain profile** — what the domain covers, who owns it, where to escalate, how fresh its knowledge must stay.
- **Few-shot** — a verified question-to-query pair; the densest way to transfer domain skill to an agent.
- **Trap** — a do-not-use-for case: legacy fields, migration breakpoints, deceptive column names.
- **Golden set** — reference questions with expected answers and a scoring rubric; run on every change of context or model.
- **Status model** — needs_review → confirmed → archived; master-system autosync counts as trusted by origin.
- **AI-ready score** — composite: roles assigned, healthy metrics share, consumption on certified objects.

## Numbers for arguing with optimists

- 25% → 80% — accuracy of a domain assistant before vs after the knowledge base is filled.
- ~61% — share of ad-hoc analytics requests automatable with SQL plus documentation, in a field study of 2 198 request threads.
- Score thresholds that worked: ≥50% of domain metrics healthy, ≥45% of dashboard views and ≥30% of mart hits landing on certified objects.
- 100% of machine-generated knowledge starts as needs_review — no exceptions, or the layer poisons itself.
- ~80% of a 10 000-term glossary captured by an AI prototype from public documents, against 9 months of manual work before — the reason the glossary row of the checklist is no longer the blocker it was. (course day 6, transcript, vendor guest)

## From the course (Data Governance Fundamentals, 6 days)

### The AI-Ready Domain checklist — the operational form of the pack

The course does not present the domain knowledge base as a technology. It presents it as a **checklist of six things a domain must grow so an agent answers correctly**, each row with a named owner and a named master system. That framing — prerequisite, not product — is the useful part. (course day 6, slides p.95)

| Row | What exactly is required | Master system | Owner |
|---|---|---|---|
| Domain boundary and owner | What falls into the domain's zone of responsibility, in 1–3 phrases; curator + BI partner by name; where to escalate data questions (chat, ticket, contact) | Confluence pages tagged `ai_analyst_domain` | Domain Owner (Head of Analytics) |
| Key metrics, certified marts, dashboards | Markup of the key / certified marts, metrics and dashboards | Data catalog | BI Partner (marts + dashboards), Metric Curator (metrics) |
| Meta per key object | Short description (1–3 phrases): what it computes, what it is used for. Limitations: period of applicability, migrations, **"do not use for…"** | Data catalog | BI Partner, Metric Curator |
| Typical "how do I…" scenarios | The user's question in the user's own wording ("How do I see revenue by CPx?") plus a short answer — which mart / metric / report to use, **what the catch is** — plus a link to a worked example | Confluence pages tagged `ai_analyst_domain` | BI Partner, Metric Curator |
| Links to adjacent domains | Briefly: for which question you go to which domain | Confluence pages tagged `ai_analyst_domain` | Domain Owner / BI Partner / Curator |
| Domain glossary | Glossary of the domain's terms | Confluence pages tagged `ai_analyst_domain` | Domain Owner / BI Partner / Curator |

- The two-master-system split is a design decision, not an accident: **narrative** knowledge (boundaries, how-to scenarios, adjacency, glossary) lives in tagged wiki pages; **object-level** knowledge (which objects are certified, per-object meta and limitations) lives in the data catalog. No third store is created for "the knowledge base" — it is assembled from the two systems that already exist and already have owners. (course day 6, slides p.95)
- Responsibility split that staffs the pack: **Domain Owner** (Head of Analytics) / **BI Partner** (marts + dashboards) / **Metric Curator** (metrics). The author maps the last two onto the classic pair — "these are two governance roles which, with a stretch, translate as technical data steward and business data steward." (course day 6, slides p.95; transcript)

### Why each row exists — the author's reasoning

- **Boundary + owner** is not documentation hygiene, it is retrieval personalization: "so that when the agent sees who is talking to it, it understands their domain and filters data objects accordingly. The person may not say they are from the real-estate domain, but the agent already knows — and will search far more precisely inside real estate." (course day 6, transcript)
- **Certified markup** is there because "we will navigate people to those objects first" — and because certification presupposes good descriptions, which is exactly what the agent needs anyway. Certification stopped being a bureaucratic ritual and became an AI prerequisite. (course day 6, transcript)
- **Per-object limitations** are the row a machine cannot write for you. Top catalog vendors' verdict, quoted approvingly: AI does field descriptions decently, but what it cannot produce is the tribal-knowledge caveat — "for this metric take this mart and these fields, but not for that one, because X is not accounted for." That sentence *is* the "do not use for…" column. (course day 4, transcript)
- **Typical scenarios** are few-shots by another name: "we build a base of typical questions and answers, usually from support-chat history — inputs and outputs the agent can lean on as examples. It raises answer accuracy very strongly. Literally a base of hints." (course day 6, transcript)
- **Adjacency links** exist because the failure mode of a domain-scoped agent is confident answering outside its scope; the cheap fix is an explicit "for X, ask domain Y" map. (course day 6, slides p.95)
- **Glossary** is needed here for a narrower reason than the classic enterprise-glossary case: "we need these glossaries to pull in the specifics *inside* the domains — everything the teams write in the wiki about their own methodology and the separate things you have to account for. Usually just large text docs, where a lot of useful stuff lives." (course day 6, transcript)

### Bottom-up assembly — the part that makes it feasible

- Domain glossaries are assembled **bottom-up** from tagged wiki pages where teams already describe their specifics and methodology. No company-wide glossary is needed first, and none exists: "we have no common glossary." (course day 6, transcript)
- This is a deliberate inversion of the course's own general advice, which files the business glossary under "reserved for the mature" — never enough resource, and physical/logical-level work matters more than the conceptual layer. The domain knowledge base is what lets you skip the enterprise glossary and still ground an agent. (course day 6, slides p.100-101; transcript)
- Where a metric store exists it partially covers the glossary job, and badly: "our metric store performs the function of a glossary, though it does it poorly — it does not contain entities like *item* or *client*, it is all about metrics, and it does not solve unification across BI and the warehouse." Domain packs fill that hole per domain rather than waiting for a corporate one. (course day 5, transcript)
- The organizational reason the domain route wins: a glossary "requires facilitating cross-domain work with business experts — much harder" than involving data teams and domain analysts, which is exactly what the domain pack asks for. (course day 5, slides p.28)

### Where the pack sits in the context stack

- Metadata layering the pack feeds into: **business context** (ontology, hierarchy) → **domain context** → **data context** (object quality, descriptions) → **user context**. The domain pack is the middle layer; the certified core layer supplies the data context; the ontology supplies the business context. (course day 6, slides p.94)
- Entry-ticket economics, stated without varnish: "the bigger the company and the more use cases you have to cover, the more expensive all of this gets." A domain pack is cheap for a small company and a programme for a large one. (course day 6, transcript)
- Two further prerequisites are explicitly labelled "more expensive" and kept outside the base checklist: **metric notes** (human explanations of metric anomalies) and **metric trees over key metrics** — needed because factor analysis, not value lookup, is the load-bearing use case. See [[context-governance]]. (course day 6, slides p.98; transcript)
- Adjacent enabler from the catalog side: **column-level lineage** is what lets an agent construct correct joins across marts — "without column-level lineage everything is rather sad" — with a base of proven successful joins as companion context. A domain pack without it will keep producing plausible but wrongly-joined answers. (course day 4, transcript)
- Knowledge graphs are re-entering the picture for the same reason: catalogs are moving toward "forming a domain knowledge base including relations — the knowledge graph and its links — to use as the basis for the context passed into agents." (course day 4, transcript)

### Filling the pack with machine help

- The historical blocker on ontologies and glossaries "was never technology — it was coordination of people and intellectual effort across many teams." GenAI removes the effort, not the coordination. (course day 5, transcript)
- Deployment posture the author endorses: generate cautiously — tag AI-generated metadata as **"requires review"**, or run a bot that pings the steward/owner to confirm. "The benefit outweighs the risks, but we don't want to fill everything without owner confirmation." (course day 4, transcript)
- Semi-automatic glossary-to-column mapping: put an agent on the certified marts to propose term↔column links — with the same unresolved verify-or-not dilemma attached. (course day 5, transcript)
- That dilemma is live and unresolved inside a large marketplace: one camp says re-checking auto-generated docs and mappings costs about as much as doing the mapping by hand; the other says "it doesn't make mistakes, especially with a second agent re-checking — shorten or extend the docs, but correcting isn't needed." Presented as a genuine governance question of the LLM era rather than a settled one. (course day 5, transcript)
- The anti-pattern to guard against while filling: the "burnt desert" — you pay for the tooling and get ghost towns of empty or generated-but-unverified descriptions; trust drops and the surface degrades into a search box. (course day 4, slides p.40, 46)

## Anti-patterns

- **Building a third store called "the knowledge base."** The checklist deliberately routes every row into either the tagged wiki space or the data catalog. A new repository means a new ownership problem. (course day 6, slides p.95)
- **Waiting for a company-wide glossary before starting domain packs.** It is filed under "reserved for the mature" for a reason; domain glossaries assemble bottom-up from what teams already wrote. (course day 6, transcript; slides p.100-101)
- **Letting a machine write the "do not use for…" rows.** Field descriptions, yes; tribal-knowledge caveats, no — that is the one thing AI cannot produce and the one thing that prevents confident wrong answers. (course day 4, transcript)
- **Filling the pack without a review gate.** Generated metadata creates "the feeling that you have everything"; untagged, unconfirmed content is worse than an empty row because it looks finished. (course day 4, transcript)
- **Writing how-to scenarios in your own wording rather than the user's.** The slide's example is a user sentence — "How do I see revenue by CPx?" — not a documentation heading. (course day 6, slides p.95)
- **A pack over an uncertified data layer.** Certification and good descriptions are prerequisites of the pack, not parallel workstreams. (course day 6, transcript)
- **Assuming the agent knows who is asking.** Without a domain boundary attached to the asker, retrieval is company-wide and precision collapses. (course day 6, transcript)

## Questions to ask

- Which of the six checklist rows does this domain actually have — and who is named on each? (course day 6, slides p.95)
- Where is each row mastered: the tagged wiki space or the catalog? If the answer is "a doc someone made", it is not in the pack. (course day 6, slides p.95)
- Does the agent know which domain the asker belongs to before it retrieves anything? (course day 6, transcript)
- Where do your few-shots come from? If the answer is not "support-chat history", you are inventing questions users never asked. (course day 6, transcript)
- For your top ten objects, is there a written "do not use for…" — written by a human? (course day 6, slides p.95; day 4, transcript)
- Do you have column-level lineage and a base of proven joins, or are you expecting the agent to guess the join? (course day 4, transcript)
- Which is cheaper for this domain right now: verifying the generated pack, or writing it by hand? Both answers are defensible; pick one deliberately. (course day 5, transcript)

## Что не покрыто этим источником

- **Pack format** — manifest, `knowledge/`, `eval/`, versioning and deployment as a unit: в материалах курса Data Governance Fundamentals не раскрыто; основной источник по теме — авторский курс BI+AI Strategy.
- **Golden set and eval mechanics** — reference questions, expected answers, scoring rubric, re-running on every context or model change: в материалах курса Data Governance Fundamentals не раскрыто; основной источник по теме — авторский курс BI+AI Strategy. Day 6 mentions an eval-agent only in the DQ-checker context, not for knowledge packs.
- **AI-ready score as a composite index** and the coverage / false-accept pairing: в материалах курса Data Governance Fundamentals не раскрыто; основной источник по теме — авторский курс BI+AI Strategy. The DG course stops at the qualitative checklist.
- **The formal status lifecycle** needs_review → confirmed → archived: only the "requires review" tag is DG-sourced (day 4, transcript); the full lifecycle comes from the BI+AI Strategy course.

## Sources

- Anthropic — skills as packaged domain knowledge lift agent accuracy from 21% to 95%+: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Author's course «Data Governance Fundamentals» (6 days), day 4, 5, 6 — slides and transcript.
- Author's course «BI+AI Strategy 2026», Domain Knowledge Base module; field notes: https://t.me/datanature
