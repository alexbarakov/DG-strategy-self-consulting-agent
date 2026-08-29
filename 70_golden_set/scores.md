---
type: eval
purpose: Independent judge scores for the 100 golden-set answers, and what the scores say about the KB
baseline: 8.78 / 10 average
---

# Judge results

Scored against the rubric in `README.md`: grounding /3, correctness /3, actionability /2, honesty /2. The judge had the answers and the KB, not the reasoning that produced them.

**A note on how to read this.** The average is not the point. Nine items scored 7 or below, and in eight of those cases the answer was as good as the base allows — the score is a measurement of the knowledge base, not of the answering. Those nine are listed at the bottom and five of them already have entries in `60_roadmap.md`; three did not, and have been added.

---

## Summary

| Company | Items | Total | Average | Lowest item |
|---|---|---|---|---|
| Nordwind Logistics | 20 | 181 | **9.05** | Q9 — bus factor (7) |
| Verdant Retail | 20 | 179 | **8.95** | Q5 — health score (7) |
| Kestrel Games | 20 | 177 | **8.85** | Q4 — loops A–E (6) |
| Meridian Bank | 20 | 173 | **8.65** | Q19 — privacy & retention (6) |
| Helios Energy | 20 | 168 | **8.40** | Q10 / Q15 — legacy, accountability (6) |
| **All** | **100** | **878** | **8.78** | |

The ordering is the finding. The base scores highest on the company it was written for — a mid-maturity organisation deciding whether to start — and lowest on the company furthest from its assumptions. Helios loses 0.65 against Nordwind not because its questions are harder but because five of its twenty land in documented gaps.

## By difficulty tier

| Tier | Items | Average | Reading |
|---|---|---|---|
| L1 — definition | 25 | **8.36** | The weakest tier, and the surprise of this run |
| L2 — applied | 35 | **8.86** | |
| L3 — hard | 25 | **9.08** | The strongest tier |
| L4 — trap | 15 | **8.80** | Refusals held: no item produced its trap answer |

**L1 scoring below L3 is the single most useful result here.** It is partly structural — a definition earns at most 1 of 2 on actionability — but not only. Four of the five lowest L1 scores are AI-era objects whose files are stubs: loops A–E (6), the Data-Driven Index (7), health score versus DQ score (7), data literacy (8). The base reasons better than it defines. An agent grounded in it will give excellent judgement on a hard sequencing question and a vague answer to "what is X", which is the opposite of the usual failure mode and worth knowing before anyone builds a chatbot on top of it.

**No trap was taken.** All fifteen L4 items produced a refusal, a scope limit or a redirect rather than the plausible wrong answer — no ROI figure, no vendor name, no invented benchmark, no privacy policy, no MDM architecture. That is the behaviour the `[missing data]` convention and `51_numbers.md` exist to produce, and it is the clearest evidence in this run that the conventions work.

## Per-criterion

| Criterion | Max | Average | Note |
|---|---|---|---|
| Grounding | 3 | **2.66** | Loses points only where the source file is thin or absent |
| Correctness | 3 | **2.92** | Two items scored 2: both extrapolated beyond what the file supports |
| Actionability | 2 | **1.62** | Definitions and refusals cap this by construction |
| Honesty | 2 | **1.58** | High where gaps exist, low where there was nothing to flag |

Honesty averaging below actionability is expected and healthy: an answer with nothing to disclose should not be rewarded for disclosing nothing. The metric matters only on the items where a limit existed — and on those, it scored 2.0 in every case.

---

## The nine items at or below 7

| Item | Score | Why | Roadmap entry |
|---|---|---|---|
| Kestrel Q4 — what are loops A–E | 6 | `llm-assistant-architecture.md` is ~1k words; the answer could name the loops and their purpose but not describe them | **C2** (existing) |
| Helios Q10 — governing a legacy estate | 6 | No material. The base assumes a platform you can change | **B4** (existing) |
| Helios Q15 — accountability where nobody can be fired | 6 | The base's accountability model assumes objectives, calibration and possible consequence. Peer visibility was the only transferable mechanism | **NEW — A6** |
| Meridian Q19 — privacy, classification, retention | 6 | ~13 incidental mentions, no material; retention exists only as content hygiene | **B2 / B3** (existing) |
| Meridian Q10 — single customer view | 7 | Failure patterns only, no method | **B1** (existing) |
| Helios Q19 — external data suppliers | 7 | Contracts described for internal flows only | **B5** (existing) |
| Helios Q5 — the Data-Driven Index | 7 | The DDI scoring grid is one of four frames that resisted machine extraction | **C3** (existing) |
| Verdant Q5 — health score vs DQ score | 7 | The distinction is asserted in two files and defined in neither | **NEW — A7** |
| Nordwind Q9 — key-person risk | 7 | Bus factor is visible everywhere in the field evidence and named nowhere as a governance object | **NEW — A8** |

Three gaps were found that `60_roadmap.md` did not have. All three are cheap Wave-A items — framing rather than subject matter — and have been added to that file.

---

## What to do with this set

- **As a regression detector.** Re-run after any substantive KB edit. A drop concentrated in one company points at a file; a drop spread evenly points at the conventions.
- **As a gap finder.** The nine low scores above are the KB's own to-do list, ranked by how badly they bit. That is the same mechanism that produced `60_roadmap.md` from the Alverta run, applied at five times the surface area.
- **Not as a leaderboard.** The set was written by the same process it scores. A model that beats 8.78 has matched this process, not exceeded it — and a model that scores 10 has probably been given the answers.

## Next run should be harder

Three ways this set is too easy, to fix before it is used as a benchmark:

1. **No multi-turn items.** Every question is answerable in one pass. The failure mode in real use is the third follow-up, where an agent contradicts its own second answer.
2. **No cross-file contradiction probes.** This session found six internal contradictions in the skills and one in the themes by reading them against each other. No golden-set item does that. Questions of the form "file A says X and file B says Y — which holds?" would score far lower.
3. **No questions with a correct answer the asker does not want.** The L4 traps refuse a request; none of them tells a sponsor that their premise is wrong and then keeps the room. That is the actual hard skill and it is untested here.
