---
type: eval
company: Nordwind Logistics
theme: whether a program is needed at all
items: 20
---

# Nordwind Logistics — 20 questions

Asset-heavy 3PL, 12 000 people, near-zero data maturity, no incident, no regulator. The CEO said the words "data governance" and nothing else happened.

---

### 1. What is data governance, in one sentence, without DMBOK vocabulary? `L1` `getting-started`

**Answer.** An organisational overlay and tooling that focuses and coordinates resources so data work gets done and survives, instead of dangling forever in individual teams' roadmaps. The fuller definition worth keeping is Villar & Kushner's: a cross-functional program for *critical* data in service of company goals — with the corollary that if it does not help the goals, it may not be needed.

**Source.** `11_dg_program_themes/getting-started.md` — the deflationary definition (course day 2, slides p.65) and the Villar & Kushner definition (day 1, slides p.40–42).

**Trap.** Reciting the DAMA wheel's eleven knowledge areas. The KB stamps that wheel "bad framework, explains nothing" and notes that read literally it is a bill for eleven programs.

---

### 2. What is "common-sense DG" and how is it different from a DG program? `L1` `getting-started`

**Answer.** Common-sense DG is the set of sensible things existing teams do without budget: platform clean-up using usage statistics, basic DQ monitoring, data access rules, git-driven core-model documentation. A program is defined financially — you were given a budget, a manager, steward roles, money for a catalog. The KB's research finding is that most leading companies live in chaos while doing isolated sensible things, and they do not break.

**Source.** `11_dg_program_themes/getting-started.md` — "common sense DG" from 20+ tech-company interviews (day 2, slides p.53); the financial definition of formalised DG (day 5, transcript).

**Trap.** Treating common-sense DG as a consolation prize. The KB calls it the default, not the fallback.

---

### 3. What is "natural DG"? `L1` `getting-started`

**Answer.** The state every company is already in: data work happens, ownership is implicit, rules are unwritten but real. It is the first stage of the evolutionary path — natural DG → common-sense DG → DG MVP → land and expand — and naming it matters because it stops the conversation starting from zero.

**Source.** `11_dg_program_themes/getting-started.md` — staged flow.

**Trap.** Describing it as "no governance". A company with 12 000 employees running on an ERP has governance; it is just nobody's job.

---

### 4. Owner, steward, custodian — what is the difference? `L1` `roles`

**Answer.** Owner is accountable for the data object and its rules; steward is the business-side role that curates meaning and quality; custodian is the technical role that operates and maintains it. The KB's field finding is sharper than the taxonomy: the custodian model works and the steward-alone model fails, because the custodian is the person who already touches the object, while a steward without recorded time is a job description entry.

**Source.** `11_dg_program_themes/roles-and-operating-model.md`; `11_dg_program_themes/dg-kitchen-research.md` — custodian works, steward alone fails.

**Trap.** Presenting the three-role model as something to roll out. At Nordwind's maturity, naming a custodian per critical object is the whole of it.

---

### 5. What is a DG MVP and why run one if approval would be easy? `L1` `getting-started`

**Answer.** An MVP is proof to management that your concept — roles, tools, initiatives — makes sense. The KB says to run it even when approval is easy, for three reasons: it knocks the ideas against reality, it produces a base of concrete themes for scaling, and it brings value forward. Exit criteria are two of four packaged outcomes, a C-level sponsor, and interest from another domain owner.

**Source.** `11_dg_program_themes/getting-started.md` — MVP purpose and exit criteria (day 2, transcript; day 6, slides p.104).

**Trap.** Skipping the MVP because the CEO already said yes. A yes based on a conference talk is not a mandate; it is a sentence.

---

### 6. The CEO said "look into data governance". Where do we start? `L2` `getting-started`

**Answer.** Not with a program. Start by proving one is needed: run the 12-statement self-assessment, where five or more relevant statements suggest a program is cost-effective. In parallel, start common-sense DG on platform resource — usage-based clean-up, a DQ floor of nulls/freshness/completeness, and a registry of the marts you consider significant with a responsible techie and a responsible business person on each. The KB's blunt version: for many companies that registry *is* eighty percent of the governance actually required.

**Source.** `11_dg_program_themes/getting-started.md` — 12-statement test, threshold 5; minimal viable governance (day 3, transcript).

**Trap.** Producing a target operating model and a roadmap in week one. The framework belongs at the implementation stage, after the pains are understood.

---

### 7. How do we test whether we need a program at all? `L2` `getting-started`

**Answer.** Three checks. The 12-statement test with its 5-of-12 threshold. The pre-start question: is the *absence* of built-out DG a current constraint, or are there more pressing problems and the chaos simply is not big enough to hurt yet. And the cross-functionality trigger: isolated domains that never need each other's data need no program. The answer space has three values, not two — "not at all", "partially", "full-scale".

**Source.** `11_dg_program_themes/getting-started.md` — the pre-start slide (day 2, slides p.23), three answers (day 1, slides p.103).

**Trap.** Answering "yes, every company needs data governance."

---

### 8. Three WMS systems with no common master. Is that a reason to start MDM? `L2` `mdm` `gap`

**Answer.** It is a reason to define one shared identifier for the objects that cross warehouse boundaries — shipment, client, SKU — not to start an MDM program. The KB's position on the archetypes: one domain × many processes is the master-data archetype, but it also records that the MDM fashion passed a decade ago while its problems remained, and that the anti-case to memorise is a 30-year payback from an MDM investment where the savings side was polished instead of the revenue side recomputed. **This base has no method for MDM or identity resolution** — that is a known gap in `60_roadmap.md` (B1), and the honest answer names it rather than improvising a program.

**Source.** `11_dg_program_themes/getting-started.md` — archetypes; `50_failure_catalog.md` — ROI inflation by polishing the savings side; `60_roadmap.md` — B1.

**Trap.** Designing an MDM roadmap. The base cannot ground it.

---

### 9. Our only DWH engineer is a single point of failure. Is that a DG problem or an HR problem? `L2` `roles`

**Answer.** Both, and the DG half is the tractable one. The failure pattern in the KB is precisely this: work that lives in one person's head and in scripts nobody else can read. The moves that apply at Nordwind's scale are git-driven documentation of the core model — a common-sense DG project requiring no budget — and naming a second person as custodian for the handful of objects finance actually depends on. That is documentation by criticality, not documentation of everything.

**Source.** `11_dg_program_themes/getting-started.md` — common-sense DG project list; documentation by criticality in the "gorgeous minimum".

**Trap.** Proposing a full metadata initiative to solve a bus-factor problem.

---

### 10. A vendor is pitching us a data catalog. Now? `L2` `catalog`

**Answer.** No. Catalog value is hostage to self-service BI, data products, contracts, ownership and DQ maturity, and unlocks only as those mature; the sharpest framing in the KB is that the benefit of a catalog is often lower than the cost of producing and supporting it. The buy trigger is a U-curve over data-team size — realistically 100+ analysts — and Nordwind has six reporting specialists. Start on existing tools; a registry in Excel is a legitimate first catalog.

**Source.** `11_dg_program_themes/data-catalog.md` — benefit-below-cost framing (day 4, slides p.42–44), the U-curve and the 100+ analyst threshold (day 2, slides p.35).

**Trap.** "A catalog will give you visibility into your estate." It will give you an empty catalog.

---

### 11. Where do we start on data quality from zero? `L2` `dq`

**Answer.** With a floor, not a program: nulls, freshness, completeness on the objects finance actually uses. The KB's caution is that every check costs money and that four things matter more than DQ dashboards — cross-role agreed processes for defining DQ metrics, slogans from authoritative management, bad-data alerting aimed at named people, and energy focused on important data — otherwise you drown in heavy DQ bureaucracy.

**Source.** `11_dg_program_themes/data-quality.md` — the four things more important than DQ dashboards (day 4, slides p.144); `11_dg_program_themes/getting-started.md` — the DQ floor of nulls, freshness and completeness.

**Trap.** Buying a DQ tool or writing a quality policy first.

---

### 12. Who should be on the MVP team? `L2` `roles`

**Answer.** Two or three leads or seniors from DWH/BI with a systemic mindset and at least two years in the company. Tenure is not a nicety: the KB says the leader must be an authoritative old-timer, because nobody lets a newcomer seriously change their processes — you can hire from the market, but then you wait until they become one.

**Source.** `11_dg_program_themes/getting-started.md` — MVP team profile; the old-timer rule (day 6, slides p.104).

**Trap.** Recommending an external hire or a consultancy to lead it.

---

### 13. Our business model does not really depend on data. Does that change the answer? `L3` `getting-started`

**Answer.** It changes it more than any other fact on the table. The KB states plainly that if the business model does not depend on data, DG will be hard both to justify and to defend in budget cuts — and that chaos is survivable with a hidden cost, two to three years of accumulation while the critical things still ship. For Nordwind the defensible scope is narrow and operational: the objects finance and operations depend on daily, kept intact, with a named person each. Anything wider will not survive the first budget review.

**Source.** `11_dg_program_themes/getting-started.md` — "if the business model doesn't depend on data…" (day 3, transcript).

**Trap.** Treating low data dependence as a maturity problem to be fixed by the program.

---

### 14. Money would probably be given if we asked. Should we ask? `L3` `getting-started`

**Answer.** Probably not yet, and the reasoning is counter-intuitive. Once you have a funded program you inherit the burden of proving payback annually; in a company that scrutinises money closely it can be better *not* to form a separate DG team, and companies sometimes hide this work inside teams that already have a clearer basis for existing. Nordwind has no incident, no regulator and no business case — taking budget now means being asked next year what it bought, with nothing measured to answer from.

**Source.** `11_dg_program_themes/getting-started.md` and `50_failure_catalog.md` — the funded-program inversion (day 5, transcript).

**Trap.** "Take the budget while the CEO is interested." The KB's own author names this as the move that creates a line item to cut.

---

### 15. Certify marts, reports or metrics first? `L3` `certification`

**Answer.** Marts first, then reports, then metrics — even though reports feel closer to the business and are the natural place a BI leader starts. The failure this ordering prevents has its own entry in the catalog: certifying reports built on uncertified marts stamps trust onto a foundation nobody checked.

**Source.** `10_ai_era_themes/certified-core-layer.md` — sequencing lesson (day 3, transcript); `50_failure_catalog.md` — "Certifying reports before marts".

**Trap.** Starting with the CFO's dashboard because it is visible.

---

### 16. What should we call this so it is not rejected? `L3` `naming`

**Answer.** Not "data governance" — going in under that flag fails in about ninety-five percent of cases because business does not want to understand what it is. Attach the work to an initiative that already has money and name the pain rather than the discipline. "Data management sync" lands better than "committee" and works identically. "Certification" is fine as a word and needs no euphemism.

**Source.** `11_dg_program_themes/getting-started.md` — the 95% figure (day 2, transcript); `11_dg_program_themes/dg-frameworks.md` — naming hygiene, with the certification flag withdrawn.

**Trap.** Renaming everything into euphemisms until nobody knows what is being proposed.

---

### 17. We have no incident to build a case on. How do we build one? `L3` `business-case`

**Answer.** Bottom-up. Map use cases onto the value-adding process flows, score impact × feasibility, keep at most twenty to thirty. The counter-intuitive strength is the pile: when twenty cases each individually "doable without DG" accumulate, together they demonstrate a systemic problem. Only the direct economy — infrastructure saved by deleting redundant objects — is fully defensible without an attribution argument. And expect a modest total: a truthful DG ROI rarely looks impressive next to product economics.

**Source.** `11_dg_program_themes/getting-started.md` — bottom-up assembly (day 2, slides p.47–49); `11_dg_program_themes/maturity-and-metrics.md` — the honest-total warning.

**Trap.** Manufacturing an incident narrative from a near-miss.

---

### 18. Just give us the ROI number for implementing DG at our size. `L4` `trap` `roi`

**Answer.** There is no such number and this base refuses to produce one. Financial ROI from data quality is close to unmeasurable and "will almost never be the sexy number for which you'd be handed a real budget"; the registry `51_numbers.md` records that no defensible public DG ROI figure exists in the source material, and the author's own figure is withheld deliberately. What can be produced is a structure: possible losses against the cost of preventing them, with the decision taken when minimal losses exceed maximal costs — and, for Nordwind, that model needs measurements the company has not taken.

**Source.** `51_numbers.md` — "Any ROI figure the author is willing to defend publicly" listed under what is not measured; `11_dg_program_themes/maturity-and-metrics.md`.

**Trap.** Any number. A percentage, a multiple, a benchmark applied to headcount.

---

### 19. Draw us a three-year target data architecture. `L4` `trap` `frameworks`

**Answer.** Not yet, and the refusal is methodological rather than coy. A framework drawn before the pains analysis becomes an aesthetic object — the warning printed in red on the source slide is "this is not yet a DG implementation project, it is an abstract mock-up of how it works", and the KB calls it the most-ignored line in the deck. Sketch the architecture at the implementation stage, once the problems, goals and organisational model exist. For Nordwind, the honest artefact today is a one-page list of the objects that must not break.

**Source.** `11_dg_program_themes/dg-frameworks.md` and `50_failure_catalog.md` — "Framework theatre".

**Trap.** Producing a layered diagram. It will be accepted, admired and never used.

---

### 20. Which catalog vendor should we buy? `L4` `trap` `catalog`

**Answer.** Wrong question at this stage, and the base does not recommend vendors in any case. What it ships is a selection *method*: weight the criteria, use an LLM for pre-scoring, shortlist two or three, then score on your own pilot — with the Eckerson evaluation-criteria workbook and the author's adapted comparison sheet as the instruments. Applied to Nordwind the method returns "not now" before it returns a shortlist.

**Source.** `11_dg_program_themes/data-catalog.md` — Eckerson criteria and the recommended flow (day 4, slides p.33–34, 125); `12_templates/templates.md`.

**Trap.** Naming a product. The KB contains vendor material only as marketing to be discounted.

---

### 21. What goes in a data strategy the board will actually read? `L3` `strategy`

**Answer.** A Summary that can be read alone and stands as the whole argument — vision, the named problems, the solutions by stream, the goals, what you deliberately will not do, the effect, the decision you need from them, the first step and the cost of doing nothing. Then the sections, for the people who will execute or review it. Prose and bullets in the Summary, no tables: a table on the opening page reads as a report, and an argument assembled from cells does not survive being skimmed. Write the sections first and compress upward — the Summary is written last and is the hardest page.

**Source.** `skills/dg-strategy/SKILL.md` — the two-part document and the Summary contents.

**Trap.** Opening with context or a table of contents. The reader must meet the ask before the background.

---

### 22. How long should it be? `L2` `strategy`

**Answer.** A Summary of one to two pages plus roughly a page per section — about nine or ten pages with eight sections, fewer if the structure is trimmed, and the structure should be trimmed for a company of this size before any interviewing starts. Length is not the variable that matters, though: an answer that must *inform* can be short, and an answer that must *convince* carries its supporting evidence. The Summary convinces; the sections inform.

**Source.** `skills/dg-strategy/SKILL.md` — Phase 0 volume question and the section list.

**Trap.** Fixing a page count first. It is the output of the structure decision, not an input to it.

---

### 23. The board asks for one number. What do we give them? `L4` `trap` `roi`

**Answer.** Not a total. The shape of the effect, and one committed line — for most companies that is infrastructure saved by deleting redundant objects, because it needs no attribution argument and shows up in an invoice rather than a model. Everything else goes in as a range with its confidence tag, and the list of what must be measured to replace the estimate with a calculation goes in as the actionable part. A single number handed to a board becomes a promise by the third reader, and this base carries no defensible public governance ROI figure to hand over in the first place.

**Source.** `skills/dg-econ-effect/SKILL.md` — the committed fraction and the precision list; `51_numbers.md` — no defensible public figure.

**Trap.** Producing the number because they asked for one. That is the request the whole effect model exists to answer differently.
