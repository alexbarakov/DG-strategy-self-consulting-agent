#!/usr/bin/env python3
"""Loop A runner. One command, one report, non-zero exit on any blocking finding.

  python3 evals/run.py --input <deliverable>        # check one document
  python3 evals/run.py --golden                     # citation validity across the golden set
  python3 evals/run.py --run <candidate.jsonl>      # forbidden-claim hard rule on a candidate run
  python3 evals/run.py --all --since HEAD~1         # everything, including rot

Loop B (pairwise comparison against the frozen baseline) is not run from here:
it needs a model and a judge, and mixing it in would let a deterministic red build
be masked by a good comparison result.
"""

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def run(script, *argv):
    cmd = [sys.executable, os.path.join(HERE, script)] + list(argv)
    return subprocess.call(cmd)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="a deliverable to check")
    ap.add_argument("--profile", default="deliverable", choices=["deliverable", "skill", "kb"])
    ap.add_argument("--golden", action="store_true", help="citation validity across the golden set")
    ap.add_argument("--run", help="candidate run file: apply the forbidden-claim hard rule before judging")
    ap.add_argument("--since", help="git ref for rot detection")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    if not any([args.input, args.golden, args.since, args.all, args.run]):
        ap.error("nothing to do — pass --input, --golden, --run, --since or --all")

    codes = []

    if args.input:
        codes.append(run("check_invariants.py", "--input", args.input, "--profile", args.profile))
        if args.profile == "deliverable":
            codes.append(run("check_structure.py", "--input", args.input))
        codes.append(run("check_citations.py", "--input", args.input))

    if args.golden or args.all:
        codes.append(run("build_index.py", "--check"))
        codes.append(run("check_citations.py", "--golden"))
        codes.append(run("check_rot.py", "--orphans"))

    if args.run:
        codes.append(run("check_forbidden.py", "--run", args.run))

    if args.since:
        codes.append(run("check_rot.py", "--since", args.since))

    failed = sum(1 for c in codes if c != 0)
    print("\n" + "=" * 72)
    if failed:
        print("LOOP A: FAILED — %d of %d checks reported blocking findings" % (failed, len(codes)))
        print("A blocking finding is the skill contradicting its own base. Stop and fix.")
    else:
        print("LOOP A: PASS — %d checks, no blocking findings" % len(codes))
        print("This says the output is self-consistent. It says nothing about whether it is any good.")
    print("=" * 72)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
