#!/usr/bin/env python3
"""Derive build-twohalf-v117.py from build-twohalf-v111.py (the same
arbit-file structure — CALC_CENSUS_JS 22..82, LOGIN_CENSUS_JS 84..119,
header 1..21, ref_exec 122..199, clone_exec 203..348, seedcheck 350..354 —
the v117 derivation is line-count-preserving on the source arbit-v117.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lesson-range bump, the lineage-note fixup LAST — the
v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v111.py"
DST = "scripts/parity-probes/build-twohalf-v117.py"

SWAPS = [
    # generic version swap FIRST (raw v111 tokens -> v117)
    ("v111", "v117"),
    # the TWOHALF_NOTE lesson range (the v111 builder carries the range
    # twice, both single-line: the docstring + the note itself)
    ("the v92..v110 lesson", "the v92..v116 lesson"),
    # the lineage note (post-generic state: 'build-twohalf-v105.py — the
    # v117 derivation' -> 'build-twohalf-v111.py — the v117 derivation' —
    # the LINE-INTERNAL bare form: the source wraps the line after 'from',
    # so the with-prefix fragment never matches, the v107 line-break
    # lesson; runs LAST so no later swap touches the inserted 'v111' token)
    ("build-twohalf-v105.py — the v117 derivation",
     "build-twohalf-v111.py — the v117 derivation"),
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

# normalize back and prove version-swap-only
back = text
for old, new in reversed(SWAPS):
    back = back.replace(new, old)
original = open(SRC, encoding="utf-8").read()
if back != original:
    print("FAIL: not a pure token swap (normalize-back mismatch)")
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)

# residual old-token check on the derived builder — the lineage-note
# fixup deliberately re-inserts 'build-twohalf-v111.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115/v116 residual-precedent discipline).
import re
whitelist = "build-twohalf-v111.py — the v117 derivation"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"v105|v92\.\.v110|arbit-v111|ref-arbit-v111|clone-arbit-v111", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived ({text.count(chr(10))} newlines), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/build-twohalf-v117.py")
