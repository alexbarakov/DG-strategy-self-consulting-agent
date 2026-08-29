#!/usr/bin/env python3
"""Loop A — structure conformance for a FORM strategy deliverable.

Covers the structural invariants: CORE-LANG-01, CORE-FMT-01, DG-ROI-03,
plus the document template from skills/dg-strategy/SKILL.md.

Usage:  python3 evals/check_structure.py --input <deliverable.md|.html>
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.kb import Report  # noqa: E402

SECTIONS = [
    ("00", r"контекст|context"),
    ("01", r"as-is"),
    ("02", r"to-be"),
    ("03", r"метрик|metrics"),
    ("04", r"портфел|portfolio"),
    ("05", r"операционн|operating"),
    ("06", r"эффект|effect"),
    ("07", r"риск|risk"),
]
GAP_MARKER = re.compile(r"\[(?:не хватает данных|missing data|requires clarification)[^\]]*\]", re.I)
MONEY = re.compile(r"[\d\s]{2,}(?:млн|млрд|тыс|m\b|bn\b|k\b|руб|₽|\$|€)|\b\d+[.,]\d+\s*[x×]", re.I)


def load(path):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    if path.endswith(".html"):
        heads = [(int(m.group(1)), re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(2))).strip())
                 for m in re.finditer(r"<h([1-3])[^>]*>(.*?)</h\1>", raw, re.S)]
        body = re.sub(r"<[^>]+>", " ", raw)
        tables = raw.count("<table")
        charts = raw.count("<svg")
    else:
        heads = [(len(m.group(1)), m.group(2).strip())
                 for m in re.finditer(r"^(#{1,3}) (.+)$", raw, re.M)]
        body = raw
        tables = len(re.findall(r"^\|.+\|$", raw, re.M))
        charts = len(re.findall(r"█", raw))
        charts = 1 if charts else 0
    return raw, heads, body, tables, charts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    args = ap.parse_args()
    path = args.input
    raw, heads, body, tables, charts = load(path)
    rep = Report("STRUCTURE  %s" % os.path.basename(path))

    tops = [(lvl, t) for lvl, t in heads if lvl <= 2]
    titles = [t.lower() for _, t in tops]

    # Summary opens the document
    sum_idx = next((i for i, t in enumerate(titles) if "summary" in t), None)
    if sum_idx is None:
        rep.add("blocking", "STR-SUMMARY", "no Summary section")
    else:
        first_section = next((i for i, t in enumerate(titles) if re.search(r"\b00\b", t)), None)
        if first_section is not None and sum_idx > first_section:
            rep.add("blocking", "STR-SUMMARY", "Summary does not open the document")

    # sections present and in order
    positions = []
    for num, pat in SECTIONS:
        idx = next((i for i, t in enumerate(titles)
                    if re.search(r"\b%s\b" % num, t) and re.search(pat, t)), None)
        if idx is None:
            rep.add("blocking", "STR-SECTIONS", "section %s missing" % num)
        else:
            positions.append((num, idx))
    if positions != sorted(positions, key=lambda p: p[1]):
        rep.add("blocking", "STR-SECTIONS", "sections out of order: %s"
                % ", ".join(n for n, _ in positions))

    # streams belong inside 02, not as their own top-level section
    if any(re.search(r"\b03\b", t) and re.search(r"стрим|stream", t) for t in titles):
        rep.add("blocking", "STR-STREAMS", "streams appear as a standalone section, not inside TO-BE")

    # no tables inside the Summary  (Summary is prose and bullets only)
    if sum_idx is not None:
        # the Summary block runs to section 00, not to the next sub-heading:
        # its own sub-headings (Vision, Problems, Goals) are part of it
        start = raw.find(tops[sum_idx][1])
        sec00 = next((t for _, t in tops if re.search(r"\b00\b", t.lower())), None)
        end = raw.find(sec00, start) if sec00 else len(raw)
        if end == -1:
            end = len(raw)
        chunk = raw[start:end]
        n = chunk.count("<table") if path.endswith(".html") else len(re.findall(r"^\|.+\|$", chunk, re.M))
        if n:
            rep.add("blocking", "STR-SUMMARY-TABLES", "%d table(s) inside the Summary" % n)
        # DG-ROI-03: no headline money figure in the Summary
        if MONEY.search(re.sub(r"<[^>]+>", " ", chunk)):
            rep.add("blocking", "DG-ROI-03",
                    "a money-shaped figure appears in the Summary; only a `calculated` number may")

    # exactly one chart
    if charts == 0:
        rep.add("serious", "STR-CHART", "no AS-IS chart found")
    elif charts > 1:
        rep.add("blocking", "STR-CHART", "%d charts; the template allows one (AS-IS)" % charts)

    # CORE-LANG-01 — gap markers are visible and collected
    markers = GAP_MARKER.findall(body)
    if markers:
        if not re.search(r"что нужно измерить|what needs measuring|что измерить|precision list", body, re.I):
            rep.add("serious", "CORE-LANG-01",
                    "%d gap markers but no closing 'what needs measuring' list" % len(markers))
    else:
        rep.add("serious", "CORE-LANG-01", "no gap markers at all — suspicious for a real diagnosis")

    # CORE-FMT-01 — both formats exist
    sibling = path[:-5] + ".md" if path.endswith(".html") else path[:-3] + ".html"
    if not os.path.isfile(sibling):
        rep.add("serious", "CORE-FMT-01", "sibling format missing: %s" % os.path.basename(sibling))

    print(rep.render())
    print("\n  %d headings, %d tables, %d chart(s), %d gap markers"
          % (len(heads), tables, charts, len(markers)))
    return 1 if rep.blocking else 0


if __name__ == "__main__":
    sys.exit(main())
