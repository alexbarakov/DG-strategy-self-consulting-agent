---
type: eval
company: Verdant Retail
theme: content sprawl, certification, self-service, definitions
items: 20
---

# Verdant Retail — 20 questions

Grocery chain, 45 000 people, 210 stores. 3 100 dashboards and 400 opened. Fourteen versions of margin. Eleven powerful category teams. A CFO offering money for a catalog.

---

### 1. What is the BI content funnel? `L1` `content-management`

**Answer.** Archive → certify → promote. Split server content into good (certified) and bad, hide sandboxes from search, and navigate people to the certified objects first. It is a funnel rather than a clean-up because the volume regenerates: without a mechanism intercepting creation, the estate refills.

**Source.** `10_ai_era_themes/bi-content-management.md`.

**Trap.** Describing it as a one-off archiving exercise.

---

### 2. What does "certified" actually mean as a status? `L1` `certification`

**Answer.** A public trust status with a lifecycle, not an event: an object enters, is maintained, and can be degraded. The base warns that certification designed as an event lets entropy do the rest, and that badge count should stay small — three statuses (Candidate / Certified / Degraded) is already generous, because every extra public status raises the user's cost of choosing a source.

**Source.** `10_ai_era_themes/certified-core-layer.md`; `50_failure_catalog.md` — certification as event.

**Trap.** "Certified means the data is correct." It means someone is accountable and the status is current.

---

### 3. What is the subbotnik? `L1` `content-management`

**Answer.** An announced clean-up event: someone responsible per large domain, run for a month, everyone involved rewarded. Real format from the field — three weeks light, about ten hours per BI developer; one June run processed 36.6% of low-use objects (299 of 817) and certified 97. The point is not the cleanup: the goal is to create a habit.

**Source.** `11_dg_program_themes/getting-started.md` — the subbotnik mechanic and figures (day 2, transcript; day 3, slides p.104–109).

**Trap.** Quoting the numbers as a target. They are one company's single run.

---

### 4. Certification in a centralised versus a decentralised BI organisation? `L1` `content-management`

**Answer.** Two fundamentally different designs. Centralised BI → hybrid certification with the business: a "Recommended by <function>" badge where the function confirms data correctness and logic actuality and joins semi-annual reviews, only cross-functional reports certified, zero bureaucracy, everything in wiki report cards. Decentralised self-service → content management at scale: split all content into good and bad and hide sandboxes from search. Verdant is the second.

**Source.** `10_ai_era_themes/bi-content-management.md` (day 3, slides p.91–97).

**Trap.** Applying the centralised design to eleven autonomous category teams.

---

### 5. What is a health score and how is it not a DQ score? `L1` `content-management`

**Answer.** A health score describes the object's condition as an asset — usage, freshness, ownership, documentation, breakage history — while a DQ score describes the correctness of the data inside it. The base insists they stay distinct in reporting, because merging them hides which of the two is failing.

**Source.** `11_dg_program_themes/maturity-and-metrics.md` — health scores kept distinct from DQ scores; `10_ai_era_themes/bi-content-management.md`.

**Trap.** Reporting one composite "data health" number.

---

### 6. The CFO offers budget for a catalog. Take it? `L2` `catalog`

**Answer.** Take the attention, redirect the spend. Verdant is past the size trigger — roughly 100+ analysts — but catalog value is hostage to ownership, contracts, self-service and DQ maturity, and its benefit is often lower than the cost of producing and supporting it. With 3 100 objects of which 400 are used and fourteen definitions of margin, a catalog would index the mess at full fidelity. Sequence: hygiene and definitions first, then the catalog buys something.

**Source.** `11_dg_program_themes/data-catalog.md` — hostage conditions, U-curve; `50_failure_catalog.md` — hiding behind catalogs.

**Trap.** Accepting because the budget window will close. It will reopen when there is something to catalog.

---

### 7. 3 100 dashboards, 400 used. Where do we start? `L2` `content-management`

**Answer.** With usage statistics, which you already have — platform clean-up via usage stats is a common-sense DG project needing no budget. Archive rather than delete, with one-click restore, so the political cost of the first wave stays low. Run it as a subbotnik with a named person per category rather than as a central project, because the category teams are the ones who must not experience it as central control.

**Source.** `11_dg_program_themes/getting-started.md` — common-sense DG projects and the subbotnik; `10_ai_era_themes/bi-content-management.md` — the funnel.

**Trap.** A central audit that deletes other teams' objects. It buys one clean-up and loses the next four.

---

### 8. Fourteen versions of margin. How do we get to one? `L2` `definitions`

**Answer.** You probably do not, and should not aim to. Establish which of the fourteen are genuinely different applications — commercial margin, finance margin, category margin after allocations — name an owner per definition, record where each applies, and retire the rest as duplicates. The unresolvable question is which is *correct*; the resolvable one is which applies where. The base's cautionary case is a company with two metrics, "sales" and "revenue", where nobody could say which was right.

**Source.** `10_ai_era_themes/semantic-layer.md` — definitions and glossary notes (day 4, transcript).

**Trap.** A working group to agree the single correct margin. It will not conclude.

---

### 9. Two teams brought different sales figures for the same week. Is this DQ? `L2` `dq` `definitions`

**Answer.** Almost certainly not. Identical source data producing two numbers is a definitions and ownership failure, not a quality failure — and misdiagnosing it as DQ sends the fix to the wrong team and buys a checker that will pass. The tell is whether the two numbers reconcile once the filters, grain and allocation rules are laid side by side.

**Source.** `11_dg_program_themes/data-quality.md` — data quality resolves into revenue or cost, not into its own category; `10_ai_era_themes/semantic-layer.md`.

**Trap.** Commissioning DQ checks on the sales mart.

---

### 10. Self-service was declared two years ago and produced 3 100 dashboards. What went wrong? `L2` `self-service`

**Answer.** Self-service without the layers beneath it is permission without a route. In the stack-rank, self-service and agentic interfaces come *last* — after ownership, trusted data and the content funnel — because the capability multiplies whatever exists underneath. Verdant declared the endpoint and skipped the sequence, so the capability multiplied ungoverned content.

**Source.** `README.md` — the stack-rank freeze order; `10_ai_era_themes/bi-content-management.md` — the content funnel.

**Trap.** Concluding that self-service was a mistake. The order was.

---

### 11. How do we stop the sprawl regenerating? `L2` `content-management`

**Answer.** Intercept creation. The named failure is leaving the reuse nudge unbuilt: if nothing intercepts the person at the moment they create a new mart or dashboard, reuse stays an aspiration. Add search that surfaces certified objects first, hide sandboxes from search, and make the certified route the default path rather than an achievement.

**Source.** `10_ai_era_themes/certified-core-layer.md` — the reuse nudge (day 3, transcript); `10_ai_era_themes/bi-content-management.md`.

**Trap.** Scheduling quarterly clean-ups. That is a treadmill, not an interception.

---

### 12. Do we need a semantic layer? `L2` `semantic-layer`

**Answer.** Apply the counting heuristic: how many analysts hand-code the same business logic. With ~90 analysts across eleven category teams reusing the same core sales and margin data, the pain is real. But the base classes the layer as a luxury reserved for the mature and offers the budget version for lower maturity: a metric tree bound to the glossary and catalog. At Verdant's state, definitions with owners come first; the layer is what makes them stick afterwards.

**Source.** `10_ai_era_themes/semantic-layer.md` — counting heuristic, luxury framing, budget version (day 5, transcript; day 6, slides p.100).

**Trap.** Buying a semantic layer as the answer to fourteen margins. The fourteen are an ownership problem first.

---

### 13. Category teams will resist central control. How do we get them to certify? `L3` `culture`

**Answer.** Do not ask them to accept control; give them a status they want and a reward for a finite effort. The subbotnik works precisely because the business already carries a background feeling of disorder and swallows the invitation well — and afterwards it turns out participants were doing steward work. Then the ratchet: "that was good, let's repeat" → "why repeat, let's just do it monthly". Add peer dynamics: a monthly meeting showing per-team metrics, where people see who is doing better, motivates before you have any right to set targets.

**Source.** `11_dg_program_themes/getting-started.md` — subbotnik and ratchet; `11_dg_program_themes/roles-and-operating-model.md` — peer dynamics (day 5, transcript).

**Trap.** A certification mandate from the centre with a compliance deadline.

---

### 14. What is the first project that buys us licence for the rest? `L3` `sequencing`

**Answer.** Dashboard certification shipped in three months. The field account is explicit: people see that something was done and that it works, on metrics and purely emotionally; a subbotnik followed immediately, and both bought licence for more expensive initiatives. Note the tension with the marts-before-reports rule — the sequencing lesson is about the *trust chain*, while this is about the *first visible win*; resolve it by certifying the small set of marts the flagship dashboards stand on, then the dashboards.

**Source.** `11_dg_program_themes/getting-started.md` — the worked first project (day 6, transcript); `10_ai_era_themes/certified-core-layer.md` — sequencing.

**Trap.** Choosing the biggest problem as the first project.

---

### 15. Should certification be run inside the catalog once we buy one? `L3` `catalog`

**Answer.** No. Preparation, review and fixes belong in domain cabinets; the catalog shows the public status. Mixing them turns the catalog into a workflow tool it was never designed to be — a named failure in the base. The corollary for Verdant: the absence of a catalog is not blocking certification today, because the status can live wherever object metadata already lives.

**Source.** `10_ai_era_themes/certified-core-layer.md` — running the operational process inside the catalog (day 3, slides p.119).

**Trap.** Sequencing certification behind the catalog purchase.

---

### 16. What should we measure so the CFO sees it working? `L3` `metrics`

**Answer.** Consumption on certified objects rather than certification counts — the share of usage that lands on trusted content is a number that can go down for a good reason, which is the test that separates outcome from activity. Add days without incidents in the weekly commercial pack, which is what the commercial director actually lost. Avoid the certification counter: it can only rise, which makes it activity accounting.

**Source.** `11_dg_program_themes/maturity-and-metrics.md` — operational metrics and the can-it-fall test.

**Trap.** "Number of certified dashboards" as the headline.

---

### 17. Eleven category teams, one central BI team of twelve. Federate or centralise? `L3` `domains`

**Answer.** Neither as a reorganisation. Distributing people into domains changes the org chart, not the behaviour — proactivity requires a goal, a ritual and a visible peer comparison, none of which arrive with the announcement. What works at Verdant's shape is the BI-partner pattern: named partners per category with matrix subordination, a standing monthly meeting showing per-partner metrics, and the central team owning the certified core rather than the ticket queue.

**Source.** `11_dg_program_themes/domains-and-data-mesh.md`; `11_dg_program_themes/roles-and-operating-model.md` — matrix subordination and the monthly ritual (day 5, transcript).

**Trap.** Announcing a data mesh.

---

### 18. Give us the target number of dashboards for a company our size. `L4` `trap` `metrics`

**Answer.** No such number exists here and inventing one would be exactly the untagged-number failure `51_numbers.md` is built to prevent. The usable framing is the ratio you already measured: 400 of 3 100 opened. The target is not a count but a direction — usage concentrated on certified content, sandboxes out of search, and creation intercepted so the count stops mattering.

**Source.** `51_numbers.md` — standing warning; `10_ai_era_themes/bi-content-management.md`.

**Trap.** Any benchmark such as "one dashboard per twenty employees".

---

### 19. Write us the self-service policy that stops people building junk. `L4` `trap` `frameworks`

**Answer.** A policy will not stop it, and this base says why: producing policy text costs nothing now, the scarce thing is readers, and each addition tightens the standards spiral. The rule belongs in the tool — certified objects ranked first in search, sandboxes excluded from search, a reuse prompt at creation time. Push the rule into the tool and the policy becomes unnecessary. If a document is politically required, keep it to one page and expect it to change nothing on its own.

**Source.** `11_dg_program_themes/dg-frameworks.md` — policy minimalism, standards spiral, LLMs collapsing document cost.

**Trap.** Delivering the policy as the deliverable.

---

### 20. Our category teams each want their own certification standard. Fine? `L4` `trap` `certification`

**Answer.** No, and this is one of the places the base is unambiguous: the same status should appear on the mart, the dashboard and the metric, because trust should be one process rather than three — and eleven local standards is the same defect at greater scale. What can be federated is *who* certifies: a named person per category applying one shared definition of the status. What cannot is the meaning of the badge.

**Source.** `52_questions.md` — "does the same status appear on the mart, the dashboard and the metric"; `10_ai_era_themes/certified-core-layer.md`.

**Trap.** Accepting eleven standards as a pragmatic compromise with powerful teams. It reproduces the fourteen-margins problem in the trust layer.

---

### 21. Should we go data mesh? Where is the line between autonomy and control? `L3` `domains`

**Answer.** Decentralisation is a response to a platform complex enough that centralisation became the bottleneck — it is not a maturity level, and "there is no single maturity ladder". A simpler centralised platform can be perfectly mature for a retail company. The real decision is where you sit on the centralisation–decentralisation slider, and that position — not the fashion — determines your role model, your RACI, and what analysts and engineers are allowed to do. Answer that before naming the model.

**Source.** `11_dg_program_themes/domains-and-data-mesh.md` — the slider as the key strategic decision, and maturity ≠ complexity.

**Trap.** Announcing a mesh. Distributing people into domains changes the org chart, not the behaviour.

---

### 22. In a mesh, what must stay central? `L2` `domains`

**Answer.** Base checker coverage and incident generation, without exception — "delegating that to the domains is a risky story: it simply won't start." Everything else is negotiable by the slider position. The companion decision is environment design: separate archive, sandbox and production, where sandboxes carry lower documentation requirements but hard restrictions — no sharing objects outside the team, no schedules.

**Source.** `11_dg_program_themes/domains-and-data-mesh.md` — what stays central, and environment design (day 3–4, transcript).

**Trap.** A percentage split of responsibilities. The answer is a named list of what never leaves the centre.

---

### 23. Our domains would be 90% the org chart. Is that a problem? `L3` `domains`

**Answer.** It is the standard temptation and the base names it: domains are very often 90–95% close to the org-structure split, and the pull is to not define domains at all — just map object owners onto departments. That works until the org chart changes, which it does faster than the data does. The practical test is the spreadsheet trick: three columns — domain, subdomain, responsible person — because "when you start filling in the responsible people, that is when you understand what the structure is". Where the person is obvious, the org chart was fine; where you stall, you found a real domain boundary.

**Source.** `11_dg_program_themes/domains-and-data-mesh.md` — the org-chart shortcut and the spreadsheet trick (day 3, transcript).

**Trap.** Designing domains from a reference model. The base's own answer is that an LLM drafts a typical domain structure better than a consultant does — the value is in the ownership column, not the taxonomy.
