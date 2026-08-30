---
type: example
kind: strategy
company: Tairin
note: invented company; output of a full FORM run. The Russian original is the primary artefact; this is the same run in English, kept in step with it.
---

# Tairin — Data Governance strategy

A 12-month horizon with a three-year outlook. Produced by the `dg-strategy` skill (FORM, DG scope) on the dg-board-kb knowledge base. Revisited quarterly.

The company is invented, for an acceptance run of the template. Gaps in the facts are marked `[missing data]`.

---

# Summary

## Vision

A year from now the manager of a dark store gets the answer to their question themselves, in a minute, and that answer matches what the CFO sees. Not because an assistant appeared, but because underneath it sit agreed definitions, named owners and a confirmed core of reporting. The assistant is the last step, not the first.

## Problems

1. **Three definitions of a completed order** — operations, finance and marketing each count differently, divergence up to 4%, argued about monthly.
2. **60% of ad-hoc requests are repeats** — analysts answer them again because the answer is not left anywhere.
3. **A wiki of 400 pages, half of it stale**, and nobody knows which half; trust in it is lower than trust in asking in chat.
4. **Certification does not exist** as a concept: search returns everything, and choosing a source is a matter of luck.
5. **All engineering capacity is committed until year end.** Twelve engineers, ten months, zero slack.

## Solutions by stream

- **S1 · Definitions** — a registry of 25–40 key metrics with owners, and a dispute-resolution protocol. Problem 1.
- **S2 · Context for answers** — a question→answer base mined from support-chat history, plus notes on metric anomalies. Problems 2 and 3.
- **S3 · Core certification** — a status on marts and dashboards, ranking in search, sandboxes out of results. Problems 3 and 4.
- **S4 · Roles without engineers** — object owners drawn from the analysts, with time recorded in their managers' objectives. The condition the other three run on.
- **S5 · AI channel** — an assistant pilot on one domain after the gates are passed. The CEO's mandate.

## Goals

Format: now → year 1 → year 3.

- Key metrics with an owner and an approved formula: 0 of ~35 → 25–40 → all management metrics.
- Divergence on completed orders between functions: up to 4% → ≤0.5% → 0.
- Share of ad-hoc closed without an analyst: `[missing data]` → target after measurement → the majority of repeats.
- Consumption on certified objects: 0% → ≥50% → ≥80%.
- Assistant accuracy on the pilot domain: none → measured on a golden set → above the stated threshold.
- Maturity, average across 9 categories: 2.1 → 2.6 → 3.0.

## What we deliberately do not do

- **We do not buy a catalog** — we return to it when roles work in three domains.
- **We do not build a semantic layer this year** — we return when definitions are fixed and have owners.
- **We do not launch the assistant broadly** — a pilot on one domain only, and only after the gates.
- **We touch nothing that requires engineering capacity** — it is committed to the migration, and that is not negotiable.
- **We do not wait for the migration to finish** — three of five streams do not touch it at all.

## Effect

The leading zone is cost saving: analyst time lost to repeats, and infrastructure freed by hygiene. Revenue is not claimed. One line goes into the commitment — the reduction in repeat ad-hoc after the question→answer base ships, and only after the baseline is measured. Everything else is an expert estimate; details in section 06.

## What we need from you

**The COO takes ownership of definitions.** Not sign-off — arbitration: when operations and finance disagree, they decide, in writing, recording where each definition applies. Deadline: the first month.

This is the only role whose decision both sides will accept without escalating to the CEO. Without it stream `S1` does not start, and `S2` and `S5` fall with it: an assistant trained on three definitions of one metric reproduces the argument faster than people do.

## First step and the cost of doing nothing

Two actions in the first month: the conversation with the COO about arbitration, and a year's export of support-chat history to size the share of repeats. The second requires nobody's agreement and produces the baseline without which half the goals are a dash.

Doing nothing: the assistant ships by year end on the CEO's mandate, answers on three definitions, and loses the trust of 340 operations managers in its first month — which a second attempt does not recover. Analysts keep spending most of their time on repeats. The migration finishes and the company gets a new platform with the old mess in its definitions.

---

# 00 · Context

## External

Delivery and dark stores is a business of real-time operational decisions: where couriers are short, which SKU is dropping out, where unit economics have been eaten by promotions. Data here is not reporting but an operating instrument, and the decision is taken by a store manager rather than an analyst.

The industry has entered a phase where the advantage comes not from having analytics but from its availability at the lowest level of management. Competitors are in the same position: everyone has a warehouse and dashboards, nobody has self-service that works for a line manager.

Two trends change what is worth doing. First, producing governance documentation has fallen to zero cost, so policies stopped being a project and the bottleneck moved to execution. Second, agents arrived not as a revolution but by seepage — they already write SQL and pick apart data, so the question is not whether to launch an assistant but what it will answer on. The demo works for everyone; on a real schema accuracy is around 40%, and the failure mode is invention rather than silence.

## Internal

Five problems, each with a mechanism and a frequency.

**A completed order is counted three ways.** Operations count on handover, finance on settlement, marketing on confirmation. The divergence reaches 4% and surfaces at every monthly review: thirty minutes spent on whose number is right instead of on the number. There is no arbiter, so the argument reproduces.

**Repeats consume the analysts.** Roughly 60% of ad-hoc requests are variations on something already answered, but the answer is not left anywhere — it lives in a private chat between an analyst and a manager. The precise share is unmeasured `[missing data]`. The mechanism is simple: there is no place for an answer to land, so the next person asks again.

**The wiki is half stale, and which half is unknown.** 400 pages without owners and without review dates. A manager burned once does not go back and writes in chat instead — which produces the flow described above.

**Certification does not exist.** Data search returns everything: production marts, sandboxes, somebody's experiments. Choosing a source is a matter of luck, and two people asking the same question get different numbers legitimately.

**There is no engineering capacity until year end.** Twelve data engineers, all on the warehouse migration to a lakehouse: eighteen months behind, around ten ahead. This is not a priority that can be moved — it is a commitment to the whole company.

The last one determines the shape of the strategy: **the binding constraint here is neither money nor approvals but engineering hands.** So anything requiring an engineer is deferred by definition, and the strategy is built from what analysts, curators and object owners can do. The temptation to wait for the migration to end is strong and wrong: companies reach the consolidation point and start thinking retroactively, and a new platform with the old definitions is the same mess on more expensive hardware.

---

# 01 · AS-IS

Management is 340 store managers plus functions; power users are around 55 analysts; business dependence on data is high; the likelihood of industry transformation is high. The justified long-term level is **3.0**. The target for the year is **2.6**, on the "+1 level a year" rule wherever an executor exists. Three categories do not move: everywhere an engineer is needed.

`█` current level · `▒` gain this year · `·` not taken

| Category | Now | Target | Profile (0–4) | Confidence |
|---|---|---|---|---|
| Getting value | 3 | 3 | `██████████████████████████████····` | high |
| Data security | 3 | 3 | `██████████████████████████████····` | medium |
| Knowing your data | 2 | 3 | `████████████████████▒▒▒▒▒▒▒▒▒▒····` | high |
| Analytics governance | 2 | 3 | `████████████████████▒▒▒▒▒▒▒▒▒▒····` | high |
| People engagement | 2 | 3 | `████████████████████▒▒▒▒▒▒▒▒▒▒····` | medium |
| Strategic leadership | 2 | 2 | `████████████████████··············` | medium |
| Data governance | 1 | 2 | `██████████▒▒▒▒▒▒▒▒▒▒··············` | high |
| Quality management | 2 | 2 | `████████████████████··············` | **low** |
| Data architecture | 2 | 2 | `████████████████████··············` | high |

High confidence means an export or a count, medium means participants' word, low means inference from adjacent facts. There is one low: DQ coverage is known only on the payment perimeter, and no target is set for that category until an inventory is taken.

Demand is distributed favourably, which is rare. The CEO wants an assistant and will give a mandate. Operations managers want answers and will use anything that works. Analysts want to be rid of repeats — the most motivated participant in the programme, because they gain personally. Finance wants one number. Only the calendar is against: the engineers are busy.

**Chain breaks.** The knowledge base's core chain applies without adaptation: `core → semantic → context → agent accuracy → self-service`. Three breaks are named. The core is not certified, so "pick the right source" has no answer. Semantics are absent, and three definitions of one metric are the symptom. There is no context at all — neither a question→answer base nor anomaly notes — so an agent asked "why did it drop" will invent. The strategy is the repair plan for those three, not a coverage plan for a framework.

---

# 02 · TO-BE

The bet: **repair the chain from the bottom, but only with the hands that are free.** Core, definitions and context are analyst and curator work rather than engineering, and therefore feasible inside the migration rather than after it. The assistant is assembled last and as a pilot.

The ceiling for the year on moving categories is level 3 where an executor exists, and the current level where an engineer is needed. Three categories are frozen deliberately. Data architecture does not move: right now it *is* the migration, and interfering with it means interfering with somebody else's commitment. Quality management does not move beyond the payment perimeter: extending checks requires engineering work. Strategic leadership stays at 2 — moving it requires CEO time, and that time has been spent on the assistant mandate, which is a reasonable trade.

The target architecture is minimally sufficient: a registry of 25–40 definitions with owners instead of a semantic layer; a question→answer base assembled from chat history instead of a catalog; a status on marts and dashboards with ranking in search instead of a portal; an assistant on one domain instead of a platform. Operating model — section 05.

## Streams of change

Five directions. A stream is a direction of change with an outcome of its own; the projects inside are listed in section 04.

**S1 · Definitions.** Changes the fact that 25–40 key metrics acquire an owner, an approved formula and a recorded scope of application, and a dispute acquires written arbitration. Justification: this is the first problem and simultaneously the prerequisite of two other streams — an assistant on three definitions reproduces the argument faster than people, and certification without an agreed metric certifies the disagreement. Requires not one engineer. Outcome of the year: 25–40 metrics with owner and formula, divergence on completed orders ≤0.5%.

**S2 · Context for answers.** Changes the fact that the answer to a typical question stays in the system rather than in a private chat. Justification: 60% of ad-hoc are repeats, which makes this the cheapest source of both saving and agent accuracy; the field evidence says a question→answer base mined from support history is the strongest accuracy booster, and anomaly notes are the only thing preventing an agent from inventing a cause for a drop. Curatorial work; no engineering capacity required. Outcome of the year: a verified base of typical questions, anomalies on key metrics commented.

**S3 · Core certification.** Changes the fact that marts and dashboards acquire a public status, and search leads to the certified one first. Justification: without it "pick the right source" has no answer, and any assistant inherits the same lottery. In the AI era certification stopped being a ritual and became a prerequisite — the agent navigates to certified objects, and certification presupposes exactly the descriptions it needs. Order: marts, then reports, then metrics. Outcome of the year: the core is confirmed, consumption on certified objects ≥50%.

**S4 · Roles without engineers.** Changes the fact that core objects acquire named owners with recorded time — drawn from the analysts who already maintain those objects. Justification: the three streams above produce artefacts that must have a keeper, or they will go stale exactly as the wiki did; the custodian model works, the steward-alone model does not. Outcome of the year: core objects have owners with recorded time.

**S5 · AI channel.** Changes the fact that an operations manager gets the answer themselves. Justification: this is the CEO's mandate, and it can be neither ignored nor executed broadly — hence a pilot on one domain after the gates, with measured accuracy and a stated false-answer rate. The stream is last in order not out of caution but because its quality is entirely determined by the three before it. Outcome of the year: the pilot works on one domain, accuracy measured on a golden set.

---

# 03 · Metrics and goals

Metrics come before the portfolio: an initiative earns its place when it moves a named metric.

| Metric | Stream | Now | Year 1 | Year 2 | Year 3 | Downward adjustment for risk |
|---|---|---|---|---|---|---|
| Metrics with owner and formula | `S1` | 0 of ~35 | 25–40 | +operational | all management metrics | requires an arbiter; this is politics, not method |
| Divergence on completed orders | `S1` | up to 4% | ≤0.5% | 0 | 0 | **can legitimately fall and rise** — the only two-way metric in the set |
| Share of ad-hoc closed without an analyst | `S2` | `[missing data]` | target after measurement | — | the majority of repeats | baseline unmeasured; not committed |
| Verified question→answer pairs | `S2` | 0 | 150–300 | +domains | coverage of typical questions | adoption: curation competes with the ad-hoc queue |
| Consumption on certified objects | `S3` | 0% | ≥50% | ≥70% | ≥80% | needs search ranking — the single point where an engineer is required |
| Core objects with owner and time | `S4` | 0% | 80% | 90% | 90% | valid only if time is recorded in managers' objectives |
| Assistant accuracy on the pilot domain | `S5` | none | measured on a golden set | above threshold | more domains | depends on `S1`–`S3`; before them there is nothing to measure |
| Maturity, average across 9 categories | all | 2.1 | 2.6 | 2.8 | 3.0 | the ceiling at zero engineering capacity |

Anti-metrics: number of wiki pages, number of certified objects, number of assistant queries. All three grow independently of usefulness.

Four of the metrics above are counters that can only rise; they are labelled proxies out loud, because an unlabelled proxy is the polite version of metric theatre. There is one two-way metric in the set — divergence on completed orders; the share of ad-hoc joins it as soon as a baseline exists. Two goals without measurement are marked and are not committed.

---

# 04 · Initiatives portfolio

Each initiative belongs to one stream. Output is what physically exists when it is done; outcome is which metric from section 03 moves and by how much, by year.

| # | Initiative | Output | Outcome by year | Owner · prerequisite | Effort · wave | Risk and how it is managed |
|---|---|---|---|---|---|---|
| 1 | **Definition arbitration** `S1` | A named arbiter; a written protocol — how a dispute is raised, prepared, decided and recorded; the no-retroactivity rule | **1:** unblocks initiatives 2, 5 and 7 — without it their outcome is zero. **2–3:** measured by time to resolve a dispute, not by number of decisions | COO · their agreement is the entry condition of the whole strategy | Low in hours, high in political weight · first month | The arbiter agrees and does not decide. Control: a dispute older than two weeks escalates to the CEO automatically |
| 2 | **Registry of key definitions** `S1` | A registry of 25–40 metrics: formula, owner, scope of application; operational and financial definitions separated where they genuinely differ | **1:** 0 → 25–40 definitions with an owner; divergence on completed orders from up to 4% → ≤0.5%. **2:** operational metrics. **3:** all management metrics | Methodology analyst; each definition owned by a person from the function · initiative 1 | Medium in work, high in negotiation · H1 | Functions will not accept someone else's definition. Do not compel: separate the two explicitly and record where each applies |
| 3 | **Question→answer base from chat history** `S2` | A year's export of correspondence; 150–300 verified pairs of "typical question → mart, metric, caveat, link"; a process for adding from the current flow | **1:** 0 → 150–300 pairs; measuring the share of repeats produces the baseline for the ad-hoc metric. **2–3:** coverage of typical questions, share of repeats falls | Head of analytics; verification by definition owners · the chat export, which needs nobody's approval | Medium, entirely analytical · H1 | Machine-generated pairs look convincing and lie: auto-documentation accuracy is around 75%. A pair enters as a candidate; a human verifies |
| 4 | **Notes on metric anomalies** `S2` | Comments on deviations in key metrics; a rule that an unexplained anomaly stays on the list until closed | **1:** anomalies on key metrics are commented. **2–3:** the share of self-explained deviations rises | Metric owners from initiative 2 · initiative 2 | Low but continuous · H2 | People stop writing notes after a month. Tied to the metric owner, with unclosed items visible in the weekly list |
| 5 | **Certification of marts and dashboards** `S3` | Three statuses — candidate, certified, degraded; status on core marts, then on reports; object cards instead of wiki pages | **1:** consumption on certified 0% → ≥50%. **2:** ≥70%. **3:** ≥80% | Head of BI; confirmation by object owners · initiative 1 for metrics; for marts, no prerequisite | Medium · H1 | Certification as an event rather than a status with a lifecycle — then in six months it goes stale exactly as the wiki did. A review date in the card is mandatory |
| 6 | **Search ranking and clean-up** `S3` | Certified first in results; sandboxes hidden from search; interception at the moment a new object is created | **1:** locks in the result of initiative 5 — without interception, consumption reverts. **2–3:** growth in object count stopped | Platform team · **the only initiative requiring an engineer** — a window after the migration or a trade inside it | Low technically, high on resource availability · H2, conditional | The resource will not appear. Then the status stays visible on the object card and ranking moves beyond the horizon — which weakens the stream but does not cancel it |
| 7 | **Owners of core objects** `S4` | A registry of core objects with owners from among the analysts; a line about object upkeep in their managers' objectives; a review date on every object | **1:** 0% → 80% of core objects with an owner and time. **2–3:** 90% as the portfolio grows | Head of analytics; time agreed with function heads · initiative 1 | Medium, negotiation-heavy · H1 | Owners named, time not recorded — then it is a document, not a role. Test: what happens at calibration if the person did not maintain the object |
| 8 | **Assistant pilot on one domain** `S5` | A golden set of domain questions; measured accuracy and false-answer rate; an assistant available to managers of one domain; a stated acceptance threshold | **1:** accuracy measured, pilot running. **2:** above threshold, a second domain. **3:** more domains | Analytics product owner and head of BI · initiatives 2, 3, 5 passed | High · H2 | Launch on the mandate before the gates are ready. The lost trust of 340 managers does not return on a second attempt — the gates are signed off by the CEO in writing before work starts |

## Freeze order

`S1` does not freeze → `S2` is the cheapest and produces the baseline → `S4` → `S3` → `S5` freezes first, mandate notwithstanding. On losing a third of the resource, initiatives 4, 6 and 8 freeze and certification narrows from marts and reports to marts alone. The order is published in advance — otherwise a cut removes definitions and roles as "not producing results", when they are the condition of everything else.

Caveat: the rule "`S1` does not freeze" applies after the decision in the Summary. Before it, this is not a protected priority but an open fork.

## Kill-gates

The assistant does not leave the pilot domain until accuracy is measured on a golden set and the threshold is stated. We do not buy a catalog until roles work in three domains. We do not build a semantic layer until definitions are fixed and owned. We do not extend DQ beyond the payment perimeter while there is no engineering capacity. We do not add a metric to the registry without an owner.

---

# 05 · Operating model

## Roles

**Definition arbiter** — the COO. Resolves disputes between functions and records the scope of application in writing. About 2 hours a month, recorded in their objectives as the condition for launching the assistant they themselves want.

**Definition owner** — a methodologist from the function the metric belongs to. Formula, scope, defence of the definition in a dispute. Load arises with disputes; not continuous.

**Core object owner** — the analyst who already maintains that mart. Description, currency, review date, incident response. About 8% of their time, as a line in their *manager's* objectives rather than their own, because the manager allocates the time.

**Context curator** — an analyst on rotation, one per domain. Verifies question→answer pairs and keeps anomaly notes. About 4 hours a week for a quarter, then rotation.

The model is custodial: responsibility sits with whoever already maintains the object. Not one role requires a data engineer — the constraint from which the whole construction is derived.

## Bodies

No separate council is created. Instead, the existing weekly analytics-leads sync gains twenty minutes for disputed definitions and unclosed anomalies. The reason is not economy: a new body in a company where everyone is on the migration will not convene, and having convened, will turn into a status report.

What that slot does not do: it does not listen to migration status, does not approve architecture, does not sign off team plans. If in two quarters it has filled with reports, the slot closes and arbitration goes directly to the COO.

## Decision protocol

A definition dispute is raised into the registry by any participant. The curator prepares the case: two definitions, who applies each, the cost of the divergence in money or in hours. The decision is taken at the next sync and recorded with a date, an owner and a scope of application. There is no retroactivity — issued reporting is not recomputed, otherwise every dispute drags a retrospective behind it and disputes stop being raised. A dispute older than two weeks escalates to the CEO automatically: that is the protection against an arbiter who agreed and does not decide.

## Interfaces

The migration programme is not an interface but a boundary. The strategy is built so as not to touch it, and the single initiative requiring an engineer is marked conditional and pushed to the second wave. Product teams are consumers of the certified core; synchronisation is needed only on the date the status becomes visible in their tools. Finance is a party to the definitions dispute, not a customer of governance.

## Resources and artefacts

No new headcount: the work is covered by time quotas inside analytics. Engineering capacity is scarce, not money and not approvals, so the whole construction was selected on the criterion "feasible by analysts".

The objection "this is bureaucracy" is answered with arithmetic. Removed: a 400-page wiki, half of it stale, replaced by object cards with review dates; sandboxes leave search; ad-hoc repeats move into the question→answer base. Created: one definitions registry, a one-page dispute protocol, a base of question→answer pairs. Everything else lives in tools: status on the object, review date, mandatory owner field. No policies are written at all — producing text costs nothing, the bottleneck is finding a reader, and an artefact without a named reader does not enter this strategy.

Enablement is targeted: a one-page instruction for object owners and a walkthrough of two real disputes at the sync as a teaching case. There is no mass training — the routine has to be built into the tools rather than learned.

## Degradation path

If arbitration is not agreed, `S1` does not start and `S2` and `S5` lose their prerequisite. What remains is `S3` and `S4`: certifying marts and naming object owners, work that needs neither an arbiter nor an engineer. The document is renamed to a programme of analytical content hygiene and stops being called a DG strategy, and the CEO's assistant mandate is returned with a written explanation of why the launch is deferred. This is not a fallback plan but an honest boundary.

---

# 06 · Effect of the strategy

> **Expert estimate.** The structure of the effect and the orders of magnitude are working; specific sums require a precise calculation on the company's data. Below is what must be measured and who owns each figure. No line from here appears in the Summary as a headline number, and none is fit for an OKR before measurement.

Of the three real zones the leading one here is cost saving. There is no regulatory risk. Revenue growth exists in theory through the quality of operational decisions, but the metric belongs to operations, attribution is not agreed, and in the model that line weighs zero.

The board reads two numbers: an agreed estimate of possible losses against the cost of preventing them, and a positive decision is taken when minimal losses exceed maximal costs. Costs are known precisely and are small: no new headcount, everything reduces to analyst time quotas — 8% for object owners, 4 hours a week for curators, 2 hours a month for the arbiter. The upper bound is computed from the analytics payroll `[missing data: cost of an analyst-hour]`.

The mechanism differs by stream. `S2` provides the main line: the share of repeat ad-hoc multiplied by average time to answer and by the cost of an analyst-hour. It is also the only line with direct economics and therefore the candidate for the commitment. `S3` provides infrastructure and compute windows freed by removing sandboxes from production-like folders, plus the time no longer spent choosing a source. `S1` provides the cost of divergence: thirty minutes of the monthly review spent arguing about a number, plus reissued reporting. `S4` provides no effect and should not — it is a prerequisite. `S5` provides no effect in year one: a pilot on one domain pays back in trust, not in hours.

The leading method is labour saving, which is awkward, because that is the method that most often lies. Three mandatory corrections. Vendor productivity percentages are not used at all — we compute from our own measurement of repeats rather than from someone else's model. Saved time does not convert into output automatically: an analyst freed from repeats does not produce proportionally more, and finance will make that correction if it is not made first. And the defensible share is on the order of 5–7% of the claimed effect, not all of it.

The range is two-sided. In the pessimistic scenario arbitration is not agreed, the question→answer base is half-built, and search ranking gets no engineer — the effect is positive but small: certified marts and removed sandboxes. In the base case definitions are fixed, the pair base works, consumption has shifted to certified content — the effect is several times larger, and its leading part is freed analyst time. There is no optimistic scenario, deliberately: it does not survive contact with finance.

One line goes into the commitment — **the reduction in repeat ad-hoc**, and only after the baseline is measured. It is chosen not as the largest but as the only one where the chain from action to effect requires no argument about attribution: a question→answer pair either closed the request without an analyst or it did not. The decision on the committed fraction was taken here, before the meeting, not in it.

The estimate can be replaced by a calculation with five measurements, four of which are two weeks of work:

- share of repeats in ad-hoc over a year — head of analytics, from the chat export; the denominator of the main line and the baseline for the metric in section 03;
- average time to answer a typical request — head of analytics, timing a sample;
- cost of an analyst-hour — HR and finance;
- infrastructure and compute windows under the sandboxes — platform team;
- cost of divergence on completed orders: how many reissues of reporting and how much review time a year — finance, and this is closer to negotiation than to measurement.

Excluded and not returning: operational efficiency as a line of its own, innovation, accelerated decision-making — the last was closed in the industry a decade ago. Time-to-insight stays a goal in the metrics and does not enter the money model. Data quality is not an independent line of effect: it resolves into revenue or cost, and we draw that line ourselves before finance draws it.

---

# 07 · Risks

**The assistant is launched on the mandate before the gates are ready.** The most likely failure: the CEO's mandate exists, the date is announced, the gates are informal. Managed by fixing the gates in writing and having the CEO sign them off before work starts, rather than producing them in December as the reason for a miss.

**The arbiter agrees and does not decide.** Agreement is easy to obtain; decisions are unpleasant to take. Managed by automatic escalation of any dispute older than two weeks, written into the protocol rather than left to a curator's initiative.

**Context curators drown in the current queue.** Verifying pairs competes with ad-hoc, and ad-hoc is always more urgent. Managed by quarterly rotation, hours recorded in the manager's objectives, and by mining the first pairs from history rather than from the live flow.

**Search ranking gets no engineer.** High likelihood — it is the only initiative dependent on the committed resource. Managed by keeping the status visible on the object card, moving ranking beyond the horizon, and weakening rather than cancelling the stream.

**The migration slips right and absorbs what attention remains.** Managed by construction: three of five streams do not touch it, and that was checked when they were selected — the strategy is deliberately independent of the migration calendar.

**Definitions are fixed and not applied.** The registry exists and reports still compute the old way. Managed by making certification of a mart require a reference to a definition from the registry — the check is built into the status rather than left to discipline.

## Revision

The strategy is revisited quarterly, with a mandatory answer to three questions: what has been frozen, which of the five measurements is closed, and whether the date engineering capacity frees up has moved. A document without a stated next revision gets quietly replaced rather than updated.

---

# Appendices

Company portrait and interview answers: [tairin-company.md](tairin-company.md). The same run in Russian, including the rework log and the list of what this knowledge base had no material for: [tairin-strategy.md](tairin-strategy.md).

## What needs measuring for the diagnosis

1. **Share of repeats in the ad-hoc flow.** Source: a year's export of support-chat history. Blocks the main effect line and one goal in section 03. Needs nobody's agreement — the first action of the first month.
2. **Average time to answer a typical request.** Source: timing a sample. Blocks converting saved time into money.
3. **DQ coverage outside the payment perimeter.** The single low-confidence score in the scorecard.
4. **The date engineering capacity frees up.** Source: the migration lead. Determines whether initiative 6 falls inside the year's horizon at all.
5. **Cost of divergence on completed orders.** Source: finance. Closer to negotiation than to measurement.

## Rework log

The CDO judge ran three passes; the ninth dimension — the position a section takes — was applied for the first time.

| Pass | Was | Became | Closes |
|---|---|---|---|
| 1 | The assistant sat in the first wave, following the CEO's mandate | The pilot moved to H2 behind gates; the mandate is answered by fixing conditions in writing rather than by a date | order · blocking |
| 1 | The strategy assumed engineering work in four initiatives | One remains, marked conditional; the whole construction was rebuilt around analysts and curators | feasibility · blocking |
| 2 | Section 02 described a target state and took no side | The bet is stated explicitly — repair the chain from the bottom, but only with free hands; three frozen categories named with a reason each | **position** |
| 2 | The risk "the arbiter agrees and does not decide" was absent | Added together with its mechanism: automatic escalation of a dispute older than two weeks | risk honesty |
| 3 | Every metric in the set could only rise | A two-way metric added — divergence on completed orders; the rest labelled proxies out loud | rationality · metric theatre |

**Loop stopped:** pass 3 produced no new blocking findings.

**What the judge did not close.** The objection "a pilot on one domain will not prove scalability" is correct and unresolvable: scalability can only be proven by scaling, and scaling is behind the gates. Moved from the judge's list into the strategy's constraints — the year's perimeter is deliberately narrow, and that is written down.

**Bullshit judge pass.** Removed actorless constructions, intensifiers without numbers, paired abstractions, and aspirations standing in for initiatives with an owner.

## Where the knowledge base had no answer

| Topic | What was needed | What the base has |
|---|---|---|
| Governance during a platform migration | how to run a programme when all engineering capacity is committed for a year | nothing; the base assumes available engineering resource |
| Economics of analyst labour saving | a method robust to "saved time does not convert" | a warning and the 5–7% coefficient; no method |
| Context curation as a role | load, rotation, reviewer burnout | the role is named; there is no sizing |
| A golden set for an assistant | how to assemble it, how many questions, what acceptance threshold | the principle exists, the procedure does not |

**What worked without strain:** the chain `core → semantic → context → agent accuracy → self-service` applied without adaptation — the first run where that is true; the custodian model; refusing the catalog and the semantic layer as premature; the question→answer base from chat history; the certification order marts → reports → metrics.

---

*Produced by the dg-strategy skill (FORM · DG) on [dg-board-kb](https://github.com/alexbarakov/dg-board-kb). The company is invented; this was an acceptance run against the specification: 6–8 pages excluding appendices, minimum tables, portfolio always a table, context in two halves, streams with justification, word precision.*
