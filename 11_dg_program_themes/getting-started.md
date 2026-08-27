---
theme: getting-started
type: dg-program-theme
frames:
  - "3458764611453525278" # Self-assessment test (need for a DG program)
  - "3458764611825830326" # Reasonable way to start DG (staged flowchart)
  - "3458764611802674401" # How to start: Common Sense DG + DG MVP flow
  - "3458764611814706547" # DG challenges: life without vs with DG
  - "3458764611453525315" # Section header: Data Governance of Common Sense
  - "3458764611453525294" # ROI of DG — Not Measurable elements
  - "3458764611453525298" # Healthcare DG business case (Jeff Fuller)
  - "3458764611453525322" # DG learning resources
---
# Getting Started with Data Governance

## What the board teaches
Do not start with a program — start by proving you need one. A 12-statement self-assessment (5+ relevant statements → a DG program is likely cost-effective) and a two-sided challenges canvas ("life without DG" starting barriers vs "life with DG" value barriers) frame the decision. The recommended path is evolutionary: every company already lives in *Natural DG* (informal, no driver); a team of 2-3 respected senior DWH/BI leads (2+ years tenure) then runs *Common Sense DG* — quick-win projects any team can do without budget (platform clean-up by usage stats, basic null/freshness DQ monitoring, access rules, git-driven core-model docs) — in parallel with a *DG MVP* on the most painful domain or key data object (e.g. customer). Sponsorship gates control scaling: minimum 1 of CDO/CTO/CFO/CEO to start the MVP, 2 of 4 plus the MVP's business domain owner to go to a full program; the MVP results are packaged into a case with a cost-benefit model, and Budget Denial is a normal outcome that loops back into Common Sense DG and an MVP restart. On the business-case side, the board acknowledges that much of DG ROI falls into a "Not Measurable" category (valuable but hard to monetize) and offers a full worked business-case example from healthcare (Divurgent) with a 3-phase plan and cost-benefit template.

## Key objects
- Self-assessment test: 12 unique pain statements (cross-functional reporting, multiple sources, PII protection, poor DQ eroding trust, third-party data, regulation, dataset discovery for analysts, consistency across apps, competitive/digital market, duplication and misinterpretation, storage cost, product improvement needs); threshold: 5 of 12
- Staged flow: Natural DG → Common Sense DG (team level) → DG MVP (most painful areas) → Land and expand with a DG program
- MVP DG team profile: 2-3 leads/seniors from DWH/BI, systemic mindset, 2+ years in the company
- Common Sense DG example projects: platform clean-up via usage statistics + monitoring; simple DQ monitoring (null checks, nightly updates); data access rules; git-driven documentation of the core data model
- DG MVP example projects: domain metrics tree and glossary; documentation by criticality; assigning owners/custodians/stewards; DQ checks + incident handling + quality measurement; data contracts with systems teams; "golden" layer of sources
- Sponsorship gates: C-level support 1/4 → 2/4; case packaging; cost-benefit model; Budget approval → DG office vs Budget denial → Common Sense DG + restart MVP
- Challenges canvas: 5 starting barriers (weak link to business goals, insufficient value drivers, no owner, opaque concepts, domain resistance) and 9 value barriers (rigid framing, DMBOK-copying, wrong data focus, stuck initiatives, hiding behind catalogs, ignored practitioners, unadopted approaches, no product mindset, anti-bureaucracy culture)
- ROI framing: "Not Measurable" ROI category; Cost Reduction / Extra Revenue Generation axes
- Healthcare business case (Jeff Fuller, Divurgent): DG definition, AI-readiness rationale, executive talking points, 10-section fill-in template, 3 phases (Foundation / Launch / Engagement), 1-3 FTE DG Office, start on existing tools before buying a catalog, illustrative cost-benefit (>50% less time locating data)
- Workshop templates for pains analysis and problems→solutions mapping exist — see [templates.md](../12_templates/templates.md)

## From the course (Data Governance Fundamentals, 6 days)

### Definitions that actually work
- "There are two big problems with data governance today: the first is data, the second is governance." — opening joke used to frame the whole course. (course day 1, slides p.36)
- Preferred definition (Villar & Kushner): DG is a cross-functional *program* of managing data as a corporate asset — for *critical* data, in service of company goals. "If it doesn't help the goals, maybe it isn't needed." (course day 1, slides p.40)
- DG vs data management: the auditor analogy — governance ensures management is done properly without directly executing it. Favorite task formulation: "increase the ratio of needed data to un-needed data." (course day 1, slides p.41-42)
- Skepticism on "data as an asset": no accounting standard recognizes data as a balance-sheet asset; the metaphor "doesn't really sell" to management — use it only in narrow monetization contexts. (course day 1, transcript)

### Do you need a program at all
- Program archetypes by (# data domains × # business processes): one domain / many processes = master data; many domains / one process = financial planning/reporting; many/many = corporate KPI system, DQ, enterprise data strategy. (course day 1, slides p.103)
- Honest pre-start question: "Is the ABSENCE of built-out DG a *current constraint* for the company?" A company can live 2-3 years just accumulating data chaos — chaos is a survivable state with a hidden cost. (course day 2, slides p.23; day 3, transcript)
- Cross-functionality is the trigger word: if domains work in isolated contours and never need each other's data, natural governance suffices; losses (and the DG case) appear only when cross-domain use starts. (course day 2, transcript)
- For a centralized org, "DG on your own hands" is legitimate: invent governance procedures inside the analytics/platform function — "the business will never care *how* you ensure the quality level it needs." (course day 1, transcript)

### Selling the start
- "Business buys solutions to problems it actually feels." Pains are concrete and emotional; drivers are where DG extracts savings or revenue — company-level pains recognized by top management matter most, ideally incidents directly linkable to DG. (course day 2, transcript)
- Going to business under the literal flag "Data Governance" fails in ~95% of cases — the word evokes "distant and secondary." Package it under something else; better to not even call it DG. (course day 2, transcript)

### Minimal viable governance
- Keep a registry (even in Excel) of your most important data marts, each with a named tech owner and business owner, wired with checkers and documentation, and watch that they "arrive intact every morning" — for many companies that is 80% of all the governance they actually need. (course day 3, transcript)
- Formalized DG = "you were given a budget"; "90% of projects never get that budget", so most companies run common-sense DG: cheap projects distributed across existing BI/platform teams, a light role model, automated checks, certification. (course day 5, transcript)
- Anti-pattern: a funded DG program inherits the burden of proving payback — in companies that scrutinize money hard, it may be strategically better NOT to form a dedicated DG team and instead hide governance work inside teams with a clearer raison d'etre. (course day 5, transcript)

## Frames on the board
- [Test to Determine the Need for a Data Governance Program](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525278)
- [Reasonable way to start Data Governance](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611825830326)
- [How to start: Common Sense DG + DG MVP flow](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611802674401)
- [DG challenges: life without vs life with Data Governance](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611814706547)
- [Data Governance of Common Sense (section header)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525315)
- [ROI of DG — Not Measurable elements](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525294)
- [Healthcare DG business case template (Jeff Fuller, Divurgent)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525298)
- [DG learning resources (blogs, communities, vendors)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525322)

## Links
- Learning resources (consume critically, marketing content warning): https://tdan.com/category/data-topics/data-governance-articles-blogs-education ; https://www.dataversity.net/category/data-topics/data-governance/data-governance-blogs/ ; https://datagovernance.com/blog-2/ ; https://datameshlearning.com/ ; https://www.dama.org/cpages/home ; https://datacrossroads.nl/free-resources/ ; https://datamanagement.wiki/ ; https://atlan.com/ ; https://www.precisely.com/category/datagovernance ; https://www.collibra.com/us/en/blog ; https://www.informatica.com/blogs.html
