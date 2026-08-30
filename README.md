# DG Strategy — self-consulting agent

Textual projection of the public Miro board **«Data Governance Program Guide»** (data nature / Alex Barakov): https://miro.com/app/board/uXjVMBRtQEA=/

Purpose: let an AI agent **consult on Data Governance and build DG strategies** grounded in this material. This README is the single link to give the agent; everything else is reachable from here by relative path.

Working principle: **AI drafts — humans validate.** An honest gap beats a padded chapter — nothing here is closed by generating plausible textbook content.

**Companion:** [BI+AI Strategy Builder](https://github.com/alexbarakov/BI-strategy-self-consulting-agent) — the BI/AI half of the same method. The two repositories are designed as a pair and share the same invariants.

## At a glance

| What | Size |
|---|---|
| AI-era themes + supporting frames | **6 + 4** |
| Classic DG themes synthesized from the program guide | **10** |
| Failure catalog — how DG programs actually die, with symptom triage | **45 in 7 families** |
| Numbers registry, every figure tagged by reliability | **175 rows** |
| Diagnostic question bank — probes, not a questionnaire | **81 questions** |
| Golden set — grounded questions from five invented companies | **100 questions** |
| Reading library across themes | **~90 links** |
| Runnable skills | **2** |

## Two ways to use this repository

**A. As a knowledge source (passive).** Add the repo or its URL to your agent's context and let it ground *other* tasks — answering DG questions, reviewing designs, preparing talks. Nothing to install; the agent follows "How the agent uses it" below.

**B. As runnable skills (active).** Two skills, each usable on its own:

- [`skills/dg-strategy/SKILL.md`](skills/dg-strategy/SKILL.md) — the strategy skill, three scenarios below.
- [`skills/dg-econ-effect/SKILL.md`](skills/dg-econ-effect/SKILL.md) — the **economic effect model**: answers "how much money is this?" in the shape a top manager actually reads — agreed possible losses against the cost of preventing them — and refuses the benefits that do not survive contact with finance. Runs standalone, as section 06 of a strategy, or in CHALLENGE mode against someone else's business case. Default output is an **expert estimate with an explicit precision marker**: every figure carries a confidence tag, and the list of what must be measured to replace the estimate with a calculation is the primary deliverable, not the appendix.

## Scenarios

| Scenario | When | What comes out |
|---|---|---|
| **CONSULT** | you have a concrete case ("how should we…") | a grounded dialogue with options and trade-offs, converging on a decision |
| **FORM** | you need a strategy | scoping → interview → the full document |
| **AUDIT** | a strategy or program already exists | 10-dimension scorecard, chain-break map, resequencing plan, quick wins |

FORM opens with three scoping questions before any interviewing:

1. **Which strategy?** — DG / BI / D&A / AI / mix. DG runs on this repository alone; BI and AI pair with the companion (its skill leads, this KB grounds governance); D&A and mixes use both — this skill leads, the builder supplies the BI/AI stream substance.
2. **Confirm the content structure** — the default skeleton is shown for trimming or reordering before work starts: a standalone **Summary** (vision, problems, solutions by stream, goals, what we deliberately do not do, the decision needed from the sponsor, first step and the cost of inaction), then flat sections **00 Context → 01 AS-IS on the Maturity Scorecard → 02 TO-BE beyond AI, closing with the streams of change → 03 Metrics & Goals → 04 Initiatives Portfolio → 05 Operating Model → 06 Effect of the Strategy → 07 Risks & Kill-gates**, then appendices. Metrics sit above the portfolio deliberately: an initiative earns its place by moving a named metric.
3. **Volume** — default is **compact** (a Summary plus about a page per section); options: a full wiki with every section expanded, or per-section delivery with review after each.

In every scenario the skill invites your existing documents (pain/landscape analyses, assessments) mid-flow and offers a single-file HTML visualization of the result at the end.

## Quickstart

```bash
# Claude Code: clone alongside your workspace and symlink the skill
git clone https://github.com/alexbarakov/DG-strategy-self-consulting-agent.git
ln -s "$PWD/DG-strategy-self-consulting-agent/skills/dg-strategy" ~/.claude/skills/dg-strategy
```

For any other agent: paste the `SKILL.md` as instructions and give the repository as a knowledge source. Plain Markdown plus one YAML graph — no build step, RAG-friendly chunking by design (one frame or theme per file).

## How the agent uses it (instructions for the agent)

0. **Something is going wrong / diagnosing a program** — start at `50_failure_catalog.md` (symptom triage), pull arguments from `51_numbers.md` (**never quote a `vendor` or `disputed` number as fact**), probe with `52_questions.md`.
1. **Answering a DG question** — find the theme in `30_graph/objects.yaml` (nodes and relations; visual in `30_graph/graph.md`), read the matching file in `10_ai_era_themes/` or `11_dg_program_themes/`; drill into per-frame detail in `20_dg_program_guide/` when needed. Quote definitions from "Key terms", defend positions with "Numbers for arguing with optimists", cite sources from `40_sources.md`.
2. **Running a workshop or artifact session** — pick a template from `12_templates/templates.md` (pains analysis, vision statement, domain classifier, scope/goals configurators, Data Mesh canvas, DDI, business case…), each with its board deep-link.
3. **Building or auditing a strategy** — run the full procedure in [`skills/dg-strategy/SKILL.md`](skills/dg-strategy/SKILL.md); the money model behind it is [`skills/dg-econ-effect/SKILL.md`](skills/dg-econ-effect/SKILL.md).
4. **Grounding BI/AI streams** — pull from the companion [BI+AI Strategy Builder](https://github.com/alexbarakov/BI-strategy-self-consulting-agent); its machine-readable map is `references/knowledge-map.yaml` inside that repository.
5. **Quoting a number** — take it from `51_numbers.md` and **carry its reliability tag with it**.
6. **Recommending reading** — use `10_ai_era_themes/library.md`; `40_sources.md` holds verification status per link.
7. **Referencing the visual** — every file's frontmatter carries a `miro:` deep-link; give it when the user wants the picture.
8. **Producing the deliverable** — always **in the user's language**. This KB is the source, not the output template. Missing facts become explicit `[missing data]` markers, localized to the output language, naming the source that would close them — never invented numbers.

## Map

| Path | Content |
|---|---|
| `30_graph/objects.yaml` | **Machine-readable graph**: themes, components, relations, statuses, frame ids. Start navigation here |
| `30_graph/graph.md` | Mermaid visual of the graph (renders on GitHub) |
| `10_ai_era_themes/` | 6 AI-era themes (semantic-layer, context-governance, domain-knowledge-base, skills-hub, certified-core-layer, ai-governance) + 4 supporting frames (llm-assistant-architecture, semantic-metric-layer-v2, bi-content-management, enterprise-ontology) + `library.md` |
| `11_dg_program_themes/` | 10 classic-DG themes synthesized from the program guide: getting started, frameworks, roadmap, roles & operating model, data catalog, data quality, maturity & metrics, domains & Data Mesh, data literacy, DG Kitchen research |
| `12_templates/templates.md` | Catalog of the board's workshop templates, each with a board deep-link |
| `20_dg_program_guide/` | Frame-by-frame summaries of the classic DG Program Guide v1.0 — the raw layer behind `11_dg_program_themes/` |
| `50_failure_catalog.md` | **How DG programs actually die**: 45 named failures in 7 families with a symptom-triage table — start here when something feels wrong |
| `51_numbers.md` | **Numbers registry**: every figure in the KB (175 rows) with a reliability tag |
| `52_questions.md` | Diagnostic question bank (81 probes) with what different answers mean — powers CONSULT |
| `40_sources.md` | All external links with verification dates + the board's resource library |
| `60_roadmap.md` | What the KB is still missing and in what order to fix it — written from stress-test findings, not aspiration |
| `70_golden_set/` | 100 grounded questions from five invented companies, with keys, traps and judge scores. A regression eval and a KB-coverage diagnostic — the low scores are a map of what the base is missing |
| `80_examples/` | Two complete FORM runs — the company portrait that went in and the strategy that came out. Invented companies, real positions. They exist because a method is easier to disbelieve than a document |
| `evals/` | Deterministic checks: citations, completeness, **forbidden claims (hard rule)**, structure, invariants (`invariants.json`), content rot. One command, non-zero exit on any blocking finding |
| `skills/dg-strategy/SKILL.md` | The strategy skill: CONSULT, FORM and AUDIT |
| `skills/dg-econ-effect/SKILL.md` | The economic effect skill: three real ROI zones, three methods, the discount ladder, and a precision list |
| `00_index.md` | Flat index of everything |

## Method invariants

Shared with the companion repository — the same rules hold on both sides.

- **Diagnose before prescribing.** A 0–4 maturity scorecard plus an AI-readiness overlay; name 2–3 breaks in the chain `core → semantic → context → AI accuracy → self-service`. The strategy is the repair plan for those breaks, not a wish list.
- **Stack-rank the freeze order:** governance & ownership → trusted data → AI readiness (the triad **certified core layer → semantic layer → domain knowledge base**, wrapped in **context governance**) → BI content funnel → self-service and agentic interfaces last. Cuts are made right to left.
- **Kill-gates block launches** until prerequisites are met: no assistant without semantic coverage and a certified core; no semantic layer without a core beneath it; no self-service scaling without a governance gate; no agent write operations without its own identity, narrow keys and an audit trail.
- **Dual track:** old-DG sustaining plus new-AI exploring, ring-fenced from each other; operate via the LLM-architecture loops A–E.
- **Rational target maturity.** The target line is calibrated to the company (4 questions), not set at "best practice"; +1 level per year unless a funded reason says otherwise; every target discounted for dependency, capacity and adoption risk; what the strategy deliberately does *not* do is written down; the budget cut is rehearsed in advance into a published freeze list.
- **CDO-judge pass before finalization.** An adversarial review in the voice of a sceptical CDO — priority, order, feasibility, complexity, concreteness, defensibility, risk honesty and rationality — including an explicit anti-bureaucracy pass that deletes artefacts with no reader, counts ceremonies per decision produced, and refuses a program that creates more paperwork than it retires. Blocking findings must be fixed or turned into named decisions, with a visible before/after of the rework.
- **Guardrails:** AI drafts — humans validate · no number without a source, gaps marked `[requires clarification]` · no over-optimism — a plan where everything succeeds is a plan nobody stress-tested.

## Evidence discipline

Every quantity in the KB lives in `51_numbers.md` with a tag saying how much to trust it:

| Tag | Meaning |
|---|---|
| **measured** | measured in a named setting, method stated |
| **benchmark** | a reproducible external benchmark or study |
| **vendor** | the vendor's own measurement, or a survey commissioned by the seller |
| **author-estimate** | the author's expert judgement, marked as such |
| **disputed** | circulating widely, sourcing does not hold up |

An agent building an argument should find the right number *and* know in the same second whether it survives being challenged. **Never quote a `vendor` or `disputed` figure as fact.** Benchmarks the author himself flagged as "industry mythology / vendor marketing" keep that flag.

The companion uses a coarser three-level scale (verifiable / vendor-measured / no data) that maps onto this one; when both repositories are in play, this finer scale wins.

## Evaluation

Quality is measured, not asserted, on two loops:

- **Loop A — deterministic (`evals/`).** Citation validity, completeness, structure, invariant violations (`invariants.json`) and content rot. One command, non-zero exit on any blocking finding, no model required.
- **Loop B — the golden set (`70_golden_set/`).** 109 grounded questions across five invented companies, with keys and deliberate traps. The first run used a holistic 0–10 judge and averaged 8.78; **that method has been retired** — an absolute model score drifts, so it stands as a historical record rather than a number to reproduce. The running measures are claim-level completeness, a binary contradiction check, and pairwise comparison on the items those two cannot separate.

On top of both loops sits a **hard rule**: `evals/check_forbidden.py` turns each item's `trap` into machine-checkable probes and fails any answer that commits it — whatever its completeness score, whatever a judge preferred. Only hand-confirmed probes block; auto-derived ones are advisory, because a false positive in a hard rule destroys the rule.

The important part is how the low scores were read: nine items scored 7 or below, and in eight of those the answer was as good as the base allows. **The score measured the knowledge base, not the answering** — and those nine became entries in `60_roadmap.md`.

## Russian edition

A derived Russian edition exists for readers who need the entry surface in Russian: the README, an overview per skill, and both worked examples. The themes, failure catalog, numbers registry, question bank, golden set and harness stay in English there — they are read by an agent rather than by a person, and translating 165 000 words for a reader they do not have would buy nothing. It lives at https://github.com/alexbarakov/dg-board-kb-ru and carries a `DERIVED_FROM.json` stamp plus a `check_sync.py` that reports drift against this repository, which is canonical.

## Caveats

- **Statuses in `objects.yaml` mirror the live board as of 2026-08-25**; the board evolves (Skills Hub is being reframed as "Agents/skill governance"; DKB and Core Layer child hexagons were removed).
- **The board is public**, so content is English, internal practices are unattributed ("a large tech company"), and numbers keep their public sources.
- **Legacy v1.0 summaries in `20_dg_program_guide/` are lossy** — generated from API summaries, images not extracted. For exact wording, open the `miro:` deep-link.
- **Most theme files carry a "From the course" section** — material distilled from the author's 6-day «Data Governance Fundamentals» program (slides and session transcripts): war stories, thresholds, anti-patterns and numbers the board alone does not show. Source tags name the day and slide; employers in war stories are anonymized; named companies appear only where the course cited them as public practice.
- **Material given in confidence does not live here.** Course feedback, participant interviews and anything carrying other people's names or employers is kept outside the synced tree — a sibling directory, not a status flag inside this one, because a path cannot be forgotten and a flag can. The rule that decides placement is the type of the claim: *"two participants asked for a worked catalog example"* is about people and stays internal; *"this base contains no worked catalog example"* is about this repository, is checkable by any reader, and is published in full with no provenance attached.
- Origin: built 2026-08-25/26 from the live board; maintained by Alex Barakov. Course backing: the author's «BI+AI Strategy 2026».

## Companion repository

[**BI+AI Strategy Builder**](https://github.com/alexbarakov/BI-strategy-self-consulting-agent) builds a BI+AI strategy for a specific company: a 66-atom knowledge base, a 101-question participant FAQ, a three-tier golden set, the Health Check diagnostic and the D&A Planner structure.

| What you are building | Who leads | Role of the other |
|---|---|---|
| **Data Governance** | **this KB** | the builder supplies the BI/AI stream |
| **BI** or **AI** strategy | the builder | this KB grounds the governance blocks and the AI foundation |
| **D&A** or a mix | **this KB** leads the structure | the builder supplies the substance of the BI/AI streams |

Conflict rule: on governance questions this KB wins, on BI/AI questions the builder does. The invariants match by construction; if they diverge, subject-matter ownership decides.

## Author

Method and materials — Alex Barakov / data nature: [data-nature.com](https://data-nature.com) · [t.me/datanature](https://t.me/datanature).
