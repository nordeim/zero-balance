#!/usr/bin/env python3
"""Derive build-twohalf-v153.py from build-twohalf-v147.py (the LOGIN+CALC
lineage's TWO-block builder form — CALC_CENSUS_JS lines 22..82 +
LOGIN_CENSUS_JS lines 84..119, header 1..21, ref_exec 122..199, clone_exec
203..348, seedcheck 350..354 — the v153 derivation is line-count-preserving
on the source arbit-v153.sh, itself a corrected-swap of arbit-v147.sh).
Token swaps only; verified by normalize-back diff (swap order: the generic
swap FIRST, then the lesson-range bump, the lineage-note fixup LAST —
the v110 swap-order rule).
NOTE the v147-lineage builder carries no embedded session token (the
session exports live in the arbit source file itself, already carrying
reflogin153arbit/refcalc153arbit/clonelogin153arbit/clonecalc153arbit
after the series derivation), so no stale-session bump is needed this
cycle."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v147.py"
DST = "scripts/parity-probes/build-twohalf-v153.py"

SWAPS = [
    # generic version swap (raw v147 tokens -> v153)
    ("v147", "v153"),
    # the TWOHALF_NOTE lesson range (the v147 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms incl. the note's line-wrapped tail, the v131 lesson)
    ("v92..v146", "v92..v152"),
    # the lineage note (the source's prose pointer 'build-twohalf-v141.py'
    # — untouched by the generic swap, so the fragments are identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v147' tokens)
    ("build-twohalf-v141.py", "build-twohalf-v147.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v147.py' (the source
# pointer), so those occurrences are whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "build-twohalf-v147.py"
residual_text = text.replace(whitelist, "")
residual = re.findall(r"v129|v92\.\.v146|arbit-v147|ref-arbit-v147|clone-arbit-v147|reflogin147|clonelogin147|refcalc147|clonecalc147", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived — version-swap-only (normalize-back diff clean), zero old tokens (the lineage-note 'build-twohalf-v147.py' whitelisted; the lesson range bumped v92..v146 -> v92..v152)")
