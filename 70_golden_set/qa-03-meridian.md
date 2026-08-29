---
type: eval
company: Meridian Bank
theme: a DG function that exists and does not work
items: 20
---

# Meridian Bank — 20 questions

30 000-person retail bank. Four years of DG, 60 stewards with no time, a half-empty catalog, 900 glossary terms, a customer who exists four times, and a new CDO asking what any of it changed.

---

### 1. What does the KB mean by "declared but not resourced"? `L1` `audit`

**Answer.** The most common real state of a governance program: described well and backed by nothing — roles named without time, targets set without capacity, policies written without an owner. The audit rule is not to average that into a middling score but to score the substance and attach the flag, then carry every flagged dimension into the gaps list, because unfunded governance is the most reliable predictor of program failure in this base's field evidence.

**Source.** `skills/dg-strategy/SKILL.md` — AUDIT scoring nuance.

**Trap.** Scoring Meridian's steward network as "partial". It is fully declared and fully unresourced, which is a different finding.

---

### 2. What is metric theatre? `L1` `metrics`

**Answer.** Reporting the *quantity* of governance — number of standards, glossary terms, owners, stewards, policies — instead of business impact. The test question is whether any headline number can legitimately go *down* for a good reason; if none can, you are counting activity. Meridian's committee slide of rising steward and term counts is the textbook instance.

**Source.** `50_failure_catalog.md` — Metric theatre; `11_dg_program_themes/maturity-and-metrics.md`.

**Trap.** Suggesting better activity metrics.

---

### 3. What is the difference between a custodian and a steward here? `L1` `roles`

**Answer.** The custodian is the person who already creates and maintains the object — usually an engineer or analyst — and carries description, quality, freshness and incident response as part of that work. The steward is a business-side curator of meaning. The field finding the base keeps repeating: the custodian model works, the steward-alone model fails.

**Source.** `11_dg_program_themes/roles-and-operating-model.md`; `11_dg_program_themes/dg-kitchen-research.md`.

**Trap.** Presenting them as equal halves of a standard model. The base has a clear preference and states it.

---

### 4. What is the standards spiral? `L1` `frameworks`

**Answer.** More policies → worse navigation → lower understanding → lower compliance. Each new regulation, data type and self-service wave adds policies, and the loop tightens. The counter-move is policy minimalism: new policy only when needed, archive when stale, and push the rule into the tool so the policy itself becomes unnecessary.

**Source.** `11_dg_program_themes/dg-frameworks.md` — policy minimalism (day 6, slides p.118–119).

**Trap.** Proposing a policy consolidation project. That is another policy.

---

### 5. What does the base say a data catalog's value depends on? `L1` `catalog`

**Answer.** It is hostage to adjacent maturity — self-service BI, data products, contracts, ownership and DQ management — and unlocks only as those mature. Stated at its sharpest: the benefit of a data catalog is often lower than the cost of producing and supporting it.

**Source.** `11_dg_program_themes/data-catalog.md` (day 4, slides p.42–44).

**Trap.** Answering "on metadata coverage". Coverage is the symptom Meridian is already optimising.

---

### 6. Sixty stewards, near-zero time spent. Fix the model or fix the people? `L2` `roles`

**Answer.** Neither — fix where the time is recorded. A role without a line in someone's objectives is a wish, and governance added to a job description with nothing removed is the standard way this fails. Two moves: switch to the custodian model so responsibility sits with whoever already touches the object, and put the governance share into the *manager's* objectives, not the steward's, because the manager allocates the time. Then test it: ask what happens at the performance review if the person did no governance work. If the answer is "nothing", the role does not exist.

**Source.** `11_dg_program_themes/roles-and-operating-model.md`; `50_failure_catalog.md` — unfunded governance.

**Trap.** Steward training. Meridian's stewards are not confused, they are unfunded.

---

### 7. The catalog is 40% described and mostly auto-generated. Rescue it or write it off? `L2` `catalog`

**Answer.** Neither in one move. Auto-generated descriptions at roughly 75% accuracy are plausible enough to poison the layer without a gate, so the first action is to stop counting them as coverage and separate verified from inferred. Then narrow: describe the critical perimeter properly rather than the estate broadly. Writing off a purchased catalog is politically expensive and usually unnecessary — the tool is rarely the defect.

**Source.** `10_ai_era_themes/context-governance.md` — the 75% figure and candidate status; `11_dg_program_themes/data-catalog.md`.

**Trap.** Launching a documentation campaign to raise coverage from 40% to 80%.

---

### 8. Nine hundred glossary terms, unread. What do we do with them? `L2` `definitions`

**Answer.** Archive most and keep a working registry of the definitions that are actually disputed — typically thirty to fifty for a company this size, not nine hundred. The base's position on glossaries is unusually blunt: they are the hardest adjacent component to launch, the only one requiring active business participation, and "reserved for the mature" — a nice suit, not a starting point. A term nobody argues about does not need governing.

**Source.** `11_dg_program_themes/getting-started.md` — glossary as reserved for the mature; `10_ai_era_themes/semantic-layer.md` — glossary adoption difficulty.

**Trap.** A glossary clean-up project that reviews all 900 terms.

---

### 9. The quarterly committee produces minutes and no change. Reform it or close it? `L2` `bodies` `gap`

**Answer.** Re-found it rather than duplicate it: change the chair to whoever holds real leverage — in a regulated bank, the risk or compliance side — strip the agenda to disputes and prioritisation, and kill status reporting, because status reports are what filled the time instead of decisions. A new body created next to the old one reads as a duplicate and splits an already weak mandate. Note the base's limit here: `60_roadmap.md` A4 records that this KB teaches how to *create* governing bodies and has nothing written on reviving or burying a dead one — the answer above is the intended fix, not yet a documented method.

**Source.** `11_dg_program_themes/roles-and-operating-model.md` — bodies and rituals; `60_roadmap.md` — A4 as an open gap.

**Trap.** Proposing a new Data Council alongside the existing one.

---

### 10. Single customer view is on its second attempt. How do we not fail again? `L2` `mdm` `gap`

**Answer.** Cut the perimeter until it is finishable — one line of business, one country, a pilot rather than a program — and decide in advance what is explicitly *not* a golden record for everyone, because cross-line agreement on the golden record is what kills these projects. Beyond that, be honest: **this base has no method for MDM or identity resolution.** `60_roadmap.md` B1 lists it as the largest subject gap, and the material available is the failure pattern (30-year payback from polishing the savings side) rather than a design.

**Source.** `60_roadmap.md` — B1; `50_failure_catalog.md` — ROI inflation by polishing the savings side; `51_numbers.md` — the bank MDM reference case.

**Trap.** Producing an MDM architecture. It would be textbook content, not KB content.

---

### 11. What should we report to the board instead of steward counts? `L2` `metrics`

**Answer.** Operational metrics with named owners, reported against a baseline or year-on-year rather than as a bare level: share of critical data with defined ownership, metadata completeness *and* age, incident resolution rate and speed, health scores kept distinct from DQ scores. If you must use proxies, say out loud that they are proxies — unlabelled, they are the polite version of metric theatre. For a bank the strongest single line is days without incidents in critical regulatory reporting.

**Source.** `11_dg_program_themes/maturity-and-metrics.md` — operational metrics (day 6, slides p.27); `50_failure_catalog.md` — Metric theatre.

**Trap.** Replacing counts with percentages of the same counts.

---

### 12. DQ checks exist only on the regulatory perimeter. Expand? `L2` `dq`

**Answer.** Not broadly. Every check costs money, and coverage reported as the headline DQ number is easy to hack while auditing checker quality to fix that is already overkill. Expand along consumption rather than along the estate: the objects the board and the regulator actually consume, each with a named person who receives the alert. Alerting aimed at nobody is the same as no check.

**Source.** `11_dg_program_themes/data-quality.md` — coverage-metric theatre (day 4, slides p.143) and the four things that matter more.

**Trap.** A coverage target such as "80% of critical tables checked by Q4".

---

### 13. The new CDO asks what four years of DG changed. What is the honest answer? `L3` `metrics`

**Answer.** Probably: the artefacts grew and nothing measurable moved — and the base's own evidence says that is the industry norm rather than a Meridian failure. Peer accounts of DG effectiveness are "assessments are rather emotional; there are almost no examples of comprehensive effectiveness and results analysis" — one company reports "it gave positives", another "entropy is decreasing", a third cannot assess time-to-market "because nobody tracks Jira properly". The distinguishing move is to be the exception: one peer that actually measured search duration via support chat versus catalog statistics × request volume × analyst payroll got a green light for further investment.

**Source.** `11_dg_program_themes/maturity-and-metrics.md` — peer evidence (day 6, slides p.34).

**Trap.** Assembling a retrospective impact story from the artefacts produced.

---

### 14. Should we keep the DG function at all? `L3` `getting-started`

**Answer.** The question is legitimate and the base does not flinch from it: a funded program inherits the burden of proving payback annually, a large fintech in the field evidence cut its entire DG team including stewards and catalog support, and the author's own structural defence was that there was no dedicated DG FTE to cut because the work was smeared across teams. For a regulated bank the argument for keeping it is not efficiency but the regulator — that is one of the three real ROI zones. Keep it, re-point it at the regulatory perimeter, and stop defending it on productivity grounds.

**Source.** `50_failure_catalog.md` — over-promising the payback, the fintech cut (day 2, transcript); `11_dg_program_themes/maturity-and-metrics.md` — three real zones.

**Trap.** Defending the function with the benefits wheel.

---

### 15. Where is the real leverage in a bank — CDO, CIO, or risk? `L3` `sponsorship`

**Answer.** Wherever an external deadline already sits, which in a regulated bank is risk and compliance. The base's sponsorship gates are 1 of CDO/CTO/CFO/CEO to start an MVP and 2 of 4 plus the domain owner to scale, but it also notes that in tech the CDO role often does not exist and that sponsorship is markedly easier where it does. Meridian has a CDO, which is an advantage — but the CDO's mandate over other people's time is weaker than a regulatory finding.

**Source.** `11_dg_program_themes/getting-started.md` — sponsorship gates and the CDO note (day 2, slides p.51, 54, 64).

**Trap.** Routing everything through the new CDO because the title exists.

---

### 16. Is our maturity model useful or is it bureaucracy? `L3` `maturity`

**Answer.** It depends on one thing: whether per-domain scores sit in top management's annual goals. A model the company has *appropriated* works as an instrument; a model that is presented and never wired into anyone's objectives is bureaucracy, and the sceptics in the room are right. The other half of using it correctly is subtractive — colour in what you do *not* need first, then current state, then read the development zone off the gap.

**Source.** `11_dg_program_themes/maturity-and-metrics.md` — appropriation test and the subtractive first move (day 6, transcript; day 2, transcript).

**Trap.** Re-running the assessment to get a fresher score.

---

### 17. Everything depends on everything. What is the correct order? `L3` `sequencing`

**Answer.** Governance and ownership first, then trusted data, then AI readiness, then the BI content funnel, with self-service and agentic interfaces last — and kill-gates blocking launches until prerequisites hold. For Meridian specifically that means ownership with recorded time before catalog coverage, and definitions before the single customer view, because identity resolution without agreed definitions reproduces the 2022 failure with better tooling.

**Source.** `README.md` — the stack-rank freeze order and kill-gates; `30_graph/objects.yaml` — the triad and its relations.

**Trap.** Running ownership, catalog, MDM and DQ in parallel because all four are urgent.

---

### 18. Give us a benchmark: how many stewards should a 30 000-person bank have? `L4` `trap` `roles`

**Answer.** This base has no such benchmark and would be wrong to invent one — headcount ratios are exactly the kind of number `51_numbers.md` exists to prevent being quoted without a source. What it offers instead is the question that replaces the ratio: how much time is recorded, in whose objectives, for which objects. Sixty stewards at zero hours is a smaller governance capacity than four custodians at ten percent.

**Source.** `51_numbers.md` — standing warning on untagged numbers; `11_dg_program_themes/roles-and-operating-model.md`.

**Trap.** Producing a ratio such as one steward per 500 employees.

---

### 19. Our privacy officer wants a data-classification and retention policy from you. `L4` `trap` `gap`

**Answer.** This base cannot produce it, and saying so is the correct output. Privacy, PII and special-category data have around a dozen incidental mentions and no material; retention exists only as content hygiene with the legal layer — mandatory retention, deletion obligations, what may not be archived away — entirely absent. Both are logged in `60_roadmap.md` as B2 and B3, filled by interview rather than generation, precisely because a well-written privacy chapter assembled from general knowledge is indistinguishable from a textbook.

**Source.** `60_roadmap.md` — B2, B3, and the "what NOT to do" rule.

**Trap.** Writing a plausible classification scheme. It would read well and be ungrounded.

---

### 20. Which of our sixty stewards should we fire? `L4` `trap` `roles`

**Answer.** None on this evidence, and the framing is the finding. The base's diagnosis of a non-working steward network is structural — time that was never allocated, a body that reviewed counts instead of deciding, and a model the field evidence says fails on its own — not individual. Removing people from a role that was never resourced replaces an unfunded network with an unfunded gap and adds a political cost you will need later. The move is to change what the role is and where its time is recorded, then see who is left doing it.

**Source.** `11_dg_program_themes/roles-and-operating-model.md`; `50_failure_catalog.md` — unfunded governance as the failure predictor.

**Trap.** Producing selection criteria. The question assumes a people problem the evidence does not support.

---

### 21. The catalog is bought and nobody opens it. How do we raise adoption? `L3` `catalog`

**Answer.** Not by filling it. Adoption is hostage to the same maturity the purchase was: a catalog earns traffic when the objects in it have owners, statuses and consequences, and until then it is a directory of things nobody is accountable for. Three moves in order: describe the critical perimeter properly instead of the estate broadly; make the certified status visible where people already choose a source, not only inside the catalog; and intercept creation — if nothing catches the person at the moment they build a new object, the catalog stays a place you visit deliberately, which nobody does twice.

**Source.** `11_dg_program_themes/data-catalog.md` — value hostage to adjacent maturity; `10_ai_era_themes/certified-core-layer.md` — the reuse nudge and status visibility.

**Trap.** A coverage campaign or an adoption KPI. Both measure the catalog, not the decision it was supposed to change.

---

### 22. Should the catalog run our review workflow, now that we have it? `L2` `catalog`

**Answer.** No. Preparation, review and fixes belong in domain cabinets; the catalog shows public status. Mixing them turns it into a workflow tool it was never designed to be — a named failure in this base — and it also couples your process to a vendor's roadmap. Keep the catalog as the place trust is *published*, not the place it is *produced*.

**Source.** `10_ai_era_themes/certified-core-layer.md` — running the operational process inside the catalog (day 3, slides p.119).

**Trap.** "It has a workflow module, so we should use it." That is the vendor's argument, not yours.

---

### 23. What actually gets people into the catalog on day two? `L2` `catalog`

**Answer.** Search that answers a question they already had. The strongest measured case in the field evidence is exactly that: one peer compared search duration via support chat against catalog search statistics, multiplied by request volume and analyst payroll, and got a green light for further investment. The mechanism underneath is that the catalog beat the chat — if asking a colleague is still faster, adoption is a training problem you cannot train your way out of.

**Source.** `11_dg_program_themes/maturity-and-metrics.md` — the peer who measured (day 6, slides p.34); `11_dg_program_themes/data-catalog.md` — the legitimate no when chats suffice.

**Trap.** Onboarding sessions. They move the number for a month.
