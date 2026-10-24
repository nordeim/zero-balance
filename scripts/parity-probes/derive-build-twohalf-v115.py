#!/usr/bin/env python3
"""Derive build-twohalf-v115.py from build-twohalf-v109.py (the same
arbit-file structure — CENSUS_JS lines 22..214, header 1..21, ref_exec
216..250, the clone half env-injected — the v115 derivation is
line-count-preserving on the source arbit-v115.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lesson-range bump, the census-provenance corrections, and
the lineage-note fixup LAST — the v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v109.py"
DST = "scripts/parity-probes/build-twohalf-v115.py"

SWAPS = [
    # generic version swap FIRST (raw v109 tokens -> v115)
    ("v109", "v115"),
    # the TWOHALF_NOTE lesson range (the v109 builder carries the
    # dot form 'v92..v95' twice: the docstring + the note — bumped to
    # the standing range through the previous cycle)
    ("v92..v95", "v92..v114"),
    # the census-provenance docstring (post-generic state)
    ("the v97/v103 census block verbatim", "the v103/v109 census block verbatim"),
    ("remediation-plan-v103.md", "remediation-plan-v109.md"),
    # the lineage note (post-generic state: 'build-twohalf-v103.py' ->
    # 'build-twohalf-v109.py'; runs LAST so no later swap touches the
    # inserted 'v109' token)
    ("build-twohalf-v103.py", "build-twohalf-v109.py"),
]

text = open(SRC, encoding="utf-8").read()
missing = []
for old, new in SWAPS:
    if old not in text:
        missing.append(old)
    text = text.replace(old, new)
if missing:
    print("MISSING SOURCES:", missing)
    sys.exit(1)
open(DST, "w", encoding="utf-8").write(text)

# normalize-back verification: the derived file must differ from the source
# by version tokens ONLY (every swapped token reverses cleanly)
def normalize_back(t):
    t = t.replace("build-twohalf-v109.py", "build-twohalf-v103.py")
    t = t.replace("remediation-plan-v109.md", "remediation-plan-v103.md")
    t = t.replace("the v103/v109 census block verbatim", "the v97/v103 census block verbatim")
    t = t.replace("v92..v114", "v92..v95")
    t = t.replace("v115", "v109")
    return t

if normalize_back(text) != open(SRC, encoding="utf-8").read():
    print("FAIL: derived builder is NOT token-swap-only vs source")
    sys.exit(1)

# residual check on the derived file: no un-swapped v109-lineage tokens
# (the lineage note's 'build-twohalf-v109.py' + the census-provenance
# 'v103/v109' pair are LEGIT survivors — historical references)
import re
bad = re.findall(r"v92\.\.v95|build-twohalf-v103|the v97/v103 census", text)
if bad:
    print("RESIDUAL OLD TOKENS in derived file:", set(bad))
    sys.exit(1)

print(f"OK: {DST} derived; token-swap-only verified by normalize-back diff")
print("run it now: python3 scripts/parity-probes/build-twohalf-v115.py")
