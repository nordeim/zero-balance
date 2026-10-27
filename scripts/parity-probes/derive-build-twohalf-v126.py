#!/usr/bin/env python3
"""Derive build-twohalf-v126.py from build-twohalf-v120.py (the same
arbit-file structure — NW_CENSUS lines 18..59, DASH_CENSUS lines 61..147,
header 1..16, ref_exec 149..185 — the v126 derivation is line-count-
preserving on the source arbit-v126.sh, itself a 220-line corrected-swap
of arbit-v120.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lesson-range bump, the lineage-note fixup LAST — the
v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v120.py"
DST = "scripts/parity-probes/build-twohalf-v126.py"

SWAPS = [
    # generic version swap FIRST (raw v120 tokens -> v126)
    ("v120", "v126"),
    # the TWOHALF_NOTE lesson range (the v120 builder carries the range
    # twice: the docstring single-line + the note itself — the bare-range
    # swap catches both forms)
    ("v92..v119", "v92..v125"),
    # the lineage note (the source's prose pointer 'build-twohalf-v114.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v120' token)
    ("build-twohalf-v114.py", "build-twohalf-v120.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v120.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "build-twohalf-v120.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"v114|v92\.\.v119|arbit-v120|ref-arbit-v120|clone-arbit-v120", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived — version-swap-only (normalize-back diff clean), zero old tokens (the lineage-note 'build-twohalf-v120.py' whitelisted)")
