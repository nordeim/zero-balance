#!/usr/bin/env python3
"""Derive build-twohalf-v132.py from build-twohalf-v126.py (the same
arbit-file structure — NW_CENSUS lines 18..59, DASH_CENSUS lines 61..147,
header 1..16, ref_exec 149..185 — the v132 derivation is line-count-
preserving on the source arbit-v132.sh, itself a 220-line corrected-swap
of arbit-v126.sh).
Token swaps only; verified by normalize-back diff (swap order: the stale
session token FIRST, then the generic swap, then the lesson-range bump,
the lineage-note fixup LAST — the v110 swap-order rule).
NOTE the stale-session fix (the v121-cycle precedent): the v126 builder's
embedded clone_login carries 'clonearbit120' — a twice-stale token the
v126 lineage inherited verbatim from v120 (its own 'session token bumped'
comment notwithstanding). The v132 derivation bumps it to 'clonearbit132'
so the built clone half's session namespace AGREES with the combined
arbit-v132.sh's own 'clonearbit132' (the bare v126->v132 swap cannot touch
it — the token carries no 'v' prefix)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v126.py"
DST = "scripts/parity-probes/build-twohalf-v132.py"

SWAPS = [
    # stale session token FIRST (no 'v' prefix — untouched by the generic swap)
    ("clonearbit120", "clonearbit132"),
    # generic version swap (raw v126 tokens -> v132)
    ("v126", "v132"),
    # the TWOHALF_NOTE lesson range (the v126 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms incl. the note's line-wrapped tail, the v131 lesson)
    ("v92..v125", "v92..v131"),
    # the lineage note (the source's prose pointers 'build-twohalf-v120.py'
    # — untouched by the generic swap, so the fragments are identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v126' tokens)
    ("build-twohalf-v120.py", "build-twohalf-v126.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v126.py' (the source
# pointer), so those occurrences are whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "build-twohalf-v126.py"
residual_text = text.replace(whitelist, "")
residual = re.findall(r"v120|v92\.\.v125|arbit-v126|ref-arbit-v126|clone-arbit-v126|clonearbit120", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived — version-swap-only (normalize-back diff clean), zero old tokens (the lineage-note 'build-twohalf-v126.py' whitelisted; the stale clonearbit120 bumped to clonearbit132)")
