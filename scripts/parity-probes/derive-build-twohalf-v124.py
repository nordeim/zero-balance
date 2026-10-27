#!/usr/bin/env python3
"""Derive build-twohalf-v124.py from build-twohalf-v118.py (the same
arbit-file structure — ARBIT_A lines 25..114, ARBIT_B lines 116..226,
header 1..24, ref_exec 228..273, clone_exec 275..323, seedcheck 325..327 —
the v124 derivation is line-count-preserving on the source arbit-v124.sh,
itself a 328-line version-swap of arbit-v118.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lesson-range bump, the lineage-note fixup LAST — the
v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v118.py"
DST = "scripts/parity-probes/build-twohalf-v124.py"

SWAPS = [
    # generic version swap FIRST (raw v118 tokens -> v124)
    ("v118", "v124"),
    # the TWOHALF_NOTE lesson range (the v118 builder carries the range
    # twice, both single-line: the docstring + the note itself)
    ("the v92..v117 lesson", "the v92..v123 lesson"),
    # the lineage note (the source's prose form 'the v112-lineage
    # derivation' — untouched by the generic swap, so the fragment is
    # identical pre/post swap; runs LAST so no later swap touches the
    # inserted 'v118' token)
    ("the v112-lineage derivation", "the v118-lineage derivation"),
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
# fixup deliberately re-inserts 'the v118-lineage derivation' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "the v118-lineage derivation"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"v112|v92\.\.v117|arbit-v118|ref-arbit-v118|clone-arbit-v118", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived ({text.count(chr(10))} newlines), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/build-twohalf-v124.py")
