---
name: dg-strategy
description: >
  Consult on, form, or audit a Data Governance strategy & tactics, grounded in
  the DG Board Knowledge Base (this repository). Triggers: "build a DG strategy",
  "audit our data governance", "review my DG program / roadmap", "DG tactics",
  "is our governance plan sound", "how should we approach <DG topic>", "advise
  on data governance", "прособери/проаудируй DG стратегию", "посоветуй по DG".
---

# DG Strategy & Tactics — consult, build, audit

Operating principle: **AI drafts — humans validate.** Every recommendation must be grounded in this repository's content (cite the file) or in the participant's own data; anything else is marked `[requires clarification]`. Never give generic consulting advice.

Grounding map: `../../README.md` (repo entry point), `../../30_graph/objects.yaml` (themes, relations, kill-gate order), `../../10_ai_era_themes/` and `../../11_dg_program_themes/` (substance), `../../12_templates/templates.md` (workshop instruments), `../../40_sources.md` (citable sources).

## Scenarios and triggers

| Scenario | Trigger examples | Shape |
|---|---|---|
| **CONSULT** | "how should we…", "does it make sense to…", "we have this situation…", "у нас кейс…", "посоветуй…" — a concrete question or case, no document, no ask to build | Dialogue: case → grounded answers with options → converge on a decision |
| **AUDIT** | "review our data strategy", "give feedback on our DG program", "проревьюй стратегию", or any strategy/roadmap document attached | 10-dimension scorecard → gaps → resequencing → quick wins |
| **FORM** | "build a DG strategy", "help me draft our governance plan", "собери DG стратегию" | Interview → diagnostic scorecard (sign-off) → 7-block strategy → 6-pager |

Routing: a document with the request → AUDIT by default; a question → CONSULT; an explicit ask to build → FORM. CONSULT escalates naturally — when the dialogue reveals the case is really a whole-program problem, offer to switch to AUDIT (if they have a strategy) or FORM (if they don't).

## Universal conventions (apply in every scenario)

- **Mid-flow document invitation.** As soon as context starts forming — after the case statement in CONSULT, after the first interview batch in FORM, at input collection in AUDIT — explicitly invite: *"If you have any existing documents — pain/landscape analyses, architecture notes, assessment results, prior strategies, survey exports — share them now; I will ground the work in them instead of re-asking."* Anything received is treated as participant data (quotable evidence), never re-asked.
- **End-of-flow visualization offer.** At the end of every scenario offer to render the result as a single-file HTML page for sharing: CONSULT — decision one-pager (case, options compared, chosen path, next steps); AUDIT — scorecard radar, chain-break map, resequenced roadmap; FORM — diagnostic scorecard, stack-ranked roadmap timeline, kill-gates board. Plain self-contained HTML, no build step.

---

## CONSULT — case consulting dialogue

1. **Take the case.** Ask for 3–5 sentences: what is being decided, who is involved, what has been tried, what constraint hurts. One clarifying batch max — this is a dialogue, not an interview.
2. **Invite documents** (universal convention above).
3. **Ground the answer.** Map the case to themes via `objects.yaml`; answer from the theme files' "What is it / Key terms"; defend positions with "Numbers for arguing with optimists"; check the case against kill-gates and the dependency chain — if the user is about to violate one (e.g., launching an AI assistant before semantic coverage), say so first.
4. **Give options, not verdicts.** 2–3 courses of action with trade-offs, each citing its KB grounding; recommend one and say why.
5. **Converge to a decision.** Fix the chosen option, name the first concrete step, and hand over the matching workshop template from `../../12_templates/templates.md` if one applies.
6. Offer the HTML one-pager; offer AUDIT/FORM if the case turned out bigger than a question.

---

## FORM — build the strategy

### Phase 0 — scope
- Depth: **Lite** (≈15 min, category-level diagnostic, key blocks) or **Full** (45–60 min, dimension-level diagnostic, all blocks).
- Reuse everything the user already has (survey, prior strategy, assessment) — do not re-ask. After the first interview batch, run the mid-flow document invitation (universal convention).

### Phase 1 — interview (batches of 2–3 questions)
1. Company context: size, industry, where data work lives organizationally.
2. Team & tooling: DWH/BI/governance roles present; catalog, semantic layer, AI assistant status.
3. Demand: user segments, self-service adoption, top-3 data pains.
4. Foundation: certified-data share, DQ state, core-layer maturity.
5. AI: what reached production; share of ad-hoc answerable with SQL + docs (field baseline: ~61%, see `11_dg_program_themes/../10_ai_era_themes/domain-knowledge-base.md`).
6. Constraints: budget, risk appetite, governance capacity.
7. 12-month ambition.

Then the mandatory self-assessment, 0–4 scale ("no/almost none" → "optimized"):
- Entry gate: the **5-of-12 test** from `../../11_dg_program_themes/getting-started.md` — if fewer than 5 hit, recommend Common-Sense DG instead of a program.
- Maturity: the 7 dimensions of `../../11_dg_program_themes/maturity-and-metrics.md` (Data informed → Driven → Led).
- AI-readiness overlay: semantic coverage, certified-data share, domain-context completeness, verify-gate capacity, eval practice (`../../10_ai_era_themes/`).

### Phase 2 — diagnostic (sign-off checkpoint)
Produce and confirm with the user before writing anything else:
- Maturity scorecard (7 dimensions + AI-readiness).
- **2–3 named breaks** in the chain `core → semantic → context → AI accuracy → self-service` — the strategy is the repair plan for these breaks.
- Position on delivery channels: centralized / self-service / agentic, current vs realistic 12-month target.

### Phase 3 — strategy document (7 blocks)

| Block | KB substance |
|---|---|
| 00 Diagnostics | scorecard from Phase 2 |
| 01 AS-IS | pain map, `getting-started.md` challenges canvas |
| 02 TO-BE vision | `dg-program-roadmap.md` (Program Map 3.0 stages), vision-statement template |
| 03 AI foundation | triad `certified-core-layer.md` → `semantic-layer.md` → `domain-knowledge-base.md`, wrapped in `context-governance.md` |
| 04 Trusted data | `data-quality.md`, `data-catalog.md`, certification |
| 05 Content & self-service | `bi-content-management.md` funnel, `library.md` |
| 06 Operations & people | `roles-and-operating-model.md`, `skills-hub.md` |
| 07 Transformation plan | stack-rank, timeline, metrics, kill-gates |

Per block: essence (2–4 sentences) → recommendation (DRAFT, grounded in participant data) → workstreams → maturity gates → templates from `../../12_templates/templates.md`.

Hard ordering rules:
- **Stack-rank freeze order** (freeze from the bottom, never the top): governance & ownership → trusted data → AI readiness (the triad) → BI content → self-service & agentic interfaces.
- **Kill-gates**: no AI assistant without semantic coverage of target domains + certified baseline; no self-service scaling without governance gatekeeping + DQ monitoring; no semantic layer without core foundation.
- **Dual track**: old-DG sustaining + new-AI exploring, ring-fenced to low-risk domains, measured by AI accuracy and human-validation overhead.
- Operations: LLM-architecture loops A–E (`llm-assistant-architecture.md`); coverage loop feeds the semantic backlog.
- Budget defense: `core → certified metrics → agent accuracy → self-service` + the "Numbers for arguing with optimists" blocks.

Close with a **6-pager**: vision · diagnosis · stack-rank · block summaries · metrics · risks + first step. Then offer the HTML visualization (universal convention).

---

## AUDIT — assess an existing strategy or program

Input: the user's strategy/roadmap/program doc, or an interview about the current program. Before scoring, run the mid-flow document invitation (universal convention) — pain analyses, landscape reviews and assessment exports often change scores by ±1. Score each dimension 0–2 (absent / partial / solid), citing evidence from their material and the KB file that defines "solid".

| # | Audit dimension | KB yardstick |
|---|---|---|
| 1 | Entry justification: is DG needed at this scale, is there a business case? | `getting-started.md` (5-of-12 test, business-case template) |
| 2 | Diagnostic base: measured AS-IS maturity, not vibes | `maturity-and-metrics.md` (7 dimensions, DDI) |
| 3 | Dependency-chain integrity: built in order core → semantic → context; no AI-before-foundation inversions | `objects.yaml` triad + kill-gates |
| 4 | Stack-rank sanity: what gets frozen under budget cut; is governance capacity funded at all | field lesson: 20% core target delivered 2% without capacity (`certified-core-layer.md`) |
| 5 | Role model: owner / steward / custodian defined and enforced | `roles-and-operating-model.md`; Kitchen check: custodian works, steward alone fails (`dg-kitchen-research.md`) |
| 6 | Stream coverage: which of the 12 roadmap streams / Program Map 3.0 stages are missing | `dg-program-roadmap.md` |
| 7 | Metrics honesty: outcome metrics vs activity metrics; anti-metric check (no "N prompts per week") | `maturity-and-metrics.md`, `skills-hub.md` |
| 8 | Content hygiene: archive → certify → promote funnel exists | `bi-content-management.md` |
| 9 | Context invariants: SSOT referenced not copied; machine output enters as candidate; verified ≠ servable | `context-governance.md` |
| 10 | Risk register: fragile chain, Jevons/AI-slop multiplier, Gartner 80%-failure default, kill-gates written down | `certified-core-layer.md`, `context-governance.md` |

Output — **audit report**:
1. Scorecard table (10 × 0–2, total /20).
2. Top-5 gaps by severity, each with: evidence quote from the user's doc → KB yardstick → board deep-link.
3. Chain-break map: where their sequence violates the triad / kill-gates, and the resequenced order.
4. Quick wins (Common-Sense DG list from `getting-started.md`).
5. What to keep: explicitly name the strong parts — an audit that only criticizes gets ignored.
6. Offer the HTML visualization of the report (universal convention).

---

## Guardrails

- No generic advice; every claim cites a KB file or participant data.
- No invented numbers; missing data → `[requires clarification]`.
- Never write the full document before the Phase-2 scorecard (FORM) or the scorecard table (AUDIT) is confirmed.
- When challenged on "why so slow / why not just launch the agent" — answer with the numbers blocks (Spider 2.0 6%, 21%→95%+, 40%→85–95%, Gartner 80%).

## Installation

- **Claude Code**: copy or symlink `skills/dg-strategy/` into your project's `.claude/skills/` — the description above auto-triggers it. Keep the whole repository cloned so relative KB paths resolve.
- **Any other agent**: paste this file as instructions and give the repository root as a knowledge source.
