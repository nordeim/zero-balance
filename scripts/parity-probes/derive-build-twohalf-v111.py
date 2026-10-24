#!/usr/bin/env python3
"""Derive build-twohalf-v111.py from build-twohalf-v105.py (the same
arbit-file structure — CALC_CENSUS_JS 22..82, LOGIN_CENSUS_JS 84..119,
header 1..21, ref_exec 122..199, clone_exec 203..348, seedcheck 350..354 —
the v111 derivation is line-count-preserving on the source arbit-v111.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lineage-note fixups that must NOT be re-touched by later
swaps — the v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v105.py"
DST = "scripts/parity-probes/build-twohalf-v111.py"

SWAPS = [
    # generic version swap FIRST (raw v105 tokens -> v111)
    ("v105", "v111"),
    # the TWOHALF_NOTE lesson range (the v105 builder carries the range
    # twice, both single-line: the docstring + the note itself)
    ("the v92..v104 lesson", "the v92..v110 lesson"),
    # the lineage note (post-generic state: 'build-twohalf-v99.py — the v111'
    # -> 'build-twohalf-v105.py — the v111'; runs LAST so no later swap
    # touches the inserted 'v105' token)
    ("build-twohalf-v99.py — the v111 derivation",
     "build-twohalf-v105.py — the v111 derivation"),
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
    t = t.replace("the v92..v110 lesson", "the v92..v104 lesson")
    t = t.replace("build-twohalf-v105.py — the v111 derivation",
                  "build-twohalf-v99.py — the v111 derivation")
    t = t.replace("v111", "v105")
    return t

if normalize_back(text) != open(SRC, encoding="utf-8").read():
    print("FAIL: derived builder is NOT token-swap-only vs source")
    sys.exit(1)

# residual check on the derived file: no un-swapped v105 session tokens
import re
bad = re.findall(r"v92\.\.v104|build-twohalf-v99", text)
if bad:
    print("RESIDUAL OLD TOKENS in derived file:", set(bad))
    sys.exit(1)

print(f"OK: {DST} derived; token-swap-only verified by normalize-back diff")
print("run it now: python3 scripts/parity-probes/build-twohalf-v111.py")
