#!/usr/bin/env python3
"""Derive build-twohalf-v146.py from build-twohalf-v140.py (the same
arbit-file structure — CENSUS_JS lines 38..190, header 1..36, ref_exec
193..224, clone_exec 227..256 — the v146 derivation is
line-count-preserving on the source arbit-v146.sh, itself a corrected-swap
of arbit-v140.sh).
Token swaps only; verified by normalize-back diff (swap order: the generic
swap FIRST, then the lesson-range bump, the lineage-note fixup LAST —
the v110 swap-order rule).
NOTE the v140-lineage builder carries no embedded clone_login session token
(the session exports live in the arbit source file itself, already carrying
refarbit146/clonearbit146 after the series derivation), so no stale-session
bump is needed beyond the assertion's refarbit token this cycle (unlike the
v133->v139 lineage form)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v140.py"
DST = "scripts/parity-probes/build-twohalf-v146.py"

SWAPS = [
    # stale session token FIRST (no 'v' prefix — untouched by the generic
    # swap): the v140 builder's ref_exec ASSERTION pins 'refarbit140'; the
    # derived arbit-v146.sh's ref block exports 'refarbit146', so the
    # assertion must agree (the v121 stale-session precedent, this
    # lineage's assertion form)
    ("refarbit140", "refarbit146"),
    # generic version swap (raw v140 tokens -> v146)
    ("v140", "v146"),
    # the TWOHALF_NOTE lesson range (the v140 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms incl. the note's line-wrapped tail, the v131 lesson)
    ("v92..v139", "v92..v145"),
    # the lineage note (the source's prose pointer 'build-twohalf-v134.py'
    # — untouched by the generic swap, so the fragments are identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v140' tokens)
    ("build-twohalf-v134.py", "build-twohalf-v140.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v140.py' (the source
# pointer), so those occurrences are whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "build-twohalf-v140.py"
residual_text = text.replace(whitelist, "")
residual = re.findall(r"v92\.\.v139|arbit-v140|ref-arbit-v140|clone-arbit-v140|refarbit140|clonearbit140", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived — version-swap-only (normalize-back diff clean), zero old tokens (the lineage-note 'build-twohalf-v140.py' whitelisted; the assertion's stale refarbit140 bumped to refarbit146; the lesson range bumped v92..v139 -> v92..v145)")
