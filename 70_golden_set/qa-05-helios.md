---
type: eval
company: Helios Energy
theme: no money lever, legacy estate, near-zero literacy — the KB's weakest branch
items: 20
---

# Helios Energy — 20 questions

State-majority power distributor, 9 000 people, ~15 analysts. Tariffs set by the regulator. Three generations of SCADA and metering. A new reporting standard in eighteen months and a board that has read about AI.

This company exists in the set to make the base fail where it is thin. Several answers below are honest refusals, and they are scored as correct.

---

### 1. What are the three real sources of ROI, and which two are air? `L1` `roi`

**Answer.** Real: revenue growth via linking governance to business initiatives, cost saving, and mitigation of regulator-related risk. Air, crossed out by name: operational efficiency ("we get reliable data faster, we shorten time-to-insight") and innovation. The whole indirect-benefit list — savings on audits, on lawyers, faster onboarding, accelerated decision-making — gets a red X and a castle-in-the-clouds picture.

**Source.** `11_dg_program_themes/maturity-and-metrics.md` (day 6, slides p.4–5, 19).

**Trap.** Offering operational efficiency to a company that cannot use the other two.

---

### 2. What is the decision rule top managers actually apply? `L1` `business-case`

**Answer.** They read two numbers: an agreed estimate of possible losses and the cost of preventing them. A positive decision is taken when the *minimal* losses exceed the *maximal* costs — so you argue from the bottom of the loss range against the top of the cost range.

**Source.** `11_dg_program_themes/getting-started.md` (day 1, slides p.45); `skills/dg-econ-effect/SKILL.md`.

**Trap.** Presenting a midpoint estimate as the answer.

---

### 3. What is the 5-of-12 test? `L1` `getting-started`

**Answer.** A twelve-statement self-assessment of pains — cross-functional reporting, multiple sources, PII, poor DQ eroding trust, third-party data, regulation, dataset discovery, consistency across applications, competitive digital market, duplication, storage cost, data-dependent strategic projects. Five or more relevant statements suggest a program is cost-effective; fewer, and common-sense DG is the recommendation.

**Source.** `11_dg_program_themes/getting-started.md`.

**Trap.** Treating it as a maturity score. It is an entry gate.

---

### 4. What does the base say about data literacy? `L1` `data-literacy`

**Answer.** Less than you would expect, and it says so: the dedicated board section is carried almost entirely by images and is a stub. The machine-readable substance is a skills model — role profiles with target levels L1–L4 across ~13 dimensions, individual and team scores against target — plus data literacy carrying the highest weight (0.15) in the Data-Driven Index, and a learning-system stream covering onboarding, training, marathons, skill belts and a gamified community.

**Source.** `11_dg_program_themes/data-literacy.md` — including its own stub warning.

**Trap.** Presenting a literacy curriculum as if the base contained one.

---

### 5. What is the Data-Driven Index? `L1` `maturity`

**Answer.** A composite company-level index rolling up component scores, in which data literacy is one of the highest-weighted components (0.15). It exists on the board as a dashboard mock-up with individual, team and department roll-ups scored against target profiles.

**Source.** `11_dg_program_themes/maturity-and-metrics.md`; `11_dg_program_themes/data-literacy.md`.

**Trap.** Treating the mock-up as a validated instrument. `60_roadmap.md` C3 records the DDI scoring grid as one of four frames that resisted machine extraction.

---

### 6. Cost reduction is not a lever here — savings return to the tariff. What is the lever? `L2` `roi`

**Answer.** Compliance and the management vertical. The base states the case directly: government bodies and some regulated structures do not think in cost reduction at all, and where that is true, ROI is not your instrument. For Helios the eighteen-month reporting standard is the strongest lever available, because it converts governance work into an obligation with a date rather than a benefit with an argument.

**Source.** `11_dg_program_themes/maturity-and-metrics.md` — "does your organisation even operate in money" (day 6, transcript); `skills/dg-econ-effect/SKILL.md` — step 0.

**Trap.** Building a cost-saving business case anyway because that is the standard shape.

---

### 7. A new reporting standard lands in eighteen months. How do we use it? `L2` `regulatory`

**Answer.** As the mandate the program rides on — attach the work to an initiative that already has money and a deadline, and do not run it under the flag of data governance. Scope to the reporting perimeter: which fields, from which sources, with which owners, traceable to origin. Note the base's limit: regulatory lineage — the auditor's "show me where this number came from" — is discussed only through catalogs and agents, and `60_roadmap.md` A5 lists it as an open gap with a different acceptance criterion from ordinary lineage.

**Source.** `11_dg_program_themes/getting-started.md` — attaching to funded initiatives; `60_roadmap.md` — A5.

**Trap.** Treating the standard as a compliance project separate from data work. It is the only funded door available.

---

### 8. Fifteen analysts in a 9 000-person company. Do we need governance or people? `L2` `getting-started`

**Answer.** People first, and the base's own gates say so. Cross-functionality is the trigger for a program, and with fifteen analysts and a monthly PDF pack there is barely a data function to coordinate. What applies is the minimal viable version: keep a registry — Excel is acceptable — of the marts that matter, put a responsible techie and a responsible business person on each, cover them with checkers and documentation, and watch that they arrive intact each morning. For many companies that is eighty percent of the governance actually required.

**Source.** `11_dg_program_themes/getting-started.md` — minimal viable governance (day 3, transcript).

**Trap.** Recommending a governance program because the company is large. Headcount is not the trigger; cross-functional data dependence is.

---

### 9. Management says "the report says so" and stops. Is that a literacy problem? `L2` `data-literacy`

**Answer.** Yes, and it is upstream of everything else — but the base's material here is thin and mostly a scoring model rather than an intervention. What it does offer: literacy carries the highest DDI weight, jargon divergence inside the data function is itself a literacy problem before any business training starts, and the author deliberately avoids DAMA/DMBOK/Kimball vocabulary with business because that language gets in the way. Practical first move at Helios: one shared vocabulary for the ten numbers management actually uses, not a training programme.

**Source.** `11_dg_program_themes/data-literacy.md` — including its acknowledged thinness.

**Trap.** Proposing a company-wide literacy curriculum on the strength of a stub file.

---

### 10. Three generations of SCADA and metering that will not be modified. What governance is even possible? `L2` `legacy` `gap`

**Answer.** Governance at the boundary rather than inside: intake contracts, validation at the point data enters the warehouse, and documented provenance as far back as the systems allow — with the depth limit measured, not assumed. Be explicit that **this base has no material on governing a legacy estate**: it assumes a platform you can change, and `60_roadmap.md` B4 lists the gap, including how deep traceability can realistically go through such systems. The answer above is the general principle, not a grounded method.

**Source.** `60_roadmap.md` — B4; `11_dg_program_themes/data-quality.md` — intake and contracts for the boundary case.

**Trap.** Proposing modernisation as a prerequisite. The systems outlive the strategy.

---

### 11. The board asked what we are doing about AI. What is the honest answer? `L2` `ai-governance`

**Answer.** That the prerequisites do not exist yet, and that the useful work is the prerequisites — with a date, so the answer is not a refusal. The chain is core → semantic → context → agent accuracy → self-service, and Helios has none of it; an agent on this estate would produce ~40%-class accuracy and the failure mode is invention rather than refusal. What can be promised in eighteen months is a documented, owned reporting perimeter, which is also what the regulator wants — the same work, two audiences.

**Source.** `10_ai_era_themes/semantic-layer.md` — accuracy without a governed route; `30_graph/objects.yaml` — the chain.

**Trap.** Launching a pilot assistant to satisfy the board. Lost trust in an assistant is not recoverable on a second attempt.

---

### 12. Procurement takes nine months. Does that change the plan? `L2` `constraints` `gap`

**Answer.** It changes what the plan optimises. The base's material is built almost entirely on the constraint "they will not give you money", with a time quota as the central move — Helios has the inverse problem, throughput rather than budget. The response is to minimise the *number of approvals* rather than the cost: package work inside mandates that already exist (the reporting standard), avoid anything requiring procurement in the first year, and prefer instruments already licensed. `60_roadmap.md` A3 records this inverted constraint as an open methodological gap.

**Source.** `60_roadmap.md` — A3; `11_dg_program_themes/getting-started.md` — common-sense DG on existing tools.

**Trap.** A tooling roadmap. Nothing new arrives inside the horizon.

---

### 13. Should we hire a CDO? `L3` `sponsorship`

**Answer.** Not as the first move. The base's rule is that the leader must be an authoritative old-timer — you can hire from the market, but then you wait until they become one, because nobody lets a newcomer seriously change their processes. In a nine-month-procurement, no-one-gets-fired culture that waiting period is long. The stronger move is to find the internal person the regulatory deadline already belongs to and attach the work to them.

**Source.** `11_dg_program_themes/getting-started.md` — the old-timer rule (day 6, slides p.104).

**Trap.** Treating the CDO hire as the sponsorship gate being satisfied.

---

### 14. Engineering trusts the asset register, finance does not. Who is right? `L3` `definitions`

**Answer.** The question is a trap in the same way "which margin is correct" is. Two functions distrusting one register usually means two definitions of the object — what counts as an asset, when it enters, how it is valued — rather than one wrong dataset. Establish which fields each function actually uses, name an owner per definition, record where each applies, and reconcile only the fields that appear in both. Reconciling the whole register is a project that does not end.

**Source.** `10_ai_era_themes/semantic-layer.md` — definitions and applicability; `11_dg_program_themes/data-quality.md`.

**Trap.** Commissioning a data-quality audit of the asset register.

---

### 15. Nobody can be fired for slowness. How do you create accountability? `L3` `roles` `gap`

**Answer.** Through visibility rather than consequence, which is the only mechanism the base offers for this shape: a standing monthly meeting showing per-owner metrics, where people see who is doing better and who worse — peer dynamics alone motivates, even before you have the right to set targets. Beyond that, be candid: this base's accountability material assumes objectives, calibration and the possibility of consequence. Where none exists, it has no tested answer, and that is worth saying rather than dressing up.

**Source.** `11_dg_program_themes/roles-and-operating-model.md` — peer dynamics (day 5, transcript).

**Trap.** A RACI matrix. It codifies accountability that cannot be enforced.

---

### 16. Which comes first here — literacy, quality, or the reporting perimeter? `L3` `sequencing`

**Answer.** The reporting perimeter, because it is the only one with a date and a sponsor. Quality follows it — checks on the fields that go into the submission, alerting a named person. Literacy runs alongside as the cheapest version available: a shared vocabulary for the numbers management already uses, not a curriculum. Reversing this order means asking a company with no analytics culture to invest in capability before obligation, which the base's own entry gates say will not survive contact with the budget.

**Source.** `30_graph/objects.yaml` — stack-rank; `11_dg_program_themes/getting-started.md` — attaching to funded initiatives.

**Trap.** Literacy first because it is foundational. Foundational is not the same as fundable.

---

### 17. Is a maturity assessment worth running at our level? `L3` `maturity`

**Answer.** Only if the result will be wired into someone's annual goals — a model presented and never appropriated is bureaucracy, and the sceptics are right. Run it subtractively if you run it: grey out what does not apply to you first, then colour current state, then read the development zone off the gap. At Helios most of the AI-era and self-service categories should be greyed out before scoring begins, which is itself the most useful output.

**Source.** `11_dg_program_themes/maturity-and-metrics.md` — appropriation test and the subtractive first move.

**Trap.** Producing a 0–4 scorecard across nine categories and presenting it. Without the greying-out step it reads as nine failures.

---

### 18. Calculate the economic effect of the governance program for us. `L4` `trap` `roi`

**Answer.** For this company the correct output is a refusal with a reason. Step 0 of the effect model asks whether the organisation decides in money at all; Helios does not, since savings return to the tariff. Producing a money model for a body that does not decide on money spends credibility for nothing. What replaces it: the obligation, the date, and what fails to be submitted without the work — expressed as regulatory exposure, not currency.

**Source.** `skills/dg-econ-effect/SKILL.md` — step 0, disqualifying questions; `11_dg_program_themes/maturity-and-metrics.md`.

**Trap.** Producing the model anyway with softer language. The refusal is the deliverable.

---

### 19. How do we govern data from our external metering contractors? `L4` `trap` `gap`

**Answer.** This base cannot ground an answer. Data contracts are described for internal flows only; nothing covers external counterparties whose quality you influence solely through contract and intake control — `60_roadmap.md` B5 lists it as an open subject gap, to be filled by interview rather than generation. The one grounded fragment that transfers: put the quality requirement into the commercial contract and validate at intake, rejecting non-conforming files rather than repairing them downstream. Everything past that would be invented.

**Source.** `60_roadmap.md` — B5; `11_dg_program_themes/data-quality.md` — intake control.

**Trap.** A supplier-governance framework. It would be textbook content with a KB label on it.

---

### 20. Our situation seems to be outside what this knowledge base covers. Is that true? `L4` `trap` `scope`

**Answer.** Substantially, yes — and the base should say so rather than stretch. Its core transfers: entry gates, the ownership model, minimal viable governance, the honest ROI conversation, the anti-bureaucracy stance, and the subtractive method. Its assumptions do not: a managed platform, a budget constraint rather than a throughput constraint, an organisation that decides in money, an AI ambition, and a data function large enough to coordinate. Five of the eight gaps in `60_roadmap.md` were found by running this material against a company shaped like Helios. Use the core, ignore the framing, and treat every regulated-sector specific as unverified.

**Source.** `60_roadmap.md` — A2, A3, A5, B4, B5; `README.md`.

**Trap.** Reassuring the asker that the fundamentals apply universally. The base has written down that they do not.
