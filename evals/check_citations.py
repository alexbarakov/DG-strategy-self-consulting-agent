#!/usr/bin/env python3
"""Loop A — citation validity.

For every KB file referenced in a text: does the file exist, and is the claim
attached to it findable in that file? The third outcome is the interesting one —
a real file cited for something it does not say is the most convincing kind of wrong.

Usage:
  python3 evals/check_citations.py --golden          # all 100 golden-set items
  python3 evals/check_citations.py --input <file>    # any document with `path.md` — claim lines
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.kb import (GOLDEN, Report, claim_overlap, is_meta_claim,  # noqa: E402
                    load_jsonl, read_kb_file)

PASS, WARN = 0.60, 0.35
PATH_RE = re.compile(r"`([\w./-]+\.(?:md|yaml|yml|json))`")
SPLIT_RE = re.compile(r";\s+")


def check_source_line(text, item_id, report, counters):
    """A source line is one or more `path` — claim segments separated by semicolons."""
    for segment in SPLIT_RE.split(text):
        paths = PATH_RE.findall(segment)
        if not paths:
            continue
        claim = PATH_RE.sub(" ", segment)
        claim = re.sub(r"^[\s—–-]+", "", claim).strip()
        for path in paths:
            counters["total"] += 1
            content = read_kb_file(path)
            if content is None:
                counters["missing"] += 1
                report.add("blocking", item_id, "file not found: %s" % path)
                continue
            if is_meta_claim(claim):
                counters["meta"] += 1
                report.add("info", item_id, "meta-claim, not scored — %s :: %s" % (path, claim[:60]))
                continue
            score = claim_overlap(claim, content)
            if score >= PASS:
                counters["ok"] += 1
            elif score >= WARN:
                counters["weak"] += 1
                report.add(
                    "serious",
                    item_id,
                    "weak match %.2f — %s :: %s" % (score, path, claim[:70]),
                )
            else:
                counters["bad"] += 1
                report.add(
                    "blocking",
                    item_id,
                    "claim not found %.2f — %s :: %s" % (score, path, claim[:70]),
                )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--golden", action="store_true")
    ap.add_argument("--input")
    args = ap.parse_args()

    report = Report("CITATIONS")
    counters = {"total": 0, "ok": 0, "weak": 0, "bad": 0, "missing": 0, "meta": 0}

    if args.golden:
        keys = load_jsonl(os.path.join(GOLDEN, "keys.jsonl"))
        for k in keys:
            check_source_line(k["source_text"], k["id"], report, counters)
    elif args.input:
        with open(args.input, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                if PATH_RE.search(line):
                    check_source_line(line, "line %d" % n, report, counters)
    else:
        ap.error("pass --golden or --input")

    print(report.render())
    t = counters["total"] or 1
    print(
        "\n  %d citations: %d ok (%.0f%%), %d weak, %d not found, %d missing file, %d meta"
        % (counters["total"], counters["ok"], 100.0 * counters["ok"] / t,
           counters["weak"], counters["bad"], counters["missing"], counters["meta"])
    )
    return 1 if report.blocking else 0


if __name__ == "__main__":
    sys.exit(main())
