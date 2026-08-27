# DG Board Knowledge Base — agent entry point

Textual projection of the public Miro board **«Data Governance Program Guide»** (data nature, Alex Barakov): https://miro.com/app/board/uXjVMBRtQEA=/

Purpose: let an AI agent **consult on Data Governance and build DG strategies** grounded in this material. This README is the single link to give the agent; everything else is reachable from here by relative path.

## Two ways to use this repository

**A. As a knowledge source (passive).** Add the repo (or its URL) to your agent's context and let it ground *other* tasks — answering DG questions, reviewing designs, preparing talks. The agent follows "How to use this KB" below; nothing to install.

**B. As a strategy skill (active).** [`skills/dg-strategy/SKILL.md`](skills/dg-strategy/SKILL.md) is a ready-to-run skill with three scenarios: **CONSULT** — bring a concrete case ("how should we…") and converge on a decision through a grounded dialogue with options and trade-offs; **FORM** — build your DG strategy & tactics ("build a DG strategy": interview → 0–4 diagnostic scorecard → 7-block document with stack-rank, kill-gates and a 6-pager); **AUDIT** — assess an existing DG strategy/program ("review our strategy" or just attach the doc: 10-dimension scorecard, chain-break map, resequencing plan, quick wins). In every scenario the skill invites your existing documents (pain/landscape analyses, assessments) mid-flow and offers a single-file HTML visualization of the result at the end. For Claude Code: symlink `skills/dg-strategy/` into `.claude/skills/` with the repo cloned alongside; for any other agent: paste the SKILL.md as instructions and give the repo as a knowledge source.

## How to use this KB (instructions for the agent)

1. **Answering a DG question** — find the theme in `30_graph/objects.yaml` (nodes + relations; visual in `30_graph/graph.md`), read the matching file in `10_ai_era_themes/` (AI-era content) or `11_dg_program_themes/` (classic DG synthesis); drill into per-frame detail in `20_dg_program_guide/` when needed. Quote definitions from "Key terms", defend positions with "Numbers for arguing with optimists", cite sources from `40_sources.md`.
1a. **Running a DG workshop or artifact session** — pick a template from `12_templates/templates.md` (pains analysis, vision statement, domain classifier, scope/goals configurators…), each with its board deep-link.
2. **Building or auditing a DG strategy** — run the full procedure in [`skills/dg-strategy/SKILL.md`](skills/dg-strategy/SKILL.md) (method adapted from the author's [BI+AI Strategy Builder](https://github.com/alexbarakov/bi-ai-strategy-builder/blob/main/skills/barakov-bi-ai-strategy/SKILL.md)). The invariants, in short:
   - Diagnose before prescribing: 0–4 maturity scorecard + AI-readiness overlay; name 2–3 breaks in the chain `core → semantic → context → AI accuracy → self-service` — the strategy is the repair plan for those breaks.
   - Stack-rank freeze order: governance & ownership → trusted data → AI readiness (the triad **Certified Core Layer → Semantic Layer → Domain Knowledge Base**, wrapped in **Context Governance**) → BI content funnel → self-service & agentic interfaces last.
   - Kill-gates block launches until prerequisites are met; dual track (old-DG sustaining + new-AI exploring, ring-fenced); operate via LLM-architecture loops A–E; defend budgets with the chain and the "Numbers for arguing with optimists" blocks.
   - Guardrails: AI drafts — humans validate; no numbers without a source — mark gaps `[requires clarification]`.
3. **Recommending reading** — use `10_ai_era_themes/library.md` (canonical articles per theme) and `40_sources.md` (verification status).
4. **Referencing the visual** — every file's frontmatter carries a `miro:` deep-link; give it when the user wants the picture.

## Map

| Path | Content |
|---|---|
| `10_ai_era_themes/` | 5 AI-era themes (semantic-layer, context-governance, domain-knowledge-base, skills-hub, certified-core-layer) + supporting frames (llm-assistant-architecture, semantic-metric-layer-v2, bi-content-management, enterprise-ontology, library) |
| `11_dg_program_themes/` | 10 classic-DG themes synthesized from the program guide: getting started, frameworks, roadmap, roles & operating model, data catalog, data quality, maturity & metrics, domains & Data Mesh, data literacy, DG Kitchen research |
| `12_templates/templates.md` | Catalog of the board's workshop templates (pains analysis, domain classifier, vision statement, scope/goals configurators, Data Mesh canvas, DDI, business case…) |
| `20_dg_program_guide/` | Frame-by-frame summaries of the classic DG Program Guide v1.0 (per-frame files + `_index-batch*.md`) — the raw layer behind `11_dg_program_themes/` |
| `30_graph/objects.yaml` | Machine-readable graph: themes, components, relations, statuses, frame ids |
| `30_graph/graph.md` | Mermaid visual of the graph (renders on GitHub) |
| `40_sources.md` | All external links with verification dates + the board's resource library |
| `skills/dg-strategy/SKILL.md` | The strategy skill: FORM (build) and AUDIT (assess) modes |
| `00_index.md` | Flat index of everything |

## Caveats

- Statuses in `objects.yaml` mirror the live board as of 2026-08-25; the board evolves (e.g., Skills Hub is being reframed as "Agents/skill governance"; DKB and Core Layer child hexagons were removed).
- The board is public: content is English, no company names for internal practices ("a large tech company"), numbers keep their public sources.
- Legacy v1.0 summaries in `20_dg_program_guide/` are lossy (generated from API summaries, images not extracted); for exact wording open the `miro:` deep-link.
- Origin: built 2026-08-25/26 from the live board; maintained by Alex Barakov ([data-nature.com](https://data-nature.com), [t.me/datanature](https://t.me/datanature)). Course backing: the author's «BI+AI Strategy 2026».

## Plugging into an agent

Give your agent this repository URL (or add it as a knowledge source / clone it into the agent's workspace) and instruct: "Use README.md of this repo as the entry point for Data Governance consulting." The files are plain Markdown + one YAML graph — no build step, RAG-friendly chunking by design (one frame or theme per file).
