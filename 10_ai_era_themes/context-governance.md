---
theme: Context Governance
type: ai-era-theme
status: draft
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681729481504"
related:
  - "[[domain-knowledge-base]] — the domain packs this governance process manages"
  - "[[llm-assistant-architecture]] — loops A–E operationalize the eval side"
---

# Context Governance

**Tagline:** Managing the meaning AI reasons on. Data governance manages the data; context governance manages the knowledge about the data.

## What is it

Data governance manages data: quality, access, lineage. Context governance manages the layer of meaning an agent reads to reason — definitions, domain knowledge, metadata, situational context. Clean data is not yet trusted data: the agent must know what a number means and when not to use it.

Managed context is built from atoms. Each piece of knowledge carries a passport: where it was mined, how much it is trusted, how fresh it is, and where the source of truth lives. Dumping documents into a vector store is not governance.

Three invariants keep it honest:
1. The SSOT is referenced, never copied.
2. Extraction never trusts itself — machine output enters as candidate only.
3. Verified is necessary but not sufficient — serving depends on status, freshness and absence of conflict with the SSOT.

## Components (child objects on the board)

| Component | Definition |
|---|---|
| Context Unit | The atom of knowledge with a passport: provenance, status, freshness, link to SSOT |
| Context Store | Governed repository of atoms; references the source of truth, never copies it |
| Trust Plane | The serving decision: SERVE_AS_FACT / SERVE_WITH_CAVEAT / WITHHOLD |
| Provenance and Freshness | Origin of each atom plus TTL: fresh, aging, stale |
| Context Mining | Extraction from query logs, catalogs and threads; outputs candidates only (—"yields candidate"→ Context Unit) |
| Verify Gate | A domain curator judges machine drafts; a gate, not authoring (—"promotes to verified"→ Trust Plane) |
| Serving Hook | The agent cannot query data without passing through context first |
| Eval Loop | A golden set ties verification to measured accuracy; what drops accuracy cannot stay verified |

## Key terms

- **Context Unit** — the atom of knowledge: provenance, status, ssot_ref, freshness, source object.
- **Status lifecycle** — inferred → candidate → verified → deprecated; only a human promotes to verified.
- **Trust plane** — serve as fact, serve with caveat, or withhold — decided by status, freshness and query risk.
- **Freshness TTL** — every atom expires: fresh → aging → stale; deprecation is automatic, by timeout, not by memory.
- **Verify gate** — the curator judges drafts the machine wrote; gate work, not authoring work.
- **False-accept rate** — share of wrong atoms that slipped into verified; read coverage only together with it.
- **Few-shots** — verified question-to-query pairs that ground the agent in the domain.

## Numbers for arguing with optimists

- 25% → 80% — accuracy of a domain assistant without vs with a filled domain context.
- ≥70% verified share and <5% false-accept — health thresholds of a context layer.
- ~75% — accuracy of AI auto-documentation: plausible enough to poison the layer if there is no gate.
- 80% of data and analytics governance initiatives will fail by 2027 — Gartner; shelfware catalogs are the default outcome.
- Context routing on simple queries: 20k → 6k tokens, 13 → 4 steps, minutes → seconds.

## Sources

- Anthropic — context and skills lift agent accuracy from 21% to 95%+: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Snowflake Cortex Analyst — the working contour (query-history mining, verified semantic model, human-confirmed pairs): https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst
- Gartner press release, Feb 2024 — 80% of D&A governance initiatives will fail by 2027.
- Author's course «BI+AI Strategy 2026», Context Governance module; field notes: https://t.me/datanature
