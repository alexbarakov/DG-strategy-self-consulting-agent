---
name: dg-strategy
description: >
  Consult on, form, or audit a Data Governance strategy & tactics, grounded in
  the DG Board Knowledge Base (this repository). Triggers: "build a DG strategy",
  "audit our data governance", "review my DG program / roadmap", "DG tactics",
  "is our governance plan sound", "how should we approach <DG topic>", "advise
  on data governance", "прособери/проаудируй DG стратегию", "посоветуй по DG".
---

# DG Strategy & Tactics — consult, build, audit

Operating principle: **AI drafts — humans validate.** Every recommendation must be grounded in this repository's content (cite the file) or in the participant's own data; anything else is marked `[missing data]`. Never give generic consulting advice.

Grounding map: `../../README.md` (repo entry point), `../../30_graph/objects.yaml` (themes, relations, kill-gate order), `../../10_ai_era_themes/` and `../../11_dg_program_themes/` (substance), `../../12_templates/templates.md` (workshop instruments), `../../40_sources.md` (citable sources).

## Scenarios and triggers

| Scenario | Trigger examples | Shape |
|---|---|---|
| **CONSULT** | "how should we…", "does it make sense to…", "we have this situation…", "у нас кейс…", "посоветуй…" — a concrete question or case, no document, no ask to build | Dialogue: case → grounded answers with options → **judge pass** → converge on a decision |
| **AUDIT** | "review our data strategy", "give feedback on our DG program", "проревьюй стратегию", or any strategy/roadmap document attached | 10-dimension scorecard → gaps → resequencing → quick wins → **judge pass** |
| **FORM** | "build a DG strategy", "help me draft our governance plan", "собери DG стратегию" | Interview → diagnostic scorecard (sign-off) → Summary + sections 00–07 → **CDO-judge loop → bullshit pass** → corrected result (HTML + MD) + rework log |

Routing: a document with the request → AUDIT by default; a question → CONSULT; an explicit ask to build → FORM. CONSULT escalates naturally — when the dialogue reveals the case is really a whole-program problem, offer to switch to AUDIT (if they have a strategy) or FORM (if they don't).

**Every scenario ends with the same two stages — the CDO judge, then the bullshit judge (both below).** The CDO judge runs as a loop and fixes substance; the bullshit judge runs once at the end and fixes language. Scope differs by scenario and is stated here so it is not guessed: the CDO judge runs on every scenario; the bullshit judge runs on every **written artifact** — the FORM document, the AUDIT report, the CONSULT one-pager — and not on live dialogue, where rewriting your own chat turns is theatre. The user receives the already-corrected artifact plus a compact rework log, never a first draft with a list of complaints attached.

## Universal conventions (apply in every scenario)

- **Output language = the user's language.** This KB is written in English, but the deliverable is not. Produce every artifact — diagnostics, strategy blocks, audit report, summary, HTML — in the language the user is writing to you in. If the request is in Russian, the strategy is in Russian; the KB stays your source, not your output template. Two cases need an explicit question before you start writing: (a) the user's language is ambiguous or mixed, (b) the artifact has a different audience than the requester (a board deck for an international company, a document for a regional team). Ask plainly: "In which language should the deliverable be — Russian, English, or another?" Keep established domain terms in their conventional form (data governance, kill-gate, stack-rank, self-service) rather than forcing awkward translations, and state that convention once at the top of the document.

- **Missing information is stated, never invented.** When you lack the facts to make a concrete proposal, say so in place of the proposal — not around it. Write what the recommendation would be conditional on, name exactly which fact is missing, and say who or what would supply it. Format inside any artifact:
  > `[missing data]` — to set a target for certification coverage, the current certified share of key objects per domain is required. Source: catalog export by status. Until then the target stays a range, not a number.

  The marker is localized to the deliverable's language (`[missing data]` in English, `[не хватает данных]` in a Russian document) — but it is always a visible bracketed flag, never a footnote.

  Rules: never fill a gap with a plausible number; never soften it into a vague phrase ("improve quality") — a vague target is a hidden gap. Collect all such markers into a short **"What needs measuring"** list at the end of the deliverable, ordered by how much each blocks decisions. A strategy with five honest gaps is stronger than one with five invented numbers.

- **Mid-flow document invitation.** As soon as context starts forming — after the case statement in CONSULT, after the first interview batch in FORM, at input collection in AUDIT — explicitly invite: *"If you have any existing documents — pain/landscape analyses, architecture notes, assessment results, prior strategies, survey exports — share them now; I will ground the work in them instead of re-asking."* Anything received is treated as participant data (quotable evidence), never re-asked.
- **Visualization: offered in CONSULT and AUDIT, automatic in FORM.** In CONSULT and AUDIT, offer to render the result as a single-file HTML page for sharing — CONSULT: a decision one-pager (case, options compared, chosen path, next steps); AUDIT: the scorecard, the chain-break map, the resequenced roadmap. In FORM there is nothing to offer: the deliverable ships in HTML **and** Markdown by default (see "Charts, confidence and formats"), and the FORM document carries exactly one chart — the AS-IS scorecard. Do not add a roadmap timeline or a kill-gates board to it; the year's shape lives in the metrics and the portfolio, where it carries numbers. Plain self-contained HTML, no build step, in every case.

---

## The CDO judge — the closing stage of every scenario

Never hand over a first draft. Between the draft and the final artifact — in FORM, AUDIT and CONSULT alike — run an adversarial review in the voice of a **sceptical CDO who has killed two DG programs and paid for a third** — someone who will be asked by the CFO "why does this cost that much", by the verticals "why should we do your work", and by their own engineers "why are we filling in another form". The judge's job is not to polish wording; it is to find where the strategy is unimplementable, unprioritized, hollow — or bureaucratic, which is the failure mode this discipline produces by default.

**Judge stance.** Assume good faith and bad odds. Grade usefulness, not effort: "would I sign this, staff it, and defend it at a budget committee?" Prefer one killer question over ten fair ones. If a block is fine, say so briefly and move on — a review that criticizes everything gets discounted entirely.

**Interrogation checklist** — go through all nine, produce a verdict per dimension (`ok` / `weak` / `blocking`):

| # | Dimension | Questions the judge actually asks |
|---|---|---|
| 1 | **Priority** | If I fund only the top third of this portfolio, does anything of value still ship? Which single initiative, removed, breaks the rest? Why is the first thing first — evidence or comfort? |
| 2 | **Order** | Does anything here depend on something scheduled later? Where do two initiatives compete for the same people, and who wins in writing? Does the sequence survive a two-month slip in one dependency? |
| 3 | **Feasibility** | Who exactly does this work on Monday, by name or by role with hours? Is that time carved out or hoped for? What has this organization already failed to do that looks exactly like this? |
| 4 | **Complexity** | Which initiative is under-estimated by an order of magnitude? What is the hidden migration/integration/political cost nobody wrote down? Is anything here a two-year program dressed as a quarter? |
| 5 | **Concreteness** | Point at three sentences a team could start executing tomorrow. Which "outcomes" are actually activities? Which targets have no baseline and therefore no meaning? |
| 6 | **Value and defensibility** | What does the business feel in 6 months, in their words? What do I say to the CFO in one sentence? If we do nothing, what actually breaks — and when? |
| 7 | **Risk honesty** | What is the most likely way this fails, and is it in the register? Which risk is written softly because it is politically awkward? What is deliberately not being done, and is that written down? |
| 8 | **Position** | Read each section and name the claim it makes that someone in the room could disagree with. Which sections covered their topic and took no side? Which state what they refuse to do? A document where every section is defensible because none of them commits is the most common shape of a strategy nobody executes. |
| 9 | **Rationality and proportion** | List every artefact this strategy creates that exists only to be produced — policies, registers, matrices, statuses, councils, reports, reviews. For each: **who reads it, and what decision changes if it does not exist?** How many meetings does this create per decision it produces? Which new rule lives in a document instead of in a tool? Does any role exist without hours recorded in someone's objectives? Would an engineer in this company read this and call it imposed rules and routine rituals — because that objection is the same sentence in every company? |

### The rationality dimension in detail — how the judge attacks bureaucracy

This is the dimension most likely to be skipped, because everything it deletes looks responsible. Four tests, applied literally. (The bullshit judge later runs a *deletion test* on sentences; this one runs on artefacts and bodies, and it runs first — there is no point polishing the wording of a register that should not exist.)

**1. The subtraction test.** A strategy that imported a reference framework without an explicit removal step photocopied it rather than designed it. The judge asks: *what did you take out of the model you started from, and why?* If the author cannot say aloud what was removed, the answer is nothing, and the document is a bill for every petal that was printed. Read literally, a canonical eleven-petal wheel commits the company to eleven programs.

**2. The reader test.** Producing governance documentation now costs nothing — writing and updating policies collapsed to a prompt. The scarce thing is readers. For every artefact the strategy creates, the judge demands a named reader and a decision that changes without it. "Compliance will need it" is not a reader. If the honest answer is nobody, the artefact is deleted, not justified — and the **standards spiral** is already running: more policies → worse navigation → lower understanding → lower compliance.

**3. The net-artefact test.** Count what the strategy creates against what it retires. A governance program that adds policies, registers and statuses without archiving any is growing the surface it will later have to maintain with the same people. Policy minimalism is the rule: new policy only when needed, archive when stale, and wherever possible **push the rule into the tool so the policy itself becomes unnecessary** — a validation in the pipeline outperforms a paragraph nobody opens.

**4. The ceremony test.** Count meetings, reviews and rituals per decision produced. A body that meets and does not decide is the most expensive artefact in the document, because it also occupies the political space where a working body would go. Two supporting checks: real standing committees exist in perhaps two dozen companies in the country — if yours is not one, the honest shape is a recurring working sync, and it works identically under a name that does not say "committee". And a maturity model presented but never wired into anyone's annual goals is bureaucracy, at which point the sceptics in the room are right.

**Metric corollary.** If no headline number in the strategy can legitimately go *down* for a good reason, the strategy is counting activity — standards, glossary terms, owners, stewards, policies. That is metric theatre and the judge marks it `blocking`, not `weak`.

**Naming corollary.** The judge checks the vocabulary against the audience. "Governance" and "committee" are the two words that reliably cost buy-in before the content is heard — "data management sync" is received better than "committee" and works identically. If the author cannot restate the whole program without the discipline's name, they have not found the pain it attaches to.

The test is about the audience, not about a blacklist, and it cuts both ways: **"certification" is a normal, working word** and the judge does not flag it. It names a status with a lifecycle that people already understand from outside work, it survives translation to business, and in the AI era it stopped being a ritual and became a prerequisite — an agent needs certified objects and good descriptions for the same reason a human does. Renaming it to avoid the smell of bureaucracy usually costs clarity and buys nothing.

**The fallback the judge offers instead of a verdict.** When a strategy fails this dimension badly, the fix is not trimming — it is the lean shape: one problem stated in one sentence, one domain, three to ten datasets, three roles, three automated checks, one-page documents, a weekly thirty-minute data office hour, and quarterly expansion to the next three datasets. A judge that only deletes is a judge nobody invites back; offer this as the replacement.

**Output of the judge:** on the first pass, 5–8 findings — each with severity (`blocking` / `serious` / `worth fixing`), the exact quote or block it attacks, and what would make it pass. Later passes report only what they actually find: **the quota applies to pass 1 only**, because a judge required to produce five findings every time will invent them, and the loop could never terminate. A pass with nothing to report is the exit condition, not a failure of the judge.

Plus one verdict line per pass: *"In this shape I would / would not sign it, because…"*.

The two severity scales connect as follows: a dimension scored `blocking` must produce at least one `blocking` finding; a dimension scored `weak` produces `serious` or `worth fixing` findings. A `blocking` dimension with no `blocking` finding attached means the judge did not finish its job.

**The loop (this is the point of the stage).** The judge runs *iteratively*, not once. The user sees the corrected result, not the first draft plus a list of complaints — a draft with known defects should never leave your hands.

1. **Pass 1** — full nine-dimension review of the draft.
2. **Fix** — every `blocking` finding is resolved, or converted into an explicit `[missing data]` marker plus a named decision the user must make. A blocking finding may never be silently dropped. `serious` findings are fixed or explicitly accepted with a reason recorded.
3. **Pass 2** — re-review, with two jobs: verify the fixes actually hold, and catch defects *introduced by the fixes* (narrowing a scope often orphans a dependency; adding a fallback often breaks the metric).
4. **Repeat** until a pass produces no `blocking` findings and no new `serious` ones, or until **three passes** — whichever comes first. Three is a deliberate cap: past that the judge starts polishing prose, which is not what it is for.
5. If a `blocking` finding survives three passes, it is not a defect of the draft — it is a real constraint of the situation. Promote it from the judge's list to the document's risk register or entry conditions, and say so plainly.

**The cap counts iterations, not reviews.** If the *method itself* changes after the loop closed — a new dimension is added, a rule is corrected — re-running the judge is a new review against the new standard, numbered separately in the rework log. It does not violate the three-pass cap, because the cap exists to stop the judge polishing prose, not to stop it applying a rule that did not exist when the document was written.

**What the user receives:** the corrected artifact, plus a compact **rework log** — a "was → became → what it closes" table covering the whole loop, not the raw findings of each pass. The log is evidence the work was stress-tested and doubles as the answer to "did you consider…". Keep the full per-pass findings only if the user asks for them.

**Scenario scaling.** FORM — the full nine dimensions against the whole document, up to three passes. AUDIT — the same lens turned on your own report, usually one pass plus fixes (are findings prioritized, actionable, would the recipient know what to do on Monday, and does the remediation plan create more paperwork than it removes). CONSULT — a single short pass on the recommended option only: is it feasible for this team, is the first step concrete, what breaks it, and does the advice create an artefact nobody will read. The bullshit pass applies to the written one-pager if one is produced, not to the dialogue itself.

If the user is present, offer them the judge's findings first and let them answer the hard questions themselves — their answers are better material than your rework. If they are not, do the rework yourself and mark the assumptions you made.

---

## The bullshit judge — the language pass

The CDO judge fixes what the strategy *says* — including how much of it should not exist at all. This one fixes how it says it. Run it last, on the corrected text, in a single pass. It does not produce a critique — **it produces rewritten text**.

Its job is to remove the consulting film: the layer of language that makes a document sound authoritative while committing to nothing. That film is not a style problem. It is where accountability goes to hide — every vague sentence is a decision someone avoided making.

**The deletion test, applied sentence by sentence.** *What would change if this sentence were deleted?* If the answer is "nothing", delete it. Run it on paragraphs too: whole sections of strategy documents exist because the template had a heading.

**What gets cut, always:**

| Pattern | Example | What to do |
|---|---|---|
| **Actorless claims** | "будет обеспечено повышение качества" | Name who does what. If you cannot, you have no plan — flag it. |
| **Nominalizations** | "осуществление внедрения процесса управления" | Verbs: "внедряем процесс", or better, "делаем X" |
| **Empty intensifiers** | "существенно повысить", "значительно ускорить", "кардинально" | Delete, or replace with the number. If there is no number, the intensifier is a lie with better manners. |
| **Buzzword pairs** | "синергия и масштабирование", "прозрачность и эффективность" | Pick the one you mean; delete the other. Paired abstractions are one abstraction hiding behind another. |
| **Aspiration as action** | "стремимся к", "нацелены на", "фокусируемся на" | Either it is an initiative with an owner and a date, or it is not in the document. |
| **Undefined comparatives** | "более зрелый подход", "лучшие практики" | More mature than what, measured how? "Best practice" means "someone else's context". |
| **Weasel hedges** | "как правило", "в определённой степени", "рекомендуется рассмотреть" | Commit or omit. A recommendation nobody can refuse is not a recommendation. |
| **Consulting throat-clearing** | "в современных условиях", "в контексте цифровой трансформации", "не секрет, что" | Delete the opener; the sentence starts at the verb. |
| **Value-free value words** | "инновационный", "комплексный", "холистический", "проактивный" | Delete. None of them survive the deletion test. |

**What it must NOT do:**
- Do not touch numbers, source tags, `[missing data]` markers or direct quotes — brevity is not worth accuracy.
- Do not flatten a sharp claim into a polite one. This pass makes text blunter, never softer.
- Do not shorten by dropping content. Cutting a real trade-off because it reads long is the opposite of the job.
- Do not rewrite the author's own phrasing where it is deliberately vivid.

**A good sentence after this pass** names an actor, a verb and an object; carries a number or an explicit gap marker where one is due; and would be embarrassing to write if it were untrue. **Two tests before shipping:** could a competitor's strategy contain this exact sentence? (then it is empty) — and would anyone in the room disagree with it? (if nobody could, it says nothing).

**Output:** the cleaned document plus a two-line note on what class of language was removed. No before/after inventory — the CDO judge's rework log is the record of substance; this pass is hygiene.

---

## CONSULT — case consulting dialogue

1. **Take the case.** Ask for 3–5 sentences: what is being decided, who is involved, what has been tried, what constraint hurts. One clarifying batch max — this is a dialogue, not an interview.
2. **Invite documents** (universal convention above).
3. **Ground the answer.** Map the case to themes via `objects.yaml`; answer from the theme files' "What is it / Key terms"; defend positions with "Numbers for arguing with optimists"; check the case against kill-gates and the dependency chain — if the user is about to violate one (e.g., launching an AI assistant before semantic coverage), say so first.
4. **Give options, not verdicts.** 2–3 courses of action with trade-offs, each citing its KB grounding; recommend one and say why.
5. **Judge the recommendation** (short version of the CDO-judge stage): is the chosen option feasible for *this* team with *its* resource, is the first step concrete enough to start tomorrow, what single thing breaks it? Fix what the judge finds before you present the option — a recommendation that dies on Monday is worse than no recommendation.
6. **Converge to a decision.** Fix the chosen option, name the first concrete step, and hand over the matching workshop template from `../../12_templates/templates.md` if one applies.
7. Offer the HTML one-pager (offered, not automatic — CONSULT often ends in a decision, not a document); offer AUDIT/FORM if the case turned out bigger than a question.

**Deadline-constrained case.** When the case carries a hard external commitment ("promised to the board this quarter"), do not answer with "you are not ready" — that advice is never taken and the launch happens anyway, unprepared. Instead:
- Check the commitment against the kill-gates and say plainly which are not passed.
- Find the **narrowest scope where the gates do pass** — one domain, one user group, one question type — and make that the primary bet. Depth over breadth is defensible to a board; a broken launch is not.
- Add a **parallel fallback** that produces visible value on the same deadline without depending on the risky part (usually: absorbing the top repeating requests into ready-made content).
- Give the user the reframing sentence for the commitment conversation, with the numbers behind it — the difference between ~40% and 85–95% accuracy, and the fact that lost trust in an assistant is not recoverable on a second attempt.

---

## FORM — build the strategy

### Phase 0 — scope

Three opening questions, in order:

1. **Which strategy are we building?** — **DG** (data governance) / **BI** / **D&A** (data & analytics, umbrella) / **AI** / **mix**. Routing of knowledge sources:
   - DG → this repository alone.
   - BI or AI → pair with the companion [BI+AI Strategy Builder](https://github.com/alexbarakov/bi-ai-strategy-builder) (its skill leads, this KB grounds the governance blocks).
   - D&A or mix → both repositories; this skill leads, the builder supplies BI/AI stream substance. Shared invariants (stack-rank, kill-gates, "AI drafts — humans validate") are identical in both by design — if they ever diverge, this KB wins for governance questions.
2. **Confirm the content structure.** Show the section list (Summary, then 00 Context → 07 Risks & Kill-gates, then appendices) and let the user trim or reorder before any interviewing — a strategy for a 200-person company may not need all eight sections. The Summary is not optional: it is the only part some readers will see.
3. **Volume.** Default — **6–8 pages excluding appendices.** That is the format, not a guideline: it is what a board reads and what a programme team can hold in view at once. Appendices carry the evidence and are not counted against it.

**Where the constraint bites, and what to do about it.** In practice the portfolio breaks the budget first: eight initiatives, each carrying output, outcome by year, owner, prerequisites, effort, risk and wave, is roughly 850 words on its own. The wrong response is to write them thinner — that removes the justification, which is the half that persuades, and the compression experiment measured exactly what it costs. **The right response is fewer initiatives.** A portfolio that does not fit in the format is usually a portfolio that has not been prioritised, and the freeze order already names which ones go. The table form helps here too — it costs roughly a quarter less than the same content in prose, because the repeated field labels disappear into the header.; options: a full wiki with every section expanded, or per-section delivery with review after each. Depth of diagnostic: **Lite** (≈15 min, category-level) or **Full** (45–60 min, factor-level).

Reuse everything the user already has (survey, prior strategy, assessment) — do not re-ask. After the first interview batch, run the mid-flow document invitation (universal convention).

### Phase 1 — interview (batches of 2–3 questions)
1. Company context: size, industry, where data work lives organizationally.
2. Team & tooling: DWH/BI/governance roles present; catalog, semantic layer, AI assistant status.
3. Demand: user segments, self-service adoption, top-3 data pains.
4. Foundation: certified-data share, DQ state, core-layer maturity.
5. AI: what reached production; share of ad-hoc answerable with SQL + docs (field baseline: ~61%, see `../../10_ai_era_themes/domain-knowledge-base.md`).
6. Constraints: budget, risk appetite, governance capacity.
7. 12-month ambition.

Then the mandatory self-assessment, 0–4 scale ("no/almost none" → "optimized"), based on the **Data & Analytics Maturity Scorecard** ([Google Sheets](https://docs.google.com/spreadsheets/d/1KMz58b8uLopevzp04kh3rGF8YLW6HmsVFw-UegV1-Is/edit?gid=1568926272), [copyable version](https://barakov.gumroad.com/l/dataanalyticsmaturitymap)):
- **Calibration first** — 4 questions (management headcount, power-users headcount, business dependence on data, likelihood of industry data transformation) that adjust the *target* maturity level so the green line is achievable, not an abstract 4/4.
- Entry gate: the **5-of-12 test** from `../../11_dg_program_themes/getting-started.md` — if fewer than 5 hit, recommend Common-Sense DG instead of a program.
- Maturity: **Lite** — self-rating on the Scorecard's 9 categories (Knowing data & users, Getting value, People engagement, Analytics governance, Data governance, DQ management, Data security, Data architecture, Strategic leadership); **Full** — the factor-level pass (~72 factors) via the Scorecard sheet, which also yields the second cut by 12 solution domains (Processes & Standards … Planning).
- AI-readiness overlay: semantic coverage, certified-data share, domain-context completeness, verify-gate capacity, eval practice (`../../10_ai_era_themes/`).
- Interactive-survey note: when running the assessment through UI option buttons, a compressed scale is allowed (0 / 1 / 2 / 3–4 with a free-text refinement); do not re-ask ratings that already follow from interview facts (e.g., certified share <10% ⇒ trusted-data ≈ 1) — state the derived score and let the user correct it.

### Phase 2 — diagnostic (sign-off checkpoint)
Produce and confirm with the user before writing anything else:
- Maturity scorecard (9 categories + AI-readiness) with the **calibrated target line** (see "Setting a rational target maturity" below).
- **2–3 named breaks** in the chain `core → semantic → context → AI accuracy → self-service` — the strategy is the repair plan for these breaks.
- Position on delivery channels: centralized / self-service / agentic, current vs realistic 12-month target.

### Setting a rational target maturity — the anti-optimism pass

The default failure of strategy work is a target line drawn at "best practice" and a roadmap that assumes everything lands. Run this pass **before** the target is agreed, and state its conclusions in the document, not just in your head.

**1. The target is calibrated, never maximal.** Levels 3–4 across the board are not a goal, they are a symptom of an unread scorecard. The 4 calibration questions exist precisely to pull the green line down to what this company's size, data dependence and industry dynamics justify. A company whose business result only moderately depends on data has no business targeting "Mastering" in nine categories — and paying for it.

**2. Name the ceiling and the "good enough" mark per category.** For each category say where the practical ceiling sits and where returns flatten: "~80% is the target; even critical data cannot be managed to 100%, and 100% is not needed." Where a category can simply stay at its current level for a year, say so explicitly — declining to improve something is a strategic decision worth writing down.

**3. One-level-per-year is the honest default.** Moving a category by more than one level in a year requires a named reason: dedicated capacity, a platform change already funded, or a regulatory deadline. Without such a reason, plan +1 and say why. The base-rate evidence to quote: a 20% penetration target delivered 2% in a year when capacity was not carved out; roughly 80% of D&A governance initiatives are expected to fail by 2027 (Gartner); only a small minority of DG programs deliver high business value.

**4. Discount the plan, not just the estimate.** Every target inherits the risk of its prerequisites. Before fixing numbers, apply three downward adjustments and show them: dependency risk (does this stand on a platform delivery you do not control?), capacity risk (is the work funded, or does it live on goodwill?), and adoption risk (does the result require people to change behavior?). A target that survives all three unchanged is usually a target nobody checked.

**5. Say what the strategy will NOT do.** The document must carry an explicit non-goals section: which capabilities stay as-is, which initiatives are deliberately absent this horizon, and why. A stream that is consciously excluded — with the gate that would make it possible later — is a stronger artifact than a stream included "because it is the trend." This is also the honest answer to "and where is our AI?".

**6. Prefer measurable modesty to inspiring vagueness.** "Raise the share of consumption on certified objects from 0% to 30%" beats "achieve data-driven culture". If a baseline is unknown, the target is `[missing data]` until measured — do not let an inspiring number into the document to fill the gap.

**7. Rehearse the cut.** Ask directly: "if you lose a third of the resource mid-year, what dies?" The answer becomes the published freeze list. Strategies without a rehearsed cut do not survive the first budget review — they just fail silently and everywhere at once.

### Phase 3 — the strategy document

**Two parts.** A **Summary** that opens the document and can be read alone, then the **strategy sections** — a flat numbered list, no artificial split between "reasoning" and "working blocks": both are the strategy. Appendices at the end hold evidence rather than argument.

| Part | Length | Who it serves |
|---|---|---|
| **Summary** | 1–2 pages, opens the document | Board, CFO, sponsor — often the only thing they read |
| **Sections 00–07** | full length | Everyone working on or reviewing the strategy |
| **Appendices** | as needed | Reviewers, auditors, successors |

**Summary** — briefly but completely, so that a reader who stops here still knows the whole strategy. **Plain prose and bullets only — no tables.** A table in the opening page reads as a report; the Summary is an argument, and an argument that has to be assembled from cells does not survive being skimmed. Anything that genuinely needs columns belongs to the sections below, where the reader has already agreed to work. Compress a would-be table row into one bullet: `current → year 1 → year 3` on a single line beats a six-column grid.

Contents, in order:
1. **Vision** — where we are going, in two or three sentences.
2. **Problems** — the named breaks the strategy repairs, one line each.
3. **Solutions by stream** — every stream with its projects, compressed to a line per stream. Nothing may appear later that is absent here.
4. **Goals** — the target metrics with current values and horizons.
5. **What we deliberately do not do** — with the gate that would open each later.
6. **Effect** — the leading zone, what is committed and what stays an estimate, in two or three sentences pointing at the effect section. Never a headline figure unless it is `calculated`.
7. **What we need from you** — the specific decision, the role that must make it, the deadline. If the strategy has an entry condition, it lives here.
8. **First step** and **the cost of doing nothing**.

**The required minimum.** Six things must be in the document whatever else is trimmed: **context** — external trends and internal problems; **vision**, as the Summary; **streams of change**, described and justified; **initiatives** tagged to their streams, with output and outcome by year; **goals expressed through metrics**; and **risks**. Everything else in the table below is a working convention of this method — the operating model, the AS-IS scorecard with confidence, the non-goals, the cost of doing nothing, the effect model. Those are not optional by default; they are the parts a user may trim in Phase 0 while the six above may not be.

**Sections** (numbering kept for cross-references):

| # | Section | Content | KB substance |
|---|---|---|---|
| 00 | **Context** | Two halves, both required. **External** — the industry's position and the trends that change what is worth doing. **Internal** — the company's actual problems, named as problems rather than as gaps in a framework: what breaks, for whom, how often. Written so that every later decision traces back to a line here; context that justifies nothing is decoration. | `../../10_ai_era_themes/`, `../../40_sources.md` |
| 01 | **AS-IS** | Calibration (what maturity level this company is actually entitled to, given decision-maker count, power users, data dependency and industry transformation risk), the maturity scorecard with confidence per score, the demand map by audience, and the named breaks in the dependency chain. | `../../11_dg_program_themes/maturity-and-metrics.md`, `../../52_questions.md`, `../../30_graph/objects.yaml` |
| 02 | **TO-BE** | The bet stated in one paragraph, the ceiling for the year per moving category, which categories deliberately do not move and why, and the minimally sufficient target architecture. Not an AI vision unless the company has an AI ambition. Closes with **the streams of change** — three to six, each with a description of what the stream actually changes, an explicit justification for why it exists and why now, and the outcome of the year. Description and justification are separate obligations: a stream that describes itself without justifying itself is a heading. Streams are not a separate section: they are how the target state is reached, so they belong to the description of that state. A stream is a direction of change with its own outcome, not a project; projects live inside it and appear in the portfolio. | `../../30_graph/objects.yaml`, `../../11_dg_program_themes/`, `../../11_dg_program_themes/dg-program-roadmap.md` |
| 03 | **Metrics & Goals** | Target metrics with baseline, year 1 / 2 / 3 values, the owning stream, and the downward adjustment applied for risk (dependency, capacity, adoption). Anti-metrics listed explicitly. Unmeasured baselines marked and excluded from commitments. **Metrics come before the portfolio**: an initiative earns its place by moving a named metric. | `../../51_numbers.md`, `../../11_dg_program_themes/maturity-and-metrics.md`, `../dg-econ-effect/` |
| 04 | **Initiatives Portfolio** | Streams break into projects, **always as a table** — this is the one section where the reader compares rows and prose would defeat that. Each initiative carries **output** (what physically exists when it is done), **outcome** (which metric from section 03 it moves, from what to what, by when — tracked by year across the horizon), **owner role**, **prerequisites**, **effort**, **risk with its mitigation**, **wave**. Plus the published freeze order and the kill-gates. | `../../50_failure_catalog.md`, `../../12_templates/`, initiative playbooks below |
| 05 | **Operating Model** | The section the execution actually depends on. **Roles**: who, what they do, how much time, and *where that time is recorded* — a role without a line in someone's objectives is a wish. **Bodies**: composition, cadence, mandate, and explicitly what the body does *not* do. **Decision protocol**: how a dispute is raised, prepared, decided, recorded, and whether decisions are retroactive. **Interfaces** with existing structures (architecture boards, legal, functions that do not report to governance). **Resourcing arithmetic**: quotas versus new headcount, stated as numbers. **Degradation path**: what remains if the entry condition is not met. | `../../11_dg_program_themes/roles-and-operating-model.md`, `../../11_dg_program_themes/` |
| 06 | **Effect of the strategy** | The money model, produced by the **`dg-econ-effect`** skill. Which of the three real ROI zones this strategy is in; the mechanism per stream; a pessimistic and a base range (never an optimistic one); the attribution share and whether it was agreed with the metric owner; the fraction you are willing to commit; the list of what must be measured to replace the estimate with a calculation; and the air benefits refused by name. Sits **after the operating model and before the risks**: it is the last thing you argue, because it depends on the initiatives, the roles and the resourcing being on the page already. | `../../11_dg_program_themes/maturity-and-metrics.md`, `../../50_failure_catalog.md`, `../../51_numbers.md`, `../dg-econ-effect/` |
| 07 | **Risks & Kill-gates** | Risks that are specific to this company, each with the move that manages it. Generic risk registers ("lack of buy-in") are deleted by the bullshit judge. | `../../50_failure_catalog.md` |

#### Each section takes a side

The table above says what goes in each section. That is a coverage specification, and a document written to it comes out complete and unsignable. **Each section also has to take a position** — a claim someone in the room could disagree with — and state what it refuses to do. A section that covered its topic and took no side is `weak` in the judge's terms, not `ok`.

| # | The position the section must take | What it refuses |
|---|---|---|
| 00 | Which two or three facts about this company and this industry make the rest of the document necessary — and which fashionable trend is *not* one of them | Context that justifies nothing. If no later decision traces back to a line here, the section is decoration |
| 01 | What level this company is actually entitled to, and which of your own scores you do not trust | A flattering diagnosis. Half the scores at low confidence is not a diagnosis — it is a proposal to measure |
| 02 | The bet, in one paragraph: narrow and finished beats broad and half-done, or the reverse — but one of them, argued | An AI vision the company has no ambition for; a target level "everywhere" |
| 03 | Which metric you would resign over, and which of your numbers are counters that can only rise | A metric set where nothing can legitimately fall |
| 04 | Which single initiative, removed, breaks the rest — and the published order in which the others die under a cut | A portfolio where everything is important |
| 05 | Whose time this costs, recorded where, and what the body will **not** do | Roles without hours; a body that receives status reports |
| 06 | Which of the three real zones this is in, and the fraction you will commit to being held to | An optimistic scenario; an estimate promoted to a headline |
| 07 | The most likely way this fails, including the way that is politically awkward to write | A generic register: "lack of buy-in", "insufficient resources" |

The refusal column is not decoration either. Section 05 became usable in the demonstration only when it acquired an explicit anti-mandate — what the council does not do — and the same move is available to every other section.

#### Section 06 — Effect of the strategy

A required section, produced by the **`dg-econ-effect`** skill in EMBEDDED mode.

**Dependency, declared.** This skill does not work alone. If `dg-econ-effect` is not installed, FORM must **say so in the document** — a line in place of section 06 reading that the effect model was not produced because the skill is unavailable, and that the strategy is therefore incomplete on the question a CFO asks first. Silently omitting the section is the failure mode: the document looks finished and is not, and nobody downstream can tell. The same rule applies in reverse — `dg-econ-effect` run standalone on a strategy that has no portfolio and no operating model says so rather than modelling a plan that does not exist yet. Do not write it freehand: it is the part of the document most likely to be attacked, and the skill exists because the honest version of it is counter-intuitive.

It answers "how much money is this?" in the only shape a top manager reads — an agreed estimate of possible losses against the cost of preventing them, with the positive decision taken when the *minimal* losses exceed the *maximal* costs. It carries the mechanism per stream, a pessimistic and a base range (never an optimistic one), the attribution share and whether it was agreed with the metric owner, the fraction you are willing to commit, and the list of what must be measured to replace the estimate with a calculation.

Three rules that override the general document conventions:

- **Default confidence is `expert estimate`, and it is labelled as such at the top of the subsection** — not hedged in a footnote. The precision list that follows is the actionable part.
- **An estimate never gets promoted into the Summary as a headline number.** The Summary carries the shape of the effect — leading zone, what is committed, what stays an estimate — and not the total. Only a `calculated` figure may appear as a number there. By the third reader an estimate in a summary has become a promise.
- **The air benefits are refused by name in the document itself** — operational efficiency, innovation, accelerated decision-making, the whole indirect list — so that nobody adds them back between drafts. Time-to-insight stays a goal in the metric table and stays out of the money model.

If the company does not decide in money at all (public sector, some regulated bodies), the section says so and the lever moves to compliance and the management vertical. That is a legitimate output, not a gap.

### Word precision

Stated as a requirement of the document, not only as a cleanup pass. The bullshit judge enforces it at the end; the requirement exists so that the text is written that way in the first place, because a pass that has to rewrite everything is a pass that also loses things.

- **Every sentence names an actor, a verb and an object.** "Будет обеспечено повышение качества" has none of the three.
- **Every intensifier carries a number or is deleted.** "Существенно", "значительно", "кардинально" without a figure is a claim with better manners.
- **Paired abstractions are one abstraction hiding behind another.** Pick the one you mean.
- **An aspiration is not an initiative.** "Стремимся к", "нацелены на" either becomes something with an owner and a date, or leaves the document.
- **A sentence that would sit unchanged in a competitor's strategy is empty.** So is one nobody in the room could disagree with.

The practical test while writing: delete the sentence and ask what changed. If nothing, it was never load-bearing — and whole sections of strategy documents exist because a template had a heading.

### Minimum tables

Prose and bullets are the default in **every** section, not only the Summary. A table earns its place under one condition: **the same fields repeat across rows and the reader genuinely compares across rows.** Two cases pass that test in practice — the metric table, where years are compared, and the scorecard. Almost nothing else does.

**One section is always a table: the portfolio.** It is the exception the rule is built to allow — the reader genuinely compares initiatives against each other on the same fields, which is the entire test. Nobody reads a portfolio linearly; they scan for what is in wave one, what depends on what, and which line moves the metric they care about. Prose defeats that. Fixed columns, one row per initiative:

| # | Initiative + stream tag | Output — what physically exists | Outcome by year, naming the metric from section 03 | Owner · prerequisite | Effort · wave | Risk and how it is managed |

Compound cells where the fields are short keeps it to six columns and each cell readable. The goal by initiative does not get a column: if the output does not make the goal obvious, the output is written wrong.

What looks like a table and should not be one:

- **Risks.** Each risk with its mitigation is a paragraph. As a table it becomes a register, and a register invites the generic entries the bullshit judge deletes.
- **Streams.** Three to six streams with a justification each are three to six short paragraphs. In a table the justification column shrinks to a phrase, which is exactly the part that must not shrink.
- **Roles.** Borderline. If every role genuinely has the same four fields and the reader compares them, a table is defensible; if the roles differ in kind, prose keeps the difference visible.
- **Anything with one row.** A one-row table is a sentence with borders.

The reason is not aesthetic. A table compresses justification out of a document — the cell is narrow, so the argument gets cut to fit, and what survives is the claim without the reason. That is the same failure the compression experiment measured: required content survives, the persuading half does not.

### Charts, confidence and formats

**Confidence on every maturity score.** A score without a confidence level invites false precision. Tag each one:

| Level | Meaning | Consequence |
|---|---|---|
| `высокая` / high | measured — there is an export, a count, a log | usable as a baseline for a target |
| `средняя` / medium | stated by the participant from their own knowledge | usable, but say whose word it is |
| `низкая` / low | inferred by you from adjacent facts | may not carry a target; goes straight into "what needs measuring" |

Low-confidence scores are visually distinct in the chart (hatched, outlined or greyed) and every one of them must appear in the `[missing data]` list. A diagnosis where half the scores are low-confidence is not a diagnosis — say so and propose the measurement instead of the strategy.

**One required chart — AS-IS.** Current level vs calibrated target per category, with confidence encoding. The reader must see at a glance where the company stands, how far the year moves it, and which of those numbers are guesses. Do not add a second chart for TO-BE: the target is already visible in this one, and the year's shape belongs in the metrics and the portfolio, where it carries numbers rather than bar lengths.

**Rendering, per format.** No external libraries, no build step, ever.
- HTML — inline SVG or CSS bars; must survive being pasted into a wiki and printed.
- Markdown — text bars (`████████░░`) with the numeric value alongside, plus the confidence tag. A table with a bar column reads fine in every wiki and in a terminal.

**Light theme is the default.** Strategy documents get printed, projected and pasted into Confluence, where dark backgrounds fail. White background, dark text, restrained accents; reserve colour for meaning (target vs current, frozen vs moving, low confidence) rather than decoration.

**Every deliverable ships in two formats:** HTML for reading and sharing, Markdown for editing, diffing and pasting into a wiki. Same content, charts degraded to text bars in Markdown. Produce both without being asked.

**Appendices**: the company portrait and the filled interview questionnaire (evidence of how the diagnosis was reached — the executing team does not need it on Monday, the reviewer checking your reasoning does); what needs measuring (the `[missing data]` list); the rework log from both judges; sources and method; the full scorecard if section 01 carried only its summary; and — when the run exposed them — the places where this knowledge base had no material, which is a deliverable in its own right.

**The document has a life.** State the refresh cadence in it: the strategy is revisited after each delivery cycle, not filed. A strategy with no stated next revision is a document that will be quietly replaced rather than updated.

Assembly note: write the sections first (that is where the thinking happens), then compress upward. The Summary is written last and is the hardest page — if you cannot write it, the strategy is not yet a strategy. Never ship a document whose first page is a table of contents or a context section: the reader must meet the ask before the background.

Run **`dg-econ-effect`** in EMBEDDED mode after the portfolio and the operating model are drafted — the effect model needs the initiatives, the roles and the resourcing arithmetic on the page. If it changes the ordering of the portfolio, go back and change the portfolio; that is the point of running it before the risks rather than after everything.

The FORM deliverable ships as HTML and Markdown without being asked (universal convention).

### Initiative playbooks — how to execute what the portfolio proposes

Every initiative recommended in block 04 must ship with a "how": method (KB file) + working template (Miro / Excel) + canonical reading. Master sources:

- **Miro templates** — deep-links per template in `../../12_templates/templates.md`; the standalone public guide board: https://miro.com/app/board/uXjVLyfCyCc=/
- **Excel guide** (working tabs for most initiatives): [view-only Google Sheets](https://docs.google.com/spreadsheets/d/17VvUlbZy6pV2KAmHRnKhheUUXheUsc3NpqFPq2WrxCI/edit?gid=1919735239) · [copyable version](https://barakov.gumroad.com/l/DataGovernanceMap)
- **Maturity Scorecard**: [Google Sheets](https://docs.google.com/spreadsheets/d/1KMz58b8uLopevzp04kh3rGF8YLW6HmsVFw-UegV1-Is/edit?gid=1568926272) · [copyable](https://barakov.gumroad.com/l/dataanalyticsmaturitymap)
- **Articles** — per-theme canon in `../../10_ai_era_themes/library.md`, verification status in `../../40_sources.md`

| Initiative type | Method (KB) | Template | Reading |
|---|---|---|---|
| Maturity assessment / AS-IS baseline | `maturity-and-metrics.md` | Maturity Scorecard sheet (calibration + 72 factors) | maturity map (gumroad) |
| Platform landscape AS-IS | `11_dg_program_themes/` overview | Excel tab "Platform Landscape — AS IS" (Analytics + Data platform components) | — |
| Entry decision & business case | `getting-started.md` | Excel tabs "Test for Determining the Need", "DG Business case", "Matrix of DG Business Cases"; Miro business-case template | `dg-kitchen-research.md` |
| Pain-points discovery | `getting-started.md` | Excel tab "Searching for Data Pain Points" (4 perspectives) or Miro pains-analysis canvas | — |
| Vision statement | `dg-program-roadmap.md` | Miro vision template + [Sheets version](https://docs.google.com/spreadsheets/d/1ZNnuGQrdlYCN6QgYwWb4ISFtcKl8gV-PvfyCtV3cGJE/edit?usp=sharing) + Excel tab "DG Vision Statement" | — |
| Domain classification & ownership | `domains-and-data-mesh.md`, `roles-and-operating-model.md` | Miro domain classifier + domain/subdomain map; Excel tab "Data Classification and Ownership" | Kitchen: custodian vs steward |
| Data catalog selection & rollout | `data-catalog.md` | Excel tabs "Data Catalog — Template for Comparing Systems" (object card, glossary, policy, risk, reporting, collaboration, relationships, automation, ops, time-to-value, integration, vendor viability, security); Miro catalog-requirements workshop | library.md → Knowledge Graph |
| DQ program / critical sources | `data-quality.md` | Excel tabs "Evaluation of DQ by Domains", "Register of Critical Sources", "Tracking DQ Issues" | DQMS concept map frame |
| Core certification | `certified-core-layer.md` | health-score approach from `bi-content-management.md` | Kimball, dbt best practices |
| Semantic / metric layer | `semantic-layer.md`, `semantic-metric-layer-v2.md` | metric-tree diagrams on the board | Spider 2.0, dbt SL vs text-to-SQL, OSI, Minerva |
| Domain knowledge base & context | `domain-knowledge-base.md`, `context-governance.md` | knowledge-pack structure (manifest / knowledge / eval) | Anthropic self-service analytics, context engineering |
| AI channel launch & evals | `llm-assistant-architecture.md` | loops A–E as the operating template | LangChain evals, Arize harness, clarify-before-answering |
| Content hygiene wave | `bi-content-management.md` | funnel frame (archive → certify → promote) | — |
| Skills & enablement | `skills-hub.md` | contribution flow + points scheme from the theme file | Agent Skills, MCP |
| Program tracking | `dg-program-roadmap.md` | Excel tabs "Track Status of DG Program", "Program Mgmt" | Program Map 3.0 frame |

Rule: a portfolio initiative without a playbook row is a red flag — either add the method or mark the initiative `[missing data]`.

---

## AUDIT — assess an existing strategy or program

Input: the user's strategy/roadmap/program doc, or an interview about the current program. Before scoring, run the mid-flow document invitation (universal convention) — pain analyses, landscape reviews and assessment exports often change scores by ±1. Score each dimension 0–2 (absent / partial / solid), citing evidence from their material and the KB file that defines "solid".

**Scoring nuance — the "declared but unfunded" flag.** The most common real state is not "partial": it is *described well and backed by nothing* — roles named without time, targets set without capacity, policies written without an owner. Do not average that into a 1 silently. Score the substance and attach the flag `[declared, not resourced]` to the dimension, then carry every flagged dimension into the gaps list: unfunded governance is the single most reliable predictor of program failure in this KB's field evidence. Half-points are allowed when they genuinely help (1.5 = solid design, weak execution) — but the flag matters more than the decimal.

| # | Audit dimension | KB yardstick |
|---|---|---|
| 1 | Entry justification: is DG needed at this scale, is there a business case? | `getting-started.md` (5-of-12 test, business-case template) |
| 2 | Diagnostic base: measured AS-IS maturity, not vibes | `maturity-and-metrics.md` (7 dimensions, DDI) |
| 3 | Dependency-chain integrity: built in order core → semantic → context; no AI-before-foundation inversions | `objects.yaml` triad + kill-gates |
| 4 | Stack-rank sanity: what gets frozen under budget cut; is governance capacity funded at all | field lesson: 20% core target delivered 2% without capacity (`certified-core-layer.md`) |
| 5 | Role model: owner / steward / custodian defined and enforced | `roles-and-operating-model.md`; Kitchen check: custodian works, steward alone fails (`dg-kitchen-research.md`) |
| 6 | Stream coverage: which of the 12 roadmap streams / Program Map 3.0 stages are missing | `dg-program-roadmap.md` |
| 7 | Metrics honesty: outcome metrics vs activity metrics; anti-metric check (no "N prompts per week") | `maturity-and-metrics.md`, `skills-hub.md` |
| 8 | Content hygiene: archive → certify → promote funnel exists | `bi-content-management.md` |
| 9 | Context invariants: SSOT referenced not copied; machine output enters as candidate; verified ≠ servable | `context-governance.md` |
| 10 | Risk register: fragile chain, Jevons/AI-slop multiplier, Gartner 80%-failure default, kill-gates written down | `certified-core-layer.md`, `context-governance.md` |

Output — **audit report**:
1. Scorecard table (10 × 0–2, total /20).
2. Top-5 gaps by severity, each with: evidence quote from the user's doc → KB yardstick → board deep-link.
3. Chain-break map: where their sequence violates the triad / kill-gates, and the resequenced order.
4. Quick wins (Common-Sense DG list from `getting-started.md`).
5. What to keep: explicitly name the strong parts — an audit that only criticizes gets ignored.
6. **Self-review before handing over** — run the CDO-judge stage against your own report: are the findings prioritized, is each one actionable, would the recipient know what to do on Monday? Drop findings that survive as "true but useless". Then run the bullshit pass on the report text, as on any written artifact.
7. Offer the HTML visualization of the report (universal convention).

---

## Guardrails

- **Deliverables are written in the user's language** (the KB is the source, not the output template); ask when it is ambiguous or the audience differs from the requester.
- No generic advice; every claim cites a KB file or participant data.
- No invented numbers; missing data → an explicit `[missing data]` marker naming the missing fact and its source, collected into a "what needs measuring" list — never a plausible substitute, never a vague phrase hiding the gap.
- **Nothing is finalized without both judges**: the CDO-judge loop (substance, up to three passes, visible rework log) and the bullshit pass (language, once, rewrites rather than critiques).
- **No over-optimism.** Targets are calibrated, not maximal; +1 level per year is the default; every target is discounted for dependency, capacity and adoption risk; what the strategy will not do is written down. A plan where everything succeeds is a plan nobody stress-tested — see "Setting a rational target maturity".
- Never write the full document before the Phase-2 scorecard (FORM) or the scorecard table (AUDIT) is confirmed.
- When challenged on "why so slow / why not just launch the agent" — answer with the numbers blocks (Spider 2.0 6%, 21%→95%+, 40%→85–95%, Gartner 80%).

## Installation

- **Claude Code**: copy or symlink **both** `skills/dg-strategy/` and `skills/dg-econ-effect/` into your project's `.claude/skills/` — the descriptions auto-trigger them. Section 06 of every FORM document is produced by `dg-econ-effect`; without it installed, FORM is missing a required section. Keep the whole repository cloned so relative KB paths resolve.
- **Any other agent**: paste this file *and* `skills/dg-econ-effect/SKILL.md` as instructions, and give the repository root as a knowledge source.
