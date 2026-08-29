#!/usr/bin/env python3
"""Forbidden-claim check — the hard rule of loop B.

Completeness asks whether the required claims are present. This asks the opposite
question: did the answer say something the KB explicitly refutes? The two are not
symmetric. An answer can cover every required claim and still be wrong, because it
also repeated the trap the item was built to catch — and completeness alone scores
that answer well.

  HARD RULE  — a confirmed forbidden probe that fires marks the item failed,
               whatever its completeness score and whatever a judge preferred.
               Ported from the companion repository's tier-2 golden set:
               https://github.com/alexbarakov/BI-strategy-self-consulting-agent

Probes live in `70_golden_set/forbidden.jsonl`, derived from the `trap` field of
each key. Two states, and the difference matters:

  confirmed: true   — reviewed by hand. Blocking.
  confirmed: false  — auto-derived from the trap text. Reported, never blocking,
                      because a false positive in a hard rule destroys the rule.

Matching is deliberately conservative, in three ways, because a false positive in
a hard rule destroys the rule:

  1. Every content word of the probe must appear, numerals included.
  2. They must appear inside ONE sentence. Words scattered across a paragraph are
     a topic match, not a claim.
  3. That sentence must not carry a refutation marker. An answer that names the
     trap in order to reject it is the behaviour we want, not the one we block —
     this check was written after the baseline tripped exactly that way.

False negatives are cheap here and false positives are not: a missed forbidden
claim costs one item, a wrongly blocked answer costs trust in the whole rule.

`numeric_forbidden` covers the items whose trap is "any number" — a refusal item
that answers with a percentage or a multiple has not refused.

Usage:
  python3 evals/check_forbidden.py --run 70_golden_set/runs/<run>.jsonl
  python3 evals/check_forbidden.py --run <run> --include-proposed
  python3 evals/check_forbidden.py --coverage
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
GS = os.path.join(ROOT, "70_golden_set")

MIN_WORD = 4
NUMERIC_RE = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)?\s*(?:%|x\b|×|times\b|per cent)", re.I)

# A sentence carrying any of these is discussing the trap, not committing it.
REFUTATION = (
    " no ", " not ", "n't", " never ", " rather than ", " instead of ", " avoid ",
    " wrong ", " myth", " warns", " trap", " fallacy", " cannot ", " isn ",
    " misleading", " do not ", " does not ", " would be ",
)


def content_words(text):
    """Alphabetic tokens of length >= MIN_WORD, plus every numeral — numerals carry
    the whole meaning of probes like '73% accuracy in production'."""
    low = text.lower()
    words = [w for w in re.findall(r"[a-z][a-z\-']+", low) if len(w) >= MIN_WORD]
    words += re.findall(r"\d+(?:[.,]\d+)?", low)
    return words


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?;])\s+|\n+", text) if s.strip()]


def refutes(sentence):
    padded = " " + sentence.lower().strip() + " "
    return any(marker in padded for marker in REFUTATION)


def fires(probe, answer):
    words = content_words(probe)
    if len(words) < 2:
        return False
    for sent in sentences(answer):
        low = sent.lower()
        if all(w in low for w in words) and not refutes(sent):
            return True
    return False


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", help="run file: {id, answer} per line")
    ap.add_argument("--include-proposed", action="store_true",
                    help="also report auto-derived probes (never blocking)")
    ap.add_argument("--coverage", action="store_true",
                    help="report how much of the set has hand-confirmed probes")
    args = ap.parse_args()

    forbidden = {r["id"]: r for r in load_jsonl(os.path.join(GS, "forbidden.jsonl"))}
    questions = {q["id"]: q for q in load_jsonl(os.path.join(GS, "questions.jsonl"))}

    if args.coverage:
        conf = [i for i, r in forbidden.items() if r.get("confirmed")]
        empty = [i for i, r in forbidden.items() if not r.get("probes")]
        print(f"forbidden probes: {len(forbidden)} items")
        print(f"  hand-confirmed (blocking): {len(conf)}")
        print(f"  auto-proposed (advisory):  {len(forbidden) - len(conf)}")
        if empty:
            print(f"  no probe derivable:        {len(empty)} -> {', '.join(sorted(empty))}")
        print("\nConfirming a probe is a review of the trap it came from; do it in batches per company.")
        return 0

    if not args.run:
        print(__doc__)
        return 2

    blocking, advisory = [], []
    for row in load_jsonl(args.run):
        rec = forbidden.get(row["id"])
        if not rec:
            continue
        answer = row.get("answer") or ""
        hits = [p for p in rec.get("probes", []) if fires(p, answer)]
        if rec.get("numeric_forbidden") and NUMERIC_RE.search(answer):
            hits.append("<any number> (refusal item answered with a figure)")
        if not hits:
            continue
        (blocking if rec.get("confirmed") else advisory).append((row["id"], hits))

    for label, rows in (("BLOCKING", blocking), ("advisory", advisory)):
        if not rows or (label == "advisory" and not args.include_proposed):
            continue
        print(f"\n{label} — forbidden claim present in the answer:")
        for qid, hits in rows:
            beh = questions.get(qid, {}).get("expected_behaviour", "?")
            print(f"  {qid} ({beh})")
            for h in hits:
                print(f"      {h}")

    total = len(load_jsonl(args.run))
    print(f"\nchecked {total} answers · {len(blocking)} blocked · {len(advisory)} advisory")
    if blocking:
        print("A blocked item is failed regardless of its completeness score. Do not send it to judging.")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
