---
theme: data-catalog
type: dg-program-theme
frames:
  - "3458764611453525320" # Evolution of Data Catalog Idea (1.0 -> 3.0)
  - "3458764611453525318" # Section header: Data Catalog Problems
  - "3458764612004792008" # Feature tiering (primary/secondary/tertiary)
  - "3458764612004885437" # Benefits vs costs
  - "3458764612004884958" # Complex questions vendors can't answer
  - "3458764612004792381" # Top challenges slide
  - "3458764611453561776" # Tool selection criteria stickies
  - "3458764611453561777" # Discussion prompt: primary value
  - "3458764611453561778" # Discussion prompt: top challenges
  - "3458764611453561780" # Template: catalog implementation requirements
---
# Data Catalog

## What the board teaches
The catalog is treated as the flagship — and most over-sold — DG tool. One track traces the idea's evolution: three generations of catalogs, five driving trends (modern data stack, diverse data teams, new decentralized vision for governance, metadata lake, active metadata platforms) converging into "Data Catalog 3.0" = active metadata + metadata lake + community-led governance + AI-driven features and programmable bots. The critical track is blunter: catalogs "have become cluttered with features in search of additional value", and their benefits are often lower than creation-plus-maintenance costs — so either reduce investment, increase value, or both, by identifying which specific value drivers matter for *you* (faster data discovery = better TTM, cross-utilization of certified objects, faster analyst onboarding). The board tiers catalog capabilities into primary/secondary/tertiary features, lists the recurring implementation challenges (business users repelled by complexity, stewards not engaged, stale descriptions, trust erosion, hard-to-articulate value), poses six "complex questions vendors have no clear answers to", and packages all of it into a five-block brainstorming template with a phased rollout plan (pilot group → MVP for data power users → product release for business users).

## Key objects
- Catalog evolution: 3 generations; 5 trends; Data Catalog 3.0 node → active metadata approach (emphasized), metadata lake, decentralized community-led governance, AI-driven features, 3rd-gen programmable bots (Slack-integrated column descriptions, risk reduction)
- Primary features: source connectors; business glossary; metadata enrichment/storage and documentation; report catalog; API; bulk labeling/classification; column-level lineage; keyword/NL search with recommendations; integrated ownership/stewardship role model
- Secondary features: DQ status by object (DQ tool integration); automated PII/PD identification; annotations and certification endorsement; customization; data sharing / access request workflow; DG adoption reporting
- Tertiary features: collaboration (chat, comment, rate); metadata generation automation; impersonation/user settings; alerting and dependency triggers; approval flow for changes; IDE / SQL-Python editor
- Primary value statements: reduced time to find and understand data = improved TTM; cross-utilization of (certified) objects; faster onboarding; cleaner landscape; faster impact analysis; PII scanned and access audited; stewardship made visible; data culture growth
- Top challenges: too complex for business users; can't engage business stewards or data professionals; insufficient/outdated metadata; lack of trust; Golden Path fragmentation; glossary as separate hard problem; expensive; budget justification; value articulation
- Six vendor-proof questions: involve business or not; lineage — who actually needs it; report catalog vs analytical portal duplication; barren field descriptions and AI-generated ones; how to measure search-time savings without time tracking; is your maturity sufficient at all
- Tool selection criteria: core features fit, community/popularity, tech stack, low TCO, sizing, simple UI, architecture complexity, low initial investment, open system
- Implementation sequence: domain structure + metadata integration → critical-layer logic → lineage (DWH, key ETL) → limited metadata load → BI layer → ownership model → MVP to production → glossary terms → certification → launch for data pros → ML classification/sharing → second-priority lineage → adoption CustDev → launch for business
- Full workshop template — see [templates.md](../12_templates/templates.md)

## From the course (Data Governance Fundamentals, 6 days)

### Economics and the buy trigger
- The buy trigger is measurable: there is a point where cumulative power-user efficiency loss exceeds the cost of a catalog — track Time to Value (project delivery date minus committed date) and detect its increase via experiments. (course day 2, slides p.35; course day 4, slides p.27)
- Real number: at a large tech company, search-and-understanding losses attributable to the catalog use case measured ~7M RUB/month — "not that much" at that scale; expect your numbers to be "average, not very sexy" because you multiply minutes by headcount. (course day 4, transcript)
- Benchmark: an ad-hoc's data communication (find marts, find people, get caveats) averages ~3-4 hours; with a certified, documented catalog + assistant the target is ~15 minutes. Works as a business case from ~100+ analysts. (course day 2, transcript)
- Pure "analyst efficiency" numbers are usually NOT enough to defend a catalog budget in big tech — hide the catalog under other initiatives (AI enablement, core layer, certification program). (course day 2, transcript)
- Vendor ROI math to steal but discount: Collibra claims 23% analyst / 26% steward productivity; Forrester TEI for Alation $3.8M benefits vs $813K costs. "The evaluation logic is worth copying" but realistically expect 5-7% provable — and saved time doesn't convert to output: "people just go drink coffee more often." (course day 4, slides p.80-86; transcript — marketing numbers, use critically)

### Build vs buy
- "For 90% of companies the boxed solution is optimal." The open-source trap: a catalog has "the illusion of a very simple product" to data engineers, but success hides heavy UX investment — you can wire up DataHub and get an ugly catalog that stores metadata but never becomes the starting point of data work. (course day 4, transcript)
- Open-source catalogs are doomed to be abandoned half-finished because competing initiatives always win the engineers; even funded catalog projects rarely justify a permanent team, so every catalog shows a "fading trend." (course day 2, transcript)
- "All available vendor comparisons are corrupt" — made by vendors with dishonestly picked criteria. (course day 4, slides p.29)
- RU pricing reality: base box with ~2 connectors, each extra connector ~1.5-2M RUB, per-steward licenses; tens of millions total, over 100M RUB with implementation. Vendor maturity test: do they bring methodology (glossary process, card templates) or just a bare box. (course day 4, transcript)
- Confluence-as-catalog fails on six counts (no sync, certification, lineage, links, checks, search) — but if all data people sit in 1-2 tight central teams, a plain wiki may genuinely beat a catalog on cost. (course day 4, slides p.31; transcript)

### Filling metadata — what works
- A large fintech: "no description — no prod deploy" gate; table-description quality grew 49%→86% in a year across ~7000 tables. Softener: pair the hard gate with an AI "generate description" button so it doesn't feel like friction. (course day 4, slides p.48; transcript)
- Anti-pattern "burnt desert": paying for a catalog and getting ghost towns of empty descriptions; trust drops and the tool degrades to a mere search box. (course day 4, slides p.40, 46)
- Don't boil the ocean: curate the top 20% node objects (most queried / used in most-viewed reports); maximize automated filling, algorithmically pre-fill domain/stewards/tags, inherit descriptions up the lineage from contracts, enter docs in the flow of work via CI/CD gate. (course day 4, slides p.47)
- The catalog, not Excel, must be the master system for domains and roles — with alerts on re-assignment, or people wash out silently: "we discovered nobody had been tending a domain for half a year." (course day 3, transcript)
- Typical starting picture to show sponsors (Azure Purview audit): only 4-45% of assets had owners assigned, ~46-74% lacked classifications. (course day 3, slides p.24)

### Product metrics and audience
- Product metrics: WAU (not DAU/MAU — natural usage frequency is weekly), target penetration 80% of target persona; CSAT out-of-band every 3-6 months; metadata completeness per object tier; metadata age — after ~1 year mark descriptions stale and auto-task domain roles to re-review. (course day 4, slides p.53, 86)
- "Data catalogs are not for casual users — that's a fact"; a report catalog inside the data catalog doesn't work for business either. Target model: data catalog for data-product teams + data marketplace/portal for consumers. (course day 4, slides p.51; transcript)
- Lineage skepticism: "the phone-a-friend option is more reliable" than a hairball dependency graph — check your logs, you may find nobody uses it. Invest only against concrete jobs: incident impact analysis and pipeline/critical-path optimization. (course day 4, slides p.57; transcript)
- A catalog becomes a DG tool only when the steward has an equipped workplace in it: a task inbox for their domain, policies to approve, DQ checks to review, documentation to fill, access rights to re-review. (course day 1, transcript)
- Security as ally: bake infosec use cases (PII classification, access audit, sensitive-data scanning) into the catalog early — "solve their task and they'll meet you halfway on everything else." Extreme constraint to design for: strictest bank infosec allows metadata only — no samples, no profiling. (course day 4, transcript)

### RU big-tech benchmark
- Peer survey of large tech companies (see `dg-kitchen-research.md` for the full board): one bought a commercial catalog (open push API was decisive) and implemented it in under 6 months with 3 part-time people; one tested an open-source catalog and dropped it (docs live in the wiki and become tech debt); two run their own products; one custom build on Atlas has owners on only 30% of objects; another rejected vendor lock — custom catalog, MVP in one quarter with 3 engineers, growing to a team of 10 in year two. (course day 4, slides p.87)

## Frames on the board
- [Evolution of Data Catalog Idea](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525320)
- [Data Catalog Problems (section header)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525318)
- [Data catalog features tiering](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764612004792008)
- [Data catalog: benefits vs costs](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764612004885437)
- [Complex data-catalog questions vendors can't answer](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764612004884958)
- [Top Challenges Encountered in Developing a Data Catalog](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764612004792381)
- [Tool selection criteria (sticky set)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561776)
- [Discussion prompt: primary value of a data catalog](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561777)
- [Discussion prompt: top challenges in developing a data catalog](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561778)
- [Template — Brainstorming on Data Catalog Implementation Requirements](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453561780)

## Links
none
