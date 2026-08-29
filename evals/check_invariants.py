#!/usr/bin/env python3
"""Loop A — invariant checks.

Runs the regex detectors from invariants.json against a deliverable and reports
llm detectors as UNCHECKED rather than silently passing them.

Usage:  python3 evals/check_invariants.py --input <file> [--pack core,dg]
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.kb import EVALS, Report  # noqa: E402

TAG_STRIP = re.compile(r"<[^>]+>")


def load_invariants():
    with open(os.path.join(EVALS, "invariants.json"), encoding="utf-8") as fh:
        return json.load(fh)


def text_lines(path):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    if path.endswith(".html"):
        raw = TAG_STRIP.sub(" ", raw)
    return [ln for ln in (l.strip() for l in raw.splitlines()) if ln]


def check_forbid(inv, lines, report):
    pats = [re.compile(p, re.I) for p in inv["patterns"]]
    unless = [u.lower() for u in inv.get("unless", [])]
    for n, line in enumerate(lines, 1):
        low = line.lower()
        for p in pats:
            if p.search(line):
                if any(u in low for u in unless):
                    break
                report.add(
                    inv["severity"],
                    inv["id"],
                    "line %d: %s" % (n, line[:110]),
                )
                break


def check_require_if(inv, lines, report):
    blob = "\n".join(lines).lower()
    if not any(re.search(c, blob, re.I) for c in inv["condition"]):
        return
    if not any(re.search(r, blob, re.I) for r in inv["require"]):
        report.add(
            inv["severity"],
            inv["id"],
            "condition present, required counterpart absent",
        )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--pack", default="core,dg")
    ap.add_argument("--profile", default="deliverable",
                    choices=["deliverable", "skill", "kb"],
                    help="skill and kb profiles skip content forbids: those files are the source of the rules, not subjects of them")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    data = load_invariants()
    packs = [p.strip() for p in args.pack.split(",")]
    lines = text_lines(args.input)

    allowed = set(data.get("profiles", {}).get(args.profile, {}).get(
        "detectors", ["regex_forbid", "regex_require_if", "structural", "llm"]))

    report = Report("INVARIANTS  %s  [%s]" % (os.path.basename(args.input), args.profile))
    unchecked, structural = [], []

    for pack in packs:
        for inv in data["packs"].get(pack, []):
            det = inv["detector"]
            if det not in allowed:
                continue
            if det == "regex_forbid":
                check_forbid(inv, lines, report)
            elif det == "regex_require_if":
                check_require_if(inv, lines, report)
            elif det == "llm":
                unchecked.append(inv["id"])
            elif det == "structural":
                structural.append(inv["id"])

    if unchecked:
        report.add("info", "UNCHECKED", "needs classifier: " + ", ".join(unchecked))
    if structural:
        report.add("info", "DELEGATED", "check_structure.py: " + ", ".join(structural))

    if args.json:
        print(json.dumps(report.findings, ensure_ascii=False, indent=2))
    else:
        print(report.render())
    return 1 if report.blocking else 0


if __name__ == "__main__":
    sys.exit(main())
