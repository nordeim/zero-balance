#!/usr/bin/env python3
"""Derive build-twohalf-v120.py from build-twohalf-v114.py (the same
arbit-file structure — NW_CENSUS lines 18..59, DASH_CENSUS lines 61..147,
header 1..16, ref_exec 149..185, the clone side env-injection — the v120
derivation is line-count-preserving on the source arbit-v120.sh, itself a
220-line corrected-swap of arbit-v114.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the stale-session fix, the lesson-range bump, the lineage-note
fixup LAST — the v110 swap-order rule).
NOTE the v114 builder's clone_login carried the STALE session token
'clonearbit108' (inherited verbatim from build-twohalf-v108.py — the
v114-cycle derivation quirk): fixed to 'clonearbit120' in this lineage
(the token's purpose — a session name distinct from the ref half's —
preserved, the version now correct)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v114.py"
DST = "scripts/parity-probes/build-twohalf-v120.py"

SWAPS = [
    # generic version swap FIRST (raw v114 tokens -> v120)
    ("v114", "v120"),
    # the stale clone session token (the v114 builder inherited it from
    # the v108 builder unbumped — fixed in this lineage)
    ("clonearbit108", "clonearbit120"),
    # the TWOHALF_NOTE lesson range (the v114 builder carries the range
    # twice: the docstring + the note itself — the bare-range swap catches
    # both occurrences)
    ("v92..v113", "v92..v119"),
    # the lineage note (the source's prose pointer 'build-twohalf-v108.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v114' token)
    ("build-twohalf-v108.py", "build-twohalf-v114.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v114.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115/v116/v117/v118/v119 residual-precedent discipline).
import re
whitelist = "build-twohalf-v114.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"v108|clonearbit108|v92\.\.v113|arbit-v114|ref-arbit-v114|clone-arbit-v114", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived ({text.count(chr(10))} newlines), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/build-twohalf-v120.py")
