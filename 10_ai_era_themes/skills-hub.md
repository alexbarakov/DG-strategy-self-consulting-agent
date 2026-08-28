---
theme: Skills Hub (board also carries a working retitle "Agents/skill governance")
type: ai-era-theme
status: draft (hexagons currently removed on the board; a huge "Agents/skill governance" heading was added by the author — theme is being reframed)
miro: "https://miro.com/app/board/uXjVMBRtQEA=/?moveToWidget=3458764681730102016"
related:
  - "[[domain-knowledge-base]] — domain packs are one asset class the hub governs"
  - "[[context-governance]] — verified traces feed the context layer"
  - "[[ai-governance]] — the risk/control side of the same object; overlap flagged below"
---

# Skills Hub / Agents & Skill Governance

**Tagline:** One place where reusable AI assets live — skills, traces, domain packs — with owners, versions and visible usage. Against the default state where useful AI work is scattered and invisible.

> ⚠️ Overlap: the *control* side of agent governance — risk tiering, audit trail, prod-access risk, agents-supervising-agents — is written up in [[ai-governance]]. This file covers the *asset* side: skills and agents as content that has owners, versions, certification and a lifecycle. Read them together; do not duplicate bullets between them.

## What is it

The problem it fixes: useful AI contribution is scattered and invisible. Analysts solve real tasks with agents, but the traces leave for model vendors, a skill's author never learns who uses it, and domain knowledge stays locked in personal setups.

The hub is one governed place for reusable AI assets — skills, solution traces, domain packs, healthy data objects. Everything has an owner, a version and visible usage; improvements flow as pull requests, not as forks.

Motivation is engineered, not hoped for: points are awarded only for confirmed value and capped monthly, badges recognize classes of contribution, and penetration of the hub — not the count of published skills — is the program's north star.

## Key terms

- **Skill** — a packaged, versioned procedure an agent executes; the unit of reuse.
- **Trace** — a recorded solution path from task to result; raw material for new skills and eval sets.
- **Skill registry** — the catalog: owner, version, dependencies, usage statistics.
- **Contribution flow** — publish a new skill or land a PR into a shared one; accepted means reviewed and used.
- **Confirmed value** — a contribution counts only when accepted; monthly caps stop leaderboard farming.
- **Badge** — recognition tied to a class of contribution, not to raw activity volume.
- **Penetration** — share of the target audience active in the hub monthly; the honest program metric.

## Numbers for arguing with optimists

- 28.5% → 60% — hub penetration target in one large tech company's pilot; monthly active contributors 218 → 459+ out of ~764 in scope.
- A working point scheme: accepted trace — 15; accepted PR into a shared skill — 20, capped at 60 per month; a published accepted skill — 30, once per skill.
- ~50× — growth in DQ-checker creation rate after an agent skill took over authoring them, with domain data partners left only to approve. (course day 3, transcript)
- 160 datamarts covered with business-logic DQ checkers in one day, against ~3 weeks by hand — one steward, one skill. (course day 6, transcript)
- Skills are what carried agent accuracy from 21% to 95%+ in Anthropic's evals — the hub is where those skills get owners and versions.
- Anti-metric: never reward «N prompts per week» — any activity metric without confirmed value gets farmed.

## From the course (Data Governance Fundamentals, 6 days)

### Skills and agents are a new asset class in the catalog

- The course puts it plainly: catalogs are expanding beyond marts — Kafka topics, "and now agents, skills — all the entities that are starting to appear also require some cataloguing, with ownership attached and an evaluation of the links, for review and optimization of all these assets." Skills are content; content management already knows how to handle content. (course day 4, transcript)
- The governance response is the ordinary content-management loop, transplanted: "a registry and cataloguing of agents, their certification, identifying the good and the bad — reuse of the good, deletion of the bad. This usual content-management practice must appear and apply to agents / skills." (course day 6, transcript)
- The enabling infrastructure named alongside it is a **metadata lakehouse**: one large store of all metadata — not only from the warehouse and BI systems, but from observability tools, repositories and metric semantic layers — framed as the reaction to "for the AI revolution we need metadata of a different level and volume." A skills registry is one tenant of that store, not a standalone tool. (course day 4, transcript)

### The Agentic AI governance table

The one slide dedicated to this theme pairs six new challenges with six countermeasures. It is worth reproducing whole because it is the only place the course commits to a control set. Agentic AI is defined on the slide as "systems that autonomously plan and execute tasks — they read, change and pass data without a human at every step." (course day 6, slides p.93)

| Challenge for the CDO | Governance response |
|---|---|
| Agents can read data from 10+ systems autonomously | **Inventory** — a registry of all AI agents with a description of their data access |
| No explicit human approval of every operation | **Standards** — a policy for verifying agents before production |
| The audit trail is far harder — who did what? | **Monitoring** — real-time observability of all agent operations on data |
| Prompt-injection attacks via data from external systems | **RBAC+** — extended access control that accounts for AI agents |
| Agents can bypass standard access policies | **Lineage** — tracing every data change made by agents |
| AI agents as a new threat vector | **Management** — a monthly governance council for AI-agent control |

Sources cited on the slide: Microsoft Data Security Index 2026, Deloitte CDO Survey 2025. (course day 6, slides p.93)

### The skill as a technical data steward

- The most concrete claim in the course about what a skill *is for* in a data organization: "you can create a skill in Claude Code that researches the upstream and packages it well into documentation, including lineage. These are AI technical data stewards, in effect — they fill the gap in missing metadata that was often the cause of failure in data catalogs standing half-empty." (course day 4, transcript)
- The author treats this as a bet being paid off, not a demo: "one of the bets in data management is genuinely being closed by this functionality." That is the strongest available argument for why a skill deserves an owner and a version — it is doing a role's job. (course day 4, transcript)
- Second worked example, from DQ: an agent skill that authors checkers itself, with data partners only approving them by eye. "It does it very well — it looks at the upstream, studies the whole lineage, and proposes good, complex *business* checkers." Checker creation grew about fiftyfold. The author's own caveat stays attached: "there is still room to strive — I can't yet say we do this at that rate routinely." (course day 3, transcript)
- Third example, the same skill at full stretch and its immediate consequence: a domain data steward covered 160 datamarts with business-logic checkers in a day, work that normally takes ~3 weeks. Then the next bottleneck appeared instantly — the checkers flooded incidents, which required an incident-management agent *plus* an eval-agent judging whether each checker was adequate, because some are fake for lack of business context. Verdict: "the boost survives after subtracting validation costs, but it is smaller than the first emotions." (course day 6, transcript)
- Structural lesson from that story for hub design: a skill that produces objects also produces the obligation to govern those objects. Publishing the skill without the downstream loop moves the bottleneck rather than removing it. (course day 6, transcript)

### Certification is coming for agents — deliberately not yet

- The certification chain is drawn explicitly through the whole delivery path: certified marts → certified semantic-layer objects → certified dashboards and metrics → **certified agents**. (course day 5, transcript)
- And the honest pause: "agents in principle deserve certification too, but for now it's a very shaky zone and we are not climbing into it — although it is already clear that the same sprawl is coming there soon, and governance will be needed there too." A rare case of a course author naming a frontier and declining to pretend it is solved. (course day 5, transcript)
- The prediction that makes the pause uncomfortable: "the volume of code, dashboards and other data artefacts will grow by an order of magnitude. Those who swam out of the content chaos need to take a breath before diving again." (course day 6, slides p.96)
- And the economic counterweight that will shape which skills survive: "after the 'Wild West' strategy comes the counting of burned tokens — many scenarios may simply not pay off. There is not yet enough data to compare with the labour cost of doing it the old way." (course day 6, slides p.96)

### The distribution mechanism the course actually recommends

- The course's answer to "how do assets reach people" is not a portal but a **bot that walks up to owners**: governance bots that either notify the relevant people about triggers on their objects, or ask users to act — write documentation, certify, archive — thereby keeping metadata current. The next stage named on the slides is a DG bot that walks up to owners — "can I archive this?" / "this looks certification-worthy, fill the docs" — with AI generating the documentation draft by button; the same pattern is what the author expects to replace gamified cleanup marathons. (course day 4, transcript; day 3, slides p.108; transcript)
- Paired with it, the AI "generate description" button so a hard gate does not feel like friction: one company's rule "no description — no prod deploy" moved table-description quality from 49% to 86% in a year across ~7 000 tables, and the generate-button is what made the gate survivable. That is the shape of skill distribution the course endorses — a skill embedded at the point of friction, not a catalog page. (course day 4, slides p.48; transcript)
- Motivation lesson transferable from stewardship, and the reason a hub needs more than a leaderboard: "everyone who gets to formalizing stewards realizes the global problem was not defining them but motivating them — it's always a second hat, a role, not a position." (course day 1, transcript)

### Model-access reality that constrains any hub design

- The stack split the author observes: companies that cannot use Western models run fine-tuned open source in local contours; those who can, use commercial frontier models — "better, but not by multiples; an open-source model handles most DG queries fine." A skills hub therefore has to be portable across model backends rather than assume one. (course day 6, transcript; day 3, transcript)
- At a large marketplace both run side by side: a fine-tuned in-house open-source model plus a green light for external models routed through an internal gateway. (course day 3, transcript)

## Anti-patterns

- **Publishing a skill without the loop it creates.** The 160-mart story is the canonical case: the skill's output became the next bottleneck within a day. Ship the skill together with whoever handles what it produces. (course day 6, transcript)
- **Treating agent output as finished work.** Human-in-the-loop is not optional yet: "everywhere review is required, otherwise various undesirable events occur" — the observation is drawn from companies a year ahead on adoption. (course day 6, transcript)
- **Ignoring the verification cost when you pitch the boost.** "The boost survives after subtracting validation costs, but it is smaller than the first emotions." Pitch the net number. (course day 6, transcript)
- **Letting agents run under a shared user account.** Today agent access = user access, and "it is not very clear what was done by whom." Registration of agents bound to employees is the stated next step. (course day 6, transcript; slides p.96)
- **Certifying agents before you can certify what they stand on.** The chain runs marts → semantic objects → dashboards/metrics → agents, in that order, for the same reason certification runs marts before reports. (course day 5, transcript)
- **Agents auditing agents as the whole answer.** "It smells slightly of loss of control" — the observability layer over agents will itself be agentic, and the author explicitly flags that as an open question, not a solution. (course day 6, transcript; slides p.96)
- **Counting activity.** The stewardship-motivation lesson applies unchanged: rewarding volume produces volume. (course day 1, transcript)

## Questions to ask

- Where is the list of agents and skills running against your data today, and who owns each one? (course day 6, slides p.93)
- Which skills produce new governed objects — checkers, descriptions, marts — and who handles the output volume? (course day 6, transcript)
- Can you reconstruct, from logs, which agent generated a given query or code change? (course day 6, slides p.93)
- What is your policy for verifying a skill before it touches production? (course day 6, slides p.93)
- Is your skills layer portable across model backends, or wired to one vendor? (course day 6, transcript)
- What is the net productivity number after validation cost — not the first-week number? (course day 6, transcript)
- When you decide to certify agents, what will "certified" guarantee — and who revokes it? (course day 5, transcript)

## Что не покрыто этим источником

- **The hub as a programme** — contribution flow, accepted-vs-published distinction, point scheme with monthly caps, badges, penetration as north-star metric: в материалах курса Data Governance Fundamentals не раскрыто; основной источник по теме — авторский курс BI+AI Strategy. The DG course reaches "registry + certification + ownership" and stops there.
- **Traces as a governed asset class** — recording solution paths and promoting them into skills or eval sets: в материалах курса Data Governance Fundamentals не раскрыто; основной источник по теме — авторский курс BI+AI Strategy. The DG course discusses mining *support-chat* history for few-shots (see [[domain-knowledge-base]]), which is a different mechanism.
- **Skill review and PR-based improvement mechanics** — versioning, dependencies, fork-vs-PR norms: в материалах курса Data Governance Fundamentals не раскрыто; основной источник по теме — авторский курс BI+AI Strategy.
- **Measured penetration numbers** (28.5% → 60%, 218 → 459 contributors) come from the BI+AI Strategy pilot, not from the DG course.

## Sources

- Microsoft Data Security Index 2026 and Deloitte CDO Survey 2025 — cited on the course slide for the agentic-AI control set (course day 6, slides p.93).
- Anthropic — skills as the unit of governed agent capability: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- Anthropic — Agent Skills: https://claude.com/blog/skills
- Model Context Protocol: https://modelcontextprotocol.io/
- Author's course «Data Governance Fundamentals» (6 days), day 1, 3, 4, 5, 6 — slides and transcript.
- Author's course «BI+AI Strategy 2026», Skills Hub program module; field notes: https://t.me/datanature
