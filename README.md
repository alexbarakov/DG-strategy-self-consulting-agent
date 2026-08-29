# DG Board Knowledge Base — agent entry point

Textual projection of the public Miro board **«Data Governance Program Guide»** (data nature, Alex Barakov): https://miro.com/app/board/uXjVMBRtQEA=/

Purpose: let an AI agent **consult on Data Governance and build DG strategies** grounded in this material. This README is the single link to give the agent; everything else is reachable from here by relative path.

## Two ways to use this repository

**A. As a knowledge source (passive).** Add the repo (or its URL) to your agent's context and let it ground *other* tasks — answering DG questions, reviewing designs, preparing talks. The agent follows "How to use this KB" below; nothing to install.

**B. As a strategy skill (active).** [`skills/dg-strategy/SKILL.md`](skills/dg-strategy/SKILL.md) is a ready-to-run skill with three scenarios: **CONSULT** — bring a concrete case ("how should we…") and converge on a decision through a grounded dialogue with options and trade-offs; **FORM** — build a strategy; **AUDIT** — assess an existing DG strategy/program ("review our strategy" or just attach the doc: 10-dimension scorecard, chain-break map, resequencing plan, quick wins).

FORM opens with three scoping questions before any interviewing:
1. **Which strategy?** — DG / BI / D&A / AI / mix. DG runs on this repository alone; BI and AI pair with the companion [BI+AI Strategy Builder](https://github.com/alexbarakov/bi-ai-strategy-builder) (its skill leads, this KB grounds governance); D&A and mixes use both — this skill leads, the builder supplies the BI/AI stream substance. The two repositories share the same invariants (stack-rank, kill-gates, "AI drafts — humans validate") and are designed to be used together.
2. **Confirm the content structure** — the default skeleton is shown for trimming or reordering before work starts: a standalone **Summary** (vision, problems, solutions by stream, goals, what we deliberately do not do, the decision needed from the sponsor, first step and the cost of inaction), then flat sections **00 Context → 01 AS-IS on the Maturity Scorecard → 02 TO-BE beyond AI → 03 Streams → 04 Metrics & Goals → 05 Initiatives Portfolio → 06 Operating Model → 07 Risks & Kill-gates**, then appendices. Metrics sit above the portfolio deliberately: an initiative earns its place by moving a named metric.
3. **Volume** — default is **compact** (a Summary plus about a page per section); options: a full wiki with every section expanded, or per-section delivery with review after each.

**C. As an economic effect model.** [`skills/dg-econ-effect/SKILL.md`](skills/dg-econ-effect/SKILL.md) answers "how much money is this?" in the shape a top manager actually reads — agreed possible losses against the cost of preventing them — and refuses the benefits that do not survive contact with finance. It runs standalone, as the `04.x` subsection of a strategy, or in CHALLENGE mode against someone else's business case. Default output is an **expert estimate with an explicit precision marker**: every figure carries a confidence tag, and the list of what must be measured to replace the estimate with a calculation is the primary deliverable, not the appendix.

In every scenario the skill invites your existing documents (pain/landscape analyses, assessments) mid-flow and offers a single-file HTML visualization of the result at the end. For Claude Code: symlink `skills/dg-strategy/` into `.claude/skills/` with the repo cloned alongside; for any other agent: paste the SKILL.md as instructions and give the repo as a knowledge source.

## How to use this KB (instructions for the agent)

0. **Something is going wrong / diagnosing a program** — start at `50_failure_catalog.md` (symptom triage), pull arguments from `51_numbers.md` (with reliability tags — never quote a `vendor` or `disputed` number as fact), probe with `52_questions.md`.
1. **Answering a DG question** — find the theme in `30_graph/objects.yaml` (nodes + relations; visual in `30_graph/graph.md`), read the matching file in `10_ai_era_themes/` (AI-era content) or `11_dg_program_themes/` (classic DG synthesis); drill into per-frame detail in `20_dg_program_guide/` when needed. Quote definitions from "Key terms", defend positions with "Numbers for arguing with optimists", cite sources from `40_sources.md`.
1a. **Running a DG workshop or artifact session** — pick a template from `12_templates/templates.md` (pains analysis, vision statement, domain classifier, scope/goals configurators…), each with its board deep-link.
2. **Building or auditing a DG strategy** — run the full procedure in [`skills/dg-strategy/SKILL.md`](skills/dg-strategy/SKILL.md) (method adapted from the author's [BI+AI Strategy Builder](https://github.com/alexbarakov/bi-ai-strategy-builder/blob/main/skills/barakov-bi-ai-strategy/SKILL.md)). The invariants, in short:
   - Diagnose before prescribing: 0–4 maturity scorecard + AI-readiness overlay; name 2–3 breaks in the chain `core → semantic → context → AI accuracy → self-service` — the strategy is the repair plan for those breaks.
   - Stack-rank freeze order: governance & ownership → trusted data → AI readiness (the triad **Certified Core Layer → Semantic Layer → Domain Knowledge Base**, wrapped in **Context Governance**) → BI content funnel → self-service & agentic interfaces last.
   - Kill-gates block launches until prerequisites are met; dual track (old-DG sustaining + new-AI exploring, ring-fenced); operate via LLM-architecture loops A–E; defend budgets with the chain and the "Numbers for arguing with optimists" blocks.
   - Rational target maturity: the target line is calibrated to the company (4 questions), not set at "best practice"; +1 level per year unless a funded reason says otherwise; every target discounted for dependency, capacity and adoption risk; what the strategy deliberately does not do is written down; the budget cut is rehearsed in advance into a published freeze list.
   - **CDO-judge pass before finalization**: an adversarial review in the voice of a sceptical CDO — priority, order, feasibility, complexity, concreteness, defensibility, risk honesty — whose blocking findings must be fixed or turned into named decisions, with a visible before/after of the rework.
   - Deliverables are produced **in the user's language** (this KB is the source, not the output template); missing facts become explicit `[missing data]` markers (localized to the output language) naming the source that would close them, never invented numbers.
   - Guardrails: AI drafts — humans validate; no numbers without a source — mark gaps `[requires clarification]`; no over-optimism — a plan where everything succeeds is a plan nobody stress-tested.
3. **Recommending reading** — use `10_ai_era_themes/library.md`: the full board link library (~90 links — canonical articles per AI-era theme; classic-DG standards, communities, people to follow, book and article shelves from Program Map 3.0; vendor blogs; the author's working resources). `40_sources.md` holds verification status per link.
4. **Referencing the visual** — every file's frontmatter carries a `miro:` deep-link; give it when the user wants the picture.

## Map

| Path | Content |
|---|---|
| `10_ai_era_themes/` | 6 AI-era themes (semantic-layer, context-governance, domain-knowledge-base, skills-hub, certified-core-layer, ai-governance) + 4 supporting frames (llm-assistant-architecture, semantic-metric-layer-v2, bi-content-management, enterprise-ontology) + library.md |
| `11_dg_program_themes/` | 10 classic-DG themes synthesized from the program guide: getting started, frameworks, roadmap, roles & operating model, data catalog, data quality, maturity & metrics, domains & Data Mesh, data literacy, DG Kitchen research |
| `12_templates/templates.md` | Catalog of the board's workshop templates (pains analysis, domain classifier, vision statement, scope/goals configurators, Data Mesh canvas, DDI, business case…) |
| `20_dg_program_guide/` | Frame-by-frame summaries of the classic DG Program Guide v1.0 (per-frame files + `_index-batch*.md`) — the raw layer behind `11_dg_program_themes/` |
| `30_graph/objects.yaml` | Machine-readable graph: themes, components, relations, statuses, frame ids |
| `30_graph/graph.md` | Mermaid visual of the graph (renders on GitHub) |
| `40_sources.md` | All external links with verification dates + the board's resource library |
| `50_failure_catalog.md` | How DG programs actually die: 45 named failures in 7 families, with a symptom-triage table — start here when something feels wrong |
| `51_numbers.md` | Every number in the KB (175 rows) with a reliability tag: `measured` / `benchmark` / `vendor` / `author-estimate` / `disputed` |
| `52_questions.md` | Diagnostic question bank (81 questions) with what different answers mean — powers the CONSULT scenario |
| `skills/dg-strategy/SKILL.md` | The strategy skill: CONSULT, FORM (build) and AUDIT (assess) modes |
| `skills/dg-econ-effect/SKILL.md` | The economic effect skill: builds the money model behind a strategy — three real ROI zones, three methods, the haircut ladder, and a precision list that says what must be measured to replace the estimate with a calculation. Runs standalone, or as subsection `04.x` inside a strategy |
| `00_index.md` | Flat index of everything |

## Caveats

- Statuses in `objects.yaml` mirror the live board as of 2026-08-25; the board evolves (e.g., Skills Hub is being reframed as "Agents/skill governance"; DKB and Core Layer child hexagons were removed).
- The board is public: content is English, no company names for internal practices ("a large tech company"), numbers keep their public sources.
- Legacy v1.0 summaries in `20_dg_program_guide/` are lossy (generated from API summaries, images not extracted); for exact wording open the `miro:` deep-link.
- Most theme files carry a **"From the course"** section — material distilled from the author's 6-day «Data Governance Fundamentals» program (slides + session transcripts): war stories, thresholds, anti-patterns and numbers that the board alone does not show. Source tags name the day and slide. Employers in war stories are anonymized ("a large tech company / telecom / fintech"); named companies appear only where the course cited them as public practice. Benchmarks the author himself flagged as "industry mythology / vendor marketing" keep that flag — do not quote them as facts.
- Origin: built 2026-08-25/26 from the live board; maintained by Alex Barakov ([data-nature.com](https://data-nature.com), [t.me/datanature](https://t.me/datanature)). Course backing: the author's «BI+AI Strategy 2026».

## Plugging into an agent

Give your agent this repository URL (or add it as a knowledge source / clone it into the agent's workspace) and instruct: "Use README.md of this repo as the entry point for Data Governance consulting." The files are plain Markdown + one YAML graph — no build step, RAG-friendly chunking by design (one frame or theme per file).
