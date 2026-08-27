---
theme: Domain Knowledge Base
type: ai-era-theme
status: draft (child hexagons currently removed on the board — hub + panel only)
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681729697250"
related:
  - "[[context-governance]] — the governance process that keeps packs trustworthy"
  - "[[semantic-layer]] — layer 2 of the triad; the KB is layer 3 on top of it"
  - "[[enterprise-ontology]] — the relationship map a domain pack builds on"
---

# Domain Knowledge Base

**Tagline:** The agent answers from a curated domain pack, not from the model's memory. Layer three of the prerequisite triad, on top of the semantic layer and core data.

## What is it

A curated corpus of domain knowledge that grounds the agent: which metric to use and why, what the known traps are, where the boundaries of the domain lie. The semantic layer holds the formulas; the knowledge base holds the judgement around them.

It ships as a pack: a manifest, knowledge files — domain profile, glossary, key objects, FAQ — and an eval folder with a golden set. Everything machine-generated enters as needs_review and counts only after a human confirms it.

Filling ≠ trust ≠ effect: coverage can be gamed by weakening the gate, so coverage and false-accept are read only together, and the domain's value is measured by its AI-ready score, not by file count.

## Key terms

- **Knowledge pack** — manifest plus knowledge/ plus eval/; the versioned, deployable unit of domain knowledge.
- **Domain profile** — what the domain covers, who owns it, where to escalate, how fresh its knowledge must stay.
- **Few-shot** — a verified question-to-query pair; the densest way to transfer domain skill to an agent.
- **Trap** — a do-not-use-for case: legacy fields, migration breakpoints, deceptive column names.
- **Golden set** — reference questions with expected answers and a scoring rubric; run on every change of context or model.
- **Status model** — needs_review → confirmed → archived; master-system autosync counts as trusted by origin.
- **AI-ready score** — composite: roles assigned, healthy metrics share, consumption on certified objects.

## Numbers for arguing with optimists

- 25% → 80% — accuracy of a domain assistant before vs after the knowledge base is filled.
- ~61% — share of ad-hoc analytics requests automatable with SQL plus documentation, in a field study of 2 198 request threads.
- Score thresholds that worked: ≥50% of domain metrics healthy, ≥45% of dashboard views and ≥30% of mart hits landing on certified objects.
- 100% of machine-generated knowledge starts as needs_review — no exceptions, or the layer poisons itself.

## From the course (Data Governance Fundamentals, 6 days)

**AI-Ready Domain checklist — the operational form of the pack**
- Prerequisites per domain for the AI Analyst: domain boundary + owner stated in 1-3 phrases with an escalation route; markup of certified datamarts/metrics/dashboards; short meta per key object including "don't use for..." limitations; typical "how do I...?" Q&A scenarios with answer + example link; pointers to adjacent domains ("for X ask domain Y"); a domain glossary. (course day 6, slides p.95)
- Responsibility split that staffs the pack: Domain Owner (Head of Analytics) / BI Partner (datamarts + dashboards) / Metric Curator (metrics). (course day 6, slides p.95)

**Bottom-up assembly**
- Domain glossaries are assembled bottom-up from tagged Confluence pages where teams already describe their specifics and methodology — no company-wide glossary needed first. (course day 6, transcript)

## Sources

- Anthropic — skills as packaged domain knowledge lift agent accuracy from 21% to 95%+: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Author's course «BI+AI Strategy 2026», Domain Knowledge Base module; field notes: https://t.me/datanature
