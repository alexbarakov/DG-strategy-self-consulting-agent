#!/usr/bin/env python3
"""Loop B — tabulate a judged run against the baseline.

Usage:  python3 evals/report_run.py --run 70_golden_set/runs/<run>.jsonl
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.kb import GOLDEN, load_jsonl  # noqa: E402

TIERS = ["L1", "L2", "L3", "L4"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    args = ap.parse_args()

    rows = load_jsonl(args.run)
    header = rows[0] if "run_id" in rows[0] else {}
    answers = {r["id"]: r for r in rows if "id" in r}
    judgments = {j["id"]: j for j in load_jsonl(args.run.replace(".jsonl", ".judgments.jsonl"))}
    questions = {q["id"]: q for q in load_jsonl(os.path.join(GOLDEN, "questions.jsonl"))}

    tally = {t: {"baseline": 0, "candidate": 0, "tie": 0} for t in TIERS}
    for qid, q in questions.items():
        w = judgments.get(qid, {}).get("winner")
        if not w:
            continue
        tally[q["tier"]][w] += 1

    # refusal errors — behaviour is judge-assigned. Keyword detection was tried and
    # dropped: a substantive "no, and here is why" is an answer, not a refusal, and no
    # keyword list separates the two reliably.
    false_answer = false_refusal = n_trap = n_answerable = 0
    unlabelled = 0
    for qid, q in questions.items():
        got = judgments.get(qid, {}).get("behaviour")
        if got is None:
            unlabelled += 1
            continue
        if q["expected_behaviour"] == "refuse_or_redirect":
            n_trap += 1
            if got == "answered":
                false_answer += 1
        elif q["expected_behaviour"] == "answer":
            n_answerable += 1
            if got == "refused_or_redirected":
                false_refusal += 1

    print("=" * 66)
    print("LOOP B  %s  vs baseline" % header.get("run_id", os.path.basename(args.run)))
    print("=" * 66)
    if header:
        print("  changed: %s" % header.get("changed", "?"))
        print("  limitation: %s" % header.get("limitation", "—"))
    print()
    print("  %-8s %8s %10s %6s   %s" % ("tier", "baseline", "candidate", "tie", "verdict"))
    total = {"baseline": 0, "candidate": 0, "tie": 0}
    ok = True
    for t in TIERS:
        d = tally[t]
        for k in total:
            total[k] += d[k]
        v = "candidate ≥" if d["candidate"] >= d["baseline"] else "BASELINE WINS"
        if d["candidate"] < d["baseline"]:
            ok = False
        print("  %-8s %8d %10d %6d   %s" % (t, d["baseline"], d["candidate"], d["tie"], v))
    print("  %-8s %8d %10d %6d" % ("overall", total["baseline"], total["candidate"], total["tie"]))
    print()
    print("  false answer rate   %d/%d   (answered where a refusal was expected)" % (false_answer, n_trap))
    if unlabelled:
        print("  %d item(s) unlabelled by the judge — refusal metrics incomplete" % unlabelled)
    print("  false refusal rate  %d/%d   (refused where an answer was available)" % (false_refusal, n_answerable))
    print()
    print("  PROMOTION: %s" % ("candidate replaces baseline" if ok else
                               "REJECTED — the rule is win >= loss on every tier, not overall"))
    print("=" * 66)
    return 0


if __name__ == "__main__":
    sys.exit(main())
