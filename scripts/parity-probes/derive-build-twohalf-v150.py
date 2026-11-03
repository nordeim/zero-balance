#!/usr/bin/env python3
"""Derive build-twohalf-v150.py from build-twohalf-v144.py (the same
arbit-file structure — NW_CENSUS lines 18..59, DASH_CENSUS lines 61..147,
header 1..16, ref_exec 149..185 — the v150 derivation is line-count-
preserving on the source arbit-v150.sh, itself a 219-line corrected-swap
of arbit-v144.sh).
Token swaps only; verified by normalize-back diff (swap order: the session
token FIRST, then the generic swap, then the lesson-range bump, the
lineage-note fixup LAST — the v110 swap-order rule).
NOTE the session-token swap (the v121-cycle stale-session-fix precedent):
the v144 builder's embedded clone_login carries 'clonearbit144' — the
v144 lineage's own CURRENT token. The v150 derivation bumps it to
'clonearbit150' so the built clone half's session namespace AGREES with
the combined arbit-v150.sh's own 'clonearbit150' (the bare v144->v150
swap cannot touch it — the token carries no 'v' prefix)."""
import re
import sys

SRC = "scripts/parity-probes/build-twohalf-v144.py"
DST = "scripts/parity-probes/build-twohalf-v150.py"

SWAPS = [
    # session token FIRST (no 'v' prefix — untouched by the generic swap)
    ("clonearbit144", "clonearbit150"),
    # generic version swap (raw v144 tokens -> v150)
    ("v144", "v150"),
    # the TWOHALF_NOTE lesson range (the v144 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms incl. the note's line-wrapped tail, the v131 lesson)
    ("v92..v143", "v92..v149"),
    # the lineage note (the source's prose pointer 'build-twohalf-v138.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v144' token)
    ("build-twohalf-v138.py", "build-twohalf-v144.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v144.py' (the source
# pointer), so that occurrence is whitelisted before the scan
# (the v115..v144 residual-precedent discipline).
whitelist = "build-twohalf-v144.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"build-twohalf-v138|v92\.\.v143|arbit-v144|ref-arbit-v144|clone-arbit-v144|clonearbit144", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived ({text.count(chr(10)) + 1} lines), normalize-back clean, zero old tokens (the lineage-note 'build-twohalf-v144.py' whitelisted; the session token bumped clonearbit144->clonearbit150)")
print("run it now: python3 scripts/parity-probes/build-twohalf-v150.py")
