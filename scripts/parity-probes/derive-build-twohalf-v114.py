#!/usr/bin/env python3
"""Derive build-twohalf-v114.py from build-twohalf-v108.py (the same
arbit-file structure — NW_CENSUS lines 18..59, DASH_CENSUS lines 61..147,
header 1..16, ref_exec 149..185, the clone half env-injected — the v114
derivation is line-count-preserving on the source arbit-v114.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lineage-note fixups that must NOT be re-touched by later
swaps — the v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v108.py"
DST = "scripts/parity-probes/build-twohalf-v114.py"

SWAPS = [
    # generic version swap FIRST (raw v108 tokens -> v114)
    ("v108", "v114"),
    # the TWOHALF_NOTE lesson range (the v108 builder carries the
    # dot form 'v92..v95' twice: the docstring + the note — bumped to
    # the standing range through the previous cycle)
    ("v92..v95", "v92..v113"),
    # the lineage note (post-generic state: 'build-twohalf-v102.py' ->
    # 'build-twohalf-v108.py'; runs LAST so no later swap touches the
    # inserted 'v108' token)
    ("build-twohalf-v102.py", "build-twohalf-v108.py"),
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
    t = t.replace("build-twohalf-v108.py", "build-twohalf-v102.py")
    t = t.replace("v92..v113", "v92..v95")
    t = t.replace("v114", "v108")
    return t

if normalize_back(text) != open(SRC, encoding="utf-8").read():
    print("FAIL: derived builder is NOT token-swap-only vs source")
    sys.exit(1)

# residual check on the derived file: no un-swapped v108-lineage tokens
# (the lineage note's 'build-twohalf-v108.py' is a LEGIT survivor)
import re
bad = re.findall(r"v92\.\.v95|build-twohalf-v102", text)
if bad:
    print("RESIDUAL OLD TOKENS in derived file:", set(bad))
    sys.exit(1)

print(f"OK: {DST} derived; token-swap-only verified by normalize-back diff")
print("run it now: python3 scripts/parity-probes/build-twohalf-v114.py")
