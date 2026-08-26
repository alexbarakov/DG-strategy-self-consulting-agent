---
theme: Semantic Layer
type: ai-era-theme
status: draft-v3 (accepted format)
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681721996210"
related:
  - "[[semantic-metric-layer-v2]] — redrawn deep-dive with diagrams and fresh links"
  - "[[certified-core-layer]] — the layer below: semantic layer stands on certified core"
  - "[[llm-assistant-architecture]] — runtime view: where the layer sits in the answer path"
---

# Semantic Layer as AI Infrastructure

**Tagline:** Why every text-to-SQL demo works and production lies. Without the layer, an LLM hallucinates business logic — regardless of the model.

## What is it

A thin layer between the warehouse and every consumer — human or AI agent — where business concepts are defined once, as code, and compiled into SQL on demand. It answers three questions: what a metric means, how it is calculated, and which cuts are legal. One definition — one number in every tool that asks.

For an agent it is the difference between guessing business logic and resolving it. The wall is organizational, not technical: everyone adopts dbt, everyone skips the metric layer. Build the layer before the agents, not after them.

## Components (child objects on the board)

| Component | Definition |
|---|---|
| Metric Store | Metric definitions as code: one place of calculation, versioned |
| Metric Tree | Relations between metrics: drivers, decomposition, impact analysis |
| Semantic Model | Entities, dimensions, relationships; joins become automatic |
| Semantic Engine | Compiles definitions into SQL at query time; meaning lives in code (Metric Store —"compiled by"→ Semantic Engine) |
| Text-to-Semantic | Natural language resolves to metrics and dimensions, not to raw SQL |
| SQL API | JDBC / REST / MCP: one governed door for BI tools and AI agents |
| Access and Certification | Ownership, permissions, trusted status of each metric |

## Key terms

- **Metric** — a governed business calculation: formula, grain, filters, owner, version.
- **Dimension** — an approved cut of a metric: region, segment, platform.
- **Entity** — a business object (customer, order) that links tables and enables automatic joins.
- **Semantic model** — the map of entities, dimensions and relationships the engine reasons over.
- **Semantic compilation** — deterministic translation of a definition into SQL; no LLM at this step.
- **Headless BI** — the layer serves any client via API, decoupled from visualization.
- **Governed route** — a question resolves through the layer; raw SQL is a fallback, never the default.
- **Pre-aggregation** — a materialized slice of a metric, refreshed on schedule, serving repeated queries cheaply.
- **Pushdown** — the runtime executes inside the warehouse instead of moving data out; the layer stays thin.

## Numbers for arguing with optimists

- ~40% — text-to-SQL accuracy on real enterprise schemas; on Spider 2.0 GPT-4o scores 6% vs 86% on the academic benchmark.
- 85–95% — with a semantic layer; the failure mode changes too: it declines to answer instead of inventing one.
- 21% → 95%+ — Anthropic's agent evals without vs with the governed route.
- Real-company scale (thousands of tables, 15 000+ metrics) is beyond any academic benchmark.

## Sources

- Spider 2.0 — enterprise text-to-SQL benchmark: https://spider2-sql.github.io/
- Anthropic — How Anthropic enables self-service data analytics with Claude: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Author's course «BI+AI Strategy 2026», AI-foundation module; field notes: https://t.me/datanature
