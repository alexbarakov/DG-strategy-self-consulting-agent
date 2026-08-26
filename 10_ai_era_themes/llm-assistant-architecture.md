---
theme: Data architecture for an LLM assistant
type: reference-architecture
status: accepted (author-made frame, translated to English)
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681720591847"
related:
  - "[[semantic-layer]] — the meaning layer is column 3 of this architecture"
  - "[[context-governance]] — loops A–E are its operational form"
---

# Data architecture for an LLM assistant: from sources to answer

Five columns, seven runtime steps, five cross-cutting loops. Color semantics: blue — the guaranteed path (query assembled from governed definitions); orange — best-effort path (the model writes SQL); red — access and risk; green — feedback loops.

## 1. Sources

- **Product databases** — business facts: orders, payments, statuses.
- **Clickstream** — user behavior: events and sessions.
- **External systems** — partner and third-party service data.
- **Reference data, MDM** — single lists: customers, products, categories.
- **Analyst query logs** — raw material for column descriptions and reference pairs.

## 2. Warehouse

- **Core layer** — shared entities, keys, history. Everything described to the right stands on it.
- **Data marts** — precomputed aggregates per domain: where most counting actually happens.
- **Contracts and DQ checks** — guard data quality. Answer quality is a different thing.
- **Warehouse roles** — the bottom line of access: what the agent cannot bypass even if a layer above fails.

## 3. Meaning layer (stores no data, describes what the data means)

- **Metadata catalog** — goal: know what exists and what can be trusted. Gives: owner, freshness, certification status.
- **Business glossary** — goal: one concept instead of ten synonyms. Gives: translation of user words into company terms.
- **Ontology and relationship graph** — goal: remove guessing of entity relationships. Gives: shared IDs and allowed join paths. (arXiv 2604.00555)
- **Semantic layer** — goal: compute a metric the same way, always and everywhere. Gives: measures, dimensions, grain, aggregation rules and access policies — in code, not in a prompt. (dbt MetricFlow)
- **Reference queries and descriptions** — goal: cover the tail that is not modeled. Gives: question-to-SQL examples and column descriptions.
- Plus: **cache and pre-aggregates** (fast answers, Cube pre-aggregations) and **versions and definition tests** (a metric cannot change unnoticed).

## 4. Assistant runtime — seven steps from question to number

1. **The question and who asked it** — roles and domain arrive with the question, not after it.
2. **Understand the question** — words into concepts, concepts into concrete objects and paths.
3. **Clarify** — if there are two readings, return the question to the user (42.5% → 92.5% accuracy; arXiv 2508.15276).
4. **Choose the route** — is the question covered by the semantic layer or not (dbt: semantic layer vs text-to-SQL, Apr 2026).
5. a. **Assemble the query (text-to-semantics)** — the compiler builds SQL from measures and dimensions; the model does not write it. / b. **Generate (text-to-SQL)** — the model writes SQL, but with context from the meaning layer; retry on error up to 3 times.
6. **Apply permissions inside the query** — row filters are baked into the SQL, not applied afterwards.
7. **Execute in the warehouse and answer** — a number, a trust label and provenance: which measure, which query, data as of which date. «I cannot» is a valid answer.

## 5. Consumers

- **Business** — asks in plain words in chat, cannot verify the answer.
- **Analyst** — speeds up their own work and finishes the answer by hand.
- **Dashboards** — read the same definitions as the assistant.
- **External agents** — get the same layer through one interface.
- **The risk all of this is built against:** the query ran without an error and silently returned a wrong number — and there is no signal.

## Cross-cutting loops — what the construction cannot survive a quarter without

- **A. Offline evals** — golden-set score before release; stop signal: share of confidently wrong answers. (langchain.com/resources/llm-evals)
- **B. Online evals** — trace of every answer from question to number; quality drift, cost, sample-volume anomalies. (arize.com — evaluation harness)
- **C. Human error review** — failures become new golden-set cases and confirmed reference queries. (galileo.ai — calibrate LLM judge)
- **D. Coverage management** — modeling queue built from the most frequent best-effort questions.
- **E. Access and security** — least privilege, query audit, review of definition changes.

Loop connections: answer → user; clarification → user; prod answers and reactions → online evals; cases into the golden set → offline evals; modeling queue → semantic layer.

## Terms

- **Golden set** — a fixed list of questions with known correct answers; the system is measured on it before rollout.
- **Eval** — running the system over such a set and scoring it. Offline — before release, online — on live traffic.
- **Loop** — a process closed on itself: the output returns to the input and changes system behavior.
- **Best-effort** — an answer mode without guarantees; the opposite is governed: built on a verified definition.
- **Grain** — what one row means: a deal, a day per category, a stock snapshot. Determines what can be summed.
- **Provenance** — the answer origin chain: which metric, which query, data as of which date.
