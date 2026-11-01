#!/usr/bin/env python3
"""Derive build-twohalf-v139.py from build-twohalf-v133.py (the same
arbit-file structure — CENSUS_JS lines 22..214, header 1..21, ref_exec
216..250 — the v139 derivation is line-count-preserving on the source
arbit-v139.sh, itself a 285-line corrected-swap of arbit-v133.sh).
Token swaps only; verified by normalize-back diff (swap order: the stale
session token FIRST, then the generic swap, then the lesson-range bump,
the lineage-note fixup LAST — the v110 swap-order rule).
NOTE the stale-session fix (the v121-cycle precedent, applied by v132/v133
on their lineages): the v133 builder's embedded clone_login carries
'clonearbit133' — current for v133 but stale the moment the combined
arbit-v139.sh is derived with its own 'clonearbit139' (the bare v133->v139
swap cannot touch it — the token carries no 'v' prefix). The v139
derivation bumps it to 'clonearbit139' so the built clone half's session
namespace AGREES with the combined arbit-v139.sh's own 'clonearbit139'."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v133.py"
DST = "scripts/parity-probes/build-twohalf-v139.py"

SWAPS = [
    # stale session token FIRST (no 'v' prefix — untouched by the generic swap)
    ("clonearbit133", "clonearbit139"),
    # generic version swap (raw v133 tokens -> v139)
    ("v133", "v139"),
    # the TWOHALF_NOTE lesson range (the v133 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms incl. the note's line-wrapped tail, the v131 lesson)
    ("v92..v132", "v92..v138"),
    # the lineage note (the source's prose pointer 'build-twohalf-v127.py'
    # — untouched by the generic swap, so the fragments are identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v133' tokens)
    ("build-twohalf-v127.py", "build-twohalf-v133.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v133.py' (the source
# pointer), so those occurrences are whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "build-twohalf-v133.py"
residual_text = text.replace(whitelist, "")
residual = re.findall(r"v127|v92\.\.v132|arbit-v133|ref-arbit-v133|clone-arbit-v133|clonearbit133", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived — version-swap-only (normalize-back diff clean), zero old tokens (the lineage-note 'build-twohalf-v133.py' whitelisted; the stale clonearbit133 bumped to clonearbit139)")
