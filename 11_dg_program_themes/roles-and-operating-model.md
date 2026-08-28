---
theme: roles-and-operating-model
type: dg-program-theme
frames:
  - "3458764611453525295" # DG Role Structure
  - "3458764611453525317" # Organizational Model of DG (CDO Office)
  - "3458764612005175528" # Comparison of 5 operational models
  - "3458764611929480210" # Data Teams Modeling template
  - "3458764611929480215" # Scorecard: Fully Centralized
  - "3458764611929480216" # Scorecard: Centralized + matrix
  - "3458764611929480217" # Scorecard: Federated analytics
  - "3458764611929480214" # Scorecard: Fully Federated (data mesh)
  - "3458764611929480213" # BI org model 5: Hybrid + cross-functional team
  - "3458764611929480212" # D&A capability matrix (as-is / to-be)
---
# Roles and Operating Model

## What the board teaches
The DG role model splits into central DG Office roles (CDO, DG Lead, Coordinating Data Steward, tools development team) and business-side roles (Executive Sponsor, Data Owner, Business Data Steward, Data Custodian). The Executive Sponsor is a senior *business* leader with ultimate accountability for a domain; the Data Custodian is the technical counterpart (DBAs, data engineers, BI professionals) — and, notably, custodian duties largely mirror what those teams already do day-to-day, which is why (per the board's DG Kitchen research) custodianship adopts far more easily than business stewardship. Above the roles sits the organizational design question: the board compares five operational models for data/analytics teams — from Complete Centralization to Full Federation (Data Mesh) — scoring each on ~13 criteria across Process Efficiency, User Experience, and Business Value. The consistent pattern: centralized models win on consistency, cost balancing, security, one-version-of-truth, and people development but bottleneck the business; federated models invert this; matrix and hybrid-with-core-team models buy business proximity while retaining most central benefits at the price of High implementation complexity. A capability matrix template (org units × 10 BI/data capabilities, done/in-progress/to-be) turns the model choice into a transformation roadmap.

## Key objects
- DG Office roles: CDO, Data Governance Lead, Coordinating Data Steward, Tools Development Team (data catalog, DQ tool)
- Business roles: Executive Sponsor (domain accountability, policy approval, arbitration between domains), Data Owner, Business Data Steward, Data Custodian (access control, integrity, DQ resolution with steward, technical protection, master data versioning, change management)
- OCDO org chart: CDO → Technical Team / DG Officers → Data Scientists, Data Engineers, Business Areas, Developers, Trainers
- Five operational models: 1) Complete Centralization (complexity Low); 2) Hybrid Centralization with Matrix Management (High); 3) Hybrid Federation with a Core / Cross-Functional Analytics Team (High); 4) Partial Federation — data engineering stays central (Medium); 5) Full Federation / Data Mesh (Medium) — plus fit ratings for large enterprise, SME, digital product company (100+ data pros), startup
- Scorecard criteria ("how easy is to provide"): capacity balancing, content/data governance, security, one-version-of-truth, cross-functional reporting, navigation/UX, quality and standardization, dedup of effort, people development/retention; vs business alignment, request throughput, time-to-market, high-context insights
- Scorecard results: Fully Centralized — consistency easy, business proximity hard; Centralized + matrix — proximity improves to medium, keeps central benefits; Federated analytics — proximity easy, consistency degrades; Fully Federated (mesh) — proximity easy, nearly all consistency criteria hard
- BI org model 5 (hybrid + cross-functional analytics team): strong on governance and TTM simultaneously; amber on capacity balancing, standardization, people development
- Data Teams Modeling template: org-chart prototypes with Managing vs Contributing roles and shared-service blocks (infrastructure, core data model, golden layer, glossary/metric store, metadata, DG/DQ framework, security)
- Capability matrix: units (Finance, Service Lines, Business Lines) × 10 capabilities (self-service BI/ETL, own governed layer, harmonized landscape, DQ tooling, catalog, data products, ...) with done/in-progress/to-be statuses
- Related workshop template (Data Teams Modeling) — see [templates.md](../12_templates/templates.md)

## From the course (Data Governance Fundamentals, 6 days)

### The role that actually carries the load
- The author's ranking puts #1 on the Data Custodian — not the Data Steward, "not the DG Committee, God forbid", not even the CDO — and he repeats the thesis three times across the course: "The Data Custodian / Data Partner / Data Curator role is probably MORE important than the Data Steward role. And at minimum it comes first." (course day 1, slides p.61; course day 2, slides p.53; course day 6, slides p.99, p.105)
- The proof is the operations slide. Access control, technical DQ fixes, conformance of new data to the common model, master-data versioning with history, change management on databases, integrity via technical processes — closed with: "Recognizable, isn't it — this is the ordinary daily work of our teams, without any extra roles." (course day 3, slides p.60)
- Because it already *is* the day job, custodianship scales: it "can be distributed inside the data platform and the data roles of domain teams, covering the whole operational cycle". Stewardship, which is nobody's day job, does not. (course day 6, slides p.105)
- Same logic in DQ: a dedicated Data Quality Engineer role only appears where data directly generates money (trading, banks). Elsewhere a platform team of tech lead plus 2-3 engineers builds the tool and technical stewards in domains enforce checkers through existing roles — "no new role model arises". (course day 4, transcript)

### Why the business-steward model fails, and what business is actually for
- "The role of business in data management is exaggerated." Draping quality duties onto CFO/HRD-type people yields pushback; their role is nominal — sponsor, arbiter, requirements. "The whole trick of DG is finding the stewards/custodians/partners who will actually do the work." (course day 3, transcript)
- The board says it flatly: "The classic problem of the Business Data Steward — they engage poorly, they ignore their duties when those duties are combined with duties inside a business function." (course day 3, slides p.78)
- Business people will never do hands-on steward work in any workflow you design — at best they answer questions, approve the glossary and state DQ requirements, "nowhere does it work otherwise". In the DQ workflow this becomes a lane rule: the business steward reviews incidents for business-logic adequacy and nothing else. (course day 2, transcript; course day 4, slides p.119-120)
- Domain type decides whether the role exists at all: "In an HR domain it's probably pointless to look for such stewards. In a finance domain they may well exist — in banks financial analysts write SQL as a matter of course." (course day 3, transcript)
- The board's fixes all remove second-class status: make stewards full members of the data team and keep informing them even when unofficial; give authority and an escalation path; put steward KPIs into compensation and data responsibility into the job description; back them publicly from the top; run the program on visible success stories rather than control; build them a community with real feedback into their tools. (course day 3, slides p.82-84)
- The Executive Sponsor is real but delegated: "as a rule he never comes himself — he delegates a sensible business person, a finance analyst or a department head." What you get is arbitration between domains, approval of access matrices and terms, funding and prioritization — he is simultaneously your biggest report customer. (course day 3, slides p.68; transcript)

### Data Owner versus data object owner
- Exec-level "Data Owner" is a near-useless concept; the useful one is "data object owner" — the specific engineer, BI developer or analyst who created the object, because central teams and even domain BI partners "have limited hands — they cannot make the step instead of every single author". (course day 3, transcript)
- On the classic Data Owner responsibility wheel the author stamps three of eight petals in red: "In fact more than half of this is done not by the DO but by the DS." Beside it, three questions he actually asks: is your owner a business stakeholder, the team of the producing system, or the DWH engineers and analysts who create the objects? (course day 3, slides p.64)
- Against anointing directors of procurement or marketing: if a domain has a head of analytics, hang domain ownership there — "they have far more understanding, context and resource". (course day 1, transcript)
- The forgotten fourth party is Data Producers — backend teams whose systems feed the warehouse; the slide's headline is literally "They are often forgotten." Target state is a service model: responsible for delivery, correctness and freshness, accepting input quality requirements, answering for data contracts. One large bank is cited as having actually forced this on all its system owners. (course day 3, slides p.65; transcript)

### Recognize, don't invent — then name it for your culture
- Three staffing strategies on one slide: **Assign** ("they have no choice but to bear responsibility"), **Dedicate** ("those best suited will naturally take the place"), **Recognize** ("people already manage data — just informally"). The author's practice is overwhelmingly the third: in every domain running on common sense someone already archives, certifies, documents and checks lineage. Leave it to object creators and "it just turns into a dump". (course day 3, slides p.80; course day 1, transcript)
- The best-practice slide agrees and adds a caveat the author only half-accepts: using IT staff as stewards is "effective short-term but not recommended as a standard operating model", and the best stewards sit in business units with direct lines to business leaders. His counterweight: in tech, the technical role is "where all the meat is". (course day 3, slides p.81; transcript)
- Position versus hat: ~95% second hat; a whole-company dedicated steward team is about five people including catalog developers; dedicated salaried positions are "extremely rare and very fat". The exception on the board is a state bank that hired business stewards from the market to own block data strategy, DQ process rollout and a project portfolio — expensive, rare, "but it greatly accelerates the rollout of all the policies you want to distribute centrally". (course day 1, transcript; course day 3, slides p.52-53)
- Naming is not cosmetic. "Data steward" lands badly in Russian corporate reality; consulting for a timber and paper company the team decided to call them "data foresters" — adapting role names to your industry "is a good topic for a brainstorm". Large tech companies use "data partner" / "BI partner"; the author refuses the textbook word himself: "I don't use 'custodian' — domain data partner is more familiar." (course day 1, transcript; course day 3, transcript)

### The role card that works
The board's most concrete artifact here is the "BI Partner in a domain" card from a large tech company — copyable because it is written as a role, not a position. (course day 3, slides p.61)
- "This is not a separate position. It is a role taken on by an experienced BI developer (Team Lead BI, Senior BI, Middle+) who assumes additional responsibility inside the domain."
- Coordinates the domain's **certified report layer** and its SLA (performance, freshness, documentation coverage, visual design), and its **certified mart layer** — data products — with SLA on performance, freshness, checker coverage, documentation and reuse.
- Coordinates rollout of company-wide BI standards inside the domain: report development cycle, consumer work and release notification, object metadata in the catalog, update/checker/alert monitoring and DQ incident triage, usage analysis and archiving of unused objects. Represents the domain in cross-domain BI CoE initiatives and influences platform product strategy.
- The two clauses that make it real: "the BI Partner's OKRs include a BI maturity goal, agreed with the goals of the BI CoE and of the domain", and "BI CoE provides methodological, tooling and hands-on support for all activities within this role".

### Two roles or one — three real splits
- A large ride-hailing tech company splits what most companies mash together: a "BI governor" owning only certified reports and report standards, and Data Partners (systems analysts) owning core layers, marts, their certification, optimization and architecture. (course day 3, slides p.63; transcript)
- A neobank: formally no BI function, everything decentralized; a 50+ person cross-data team informally acts as BI CoE (templates, standards, courses, tools); a per-domain "CDO" owns domain data strategy while real governance is done by business data engineers with their team leads; density ~1 BI developer per 133 users. (course day 3, slides p.62; transcript)
- A real-estate classified runs three tiers — strategic; tactical, with a methodological committee (glossary, classification, rules) on the analytics platform and an architecture committee (catalog, quality monitoring, incidents) on the data platform; operational, inside product teams. Context: "they tried to designate data stewards and force them to do things, and not much worked out — so they created the Data Custodian role." Two years to get there, and the verdict is careful: "A good picture. If it starts up, great — but it will most likely break at the steward stage." (course day 3, slides p.71; transcript)

### Central capacity: coordinators, Core BI, and life without an office
- Coordinating data stewards are effectively project managers "who walk around nudging all the domains" and build observability tooling for them; usually data engineer or PM titles. The standalone "methodologist" rarely exists — the coordinating steward carries methodology plus keeping the DG wiki current. (course day 1, transcript; course day 5, transcript)
- A working central shape from a large telecom ecosystem: split the DG core team by expertise (catalog, metadata, reference data), each expert supporting many domain stewards — "at the bottom level everyone does everything; the middle level is split into cubes". (course day 1, transcript)
- With no DG office, the cross-functional Core BI team becomes the backbone — metric tree and glossary, criticality classification, golden layer, content management — "and it also takes on the data curator role in weak domains". You then never get one consolidated program: you assemble it per component, and documentation exists per component rather than per program. "And that's fine." (course day 6, slides p.105; course day 5, transcript)
- The breaking point is named: DWH/Platform leads absorb DG in their own zone until platform scale, where they "lack the authority, the interest and the resource to assemble the whole puzzle". That is when you form a DG project team and start an MVP — or don't, if drivers haven't reached critical mass. (course day 6, slides p.102)

### Funding the capacity
- Three models: business pays, platform pays, or a negotiated "platform tax" — each domain commits a % of existing capacity to governance. At the author's company the tax lands in roughly 70% of cases, "without any extra headcount or extra budget". (course day 2, transcript)
- One big-tech variant: six people carved out of an overloaded 20-person DWH team, zero new hires, overhead hidden inside product work — "to make your product's data a product, add one hour on top", blessed at C-level, the real cost being a mindset change nobody deliberately totals up. A large telecom ran the inverse: a separate top-management DG budget buying slices of product analyst teams. (course day 2, transcript)
- With no budget, ownership spreads at 0.2-0.3 FTE per person; centers of expertise per governance slice form naturally because nobody can own it all — "you find the right team, sell them the idea, land it in their goals". But someone must be the visionary coordinating the pieces, or the fragments never converge. (course day 5, transcript)
- The obvious alternative doesn't work: pushing BI development costs into business-unit budgets "never works anywhere". Report actuals of where central resource went and rebalance. (course day 3, transcript)
- Counterintuitive: once funded, you inherit the burden of proving payback. Where money is scrutinized hard it may be strategically better *not* to form a dedicated DG team, and to hide governance inside teams with a clearer raison d'être. (course day 5, transcript)

### Motivation and enforcement
- "Everyone who gets to formalizing stewards realizes the global problem was not defining them but motivating them — it's always a second hat, a role, not a position." (course day 1, transcript)
- The hard mechanism at a large tech company: ~20 domains with designated BI partners, and a competency matrix rewritten so "they cannot pass calibration without doing a defined set of governance activities" — "a carrot in front and a carrot behind". Capacity is protected by an administrative agreement that "tech debt includes data governance", reserving ~20% of their time. (course day 2, transcript)
- Top-down alternative: adopt a five-level DG maturity model and give each top manager an annual goal "my function reaches level X" — steward duties then cascade by themselves. Weaker variant: weave DG tasks into the OKRs of the people you depend on. (course day 3, transcript)
- Monthly ritual that works: a standing meeting with domain BI partners showing dashboards with per-steward metrics. "People see who is doing better and who worse — peer dynamics alone motivates, even before you have the right to set targets." Matrix subordination (functional lead plus domain manager) is the norm. (course day 5, transcript)
- Tom Sawyer in practice: gamified BI cleanup marathons with per-domain coordinators and prizes, whose participants are told afterwards that what they did was stewardship — that is how the BI-partner program was bootstrapped. (course day 3, slides p.85; transcript)
- Manipulation alone decays: "after the first few waves, if it doesn't map to real business problems, you'll have trouble." The author's own scar is a low calibration score for failing to communicate core-layer value to one domain stakeholder; the fix became in-domain demos plus outcomes stated in money or operations — "twelve marts became six, the critical path builds faster, fewer failures, fewer joins." (course day 3, transcript)
- Sequencing: not all data needs stewards, but all critical data must have one. "With ten or twenty domains you will always have two or three who understand you and are ready without persuasion. Start there; the rest get worn down by success posts." (course day 3, slides p.88; transcript)
- The honest ceiling, about his own company: no dedicated DG team, DG distributed with named drivers and shared goals, "I cannot force anyone — I can only build systems where doing it right is easier than not". Target ~80% of critical data managed, because "you can't manage even critical data to 100%, and I don't need 100%". (course day 6, transcript)

### Bodies, escalation, rituals
- Framing first: committees and offices are "not a mismatch — this is the standard management system of any enterprise program", nothing DG-specific. The DAMA stack (Steering Committee → Council → Office → steward teams → local councils) is "a maximum program. Without necessity, build a smaller-scale governance system." (course day 5, slides p.68, p.56)
- Reality check: real committees emerge only in transnationals or the largest domestic groups — "maybe two dozen companies max". Don't call them committees: "data management sync" sounds less bureaucratic and works the same. Local domain councils are realistic only where a transnational has country offices. (course day 5, transcript)
- Escalation benchmark kept as a balance check: 80-85% of data conflicts resolved at business-unit stewardship level, <20% reaching the DG Council, <5% the Steering Committee. Operational questions should not travel upward at all. (course day 5, slides p.65)
- Council hygiene: expect stewards to ask "should I keep attending?" after the very first meeting — "you must have a ready answer, and repeat it at every session". If someone's honest answer is "no" or "only sometimes", admit it. Never meet for the meeting's sake; close by listing what the day achieved. (course day 3, slides p.86-87)
- The packaging trick: in an HR-domain case an existing stream of DQ projects was relabelled "DG working group + committee" with sponsors invited from platform, HR and analytics — solely to make progress trackable upward. "Ordinary work, packaged so it can be tracked." (course day 5, slides p.64; transcript)
- The master system for domains and roles must be the catalog, not a spreadsheet, with alerts on assignment, re-assignment and onboarding — "otherwise people wash out silently and we discover nobody has been properly tending a domain for half a year". The companion artifact is a per-domain communication plan: domain × business owner / steward / SME × meeting type, channel, current and target frequency, day, duration, participants. (course day 3, transcript; slides p.44)

### Where the CDO sits, and who ends up leading
- In tech companies the CDO usually doesn't exist or is distributed across heads; the role fits traditional business, where one person can own DWH, BI, AI and DG wholesale. Where a CDO does exist, sponsorship is measurably easier. Placement then matters more than the title — business unit (fast start, shadow-IT risk, bias to that unit), inside IT (synced with services, drifts into technology and ends up opposing the business), or standalone under CEO/COO (independence and "no way to hide behind anyone's back", but resistance from both sides and a year-plus just to spin up). (course day 2, slides p.54; course day 5, slides p.66-67)
- Why DG so often lands on the BI lead instead: "BI is the interface between data and business" — the layer that simultaneously sees the weird data and hears the business asking why everything is wrong. Counter-view from a participant: data engineers understand best what's broken. (course day 2, transcript)
- The leader manifesto: DG leaders are "people who have known pain", because moving tectonic plates requires authority plus expertise in how the company really works — a change manager with mileage, a communicator, a person with will, "and ideally not yet burned out. A rarely encountered combination." (course day 5, transcript)
- Hiring that person externally is the trap: "You can take one from the market, but then you'll wait for him to become an old-timer, because before that nobody will let him seriously change their processes. You'll get sabotage and imitation." And the reason it must come from data at all: "Business will support you, but it will never postpone its own tasks for DG tickets. DG is a thing data/analytics leaders must arrive at themselves." (course day 6, slides p.104)
- The job description is mediation: every key DG initiative is cross-role, so "'we developed an approach but they don't follow it' — kindergarten". (course day 6, slides p.105)

### Shift-left, producers, and the centralization slider
- Shift-left is a role-model problem, not a tooling one: dashboard certification → forces mart quality → forces raw-layer quality → forces data contracts with source systems → forces product thinking on system owners. The obstacle, quoted from a participant: for backend teams "data is exhaust — they need to ship features, and the data… fine, take what there is." (course day 2, transcript)
- Career mechanics decide whether anyone wants the domain-facing seat: "business data engineer" and "platform data engineer" are different tracks with a ceiling on the former, so at the author's company business-impact work was deliberately normalized in engineering calibration at senior grades. (course day 2, transcript)
- The slider position — not the fashion — is the key strategic decision of the DWH/platform head: it determines your role system, your stack and even which architectures fit. Domains are needed even in a fully centralized model, just with far fewer expectations of them. (course day 2, transcript)
- The rule: build a mesh *starting from centralization*, because engineers seeded outward from the platform carry platform culture into domains. His own company did the opposite — "immediately maximum Wild West: full decentralization, full freedom, and governance activities never took root. We're still cleaning that up." Consultant view on the board agrees: start more centralized, let the center retreat into a facilitator role as the business matures — "very similar to self-service BI". (course day 2, transcript; course day 5, slides p.71)
- The permanent tension underneath: in the platform, engineers build a great platform but drift from the business; in a domain, one or two engineers are hard to manage — "under a single engineering lead they'd be more effective, churn less, develop better and stay longer". That is the whole point of platformization, and why the hybrid matrix is what everyone keeps re-inventing. (course day 2, transcript)

## Maturity signals
What separates stages on *this* dimension, drawn from the author's peer interviews and war stories rather than an abstract ladder.

- **Nobody has hours.** Roles exist in a document, are announced, and nothing happens. The peer status board records exactly this at a neobank: "regulating rules and imposing roles gets rejected by the culture; de-facto acceptance of the roles never started, nobody there began doing it". (course day 6, slides p.107; course day 3, slides p.72)
- **Roles exist, behaviour is reactive.** A ride-hailing tech company distributed engineers into domains, invented the Data Partner role, kept the rules — and still "failed to make the data partners proactive; they continued to act reactively". Assignment is not adoption. (course day 6, slides p.107)
- **The role is in the competency matrix with reserved capacity.** The step change is when it stops being goodwill: it enters review/calibration criteria and a named share of time (~20%) is protected by an agreed rule such as "tech debt includes governance". (course day 2, transcript)
- **Ownership coverage is a number you can say out loud.** Starting pictures worth showing sponsors: in one enterprise catalog only 4-45% of assets per domain collection had owners and 46-74% lacked classifications; a job-search platform ran at ~30% of objects with owners. (course day 3, slides p.24; course day 4, slides p.87)
- **The role registry lives in the catalog, with alerts on re-assignment.** The failure it prevents is specific: silent washout, discovered half a year later. (course day 3, transcript)
- **The business/technical split exists per domain.** Early stages have one blurred "steward". One real-estate classified reached an explicit Data Custodian role only after stewardship visibly failed — two years in. (course day 3, slides p.50, p.71; transcript)
- **Hat, badge, or position.** ~95% second hat; a dedicated company-wide team of ~5 including catalog developers is already unusual; market-hired business stewards with their own project portfolio sit at the far, expensive end. (course day 1, transcript; course day 3, slides p.52-53)
- **Bodies scale with the org, not with ambition.** No body → a monthly "data management sync" with per-steward dashboards → a real council → the full DAMA stack with local domain councils, which realistically exists only in transnationals. Building the top of that ladder early is a maturity *negative*. (course day 5, slides p.56; transcript)
- **Escalation ratios are healthy.** 80-85% settled at stewardship level, <20% at the council, <5% at the steering committee; operational traffic climbing upward is the symptom. (course day 5, slides p.65)
- **Funding has a name.** No budget and 0.2-0.3 FTE smeared → an explicit platform tax accepted by ~70% of domains → a top-management DG budget buying slices of analyst teams → a standing DG team (one delivery platform ran six: two tooling, two compliance, one AI/ML governance, one manager). (course day 2, transcript; course day 3, slides p.72; course day 5, transcript)
- **Spread across domains is moving.** You will always have two or three of ten-twenty genuinely engaged; maturity is whether that number grows via success posts and demos rather than mandate. (course day 3, slides p.88; transcript)

## Anti-patterns

- **The business data steward who was never going to do it.** Designing workflows that assume hands-on work from accountants and marketers. Fix: keep them for definitions, requirements and sign-off; move execution to the domain's data person. (course day 3, slides p.78; course day 2, transcript)
- **Owner on the org chart.** Anointing a CFO or procurement director "Data Owner" and waiting — more than half the wheel's duties are in reality done by the steward. Fix: head of analytics for the domain, object creator for the object. (course day 3, slides p.64; transcript)
- **Roles announced, hours nowhere.** Rules regulated, roles distributed, no capacity reserved, no review consequence. (course day 6, slides p.107)
- **The reactive data partner.** Role declared, nobody makes it proactive; it degenerates into a ticket queue. (course day 6, slides p.107)
- **Three VPs.** Elevating DG to group level with practice, methodology and platform reporting to different executives — competing centers of power, heavy spend, organizational dissolution, parts terminated. (course day 1, transcript)
- **Silent washout.** Role register in a spreadsheet, so departures never propagate; a domain turns out unattended half a year later. (course day 3, transcript)
- **Committee theatre.** Building the full DAMA body stack because the book has it. Fix: call it a data management sync and keep one body. (course day 5, slides p.56; transcript)
- **Kindergarten.** "We developed an approach but they don't follow it." Every key initiative is cross-role; without the leader mediating priorities, the approach is just a document. (course day 6, slides p.105)
- **Collective responsibility.** Quality owned by "everyone": developers don't monitor event emission, QA rarely tests data events, and nobody can say how good quality actually is. "Under collective responsibility there must be leadership and a managing process, otherwise collective responsibility equals irresponsibility." (course day 4, slides p.99)
- **Merging the lanes.** Letting business and technical stewards share the DQ incident workflow instead of one reviewing business-logic adequacy and the other doing the work. (course day 4, slides p.119-120)
- **Cost recharge.** Pushing central BI/DG cost into business-unit budgets. "Never works anywhere." (course day 3, transcript)
- **Metric ownership scattered to product teams.** A real-estate classified tried assigning all metrics to product teams and failed: responsibility is genuinely cross-functional, coordination costs more than teams will pay, and data analysts push back hard on writing methodology — it needs a business/systems-analyst skill set. Fix: key metrics to a steward, local product metrics to the analyst. (course day 5, slides p.31-33)
- **The imported DG leader.** "Nobody will let a newcomer seriously change their processes. You'll get sabotage and imitation." (course day 6, slides p.104)
- **Wild West first, governance later.** Full autonomy before processes and culture exist; winning influence back then means slowing TTM and taking freedom away. (course day 2, transcript)

## Questions to ask when designing this

- Who in this domain is *already* doing it — archiving, certifying, documenting, checking lineage? Can we recognize that person instead of inventing a role? (course day 1, transcript; course day 3, slides p.80)
- Does the domain structure stretch onto your actual people? The test is filling in the responsible-person column. (course day 3, transcript)
- Is this a position or a second hat? If a hat, what percentage of capacity is reserved, and by what agreement? (course day 1, transcript; course day 2, transcript)
- What happens at calibration if he doesn't do the governance work? If the answer is "nothing", you have a document, not a role. (course day 2, transcript)
- Who pays — business, platform, or a tax on existing capacity? And if you get a dedicated budget, are you ready to defend payback every year? (course day 2, transcript; course day 5, transcript)
- Which two or three of your domains will say yes without persuasion? (course day 3, slides p.88)
- When a steward asks after the first council whether he should keep coming — what is your answer, and will you repeat it every session? (course day 3, slides p.86)
- Is the master system for domains and role assignment the catalog, with alerts — or a spreadsheet? (course day 3, transcript)
- What share of your data conflicts is actually resolved at stewardship level? (course day 5, slides p.65)
- Where does the CDO sit — business unit, IT, or standalone — and does DG fall inside that perimeter at all? (course day 5, slides p.66-67; course day 2, slides p.54)
- Where are you on the centralization slider, and did you get there by design or by accident? (course day 2, transcript)
- Do the producers of the data — backend system teams — appear anywhere in your role model? (course day 3, slides p.65)
- Does the business have any lane besides approving? If sign-off is all you can name, stop building workflows that assume more. (course day 3, transcript; course day 4, slides p.119-120)
- Is your DG leader an authoritative old-timer with the will to move plates — or a recent hire you're hoping will become one? (course day 6, slides p.104; course day 5, transcript)
- Have you tried renaming the roles for your industry? (course day 1, transcript)

## Frames on the board
- [DG Role Structure](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525295)
- [Organizational Model of DG](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611453525317)
- [Comparison of Operational Models for Data Analytics Teams](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764612005175528)
- [Template — Data Teams Modeling (centralization vs self-service)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480210)
- [Scorecard — 1. Fully Centralized](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480215)
- [Scorecard — 2. Centralized with matrix management](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480216)
- [Scorecard — 3. Federated analytics](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480217)
- [Scorecard — 4. Fully Federated (data mesh)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480214)
- [BI org model 5: Hybrid + cross-functional analytics team](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480213)
- [D&A operating model capability matrix (as-is / to-be)](https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764611929480212)

## Links
- https://data-nature.com (source attribution on the comparison matrix)
