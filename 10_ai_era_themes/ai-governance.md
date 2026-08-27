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

## From the course (Data Governance Fundamentals, 6 days)

**The dam has opened**
- "The feeling is that a dam has been opened. One quarter of chasing efficiency is enough to flood the whole valley. Governance must be thought through. Immediately." And: "After the 'Wild West' strategy comes the counting of burned tokens" — many agent scenarios simply won't pay off. (course day 6, slides p.96)
- "Everyone was waiting for the revolution — and it arrived as a creeping infiltration of local agents" (Claude Code, Cursor and co.) into data operations: code writing, testing, analytical scenarios. (course day 1, transcript)
- AI-first policy datapoint from two large tech companies: "to open any vacancy we must prove that AI cannot do this work" — one has run this rule for over a year. Big tech fully supports AI adoption even at the expense of perceived risks, unlike banks and regulated industries. (course day 1, transcript)

**Predictions to plan against**
- Agent query share will spike — "agents join like crazy and not always elegantly"; expect infra degradation, plan agent request filtering, sampling and quotas. (course day 6, slides p.96)
- Prod-access risk is real today: an agent can write code, push it, and review its own PR — "catch and block such cases, for now." (course day 6, slides p.96)
- Today agent access = user access; next comes registering agents bound to employees with separate service-account-like credentials "but with character." (course day 6, slides p.96)
- A new observability class emerges — monitoring agent actions (queries generated, tokens burned, code changed) — which will itself be agentic ("is that good?"). Content volume grows by an order of magnitude: "those who swam out of the content chaos need to take a breath before diving again." (course day 6, slides p.96)

**New governance objects**
- AI agents and skills are assets that need cataloging like tables: a registry with certification, reuse of good ones and deletion of bad ones — "the usual content-management practice now applies to agents"; plus marking corporate content (Confluence, chats) for what agents may ingest. (course day 6, transcript; day 4, transcript)
- DG-for-GenAI checklist: quality data feeding models; a navigation layer of linked certified sources with semantic logic on top; prompt-input checks against leaking sensitive info/IP; cataloging and inventory of AI models as data products; resource optimization. (course day 2, slides p.38)
- AI is currently the strongest budget hook for DG: "for the AI model to work you need to feed it quality data — surprise." The catalog is the proto-base of AI context — this justifies investing in the catalog AND the role model, because tooling alone can't make owners do the right things regularly. (course day 2, transcript)

**War stories and hidden costs**
- A domain data steward used an AI skill to create business-logic DQ checkers for 160 datamarts in one day (normally ~3 weeks). The next bottleneck appeared immediately: the checkers flooded incidents, requiring an incident-management agent plus an eval-agent judging checker adequacy. "The boost survives after subtracting validation costs, but it's smaller than the first emotions." (course day 6, transcript)
- Human-in-the-loop hidden cost: a day of pure intellectually-loaded verification of agent output burns people out much faster than when review was mixed with routine. (course day 6, transcript)
- Agents supervising agents "smells like loss of control" — human oversight stays mandatory for now; every autonomous flow without review has produced undesired events. (course day 6, transcript)
- Live unresolved dispute inside a large tech company: one camp says re-checking auto-generated docs/mappings costs about as much as doing the mapping manually; the other says "it doesn't make mistakes, especially with a second agent re-checking." Presented as a genuine governance question of the LLM era. (course day 5, transcript)

**AI-generated metadata posture**
- Vendor-verified verdict: AI-generated metadata creates "the feeling that you have everything," but quality demands human-in-the-loop review; what AI can't produce is tribal-knowledge caveats. Deployment posture: tag AI-generated metadata "requires review," or run a bot that pings the owner to confirm. (course day 4, transcript)
- LLMs killed the cost of producing governance documentation: "Writing and updating policies became simple — detailed accents in prompts and compile. What's left is to find those who will read them." Readability, not production, is now the constraint. (course day 5, slides p.93; transcript)

**Market reality (use critically — anecdotal)**
- A full chat-with-your-data feature over all metadata layers excited vendor prospects but generated zero purchases — "the concrete loop 'do this and your business runs better' is still not assembled." Yet AI transformed implementation itself: glossary building went from 9 months of manual work to an AI prototype capturing ~80% (a central-bank case, 10k+ terms from public PDFs). (course day 6, transcript)
- Anti-FOMO: vacancies for data people grow rather than shrink; AI growth is throttled by compute cost — "if AI costs more than a human, automation stops being profitable — a natural economic limit"; laggard companies can enter in 2-5 years when practices commoditize. (course day 6, slides p.97; transcript)

## Sources

- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- EU AI Act (Regulation 2024/1689): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- ISO/IEC 42001 — AI management systems: https://www.iso.org/standard/81230.html
- Anthropic — governance scope of a service account for ad-hoc analytics: https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
