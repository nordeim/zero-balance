#!/usr/bin/env python3
"""Derive build-twohalf-v154.py from build-twohalf-v148.py (the NETWORTH+
DRILL-DOWN lineage's TWO-block builder form — ARBIT_A census JS lines
25..114 + ARBIT_B census JS lines 116..226, header 1..24, ref_exec
228..273, clone_exec 275..323, seedcheck 325..327 — the v154 derivation is
line-count-preserving on the source arbit-v154.sh, itself a corrected-swap
of arbit-v148.sh at identical boundaries).
Token swaps only; verified by normalize-back diff (swap order: the generic
swap FIRST, then the lesson-range bump, the lineage-note fixup LAST —
the v110 swap-order rule).
NOTE the v148-lineage builder carries no embedded session token (the
session exports live in the arbit source file itself, already carrying
refar154/clonear154 after the series derivation), so no stale-session bump
is needed this cycle."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v148.py"
DST = "scripts/parity-probes/build-twohalf-v154.py"

SWAPS = [
    # generic version swap (raw v148 tokens -> v154)
    ("v148", "v154"),
    # the TWOHALF_NOTE lesson range (the v148 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms incl. the note's line-wrapped tail, the v131 lesson)
    ("v92..v147", "v92..v153"),
    # the lineage note (the source's prose pointer 'the v142-lineage
    # derivation' — untouched by the generic swap, so the fragments are
    # identical pre/post swap; runs LAST so no later swap touches the
    # inserted 'v148' tokens)
    ("the v142-lineage derivation", "the v148-lineage derivation"),
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
# fixup deliberately re-inserts 'the v148-lineage derivation' (the source
# pointer), so those occurrences are whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "the v148-lineage derivation"
residual_text = text.replace(whitelist, "")
residual = re.findall(r"v92\.\.v147|arbit-v148|ref-arbit-v148|clone-arbit-v148|refar148|clonear148|refvlm148|clonevlm148", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived — version-swap-only (normalize-back diff clean), zero old tokens (the lineage-note 'the v148-lineage derivation' whitelisted; the lesson range bumped v92..v147 -> v92..v153)")
