"""Shared helpers for the evaluation harness. Standard library only."""

import json
import os
import re
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
KB_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
EVALS = os.path.join(KB_ROOT, "evals")
GOLDEN = os.path.join(KB_ROOT, "70_golden_set")

# Words that carry no discriminating power when matching a claim to a file.
STOP = set("""a an the and or of to in on for by with as is are was were be been being
it its this that these those from at into than then so such not no nor but if which who whom
whose what when where how why all any both each few more most other some only own same too very
can will just should now does do did done has have had having i you he she we they them their our
your his her one two three there here about after before over under again further once because
while during against between through above below up down out off then also may might must shall
""".split())

WORD = re.compile(r"[\wЀ-ӿ]+", re.UNICODE)


def normalise(text):
    """Lowercase, strip accents and punctuation, collapse whitespace."""
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return " ".join(WORD.findall(text))


META = ("its own", "itself", "acknowledged", "admits", "including its", "own stub",
        "own warning", "this file", "the file itself")


def is_meta_claim(claim):
    """A claim about the file rather than from it — overlap scoring is meaningless."""
    low = claim.lower()
    return any(m in low for m in META)


def content_words(text, min_len=3):
    """Digits are kept at any length: "75%" and "B2" are the whole claim in short citations."""
    return [w for w in normalise(text).split()
            if w not in STOP and (len(w) >= min_len or any(c.isdigit() for c in w))]


_file_cache = {}


def read_kb_file(relpath):
    """Read a KB file by repo-relative path. Returns None if missing."""
    relpath = relpath.strip().strip("`").lstrip("./")
    # skill files sometimes reference ../../ from inside skills/
    relpath = relpath.replace("../../", "")
    if relpath in _file_cache:
        return _file_cache[relpath]
    path = os.path.join(KB_ROOT, relpath)
    if not os.path.isfile(path):
        _file_cache[relpath] = None
        return None
    with open(path, encoding="utf-8") as fh:
        content = normalise(fh.read())
    _file_cache[relpath] = content
    return content


def claim_overlap(claim, file_text):
    """Fraction of the claim's content words present in the file."""
    words = content_words(claim)
    if not words:
        return 1.0
    hits = sum(1 for w in words if w in file_text)
    return hits / len(words)


def load_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def dump_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


class Report:
    """Collects findings and decides the exit code."""

    def __init__(self, name):
        self.name = name
        self.findings = []

    def add(self, severity, item, message):
        self.findings.append({"severity": severity, "item": item, "message": message})

    @property
    def blocking(self):
        return [f for f in self.findings if f["severity"] == "blocking"]

    @property
    def serious(self):
        return [f for f in self.findings if f["severity"] == "serious"]

    @property
    def info(self):
        return [f for f in self.findings if f["severity"] == "info"]

    def render(self):
        lines = ["", "=" * 72, self.name, "=" * 72]
        if not self.findings:
            lines.append("  clean")
            return "\n".join(lines)
        for sev in ("blocking", "serious", "info"):
            group = [f for f in self.findings if f["severity"] == sev]
            if not group:
                continue
            lines.append("")
            lines.append("  %s (%d)" % (sev.upper(), len(group)))
            for f in group:
                lines.append("    %-28s %s" % (f["item"], f["message"]))
        return "\n".join(lines)
