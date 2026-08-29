#!/usr/bin/env python3
"""Correctness and completeness against the reference keys.

Neither is a holistic 0-10 score. Both decompose into units with a ground truth,
which is what makes them stable where a quality score is not:

  COMPLETENESS  — automated. The key is decomposed into atomic claims tagged
                  `required` (the answer is wrong without it) or `enriching`
                  (absence is a loss, not an error). Coverage is measured by
                  content-word overlap between the claim and the answer.

  CORRECTNESS   — judge-assigned, binary per item: does the answer contradict
                  the key or the KB? A binary judgment on a stated reference is
                  far more stable than a graded opinion.

The baseline scores ~1.0 on completeness by construction — the claims were
derived from it. The measure is meaningful for candidates, not for the reference.

Usage:
  python3 evals/check_completeness.py --run <run.jsonl>
  python3 evals/check_completeness.py --baseline
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.kb import GOLDEN, content_words, load_jsonl, normalise  # noqa: E402

COVERED, PARTIAL = 0.60, 0.35


def coverage(claim, answer_norm):
    words = content_words(claim)
    if not words:
        return 1.0
    return sum(1 for w in words if w in answer_norm) / len(words)


def classify(score):
    if score >= COVERED:
        return "covered"
    if score >= PARTIAL:
        return "partial"
    return "missing"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run")
    ap.add_argument("--baseline", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--needs-judging", action="store_true",
                    help="list only the items where the automated metrics cannot separate the "
                         "candidate from the baseline. Those are the only ones worth judging by hand.")
    args = ap.parse_args()

    claims = {c["id"]: c for c in load_jsonl(os.path.join(GOLDEN, "claims.jsonl"))}
    questions = {q["id"]: q for q in load_jsonl(os.path.join(GOLDEN, "questions.jsonl"))}

    if args.baseline:
        src = load_jsonl(os.path.join(GOLDEN, "baseline", "answers.jsonl"))
        label = "baseline"
        judgments = {}
    elif args.run:
        src = [r for r in load_jsonl(args.run) if "id" in r]
        label = os.path.basename(args.run)
        jpath = args.run.replace(".jsonl", ".judgments.jsonl")
        judgments = {j["id"]: j for j in load_jsonl(jpath)} if os.path.isfile(jpath) else {}
    else:
        ap.error("pass --run or --baseline")

    answers = {r["id"]: normalise(r["answer"]) for r in src}

    tiers = {}
    misses = []
    for qid, c in claims.items():
        tier = questions[qid]["tier"]
        t = tiers.setdefault(tier, {"req": 0, "req_cov": 0, "req_part": 0,
                                    "enr": 0, "enr_cov": 0, "items": 0, "contradicted": 0})
        t["items"] += 1
        ans = answers.get(qid, "")
        for cl in c["required"]:
            t["req"] += 1
            k = classify(coverage(cl, ans))
            if k == "covered":
                t["req_cov"] += 1
            elif k == "partial":
                t["req_part"] += 1
            else:
                misses.append((qid, tier, cl))
        for cl in c["enriching"]:
            t["enr"] += 1
            if classify(coverage(cl, ans)) == "covered":
                t["enr_cov"] += 1
        if judgments.get(qid, {}).get("contradicts_key"):
            t["contradicted"] += 1

    if args.needs_judging:
        base = {r["id"]: normalise(r["answer"])
                for r in load_jsonl(os.path.join(GOLDEN, "baseline", "answers.jsonl"))}
        need, skip = [], []
        for qid, c in claims.items():
            def score(a):
                req = c["required"]
                return sum(coverage(cl, a) >= COVERED for cl in req) / len(req) if req else 1.0
            cand_r, base_r = score(answers.get(qid, "")), score(base.get(qid, ""))
            enr = c["enriching"]
            cand_e = sum(coverage(cl, answers.get(qid, "")) >= COVERED for cl in enr) / len(enr) if enr else None
            base_e = sum(coverage(cl, base.get(qid, "")) >= COVERED for cl in enr) / len(enr) if enr else None
            separated = cand_r != base_r or (cand_e is not None and cand_e != base_e)
            (skip if separated else need).append(qid)
        print("=" * 74)
        print("ITEMS THAT STILL NEED A HUMAN OR MODEL JUDGE  —  %s" % label)
        print("=" * 74)
        print("  %d of %d items: the automated metrics already separate them, no judging needed"
              % (len(skip), len(claims)))
        print("  %d of %d items: metrics tie, preference is the only discriminator" % (len(need), len(claims)))
        print()
        for qid in sorted(need):
            print("    %s  %s" % (qid, questions[qid]["tier"]))
        print("=" * 74)
        return 0

    print("=" * 74)
    print("CORRECTNESS & COMPLETENESS  —  %s" % label)
    print("=" * 74)
    print("  %-6s %10s %12s %12s %14s" % ("tier", "required", "completeness", "enrichment", "contradictions"))
    tot = {"req": 0, "req_cov": 0, "req_part": 0, "enr": 0, "enr_cov": 0, "contradicted": 0, "items": 0}
    for tier in sorted(tiers):
        t = tiers[tier]
        for k in tot:
            tot[k] += t[k]
        comp = (t["req_cov"] + 0.5 * t["req_part"]) / t["req"] if t["req"] else 1.0
        e = t["enr_cov"] / t["enr"] if t["enr"] else 0
        print("  %-6s %10d %11.0f%% %11.0f%% %14s"
              % (tier, t["req"], 100 * comp, 100 * e,
                 "%d/%d" % (t["contradicted"], t["items"])))
    comp = (tot["req_cov"] + 0.5 * tot["req_part"]) / tot["req"]
    enr = tot["enr_cov"] / tot["enr"] if tot["enr"] else 0

    corr = 1 - tot["contradicted"] / tot["items"]
    print("  %-6s %10d %11.0f%% %11.0f%% %14s" % ("ALL", tot["req"], 100 * comp, 100 * enr,
                                                  "%d/%d" % (tot["contradicted"], tot["items"])))
    print()
    print("  completeness (required claims)   %.0f%%   partial credit 0.5 for partial coverage" % (100 * comp))
    print("  enrichment retained              %.0f%%   absence is a loss, not an error" % (100 * enr))
    print("  correctness (no contradiction)   %.0f%%   %s"
          % (100 * corr, "judge-assigned" if judgments else "NOT JUDGED — no judgments file"))
    print()

    if args.verbose and misses:
        print("  missing required claims (%d):" % len(misses))
        for qid, tier, cl in misses[:40]:
            print("    %-14s %s  %s" % (qid, tier, cl))
    print("=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
