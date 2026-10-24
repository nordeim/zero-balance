#!/usr/bin/env python3
"""Derive build-twohalf-v112.py from build-twohalf-v106.py (the same
arbit-file structure — ARBIT_A lines 25..114, ARBIT_B lines 116..226,
header 1..24, ref_exec 228..273, clone_exec 275..323, seedcheck 325..327 —
the v112 derivation is line-count-preserving on the source arbit-v112.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lineage-note fixups that must NOT be re-touched by later
swaps — the v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v106.py"
DST = "scripts/parity-probes/build-twohalf-v112.py"

SWAPS = [
    # generic version swap FIRST (raw v106 tokens -> v112)
    ("v106", "v112"),
    # the TWOHALF_NOTE lesson range (the v106 builder carries the range
    # twice, both single-line: the docstring + the note itself)
    ("the v92..v105 lesson", "the v92..v111 lesson"),
    # the lineage note (post-generic state: 'the v100-lineage derivation'
    # -> 'the v106-lineage derivation'; runs LAST so no later swap
    # touches the inserted 'v106' token)
    ("the v100-lineage derivation",
     "the v106-lineage derivation"),
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
    t = t.replace("the v106-lineage derivation",
                  "the v100-lineage derivation")
    t = t.replace("the v92..v111 lesson", "the v92..v105 lesson")
    t = t.replace("v112", "v106")
    return t

if normalize_back(text) != open(SRC, encoding="utf-8").read():
    print("FAIL: derived builder is NOT token-swap-only vs source")
    sys.exit(1)

# residual check on the derived file: no un-swapped v106 lineage tokens
import re
bad = re.findall(r"v92\.\.v105|v100-lineage", text)
if bad:
    print("RESIDUAL OLD TOKENS in derived file:", set(bad))
    sys.exit(1)

print(f"OK: {DST} derived; token-swap-only verified by normalize-back diff")
print("run it now: python3 scripts/parity-probes/build-twohalf-v112.py")
