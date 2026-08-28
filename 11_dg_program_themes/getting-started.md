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
Do not start with a program — start by proving you need one. A 12-statement self-assessment (5+ relevant statements → a program is likely cost-effective) and a two-sided challenges canvas ("life without DG" starting barriers vs "life with DG" value barriers) frame the decision. The path is evolutionary: every company already lives in *Natural DG*; a team of 2-3 respected senior DWH/BI leads (2+ years tenure) then runs *Common Sense DG* — quick wins any team can do without budget — in parallel with a *DG MVP* on the most painful domain or key data object. Sponsorship gates control scaling: 1 of CDO/CTO/CFO/CEO to start the MVP, 2 of 4 plus the MVP's business domain owner to go to a program; MVP results are packaged into a case with a cost-benefit model, and Budget Denial is a normal outcome looping back into Common Sense DG. The board also admits much of DG ROI is "Not Measurable", and ships a worked healthcare business case (Divurgent) with a 3-phase plan and cost-benefit template.

## Key objects
- Self-assessment test: 12 pain statements (cross-functional reporting, multiple sources, PII, poor DQ eroding trust, third-party data, regulation, dataset discovery, consistency across apps, competitive digital market, duplication, storage cost, data-dependent strategic projects); threshold 5 of 12
- Staged flow: Natural DG → Common Sense DG (team level) → DG MVP (most painful areas) → Land and expand
- MVP DG team profile: 2-3 leads/seniors from DWH/BI, systemic mindset, 2+ years in the company
- Common Sense DG projects: platform clean-up via usage statistics; simple DQ monitoring; data access rules; git-driven core-model documentation
- DG MVP projects: domain metric tree and glossary; documentation by criticality; owners/custodians/stewards; DQ checks + incident handling; data contracts with systems teams; "golden" source layer
- Sponsorship gates: 1/4 → 2/4 C-level; case packaging; cost-benefit model; approval → DG office vs denial → Common Sense DG + MVP restart
- Challenges canvas: 5 starting barriers (weak link to business goals, insufficient value drivers, no owner, opaque concepts, domain resistance); 9 value barriers (rigid framing, DMBOK-copying, wrong data focus, stuck initiatives, hiding behind catalogs, ignored practitioners, no product mindset, anti-bureaucracy culture)
- ROI framing: "Not Measurable" category; Cost Reduction / Extra Revenue axes
- Healthcare case (Jeff Fuller, Divurgent): AI-readiness rationale, executive talking points, 10-section template, 3 phases, 1-3 FTE DG Office, start on existing tools before buying a catalog
- Workshop templates for pains analysis and problems→solutions mapping — see [templates.md](../12_templates/templates.md)

## From the course (Data Governance Fundamentals, 6 days)

### Definitions that actually work
- "There are two big problems with data governance today: the first is data, the second is governance." (course day 1, slides p.36)
- Definition of choice (Villar & Kushner): a cross-functional *program* for *critical* data in service of company goals — "if it doesn't help the goals, maybe it isn't needed." (course day 1, slides p.40-42)
- The deflationary version to carry through the whole start: "DG is just an organizational overlay and tooling that focuses and coordinates resources so the work gets done and survives — instead of dangling forever in individual teams' roadmaps." (course day 2, slides p.65)

### Do you need a program at all
- The pre-start question gets its own slide: "Is the ABSENCE of built-out DG a *current constraint* for the company? Maybe more pressing problems are unsolved, or the chaos just isn't big enough to hurt." (course day 2, slides p.23)
- Three answers, not two: "not at all" (no maturity, no drivers), "partially", "full-scale" — with archetypes by (# domains × # processes): one/many = master data, many/one = financial reporting, many/many = corporate KPI system, DQ, enterprise data strategy. (course day 1, slides p.103)
- Chaos is survivable with a hidden cost — 2-3 years of accumulation and the critical things still ship. "If the business model doesn't depend on data, DG will be hard both to justify and to defend in budget cuts." (course day 3, transcript)
- Cross-functionality is the trigger word: isolated domains that never need each other's data need no program. And for a centralized org, "DG on your own hands" is a mature answer, not a compromise — "the business will never care *how* you ensure the quality level it needs." (course day 2, transcript; day 1, transcript)

### Going to the business — and what to call it instead
- "Business buys solutions to problems it actually feels" — so hunt company-level pains recognized by top management, ideally incidents linkable directly to DG. But going in under the literal flag "Data Governance" fails "in ninety-five percent of cases — business simply doesn't want to understand what DG is." So: "better not to call it DG at all." (course day 2, slides p.11-12; transcript)
- Stated as strategy on the success-factor slide: "It is useless to explain DG to the business and wait for enthusiastic support. Business will support you, but will never postpone its own tasks for DG tickets. **DG is a thing data/analytics leaders must arrive at themselves.**" Corollary: start endogenously on platform resource — "the business will never understand the full scope of the problem you are solving." (course day 6, slides p.104; transcript)
- What works instead: attach DG under an initiative that already has money; today's strongest disguise is AI — "for the AI model to work you need to feed it quality data — surprise." Public example: SOFTSWISS ran "DG as a service unblocking business initiatives" — 2 FTE, one quarter of investigation, then a breakdown of month-end closing showing 2-3 excess workdays × 11 finance employees and invoice deltas from 100€ to >100k€. (course day 2, transcript; slides p.41-43)

### Sponsorship reality and the gates
- Two approval scenarios, and most starts are the first: no business case, built on unverified drivers ("bad data", regulation, "better decision-making"; typical trigger: the CEO tells the CIO to "look into DG"); or a case exists and you focus on the most obvious business-tied driver. Board gates: 1 of CDO/CTO/CFO/CEO for the MVP, 2 of 4 plus the MVP domain's business owner to scale. (course day 2, slides p.51, p.64)
- But sponsorship is deliberately *not* in the common-sense minimum set: "some things can be done on the back of the sponsorship of *other* projects. A separate DG sponsor becomes necessary later, when you need committees and big teams." (course day 6, transcript)
- The leader is himself a gate: he "must be an authoritative old-timer. You can hire from the market, but then you wait until he becomes one — nobody lets a newcomer seriously change their processes." In tech the CDO role usually doesn't exist; where it does, sponsorship is markedly easier (hh: DG manager under a CDO who is CEO-1). (course day 6, slides p.104; day 2, slides p.54)

### Common-sense DG is the default, not the fallback
- The research finding that reframes everything: "Most leading companies live in chaos while doing isolated sensible things — 'common sense DG'. They live and they don't break." From 20+ tech-company interviews. (course day 2, slides p.53; day 6, slides p.99)
- Formalized DG is defined financially: "For me it means you were given a budget — a DG manager and some people, maybe steward roles in domains, plus budget for a catalog, DQ, a portal. The second option: you weren't given a budget and you still have to solve the problems." Then: "ninety percent of projects never get that budget." The trade-off is admitted — common-sense DG "will most likely be *less* effective, less systematic, slower. But it solves part of the problems." (course day 5, transcript)
- Concretely: "standardization of data-lifecycle operations (Data/BIOps) + basic DQ checks and tooling + DWH/BI metrics reporting", delivered by existing teams. The fuller canvas adds domains and criticality, domain roles, cleanup of reports and marts, contracts and monitoring, certification, catalog/portal, metric tree. (course day 6, slides p.102; day 2, slides p.69)
- Minimal viable governance, the 80% version: "keep, somewhere — a registry, a catalog, or just Excel — the marts you consider most significant. Put a responsible techie and a responsible business person on each. Cover them with checkers and documentation, and watch that they arrive intact every morning. For many companies that is eighty percent of the governance actually required." DQ floor: nulls, freshness, completeness. "That may already be enough." (course day 3, transcript; day 2, transcript)

### The MVP and what a good first project looks like
- What it is for: "essentially a proof for management that your concept — roles, tools, initiatives — makes sense." Run it even when approval is easy: it "lets you knock ideas against reality, gives a base of concrete themes for scaling, and accelerates the arrival of value." Scope by criticality of the *business* domain; exit criteria are 2 of 4 packaged outcomes, a C-level sponsor and interest from other domain owners. (course day 2, transcript; day 6, slides p.104; day 1, slides p.118)
- The worked first project: dashboard certification shipped in 3 months. "People see that we did something and it works — on metrics and purely emotionally." A subbotnik followed immediately; both bought licence for more expensive initiatives. Sequencing lesson: certify marts first, then reports, then metrics. (course day 6, transcript; day 3, transcript)
- Stage-colouring for the first pass. **Gorgeous minimum**: domain model and owners; documentation by criticality; certification of metrics, marts, dashboards; metric tree; Data/BIOps standardization; DQ checkers; incident management. **Reasonable addition**: core/golden layer, PII classification, data contracts. **Reserved for the mature**: semantic layer and business glossary — the glossary because "there is never resource for it, and it is not a starting point; when you get to it, it's a nice suit." (course day 6, slides p.100-101; transcript)

### The subbotnik: a cleanup event as a habit machine
- The mechanic, verbatim: "We run a *subbotnik* — we announce an event, 'let's tidy up our reports and data'. The business swallows this well, because they always have a background feeling of disorder. In each large domain we designate someone responsible, run it for a month, reward everyone involved. And then it turns out that during the subbotnik they were doing exactly what a data steward does — they archived, they certified, they documented." (course day 2, transcript)
- Then the ratchet: "that was good, let's repeat periodically" → "why repeat, let's just do it monthly." That is how the BI-partner programme was bootstrapped; bots now replace subbotniks. Real format: 3 weeks light, ~10 hours per BI developer; a June run processed 36.6% of low-use objects (299/817) and certified 97. But the point is not the cleanup: "**the goal is not to do everything — the goal is to create a habit.**" (course day 2, transcript; day 3, slides p.104-107, 109)

### The business case: losses vs cost of prevention
- The framing he trusts, credited to Alfa-Bank's DQ practice (Andrey Zavarzin, 2011): "Quality is free — what's expensive is poor-quality information." And the textbook optimum curve is fiction: "we never managed to see a single such 'beautiful' curve of losses and costs built from several points." (course day 1, slides p.44-45)
- Top managers look at exactly two numbers: an agreed estimate of possible losses, and the cost of preventing them. "A positive decision is always taken when the *minimal* losses exceed the *maximal* costs." Prove that one point and you gain a reserve of trust and authority. (course day 1, slides p.45)
- Bottom-up assembly: map use cases onto the value-adding process flows, score impact × feasibility, keep at most 20-30. The counter-intuitive strength of the pile: when ~20 cases each individually "doable without DG" accumulate, together they prove a systemic problem. Only the *direct* economy — infrastructure saved by deleting redundant marts — is fully defensible. (course day 2, slides p.47-49; transcript)

### The honest ROI conversation
- Financial ROI of data quality is nearly unmeasurable: "it will almost never be the sexy number for which you'd be handed a real budget." Only three legitimate sources — revenue growth via business initiatives, cost savings, regulator-risk mitigation; "operational efficiency" and "innovation" are "air". (course day 6, transcript; slides p.4-5)
- The question that kills weak cases: "they ask — what share of this are you ready to save *provably*, over a year, two, three? And you most likely don't know. You will have to promise something. And if it doesn't come true, you take a defeat in management's eyes — or in the end, get fired. I am in that situation right now." He discloses his own figure in the course as a warning — a monthly effect that looked very small against the scale of his company. The number is withheld here; the warning is what travels. (course day 6, transcript)
- Saved time is not saved money: expect ~5-7% of the claimed effect to be provable — "saved time doesn't convert into output; people just go drink coffee more often." So carry the conversation on operational metrics, above all "days without incidents in critical reporting". Business often doesn't ask for money at all: "just rid me of this pain, make it not every day." (course day 4, transcript; day 6, transcript)

### When there is no budget (which is most of the time)
- The inversion most people miss: "once you have a funded DG program, you inherit the burden of proving payback. If your company scrutinizes money closely, it may be better *not* to form a separate DG team. Sometimes companies strategically choose to hide this work inside teams that have a clearer basis for their existence." (course day 5, transcript)
- Ownership without headcount: 0.2-0.3 FTE per person across teams; centres of expertise form naturally because nobody can own everything. "But someone must be the visionary coordinating the pieces, or the fragments never converge." Funding via a "platform tax" — each domain commits a % of existing capacity — works ~70% of the time at his company. (course day 5, transcript; day 2, transcript)
- His name for the mode: "invisible / non-invasive DG" — chaining initiatives so they pull each other. "The core layer pulls data checks, checks pull the catalog, domains pull roles, roles pull the need for domains. Which is much slower than if I had a focused resource." Expect no single program document: "documentation exists per-component, not per-program — and that's fine." (course day 6, transcript; day 5, transcript)
- Survival when cuts come runs through AI: there is no dedicated DG FTE to cut, and "under all our agents there must be a core data layer, a semantic layer and certified reports — and certification can only be achieved communally." Contrast: a large fintech recently cut its entire DG team. (course day 3, transcript; day 2, transcript)

## Maturity signals — which starting mode you are in
Triage questions, not a score. From the diagnostic slides and the 20+ company interview research.

1. **Is data a constraint right now?** If critical work still gets done and no C-level person names a data incident, you are in survivable chaos — a program will neither be funded nor defended. (course day 3, transcript; day 2, slides p.23)
2. **Cross-domain traffic.** Isolated contours need no program; hence the test opens with "multiple sources needing unified access" and "cross-functional analytical reporting". (course day 2, transcript; slides p.24)
3. **The 5-of-12 threshold.** 5+ → "most likely a DG program will be useful and will pay for itself." Below → stay in common sense. (course day 2, slides p.24)
4. **Regulation × complexity.** McKinsey's 2×2: regulation raises the *minimum* bar; complexity grows with business variety, speed of core-data change and — counter-intuitively — *low* automation maturity. (course day 1, slides p.104)
5. **The tearing point.** "Without a dedicated DG team, DWH/Data Platform Lead / Head of BI will take part of the initiatives in their own zone and achieve results — this happens in small tech companies and startups. At platform scale this governance *tears*: DWH/BI leads lack the authority, the interest and the resource to assemble the whole puzzle. That is the moment to exhale, form a DG project team and start an MVP. Or not start, if the drivers haven't reached critical mass." (course day 2, slides p.66; day 6, slides p.102)
6. **Catalog U-curve.** Time-to-value follows a U-curve over data-team size; there is a measurable point where power-user efficiency loss exceeds the cost of a catalog. Detect the *increase*, then start — realistically 100+ analysts. (course day 2, slides p.35)
7. **Where the industry sits.** Eckerson/RateMyData: average maturity 2.88/5.0 ("Initiating"); only 2% of programs deliver high business value, 22% none; top challenge is lack of stewards (54%). (course day 6, slides p.40-43)
8. **Peer archetypes.** Bottom-up on platform-head will, no CDO (a ride-hailing big-tech). No calm period because the org re-transforms quarterly (a large marketplace). Culture that rejects imposed rules and roles (a large fintech). Top-down request on DQ, InfoSec as locomotive (a social platform). Justified through metric discrepancies (hh). Find the one you resemble before designing anything. (course day 2, slides p.54; day 6, slides p.107)
9. **Maturity models are motivation machines, not diagnoses.** They work when a company appropriates one and embeds per-domain scores into top-management yearly goals. Best open model per the author: the UK Government Data Maturity Framework. (course day 6, slides p.44-45; transcript)
10. **Start by deleting.** On any maturity or goals canvas the first move is subtractive: "your maturity starts with removing what doesn't apply to you." (course day 2, slides p.57; transcript)

## Anti-patterns of DG starts
- **Marching in under the DG flag.** ~95% failure; the word reads as "distant and secondary". (course day 2, transcript)
- **Copying DMBOK.** The DAMA Wheel and the Aiken Pyramid are stamped "bad framework, explains nothing"; the pyramid's phase logic is artificial — real companies do it in any order. (course day 1, slides p.107-108)
- **Building the org chart first.** DAMA's full body stack is "a maximum program. Without necessity, build a smaller-scale governance system." Real committees exist only at transnational scale — "maybe two dozen companies max in Russia". (course day 5, slides p.56; transcript)
- **Hiding behind the data catalog.** A headline research finding: the platform team "hides behind the data catalog and avoids solving the hard data-management questions" — chiefly the role model. (course day 2, slides p.53; day 4, slides p.66)
- **Data-first cleansing.** Per McKinsey up to 70% of cleansing effort is wasted; a large company burned hundreds of millions of dollars and 2+ years on enterprise-wide cleansing because nobody knew which data served which use cases. (course day 3, slides p.9)
- **Starting with the glossary.** "Why does everyone declare metric divergence as almost their main pain, yet nobody builds glossaries?" It is the only component requiring active business participation; his own catalog lived 3 years without one. (course day 5, slides p.28; day 4, transcript)
- **Drafting business people as the working stewards.** "Business people — accountants, marketers — will never do hands-on steward work in any workflow you design." (course day 2, transcript; day 3, transcript)
- **Hiring the DG leader from outside.** You wait years for him to become an old-timer; meanwhile "you get sabotage and imitation." (course day 6, slides p.104)
- **"We developed an approach but they don't follow it."** The verdict is one word: "kindergarten." The leader's job is mediation, not publication. (course day 6, slides p.105)
- **Taking budget and inheriting the payback burden.** A funded team must prove its economics annually, and the honest number is usually modest; in the fight for engineers the catalog always loses. (course day 5, transcript; day 2, transcript)
- **Writing goals you can't measure.** "Data transparency", "trust" — don't; use reuse rate, DQ metrics, search speed. "You can't and shouldn't try to do everything at once." (course day 2, slides p.57, p.61)
- **Over-promising ROI to win the start.** The follow-up — "what share can you provably reduce?" — turns an approved program into a personal liability. (course day 6, transcript)
- **Full decentralization first, governance later.** His own company "went immediately to maximum Wild West — governance activities never took root; we're still cleaning that up." (course day 2, transcript)
- **Bureaucratic vocabulary.** Even "certification" "smells of bureaucracy" to some audiences — consider another term. (course day 3, transcript; day 5, transcript)

## First 90 days
Only actions the author explicitly recommends. The *calendar* is inferred — he gives a flow, a stage-colouring and "this worked in 3 months" examples, never weeks.

**Weeks 1-2 — decide whether to start at all.**
1. Answer in writing: is the *absence* of built-out DG a current constraint? (course day 2, slides p.23)
2. Run the 12-statement test. Fewer than 5 → stay in common sense and stop here. (course day 2, slides p.24)
3. Place yourself on the archetype grid and the regulation × complexity 2×2. (course day 1, slides p.103-104)
4. Locate yourself among the peer archetypes rather than against a maturity ladder. (course day 2, slides p.54)

**Weeks 2-5 — collect pains, not requirements.**
5. Run the pains express-session: dump pains by audience bucket, cluster into bundles, rank in a mixed group. (course day 1, slides p.120-121)
6. Separate pains from drivers; prioritize top-management-recognized pains, above all incidents linkable to DG. (course day 2, transcript)
7. Find the already-funded initiatives your work could unblock — that is your packaging. (course day 2, transcript)
8. *Inferred:* write the one-sentence problem statement per Lean DG before going further. (course day 1, slides p.119)

**Weeks 4-8 — ship common-sense wins in parallel with the analysis.**
9. Sketch the domain structure in a spreadsheet, domain + owner columns — "a bad domain structure simply won't stretch onto your people." (course day 3, transcript)
10. Build the registry of most-significant marts (Excel allowed): named tech + business owner, checkers, docs, watched daily. (course day 3, transcript)
11. Turn on three checker types across key objects: nulls, freshness, completeness. (course day 2, transcript; day 4, transcript)
12. Run a subbotnik: one responsible person per domain, one month, public rewards — name it stewardship only afterwards. (course day 2, transcript; day 3, slides p.104-107)
13. Pick one visible certification win with a 3-month horizon; dashboard certification is the worked example. (course day 6, transcript)

**Weeks 6-10 — build the case while the wins land.**
14. Map use cases onto value-adding process flows; score impact × feasibility; keep at most 20-30. (course day 2, slides p.47-49)
15. Frame the numbers as agreed losses vs cost of prevention; prove minimal losses > maximal costs. (course day 1, slides p.45)
16. Prepare the answer to "what share of this can you provably reduce?" before you are asked. (course day 6, transcript)
17. Assemble the operational metrics you will report on, incl. days without incidents in critical reporting. (course day 6, transcript)

**Weeks 8-12 — decide the mode and write it down.**
18. Write the DG Vision as a 4-6 page six-pager — "in the end it may be the only document you actually need." (course day 2, slides p.50)
19. Set goals in three tiers — program, DG team (SMART, annual), steward — and delete every goal you can't measure. (course day 2, slides p.56-57)
20. Test the sponsorship gate: 1 of CDO/CTO/CFO/CEO for the MVP. If you can't clear it, don't stall — borrow the sponsorship of other funded projects. (course day 2, slides p.64; day 6, transcript)
21. Choose the branch honestly: an MVP on one critical business domain, or common-sense DG with chained initiatives. Budget denial is a normal branch, not a failure. (course day 6, transcript; day 1, slides p.118)
22. *Inferred:* if you take the MVP branch, write the exit criteria on day one, so the MVP ends rather than fades. (course day 1, slides p.118)

**What not to do in the first 90 days**, from the stage-colouring: no business glossary, no semantic layer, no committees, no catalog procurement. (course day 6, slides p.100-101)

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
- UK Government Data Maturity Framework — the author's pick of open maturity models, free self-assessment sheets (course day 6, slides p.44-45)
