---
theme: Semantic & Metric Layer (redrawn deep-dive)
type: deep-dive
status: draft-v2
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681745815982"
related:
  - "[[semantic-layer]] — the theme frame this deep-dive expands"
---

# Semantic & Metric Layer — the meaning layer for BI and AI

Business definitions as code: metrics, entities and terms defined once — and served to people, BI tools and AI agents through one governed door.

## Concepts

- **Semantic model** — the data map: entities (keys that make joins automatic), dimensions and measures — declared in YAML on top of warehouse models. The engine reasons over this map, so nobody guesses joins.
- **Metric layer** — metrics as versioned code: simple, ratio, cumulative — formula, grain and filters in one place (MetricFlow in dbt). Every tool asks the layer and gets the same number.
- **Glossary & data dictionary** — glossary: business terms and definitions; data dictionary: technical metadata (types, constraints, PII flags). They stay alive only when a term is bound to a metric definition in code and surfaces in the catalog — otherwise they rot in a wiki.

## Target architecture (diagram on the board)

Consumers (BI dashboards, chat / ad-hoc questions, AI agents) → **SQL API · REST · MCP — one governed door** → **Semantic layer** (semantic models YAML; metric store; semantic engine compiling definitions into SQL at query time) → **Core layer** (conformed entities, shared keys, history) → normalized core (dds) · raw landing · ETL. A **Catalog & context** box (business glossary, lineage, DQ status, owners, certification) feeds context sideways into the semantic layer and directly into agents.

Principle: every query route — human or agent — enters through the semantic layer.

## Metric families, not a strict tree (diagram on the board)

Metric cards: North Star (Revenue, Margin) ← drivers (Active customers, Conversion, Avg order value, Cost per order) ← base metrics (Orders, Sessions, Discounts). Cross-family links (Avg order value → both Revenue and Margin; Discounts → both Avg order value and Cost per order) show why a strict hierarchy fails. Govern the links, not the hierarchy.

## Fresh links (verified Aug 2026)

- dbt Semantic Layer — docs: https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl
- dbt — Semantic layer vs text-to-SQL (Apr 2026): https://docs.getdbt.com/blog/semantic-layer-vs-text-to-sql-2026
- Cube — Semantic layer for AI agents (2026): https://cube.dev/articles/semantic-layer-for-ai-agents-2026
- Snowflake Cortex Analyst — semantic models in production: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst
- Open Semantic Interchange — vendor-neutral semantic spec (now Apache Ossie): https://www.snowflake.com/en/blog/open-semantic-interchange-ai-standard/ · spec: https://github.com/open-semantic-interchange/OSI
- Airbnb Minerva — metric consistency at scale: https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70
- Spider 2.0 — why text-to-SQL fails on enterprise schemas: https://spider2-sql.github.io/
- Anthropic — 21% → 95%+ with a governed route: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude

Source: author's course «BI+AI Strategy 2026», module 07 — AI foundation (slides 49–64: plausible-but-wrong, ~40% enterprise text-to-SQL accuracy, prerequisite triad, target architecture, Airbnb Minerva reference, metric families).
