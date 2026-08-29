---
type: eval
purpose: Protocol for producing a candidate run and judging it against the frozen baseline (loop B)
---

# Loop B — candidate run and pairwise judging

Loop A asks *did something break*. Loop B asks *did this change make it better or worse*. It never produces an absolute score, because absolute scores from a model judge drift between versions and make "8.78 → 8.6" uninterpretable.

## 1. Produce the candidate

Give the agent the repository and `questions.jsonl` **with keys stripped** — `questions.jsonl` already contains no answers, which is why it is a separate file from `keys.jsonl`. One answer per item, same format as the baseline.

Record the run header, and vary exactly one thing between runs. That discipline is the whole loop:

```json
{"run_id": "...", "date": "...", "model": "...", "skill_version": "...", "kb_commit": "...", "changed": "what is different from the previous run"}
```

Write results to `70_golden_set/runs/<run_id>.jsonl`, one line per item: `{"id": ..., "answer": ...}`.

## 2. Screen with loop A first

```bash
python3 evals/run.py --golden
```

A candidate with a blocking invariant violation does not proceed to judging. A better-written answer that contradicts the base is not a better answer, and letting the judge weigh the two against each other is how that gets lost.

## 2a. Apply the forbidden-claim hard rule

```bash
python3 evals/check_forbidden.py --run 70_golden_set/runs/<run>.jsonl
```

Completeness asks whether the required claims are there. This asks whether the answer said something the base explicitly refutes — the `trap` field of each key, turned into machine-checkable probes in `forbidden.jsonl`.

The two questions are not symmetric, and that is the whole point: **an answer can cover every required claim and still repeat the trap the item was built to catch.** Completeness scores that answer well. A blocked item is failed regardless of its completeness score and does not go to judging.

Only hand-confirmed probes block. Auto-derived ones are reported with `--include-proposed` and never block, because a false positive in a hard rule destroys the rule. `--coverage` shows how much of the set has been confirmed.

The matcher is deliberately strict: every content word of the probe, numerals included, inside one sentence, and that sentence must not carry a refutation marker. The last condition exists because the frozen baseline tripped without it — it names traps in order to reject them, which is the behaviour the set wants.

Ported from the companion repository's tier-2 golden set: https://github.com/alexbarakov/bi-ai-strategy-builder

## 3. Measure first, judge only what is left

Run the automated metrics before any judging:

```bash
python3 evals/check_completeness.py --run 70_golden_set/runs/<run>.jsonl
python3 evals/check_completeness.py --run 70_golden_set/runs/<run>.jsonl --needs-judging
```

Required-claim completeness and the contradiction check separate most items on their own. **Judge by hand only the items the metrics tie on** — there, preference is the only discriminator left, and that is what a judge is for.

On `run-002-terse` this rule would have cut judging from 100 items to 35. The first run judged all hundred and reached a conclusion the automated enrichment metric had already produced, more precisely and for free. That is the pruning this protocol now encodes.

## 4. Judge pairwise — on the tied items only

Use a **different model** than the one that produced the candidate. For each item, present:

- the question and its `expected_behaviour` (`answer` / `refuse_or_redirect` / `declare_gap`)
- the trap
- two answers labelled **A** and **B**, **order randomised per item**, with no indication of which is the baseline

The judge's whole rubric is one question:

> Which of these would a sceptical CDO rather have been handed — one who will be asked by the CFO why this costs that much, by the verticals why they should do your work, and by their own engineers why they are filling in another form?

Output per item: `A` / `B` / `tie`, plus one line of reason. No numbers.

Two hard rules for the judge:

- An answer that produces the item's trap loses regardless of how well it reads.
- An answer that refuses where `expected_behaviour` is `answer` loses. Over-refusal is a failure mode, not caution — this is the half the original set did not measure.

## 5. Report

```
run_id vs baseline <commit>
              win   loss   tie
L1              -      -     -
L2              -      -     -
L3              -      -     -
L4              -      -     -
overall         -      -     -

false answer rate   n/15 trap items answered substantively
false refusal rate  n/85 answerable items refused
```

Report by tier, not only overall. A candidate that gains on L2 and collapses on L4 has become more helpful and less honest, and the overall number hides exactly that.

## 6. Promotion

A candidate replaces the baseline only when **all** of:

- zero blocking invariant violations
- win ≥ loss on **every** tier, not merely overall
- neither refusal error rate increased

Otherwise the baseline stands and the change gets investigated. Losing a run is information; overwriting the baseline to make the number go up is how an eval stops meaning anything.

## What this cannot tell you

Whether the answers are any good in the world. Loop B measures movement against a frozen artefact produced by the same process that wrote the questions. A candidate that beats the baseline has matched or exceeded that process — not reality. External validity would need loop C, annotating real runs with what the user accepted, defended and shipped, and that was deliberately deferred.
