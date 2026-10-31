#!/usr/bin/env python3
"""Derive build-twohalf-v137.py from build-twohalf-v131.py (the same
arbit-file structure — ARBIT_G lines 28..89, ARBIT_Q lines 91..148,
ARBIT_X lines 151..175, header 1..25, ref_exec 177..217, clone_exec
218..258 — the v137 derivation is line-count-preserving on the source
arbit-v137.sh, itself a 258-line version-swap of arbit-v131.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lesson-range bump, the lineage-note fixup LAST — the
v110 swap-order rule)."""
import re
import sys

SRC = "scripts/parity-probes/build-twohalf-v131.py"
DST = "scripts/parity-probes/build-twohalf-v137.py"

SWAPS = [
    # generic version swap FIRST (raw v131 tokens -> v137)
    ("v131", "v137"),
    # the TWOHALF_NOTE lesson range (the v131 builder carries the range
    # twice: the docstring's single-line form + the note's own LINE-WRAPPED
    # form — 'the v92..v130\n# lesson' — so the bare range token is the
    # swap unit, both occurrences within-line)
    ("v92..v130", "v92..v136"),
    # the lineage note (the source's prose form 'verbatim from
    # build-twohalf-v125.py — the v137 derivation' — untouched by the
    # generic swap, so the fragment is identical pre/post swap; runs LAST
    # so no later swap touches the inserted 'v131' token)
    ("verbatim from build-twohalf-v125.py — the v137 derivation",
     "verbatim from build-twohalf-v131.py — the v137 derivation"),
]

# NOTE: the lesson-range swap runs as the BARE token because the v131
# lineage's TWOHALF_NOTE wraps the phrase across two lines.

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
# fixup deliberately re-inserts 'build-twohalf-v131.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115..v130 residual-precedent discipline).
whitelist = "build-twohalf-v131.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"build-twohalf-v125|v92\.\.v130|arbit-v131|ref-arbit-v131|clone-arbit-v131", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived ({text.count(chr(10)) + 1} lines), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/build-twohalf-v137.py")
