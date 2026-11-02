#!/usr/bin/env python3
"""Derive build-twohalf-v145.py from build-twohalf-v139.py (the same
arbit-file structure — CENSUS_JS lines 22..214, header 1..21, ref_exec
216..250 — the v145 derivation is line-count-preserving on the source
arbit-v145.sh, itself a 285-line corrected-swap of arbit-v139.sh).
Token swaps only; verified by normalize-back diff (swap order: the session
token FIRST, then the generic swap, then the lesson-range bump, the
lineage-note fixup LAST — the v110 swap-order rule).
NOTE the session-token swap (the v121-cycle stale-session-fix precedent):
the v139 builder's embedded clone_login carries 'clonearbit139' — the
v139 lineage's own CURRENT token. The v145 derivation bumps it to
'clonearbit145' so the built clone half's session namespace AGREES with
the combined arbit-v145.sh's own 'clonearbit145' (the bare v139->v145
swap cannot touch it — the token carries no 'v' prefix)."""
import re
import sys

SRC = "scripts/parity-probes/build-twohalf-v139.py"
DST = "scripts/parity-probes/build-twohalf-v145.py"

SWAPS = [
    # session token FIRST (no 'v' prefix — untouched by the generic swap)
    ("clonearbit139", "clonearbit145"),
    # generic version swap (raw v139 tokens -> v145)
    ("v139", "v145"),
    # the TWOHALF_NOTE lesson range (the v139 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms incl. the note's line-wrapped tail, the v131 lesson)
    ("v92..v138", "v92..v144"),
    # the lineage note (the source's prose pointer 'build-twohalf-v133.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v139' token)
    ("build-twohalf-v133.py", "build-twohalf-v139.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v139.py' (the source
# pointer), so that occurrence is whitelisted before the scan
# (the v115..v144 residual-precedent discipline).
whitelist = "build-twohalf-v139.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"build-twohalf-v133|v92\.\.v138|arbit-v139|ref-arbit-v139|clone-arbit-v139|clonearbit139", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived ({text.count(chr(10)) + 1} lines), normalize-back clean, zero old tokens (the lineage-note 'build-twohalf-v139.py' whitelisted; the session token bumped clonearbit139->clonearbit145)")
print("run it now: python3 scripts/parity-probes/build-twohalf-v145.py")
