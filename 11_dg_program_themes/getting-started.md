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
