#!/usr/bin/env python3
"""Phase 0 — turn the golden set from prose into data.

Reads 70_golden_set/qa-*.md and emits:
  questions.jsonl  one line per item, keys stripped — this is what a candidate run gets
  keys.jsonl       the reference answers, sources and traps
  index.json       reverse index: KB file -> item ids citing it (the rot detector)

Usage:  python3 evals/build_index.py [--check]
"""

import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.kb import GOLDEN, KB_ROOT, dump_jsonl  # noqa: E402

ITEM_RE = re.compile(
    r"^### (?P<num>\d+)\. (?P<question>.+?) (?P<tags>(?:`[^`]+`\s*)+)$", re.M
)
TAG_RE = re.compile(r"`([^`]+)`")
FIELD_RE = re.compile(r"^\*\*(Answer|Source|Trap)\.\*\*\s*(.*)$", re.M | re.S)
PATH_RE = re.compile(r"`([\w./-]+\.(?:md|yaml|yml|json))`")

COMPANY_RE = re.compile(r"qa-(\d+)-(\w+)\.md$")


def split_fields(block):
    """Split an item body into Answer / Source / Trap."""
    out = {}
    parts = re.split(r"^\*\*(Answer|Source|Trap)\.\*\*", block, flags=re.M)
    # parts = ['', 'Answer', ' text', 'Source', ' text', ...]
    for i in range(1, len(parts) - 1, 2):
        out[parts[i].lower()] = parts[i + 1].strip()
    return out


def expected_behaviour(tags):
    if "trap" in tags:
        return "refuse_or_redirect"
    if "gap" in tags:
        return "declare_gap"
    return "answer"


def parse_file(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    m = COMPANY_RE.search(path)
    order, company = m.group(1), m.group(2)

    matches = list(ITEM_RE.finditer(text))
    items = []
    for i, mt in enumerate(matches):
        start = mt.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        fields = split_fields(body)

        tags = TAG_RE.findall(mt.group("tags"))
        tiers = [t for t in tags if re.fullmatch(r"L[1-4]", t)]
        topics = [t for t in tags if t not in tiers]

        source_text = fields.get("source", "")
        cites = sorted(set(PATH_RE.findall(source_text)))

        items.append(
            {
                "id": "%s-%02d" % (company, int(mt.group("num"))),
                "company": company,
                "order": int(order),
                "num": int(mt.group("num")),
                "tier": tiers[0] if tiers else "L?",
                "topics": topics,
                "question": mt.group("question").strip(),
                "expected_behaviour": expected_behaviour(topics),
                "answer": fields.get("answer", "").strip(),
                "source_text": source_text.strip(),
                "cites": cites,
                "trap": fields.get("trap", "").strip(),
            }
        )
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate only, write nothing")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(GOLDEN, "qa-*.md")))
    items = []
    for f in files:
        items.extend(parse_file(f))

    problems = []
    if len(items) != 100:
        problems.append("expected 100 items, parsed %d" % len(items))
    for it in items:
        if it["tier"] == "L?":
            problems.append("%s has no tier tag" % it["id"])
        for field in ("question", "answer", "source_text", "trap"):
            if not it[field]:
                problems.append("%s missing %s" % (it["id"], field))
        if not it["cites"]:
            problems.append("%s cites no file" % it["id"])

    tiers = {}
    for it in items:
        tiers[it["tier"]] = tiers.get(it["tier"], 0) + 1

    print("parsed %d items from %d files" % (len(items), len(files)))
    print("tiers:", ", ".join("%s=%d" % kv for kv in sorted(tiers.items())))
    if problems:
        print("\nPROBLEMS (%d):" % len(problems))
        for p in problems[:20]:
            print("  " + p)
        return 1
    print("structure ok")

    if args.check:
        return 0

    dump_jsonl(
        os.path.join(GOLDEN, "questions.jsonl"),
        [
            {k: it[k] for k in ("id", "company", "tier", "topics", "question", "expected_behaviour")}
            for it in items
        ],
    )
    dump_jsonl(
        os.path.join(GOLDEN, "keys.jsonl"),
        [
            {k: it[k] for k in ("id", "answer", "source_text", "cites", "trap", "expected_behaviour")}
            for it in items
        ],
    )

    index = {}
    for it in items:
        for c in it["cites"]:
            index.setdefault(c, []).append(it["id"])
    for c in index:
        index[c].sort()
    with open(os.path.join(GOLDEN, "index.json"), "w", encoding="utf-8") as fh:
        json.dump(
            {"kb_root": os.path.basename(KB_ROOT), "items": len(items), "by_file": index},
            fh,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )

    print("wrote questions.jsonl, keys.jsonl, index.json")
    print("index covers %d KB files" % len(index))
    return 0


if __name__ == "__main__":
    sys.exit(main())
