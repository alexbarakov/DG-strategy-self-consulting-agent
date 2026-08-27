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

## From the course (Data Governance Fundamentals, 6 days)

**Adoption reality**
- The adoption paradox: "everyone already understands what it is, but very few have actually acquired one" — both the DWH and BI systems fight to keep business logic inside themselves, and wedging a separate system between layers of an already-running landscape is architecturally hard. (course day 1, transcript)
- "It's fashionable to talk about semantic layers, but very few actually build them; people lived 15 years without them." Decision heuristic: count the BI devs/analysts hand-coding the same business logic — the pain is real only when dozens of independent teams reuse the same core data. (course day 5, transcript)
- The layer is explicitly classed as a luxury, "reserved for the mature": "don't assume you must have it — it may simply not be affordable for you" at current maturity. Budget version for lower maturity: a metric tree bound to the glossary and catalog. (course day 6, slides p.100; course day 2, transcript)

**Lineage of the idea**
- The MDM fashion passed ~10 years ago but its problems remain; the semantic layer and data products now play the same unification role for "master" business logic. (course day 1, slides p.97, 101)
- Airbnb Minerva as the legendary case: programmatic denormalization — a computation-DAG engine over certified normalized marts replacing the zoo of ever-wider denormalized tables; "define once — use everywhere". (course day 5, slides p.21)
- A large tech company's metric UI grew out of the AB-testing platform — the same declarative metrics serve experiments and BI, which is what made the store trustworthy. (course day 5, transcript)

**Design notes**
- dbt distinction worth keeping: semantic layer (entities, measures, dimensions; automatic joins) vs metric layer (declarative metric definitions on top); a glossary is mapped alongside the metric store, not inside it. (course day 5, slides p.19-20)
- Metric trees: "a strictly hierarchical tree is exactly what you won't get" — real metric graphs are overlapping clouds of metric groups with tangled links; a single global tree "carries nothing but beauty"; domain-level trees are the working unit. (course day 5, slides p.30; transcript)
- Two-track BI that works at scale: dashboard-centric BI for monitoring/reporting plus metric-centric BI (metric store / constructor over the semantic layer) for ad-hoc metric analysis — deliberately coexisting, separated by use case. (course day 2, transcript)
- Glossaries are the hardest adjacent component to launch — the only part requiring active business participation; the pitch "the whole company speaks one language" sells far worse than lineage. Memorable case: a company with two metrics, "sales" and "revenue", where nobody can say which is correct. (course day 4, transcript)

## Sources

- Spider 2.0 — enterprise text-to-SQL benchmark: https://spider2-sql.github.io/
- Anthropic — How Anthropic enables self-service data analytics with Claude: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Author's course «BI+AI Strategy 2026», AI-foundation module; field notes: https://t.me/datanature
