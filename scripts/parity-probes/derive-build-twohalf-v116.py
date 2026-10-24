#!/usr/bin/env python3
"""Derive build-twohalf-v116.py from build-twohalf-v110.py (the same
arbit-file structure — SV_CENSUS_JS lines 38..190, header 1..36, ref_exec
193..224, clone_exec 227..256 — the v116 derivation is line-count-
preserving on the source arbit-v116.sh, itself line-identical to the
v110 source [within-line corrections only]). Token swaps only; verified
by normalize-back diff (swap order: generic FIRST, then the lesson-range
bump, the lineage-note fixup LAST — the v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v110.py"
DST = "scripts/parity-probes/build-twohalf-v116.py"

SWAPS = [
    # generic version swap FIRST (raw v110 tokens -> v116)
    ("v110", "v116"),
    # the ref_exec startswith assertion's bare session token (no 'v'
    # prefix — untouched by the generic swap; must match arbit-v116.sh's
    # own refarbit116 session line, itself swapped by the series derive)
    ("refarbit110", "refarbit116"),
    # the TWOHALF_NOTE lesson range (the v110 builder carries the dot
    # form 'v92..v109' twice: the docstring + the note — bumped to the
    # standing range through the previous cycle)
    ("v92..v109", "v92..v115"),
    # the lineage note (post-generic state: 'build-twohalf-v104.py — the
    # v116' -> 'build-twohalf-v110.py — the v116'; runs LAST so no later
    # swap touches the inserted 'v110' token)
    ("Line numbers inherited verbatim from build-twohalf-v104.py — the v116",
     "Line numbers inherited verbatim from build-twohalf-v110.py — the v116"),
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
# fixup deliberately re-inserts 'build-twohalf-v110.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115 residual-precedent discipline).
import re
whitelist = "build-twohalf-v110.py — the v116"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"v110|v92\.\.v109|refarbit110|clonearbit110|ref-arbit-v110|clone-arbit-v110", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived ({text.count(chr(10))} lines), normalize-back clean, zero old tokens")
