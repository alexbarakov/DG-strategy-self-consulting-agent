---
type: plan
purpose: Build and operate the A+B evaluation harness for the dg-strategy and dg-econ-effect skills
status: phases 0-2 built and run (first loop B run rejected its candidate, as designed); phase 3 open; blind cross-model judging still owed
owner: aabarakov
---

# Evaluation harness — plan

Two loops, deliberately separated because they answer different questions.

**A — the deterministic loop** answers *did something break*. No model in it. Runs on every commit that touches the KB or the skills. Zero tolerance on blocking invariants: a violation is a red build, not a score.

**B — the comparison loop** answers *did the change make it better or worse*. A judge model compares a candidate answer against a frozen baseline answer, pairwise, without absolute scoring. Runs on demand — before merging a skill change, after a KB wave, when the model version moves.

Neither answers *is it any good*. That is loop C, deferred by decision.

---

## Phase 0 — make the set machine-addressable

Everything else depends on this, and none of it exists yet.

| Artefact | What it is |
|---|---|
| `70_golden_set/questions.jsonl` | One line per item: `id`, `company`, `tier`, `topic`, `question`, `expected_behaviour` (`answer` / `refuse` / `redirect`), `trap`, `cites[]` |
| `70_golden_set/keys.jsonl` | The reference answers, split out so a candidate run can be given questions without keys |
| `70_golden_set/index.json` | Reverse index: KB file → item ids that cite it. This is the rot detector |

**Built.** 100 items parsed, tiers exactly as designed (L1=25, L2=35, L3=25, L4=15), index covers 25 KB files.

`cites[]` is extracted from the existing `qa-*.md` files, not re-authored — every item already names its sources.

**Output of the phase:** the set stops being prose and becomes data. Effort: a few hours, mostly parsing.

---

## Phase 1 — loop A, the deterministic harness

Python 3, standard library only. No dependencies, no build step, consistent with everything else in this repository.

### A1. Citation validity — `evals/check_citations.py`

For every file reference in an output: the file exists at that path, and the claim attached to it is findable in that file. Fuzzy match on a normalised token overlap, threshold tuned so paraphrase passes and invention fails.

Reports: `valid` / `file missing` / `claim not found`. The third class is the interesting one — it catches an answer that cites a real file for something the file does not say, which is the most convincing kind of wrong.

### A2. Invariants — `evals/invariants.json` + `evals/check_invariants.py`

The core of loop A. Each invariant: `id`, `statement`, `severity` (`blocking` / `serious`), `detector`, `source` (the KB file that establishes it). JSON rather than YAML: the harness is standard-library only and Python ships no YAML parser.

**Built.** 19 invariants — 5 regex, 3 structural, 11 needing the classifier and reported as UNCHECKED on every run. A `--profile` switch was added that the plan did not anticipate: the file establishing a rule necessarily quotes what the rule forbids, so `skill` and `kb` profiles run structural checks only.

Starter set, to be completed in this phase. These are extracted from positions the KB already states, not invented:

| id | Invariant | Severity |
|---|---|---|
| `NUM-01` | No number tagged `vendor` or `disputed` in `51_numbers.md` is quoted as fact | blocking |
| `NUM-02` | No numeric target is stated where the baseline is unmeasured — it carries `[missing data]` instead | blocking |
| `ROI-01` | Operational efficiency, innovation and accelerated decision-making never appear as effect lines | blocking |
| `ROI-02` | No optimistic scenario is produced | blocking |
| `ROI-03` | An `expert estimate` figure never appears in the Summary as a headline number | blocking |
| `ROI-04` | Data quality never appears as its own ROI category | serious |
| `SEQ-01` | Reports are never certified before marts | blocking |
| `SEQ-02` | A catalog is never recommended before ownership works in ≥3 domains | blocking |
| `SEQ-03` | Self-service and agentic interfaces are never sequenced before trusted data | blocking |
| `ROLE-01` | No role is proposed without stated time and where that time is recorded | blocking |
| `ROLE-02` | A steward-only model is never recommended without the custodian alternative stated | serious |
| `MET-01` | At least one headline metric can legitimately fall; pure counters are labelled proxies | blocking |
| `MET-02` | Glossary term counts, steward counts and meeting counts never appear as success metrics | blocking |
| `BUR-01` | Every artefact proposed has a named reader and a decision that changes without it | serious |
| `BUR-02` | The strategy retires at least as many artefacts as it creates, or states the imbalance | serious |
| `GAP-01` | Where the KB has no material (MDM, privacy, retention, legacy, external suppliers), the answer says so rather than improvising | blocking |
| `LANG-01` | The deliverable is in the user's language; `[missing data]` is localised but always a visible bracketed flag | serious |
| `FMT-01` | Every deliverable exists in both HTML and Markdown | serious |

Detection: about half are regex or structural. `BUR-01`, `GAP-01` and `MET-01` need a small classifier call — kept as `llm` detectors but with a fixed prompt and a binary output, which is stable in a way that a 0–10 score is not.

### A3. Structure conformance — `evals/check_structure.py`

For FORM deliverables only: Summary present and first; no tables inside the Summary; sections 00–07 present and in order; streams inside 02 rather than standalone; section 06 present; exactly one chart, and it is AS-IS; every `[missing data]` marker collected into the closing list; appendices carry the portrait, the rework log and the KB-gap list.

### A4. Rot detection — `evals/check_rot.py`

Reads `index.json` and `git diff --name-only`. Any commit touching a KB file flags the items citing it as `needs-review`. Output is a list of item ids, not a failure — the set is stale, not wrong, and someone has to look.

### A5. Runner — `evals/run.py` and a pre-push hook

One command, human-readable report, non-zero exit on any `blocking` violation.

```bash
python3 evals/run.py --input <deliverable> --all
```

**Output of the phase:** breaking a KB position stops being invisible. Effort: one working session for the checkers, plus the invariant list, which is the part worth thinking about rather than typing.

---

## Phase 2 — loop B, pairwise comparison

### B1. Freeze the baseline

`70_golden_set/baseline/` — the 100 current answers, stored one per item, stamped with the KB commit hash and the model that produced them. This is what candidates are compared against. It is not "correct"; it is "what we had".

### B2. Candidate run protocol — `70_golden_set/RUN.md`

Give an agent the repository and `questions.jsonl` with keys stripped. Collect one answer per item. Record: model, skill version, KB commit, date. Nothing else is allowed to vary between runs — that is the whole discipline of the loop.

### B3. Judge — the protocol lives in `70_golden_set/RUN.md`

Given the question, the key, and two answers labelled A and B with the order randomised per item: pick the better one or declare a tie, plus one line of reason. **A different model than the one that produced the candidate.** No numeric score — the reason absolute scoring was dropped is that it drifts between model versions and makes "8.78 → 8.6" uninterpretable.

The judge's rubric collapses to one question: *which answer would a sceptical CDO rather have been handed?*

### B4. Report

Win / loss / tie against baseline, broken out by tier and by company, plus two refusal metrics:

- **False answer rate** — answered where the KB has no material (measured on the trap items)
- **False refusal rate** — refused where the KB does have material (measured on the near-traps from Phase 3)

Both are needed. The current set measures only the first, which pushes the skill toward cowardice over time.

**Run.** `run-002-terse` compared 2-3 sentence answers against the baseline's 4-6. Rejected on all four tiers, but the shape was the payload: 16 ties on L1 against 5 on L3 — compression is nearly free on definitions and expensive on judgement. See `runs/RESULTS.md`.

### B5. Promotion rule

A candidate becomes the new baseline when: zero blocking invariant violations, win rate ≥ loss rate on every tier (not just overall — a candidate that gains on L2 and collapses on L4 is a regression), and no increase in either refusal error. Otherwise the baseline stands and the change is investigated.

**Output of the phase:** skill changes stop being judged by whether the last output read well. Effort: half a session plus the token cost of each run.

---

## Phase 3 — close the holes `scores.md` already named

The current set is too easy in three specific ways, and the harness inherits every one of them.

| Gap | Fix | Size |
|---|---|---|
| No near-traps → over-refusal invisible | ~10 items that look unanswerable and are answerable, spread across the five companies | small |
| No multi-turn items | ~10 three-turn items where turn 3 tests consistency with turn 1 | medium |
| No "correct answer the sponsor does not want" items | ~5 items where the right move is to reject the premise and keep the room | medium, hardest to key |

This phase is content authoring, not engineering. It can lag Phases 1–2 without blocking them.

---

## Operating rules

| Question | Answer |
|---|---|
| When does A run | Every commit touching `10_*`, `11_*`, `12_*`, `5*`, `skills/` — and on every generated deliverable before it is shown to anyone |
| When does B run | Before merging a skill change; after a KB wave; when the model version moves. Not on a schedule — a scheduled eval nobody reads is the ceremony this KB's own judge would delete |
| What a red A build means | Stop. A blocking invariant violation is the skill contradicting its own base, which is worse than a bad answer |
| What a lost B run means | Investigate, do not revert automatically. Loss on L4 with gains elsewhere usually means the skill got more helpful and less honest |
| Who owns this | Named owner with recorded time, per the base's own `ROLE-01`. Currently `aabarakov`; if that is nominal, the harness is an artefact without a reader and `BUR-01` applies to it |
| TTL | The set is reviewed when `check_rot.py` flags more than 15 items, or every six months, whichever comes first |

---

## Two design decisions, taken

Recorded here so they are not re-argued each time the skill is edited.

**Where the opinion lives: in the knowledge base, not in the skill.** Four of the internal contradictions found in this repository were the skill and the base drifting apart on the same question. That class disappears by construction if a position is stated once. The cost — the skill is unusable without the repository cloned — is nominal, since every path in it is already relative. Consequence for future edits: a position added to the skill that also exists in a theme file is a defect, not a convenience.

**One skill or a family: a family, with the dependency declared.** `dg-strategy` and `dg-econ-effect` stay separate because the economic model is not DG-specific and will be reused. The price is a discovery and dependency problem, and it had already produced a live bug: FORM shipped a document missing its required section 06 whenever `dg-econ-effect` was not installed, silently. The rule now is that a missing dependency is stated in the deliverable, not worked around. A third skill would need a dispatcher; two do not.

## Pruning pass — what was removed after the first run

Applied the CDO judge's rationality dimension to the harness itself. Four things failed the reader test and are gone:

| Removed | Reason |
|---|---|
| Invariants `CORE-BUR-01`, `CORE-BUR-02` | duplicated dimension 8 of the CDO judge, which runs on every deliverable anyway |
| Pairwise judging of all 100 items | the automated metrics separate 65 of them on their own. Judging is escalation-only now; `check_completeness.py --needs-judging` produces the list |
| The holistic 0–10 rubric as a running metric | drifts between model versions, so a change in it cannot be read. Kept in `scores.md` as history, since its findings stand |
| A planned golden-set item type for cross-file contradictions | duplicated a cheaper method — seven real contradictions were found by reading files against each other, with no eval involved |

19 invariants → 17. 100 judgments per run → ~35. Two scoring systems → one. The harness now retires more than it adds, which is the test it applies to everything else.

**Do not re-add these without a reason that did not exist before.** Each was removed with its argument recorded; re-adding one silently is how a harness grows back into ceremony.

## Triage of the unchecked detectors

Nine of seventeen invariants printed UNCHECKED on every run — more than half the file not working. Triaged rather than wired wholesale:

| Invariant | Outcome |
|---|---|
| `DG-ROLE-01` — no role without recorded time | **mechanised** as `regex_require_if`: if roles are proposed anywhere, a time quantity must appear somewhere. Coarse — it cannot say *which* role lacks the hours — but it catches the document that names roles and never mentions time at all, which is the common case |
| `CORE-NUM-02` — no target on an unmeasured baseline | **mechanised** as structural: `check_structure.py` already enforces that gap markers exist and are collected |
| `DG-NAME-01` — does it go to business under the DG flag | **cut.** The CDO judge's naming corollary already makes this judgement on every deliverable |
| `DG-ROI-04` — data quality as its own ROI category | **cut.** Fires so rarely that an unchecked entry cost more attention than the risk it covered |

15 invariants, 10 enforced automatically (4 forbid, 2 require-if, 4 structural), 5 needing a classifier. Up from 8 of 19.

## What this deliberately does not measure

Whether the strategies are any good. Loop A measures self-consistency, loop B measures relative movement, and neither has external validity. The only thing that would is loop C — annotating real runs with what the user accepted, defended and shipped — and it was consciously deferred. Worth restating in whatever report this harness produces, so that a green build is never read as a claim about quality.

---

## Cross-product note

None of Phases 0–2 is DG-specific. Citation validity, an invariant list, rot detection and pairwise comparison against a frozen baseline are the same shape for any skill grounded in a knowledge source — the `ai-analyst` skills, SQL Copilot, the Redash reporting agent. Building it as `DG-strategy-self-consulting-agent/evals/` means it will be rebuilt three more times.

`[⚠️ Overlap: skill evaluation harness — DG-agent & ai-analyst & sql-copilot]`

The decision to make before Phase 1 starts: build it here and extract later, or build it generic from the start. Building generic first costs roughly a day more and needs a home repository that does not currently exist.
