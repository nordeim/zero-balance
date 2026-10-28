#!/usr/bin/env python3
"""Derive build-twohalf-v131.py from build-twohalf-v125.py (the same
arbit-file structure — ARBIT_G lines 28..89, ARBIT_Q lines 91..148,
ARBIT_X lines 151..175, header 1..25, ref_exec 177..217, clone_exec
218..258, seedcheck through 259 — the v131 derivation is
line-count-preserving on the source arbit-v131.sh, itself a 259-line
version-swap of arbit-v125.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lesson-range bump, the lineage-note fixup LAST — the
v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v125.py"
DST = "scripts/parity-probes/build-twohalf-v131.py"

SWAPS = [
    # generic version swap FIRST (raw v125 tokens -> v131)
    ("v125", "v131"),
    # the TWOHALF_NOTE lesson range (the v125 builder carries the range
    # twice: the docstring's single-line form AND the note's line-wrapped
    # form "the v92..v124\n# lesson" — the bare range token covers both)
    ("v92..v124", "v92..v130"),
    # the lineage note (the source's prose form 'from
    # build-twohalf-v119.py' — untouched by the generic swap, so the
    # fragment is identical pre/post swap; runs LAST so no later swap
    # touches the inserted 'v125' token)
    ("verbatim from build-twohalf-v119.py", "verbatim from build-twohalf-v125.py"),
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
# fixup deliberately re-inserts 'from build-twohalf-v125.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115/v116/v117/v118/v124/v130 residual-precedent discipline).
import re
whitelist = "verbatim from build-twohalf-v125.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"build-twohalf-v119|v92\.\.v124|arbit-v125|ref-arbit-v125|clone-arbit-v125", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived ({text.count(chr(10))} newlines), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/build-twohalf-v131.py")
