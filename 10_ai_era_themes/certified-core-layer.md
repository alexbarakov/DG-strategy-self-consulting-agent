---
theme: Certified Core Layer
type: ai-era-theme
status: draft (child hexagons currently removed on the board — panel only)
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681730395308"
related:
  - "[[semantic-layer]] — stands on the certified core"
  - "[[bi-content-management]] — the content funnel that produces the certified layer"
---

# Certified Core Layer

**Tagline:** The trusted middle of the warehouse: marts with a declared, guaranteed trust status. The healthy diet of an AI analyst — and of everyone else.

## What is it

The core layer is the set of data marts with a declared, guaranteed trust status — an owner, an SLA, quality checks and metadata — plus active promotion of reuse instead of «I'll just build another mart». It is the trusted middle of the warehouse the semantic layer stands on.

Two mart profiles serve two needs: wide denormalized marts for exploration and ad-hoc, normalized ones for building derivatives. Both sit on one logical and conceptual model, and the layer starts from the most reused cross-domain entities — not from the sickest marts, where a project dies on the first hard case.

Why it needs governance muscle: cheaper production means more objects — the Jevons paradox — and complexity eats the gains. An AI analyst fed from thousands of uncertified marts produces plausible garbage. The dependency chain is core → certified metrics → agent accuracy → self-service.

## Key terms

- **Certified** — declared trust: owner, SLA, DQ coverage, metadata; the status is visible where the object is consumed.
- **Core mart** — governed and reused; wide profile for ad-hoc, normalized profile for derivatives.
- **Cross-domain entity** — an object every domain touches: customer, listing, order; the starting point of the layer.
- **Conceptual and logical model** — business entities and relations, and their table-level shape.
- **Health score** — penalties for no owner, staleness, no usage, duplicates; multipliers for wide and decision-level consumption.
- **Upstream check** — derived objects must stand on certified sources; checked at build, not discovered later.
- **Jevons paradox** — cheaper production → more objects → complexity eats the gains.

## Numbers for arguing with optimists

- The honest lesson: a 20% core-penetration target delivered 2% in a year — without dedicated capacity and enforcement the layer does not build itself.
- 20% vs 80% — agent accuracy without vs with grounding in certified sources.
- Thousands of marts, a single-digit certified share — the default state of a mature multi-domain warehouse.
- What AI adds now: generated DQ checks and descriptions with human-approved thresholds — check 100% instead of a sample.

## Sources

- Anthropic — a canonical table alone saves nothing: near-copies get deleted, and data code lives in one governed repo: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Author's course «BI+AI Strategy 2026», core layer module; field notes: https://t.me/datanature (post of 21 Mar 2026)
