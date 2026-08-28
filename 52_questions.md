---
type: cross-cutting
purpose: Diagnostic question bank — what to ask, in what order, and what the answers mean
---
# Questions bank

This is not a questionnaire. Nobody fills it in; nobody scores it. These are probes — each one exists because the *shape* of the answer sorts a company into a different branch, and because the follow-up is where the real information lives. A question that cannot be answered wrongly is not on this list.

How to use it:

- **Triage first.** The opening block is ordered so that each answer routes the next. Stop when you have found where it actually hurts — usually three or four questions in.
- **Read the interpretation line, not the question.** The value of "who does this work on Monday?" is entirely in knowing what "we'll find someone" means versus "Ivan, 20% of his time, agreed with his lead".
- **Do not ask a question you already have the answer to.** If the participant shared a document, an assessment or a survey, mine it and state the derived answer for them to correct. Re-asking burns the twenty minutes.
- **Follow the flinch.** The questions in "The uncomfortable questions" are the ones people route around. When someone answers a neighbouring question instead, that *is* the finding.
- **Every answer is legitimate somewhere.** "We have no catalog and chats are enough" is a defensible mature position for a company with two central data teams. The bank discriminates between contexts, not between right and wrong.

Source tags in brackets point at the KB file the question and its interpretation come from: `[getting-started]`, `[frameworks]`, `[roadmap]`, `[domains]`, `[roles]`, `[dq]`, `[catalog]`, `[maturity]`, `[kitchen]`, `[core-layer]`, `[bi-content]`, `[semantic]`, `[context]`, `[domain-kb]`, `[skills-hub]`, `[ai-gov]`, `[literacy]`, `[SKILL]`. Questions marked `(derived)` are implied by the material rather than stated in it.

---

## The first 20 minutes — triage

Ask roughly in this order. Each answer narrows what is worth asking next.

**1. Is the *absence* of built-out data governance a current constraint for the company — or is the chaos simply not big enough to hurt yet?** `[getting-started]`
- *Good answer:* a specific thing that did not happen or shipped late because of data — an initiative blocked, a decision deferred, a close that ran long.
- *Worrying answer:* "everyone knows we need governance", or a list of things that are untidy but that nobody has missed. Survivable chaos accumulates for two or three years while the critical things still ship — a program built on it will neither be funded nor defended in a cut.
- *Routes to:* if there is no constraint, stop the strategy conversation and go to Common-Sense DG quick wins.

**2. Which pain did a named C-level person say out loud in the last quarter, and can you trace it to data?** `[getting-started]` `[kitchen]`
- *Good answer:* an incident or a complaint with an owner attached ("I can't trust the reports", "invoices are late"), ideally one you can decompose into workdays or money.
- *Worrying answer:* pains collected from the data team's own list. Business buys solutions to problems it actually feels; pains you discovered for them do not fund anything.
- *Routes to:* a named executive pain is your packaging; without one, question 5 becomes decisive.

**3. How many of the twelve DG-need statements apply to you — and is there real cross-functional data use?** `[getting-started]`
- *Good answer:* five or more, and named cases where one domain must consume another's data.
- *Worrying answer:* fewer than five, or domains that live in isolated contours. Cross-functionality is the trigger word: with no cross-domain use there are no losses and no case, and natural governance suffices.

**4. Which peer archetype do you resemble, and does your organization have a calm period?** `[getting-started]` `[kitchen]`
- *Good answer:* a recognizable comparable (bottom-up on the platform head's will; top-down through infosec; justified through metric discrepancies) plus at least a quarter without a reorg.
- *Worrying answer:* "we're unique", or process transformation every quarter. A permanent reorg cadence is the single clearest one-variable explanation for DG programs that never got off the ground — pick initiatives that fit inside one quarter, or don't start.

**5. Do you have a budget for this — and do you actually want one?** `[getting-started]` `[roadmap]`
- *Good answer:* an explicit position either way. "No budget, so we chain initiatives that pull each other" is a real strategy. So is "we deliberately keep governance inside teams that already justify themselves."
- *Worrying answer:* "we're going to ask for a program." Ninety percent of projects never get that budget, and a funded program inherits the burden of proving payback annually — in a money-scrutinizing company, taking the budget is the worse move.

**6. Who does this work on Monday — by name, or by role with hours?** `[SKILL]` `[roles]`
- *Good answer:* named people, a percentage of their week, and the agreement that protects it ("tech debt includes governance, ~20%").
- *Worrying answer:* a role model with boxes and no names, or names with no reserved time. Roles announced with hours nowhere is the most reliable predictor of a program that never starts.

**7. What share of your data objects have an owner?** `[domains]` `[catalog]`
- *Good answer:* a number, even an embarrassing one. Field baselines to compare against: 4–45% of assets with owners per domain collection; ~30% in one custom catalog with 30 analysts.
- *Worrying answer:* "everything has an owner in principle." Below half, you are at stage 1–2 whatever the program page claims.

**8. What share of consumption lands on objects you would personally be willing to guarantee?** `[core-layer]`
- *Good answer:* a traffic share, not a count of certified objects, plus a target. Reference targets: analyst queries hitting core tables 1% → 15% → 40%; queries with 2+ joins 47% → 35% → 25%.
- *Worrying answer:* "we have N certified marts." The badge is not the outcome. The default state of a mature multi-domain warehouse is thousands of marts and a single-digit certified share — 5 004 marts scored, 12 healthy, is a real published baseline.

**9. Can anyone on your data team answer, in metric terms, whether your data quality is good and how good?** `[dq]`
- *Good answer:* yes, with the caveat named — which numbers are gameable and what is published alongside them.
- *Worrying answer:* a dashboard exists and nobody can summarize it. "The tool exists = the process doesn't" is the recurring shape: a DQ module with two checks, used voluntarily, without control or goals.

**10. Who finds your incidents first — you, or the business?** `[dq]`
- *Good answer:* you do, and it is a tracked KPI ("share of incidents discovered by business"), with proactive announcement and a fix ETA.
- *Worrying answer:* the business, and there is no metric for it. This is the cheapest single indicator of whether DQ is a process or a tool.

**11. What is the share of your analysts' target tasks?** `[maturity]`
- *Good answer:* an instrumented number of your own. The author's runs 60–70%; industry research claims 29–36% of working time lost to bad data, and that gap is the point.
- *Worrying answer:* a vendor benchmark quoted as your baseline. Importing someone else's number sets an expectation you will then be held to.

**12. If you lose a third of the resource mid-year, what dies?** `[SKILL]`
- *Good answer:* a named freeze list, frozen from the bottom of the stack rank, that the participant can recite.
- *Worrying answer:* "we'd have to see." A strategy without a rehearsed cut does not survive the first budget review — it fails silently and everywhere at once.

---

## By theme

### Entry, drivers and the business case

- **Which of the three honest degrees are you — "not at all", "partially", or "full-scale"?** `[getting-started]` — Most consulting starts by assuming the third. "Not at all" (no maturity, no drivers) is a legitimate diagnosis. The archetype follows from the count of domains × business processes: one/many points at master data, many/one at financial reporting, many/many at the full corporate KPI + DQ + strategy set.
- **What are the two numbers your top managers will actually look at?** `[getting-started]` — There are only two: an agreed estimate of possible losses, and the cost of preventing them. A positive decision is taken when *minimal* losses exceed *maximal* costs. If the participant answers with a benefits wheel instead, they have not yet had the conversation they think they've had.
- **Which already-funded initiative could your work unblock?** `[getting-started]` `[kitchen]` — Naming one means you have packaging. Naming none means you are planning to march under the literal flag "Data Governance", which fails in ~95% of cases because the word reads as distant and secondary. Today's strongest disguise is AI.
- **What visible win can you ship in three months, and have you written its exit criteria on day one?** `[getting-started]` `[roadmap]` — Dashboard certification in three months is the worked example: it moved metrics *and* worked emotionally, which bought licence for more expensive initiatives. An MVP without written exit criteria does not end, it fades.
- **Are you counting only the direct economy, or also the castle in the clouds?** `[maturity]` — Infrastructure saved by deleting redundant objects is the only fully defensible direct economy in the whole field evidence. Faster onboarding, savings on audits and lawyers, accelerated decisions, fraud caught by DQ rules: all plausible, none buyable.

### Framework and scope

- **Can you draw the unformalized framework you already run?** `[frameworks]` — If the company governs data at all, a framework exists; the exercise is making it visible, not importing one. Someone who cannot draw theirs is about to photocopy somebody else's.
- **What are you deleting from the picture, and can you defend each deletion out loud?** `[frameworks]` — The deletion step *is* the method, and it recurs everywhere: the goals configurator starts by removing irrelevant goals, the maturity canvas by greying out inapplicable bricks. A framework with no visible exclusion list is not finished — it is a commitment to eleven programs.
- **Does it survive being executed out of order?** `[frameworks]` — Phase dogma ("you cannot build layer N without N−1") is artificial; real companies do it in any order. A framework that only works in sequence will break on the first dependency slip and take the credibility with it.
- **Who reads the documents this framework asks you to produce?** `[frameworks]` `[ai-gov]` — LLMs collapsed the cost of writing and updating policies. What is left is finding readers. If the answer is "nobody", the framework is asking for the wrong artefacts — and the standards spiral (more policies → worse navigation → lower compliance) is already running.

### Sequencing and roadmap

- **Which stream leads after launch — and did the driver pick it, or the methodology?** `[roadmap]` — All-in on compliance, or DQM, or certification, or literacy: this is not a methodological choice. A roadmap whose lead stream cannot be traced to the named driver was assembled from a template.
- **Are you certifying marts before reports, or the reverse because reports feel closer to the customer?** `[core-layer]` `[roadmap]` — The report inherits the mart's trust, not the other way round. Certifying reports first is the natural instinct of a BI leader and the most common inversion in the chain.
- **What is this strategy deliberately *not* doing this horizon, and what gate would open it later?** `[SKILL]` `[frameworks]` — A consciously excluded stream with a named gate is a stronger artefact than one included because it is the trend. Silence on the obvious candidate (usually AI) reads as an oversight and invites it back through the side door.
- **What bottleneck will the thing you are about to automate create next?** `[dq]` `[skills-hub]` — The canonical case: one steward covered 160 datamarts with business-logic checkers in a day instead of three weeks; the checkers immediately flooded incidents, requiring an incident agent *plus* an eval agent to judge whether the checkers were fake. Plan the next roadmap stage for the bottleneck you are about to create.
- **Is procurement on the critical path?** `[roadmap]` — Catalog market analysis is supposed to start *before* the official program start for exactly this reason. If the first six months of the roadmap are a tender, the roadmap is a purchase order.

### Domains and operating model

- **Where does your self-service line sit?** `[domains]` — "The whole question is where you draw the point of your self-service, of your data platform." Everything downstream — expectations of domains, role model, RACI, even which architectures fit — follows from that one answer. A participant who has not decided it is not yet designing anything.
- **Can you name a person for every cell, today, without a meeting?** `[domains]` `[roles]` — The failure test is physical, not conceptual: a bad domain structure "simply won't stretch onto your people." If the owner column stalls, the cell is wrong — merge it, split it or delete it. This also makes the exercise cheap: it fails fast and visibly.
- **What do you actually expect this domain to do?** `[domains]` — Glossary approval and requirements only, or ingestion, cleaning, transformation, DQ, reporting and documentation? Write the list before drawing the map. Domains are worth nothing until they carry duties; the value is in responsibility routing, not the picture.
- **Which entities are genuinely cross-domain, and which core domain will own them?** `[domains]` — Client, employee, and the other "middle" entities with many inputs and many use cases. A cross-domain entity belongs to a core domain with its own owner, not to whichever consumer domain shouted first.
- **Are you at the growth stage or the consolidation point?** `[domains]` — Freedom is cheap in growth and expensive afterwards. Once domains have sailed away, winning influence back means slowing time-to-market and taking freedom away. Answer this before arguing about mesh.
- **Where are you on the centralization slider, and did you get there by design or by accident?** `[roles]` `[domains]` — The slider position, not the fashion, is the key strategic decision of the platform head. "We went straight to maximum Wild West and governance never took root" is a common and expensive accident. The rule: build the mesh *starting from* centralization, so engineers seeded outward carry platform culture with them.

### Roles, capacity and motivation

- **Who in this domain is *already* doing it — archiving, certifying, documenting, checking lineage?** `[roles]` — Three staffing strategies exist — assign, dedicate, recognize — and the third works far better than the other two. In every domain running on common sense somebody already does this informally. Recognizing them costs nothing; inventing a role costs a year.
- **Is this a position or a second hat? If a hat, what percentage of capacity is reserved, and by what agreement?** `[roles]` — ~95% of stewardship is a second hat. The step change is not the definition but the protection: a named share of time (~20%) backed by an explicit rule such as "tech debt includes governance".
- **What happens at calibration if he doesn't do the governance work?** `[roles]` — If the answer is "nothing", you have a document, not a role. The hard mechanism that works is a competency matrix rewritten so the person cannot pass calibration without a defined set of governance activities — a carrot in front and a carrot behind.
- **Who pays — business, platform, or a tax on existing capacity?** `[roles]` — A negotiated platform tax (each domain commits a % of existing capacity) lands in roughly 70% of cases without new headcount. Pushing central BI/DG cost into business-unit budgets "never works anywhere" — if that is the plan, the plan is the risk.
- **Does the business have any lane besides approving?** `[roles]` `[dq]` — Business people will answer questions, approve the glossary and state DQ requirements; they will not do hands-on stewardship in any workflow you design. If sign-off is all you can honestly name, stop building workflows that assume more. In the DQ lane this is exact: the business steward reviews incidents for business-logic adequacy, and nothing else.
- **Do the producers of the data — the backend system teams — appear anywhere in your role model?** `[roles]` — They are the forgotten fourth party. For them "data is exhaust — they need to ship features." A role model that stops at the warehouse boundary cannot deliver shift-left, which is the longest and most valuable chain you have.
- **Is your DG leader an authoritative old-timer with the will to move plates — or a recent hire you're hoping will become one?** `[roles]` `[kitchen]` — Fast benefits correlate with a respected internal veteran running the MVP. Hire from the market and you wait years for tenure while getting "sabotage and imitation" — this is one of the few single-variable predictors in the whole research set.

### Data quality

- **Do you have DQM as a process? What does it actually consist of? Who participates, and who drives it?** `[dq]` — The author's own diagnostic pair, asked verbatim. An answer made of tool names is the diagnosis: ~90% of DQ systems in the wild are a self-written checker engine plus incident dumping, and the feeling that you therefore have quality management never appears.
- **What share of your data have you declared critical, and by what logic?** `[dq]` — A factor rating (regulatory 3, compliance 3, accounting 2, operational 1, threshold >10) or the owner simply picking — both legitimate, neither is not. Reference: ~30% of all data declared critical at one large classifieds player. No criticality logic means you are about to boil the ocean, and up to 70% of cleansing effort is wasted when nobody knows which data serves which use case.
- **Which layers of the test pyramid do you actually have — and which are you deliberately fine without?** `[dq]` — Contracts (producers) → unit tests (DE) → pipeline checks (DE) → observability (DataOps) → DQ monitoring (stewards) → functional tests (DQ testers) → ad-hoc tests (everyone). The lower, the cheaper and more reliable. Not all layers are mandatory — but the missing ones should be a decision, not a discovery.
- **Where is the boundary between the central DQ team and the domains, and does your tool assume the same boundary?** `[dq]` — Fix this *before* building tooling: federated and centralized are two different approaches to the tool. One thing must stay central even in a mesh — base checker coverage and incident generation. "Delegating that to the domains is a risky story — it simply won't start."
- **What fluctuation range is normal versus an incident, and which business person actually said so?** `[dq]` — This is the entirety of business's contribution to check design, and it is the part most often skipped. Without a stated baseline, every check is either noise or theatre.
- **What does one check cost you to run, and should that change how many you have?** `[dq]` — On pay-as-you-go compute "every check = money", and the mature move inverts: deliberately not blanketing, leaning on anomaly detection, keeping only narrowly-targeted checks. Maturity here can look like *fewer* checks.
- **Can your coverage metric be moved by writing trivial checks — and what do you publish alongside it?** `[dq]` — The pair is mutually gameable: raise coverage and apparent quality falls (more checkers detect more), so the cheapest way to look better is deleting checkers; but coverage itself is easy to hack with trivial checks. Publishing only one of the two is the anti-pattern.

### Data catalog

- **Do you have enough *aggregate* maturity to launch a catalog and get value from it at all?** `[catalog]` — Catalog value is hostage to self-service BI, data products, contracts, ownership and DQM, and unlocks only as those mature. If they are immature, the resource belongs there. The sharpest framing: "the benefit of a data catalog is often lower than the cost of producing and supporting it."
- **What is your baseline search time today, and how will you measure it a year from now?** `[catalog]` — Nobody has that kind of time tracking, which is why the practical answer matters: mine catalog logs for search sessions with a success criterion, and parse help chats for the baseline. Reference benchmark: an ad-hoc's data communication averages ~3–4 hours today against a ~15-minute target with a certified catalog plus assistant, and the case works from ~100 analysts.
- **Which single golden path are you choosing for conversations, knowledge base and querying — and what are you switching off?** `[catalog]` — UX fragmentation is the structural risk: a built-in messenger nobody uses, a second knowledge base competing with the wiki, a second querying surface. Two of everything means the data team supports two of everything.
- **Lineage: where do you stop with integrations, and who actually needs it and why?** `[catalog]` — Lineage is the most hyped element and often the least used. If you have logs, dig into them — you may discover nobody opens it. Invest against two concrete jobs only: incident impact analysis, and pipeline/critical-path optimization. The one hard requirement is column-level.
- **To the vendor: do you bring methodology — glossary process, target processes, default object-card templates — or a bare box?** `[catalog]` — "It all depends on the customer" is the red flag. Ask the same way about pricing: is the core licensed whole, what is priced separately (connectors per source type, steward seats, admin seats, instances), and what still works if infosec allows metadata only, with no samples and no profiling.
- **If you are building: who owns the UX, and for how many years?** `[catalog]` — The hidden cost is not the metadata store, it is the product work — CustDev, adoption, feature delivery. A catalog looks like "a very simple product" to data engineers, which is exactly why open-source builds end as ugly metadata stores. And in the fight for engineers between platform streams, the catalog loses; every catalog surveyed shows a fading trend.

### Certified core layer and BI content

- **If a mart is Certified, who carries the warranty, and what exactly happens when it breaks?** `[core-layer]` — Certified must imply default guarantees: owner and contacts, freshness SLA, base DQ thresholds, lineage, change rules as a contract. The object is "taken under platform warranty." If nobody can say what breaks and who answers, the badge is decoration.
- **When was a certification last revoked?** `[core-layer]` — If never, the badge carries no information and users are back to asking a colleague. Certification must be continuously challenged and revoked on major changes; deprecation ships with a reason, a deadline and consumer notification.
- **Does the same status appear on the mart, the dashboard and the metric — or does each tool have its own idea of trust?** `[core-layer]` — Trust should be one process, not three. And keep the badge count small: every extra public status raises the user's cost of choosing a source; three (Candidate / Certified / Degraded) is already generous.
- **At the moment someone creates a new mart, does anything suggest an existing one?** `[core-layer]` — If nothing intercepts the person at creation time, reuse stays an aspiration and the Jevons paradox wins: cheaper production means more objects and complexity eats the gains. The certified layer has to "shout at you from every interface."
- **Who will actually build this layer, and are they product people?** `[core-layer]` — In ~80% of companies the core layer is built by data engineers, "who by nature are not product people." Expect product-ownership problems and budget for them, or name who supplies the product ownership.
- **Do you know your own content funnel?** `[bi-content]` — All dashboards → non-sandbox → actually in use → healthy → recommended key reports. Reference shape: ~13k dashboards → ~90% outside sandboxes → roughly a third in use → a few hundred key reports; metrics ~15k → ~30% important → ~10% in use. Having the funnel at all is a maturity signal; the strategy is growing the "healthy ∩ recommended" inner join.

### Semantic layer and the meaning of metrics

- **Count the BI developers and analysts hand-coding the same business logic — do they actually overlap?** `[semantic]` — The decision heuristic for whether a semantic layer is a need or a fashion. The pain is real only when dozens of independent teams reuse the same core data; below that, keep writing SQL. The layer is explicitly "reserved for the mature" — it may simply not be affordable at your maturity, and the budget version is a metric tree bound to the glossary and catalog.
- **Are you promising a strict metric tree, or metric families with governed links?** `[semantic]` — "A strictly hierarchical tree is exactly what you won't get." Real metric graphs are overlapping clouds with tangled cross-links; a single global tree "carries nothing but beauty". Domain-level trees are the working unit — govern the links, not the hierarchy.
- **Which of your metrics are key — cross-team, in the business model, externally reported — and which are local product drivers?** `[domains]` `[roles]` — Assigning *all* metrics to product teams has been tried and failed: responsibility for a metric is genuinely cross-functional, coordination costs more than teams will pay, and analysts push back hard on writing methodology. The working split is key metrics → steward, local product metrics → analyst, one domain pair per year.

### Context, domain knowledge and agents

- **Which of the six AI-Ready Domain checklist rows does this domain actually have — and who is named on each?** `[domain-kb]` — Boundary and owner; certified marts/metrics/dashboards markup; per-object meta with limitations; typical "how do I…" scenarios in the user's own words; adjacency links; domain glossary. Rows without a named owner are aspirations. Rows mastered in "a doc someone made" are not in the pack.
- **Does the agent know which domain the asker belongs to before it retrieves anything?** `[domain-kb]` `[context]` — Domain identity is a retrieval filter, not documentation hygiene: the asker may never say they are from real estate, and the agent filters anyway. Without it, retrieval is company-wide and precision collapses.
- **Where do your few-shots come from?** `[domain-kb]` — If the answer is not "support-chat history", you are inventing questions users never asked. A base of typical question → which mart/metric/report, with the catch and a worked link, is the single strongest accuracy booster available — "literally a base of hints."
- **For your top ten objects, is there a written "do not use for…" — written by a human?** `[domain-kb]` `[catalog]` — This is the one row a machine cannot write. AI does field descriptions decently; what it cannot produce is the tribal-knowledge caveat ("take this mart and these fields for this metric, but not for that one, because X isn't accounted for"). That sentence is what prevents confident wrong answers.
- **Do you have column-level lineage and a base of proven joins, or are you expecting the agent to guess the join?** `[domain-kb]` `[llm-arch]` — "Without column-level lineage everything is rather sad." A knowledge pack over an ambiguous join graph keeps producing plausible but wrongly-joined answers, which is the worst failure mode: the query ran without error and silently returned a wrong number.
- **Where is the list of agents and skills running against your data today, and who owns each one?** `[skills-hub]` `[ai-gov]` — Agents and skills are a new asset class needing exactly the old content-management loop: registry, ownership, certification, reuse of the good, deletion of the bad. If no list exists, agent access currently equals user access and nobody can say who did what.
- **Which of your skills produce new governed objects — checkers, descriptions, marts — and who handles the output volume?** `[skills-hub]` — A skill that produces objects also produces the obligation to govern them. Publishing the skill without the downstream loop moves the bottleneck rather than removing it. Ask for the net productivity number after validation cost, not the first-week number.
- **Which is cheaper for this domain right now: verifying the generated pack, or writing it by hand?** `[domain-kb]` — A genuinely open question with two defensible camps — one says re-checking generated docs costs about as much as doing the mapping by hand, the other says a second agent re-checking is enough. What matters is that the participant picked deliberately rather than drifted.

### Metrics, ROI and maturity

- **Which of the three real ROI zones is yours — revenue growth, cost saving, or regulator risk?** `[maturity]` — Those are the only three worth searching. If the honest answer is "operational efficiency" or "innovation", you have air. And check the premise: government bodies and some regulated structures do not think in cost reduction at all, in which case compliance and the management vertical are the lever, not ROI.
- **Which of your metrics are outcomes, which are proxies, and which are activity counts — and can any headline number go *down* for a good reason?** `[maturity]` — If none can, you are counting activity: numbers of standards, glossary terms, owners, stewards, policies. None of those can legitimately fall. Proxies are usable, but only when labelled proxies out loud; unlabelled, they are the polite version of metric theatre.
- **What are you putting in the "% productivity improvement" cell, and who agreed to it?** `[maturity]` `[catalog]` — Every vendor calculator makes one move: assume a percentage, multiply by headcount and salary. Vendors put 23–26% there; provable reality is 5–7%; and saved time doesn't convert to output anyway. Copy the evaluation logic, not the numbers.
- **Who will be credited with the benefit — governance, the platform, or the business team that shipped the metric — and have you negotiated the attribution share in advance, in writing?** `[maturity]` — Attribution is a negotiated parameter, not a measurement. Its *existence* matters more than the percentage. In big tech, value is never attributed to "data governance" at all; it is ascribed to the products governance runs inside.
- **Has the business ever asked you for money — or did they ask you to make the pain stop?** `[maturity]` `[dq]` — Often nobody wants quality converted into money: "just rid me of this pain, make it not every day." Then the metric belongs in *their* units, and the one that lands is "days without incidents in critical reporting."
- **Which bricks on the maturity map did you grey out as not applicable, and could you defend that list to your CEO?** `[maturity]` — The first move on any maturity canvas is subtractive. If nothing was greyed out, the assessment hasn't started — someone else's target state was imported wholesale. Related: maturity ≠ complexity; a simpler centralized platform can be perfectly mature.
- **Are your domain or department maturity scores in anyone's annual goals?** `[maturity]` — This is what separates a maturity model used as an instrument from one used as a slide. Models work when the company *appropriates* one and embeds per-domain scores in top management's yearly goals; otherwise it is bureaucracy and the sceptics in the room are right.

---

## The uncomfortable questions

These surface what people avoid saying. Ask them late, ask them plainly, and let the silence run.

- **What share of the claimed effect are you prepared to commit to as *provably* saved over a year, two, three?** `[maturity]` `[getting-started]` — The question that kills weak cases, and it always arrives after the total. Decide the number before the meeting, not in it. The downside is personal: an approved program becomes a personal liability, "a defeat in management's eyes — or in the end, get fired."
- **If you got the budget, are you ready to defend payback every year — and would you rather not have it?** `[roles]` `[roadmap]` — Taking money inherits the proof burden. Sometimes the stronger play is leaving governance hidden inside teams that already justify their existence, precisely so there is no line item to cut.
- **What is your honest monthly money effect, and would you show that number to anyone?** `[maturity]` `[kitchen]` — The author disclosed his own figure in the course as a warning — a monthly effect that looked very small against the scale of his company, and one he hesitated to show anyone. The figure itself is withheld here; the expectation-setting is the point. A truthful DG ROI rarely looks impressive next to product economics. That is a property of the domain, not of your arithmetic.
- **Is your governance a retrofit for an architecture decision you got wrong?** `[domains]` — The accusation worth keeping, from a workshop participant: "so it's a crutch — we architected it wrong at the start and then propped it up with governance, hoping it'll work now." The honest answer is often yes, and often it could not have gone otherwise at the growth stage. Saying so is stronger than pretending the plan was always this.
- **Is your platform team hiding behind the data catalog?** `[catalog]` `[kitchen]` — A headline finding of the peer research: buying a tool reads as progress and defers the hard organizational questions — ownership, criticality, contracts, the role model — indefinitely. If the catalog answers every governance question you ask, the role model does not exist.
- **Is the honest description of your program "the tool exists, the process doesn't"?** `[dq]` `[kitchen]` — Applied to a DQ engine with two checks, to a catalog in prod with view-only input and ~10% adoption, to a good tool "used voluntarily, without control or goals". A deployed tool proves procurement maturity and nothing else.
- **Who is the single point of failure — one sponsor, one leader, one enthusiast?** `[roadmap]` — Programs die three quiet ways: sponsor rotation (a program depending on one executive has a half-life equal to that executive's tenure), organizational dissolution (practice, methodology and platform reporting to three different VPs), and silent budget cuts. Ask which of the three is closest.
- **Did you publish an approach and call it done?** `[roles]` `[frameworks]` — "We developed an approach but they don't follow it" gets a one-word verdict: kindergarten. Every key initiative is cross-role; the leader's job is mediation, not publication.
- **Which of your objects has no owner — and how long has that been true without anyone noticing?** `[roles]` `[catalog]` — The specific failure is silent washout: role registries kept in spreadsheets do not propagate departures, and "we discovered nobody had been tending a domain for half a year." The catalog, with alerts on assignment and re-assignment, is the only master system that prevents it.
- **Are you calling it data governance to an audience that will never buy that word?** `[getting-started]` `[frameworks]` — Even "certification" smells of bureaucracy to some audiences. If the participant cannot restate the whole program without the term, they have not found the pain it attaches to.

---

## Questions to ask yourself before proposing anything

Run these on your own draft, in the voice of a sceptical CDO who has killed two DG programs and paid for a third. Verdict per dimension: `ok` / `weak` / `blocking`. Prefer one killer question over ten fair ones. `[SKILL]`

- **Priority — if I fund only the top third of this portfolio, does anything of value still ship?** Follow with: which single initiative, removed, breaks the rest? And why is the first thing first — evidence, or comfort?
- **Order — does anything here depend on something scheduled later?** Where do two initiatives compete for the same people, and who wins *in writing*? Does the sequence survive a two-month slip in one dependency?
- **Feasibility — who exactly does this work on Monday, by name or by role with hours, and is that time carved out or hoped for?** Then the one that hurts: what has this organization already failed to do that looks exactly like this?
- **Complexity — which initiative is under-estimated by an order of magnitude?** What is the hidden migration, integration or political cost nobody wrote down? Is anything here a two-year program dressed as a quarter?
- **Concreteness — can I point at three sentences a team could start executing tomorrow?** Which "outcomes" are actually activities? Which targets have no baseline, and therefore no meaning?
- **Value — what does the business feel in six months, in their words, and what do I say to the CFO in one sentence?** If we do nothing, what actually breaks, and when?
- **Risk honesty — what is the most likely way this fails, and is it in the register?** Which risk is written softly because it is politically awkward? What is deliberately not being done, and is that written down?
- **Optimism — is any target here more than +1 maturity level in a year without a named reason?** Dedicated capacity, a funded platform change, or a regulatory deadline are reasons; ambition is not. The base rate to quote yourself: a 20% core-penetration target delivered 2% in a year when capacity was not carved out.
- **Honesty of numbers — did I invent anything?** Every gap should be a visible `[missing data]` marker naming the missing fact and its source, collected into a "what needs measuring" list. A strategy with five honest gaps is stronger than one with five invented numbers — and a vague target ("improve quality") is a hidden gap, not a soft one.

---

## If you can only ask five

1. Is the *absence* of built-out data governance a current constraint for the company right now?
2. Who does this work on Monday — by name, or by role with hours?
3. What share of consumption lands on objects you would personally be willing to guarantee?
4. Who finds your incidents first — you, or the business?
5. If you lose a third of the resource mid-year, what dies?
