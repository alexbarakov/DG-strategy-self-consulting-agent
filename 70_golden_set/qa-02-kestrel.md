---
type: eval
company: Kestrel Games
theme: AI-era themes, engineer culture, semantic layer
items: 20
---

# Kestrel Games — 20 questions

800-person game studio. Excellent product analytics, no governance, ~140 SQL writers, six definitions of retention, and a CPO who wants an AI analyst in Slack this quarter.

---

### 1. What is a semantic layer, in the terms this base uses? `L1` `semantic-layer`

**Answer.** A thin layer between the warehouse and every consumer — human or agent — where business concepts are defined once as code and compiled into SQL on demand. It answers three questions: what a metric means, how it is calculated, and which cuts are legal. For an agent it is the difference between guessing business logic and resolving it.

**Source.** `10_ai_era_themes/semantic-layer.md` — "What is it".

**Trap.** Describing it as a BI feature or as "the dbt metrics layer we already have". The base distinguishes semantic layer (entities, measures, dimensions, automatic joins) from metric layer (declarative definitions on top).

---

### 2. What is context governance and how is it not data governance? `L1` `context-governance`

**Answer.** Data governance manages the data — quality, access, lineage. Context governance manages the layer of meaning an agent reads to reason: definitions, domain knowledge, metadata, situational context. Clean data is not yet trusted data; the agent must know what a number means and when not to use it.

**Source.** `10_ai_era_themes/context-governance.md`.

**Trap.** "It is RAG." Dumping documents into a vector store is explicitly named as not governance.

---

### 3. What is a Context Unit and what is a passport? `L1` `context-governance`

**Answer.** The atom of managed knowledge, carrying provenance, status, freshness TTL and a reference to the source of truth. Status moves inferred → candidate → verified → deprecated, and only a human promotes to verified. The SSOT is referenced, never copied.

**Source.** `10_ai_era_themes/context-governance.md` — components and the three invariants.

**Trap.** Treating "verified" as sufficient to serve. Verified is necessary but not sufficient; serving also depends on freshness and absence of conflict with the SSOT.

---

### 4. What are the loops A–E? `L1` `llm-architecture`

**Answer.** The operating loops of an LLM assistant architecture — the runtime view of how a question becomes a governed answer, with loop E covering access and security. In the KB they are used as the operating template for launching an AI channel, not as a diagram.

**Source.** `10_ai_era_themes/llm-assistant-architecture.md`; playbook row "AI channel launch & evals" in `skills/dg-strategy/SKILL.md`.

**Trap.** Over-claiming detail. The base's file on this is thin (~1k words) and `60_roadmap.md` C2 records it as needing the author's BI+AI course as its source.

---

### 5. What is the verify gate? `L1` `context-governance`

**Answer.** A domain curator judging machine-written drafts — gate work, not authoring work. It exists because extraction never trusts itself: machine output enters as a candidate only. Its health metrics are a verified share of ≥70% read together with a false-accept rate below 5%; coverage alone is meaningless.

**Source.** `10_ai_era_themes/context-governance.md` — verify gate, thresholds.

**Trap.** Reporting coverage without false-accept rate.

---

### 6. Our AI prototype answered 11 of 15 questions correctly. Is that ready to ship? `L2` `semantic-layer` `evals`

**Answer.** No — 73% on fifteen hand-picked questions is the demo regime the base warns about explicitly: every text-to-SQL demo works and production lies. The comparable field numbers are ~40% accuracy on real enterprise schemas, 6% for GPT-4o on Spider 2.0 against 86% on the academic benchmark, and 85–95% once a semantic layer is in the path. Fifteen questions is not an eval; a golden set with a measured false-accept rate is.

**Source.** `10_ai_era_themes/semantic-layer.md` — numbers for arguing with optimists; `10_ai_era_themes/context-governance.md` — eval loop.

**Trap.** Reading 11/15 as 73% accuracy in production. The sample is the problem, not the score.

---

### 7. Six definitions of retention across squads. Fix the definitions or build the layer? `L2` `semantic-layer`

**Answer.** The definitions, and the layer is how you keep them fixed. But check the trigger first: the base's heuristic is to count the BI developers and analysts hand-coding the same business logic — the pain is real only when dozens of independent teams reuse the same core data. With ~140 SQL writers and six live definitions of one metric, Kestrel passes that test, which most companies asking the question do not.

**Source.** `10_ai_era_themes/semantic-layer.md` — the counting heuristic (day 5, transcript).

**Trap.** Starting with a company-wide glossary. Glossaries are the hardest adjacent component to launch and the only part requiring active business participation.

---

### 8. Can we skip the semantic layer and go straight to the agent? `L2` `kill-gates`

**Answer.** You can, and the base predicts what happens: the agent hallucinates business logic regardless of model quality, and the failure mode is invention rather than refusal. The stack-rank order is governance and ownership → trusted data → AI readiness → self-service and agentic interfaces last, and the instruction is explicit: build the layer before the agents, not after them. Lost trust in an assistant is not recoverable on a second attempt.

**Source.** `30_graph/objects.yaml` — kill-gate order; `10_ai_era_themes/semantic-layer.md`.

**Trap.** "We will add the layer later once the agent proves value." The agent's first wrong answer to a founder is the value it proves.

---

### 9. Marketing attribution disagrees with finance by 8%. Governance problem or a modelling problem? `L2` `definitions`

**Answer.** A definitions problem with an ownership vacuum behind it, and the fix is not to determine which is correct. Two different definitions can both be right for different applications; what is missing is a named owner per definition and a recorded decision about where each applies. The base's memorable case is a company with two metrics, "sales" and "revenue", where nobody could say which was correct — the resolvable question is applicability, not truth.

**Source.** `10_ai_era_themes/semantic-layer.md` — glossary/definitions notes (day 4, transcript).

**Trap.** Convening a working group to pick the correct number.

---

### 10. Our culture rejects process. How do we introduce anything? `L2` `culture`

**Answer.** Accept the objection as data, not resistance — the base records it as the same sentence in different companies: imposed rules, distributed roles and routine rituals are considered bullshit, and DG "conflicts with tech-company culture". What works is the subbotnik mechanic: announce a clean-up event, appoint someone per domain, run it a month, reward participants — and afterwards observe that they were doing steward work. The goal is not the clean-up; the goal is to create a habit.

**Source.** `11_dg_program_themes/dg-kitchen-research.md` — the culture objection; `11_dg_program_themes/getting-started.md` — the subbotnik (day 2, transcript).

**Trap.** A stewardship rollout with training. Kestrel already failed that once, in one quarter.

---

### 11. Should we build a knowledge base for the agent, and out of what? `L2` `dkb`

**Answer.** Yes, and the cheapest high-yield material is already in your Slack. A few-shot Q&A base mined from support-chat history — typical question → which mart, metric or report, with caveats and a link — is the single strongest accuracy booster, "literally a base of hints". Add metric notes: human comments attached to anomalies, without which an agent asked "why did it fall" either says nothing or invents an answer you cannot distinguish from a real one.

**Source.** `10_ai_era_themes/context-governance.md` — few-shot base and metric notes (day 6, transcript and slides p.98).

**Trap.** Starting with documentation of every table.

---

### 12. What does certification mean for us if we have no catalog? `L2` `certification`

**Answer.** A status with a lifecycle, held wherever you already keep object metadata — a registry, a wiki, the warehouse itself. Keep the badge count small: every extra public status raises the user's cost of choosing a source, and three (Candidate / Certified / Degraded) is already generous. Certify marts before reports before metrics. In the AI era certification stopped being a ritual and became a prerequisite: the agent navigates users to certified objects first, and certification presupposes the good descriptions the agent needs anyway.

**Source.** `10_ai_era_themes/certified-core-layer.md`; `10_ai_era_themes/domain-knowledge-base.md` — certification as AI prerequisite (day 6, transcript).

**Trap.** Waiting for a catalog purchase to start certifying.

---

### 13. The CPO wants the assistant live in one quarter and has told the board. What now? `L3` `deadline`

**Answer.** Do not answer "you are not ready" — that advice is never taken and the launch happens anyway, unprepared. Instead: check the commitment against the kill-gates and name which are not passed; find the narrowest scope where the gates *do* pass — one domain, one user group, one question type — and make that the primary bet; add a parallel fallback delivering visible value on the same date without depending on the risky part, usually absorbing the top repeating questions into ready-made content. Depth over breadth is defensible to a board; a broken launch is not.

**Source.** `skills/dg-strategy/SKILL.md` — the deadline-constrained case, built on the accuracy numbers in `10_ai_era_themes/`.

**Trap.** Either capitulating to the date or refusing it. Both end the same way.

---

### 14. Agents will start querying the warehouse. What breaks? `L3` `ai-governance`

**Answer.** Infrastructure first. The base's prediction is that agent query share spikes — "agents join like crazy and not always elegantly" — so plan request filtering, sampling and quotas before the spike, not after. Second, economics: after the Wild West strategy comes the counting of burned tokens, and many agent scenarios will not pay off. Third, provenance: without an audit trail you cannot reconstruct which query, which definitions and which context version produced an answer.

**Source.** `10_ai_era_themes/ai-governance.md` — predictions to plan against (day 6, slides p.96).

**Trap.** Treating this as a cost-optimisation problem to solve later.

---

### 15. Is a company-wide metric tree worth building? `L3` `semantic-layer`

**Answer.** No. The base is direct: a strictly hierarchical tree is exactly what you will not get, real metric graphs are overlapping clouds with tangled links, and a single global tree "carries nothing but beauty". Domain-level trees are the working unit — and they earn their keep twice, as a navigator for factor analysis and as context for an agent answering "why did it move".

**Source.** `10_ai_era_themes/semantic-layer.md` — metric trees (day 5, slides p.30 and transcript).

**Trap.** Commissioning the company metric tree as a visible artefact for the board.

---

### 16. Do we need a data catalog at 140 SQL writers? `L3` `catalog`

**Answer.** You are past the usual trigger — the U-curve turns at roughly 100+ analysts — but the base adds a second condition: catalog value unlocks only as ownership, contracts, self-service and DQ mature, and its benefit is often lower than the cost of producing and supporting it. There is also a legitimate no in the field evidence: teams that work entirely inside their own domain and never go outside find chats sufficient. At Kestrel, squads *do* reuse core data, so the answer is yes — but after the definitions, not before.

**Source.** `11_dg_program_themes/data-catalog.md` — U-curve, hostage conditions, the legitimate no (day 4, transcript).

**Trap.** Buying the catalog as the first governance artefact because the headcount threshold is met.

---

### 17. AI auto-documentation would fill our metadata gap in a week. Why not? `L3` `context-governance`

**Answer.** Because ~75% accuracy is exactly plausible enough to poison the layer if there is no gate. Machine output enters as candidate; a domain curator promotes it. The base also records this as its single live unresolved dispute: one camp says re-checking auto-generated docs costs about as much as doing the mapping by hand, the other says it does not make mistakes, and nobody has published a number — `51_numbers.md` names measuring it as the most useful measurement anyone reading the base could go and take.

**Source.** `10_ai_era_themes/context-governance.md` — the 75% figure; `51_numbers.md` — verification cost of AI-generated metadata, unmeasured.

**Trap.** Shipping generated descriptions straight to verified because the samples read well.

---

### 18. Give us a target accuracy number to promise the board. `L4` `trap` `evals`

**Answer.** Not from this base as a promise. The numbers it carries are field references, not commitments: ~40% without a governed route, 85–95% with a semantic layer, 21% → 95%+ in Anthropic's agent evals, 25% → 80% for a domain assistant without versus with filled domain context. All of them are tagged by reliability in `51_numbers.md` and none of them is a forecast for Kestrel's schema. What you can promise is a measured golden set with a stated false-accept rate by a stated date.

**Source.** `51_numbers.md` — reliability tags; `10_ai_era_themes/semantic-layer.md`, `context-governance.md`.

**Trap.** Quoting 85–95% to a board. It is another company's number on another company's schema.

---

### 19. Write us the AI usage policy — we need something for legal by Friday. `L4` `trap` `ai-governance`

**Answer.** You can have it, and it will change nothing, which is the point worth making before Friday. Producing policy text collapsed to a prompt; the scarce thing is readers, and the standards spiral — more policies, worse navigation, lower compliance — is the predictable outcome. The three public anchors exist if you need them (NIST AI RMF, EU AI Act, ISO/IEC 42001), but what actually governs at Kestrel is a model and agent inventory with named accountable owners, risk tiering of scenarios, and an audit trail. Push the rule into the tool and the policy becomes unnecessary.

**Source.** `10_ai_era_themes/ai-governance.md` — anchors and what it lands as; `11_dg_program_themes/dg-frameworks.md` — the standards spiral, policy minimalism.

**Trap.** Delivering the policy without saying that a document nobody reads is the failure mode, not the deliverable.

---

### 20. Our stack is modern and our analytics is better than most. Does any of the classic DG material apply to us? `L4` `trap` `scope`

**Answer.** Partly, and the base should say which part rather than claim universality. What applies: ownership, definitions, certification, content hygiene, the culture findings — all of it is written for exactly your kind of company, since the source material comes from tech-company practice. What does not: the assumption of a budget fight, the committee machinery, and most of the regulated-industry framing. The base has never declared its intended reader out loud, and `60_roadmap.md` A2 lists that as its highest honesty-per-effort defect — so treat the classic half as scope-bound until it does.

**Source.** `60_roadmap.md` — A2, "the base never declares who it was written for"; `11_dg_program_themes/dg-kitchen-research.md`.

**Trap.** Answering "yes, the fundamentals are universal." They are not, and the base admits it in writing.
