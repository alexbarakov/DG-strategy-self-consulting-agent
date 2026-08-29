#!/usr/bin/env python3
"""Loop A — rot detection.

The golden set cites KB files. Files change; keys go stale. This maps a set of
changed files onto the items that cite them. The output is a review list, not a
failure: the set is stale, not wrong, and a human has to look.

Usage:
  python3 evals/check_rot.py --since HEAD~1        # what a commit invalidated
  python3 evals/check_rot.py --files a.md b.md     # explicit
  python3 evals/check_rot.py --orphans             # citations pointing at files that no longer exist
"""

import argparse
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.kb import GOLDEN, KB_ROOT, Report  # noqa: E402

THRESHOLD = 15  # per HARNESS_PLAN.md: more than this and the set gets a review pass


def load_index():
    with open(os.path.join(GOLDEN, "index.json"), encoding="utf-8") as fh:
        return json.load(fh)


def changed_since(ref):
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", ref, "--", "."],
            cwd=KB_ROOT, stderr=subprocess.DEVNULL, text=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    prefix = os.path.relpath(KB_ROOT, subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], cwd=KB_ROOT, text=True).strip())
    files = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith(prefix + "/"):
            line = line[len(prefix) + 1:]
        files.append(line)
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since")
    ap.add_argument("--files", nargs="*")
    ap.add_argument("--orphans", action="store_true")
    args = ap.parse_args()

    index = load_index()
    by_file = index["by_file"]
    rep = Report("ROT")

    if args.orphans:
        missing = [f for f in by_file if not os.path.isfile(os.path.join(KB_ROOT, f))]
        for f in missing:
            rep.add("blocking", "ORPHAN", "%s cited by %d items but does not exist"
                    % (f, len(by_file[f])))
        print(rep.render())
        print("\n  %d cited files, %d orphaned" % (len(by_file), len(missing)))
        return 1 if rep.blocking else 0

    files = args.files
    if args.since:
        files = changed_since(args.since)
        if files is None:
            print("  git unavailable — pass --files instead")
            return 0
    if not files:
        ap.error("pass --since, --files or --orphans")

    stale = {}
    for f in files:
        for item in by_file.get(f, []):
            stale.setdefault(item, []).append(f)

    for item, causes in sorted(stale.items()):
        rep.add("info", item, "cites changed: " + ", ".join(causes))

    print(rep.render())
    n = len(stale)
    print("\n  %d changed file(s) → %d item(s) need review" % (len(files), n))
    if n > THRESHOLD:
        print("  over the review threshold of %d — the set gets a pass, not spot fixes" % THRESHOLD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
