#!/usr/bin/env python3
"""Derive build-twohalf-v140.py from build-twohalf-v134.py (the same
arbit-file structure — CENSUS_JS lines 38..190, header 1..36, ref_exec
193..224, clone_exec 227..256 — the v140 derivation is
line-count-preserving on the source arbit-v140.sh, itself a corrected-swap
of arbit-v134.sh).
Token swaps only; verified by normalize-back diff (swap order: the generic
swap FIRST, then the lesson-range bump, the lineage-note fixup LAST —
the v110 swap-order rule).
NOTE the v134-lineage builder carries no embedded clone_login session token
(the session exports live in the arbit source file itself, already carrying
refarbit140/clonearbit140 after the series derivation), so no stale-session
bump is needed this cycle (unlike the v133->v139 lineage form)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v134.py"
DST = "scripts/parity-probes/build-twohalf-v140.py"

SWAPS = [
    # stale session token FIRST (no 'v' prefix — untouched by the generic
    # swap): the v134 builder's ref_exec ASSERTION pins 'refarbit134'; the
    # derived arbit-v140.sh's ref block exports 'refarbit140', so the
    # assertion must agree (the v121 stale-session precedent, this
    # lineage's assertion form)
    ("refarbit134", "refarbit140"),
    # generic version swap (raw v134 tokens -> v140)
    ("v134", "v140"),
    # the TWOHALF_NOTE lesson range (the v134 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms incl. the note's line-wrapped tail, the v131 lesson)
    ("v92..v133", "v92..v139"),
    # the lineage note (the source's prose pointer 'build-twohalf-v128.py'
    # — untouched by the generic swap, so the fragments are identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v134' tokens)
    ("build-twohalf-v128.py", "build-twohalf-v134.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v134.py' (the source
# pointer), so those occurrences are whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "build-twohalf-v134.py"
residual_text = text.replace(whitelist, "")
residual = re.findall(r"v128|v92\.\.v133|arbit-v134|ref-arbit-v134|clone-arbit-v134|refarbit134|clonearbit134", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived — version-swap-only (normalize-back diff clean), zero old tokens (the lineage-note 'build-twohalf-v134.py' whitelisted; the assertion's stale refarbit134 bumped to refarbit140; the lesson range bumped v92..v133 -> v92..v139)")
