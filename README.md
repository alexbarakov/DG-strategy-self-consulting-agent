# DG Board Knowledge Base — agent entry point

Textual projection of the public Miro board **«Data Governance Program Guide»** (data nature, Alex Barakov): https://miro.com/app/board/uXjVMBRtQEA=/

Purpose: let an AI agent **consult on Data Governance and build DG strategies** grounded in this material. This README is the single link to give the agent; everything else is reachable from here by relative path.

## How to use this KB (instructions for the agent)

1. **Answering a DG question** — find the theme in `30_graph/objects.yaml` (nodes + relations; visual in `30_graph/graph.md`), read the matching file in `10_ai_era_themes/` (AI-era content) or `11_dg_program_themes/` (classic DG synthesis); drill into per-frame detail in `20_dg_program_guide/` when needed. Quote definitions from "Key terms", defend positions with "Numbers for arguing with optimists", cite sources from `40_sources.md`.
1a. **Running a DG workshop or artifact session** — pick a template from `12_templates/templates.md` (pains analysis, vision statement, domain classifier, scope/goals configurators…), each with its board deep-link.
2. **Building a DG strategy** — run it as a procedure, not a reading list (method adapted from the author's [BI+AI Strategy Builder](https://github.com/alexbarakov/bi-ai-strategy-builder/blob/main/skills/barakov-bi-ai-strategy/SKILL.md); this KB supplies the DG substance for each step):

   **Step 1 — Diagnose before prescribing.** Collect context (team, tooling, demand, constraints, 12-month ambition) and a self-rated maturity profile on a 0–4 scale ("no/almost none" → "optimized"). Use `11_dg_program_themes/maturity-and-metrics.md` (7-dimension map, DDI) and the 5-of-12 entry test from `getting-started.md`. Overlay AI-readiness: semantic coverage, certified-data share, domain-context completeness. Name 2–3 concrete breaks in the chain `core → semantic → context → AI accuracy → self-service` — the strategy is the repair plan for those breaks.

   **Step 2 — Order by stack-rank (hard freeze order).** When resources shrink, freeze from the bottom up, never the top: (1) governance & ownership (`roles-and-operating-model.md`) → (2) trusted data layer (`certified-core-layer.md`, start from the most reused cross-domain entities, not the sickest marts) → (3) AI readiness: the prerequisite triad **Certified Core Layer → Semantic Layer → Domain Knowledge Base**, wrapped in **Context Governance** (status lifecycle, verify gate, freshness TTL, trust plane — otherwise machine-generated knowledge poisons the layer) → (4) BI content (the **content management funnel**: archive unused → certify → promote ~5% key reports) → (5) self-service & agentic interfaces last.

   **Step 3 — Enforce kill-gates.** Every initiative has launch prerequisites; do not argue, block: no AI analytics assistant without a semantic layer covering the target domains and a certified-data baseline; no self-service scaling without governance gatekeeping and DQ monitoring; no semantic layer without a core-layer foundation. Gates come from the triad order in `30_graph/objects.yaml`.

   **Step 4 — Run a dual strategy.** Old-DG sustaining track (catalog, DQ, certification, standards) in parallel with a new-AI exploring track (agentic interfaces, domain packs, context mining) — ring-fenced to low-risk domains, measured by AI accuracy plus human-validation overhead. Scale the people side through **Skills Hub / agent-skill governance** (owners, versions, confirmed-value motivation).

   **Step 5 — Operate and measure.** Run the **LLM assistant architecture** loops A–E (offline/online evals, error review, coverage management, access & security); the coverage loop feeds the semantic-layer backlog. Defend budgets with the chain `core → certified metrics → agent accuracy → self-service` and the "Numbers for arguing with optimists" blocks in each theme file.

   **Deliverable shape.** A 7-block document (diagnostics → AS-IS → TO-BE → AI foundation → trusted data → content & self-service → operations → transformation plan with stack-rank, timeline, metrics and kill-gates) plus a one-page 6-pager synthesis. Guardrails: AI drafts — humans validate; no recommendation without participant data behind it; no numbers without a source — mark gaps as `[requires clarification]`.
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
| `00_index.md` | Flat index of everything |

## Caveats

- Statuses in `objects.yaml` mirror the live board as of 2026-08-25; the board evolves (e.g., Skills Hub is being reframed as "Agents/skill governance"; DKB and Core Layer child hexagons were removed).
- The board is public: content is English, no company names for internal practices ("a large tech company"), numbers keep their public sources.
- Legacy v1.0 summaries in `20_dg_program_guide/` are lossy (generated from API summaries, images not extracted); for exact wording open the `miro:` deep-link.
- Origin: built 2026-08-25/26 from the live board; maintained by Alex Barakov ([data-nature.com](https://data-nature.com), [t.me/datanature](https://t.me/datanature)). Course backing: the author's «BI+AI Strategy 2026».

## Plugging into an agent

Give your agent this repository URL (or add it as a knowledge source / clone it into the agent's workspace) and instruct: "Use README.md of this repo as the entry point for Data Governance consulting." The files are plain Markdown + one YAML graph — no build step, RAG-friendly chunking by design (one frame or theme per file).
