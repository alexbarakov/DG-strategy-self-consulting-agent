---
type: eval
purpose: Loop B run log — one entry per candidate run
---

# Loop B — run log

## run-002-terse · 2026-08-29 · REJECTED

**Variable under test:** answer length. Candidate targets 2–3 sentences per item; baseline runs 4–6. Nothing else varied — same model, same KB commit `91ffff22`, same skill version.

**Why this variable.** A run where nothing changed measures only judge noise. Compression is a change worth actually considering — shorter answers are cheaper, faster to read and were the obvious response to the earlier finding that L1 scored low on actionability.

| tier | baseline | candidate | tie | verdict |
|---|---|---|---|---|
| L1 — definition | 7 | 2 | 16 | baseline |
| L2 — applied | 14 | 2 | 19 | baseline |
| L3 — hard | 19 | 1 | 5 | baseline |
| L4 — trap | 8 | 0 | 7 | baseline |
| **overall** | **48** | **5** | **47** | |

False answer rate 0/15 · false refusal rate 0/79 · loop A screen clean (96% citations valid, zero blocking invariants).

**Promotion: rejected.** The rule is win ≥ loss on every tier. The candidate lost all four.

### Correctness and completeness

The pairwise result says which answer was preferred. It does not say whether the loser was wrong. The claim-level measure does, and it changes the conclusion.

| | baseline | candidate | reading |
|---|---|---|---|
| Completeness — required claims | 97% | **96%** | inside the 3% measurement noise. Compression cost nothing essential |
| Enrichment retained | 84% | **33%** | two thirds of the supporting material gone |
| Correctness — no contradiction | 100% | **100%** | the candidate omits; it never contradicts |

Per tier, enrichment is where the whole pairwise result lives:

| tier | baseline enrichment | candidate enrichment | pairwise |
|---|---|---|---|
| L1 | 77% | 41% | 16 ties of 25 |
| L2 | 82% | 40% | 19 ties of 35 |
| L3 | 90% | **21%** | 5 ties of 25 |
| L4 | 89% | **28%** | 7 ties of 15 |

**The candidate lost without being wrong or incomplete.** Every required claim survived compression on every tier — L4 kept 100% of them. What it dropped was the enriching layer, and the drop is steepest exactly where the judge punished it hardest: L3 keeps a fifth of its enrichment and ties five times out of twenty-five.

That reframes the earlier conclusion. Compression is not a correctness risk and not a completeness risk. It is a **persuasion** risk: the enriching claims are the evidence — *chaos is survivable for two or three years*, *the one peer who actually measured*, *a large fintech cut its entire DG team* — and an answer without them states the right conclusion with nothing behind it. A reader who already trusts you loses nothing. A sceptical CDO loses the reason to agree.

So the length policy is keyed to audience rather than tier: an answer that must **inform** can be short; an answer that must **convince** carries its enrichment. That is a sharper rule than "L3 answers should be long", and it only became visible once the score was decomposed.

### What the shape says

The interesting result is not that the candidate lost — it is *where*.

- **L1: 16 ties out of 25.** Compression is nearly free on definitions. Two thirds of the time the terse answer is indistinguishable from the long one, and the candidate even won twice.
- **L3: 5 ties out of 25.** Compression is expensive on judgement. What the long answers carry is not padding — it is the counter-intuitive half: *chaos is survivable for two or three years*, *taking the budget creates a line item to cut*, *the one peer who actually measured*, *lost trust in an assistant is not recoverable*. Cut the second half of the answer and what survives is the recommendation without the reason a sceptic needs to accept it.
- **L4: zero candidate wins, seven ties.** A terse refusal is a worse refusal. Refusing without naming the replacement reads as dodging; the baseline's refusals win because they hand back something usable — the min-losses/max-costs structure instead of an ROI figure, the one-page list of objects that must not break instead of an architecture diagram.

The practical conclusion is a length policy per tier rather than per document: definitions can be short, judgement and refusals cannot. That is a change worth making to the skill, and it came out of a run whose candidate was rejected — which is the argument for running comparisons even when you expect the baseline to hold.

### What this run cannot claim

Candidate and baseline were produced by the same model, and the judge knew which was which. The protocol in `RUN.md` requires a different judge model and blind ordering, and neither was available here. Treat this as **a measurement of the cost of compression, not a validation of the harness's ability to detect quality differences between models.** The blind, cross-model version is still owed.

### Harness defects this run exposed

| Defect | Fix applied |
|---|---|
| `check_citations.py --run` crashed on the run header line | Header lines skipped |
| Refusal metrics derived by keyword reported 7/15 false answers where the true figure was 0/15 | Behaviour is now a judge-assigned field. A substantive "no, and here is why" is an answer, not a refusal, and no keyword list separates the two reliably |

The second one is the more useful finding: it is the same class of error as the invariant exemption that let a vendor number through — an automated check that looked like it was working and was not. Both were found by running the harness against real material rather than by reading it.
