#!/usr/bin/env python3
"""Derive build-twohalf-v125.py from build-twohalf-v119.py (the same
arbit-file structure — ARBIT_G lines 28..89, ARBIT_Q lines 91..148,
ARBIT_X lines 151..175, header 1..25, ref_exec 177..217, clone_exec
218..258 — the v125 derivation is line-count-preserving on the source
arbit-v125.sh, itself a 259-line corrected-swap of arbit-v119.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lesson-range bump, the lineage-note fixup LAST — the
v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v119.py"
DST = "scripts/parity-probes/build-twohalf-v125.py"

SWAPS = [
    # generic version swap FIRST (raw v119 tokens -> v125)
    ("v119", "v125"),
    # the TWOHALF_NOTE lesson range (the v119 builder carries the range
    # twice: the docstring single-line + the note itself — the bare-range
    # swap catches both forms)
    ("v92..v118", "v92..v124"),
    # the lineage note (the source's prose pointer 'build-twohalf-v113.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v119' token)
    ("build-twohalf-v113.py", "build-twohalf-v119.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v119.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "build-twohalf-v119.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"v113|v92\.\.v118|arbit-v119|ref-arbit-v119|clone-arbit-v119", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived — version-swap-only (normalize-back diff clean), zero old tokens (the lineage-note 'build-twohalf-v119.py' whitelisted)")
