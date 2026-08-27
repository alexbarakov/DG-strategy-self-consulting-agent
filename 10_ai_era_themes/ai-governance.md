---
theme: AI Governance
type: ai-era-theme
status: library-only (no dedicated theme frame on the board yet; section on the Library frame)
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681744960974"
related:
  - "[[context-governance]] — governs the knowledge AI reasons on; AI governance governs the systems themselves"
  - "[[skills-hub]] — agent-skill governance is the operational slice of AI governance"
  - "[[llm-assistant-architecture]] — loop E (access & security) implements the control side"
---

# AI Governance

**Tagline:** Governing the AI systems themselves — risk tiering, accountability, auditability — as the regulatory wrapper around everything the other themes build.

## What is it

Data governance manages data; context governance manages the knowledge AI reads; AI governance manages the AI systems: which risk class each use case falls into, who is accountable, what must be logged, when a human must stay in the loop, and what evidence an auditor gets. For an analytics organization it lands as: a model/agent inventory, risk tiering of AI scenarios (an internal ad-hoc assistant is not the same class as a customer-facing decision system), audit trails for queries and definition changes, and named accountable owners.

The three public anchors: **NIST AI RMF** (govern / map / measure / manage — voluntary framework, the de-facto vocabulary), **EU AI Act** (Regulation 2024/1689 — binding risk-tiered obligations), **ISO/IEC 42001** (certifiable AI management system standard).

## Key terms

- **Risk tiering** — classifying AI use cases by potential harm; controls scale with the tier.
- **Model / agent inventory** — the register of AI systems in production: owner, purpose, data touched, tier.
- **Human-in-the-loop** — a required human decision point for higher-tier actions; the verify gate is its DG instance.
- **Audit trail** — reconstructable history: which query, which definitions, which context version produced an answer.
- **Accountable owner** — a named person per AI system; committees do not count.

## Sources

- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- EU AI Act (Regulation 2024/1689): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- ISO/IEC 42001 — AI management systems: https://www.iso.org/standard/81230.html
- Anthropic — governance scope of a service account for ad-hoc analytics: https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
