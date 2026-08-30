---
type: example
kind: strategy
company: Alverta Insurance Group
note: invented company; output of a full FORM run. The Russian original is the primary artefact; this is the same run in English.
---

# Alverta Insurance Group — Data Governance strategy

A 12-month horizon with a three-year outlook. Produced by the `dg-strategy` skill (FORM, DG scope) on the dg-board-kb knowledge base.

The company is invented, and deliberately chosen as an awkward test: a regulated industry, a legacy estate, a failed MDM attempt. Gaps in the facts are marked `[missing data]`.

---

# Summary

## Vision

A year from now, both the customer and the number in the regulatory report can be proven — where they came from. Not everywhere, but on a narrow perimeter and all the way through: retail in one country, and the regulatory reporting contour. A single view of the customer and an answer to the supervisor are not two programmes, as the board believes, but one: both rest on identity and on owners of definitions.

## Problems

1. **No customer identity** — four records in four systems, three reports with different numbers.
2. **No owner of definitions** — actuaries and BI disagree on loss ratio; there is no arbiter.
3. **No traceability** — a supervisory finding has already been received.
4. **A theatre council** — three years of minutes occupying the place a working body would take.
5. **Content overhang** — 2 400 reports against 300 in use.

## Solutions by stream

- **S1 · Roles with hours** — re-founding the council; a registry of owners with recorded time. Problem 4; unblocks the rest.
- **S2 · Identity** — identity resolution for retail individuals in one country. Problem 1.
- **S3 · Definitions** — a registry of 30–50 metrics with owners and a dispute-resolution protocol. Problem 2.
- **S4 · Traceability** — tracing report fields, intake control on broker files, DQ on the key contour. Problem 3.
- **S5 · Hygiene** — inventory, archiving, confirmation of the core. Problem 5.

## Goals

Format: now → year 1 → year 3.

- Regulatory-contour objects with an owner and recorded time: 0% → 90% → 90% (the perimeter's ceiling).
- Definitions with an owner and an approved formula: 0 of ~40 → 30–50 → all management and regulatory metrics.
- Report fields traceable to source: `[missing data]` → 100% of the finding's perimeter → the whole regulatory contour.
- Retail individuals with resolved identity: 0% → one country → four countries.
- Unused reports archived: 0% → ≥60% → a continuous process.
- Maturity, average across 9 categories: 1.4 → 2.0 → 3.0.

## What we deliberately do not do

Every refusal is lifted by its own gate, not by a change of mood.

- **We do not buy a data catalog** (discussed for three years) — we return when roles work in three domains.
- **We do not do full MDM** with a golden record for all lines — we return when the retail contour is accepted by the lines.
- **We do not touch architecture or legacy** — the decision to retire the mainframe sits outside the horizon.
- **We do not declare AI a goal for the year** — we return when identity and definitions work.
- **We do not rewrite policies** — producing text costs nothing; the bottleneck is execution.

## Effect

The leading zone is regulatory risk: the finding has already been received, so the event has happened and does not need forecasting. Second is cost saving. Revenue through cross-sell runs on someone else's metric and weighs zero in the model until an attribution share is agreed. Costs are known more precisely than the effect: no new headcount, everything reduces to time quotas.

One line goes into the commitment — the infrastructure saving from archiving reports. The rest is an expert estimate requiring precise calculation; seven measurements with named owners are listed in section 06.

## What we need from you

**The Chief Risk Officer takes the chair of the re-founded council.** Agenda: disputes about definitions and prioritisation; status reporting is abolished. Deadline: the first month.

This is the only role with leverage: the supervisory finding has been received, and only that role can demand. **If the decision is not taken**, the strategy shrinks to S4 and S5 and is renamed; building identity without a mandate holder means repeating 2022. In return they get a documented answer to the supervisor, traceability that removes personal exposure at the next inspection, and the right to prioritise data work — which today is smeared across the architecture committee.

## First step and the cost of doing nothing

Two actions in the first month, with everything else waiting on their result: the conversation with the CRO about the chair, and a technical reconnaissance — is traceability achievable through the mainframe, which carries 40% of the book.

Doing nothing: a second supervisory finding on the same subject turns the conversation into "by when will you fix it", on dates we do not set; the cross-sell programme starts on data where the numbers can be computed but not proven; and the three-week close firefight repeats every quarter and grows with the book.

---

# 00 · Context

## External

Insurance is built on data: pricing, reserving, loss ratio. And yet the industry norm is data smeared across systems of different generations. Competitors are in the same position; the winner is whoever assembles identity first.

The supervisor presses harder on traceability than on accuracy: "explain where this number came from" arrives before "prove that it is right". That changes the priority — provability outranks cleanliness.

Producing governance documentation has fallen to zero cost, so the bottleneck moved to execution and policies stopped being a project. Catalogs stopped being the entry ticket — buying one has become a durable way of not answering the question about roles. AI does not touch the company yet, but it sets a clock: the later the foundation is assembled, the more expensive the entry when the board asks about agents.

## Internal

Four problems, each with a mechanism and a frequency.

**The customer is not one customer.** One person exists as four records in four systems, and a human reconciles them by hand. This breaks on every cross-sell calculation: three reports give three numbers, because each analyst matches records their own way. The board sees the divergence monthly and has stopped discussing the metric itself.

**Definitions have no owner.** Actuaries and BI compute loss ratio differently, and the divergence reproduces every cycle because there is no person whose definition counts. The dispute arises not from ignorance but from the absence of an arbiter.

**The number is not connected to its source.** A field in the regulatory report cannot be shown to an inspector as a chain back to origin. This has already cost a supervisory finding — an event, not a forecast. The quarterly close runs three weeks of firefighting because reconciliation is manual.

**The council exists and changes nothing.** The DG Council has kept minutes for three years. It is not merely useless — it is harmful: it occupies the political space a working body would take, and any proposal to create a new one reads as a duplicate.

A fifth, less painful and cheap to fix: 2 400 reports of which roughly 300 are opened.

The constraint that determines the shape of the solution: **what is scarce is not budget but approval throughput.** Everything goes through the architecture committee. So we optimise the number of approvals rather than the cost. And the legacy will not go away — 40% of the book lives on a mainframe for at least five more years, so any plan beginning "after the legacy is retired" is a plan for later.

---

# 01 · AS-IS

Management is hundreds of decision-makers; power users number around 140; business dependence on data is high; the likelihood of an industry data transformation is moderately high. The justified long-term level is **3.0**. The target for the year is **2.0**, on the "+1 level a year" rule for categories where both resource and mandate exist. A target of 3.0 in a year is unreachable — not because of money, but because of approval throughput.

`█` current level · `▒` gain this year · `·` not taken

| Category | Now | Target | Profile (0–4) | Confidence |
|---|---|---|---|---|
| Data security | 3 | 3 | `██████████████████████████████····` | high |
| Getting value | 2 | 2 | `████████████████████··············` | medium |
| Strategic leadership | 2 | 3 | `████████████████████▒▒▒▒▒▒▒▒▒▒····` | medium |
| Knowing your data | 1 | 2 | `██████████▒▒▒▒▒▒▒▒▒▒··············` | high |
| People engagement | 1 | 2 | `██████████▒▒▒▒▒▒▒▒▒▒··············` | high |
| Analytics governance | 1 | 2 | `██████████▒▒▒▒▒▒▒▒▒▒··············` | high |
| Data governance | 1 | 2 | `██████████▒▒▒▒▒▒▒▒▒▒··············` | high |
| Quality management | 1 | 2 | `██████████▒▒▒▒▒▒▒▒▒▒··············` | **low** |
| Data architecture | 1 | 1 | `██████████························` | medium |

High confidence means an export or a count, medium means participants' word, low means inference from adjacent facts. There is one low score: DQ coverage is known only where the regulator demanded it, and no target is set for that category until it is measured.

Demand is uneven, and that determines whom to lean on. The board wants cross-sell and receives three reports with different numbers. Risk and compliance live in a quarterly firefight and have already taken a finding — the most motivated consumer of governance in the company. Actuaries do not consider themselves part of the problem: "it is BI that has something wrong". Business lines feel no pain, their local reports work — so the programme cannot be built on their goodwill.

> **A caveat on method.** The knowledge base's core chain — `core → semantic → context → agent accuracy → self-service` — is written for a company with an AI ambition. Alverta has none. The working analogue is `identity → definitions → traceability → regulatory trust and cross-sell`.

---

# 02 · TO-BE

The bet: **narrow and finished rather than broad and half-done.** One chain from an identified customer to a traceable number, working for retail in one country and for the regulatory contour.

The ceiling for the year on each moving category is level 2 — "works on the key perimeter", not "works everywhere". The expectation of "everywhere" in a company with three generations of systems is unreachable at any price within a year.

Three categories of nine stay where they are, deliberately. Security holds on its regime and needs no attention. Getting value — the actuarial function is strong. Architecture is frozen against the temptation: the legacy does not leave within the horizon, and an attempt to "clean up the systems first" will consume a year of approvals.

The target architecture is minimally sufficient: an identity layer for retail (identity resolution with a traceable rule, not full MDM); a registry of 30–50 key definitions instead of a 340-term glossary; traceability on the finding's perimeter; a certified core of the ~300 reports actually in use. Operating model — section 05.

## Streams of change

| Stream | Why now | Outcome of the year |
|---|---|---|
| **S1 · Roles with hours** | nothing downstream works without owners; the theatre council zeroes out trust in the topic | key objects and definitions have named owners with recorded time |
| **S2 · Identity** | a board ask; break 1 | cross-sell is computed one way for retail in one country |
| **S3 · Definitions** | break 2; removes the actuary–BI conflict | 30–50 metrics with an owner and an approved formula |
| **S4 · Traceability** | break 3; the supervisory finding has already arrived | the regulatory report's numbers are traceable to source |
| **S5 · Hygiene** | 2 400 reports against 300 in use; a cheap visible win | the core is confirmed, the rest archived |

---

# 03 · Metrics and goals

Metrics come before the portfolio: an initiative earns its place when it moves a named metric.

| Metric | Stream | Now | Year 1 | Year 2 | Year 3 | Downward adjustment for risk |
|---|---|---|---|---|---|---|
| Contour objects with owner and recorded time | `S1` | 0% | 90% | 90% | 90% (ceiling) | valid only if time is recorded in managers' objectives |
| Definitions with owner and formula | `S3` | 0 of ~40 | 30–50 | +corporate line | all management and regulatory | requires resolving the actuary–BI conflict — politics, not method |
| Report fields traceable to source | `S4` | `[missing data]` | 100% of the finding's perimeter | +adjacent reports | the whole regulatory contour | some fields come from the mainframe |
| Duration of quarterly close | `S4` | ~3 weeks of firefighting | reduction, target after measurement | — | normal, without firefighting | baseline not formalised |
| Retail individuals with resolved identity | `S2` | 0% | one country `[missing data]` | four countries | +corporate and health | legal clearance on the acquired company |
| Divergences in board reports per quarter | `S3` | 3 versions of one number | ≤1 | 0 | 0 | **the only metric in the set that can legitimately fall** |
| Unused reports archived | `S5` | 0% | ≥60% | continuous | continuous | archiving meets owner resistance |
| DQ coverage of the key contour | `S4` | `[missing data]` | target after inventory | — | — | the low-confidence score in the scorecard |
| Maturity, average across 9 categories | all | 1.4 | 2.0 | 2.5 | 3.0 | +1 level a year is the ceiling at current approval throughput |

Anti-metrics that may not be reported: number of glossary terms, number of council meetings, percentage of metadata completeness. The 2022 failure reported on exactly those.

Five of the metrics above are counters that can only rise. They are kept as indicators of perimeter coverage but labelled proxies out loud: an unlabelled proxy is the polite version of metric theatre. There is one metric that can legitimately fall; at the next revision the close duration and time-to-resolve-a-dispute join it, as soon as they have baselines. Three goals without measurement are marked and are not committed.

---

# 04 · Initiatives portfolio

Each initiative belongs to one stream. Output is what physically exists when it is done; outcome is which metric from section 03 moves and by how much, by year.

| # | Initiative | Output | Outcome by year | Owner · prerequisite | Effort · wave | Risk and how it is managed |
|---|---|---|---|---|---|---|
| 1 | **Re-founding the council** `S1` | An order changing the chair; an agenda of definition disputes and prioritisation; the status-report format abolished; the first meeting held | **1:** unblocks initiatives 2 and 4 — without it their outcome is zero. **2–3:** the body works as arbitration, measured by time to resolve a dispute | CRO as chair, secretary the head of the data platform · their agreement is the entry condition of the whole strategy | Low in hours, high in political weight · first month | The sign changes, the behaviour does not. Control: if status reports return, the body is theatre again |
| 2 | **Registry of contour owners** `S1` | A registry of objects with owners; a governance line in their managers' objectives; the owner field mandatory in the tool — an object without an owner appears in the secretary's weekly list | **1:** contour objects with owner and time 0% → 90%. **2–3:** holding 90% as the portfolio grows; no expansion to adjacent contours planned | Head of the data platform, time agreed through the council · initiative 1 | Medium · H1 | Owners named, time not recorded — then it is a document, not a role. Test: what happens at calibration if the person did no governance work |
| 3 | **Identity resolution for retail individuals** `S2` | A record-matching rule, traceable and explicable to a human; a working contour for retail in one country; a documented decision that this is not a golden record for all lines | **1:** retail in one country, target percentage after the pilot `[missing data]`. **2:** four countries. **3:** corporate and health, only after the lines confirm | Customer-domain data architect and a retail-line curator · initiative 2 and legal clearance on the acquired company | High, the heaviest in the portfolio · H1–H2 | Reads as a second MDM. Removed by the explicit difference: one country, one line, a pilot rather than a programme, cross-line agreement pushed beyond the year |
| 4 | **Registry of key definitions** `S3` | A registry of 30–50 board and regulatory metrics with formula, owner and scope; a written dispute-resolution protocol; actuarial and management definitions separated where they genuinely differ | **1:** 0 → 30–50 definitions with an owner. **2:** the corporate line. **3:** all management and regulatory metrics | The council as arbitration, registry kept by the platform, each definition owned by a person from the domain · initiative 1 | Medium in work, high in negotiation · H1 | Actuaries will not accept someone else's definition. Do not compel: separate the two explicitly and record where each applies |
| 5 | **Traceability of the regulatory report** `S4` | Tracing report fields to source on the finding's perimeter; a described scenario for fields coming from legacy; material to show an inspector | **1:** 100% of the perimeter's fields — conditional until reconnaissance. **2:** adjacent reports. **3:** the whole regulatory contour | Head of regulatory reporting and a legacy support engineer · technical reconnaissance of depth through the mainframe | Unknown until reconnaissance; the portfolio's main uncertainty · H1–H2 | The mainframe does not yield the required depth. Then the perimeter narrows to non-legacy fields, and this is stated to the supervisor in advance rather than discovered at inspection |
| 6 | **Intake control on broker files** `S4` | A quality contract in the broker agreement; an automatic file check on intake; a return procedure for non-conforming files | **1:** intake control works, metric after inventory. **2–3:** the return rate falls — the signal that the contract works on the brokers' side | Broker channel owner and the platform · no prerequisites | Medium; mostly contractual · H2 | Brokers will not accept a quality contract. Phased introduction: warning first, rejection later |
| 7 | **Inventory and archiving of reporting** `S5` | An inventory of 2 400 reports by usage; the unused archived; a confirmed and marked core of ~300 | **1:** ≥60% of unused archived. **2–3:** a continuous process, growth in object count stopped | The platform; core confirmation by report owners · no prerequisites, starts independently | Low technically, medium on resistance · H1 | Owner resistance. Move to archive rather than delete, with one-click restore |
| 8 | **DQ checks on the key contour** `S4` | Checks on contour objects; an incident-handling process with a named owner | **1:** contour coverage, target after inventory `[missing data]`. **2–3:** share of incidents found before the business finds them | Object owners from initiative 2 · initiative 2, without owners there is nobody to triage | Medium · H2 | A stream of unhandled incidents devalues the checks — hence after the owner registry rather than alongside it |

## Freeze order

`S1` does not freeze → `S4` is protected by an external deadline → `S3` → `S2` → `S5` freezes first. On losing a third of the resource, initiatives 6, 7 and 8 freeze and the identity perimeter narrows from a country's retail to one line. The order is published in advance — otherwise a cut removes roles as "not producing results".

Caveat: the rule "`S1` does not freeze" applies after the decision in the Summary. Before it, roles are not a protected priority but an open fork — there is simply nobody whose time to record.

## Kill-gates

We do not buy a catalog until `S1` roles work in three domains. We do not extend identity to corporate and health until the retail contour is legally confirmed and accepted by the lines. We do not add a metric to the registry without an owner. We do not launch blanket DQ coverage — only the regulatory and customer contours. And no initiative goes under the flag of Data Governance.

---

# 05 · Operating model

The section on which everything above depends.

## Roles

**Council chair** — the CRO. Arbitration of definition disputes, prioritisation, escalation to the board. About 4 hours a month, recorded in their objectives as the answer to the supervisory finding.

**Object owner (custodian)** — whoever already creates and maintains the object, engineer or analyst. Description, quality, currency, incident response. About 10% of their time, as a line in their manager's objectives.

**Definition owner** — a domain subject expert. The metric's formula, its scope, defending the definition at the council. Load arises with disputes; not continuous.

**Council secretary** — head of the data platform. Keeps the registries, prepares disputed cases, tracks decisions. About 8 hours a month, part of the main role.

**Legacy support engineer** — from the mainframe team. Technical reconnaissance and field tracing under initiative 5; sizing after reconnaissance.

The model is custodial rather than stewardship-based: responsibility sits with whoever already maintains the object. The business retains acceptance of definitions and resolution of disputes — not operational work. A role without a line in someone's objectives stays a wish, so time is stated for each.

## Bodies

The council is re-founded rather than created. Composition: chair the CRO; secretary the head of the platform; one representative each from retail, corporate, actuarial, compliance and IT. Monthly rather than quarterly, sixty minutes. Mandate: resolving definition disputes, prioritising work, removing blockers.

What the council does not do: it does not listen to status reports, does not approve architecture, does not sign off team plans, does not keep minutes for their own sake. Abolishing status reports is not cosmetic — they are precisely what filled three years with time instead of decisions.

A new body beside the old one reads as a duplicate and splits an already weak mandate. So the existing council changes its chair and its agenda; if in two quarters it has filled with reports again, it is closed and arbitration passes directly to the chair.

## Decision protocol

A definition dispute is raised into the registry by any participant. The secretary prepares the case: two definitions, who applies each, the cost of the divergence. The council decides at the next meeting, and the decision is recorded with a date, an owner and a scope. There is no retroactivity — previously issued reporting is not recomputed. Without that rule every dispute drags a retrospective behind it and disputes stop being raised.

## Interfaces

The architecture committee is the main throughput constraint. The workaround: initiatives are packaged into two existing mandates — the supervisory answer and cross-sell — and are not opened as a new programme. This is a political construction, not a way around procedure. Legal and the DPO are a blocking dependency for initiative 3, placed in the prerequisites rather than in the work. The actuarial function does not report to governance and should not: the interface is the definitions registry and arbitration, not requirements. The cross-sell programme is a consumer of initiative 3's output; the two are synchronised on dates so that it does not start before identity exists.

## Resources and artefacts

No new headcount: the work is covered by quotas inside existing teams. What is scarce is approval throughput, not budget, so the resourcing decision here is cheaper than in a typical case and the political one is dearer.

The objection "this is bureaucracy" is answered with arithmetic. Removed: ~2 100 unused reports; a 340-term glossary last updated two years ago, replaced by a registry of 30–50 live definitions; the council's status-report format; a quarterly ritual replaced by a shorter monthly one with decisions instead of presentations. Created: two registries, a one-page dispute protocol, a one-page instruction for object owners, a quality contract in the broker agreement. Everything else lives in tools rather than documents: the mandatory owner field, the automatic broker-file check, DQ checks on the contour. Policies are not rewritten: producing governance text costs nothing, the bottleneck is finding a reader, and an artefact without a named reader does not enter this strategy.

The sustaining track — hygiene and DQ on the contour — runs continuously across units; the exploratory one, identity, is fenced into a one-country pilot. Enablement is minimal and targeted: a one-page instruction for object owners and a walkthrough of two real definition disputes at the council as a teaching case. There is no mass training — the governance routine has to be built into the tools rather than learned.

## Degradation path

If the chair is not agreed, stream `S1` does not start and initiatives 2, 3 and 4 lose their prerequisite. What remains is `S4`, held by the regulatory deadline, and `S5`, which needs no mandate. The document is renamed to a programme of supervisory response and reporting hygiene and stops being called a DG strategy. This is not a fallback plan but an honest boundary: without a mandate holder the rest does not happen.

---

# 06 · Effect of the strategy

> **Expert estimate.** The structure of the effect and the orders of magnitude are working; specific sums require a precise calculation on the company's data. Below is what must be measured and who owns each figure. No line from here appears in the Summary as a headline number, and none is fit for an OKR before measurement.

Of the three real zones the leading one is **regulatory risk**, and that is a rare piece of luck: the finding has been received, so the event has happened and does not need forecasting. Second by weight is **cost saving**. **Revenue growth** through cross-sell is present but runs through another programme and another metric, so in the model it lives only with an agreed attribution share, which does not exist yet.

The board reads two numbers: an agreed estimate of possible losses against the cost of preventing them, with the positive decision taken when minimal losses exceed maximal costs. So losses are taken at the bottom of the range and costs at the top. The year's costs are known more precisely than the effect, which is a strength: **no new headcount**, the cost reduces to time quotas inside existing teams (~10% of an object owner's time, 4 hours a month for the chair, 8 for the secretary) plus the work under initiative 5, whose size is unknown until reconnaissance. The upper bound is computed from payroll and sits in months of FTE, not tens `[missing data: cost of an hour by role]`.

The mechanism differs by stream. `S4` provides the cost of a second finding on the same subject multiplied by the probability of receiving it without traceability, plus the reduction of the three-week close firefight. `S5` provides infrastructure, licences and compute windows freed by retiring 2 100 reports — the most reliable line in the model. Broker intake control provides the share of non-conforming files multiplied by the cost of manual handling, and removes the operational risk of depending on a departed employee. `S3` provides the cost of the actuary–BI divergence: rework, reissued reporting, board time spent on three versions of one number. `S2` provides cross-sell uplift, but the metric belongs to another programme. `S1` provides no effect and should not — it is the prerequisite of the others.

The leading method is **business cases and freed profit**, chosen for availability rather than size of result: the cleansed-record method requires per-record economics we do not have, and the labour-saving method requires a catalog cut off by a kill-gate. It also works where "give us money for data governance" does not pass: we do not ask for money for governance, we attach to what is already funded.

The range is two-sided. In the pessimistic scenario traceability through the mainframe is unreachable, the perimeter is narrowed, attribution is not agreed, and only hygiene and intake control count — the effect is positive but small. In the base case traceability closes on the finding's perimeter, a second finding is not received, definitions stop diverging — the effect is several times larger, and its leading part is not money but regulatory damage not incurred. There is no optimistic scenario, deliberately: it does not survive contact with finance, and its presence turns the other two into negotiating positions.

Five downward adjustments apply. Vendor percentages are not used — no vendor model is in play and no catalog is being bought. Productivity does not convert into output: freed hours in risk and compliance do not become results automatically. Attribution zeroes the cross-sell line until it is agreed. Adoption shifts the start — hygiene from the second quarter, traceability after reconnaissance. Dependencies zero `S2` entirely until legal clearance is obtained.

One line goes into the commitment — **the infrastructure saving from archiving reporting**. The only one where the economics is direct and requires no argument about attribution: retired objects stop consuming resource, and that shows up in an invoice rather than in a model. Everything else is present as an estimate and is not committed. The decision on the committed fraction was taken here, before the meeting, not in it: a fraction named under pressure in the room is a promise somebody answers for personally.

The estimate can be replaced by a calculation with seven measurements, six of which are two weeks of work:

- cost of a second supervisory finding — fine, remediation, management time — CRO and legal; unblocks the leading line of the model;
- timing of the quarterly close by role — head of regulatory reporting, one cycle;
- infrastructure cost of the 2 100 reports — the platform; unblocks the committed line, which until measured remains an estimate;
- share of non-conforming broker files and the cost of manual handling — broker channel owner;
- number of reporting reissues a year as the price of definition divergence — council secretary, after initiative 4;
- cost of an hour by role — HR and finance; the denominator of the whole model;
- cross-sell attribution share — the cross-sell programme owner; this is negotiation, not measurement.

The list of what can be assigned this week matters more than any figure in it.

Excluded and not returning: operational efficiency, innovation, accelerated decision-making — the last was closed in the industry a decade ago, and reopening it burns credibility needed later in the same meeting. Likewise savings on auditors and lawyers and faster onboarding. All plausible, none purchasable. Time-to-insight stays a goal in the metrics and does not enter the money model. Data quality is not an independent line of effect: it resolves into revenue or cost, and we draw that line ourselves before finance draws it.

---

# 07 · Risks

**"This is a second MDM."** The difference is stated first: not a golden record for all lines but identity for retail in one country; not fourteen months to a result but a pilot. The 2022 failure is discussed aloud rather than hidden.

**The council stays theatre.** The entry condition is the CRO in the chair and an agenda without status reports. Not agreed — the degradation path in section 05 applies.

**Actuaries will not accept someone else's definition.** Do not compel: separate the actuarial and management definitions explicitly, name an owner for each, record the scope.

**The mainframe does not yield traceability.** `[missing data]` — technical reconnaissance before any target is fixed. In the worst case the perimeter narrows to non-legacy fields, and that is stated to the supervisor in advance.

**Legal blocking on the acquired company's data.** Legal work is a prerequisite of initiative 3. Without clearance, identity is built without the acquired company's CRM, with an explicit loss of completeness.

**Approval throughput consumes the year.** Packaging into existing mandates, plus a quarterly review with the explicit question "what was frozen".

## Revision

The strategy is revisited after each delivery cycle — quarterly — with a mandatory answer to two questions: what has been frozen, and which of the seven measurements is closed. A document without a stated next revision gets quietly replaced rather than updated.

---

# Appendices

Company portrait and interview answers: [alverta-company.md](alverta-company.md). The same run in Russian, including the full rework log: [alverta-strategy.md](alverta-strategy.md).

## What needs measuring for the diagnosis

1. **Depth of traceability through legacy.** Is field-to-source tracing achievable for the 40% of the book on the mainframe? Source: technical reconnaissance by the support team, 2–3 weeks. Blocks initiative 5's target and the conversation with the supervisor.
2. **Legal clearance on the acquired company's data.** May customer data be combined before the legal merger? Source: legal and the DPO. Blocks the completeness of identity.
3. **DQ coverage outside the regulatory contour.** The single low-confidence score in the scorecard.
4. **Baseline of the regulatory close.** How many person-hours and on what. Source: timing one cycle.
5. **The real number of definition divergences.** Three metrics or thirty. Source: reconciliation on a sample of board reports. "30–50" is an estimate, not a calculation.

## Rework log

The CDO judge ran four passes: on the first draft, after the fixes, on the restructured document, and on the rationality dimension.

| Pass | Was | Became | Closes |
|---|---|---|---|
| 1 | Identity across all four countries — the construction that died in 2022 | A pilot in one country; cross-line agreement outside the horizon | feasibility · blocking |
| 1 | "100% of fields traceable" without checking achievability through the mainframe | Target made conditional; technical reconnaissance moved into prerequisites | complexity · blocking |
| 1 | "Re-found the council" as a single line | An initiative with output, owner, risk and a date for the first meeting | concreteness |
| 1 | Traceability hard-dependent on the definitions registry | A bypass: start with fields whose definition is not disputed | order |
| 2 | The key decision sat in the risks on the last pages | Moved into the Summary with the role named and a deadline | defensibility · blocking |
| 2 | The mandate holder was asked for effort without being told the gain | Added what they receive in return | defensibility |
| 3 | The freeze list asserted "roles never freeze" although roles depend on an undecided condition | A caveat: the rule applies after the decision in the Summary | order · a defect introduced by pass 2 |
| 3 | The operating model was four paragraphs of general principle | Roles with time and where it is recorded, the council's composition and anti-mandate, the decision protocol, interfaces, degradation path | feasibility |
| 4 | A handover regulation for departing owners — an artefact with no reader | The rule moved into the tool: mandatory owner field, ownerless objects surface weekly | rationality |
| 4 | Every metric was a counter that could only rise | A metric that can legitimately fall was added; the rest labelled proxies out loud | rationality · metric theatre |
| 4 | The create-versus-retire balance was nowhere counted, though it is the only answer to "this is bureaucracy" | An artefact-balance passage in the operating model | rationality |

**Loop stopped:** pass 4 produced no new blocking findings.

**What the judge did not close.** The objection "identity without the lines' participation will give an incomplete picture" survived every pass. It is correct and unresolvable within the horizon: a complete picture requires the agreement that already killed the programme once. Moved from the judge's list into the strategy's constraints — the year's perimeter is deliberately incomplete, and that is written down rather than disguised.

**Bullshit judge pass.** Removed actorless constructions, intensifiers without numbers, paired abstractions, consulting throat-clearing, and aspirations standing in for initiatives with an owner.

## Where the knowledge base had no answer

A separate class of gap: not "facts about the company are missing" but "the base has no material on the topic".

| Topic | What was needed | What the base has |
|---|---|---|
| MDM and identity resolution | a method for the largest initiative in the strategy | mentions in the context of other topics; no dedicated file |
| Privacy, PII, health data | processing regimes, classification, limits on combining | almost nothing |
| Retention and lifecycle | the legal side of storage and deletion | archiving as hygiene; no legal layer |
| Regulatory traceability | what the supervisor requires, how a provable chain is built | lineage through the catalog and through agents; the regulatory angle is not developed |
| Legacy estate | governance over systems that cannot be changed | nothing; the base assumes a manageable platform |
| External data suppliers | quality control over hundreds of counterparties | nothing; contracts are described for internal flows |
| "Budget yes, speed no" | a programme under an approval-throughput constraint | inverted: the material is built on "they will not give you money" |
| A dead governing body | how to revive or bury an existing council | how to create one; no revival scenario |

**What worked without strain:** the custodian model against stewardship, refusing the catalog as a first step, anti-metrics, the "what we do not do" section, rehearsing the cut, and the move of not going under the DG flag. The core of the base is universal; its industry wrapping is not.

---

*Produced by the dg-strategy skill (FORM · DG) on [dg-board-kb](https://github.com/alexbarakov/dg-board-kb). The company is invented and deliberately chosen as an awkward test: a regulated industry, a legacy estate, MDM pain. The anti-optimism pass, the CDO-judge loop and the bullshit-judge pass were applied.*
