---
type: cross-cutting
purpose: Recognize a failing DG program early, by symptom
---
# Failure catalog — how DG programs actually die

This file consolidates every anti-pattern, war story and post-mortem scattered across the theme files into one diagnostic surface. It is not a list of vices: each entry starts from something you can observe this week, names the mechanism behind it in the author's own logic, gives the number or quote that proves it, and — where the source material actually has one — the counter-move. Where it doesn't, the entry says so rather than inventing advice.

Use it two ways. **Triage:** find your symptom in the table below and follow it into the family. **Design review:** read a whole family before you commit to a roadmap, a role model or a tool purchase, and check which of these you are about to build.

Source tags are kept exactly as they appear in the theme files (`course day N, slides p.X` / `transcript`). Employers stay anonymized. Two of the themes contradict each other in places; where they do, this file says so instead of merging silently — see [Where the themes disagree](#where-the-themes-disagree) at the end.

---

## Quick triage — symptoms you can observe this week

| Symptom you can see | Likely failure below | Where to read |
|---|---|---|
| Business politely nods at your deck and nothing changes | [Marching in under the DG flag](#marching-in-under-the-dg-flag) | `11_dg_program_themes/getting-started.md` |
| Roles were announced six months ago; the assigned people have never done anything | [Roles announced, hours nowhere](#roles-announced-hours-nowhere) | `11_dg_program_themes/roles-and-operating-model.md` |
| Your stewards only act when someone files a ticket | [The reactive data partner](#the-reactive-data-partner) | `11_dg_program_themes/roles-and-operating-model.md` |
| Nobody noticed a domain lost its owner half a year ago | [Silent washout](#silent-washout) | `11_dg_program_themes/roles-and-operating-model.md` |
| You bought the catalog; the org questions are still open | [The platform team hides behind the data catalog](#the-platform-team-hides-behind-the-data-catalog) | `11_dg_program_themes/data-catalog.md` |
| The tool is deployed, usage is voluntary, nobody has a target | [The tool exists, the process doesn't](#the-tool-exists-the-process-doesnt) | `11_dg_program_themes/data-quality.md` |
| Field descriptions are empty or auto-generated; people stopped opening the catalog | [The burnt desert](#the-burnt-desert) | `11_dg_program_themes/data-catalog.md` |
| Your DQ system is a checker engine plus an incident dump | [Engine-and-dump](#engine-and-dump) | `11_dg_program_themes/data-quality.md` |
| More checkers went in and quality "got worse" | [Coverage gaming and the red wall](#coverage-gaming-and-the-red-wall) | `11_dg_program_themes/data-quality.md` |
| Your status report counts stewards, standards and glossary terms | [Metric theatre](#metric-theatre) | `11_dg_program_themes/maturity-and-metrics.md` |
| Someone asked "what share of that can you provably save?" and you froze | [Over-promising the payback](#over-promising-the-payback) | `11_dg_program_themes/getting-started.md` |
| Your business case rests on faster decisions and easier onboarding | [The castle in the clouds](#the-castle-in-the-clouds) | `11_dg_program_themes/maturity-and-metrics.md` |
| Your ROI model has a "% productivity improvement" cell somebody guessed | [Vendor arithmetic taken at face value](#vendor-arithmetic-taken-at-face-value) | `11_dg_program_themes/maturity-and-metrics.md` |
| The domain map is beautiful and the owner column is empty | [Domains without owners](#domains-without-owners) | `11_dg_program_themes/domains-and-data-mesh.md` |
| Three months of debate about the right splitting criterion | [Taxonomy paralysis](#taxonomy-paralysis) | `11_dg_program_themes/domains-and-data-mesh.md` |
| Domains build what they like; the platform can only ask nicely | [Wild West first, governance later](#wild-west-first-governance-later) | `11_dg_program_themes/domains-and-data-mesh.md` |
| The glossary project has been "starting" for a year | [Glossary-first](#glossary-first) | `11_dg_program_themes/dg-program-roadmap.md` |
| Certified dashboards sit on uncertified marts | [Certifying reports before marts](#certifying-reports-before-marts) | `10_ai_era_themes/certified-core-layer.md` |
| Certified object count is up; traffic to them isn't | [Counting badges instead of traffic](#counting-badges-instead-of-traffic) | `10_ai_era_themes/certified-core-layer.md` |
| Nobody remembers the last time a certification was revoked | [Badge decay](#badge-decay) | `10_ai_era_themes/certified-core-layer.md` |
| The framework diagram is finished; the pains analysis was never done | [Framework theatre](#framework-theatre) | `11_dg_program_themes/dg-frameworks.md` |
| Your program has one sponsor's name on it, or reports into three of them | [The program dies with its org chart](#the-program-dies-with-its-org-chart) | `11_dg_program_themes/dg-program-roadmap.md` |
| An agent generated hundreds of checkers and now incidents are flooding | [The AI checker flood](#the-ai-checker-flood) | `11_dg_program_themes/data-quality.md` |
| Catalog descriptions filled up fast and nobody confirmed any of them | [AI-filled metadata without a review gate](#ai-filled-metadata-without-a-review-gate) | `11_dg_program_themes/data-catalog.md` |
| You cannot tell which agent ran which query | [Agents under a shared user account](#agents-under-a-shared-user-account) | `10_ai_era_themes/ai-governance.md` |
| Your assistant answers confidently and wrongly about neighbouring domains | [Governing the AI layer before the layer under it](#governing-the-ai-layer-before-the-layer-under-it) | `10_ai_era_themes/domain-knowledge-base.md` |

---

## Family 1 — Failures of mandate and resource

The program never gets the authority, the hours or the political cover it assumed. Most of these are decided before the first sprint.

### Marching in under the DG flag

**Looks like:** You present "our Data Governance program" to business stakeholders. They are polite, they agree it sounds important, and nothing moves. Follow-up meetings get rescheduled. The word "governance" comes back to you as "that platform thing".

**Why it happens:** "Business buys solutions to problems it actually feels." DG is not a felt problem; it is your abstraction of many felt problems. The word itself reads as "distant and secondary", and the vocabulary that comes with it — DMBOK, stewardship, custodianship — signals academic exercise exactly where you need to sound like operations.

**Evidence:** Going in under the literal flag fails "in ninety-five percent of cases — business simply doesn't want to understand what DG is." So: "better not to call it DG at all." (course day 2, transcript). The success-factor slide states it as strategy: "It is useless to explain DG to the business and wait for enthusiastic support. Business will support you, but will never postpone its own tasks for DG tickets. **DG is a thing data/analytics leaders must arrive at themselves.**" (course day 6, slides p.104)

**What actually works:** Attach the work to an initiative that already has money. Today's strongest disguise is AI — "for the AI model to work you need to feed it quality data — surprise." (course day 2, transcript). Name the pain, not the discipline: one mid-size peer sold it as "DG as a service unblocking business initiatives" and funded a 3-person team off an Excel of small monetized cases (course day 2, slides p.41-43). And watch every word — though the blacklist is shorter than it looks: "data management sync" is received better than "committee" and works identically (course day 5, transcript), while "certification" is a normal word and needs no euphemism (the course's day-3 warning about it has been withdrawn by the author; see `10_ai_era_themes/certified-core-layer.md`).

**Read:** `11_dg_program_themes/getting-started.md`, `11_dg_program_themes/dg-frameworks.md`

### Taking the budget in a company that counts

**Looks like:** You win the fight for a funded DG team. Twelve months later most of your calendar is spent defending the line item, and every planning cycle re-opens the question of what it returned.

**Why it happens:** Funding converts governance from a background practice into an accountable investment, and the honest return is modest. Meanwhile a dedicated team is a single visible object that a cost cut can remove in one decision.

**Evidence:** "Once you have a funded DG program, you inherit the burden of proving payback. If your company scrutinizes money closely, it may be better *not* to form a separate DG team. Sometimes companies strategically choose to hide this work inside teams that have a clearer basis for their existence." (course day 5, transcript). The author's own calibration number, disclosed as a warning: "my whole DG slice brings the company about 11M RUB a month — very little for a company that size" (course day 6, transcript). A large fintech cut its entire DG team — stewards and catalog support included (course day 2, transcript). His own defence is structural: "there was no dedicated DG FTE to cut — DG is smeared across teams" (course day 3, transcript).

**What actually works:** Decide *whether to ask* before you decide how much to ask for. Where money is scrutinised hard, run the work inside teams with a clearer raison d'être and fund it with a platform tax — each domain commits a % of existing capacity, which lands in roughly 70% of cases "without any extra headcount or extra budget" (course day 2, transcript). Related trap on the same axis: pushing central BI/DG cost into business-unit budgets. "Never works anywhere." (course day 3, transcript)

**Read:** `11_dg_program_themes/getting-started.md`, `11_dg_program_themes/dg-program-roadmap.md`, `11_dg_program_themes/maturity-and-metrics.md`

### Over-promising the payback

**Looks like:** You bring a big total to the approval meeting. Then comes the follow-up question, and you improvise a commitment on the spot.

**Why it happens:** Building the case is the visible task; the second question is the real one, and nobody rehearses it.

**Evidence:** "They ask — what share of this are you ready to save *provably*, over a year, two, three? And you most likely don't know. You will have to promise something. And if it doesn't come true, you take a defeat in management's eyes — or in the end, get fired. I am in that situation right now." (course day 6, transcript)

**What actually works:** Decide the committed fraction before the meeting, not in it (course day 6, transcript). Frame the case the way top managers actually read it — agreed possible losses versus the cost of preventing them, and "a positive decision is always taken when the *minimal* losses exceed the *maximal* costs" (course day 1, slides p.45). Commit only where the economy is direct: infrastructure saved by deleting redundant objects is the one line that needs no attribution argument (course day 6, transcript; course day 2, transcript).

**Read:** `11_dg_program_themes/maturity-and-metrics.md`, `11_dg_program_themes/getting-started.md`

### Roles announced, hours nowhere

**Looks like:** Rules are regulated, roles are distributed, an announcement went out. No capacity was reserved, nothing happens at review time if the work isn't done, and quality is nominally owned by "everyone".

**Why it happens:** Assignment is free and adoption is not. Stewardship is always a second hat, never a position — so it competes with work that has consequences attached, and loses every time.

**Evidence:** The peer status board records exactly this at a neobank: "regulating rules and imposing roles gets rejected by the culture; de-facto acceptance of the roles never started, nobody there began doing it" (course day 6, slides p.107; course day 3, slides p.72). "Everyone who gets to formalizing stewards realizes the global problem was not defining them but motivating them — it's always a second hat, a role, not a position." (course day 1, transcript). The collective-responsibility variant is named separately: developers don't monitor event emission, QA rarely tests data events, nobody can say how good quality actually is — "under collective responsibility there must be leadership and a managing process, otherwise collective responsibility equals irresponsibility" (course day 4, slides p.99).

**What actually works:** Put the role in the competency matrix so "they cannot pass calibration without doing a defined set of governance activities" — "a carrot in front and a carrot behind" — and protect ~20% of their time with an administrative agreement that "tech debt includes data governance" (course day 2, transcript). Top-down alternative: adopt a maturity model and give each top manager an annual goal "my function reaches level X"; steward duties then cascade by themselves (course day 3, transcript). Cheap interim: a monthly meeting with domain partners showing per-steward dashboards — "peer dynamics alone motivates, even before you have the right to set targets" (course day 5, transcript). The diagnostic question: "What happens at calibration if he doesn't do the governance work? If the answer is 'nothing', you have a document, not a role." (course day 2, transcript)

**Read:** `11_dg_program_themes/roles-and-operating-model.md`

### The program dies with its org chart

Two variants of the same mechanism: the program's survival is pinned to an organisational arrangement that will change.

**Looks like:** *(a) Three VPs.* DG gets elevated to group or ecosystem level. Practice, methodology and platform report to different executives. Budgets grow, so do the meetings, and within two years parts of it are being terminated. *(b) The one-sponsor program.* The program has one executive's name attached. That executive changes role. Within a quarter it is "under review", then suspended, then quietly gone — and later, maybe, resuscitated.

**Why it happens:** Splitting one program across several reporting lines creates competing centres of power over the same asset, and the asset is data — which everyone wants to own and nobody wants to fund. The mirror failure is the opposite concentration: a program depending on one executive has a half-life equal to that executive's tenure, and it is the single most convenient thing to cut, because cutting it removes a line item rather than a capability anyone will miss next week.

**Evidence:** At a large telecom ecosystem the DG team was elevated with ~20 stewards, then "dissolved organizationally — it ate a lot of money, internal centers of power over data emerged and competed for budgets; DG practice, methodology and the data platform reported to three different VPs; some parts got terminated." (course day 1, transcript). At a large fintech the program was suspended after the CDO changed (course day 3, slides p.72); the same company later cut its whole DG team, stewards and catalog support included — "they'll probably resuscitate it later" (course day 2, transcript). Standing lesson from the research: "in the fight for engineers between platform product streams, the catalog loses" — every catalog surveyed shows a "fading trend" (course day 2, transcript).

**What actually works:** Leave no single point to cut. The author's own posture is explicit: DG is smeared across teams with named drivers and shared goals, so "there was no dedicated DG FTE to cut" (course day 3, transcript). Where you do build a core team, split it by *expertise* rather than by executive — catalog lead, metadata lead, reference-data lead — each supporting many domain custodians: "at the bottom level everyone does everything; the middle level is split into cubes" (course day 1, transcript). And on the upside, don't scale on one sponsor: the board's gate is 2 of 4 C-level sponsors (CDO/CTO/CFO/CEO) plus the MVP domain owner plus interest from other domain owners. "Below that you have a project, not a program." (course day 6, slides p.100)

**Read:** `11_dg_program_themes/dg-kitchen-research.md`, `11_dg_program_themes/dg-program-roadmap.md`, `11_dg_program_themes/roles-and-operating-model.md`

### No calm period

**Looks like:** Every initiative you start gets orphaned by a reorg before it lands. Owners change mid-project. The roadmap is re-cut quarterly and nothing ever reaches its second stage.

**Why it happens:** DG initiatives are cross-role and slow by construction; an organisation that re-transforms on a quarterly cadence never gives one a full run. This is an environmental blocker, not a design flaw in your plan.

**Evidence:** From the peer research: "process transformation every quarter — there is no calm period for DG projects." (course day 2, slides p.54; course day 6, slides p.107). And the research's own verdict: the company transforming its processes every quarter never got a DG project off the ground — "the clearest single-variable explanation in the whole set" (course day 6, slides p.107).

**What actually works:** Pick initiatives that fit inside one quarter (course day 2, slides p.54). The worked example is dashboard certification shipped in 3 months, which "moved metrics AND worked emotionally" and bought licence for more expensive initiatives (course day 6, transcript).

**Read:** `11_dg_program_themes/dg-kitchen-research.md`, `11_dg_program_themes/dg-program-roadmap.md`

### The imported DG leader

**Looks like:** A capable DG manager is hired from the market with a strong mandate on paper. A year in, the approaches are published, the meetings happen, and no team's process has actually changed.

**Why it happens:** Moving tectonic plates requires authority plus expertise in how the company really works. A newcomer has neither, and the organisation knows it.

**Evidence:** "You can take one from the market, but then you'll wait for him to become an old-timer, because before that nobody will let him seriously change their processes. You'll get sabotage and imitation." (course day 6, slides p.104). The leader profile the material asks for: "people who have known pain" — a change manager with mileage, a communicator, a person with will, "and ideally not yet burned out. A rarely encountered combination." (course day 5, transcript). The research corroborates from the other side: fast benefits correlate with a *respected internal senior* running the MVP (board frame "success factors").

**What actually works:** Staff the MVP from inside — the specified team shape is 2-3 leads or seniors from DWH/BI, systemic thinkers, **2+ years in the company**; tenure is a selection criterion, not a preference (course day 6, slides p.100). No reliable counter-move exists for the case where you have already hired externally; the source material only describes the wait.

**Read:** `11_dg_program_themes/roles-and-operating-model.md`, `11_dg_program_themes/getting-started.md`

---

## Family 2 — Failures of roles and ownership

The role model is drawn from a book rather than from the people who will actually carry it.

### The business data steward who was never going to do it

**Looks like:** Your workflows assume hands-on work from accountants, marketers or HR managers. The duties were combined with their business-function duties. Nothing gets done, and every escalation ends in "we'll get to it".

**Why it happens:** "The role of business in data management is exaggerated." Their real contribution is nominal — sponsor, arbiter, requirements — and no workflow design changes that.

**Evidence:** The board says it flatly: "The classic problem of the Business Data Steward — they engage poorly, they ignore their duties when those duties are combined with duties inside a business function." (course day 3, slides p.78). "Business people will never do hands-on steward work in any workflow you design — at best they answer questions, approve the glossary and state DQ requirements, nowhere does it work otherwise." (course day 2, transcript; course day 3, transcript). The research generalises it: designed everywhere, staffed almost nowhere (course day 3, transcript; slides p.82).

**What actually works:** Keep business for definitions, requirements and sign-off; move execution to the domain's data person. The role that carries the load is the **Data Custodian / Data Partner / Data Curator** — "probably MORE important than the Data Steward role. And at minimum it comes first" — because custodian duties are already the day job: access control, technical DQ fixes, conformance of new data, master-data versioning, change management. "Recognizable, isn't it — this is the ordinary daily work of our teams, without any extra roles." (course day 1, slides p.61; course day 3, slides p.60; course day 6, slides p.105). Note the counter-evidence the KB itself preserves: one large bank hired business Data Stewards from the market as full positions and policy rollout visibly accelerated — "rare, expensive, and the honest counter-evidence to 'second hat is enough'" (course day 3, slides p.52-53).

**Read:** `11_dg_program_themes/roles-and-operating-model.md`, `11_dg_program_themes/dg-kitchen-research.md`

### Owner on the org chart

**Looks like:** A CFO, an HR director or a procurement director is anointed "Data Owner" for a domain. The title appears in the deck. The duties are performed, if at all, by someone else.

**Why it happens:** The classic ownership wheel assigns eight petals to an executive who has neither the context nor the hands for most of them.

**Evidence:** On that wheel the author stamps three of eight petals in red: "In fact more than half of this is done not by the DO but by the DS." Beside it, the three questions he actually asks: is your owner a business stakeholder, the team of the producing system, or the DWH engineers and analysts who create the objects? (course day 3, slides p.64). Draping quality duties onto CFO/HRD-type people "yields pushback; their role is nominal" (course day 3, transcript).

**What actually works:** Exec-level "Data Owner" is a near-useless concept; the useful one is **data object owner** — the specific engineer, BI developer or analyst who created the object, because central teams "have limited hands — they cannot make the step instead of every single author." If a domain has a head of analytics, hang domain ownership there: "they have far more understanding, context and resource." (course day 3, transcript; course day 1, transcript)

**Read:** `11_dg_program_themes/roles-and-operating-model.md`, `11_dg_program_themes/domains-and-data-mesh.md`

### The reactive data partner

**Looks like:** The role exists, the people are named, the rules are written — and they only move when a ticket arrives. The role has become a queue.

**Why it happens:** Distributing people into domains changes the org chart, not the behaviour. Proactivity requires a goal, a ritual and a visible peer comparison; none of those come with the announcement.

**Evidence:** A ride-hailing tech company distributed engineers into domains, invented the Data Partner role, kept the rules — and still "failed to make the data partners proactive; they continued to act reactively." (course day 6, slides p.107). The board's own summary: "Assignment is not adoption."

**What actually works:** The role card that does work is written as a role, not a position: an experienced BI developer coordinating the domain's certified report layer and certified mart layer against SLAs, running company-wide BI standards inside the domain — with two clauses that make it real: "the BI Partner's OKRs include a BI maturity goal, agreed with the goals of the BI CoE and of the domain", and "BI CoE provides methodological, tooling and hands-on support for all activities within this role." (course day 3, slides p.61)

**Read:** `11_dg_program_themes/roles-and-operating-model.md`, `11_dg_program_themes/domains-and-data-mesh.md`

### Silent washout

**Looks like:** The role register lives in a spreadsheet. People leave, change teams, get reassigned. Nobody re-opens the sheet. Six months later you discover a domain has been unattended the whole time.

**Why it happens:** A registry with no event model cannot propagate a departure. Ownership decays silently because nothing fires when it changes.

**Evidence:** "The master system for domains and roles must be the catalog, not a spreadsheet, with alerts on assignment, re-assignment and onboarding — otherwise people wash out silently and we discover nobody has been properly tending a domain for half a year." (course day 3, transcript). The starting picture for sponsors: 4-45% of assets per domain collection had owners and 46-74% lacked classifications; a job-search platform ran at ~30% of objects with owners (course day 3, slides p.24; course day 4, slides p.87).

**What actually works:** Master domains and roles in the catalog with alerts on re-assignment and onboarding, plus a per-domain communication plan — domain × business owner / steward / SME × meeting type, channel, current and target frequency (course day 3, transcript; slides p.44).

**Read:** `11_dg_program_themes/roles-and-operating-model.md`, `11_dg_program_themes/data-catalog.md`

### Merging the two steward lanes

**Looks like:** One incident workflow, one "steward" in it. The business person is asked to maintain checkers or write documentation. Within a month they have stopped responding.

**Why it happens:** The business steward's contribution is *judgement*, not labour. Give them labour and the role quietly dies, taking the judgement with it.

**Evidence:** Four swimlanes, and the split matters: the Data Owner approves significant platform/application changes; the **Business Data Steward's ONLY operation is reviewing incidents that require business knowledge**; the Technical Data Steward / DataOps confirms the incident and manages the checks; the Data Engineer fixes, reloads and revalidates. "Don't merge the business and technical steward." (course day 4, slides p.119-120; transcript). Their entire contribution to check design is the baseline: "can this metric fluctuate this much from week to week, or is that already an incident?" (course day 4, transcript)

**What actually works:** Keep the lanes separate and link incidents, tickets and tasks. The split-role pattern from a large ride-hailing tech company is the reusable version: a "BI governor" owning only certified reports and report standards, and Data Partners owning core layers, marts, certification and architecture — "separating a reporting-standards owner from mart-and-core-layer owners produced clarity that the single-steward companies never reached." (course day 3, slides p.63; `dg-kitchen-research.md`)

**Read:** `11_dg_program_themes/data-quality.md`, `11_dg_program_themes/roles-and-operating-model.md`

### Full metric devolution

**Looks like:** Every metric is assigned to the product team that "owns" it. Cross-functional metrics have three claimed owners or none. Analysts push back hard on writing methodology.

**Why it happens:** Responsibility for a metric is genuinely distributed across functions, so devolving it multiplies coordination cost beyond what any team will pay — and methodology writing needs a business/systems-analyst skill set that data analysts do not have and do not want.

**Evidence:** A real-estate classified tried assigning all metrics to product teams and failed. CPT revenue touches Monetization, Pricing, Sales and Finance; audience metrics touch every product line plus Marketing and CRM; "cross-team coordination costs more than teams will pay, and data analysts turn out to be bad at writing methodology — strong pushback on such tasks." (course day 5, slides p.31)

**What actually works:** The working split: **key metrics** (top-level, in the company business model, cross-team, externally reported) → Data Steward, and that is where DG focus goes; **local product metrics** (drivers) → Data Analyst, accumulated systematically but second priority. The chain that worked: metric registry → classify the key ones → assign owners → describe methodology → business glossary, scoped to one domain *pair* per year. "It worked because it was narrow." (course day 5, slides p.32-33)

**Read:** `11_dg_program_themes/domains-and-data-mesh.md`, `11_dg_program_themes/roles-and-operating-model.md`

### Kindergarten

**Looks like:** "We developed an approach but they don't follow it." The approach is published, correct, and universally ignored.

**Why it happens:** Every key DG initiative is cross-role. Publishing rules for other people's teams is not leadership of a cross-role initiative; it is the absence of it.

**Evidence:** The verdict on the success-factors slide is one word: "kindergarten." The DG leader's job description is mediation, not publication. (course day 6, slides p.105)

**What actually works:** Mediate priorities with the teams you depend on before publishing — weave DG tasks into their OKRs (course day 3, transcript) — and accept the honest ceiling the author states about his own company: "I cannot force anyone — I can only build systems where doing it right is easier than not." (course day 6, transcript)

**Read:** `11_dg_program_themes/dg-frameworks.md`, `11_dg_program_themes/roles-and-operating-model.md`

---

## Family 3 — Tooling without process

The purchase or the build reads as progress. The organisational work it was supposed to enable never starts.

### The platform team hides behind the data catalog

**Looks like:** The catalog project has a roadmap, a budget and a demo. Meanwhile ownership, criticality classification, contracts and the role model have no owner and no date.

**Why it happens:** Buying a tool is legible progress; changing a role model is not. So the tool becomes the answer to every governance question and defers the org work indefinitely.

**Evidence:** One of the four headline findings of the peer research: the platform team "hides behind the data catalog and avoids solving the hard data-management questions" — chiefly the role model (course day 1, slides p.117; course day 2, slides p.53; course day 6, slides p.99). The board's Program Map carries it as an explicit fail branch: **"pseudo DG — only a catalog, no business involvement"** (board, Program Map 3.0). Diagnostic: "If the catalog answers every governance question, the role model doesn't exist." (course day 6, slides p.99)

**What actually works:** "A catalog becomes a DG tool only when the steward has an equipped workplace in it: a task inbox for their domain, policies to approve, DQ checks to review, documentation to fill, access rights to re-review." Otherwise it is a search box. (course day 1, transcript)

**Read:** `11_dg_program_themes/data-catalog.md`, `11_dg_program_themes/dg-program-roadmap.md`

### The tool exists, the process doesn't

**Looks like:** A DQ module with two checks. A catalog in production with view-only input. A perfectly decent in-house tool that people use if they feel like it. No criticality classification, no coverage target, no consequence.

**Why it happens:** Deploying proves procurement maturity and nothing else. Voluntary adoption looks like success from the outside, which is exactly why it survives.

**Evidence:** The author's self-diagnosis on his own platform: a DQ module with two checks (duplicates, nulls), analysts free to add their own — "the tool exists = the process doesn't." A peer's home-grown DQ product is flagged red on the same slide for being "used voluntarily, without control or goals." (course day 4, slides p.145). Adoption reality elsewhere: a catalog in prod with all input via git and integrations, 900 target power users against 90 monthly actives — ~10% against the 80%-of-target-persona benchmark (course day 4, slides p.87 vs p.53). Only 10% of the surveyed sample monitors DQ incident SLAs (board frame 6).

**What actually works:** Gates in the delivery flow, not exhortation. "No description — no prod deploy" moved table-description quality from 49% to 86% in a year across ~7000 tables — "nothing voluntary in the study moved a number like that" (course day 4, slides p.48). The gate can sit on deploy or on scheduling: "you cannot put an object on a schedule if it has no description." Pair the hard gate with an AI "generate description" button so it stays survivable. And make checkers a *precondition of certification*, not an optional extra (course day 4, transcript). Watch the social failure mode of any gate: "your release manager is on vacation — ship it anyway." The whole game is the balance between blocking checks and post-hoc checks. (course day 2, transcript)

**Read:** `11_dg_program_themes/data-quality.md`, `11_dg_program_themes/dg-kitchen-research.md`

### Engine-and-dump

**Looks like:** A self-written checker engine plus an incident dump, and nothing else. Business checkers rarely get created. False positives flood the channel. Incidents are badly triaged. And "then the feeling that you therefore have data quality management does not appear."

**Why it happens:** The engine is the easy, engineering-shaped part. Triage, criticality logic and the incident lifecycle are the organisational part, and they are what actually produces trust.

**Evidence:** "90% of DQ systems in the wild = a self-written checker engine + incident dumping." (course day 4, transcript). And the reason the tool is not the variable: unlike catalogs, "these tools work — they never require complex social scenarios inside themselves. You just need a good checker library and a good performant engine. And that's it." Which is exactly why process, roles and criticality logic decide the outcome. (course day 4, transcript)

**What actually works:** Group similar issues into incidents and then **filter** them — the platform slide carries an explicit "ignored incident" branch, "the part homegrown engines skip" (course day 4, slides p.119). Separate issue from incident. Route the four swimlanes properly (see [Merging the two steward lanes](#merging-the-two-steward-lanes)). And put a team KPI on the exec report: "share of incidents discovered by business" — the team must announce incidents proactively with a fix ETA; business finding it first counts against the metric (course day 4, transcript).

**Read:** `11_dg_program_themes/data-quality.md`

### The burnt desert

**Looks like:** You paid a lot of money and got ghost towns of empty field descriptions. Trust drops. The tool degrades into a search box "in the best case", and people go back to asking a colleague.

**Why it happens:** Completeness is best near the end of the delivery process, but "motivation to enter anything collapses after release." Nothing in a voluntary model bridges that gap.

**Evidence:** (course day 4, slides p.40, 44, 46). Baseline pictures from the same material: 780 tables with 21 fully described (3%), 92 partial (12%), 668 with none (86%); 24,807 columns of which 3,363 described (14%) (course day 6, slides p.33). Eckerson's deployment-challenge survey for calibration: tool complexity 42.6%, lack of user adoption 40.7%, lack of integration 37.0%, missing functionality 25.9%, missing data or objects 22.2%, users don't trust the information 11.1% (course day 4, slides p.65).

**What actually works:** The fix is sequencing, not effort. Maximise automated filling ("no reason for anyone to fill keys for every individual dataset"); a federated-catalog API so domain catalogs push in; algorithmic pre-fill of domain, stewards and tags; descriptions inherited up the lineage from data contracts; documentation entered in the flow of work via a CI/CD check that breaks the build; "don't boil the ocean" — curate the top 20% node objects (most queried, or used in the most-viewed reports); ownership culture with domain data partners carrying a KPI on completeness. (course day 4, slides p.47). Pair that with the top-20% rule of the core-layer program: compute candidates from query analysis, let each domain finalize the list, raise requirements on that layer only, and monitor completeness separately for core versus the rest (course day 4, transcript).

**Read:** `11_dg_program_themes/data-catalog.md`

### The open-source trap

**Looks like:** A catalog looks like a simple product to data engineers, so it gets built or self-deployed. It honestly stores metadata and lineage. Adoption never happens, because nobody outside the developer audience can navigate it.

**Why it happens:** The metadata store is the small half. The hidden cost is *product work* — UX, CustDev, feature adoption — for years, and nobody funds a permanent team for it.

**Evidence:** "A catalog has the illusion of a very simple product to data engineers and platform managers. Wire up DataHub and it honestly stores metadata and lineage — and gets bad adoption, being hard to navigate for anyone wider than developers." Many such projects "sit permanently on the edge of ineffectiveness." (course day 4, transcript). "For 90% of companies the boxed solution is optimal" — its flaw is psychological, expensive licences in the moment, but the odds of value beat "permanently operating a half-written, crooked, lopsided catalog" (course day 4, transcript). The peer three-path table: boxed = fast rollout, vendor support, no admin payroll / expensive now, redundant features. Open source = conditionally free, extendable / needs a team, "integration = dancing with a tambourine". In-house = only what you need / working functionality "can take years" (course day 4, slides p.30).

**What actually works:** Building is legitimate when it is *funded like a product*: the one place in the research where refusing vendors worked funded an MVP in a quarter with three engineers and then a team of up to ten in year two. "Without that headcount, the same decision produces an ugly metadata store." (course day 4, slides p.87; `dg-kitchen-research.md`). And ask the reducing question first: "if all you actually need is impact analysis, would a lineage library plus an internal graph tool be enough — without a catalog product at all?" (course day 4, transcript)

**Read:** `11_dg_program_themes/data-catalog.md`, `11_dg_program_themes/dg-kitchen-research.md`

### The catalog as everything-tool

**Looks like:** The catalog acquires a built-in messenger, a second knowledge base competing with the wiki, an in-catalog SQL editor, a report catalog for business users, a DQ engine and a data-access request workflow. The data team now supports two of everything.

**Why it happens:** Vendors ship features "for good measure" and every one of them looks free at purchase time. The catalog went wide and shallow; each duplicated surface splits the golden path.

**Evidence:** Four myths, each refused by name. *Catalog = DG tool*: no tool embodies governance, because governance is "an organizational wrapper that in essence doesn't fit inside a data catalog" (course day 4, slides p.66). *Catalog = DQM solution*: "the catalog's role is not quality control, but maximum dissemination of the results of that control"; a practitioner veto seals it — the catalog's engine is not built for high-performance checks, which killed the "DQ inside OpenMetadata" option in one enterprise evaluation (course day 4, slides p.67; transcript). *Catalog = compliance solution*: compliance is documentation and evidence; in-catalog auditor cabinets are "a very rare, niche story" (course day 4, slides p.66-69). *Catalog = query solution*: "not only redundant but quite risky"; and "integrating data-access workflows into a catalog rollout is the surest way to make the project long, costly and disappointing" (course day 4, slides p.75). On the golden path: "don't believe the built-in messenger of a data catalog, it's self-deception"; an in-catalog IDE is "definitely not something to aim for" (course day 4, slides p.52; transcript). On business users: "data catalogs are not for casual users — that's a fact", and a report catalog inside the data catalog doesn't work for business either — "as a rule, the right answer is: don't" (course day 4, slides p.51; transcript).

**What actually works:** Pick one golden path per capability and switch the duplicates off (course day 4, slides p.52). Target model: data catalog for data-product teams + a data marketplace/portal for consumers, with chatbot-style discovery as the plausible new UX (course day 4, slides p.51). Integrate DQ, don't merge it: the checker engine lives in the DQ portal, the *results* ship as a module inside the catalog with incident review and time-to-resolution (course day 4, transcript). Where business does belong: the self-service scenario — a user sees certified, described objects, clicks through to open them in the BI tool, and knows whom to contact (course day 4, transcript).

**Read:** `11_dg_program_themes/data-catalog.md`, `11_dg_program_themes/data-quality.md`

### Buying before the surrounding maturity exists

**Looks like:** The catalog is procured on general principle. Self-service BI, data products, contracts, ownership and DQM are all immature. The tool has nothing to catalog that anyone trusts.

**Why it happens:** Catalog value is *hostage* to the maturity of everything around it, and unlocks only as those mature. Buying early converts budget into shelfware.

**Evidence:** The sharpest framing of the day: "the benefit of a data catalog is often lower than the cost of producing and supporting it." (course day 4, slides p.42-44). The buy trigger is a U-curve over data-team size: more people first means faster value, then tech debt, a bigger lake, growth and worse DQ turn it around; detect the *increase* in Time to Value, then start — realistically 100+ analysts (course day 2, slides p.35). A legitimate no: one respondent's "everyone works inside their own domain and doesn't go outside — chats are enough for us", valid when all data people sit in one or two tight central teams (course day 4, transcript). Real economics: search-and-understanding losses attributable to the catalog use case measured ~7M RUB/month at a large tech company — "not that much" at that scale (course day 4, transcript).

**What actually works:** If the surrounding maturity is low, redirect the resource there (course day 4, slides p.42-45). Two questions before any demo: "Do you have enough *aggregate maturity* to launch a catalog and get value from it at all?" and "Do you have enough *aggregate practical value* in it to expect analysts and engineers to keep coming back?" (course day 4, slides p.43, 50). And when you do go to market: "all available vendor comparisons are corrupt" — made by vendors with dishonestly picked criteria; weight the criteria for yourself, use an LLM pass only to reach a shortlist of 2-3 to pilot, and treat "we supply no methodology, it all depends on the customer" as the vendor red flag (course day 4, slides p.29; transcript).

**Read:** `11_dg_program_themes/data-catalog.md`, `11_dg_program_themes/dg-program-roadmap.md`

---

## Family 4 — Metrics and theatre

The reporting is impeccable and measures nothing that can go down for a good reason.

### Metric theatre

**Looks like:** The status report counts standards, glossary terms, data owners, stewards, custodians, authorised sources and policies. Every number rises every quarter. Nobody can name a business outcome.

**Why it happens:** Activity counters are the only numbers a young program can produce, and none of them can legitimately fall — which is precisely what makes them safe and useless.

**Evidence:** The clearest published statement of the shift is an insurer's: measuring *quantity* of governance (# standards, # glossary terms, # owners, # stewards, # policies) versus measuring *business impact* (% of consumer DG requirements, % of processes impacted by quality, % of manual processes with automated validations, % of call-centre calls due to data defects, % of reserves held due to data issues). The banner: "a fundamental shift has taken place — what we may have governed 10 years ago is not what we want to govern now." (course day 6, slides p.30-31). Adjacent failures in the same family: writing goals you can't measure — "data transparency", "trust" — instead of reuse rate, DQ metrics, search speed (course day 2, slides p.57, p.61); and adopting a maturity model that is presented and never wired into anyone's annual goals — it works "if the company appropriated it", otherwise it is bureaucracy and the sceptics are right (course day 6, transcript).

**What actually works:** The test question: "can any headline number go *down* for a good reason? If none can, you are counting activity." (course day 6, transcript). Move to operational metrics with owners — % of critical data with defined ownership, metadata completeness *and* age, incident resolution rate and speed, health scores kept distinct from DQ scores — each with a named owner, in a team or personal KPI, reported against a baseline or YoY rather than as a bare level (course day 6, slides p.27; transcript). If you must use proxies ("number of processes with an embedded DQ process"), say out loud that they are proxies: unlabelled, "they are the polite version of metric theatre" (course day 6, transcript).

**Read:** `11_dg_program_themes/maturity-and-metrics.md`

### Coverage gaming and the red wall

**Looks like:** Checker coverage rises. Apparent quality falls — everything goes red, because more checkers detect more events. Someone works out that the cheapest way to move the number is to delete checkers. Meanwhile coverage itself gets padded with trivial checks.

**Why it happens:** The two numbers are mutually gameable by construction, and publishing only one of them invites the game.

**Evidence:** "The more checkers you create, the worse your apparent quality — you simply detect more events and drown in red. Pair quality with coverage metrics so nobody games it by deleting checkers." But coverage is gameable too: annotating a peer's dashboard the author writes that checker coverage is "easy to hack. You'd have to check the quality of the checkers themselves — and that's already overkill." (course day 4, transcript; slides p.143)

**What actually works:** Report both and accept that neither is clean (course day 4, slides p.143). Aggregating DQ upward is "quite debatable"; realistically two options — days without incidents per critical object summed upward, or weighted quality scores with field/object significance, "and the second is where teams fail organizationally" (course day 4, transcript). And keep the four things "more important than DQ dashboards" in view: cross-role agreed processes for defining and updating DQ metrics; good slogans from authoritative management; bad-data alerting aimed at stewards plus shame lists; energy focused on important data — "otherwise you quickly drown in heavy DQ bureaucracy" (course day 4, slides p.144).

**Read:** `11_dg_program_themes/data-quality.md`, `11_dg_program_themes/maturity-and-metrics.md`

### The castle in the clouds

**Looks like:** The business case rests on multiplier-on-existing-investments, faster onboarding via a knowledge base, savings on audits, savings on lawyers, fraud detection, accelerated decision-making, easier self-service and problems fixed before they cost anything.

**Why it happens:** Every item is true and none is buyable. They survive in decks because nobody has to defend them until the CFO asks.

**Evidence:** The whole indirect-benefit list gets a red X and a castle-in-the-clouds picture on the slide (course day 6, slides p.19). Only three zones are worth searching: revenue growth via linking DG to business initiatives, cost savings, and regulator-risk mitigation. On the six-petal ROI wheel *operational efficiency* — "we get access to reliable data faster, we shorten time-to-insight" — is "a very shaky thing… in general it's air", and *innovation* is "also shaky" (course day 6, slides p.4-5; transcript). One sub-case is closed permanently: "attempts to measure the acceleration of decision-making were worked over some ten years ago; it seems there are no fools left" — every company that went deep stopped, and reinventing it burns credibility you'll need later (course day 6, transcript). And *data quality* is refused as its own petal: "in my view it isn't really an independent area" — it always resolves into revenue or cost, so draw that line yourself (course day 6, slides p.5).

**What actually works:** Accept what a DG case actually is: "as a rule, all such proofs work on moral authority or on emotional argumentation. You describe what will not happen if this isn't done, and which initiatives stay blocked" — a legitimate argument, but "call it what it is before the CFO does" (course day 6, transcript). Then carry the conversation on operational metrics, above all **days without incidents in critical reporting**, because business often isn't asking for money at all: "just rid me of this pain, make it not every day." (course day 6, transcript). One caveat the source preserves: organisations with no cost-reduction agenda — government bodies — run on compliance pressure through the management vertical, and the author concedes the three-source model is written for organisations that operate in money (course day 6, transcript).

**Read:** `11_dg_program_themes/maturity-and-metrics.md`, `11_dg_program_themes/getting-started.md`

### Vendor arithmetic taken at face value

**Looks like:** Your ROI model has a "% productivity improvement" cell. Somebody put 23% in it because a vendor calculator did. The rest of the model is arithmetic on that guess, and the totals look excellent.

**Why it happens:** Every vendor calculator makes exactly one move — assume a productivity percentage, multiply by headcount and salary — and the assumption is invisible once the spreadsheet is built.

**Evidence:** Collibra's assumptions: 23% for BI/data analysts and data scientists, 5% for report/app developers and enterprise architects, 26% for integration engineers, DG professionals and stewards, 27% for compliance professionals; plug in 120+120+45 people and it returns $8.379M annual gain and 9.3× three-year ROI (course day 4, slides p.80-86 — marketing numbers, use critically). Forrester's TEI is more instructive because the chain is visible: $3.8M benefits PV vs $813K costs, built on "70% of an analyst's work affected by the tool", 50% productivity capture, 10% risk adjustment (same slides). The author's discount: "we can't verify the numbers, but the evaluation logic is worth copying" — realistically expect **5-7% provable**, and "here a huge zone of speculation arises" (course day 6, slides p.20; course day 4, transcript). The correction finance will make, so make it first: "a productivity improvement does not convert into output. People just start going for coffee more often." (course day 4, transcript)

The same disease in the benchmark family: bad-data rules of thumb ($1 prevent / $10 correct / $100 do-nothing per record) carry the author's annotation directly on the slide — "$100 per bad data record — beautiful, but unrealistic" — and an entire three-year $8.495M savings model is built on that invented constant (course day 6, slides p.12-15). The 1x→10,000x shift-left cost-by-finder chart "is frankly marketing, based on nothing… The chart is really about trust, not cost." (course day 4, slides p.156). Vendor research on lost time — 29-36% of working time, finance worst at 36% — versus the author's own instrumented "share of analysts' target tasks" running 60-70%: measure your own equivalent before quoting theirs (course day 2, slides p.44; transcript). And when someone waves "only 2% of DG programs deliver high business value", quote the small print: **N=59** on a vendor self-assessment site (course day 6, slides p.39-43).

**What actually works:** Copy the evaluation logic, not the numbers (course day 4, transcript). The one multiplier worth stealing wholesale is onboarding: an analyst reaches full productivity in three months; with a well-described catalog, in two (course day 6, slides p.20). And check every benefit term for overlap — the cleaned-record method carries a one-line guard, "*one record is counted once*", because its three terms overlap by construction (course day 6, slides p.23).

**Read:** `11_dg_program_themes/maturity-and-metrics.md`, `11_dg_program_themes/data-catalog.md`

### ROI inflation by polishing the savings side

**Looks like:** The savings side of the model gets refined and re-refined. The investment stays large. When the payback comes out badly, the response is to bolt another benefit onto the same savings line.

**Why it happens:** Savings are the side you control and can compute; revenue requires a business owner to co-sign. So the model grows where it is easy to grow.

**Evidence:** The anti-case to memorise. A company sends 10M direct-mail items a year, ~10% wrong-address or duplicate. MDM would nearly eliminate that: ~$500k/yr saved at 50 cents an item — **but only $100k net** after $400k/yr of new process upkeep. Against a $3M MDM investment that is **30 years' payback**. Rescuing it by bolting on marketing's advanced segmentation model gets the verdict "they probably won't buy this either." Directional lesson: "*recompute the revenue side*, don't polish the savings side." (course day 6, slides p.16-18)

**What actually works:** Method 3 from the same material — a matrix of concrete business projects with income and expense per case, plus a standing DG Office cost line with zero income against it. Because each case must be concrete they are individually small, "and therefore you need many of them" — a dozen, at most twenty to thirty, hunted among initiatives that already have money attached (course day 6, slides p.21). The counter-intuitive strength of the pile: when ~20 cases each individually "doable without DG" accumulate, together they prove a systemic problem (course day 2, slides p.47-49). And negotiate attribution in advance: "we agree with the business that a part of the metric uplift the analyst brings will be attributed to the platform" — attribution share is a negotiated parameter, not a measurement (course day 6, transcript).

**Read:** `11_dg_program_themes/maturity-and-metrics.md`

### A scorecard nobody opens

**Looks like:** A well-built dashboard of per-partner governance metrics exists. It is accurate, it is public, and no meeting references it.

**Why it happens:** Metrics without a ritual that forces people to look at them are decoration. Building the scorecard is the easy half.

**Evidence:** Peer scorecard from a big-tech ride-hailing player, presented as a cautionary artefact: a dashboard of domain-data-partner metrics — share of certified objects, share of traffic reaching certified objects that meet requirements, % legacy objects, description quality — "which nobody looked at." (course day 6, transcript). The industry-wide version of the same failure: effectiveness evidence is "rather emotional. There are almost no examples of comprehensive effectiveness and results analysis" — "it gave positives", "entropy is decreasing", and the reason no better number exists is that "nobody tracks Jira properly" (course day 6, slides p.34).

**What actually works:** Attach the numbers to a standing ritual. A monthly meeting with domain BI partners showing dashboards with per-steward metrics: "People see who is doing better and who worse — peer dynamics alone motivates, even before you have the right to set targets." (course day 5, transcript). And be the one company in twenty that computed something: the single peer that ran a real analysis — chat search time without a catalog vs catalog search statistics × request volume × analyst FTE cost — got a green light for further investment (course day 6, slides p.34).

**Read:** `10_ai_era_themes/certified-core-layer.md`, `11_dg_program_themes/maturity-and-metrics.md`

---

## Family 5 — Sequencing and dependencies

The individual initiatives are right. The order is wrong, and mis-ordering is negative rather than merely late.

### Glossary-first

**Looks like:** Metric divergence is named as the main pain, so the glossary becomes the first project. A year later it is still "starting". Business hasn't written definitions; analysts know the content but treat it as somebody else's priority.

**Why it happens:** The glossary is the one component requiring *active business participation*, and it deadlocks on two hard dependencies at once — cross-domain facilitation with business experts, and a synchronous semantic-layer project.

**Evidence:** "Why does everyone declare metric divergence as almost their main pain, yet nobody builds glossaries?" (course day 5, slides p.28). 2 of 20 companies in the research have a consolidated glossary plus metric tree (board frame 5). The author's own catalog lived three years without one: "problematic, but we can't find a driver for it" (course day 4, transcript). It sits under "reserved for the mature" — "there is never resource for it, and it is not a starting point; when you get to it, it's a nice suit" (course day 6, slides p.100-101). Evidence from the room: a company with two metrics, "sales" and "revenue", where nobody can say which is correct (course day 4, transcript). Attempting it first "burns the political capital you need for everything else" (course day 6, transcript).

**What actually works:** Two routes, and the KB is explicit that the second inverts its own general advice. (1) Prioritise the physical layer — metric store, golden layer, core catalog features — which "sell far better" than "the whole company speaks one language" (course day 4, transcript; board frame 5). (2) Assemble **domain** glossaries bottom-up from tagged wiki pages where teams already describe their own methodology; "no company-wide glossary is needed first, and none exists: we have no common glossary" (course day 6, transcript). See [Where the themes disagree](#where-the-themes-disagree).

**Read:** `11_dg_program_themes/dg-program-roadmap.md`, `10_ai_era_themes/domain-knowledge-base.md`

### Semantic layer as an entry ticket

**Looks like:** A semantic-layer project is opened because everyone is talking about semantic layers. Both the DWH and the BI system fight to keep business logic inside themselves, and the project stalls between them.

**Why it happens:** Wedging a new system between layers of an already-running landscape is architecturally hard, and the pain it solves is real only at a specific scale.

**Evidence:** "It's fashionable to talk about semantic layers, but very few actually build them; people lived 15 years without them." The adoption paradox: "everyone already understands what it is, but very few have actually acquired one." (course day 1 and day 5, transcript). It is classed as a luxury, "reserved for the mature": "don't assume you must have it — it may simply not be affordable for you." (course day 6, slides p.100)

**What actually works:** The heuristic is a headcount question: "count the BI devs/analysts hand-coding the same business logic — the pain is real only when dozens of independent teams reuse the same core data." If they don't overlap much, keep writing SQL. Budget version for lower maturity: a metric tree bound to the glossary and catalog (course day 5, transcript; course day 2, transcript). One shape to avoid inside the layer itself: "a strictly hierarchical tree is exactly what you won't get" — a single global metric tree "carries nothing but beauty"; domain-level trees are the working unit (course day 5, slides p.30).

**Read:** `10_ai_era_themes/semantic-layer.md`, `11_dg_program_themes/dg-program-roadmap.md`

### Data-first cleansing

**Looks like:** An enterprise-wide cleansing or data-lake initiative starts from the data rather than from the use cases. It runs for years and produces a cleaner version of things nobody needed.

**Why it happens:** Cleansing scope is unbounded unless a use case bounds it, and "ensuring quality is expensive" — which is exactly why you classify first and right-size the framework.

**Evidence:** Per McKinsey up to 70% of cleansing effort is wasted; a large company burned hundreds of millions of dollars and 2+ years on enterprise-wide cleansing "because nobody knew which data served which use cases." (course day 3, slides p.9)

**What actually works:** "Don't try to boil the ocean hanging DQ checks on everything — the logic by which you define criticality is a core piece of any DG program." (course day 1, transcript). Cover the entire warehouse with three automatic checkers — record completeness, freshness, format — and require business checkers only from critical objects; that kit "may already be enough" (course day 4, transcript). Only ~30% of all data is critical at one large classifieds player (course day 4, slides p.99). And the honest ceiling: ~80% of critical data managed. "You can't properly manage even critical data to 100%, and I don't need 100%." (course day 6, transcript)

**Read:** `11_dg_program_themes/data-quality.md`, `11_dg_program_themes/dg-program-roadmap.md`

### Framework theatre

**Looks like:** A beautiful framework diagram, drawn before the pains analysis, presented as if it were a plan. Nobody can trace any box back to a business complaint. Eleven petals were copied because they were printed, which means committing to eleven programs.

**Why it happens:** The framework encodes conclusions; drawn first it becomes an aesthetic object. And importing one without an explicit deletion step is photocopying, not designing.

**Evidence:** The warning is printed in red on the slide and is "the most-ignored line in the deck": "this is not yet a DG implementation project — it is an abstract mock-up of how it works." (course day 1, slides p.115). The homework definition builds exclusion in: "structuring the data-management elements relevant for the company into a form practical for implementation, *while excluding all unneeded components*." (course day 1, slides p.122). On the canonical wheels: the DAMA Wheel is stamped "bad framework, explains nothing", and the Aiken Pyramid's phase logic — you cannot build layer N without layer N-1 — "looks like artificial logic, because we know a heap of examples where all of it happens in a different order" (course day 1, slides p.107-108). Read literally, the wheel "is a bill for eleven programs."

**What actually works:** Sketch it "somewhere at the implementation stage — when you have already understood the problems and drawn out the goals and the organizational model" (course day 1, transcript). Then run the deletion step, which recurs across the whole course as *the method*: the goals configurator is subtractive, the maturity canvas starts by greying out bricks you don't need, the strategy canvas says "delete everything that doesn't fit your company's maturity" (course day 2, slides p.57; course day 6, slides p.124). "If you cannot say aloud what you removed and why, you have not built a framework." And if you cannot staff a framework at all, Lean DG is the honest shape: 1 problem in one sentence, 1 domain, 3-10 datasets, 3 roles, 3 automated checks, one-page docs, weekly 30-min data office hours, quarterly expansion to the next 3 datasets (course day 1, slides p.56, 119).

**Read:** `11_dg_program_themes/dg-frameworks.md`

### Certifying reports before marts

**Looks like:** Certified dashboards sit on uncertified marts. The badge promises something the layer underneath cannot deliver, and the first bad number spends the badge's credibility.

**Why it happens:** Reports feel closer to the business, and are the natural place a BI leader starts. But trust flows upward from the data, not downward from the label.

**Evidence:** "For a BI report to be certified you need to certify the datamart under it; to certify the datamart you need data contracts, data checks, health — and a role model under that." Hence the sequence **marts → reports → metrics**, even though reports feel closer to the user. (course day 2, transcript; course day 3, transcript). "The report inherits the mart's trust, not the other way round." (course day 3, transcript). And the honest baseline behind any "we have a core layer" claim: 5,004 marts scored, 12 healthy — 0.2% (course day 3, slides p.115); a 20% core-penetration target delivered 2% in a year "without dedicated capacity and enforcement".

**What actually works:** Run the chain in order — certified marts → certified semantic-layer objects → certified dashboards and metrics → (soon) certified agents (course day 5, transcript). Make the status single-sourced: the catalog carries Core / Certified / Degraded badges with click-through to *why*, and the BI tool and metric store show **the same status**, "so trust is one process rather than three" (course day 3, slides p.117).

**Read:** `10_ai_era_themes/certified-core-layer.md`, `11_dg_program_themes/dg-program-roadmap.md`

### Wild West first, governance later

**Looks like:** Full domain autonomy is granted early, on the promise that federated governance will follow. It doesn't. Every team accumulates tech debt, the platform's influence is weak by design, and winning it back now means slowing TTM and taking freedom away.

**Why it happens:** Nothing in a maximally decentralized model penalizes creating nonsense on the platform. Governance that is supposed to grow alongside autonomy has no lever to grow with.

**Evidence:** The author on his own company: "in our case it was not like that — we had maximum Wild West immediately: decentralization, full freedom, and the governance activities never took root. We're still cleaning that up now." (course day 2, transcript). The structural verdict: "a decentralized approach with a high degree of domain autonomy from the start leads to chaos, and the governance that is supposed to exist alongside it does not take off. The platform's influence over the domains is very weak in this scheme by design." And the trap closing: "once you have let the domains go and they've sailed away, your ability to influence them starts to fall too." (course day 5, transcript). Self-assessment: "we say we have an à-la-data-mesh architecture, but of the four components we really only have one — the platform. No self-service, no proper domain structure, no federated governance." (course day 1, transcript). A participant's sharpened accusation, kept as a warning label: "so it's a crutch — we architected it wrong at the start and then propped it up with governance, hoping it'll work now." (course day 5, transcript)

**What actually works:** "Any data mesh must be built starting from centralization. Then, once the processes and approaches are built out, you decentralize the central platform team a little and hand out that freedom — because the engineers working in the domains will keep the platform culture we want from them." Seed the domains from the platform; don't seed the platform from the domains (course day 2, transcript). One specific thing must stay central even in a mesh: **base checker coverage and incident generation** — "delegating this to domains is a risky story — it just won't start" (course day 4, transcript). Environment design as the practical middle: separate archive / sandbox / prod, with sandboxes carrying lower documentation and health requirements but hard restrictions — no sharing objects outside the team, no schedules (course day 2, transcript). Once autonomy is already granted, the available instruments are indirect: program the platform's behaviour in the tooling, or catch inefficiency through product metrics — health scores, join counts, platform analytics (course day 5, transcript).

**Read:** `11_dg_program_themes/domains-and-data-mesh.md`, `11_dg_program_themes/dg-program-roadmap.md`

---

## Family 6 — Content, domains and scale

The structure and the content pool outgrow the process that was supposed to maintain them.

### Taxonomy paralysis

**Looks like:** Months of debate over the splitting criterion — by source system? by consumer? by business capability? — and zero names assigned. The discussion has moved to criteria and stopped producing people.

**Why it happens:** There is no correct partitioning principle to find. "You can stare at your data forever trying to find the right splitting criterion and regroup it this way and that — and it usually has neither meaning nor benefit."

**Evidence:** "The real value is just agreeing on a structure by common sense." (course day 3, transcript). The honest business objection the material lets stand unrebutted: "Okay, I appointed the HR director responsible. What is she supposed to actually *do*?" — domains are worth nothing until they carry duties; the value is in responsibility routing, not the picture (course day 3, transcript).

**What actually works:** The spreadsheet trick, stated exactly: open a sheet with three columns — domain, subdomain, responsible person. "As a rule, when you start filling in the responsible people, that is when you understand what the structure must be, because in real life it assembles itself." Fill names, not definitions (course day 3, transcript). And do the machine pass first: "today any LLM will draft a typical domain structure better than I will. Feed it your warehouse schema… I'd now solve this task not with consultants but with a chat model." Spend the human time on owners, not on boxes (course day 3, transcript).

**Read:** `11_dg_program_themes/domains-and-data-mesh.md`

### Domains without owners

**Looks like:** A published domain map with empty accountability cells. Or its shortcut cousin: no domains at all, object owners mapped straight onto departments — which survives exactly until the next reorg.

**Why it happens:** The map is cheap to draw and the owner column is expensive to fill, so it gets deferred. And "domains are very often 90-95% close to the org-structure split, and there is always the temptation to essentially not define any domains at all."

**Evidence:** A real audit across domain collections: 4-45% of assets with an owner assigned, 46-74% with no classification; a job-search platform's custom catalog at ~30% of objects with owners on an audience of 30 analysts — "a rather sad current situation" (course day 3, slides p.24; course day 4, slides p.87). The failure test is physical, not conceptual: a bad domain structure "simply won't stretch onto your people." If you cannot name one person per cell without an argument, the cell is wrong — merge it, split it, or delete it (course day 3, transcript). The related sovereignty fight: a domain declaring "these are our data, we do what we want with them, no governance for us" — shut down by their CIO with "these are not your data — they are the whole business group's data. It is our common cause." It needs an executive counter-statement, not a policy document (course day 3, transcript).

**What actually works:** Show the coverage number to the sponsor — it is the baseline, and it is supposed to be embarrassing (course day 3, slides p.24). Master domains and roles in the catalog with alerts (see [Silent washout](#silent-washout)). And phase it: "with 10-20 domains you will always find 2-3 proactive ones — start there; the rest get worn down by success posts" (course day 3, slides p.88).

**Read:** `11_dg_program_themes/domains-and-data-mesh.md`

### Badge decay

**Looks like:** Certifications were granted and never re-challenged. Nothing is revoked on a major change. The catalog has grown five or six public statuses. Deprecated objects have no reason, no deadline and no consumer notification attached.

**Why it happens:** Certification is designed as an event rather than as a status with a lifecycle, so entropy does the rest. Every extra public badge also raises the user's cost of choosing a source.

**Evidence:** "Certification must be continuously challenged and revoked on major changes, otherwise the badge loses its meaning." Few public badges (Promoted / Certified / Deprecated, or just Certified / Deprecated) so the user's cost of choosing stays minimal; the right to certify is strictly limited and certification is **not self-service**; deprecation ships with a plan: reason, deadline, consumer notification (course day 3, slides p.119). Badge design in practice: three colours, no more — blue Candidate, green Certified, red Degraded, where Degraded means certified but currently failing health requirements — "that is the fix queue, not a demotion" (course day 3, slides p.120). Diagnostic: "When was a certification last revoked? If never, the badge is decorative." (course day 3, slides p.119)

**What actually works:** Wire status changes into events other services consume, keep public status in the catalog and the operational work in domain cabinets, and fold data contracts into the health score rather than running them beside it, "so a break arrives as a signal rather than as a surprise" (course day 3, slides p.117, 119). Related failure worth naming: running the operational process *inside* the catalog — preparation, review and fixes belong in domain cabinets; mixing them "makes the catalog a workflow tool it was never designed to be" (course day 3, slides p.119).

**Read:** `10_ai_era_themes/certified-core-layer.md`

### Counting badges instead of traffic

**Looks like:** Certified object count rises every month. Share of queries actually landing on certified objects doesn't. Duplicates are still being created, and nothing intercepts the person at the moment they build another mart.

**Why it happens:** The badge is measurable in the certification team's own control; traffic is not. So the metric drifts to the thing you can move alone.

**Evidence:** "The programme's key metric is **share of traffic** going to core marts, not the count of certified objects: we need them to actually be used, and duplicates to gradually leave or be archived." (course day 3, transcript). Operational targets on the slide: share of user queries with 2+ joins 47% → 35% (2026) → 25% (2027); share of analyst queries hitting core tables 1% → 15% → 40% (course day 3, slides p.114). "Until reuse moves, 'data products' are a naming convention." (course day 5, slides p.114). The adjacent unbuilt piece the author flags on himself: the layer must "shout at you from every interface" — including where a person is about to create something new, "where it should first ask: maybe use this mart instead of building another one." Those nudge scenarios are named as still unbuilt: "we still have to work those through." (course day 3, transcript)

**What actually works:** Make share-of-traffic the north star and instrument reuse directly — count joins and reuse parameters of certified marts (course day 1, transcript). Copy the promotion surfaces vendors already ship: the certification badge in the **dataset picker** at the moment a report is created, and certification as a **search filter** rather than only a label on a card (course day 3, slides p.121). Quick win that moves the metric early: pre-mark the objects that already qualify (course day 3, slides p.116).

**Read:** `10_ai_era_themes/certified-core-layer.md`, `10_ai_era_themes/bi-content-management.md`

### The policy and documentation spiral

**Looks like:** Each new regulation, data type and self-service wave adds policies. Navigation gets worse, understanding drops, compliance falls. Meanwhile the strategy document you wrote went stale before it was socialized.

**Why it happens:** Policies accumulate monotonically because nothing archives them, and documentation decay is structural rather than a discipline failure — current, beautiful DG documentation exists only where a DG office is paid to maintain it.

**Evidence:** The spiral: more policies → worse navigation → lower understanding and compliance (course day 6, slides p.118-119). On decay: "it looks like I have to write it anew" — the author's own BI strategy went stale between writing and socialization; keeping documentation beautiful and current is "quite an expensive thing" (course day 5, transcript). And the LLM-era twist: "writing and updating policies became simple — detailed accents in the prompt and compile. What's left is to find those who will read them." Document *production* is no longer the constraint; readability and relevance are (course day 5, slides p.93).

**What actually works:** New policies only when needed, archive when stale, and push policy into tools "so the policy itself becomes unnecessary" (course day 6, slides p.118-119). Invert the enforcement ladder: from develop → monitor → enforce, to facilitate policy writing → prevention/warning → intervention → enforcement as a rare last resort reserved for genuinely critical things like personal data. **Guides / Guardrails / Gates**, where guardrails mean changing the environment so it is hard to do it wrong, on the principle "govern with the belief that most people want to do the right thing" (course day 6, slides p.116-117). Accept the shape of documentation without a DG office: "documentation exists per-component, not per-program — and that's fine" (course day 5, transcript). And ask: "Who reads the documents this framework asks you to produce? If nobody, the framework is asking for the wrong artefacts." (course day 5, slides p.93)

**Read:** `11_dg_program_themes/dg-frameworks.md`, `11_dg_program_themes/dg-program-roadmap.md`

### Checkers on columns instead of business rules

**Looks like:** Checkers hang directly off core-layer tables and columns. You cannot see which business rules exist for a given field, and the same rule is smeared across many objects.

**Why it happens:** Attaching a check to a column is the shortest path and requires no glossary, no business-term layer and no agreement. It is "a consequence of a high degree of freedom and a poor level of governance."

**Evidence:** The author's confessed anti-pattern from his own platform (course day 5, transcript). Requirements-to-checks traceability is what is lost: "checkers hanging off glossary terms would make requirements-to-checks traceable."

**What actually works:** No fully worked counter-move in the source material — the fix is named as a design direction (checkers bound to business terms) rather than as a delivered practice. What *is* delivered nearby: architectural checkers used as **certification criteria** rather than data checks — contract coverage, no open incidents, column metadata filled, optimal storage structure, resources used correctly. "This is roughly the tenth version of the methodology." (course day 3, transcript; slides p.115)

**Read:** `11_dg_program_themes/data-quality.md`, `11_dg_program_themes/dg-kitchen-research.md`

---

## Family 7 — AI-era specific

New assets, new speed, and the same governance debts — now compounding faster than the process that was supposed to absorb them.

### The AI checker flood

**Looks like:** An agent skill authors DQ checkers at machine speed. Coverage explodes. Within days incidents are flooding, and you need an incident-management agent — and then an agent to judge whether the checkers were any good.

**Why it happens:** The bottleneck moves one step downstream every time you automate. A skill that produces governed objects also produces the obligation to govern those objects; publishing it without the downstream loop relocates the problem rather than solving it.

**Evidence:** Checker creation grew ~50× at a large marketplace once an agent authored them, with data partners left only to approve (course day 3, transcript). Then the number that makes it concrete: a domain data steward covered **160 datamarts with business-logic checkers in one day**, work that normally takes ~3 weeks — "and these were real per-mart business checkers, not templates." The next bottleneck appeared immediately: "the checkers flooded incidents, which requires an incident-management agent, plus an eval-agent judging checker adequacy, because they can decidedly be fake — the level of business context may still be insufficient." (course day 6, transcript). The verdict: this "grows into a system that is expensive to support, which — if you believe in it and invest — probably gives a boost, but it's a luxury that not everyone can afford right now." And on how to pitch it: "the boost survives after subtracting validation costs, but it's smaller than the first emotions everyone feels." (course day 6, transcript). Hidden human cost: a full day of purely intellectually-loaded verification "hollows a person out much faster than when the operation was mixed with routine." (course day 6, transcript)

**What actually works:** Ship the skill together with whoever handles what it produces (course day 6, transcript). Plan the next roadmap stage for the bottleneck you are about to create (course day 6, transcript). And pitch the **net** number, after validation cost, not the first-week number.

**Read:** `11_dg_program_themes/data-quality.md`, `10_ai_era_themes/skills-hub.md`

### AI-filled metadata without a review gate

**Looks like:** Catalog coverage jumps. Every field has a description. Nobody confirmed any of them, and the descriptions are plausible enough that you cannot tell by reading.

**Why it happens:** Generated metadata creates "the feeling that you have everything." Unconfirmed content is worse than an empty row *because it looks finished* — the empty row at least tells the truth.

**Evidence:** Per top catalog vendors themselves: AI-generated metadata creates that feeling, "but quality demands human-in-the-loop review." (course day 4, transcript). And: ~75% accuracy on AI auto-documentation is "plausible enough to poison the layer if there is no gate" (`context-governance.md`). Everywhere review is required, "otherwise various undesirable events occur" — an observation drawn from companies a year ahead on adoption (course day 6, transcript).

**What actually works:** Tag output "requires review", or run a bot pinging the owner to confirm: "the benefit outweighs the risks, but we don't want to fill everything without owner confirmation." (course day 4, transcript). Read coverage only together with false-accept rate — coverage can be gamed by weakening the gate. The unresolved half, preserved as a live governance question rather than a settled one: one camp inside a large marketplace says re-checking auto-generated docs costs about as much as doing the mapping by hand; the other says "it doesn't make mistakes, especially with a second agent re-checking." Pick deliberately per domain; both answers are defensible (course day 5, transcript).

**Read:** `11_dg_program_themes/data-catalog.md`, `10_ai_era_themes/context-governance.md`

### Letting a machine write the "do not use for…" rows

**Looks like:** The AI drafted field descriptions and everyone declared documentation solved. Then the assistant confidently uses a metric in the one context where that metric is wrong.

**Why it happens:** AI does field descriptions decently. What it cannot produce is tribal knowledge — the caveat that exists only in someone's head because it came from an incident.

**Evidence:** The vendor-verified verdict, quoted approvingly: what AI cannot produce is the caveat "for this metric take this mart and these fields, but not for that one, because X isn't accounted for." (course day 4, transcript). "That sentence *is* the 'do not use for…' column." Per-object limitations are the one row of the AI-Ready Domain checklist a machine cannot write for you (course day 6, slides p.95).

**What actually works:** Make it a named human deliverable per key object: short meta (what it computes, what it is used for) plus limitations — period of applicability, migrations, "do not use for…" — mastered in the data catalog, owned by the BI Partner and the Metric Curator (course day 6, slides p.95). Diagnostic: "For your top ten objects, is there a written 'do not use for…' — written by a human?"

**Read:** `10_ai_era_themes/domain-knowledge-base.md`, `11_dg_program_themes/data-catalog.md`

### A third store called "the knowledge base"

**Looks like:** A new repository is created for domain knowledge, separate from the wiki and the catalog. It now needs its own owner, its own freshness process and its own migration story.

**Why it happens:** "The knowledge base" sounds like a thing, so a place gets built for it. A new repository means a new ownership problem.

**Evidence:** The checklist deliberately routes every row into one of exactly two existing systems: **narrative** knowledge (boundaries, how-to scenarios, adjacency, glossary) lives in tagged wiki pages; **object-level** knowledge (which objects are certified, per-object meta and limitations) lives in the data catalog. "No third store is created for 'the knowledge base' — it is assembled from the two systems that already exist and already have owners." (course day 6, slides p.95)

**What actually works:** Two master systems, six checklist rows, three named owners — Domain Owner (Head of Analytics), BI Partner (marts and dashboards), Metric Curator (metrics), which the author maps onto the classic pair: "two governance roles which, with a stretch, translate as technical data steward and business data steward." (course day 6, slides p.95; transcript). Test question: "Where is each row mastered — the tagged wiki space or the catalog? If the answer is 'a doc someone made', it is not in the pack."

**Read:** `10_ai_era_themes/domain-knowledge-base.md`

### Agents under a shared user account

**Looks like:** Agents run with a human's credentials. Queries multiply. When something goes wrong you cannot reconstruct which agent did what, and agent access is simply user access.

**Why it happens:** It is the fastest way to ship an agent, and identity design is invisible until the first incident or the first infra degradation.

**Evidence:** "Today agent access = user access", and "it is not very clear what was done by whom." Registration of agents bound to employees, with separate service-account-like credentials "but with character", is the stated next step (course day 6, slides p.96; transcript). Prod-access risk is real today: an agent can write code, push it, and review its own PR — "catch and block such cases, for now." Agent query share will spike — "agents join like crazy and not always elegantly"; expect infra degradation, plan agent request filtering, sampling and quotas (course day 6, slides p.96).

**What actually works:** The agentic-AI control set, the one place the course commits to a table: **Inventory** — a registry of all AI agents with a description of their data access; **Standards** — a policy for verifying agents before production; **Monitoring** — real-time observability of all agent operations on data; **RBAC+** — extended access control that accounts for AI agents; **Lineage** — tracing every data change made by agents; **Management** — a monthly governance council for AI-agent control (course day 6, slides p.93). Caveat the author attaches himself: agents supervising agents "smells slightly of loss of control" — flagged as an open question, not a solution (course day 6, transcript).

**Read:** `10_ai_era_themes/ai-governance.md`, `10_ai_era_themes/skills-hub.md`

### Governing the AI layer before the layer under it

**Looks like:** A domain knowledge pack is assembled over uncertified marts. Or agent certification is designed while marts, semantic objects and dashboards are still uncertified. The assistant retrieves company-wide because it doesn't know which domain the asker belongs to, and answers confidently outside its scope.

**Why it happens:** The AI layer is the visible, fundable one. The chain runs bottom-up — core → certified metrics → agent accuracy → self-service — and skipping a link produces plausible garbage rather than an obvious failure.

**Evidence:** "An AI analyst fed from thousands of uncertified marts produces plausible garbage." (`certified-core-layer.md`). Certification and good descriptions are **prerequisites** of the pack, not parallel workstreams (course day 6, transcript). The certification chain is explicit — certified marts → certified semantic-layer objects → certified dashboards and metrics → certified agents — and the author declines to jump it: "agents in principle deserve certification too, but for now it's a very shaky zone and we are not climbing into it — although it is already clear that the same sprawl is coming there soon." (course day 5, transcript). On retrieval scope: without a domain boundary attached to the asker, retrieval is company-wide and precision collapses — "the person may not say they are from the real-estate domain, but the agent already knows — and will search far more precisely inside real estate." (course day 6, transcript). The failure mode of a domain-scoped agent is confident answering outside its scope; the cheap fix is an explicit "for X, ask domain Y" map (course day 6, slides p.95). And the enabler most often missing: "without column-level lineage everything is rather sad" — a pack without it "will keep producing plausible but wrongly-joined answers" (course day 4, transcript).

**What actually works:** The numbers that justify the order: 20% vs 80% agent accuracy without vs with grounding in certified sources; 25% → 80% accuracy of a domain assistant before vs after the knowledge base is filled; score thresholds that worked — ≥50% of domain metrics healthy, ≥45% of dashboard views and ≥30% of mart hits landing on certified objects (`certified-core-layer.md`, `domain-knowledge-base.md`). Mine few-shots from support-chat history rather than inventing questions: a typical-question base is "the single strongest accuracy booster — literally a base of hints" (course day 6, transcript).

**Read:** `10_ai_era_themes/domain-knowledge-base.md`, `10_ai_era_themes/certified-core-layer.md`, `10_ai_era_themes/skills-hub.md`

---

## Where the themes disagree

Four genuine tensions in the source material. They are kept rather than resolved, because in each case both sides are argued from evidence.

**1. Blanket DQ coverage vs deliberately fewer checks.** `data-quality.md` states the coverage rule as a rule: cover the *entire* warehouse with three automatic checkers — record completeness, freshness, format — and treat everything else as business checkers on critical objects (course day 4, transcript). The same file's maturity signals then invert it as an "orthogonal signal — economics": once compute is charged per query, "every check = money" and the mature move flips to deliberately *not* blanketing, leaning on anomaly detection and keeping only narrowly-targeted manual checks. "Maturity here looks like fewer checks, not more." (course day 4, slides p.145). Both are in the same file. The reconciling variable is your compute billing model, and neither passage says so explicitly.

**2. Glossary-last vs domain-glossary-first.** `dg-program-roadmap.md` and `getting-started.md` file the business glossary under "reserved for the mature" and treat glossary-first as a capital-burning mistake. `domain-knowledge-base.md` names its own advice as an inversion: "This is a deliberate inversion of the course's own general advice… The domain knowledge base is what lets you skip the enterprise glossary and still ground an agent." The disagreement is about *scope* — enterprise glossary versus per-domain glossary assembled bottom-up — but the files do not use the same word for the two things, so a reader following only the roadmap will skip something the AI-era track considers a Stage-1 requirement.

**3. Business stewards never work — except where someone paid for them.** The dominant thesis across `roles-and-operating-model.md`, `getting-started.md` and `dg-program-roadmap.md` is categorical: "business people will never do hands-on steward work in any workflow you design." `dg-kitchen-research.md` preserves the counter-evidence in its "What only worked where…" section: one large bank hired business Data Stewards from the market as full salaried positions with a project portfolio, and it is "the only place where policy rollout visibly accelerated — rare, expensive, and the honest counter-evidence to 'second hat is enough'." Same for the IT-staff question inside `roles-and-operating-model.md`, where the best-practice slide says using IT staff as stewards is "effective short-term but not recommended as a standard operating model" and the author's counterweight is that in tech "the technical role is where all the meat is."

**4. Lineage is over-hyped vs lineage is the agent prerequisite.** `data-catalog.md` calls lineage "certainly the most hyped element", answers it with a hairball graph captioned "the phone-a-friend option is more reliable", and includes the author's self-disclosure: "our lineage is complex, badly visualized, and it seems we extract very little value from it in fact" — with the advice to check the logs and possibly discover nobody uses it. `domain-knowledge-base.md` and `llm-assistant-architecture.md` make column-level lineage a hard requirement: "without column-level lineage everything is rather sad", because it is what lets an agent construct correct joins across marts. The same file that deflates lineage also contains the reconciliation ("the one hard requirement is column-level"), but the two themes read very differently depending on which you open first.

**One consistency note, not a disagreement.** `11_dg_program_themes/dg-program-roadmap.md` and `11_dg_program_themes/maturity-and-metrics.md` carry real employer names for several peer cases that `dg-kitchen-research.md`, `data-catalog.md` and `roles-and-operating-model.md` anonymize ("a large fintech", "a ride-hailing arm of a large tech group", "a job-search platform"). The README states the convention explicitly: "no company names for internal practices". This file uses the anonymized form throughout, including for facts that appear named elsewhere in the KB.

---

## What this file does not contain

- **Failure modes from the BI+AI Strategy course only.** Several AI-era theme files mark sections as "not covered by this source" (pack format and versioning, golden-set eval mechanics, the AI-ready score as a composite index, traces as a governed asset class, skills-hub programme mechanics). Failures specific to those mechanics are therefore absent here.
- **Anything not already in the theme files.** This is a consolidation. Where the theme files have no counter-move, the entry says so instead of supplying one.
- **Benchmarks the author flagged as mythology, used as facts.** The $100-per-bad-record pyramid, the 1x→10,000x shift-left chart and the vendor productivity percentages appear here only as *examples of a failure*, with their flags attached.
