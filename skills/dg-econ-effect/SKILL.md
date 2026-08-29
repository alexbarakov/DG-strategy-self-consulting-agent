---
name: dg-econ-effect
description: Build the economic effect model for a data governance / BI / D&A strategy. Produces an expert estimate with an explicit precision marker and a named list of what must be measured to replace the estimate with a calculation. Runs standalone or as the "effect of the strategy" subsection inside dg-strategy.
---

# dg-econ-effect — the economic effect model

## What this skill is for

Sooner or later someone asks the strategy "and how much money is this?" This skill produces the answer in a form that survives the follow-up question, which is always the same and always harder: **"what share of that are you prepared to book as provably saved?"**

It is deliberately built to under-promise. The base material behind it is unusually honest for its genre: the author who wrote it disclosed his own real monthly money effect from an entire DG slice as a *warning* — it looked very small against the scale of his company, small enough that he hesitated to show it. Expect the same shape. A truthful DG ROI rarely looks impressive next to product economics, and that is a property of the domain, not of your arithmetic. A model that comes out impressive on the first pass is usually a model with a vendor's percentage hidden in a cell.

**Default output is an expert estimate, not a calculation.** Every figure ships with a confidence tag and, where it is an estimate, with the specific measurement that would turn it into a number. That marker is not a hedge — it is the deliverable. A sponsor who knows which three numbers are guesses can decide to fund the measurement; a sponsor handed a clean total cannot.

## Triggers

| Trigger | Mode |
|---|---|
| "посчитай экономический эффект", "сколько это принесёт денег", "build the business case", "what's the ROI" | **STANDALONE** — full run, own deliverable |
| Invoked by `dg-strategy` FORM after section 04 metrics are agreed | **EMBEDDED** — produces the `04.x Effect of the strategy` subsection only |
| "проверь их бизнес-кейс", "is this ROI model defensible" | **CHALLENGE** — audit an existing model against the guards below |

In EMBEDDED mode do not re-interview: the metrics, initiatives, owners and constraints are already established. Ask only for the economic inputs that section 04 does not carry.

## Step 0 — the disqualifying questions

Ask these before modelling anything. Two of them can end the run legitimately, and ending it is a better outcome than a model nobody can defend.

1. **Does this organisation operate in money at all?** Government bodies and some regulated structures do not think in cost reduction. If yours is one, the lever is compliance and the management vertical, not ROI — say so and stop. Producing a money model for a body that does not decide on money is wasted credibility.
2. **Which of the three real zones is this strategy in?** Revenue growth, cost saving, regulatory-risk mitigation. Those are the only three worth searching.
3. **Is there a customer base large enough, with real quality problems and access to per-record economics?** If not, Method 1 is unavailable to you — and you should say so before someone asks for it, not after.
4. **Would you rather not have the budget?** A funded program inherits the burden of proving payback annually. In a company that scrutinises money closely, the stronger play is sometimes leaving the work inside teams that already justify their existence, precisely so there is no line item to cut. If that is the case, the honest deliverable is a note explaining why there is no business case, not a business case.

## The three zones — and the two that are air

**Real:**
- **Revenue growth** — by tying governance work to business initiatives that already have money attached to them. You do not create the revenue; you unblock or improve an initiative that was already going to be measured.
- **Cost saving** — infrastructure, licences, storage, avoided rework, avoided failed communications. The one line here that needs no attribution argument at all is **infrastructure freed by deleting redundant objects**: nobody disputes a decommissioned cluster.
- **Regulatory risk** — the cost of the fine, the remediation, and the management time an inspection consumes, weighted by probability.

**Air — refuse these by name before someone puts them in the deck:**
- **Operational efficiency** ("we get reliable data faster, we shorten time-to-insight") — shaky to the point of being air.
- **Innovation** ("faster adoption, faster adaptation") — also shaky.
- **The whole indirect-benefit list**: multiplier on existing investments, faster onboarding via a knowledge base, savings on audits, savings on lawyers, fraud detection via DQ rules, accelerated decision-making, easier self-service, problems fixed before they cost anything. All plausible, all unbuyable.
- **Accelerated decision-making specifically is closed permanently.** Attempts to measure it were worked over a decade ago; everyone who went deep stopped. Reinventing it burns credibility you will need later in the same meeting.
- **Data quality is not its own petal.** It always resolves into revenue or cost. Draw that line yourself before finance draws it for you.

Note the trap in the refusals: time-to-insight is a perfectly good *strategy* metric and a bad *money* metric. Keep it in section 04 as a goal; keep it out of the effect model as a revenue line.

## The decision rule to model against

Top managers do not read a benefits wheel. They read two numbers: **an agreed estimate of possible losses, and the cost of preventing them.** The positive decision is taken when the *minimal* losses exceed the *maximal* costs.

Build the model in that shape. It means:
- Losses go in as a **range**, and you argue from the bottom of the range.
- Costs go in as a range, and you argue from the top of it.
- If the pessimistic-loss / optimistic-cost comparison still clears, you have a case. If it only clears in the middle, you have a discussion — say that plainly instead of showing the midpoint as the answer.

## The three methods

Pick by availability, not by which gives the nicer number. All three ship ready-to-fill as sheet 11 "Economics" of the **DG Planner** workbook (`12_templates/templates.md`).

### Method 1 — the cost of a cleaned record

For duplicate/quality problems on a large customer base. Structure: identified duplicates × unit cost of a duplicate, plus bad records × annual profit per newly-cleaned record, against the technical solution, the one-off cleanup, and annual upkeep.

The cost side is spend avoided on failed communications — operators, call-centre, SMS, email. The income side is debt collection and secondary sales that depend on contact-data quality. A third term — improved attributes feeding a customer-potential model — requires a record-completeness value model you probably do not have; leave it out rather than guess it.

**The guard printed under the formula: one record is counted once.** The three benefit terms overlap by construction. Drop the guard and the model inflates itself.

**Scope condition:** genuinely customer data, a large base, real quality problems, and figures you can actually assemble. Otherwise you will not pull this off — say so.

Reference point (a large bank's published MDM case, `51_numbers.md`): 320M records, 230M duplicates, 50% initial contact quality, >$300 acquisition cost, ~$300 per failed communication, claimed effect >4B RUB. Copy the structure; do not import the ratios.

### Method 2 — labour savings (the catalog model)

Role groups × headcount × fully-loaded annual cost × a productivity percentage, against tool TCO plus the product team.

This is the method most likely to be handed to you by a vendor and the most likely to be wrong. Its premise — that analysts will spend the freed time working with data rather than searching for it — is a very large assumption that holds only if the tool is filled, documented, decently integrated, and used at scale.

**Three mandatory corrections:**
1. **Discount the percentage.** Vendors put 23–26% in that cell. Provable reality is **5–7%**. Model the vendor number only to show what you are discounting.
2. **Saved time does not convert to output.** Finance will make this correction, so make it first: a productivity improvement is not production. People go for coffee more often.
3. **Copy the evaluation logic, not the numbers.** Forrester-style TEI is instructive because the chain is visible — benefits PV, costs, a stated coverage assumption, a stated capture rate, an explicit risk adjustment. Reproduce that chain with your own inputs.

The adjacent measurable that survives better than raw labour savings is **self-service**: it has numbers you can take, and governance sits underneath it as the precondition — the locomotive argument.

### Method 3 — business cases and freed-up profit

A matrix of concrete business projects, each with its own income and expense, plus a standing governance-office cost line with zero income against it. Typical entries: profit from better targeting, purchasing and stock optimisation, theft reduction through monitoring, average-cheque growth from a recommender or better shelf layout, headcount optimisation.

Because each case must be concrete, each is individually small — **and therefore you need many of them.** A dozen; at most twenty to thirty. Hunt among initiatives that already have money attached and are decomposed out of the company strategy. This is the method that works in companies where "give us this much money for data governance" is a non-starter: you never ask for money for governance, you attach to things already being funded.

## Attribution — a negotiated parameter, not a measurement

When the effect lands on someone else's metric, the share credited to your work is agreed, not calculated. The working formulation from a real platform: *we agree with the business that a part of the metric uplift the analyst brings will be attributed to the platform.*

Fix the share upfront, in writing, with the people whose metric it is. An attribution share invented at presentation time is the fastest way to lose the room. Record it in the model as an explicit line — "attribution share: X%, agreed with N on DATE" — or, if it has not been agreed, as `[missing data]` with the name of the person who has to agree it.

## The haircut ladder

Apply in order, and show the intermediate values rather than only the total. A model whose working is visible survives challenge; a model that shows only a total invites the challenger to attack the total.

| # | Haircut | Typical | Why |
|---|---|---|---|
| 1 | Vendor → provable productivity | 23–26% → **5–7%** | the single largest source of inflation |
| 2 | Productivity → realised output | further discount, stated explicitly | freed time is not production |
| 3 | Attribution share | negotiated, often well under half | the metric belongs to someone else |
| 4 | Adoption / ramp | effect starts partway through the year | nothing lands on 1 January |
| 5 | Dependency risk | zero out anything gated on an undecided prerequisite | an effect behind a blocked gate is not an effect |

**The committed fraction.** Decide before the meeting — never in it — which portion of the modelled effect you are willing to have written down as a commitment. Commit only where the economy is direct. Infrastructure saved by deleting redundant objects is the line that needs no attribution argument and is therefore the natural place to put the commitment.

## Guards

- **Recompute the revenue side; do not polish the savings side.** The anti-case worth memorising: 10M direct-mail items a year, ~10% wrong or duplicate, ~$500k/yr gross saved at 50c an item — but only **$100k net** after $400k/yr of new process upkeep, against a $3M investment. **Thirty years' payback.** Bolting marketing's segmentation model onto the same savings line does not rescue it.
- **Net, not gross.** Every benefit line carries the new process it creates. A model without an upkeep line is not finished.
- **One record counted once.**
- **No cell may contain a number whose provenance you cannot state.** If a figure came from a vendor calculator, label it `vendor` and show what it becomes after haircut 1.
- **Do not model what the KB says nobody has measured.** Per-object certification cost, per-check DQ cost, verification cost of AI-generated metadata, token economics of agent scenarios, human-in-the-loop review burnout — all are named as unmeasured in `51_numbers.md`. If your model needs one of them, it is an assumption, and it goes in the precision list.
- **Expect a modest total, and set the expectation before you present it.** The failure mode is not a small number; it is a sponsor who was led to expect a large one.

## Confidence and the precision marker

Every line in the model carries a tag:

| Tag | Meaning | Allowed use |
|---|---|---|
| `calculated` | derived from the company's own measured figures | may be committed |
| `expert estimate` | your structured judgement on the company's real inputs | may be presented, may not be committed |
| `benchmark` | someone else's published figure, structurally adapted | orientation only, never a total |
| `vendor` | from a supplier's model | shown only alongside its haircut |
| `[missing data]` | the input does not exist yet | blocks the line; names the measurement |

**The mandatory header on every standalone or embedded output:**

> Экспертная оценка. Порядок величины и структура эффекта — рабочие; конкретные суммы требуют точного расчёта на данных компании. Ниже перечислено, что именно нужно измерить и кто владеет каждой цифрой.

(localised into the user's language — see the language convention in `dg-strategy`.)

Immediately after the model, a **precision list**: each unmeasured input, the measurement that would settle it, who owns that number, and how long the measurement takes. This list is the part a sponsor can act on this week; treat it as the primary output, not the appendix.

## Output format

### Standalone

1. **Verdict in three lines** — which zone, the range of the effect, and whether the min-loss / max-cost rule clears.
2. **Model by method**, one table per method used, working shown line by line.
3. **Haircut ladder** applied, with intermediate values.
4. **Committed fraction** — what you are willing to write down, and why that line and not another.
5. **Scenarios** — pessimistic and base only. No optimistic column: it never survives contact with finance and its presence makes the other two look like negotiating positions.
6. **Precision list.**
7. **What we will not claim** — the refused air lines, named, so nobody adds them back later.

Two formats, as everywhere in this repo: HTML for reading, Markdown for editing.

### Embedded in a strategy (`04.x`)

A compact subsection under the metrics, before the portfolio, containing:

| Element | Content |
|---|---|
| Zone | which of the three, in one line |
| Mechanism per stream | how the stream turns into money or avoided loss — a sentence, not a formula |
| Range | pessimistic and base, with the confidence tag |
| Attribution | the share and whether it is agreed |
| Committed fraction | the part that goes into the commitment |
| Precision list | what to measure, who owns it, how long |
| Refused | the air lines, named |

**Placement rule:** the effect subsection sits inside section 04, after the metric table and before the portfolio. It is an argument about the metrics, not a separate document — and it must not appear in the Summary as a headline number unless the number is `calculated`. An estimate promoted to the Summary becomes a promise by the time it reaches the third reader.

## CHALLENGE mode — auditing someone else's model

Run the guards as a checklist and report by severity:

1. Is there a `% productivity improvement` cell somebody guessed? → the largest finding, always.
2. Does the model show gross where it should show net — is there an upkeep line?
3. Are any of the air benefits carrying weight in the total?
4. Is the attribution share stated, and was it agreed with the metric owner?
5. Is any record, saving or benefit counted twice?
6. Was the savings side polished instead of the revenue side recomputed?
7. Does the total rest on a benchmark imported with its ratios rather than its structure?
8. Is a committed fraction named — and would the author survive being held to it?

Finish with the question the model exists to answer: *what share of this are you prepared to book as provably saved over one, two, three years?* If the model cannot answer it, that is the finding.

## Source material in this KB

| Where | What it carries |
|---|---|
| `11_dg_program_themes/maturity-and-metrics.md` | the three zones, the three methods with worked numbers, attribution, the scorecard |
| `50_failure_catalog.md` | over-promising the payback; the castle in the clouds; vendor arithmetic at face value; ROI inflation by polishing the savings side; double-counting records |
| `51_numbers.md` | every number above with its reliability tag, plus the explicit list of things nobody has measured |
| `52_questions.md` | the diagnostic questions in step 0, with interpretation of the answers |
| `12_templates/templates.md` | DG Planner workbook, sheet 11 "Economics" — the three methods ready to fill |

## Guardrails

- Never produce a total without its confidence tag and its precision list.
- Never present an optimistic scenario.
- Never promote an `expert estimate` into a commitment, a Summary headline, or an OKR.
- Never model an air benefit even if asked — explain the refusal in one sentence and offer the nearest defensible line instead.
- If step 0 disqualifies the run, say so and stop. A refusal with a reason is a better deliverable than a model that cannot be defended.
