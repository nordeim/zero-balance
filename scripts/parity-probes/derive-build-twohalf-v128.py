#!/usr/bin/env python3
"""Derive build-twohalf-v128.py from build-twohalf-v122.py (the same
arbit-file structure — SV_CENSUS_JS lines 38..190, header 1..36, ref_exec
193..224, clone_exec 227..256 — the v128 derivation is line-count-preserving
on the source arbit-v128.sh, itself a 262-line corrected-swap of
arbit-v122.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the explicit session-token swap + the lesson-range bump, the
lineage-note fixup LAST — the v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v122.py"
DST = "scripts/parity-probes/build-twohalf-v128.py"

SWAPS = [
    # generic version swap FIRST (raw v122 tokens -> v128)
    ("v122", "v128"),
    # the session-token swap (the v121-cycle stale-session-fix precedent:
    # 'refarbit122' carries no 'v122' substring, so the generic swap
    # cannot touch it — an EXPLICIT swap is required; the v122 builder
    # carries the REF-side session token at its ref_exec assert)
    ("refarbit122", "refarbit128"),
    # the TWOHALF_NOTE lesson range (the v122 builder carries the range
    # twice: the docstring single-line + the note itself — the bare-range
    # swap catches both forms; v92..v121 -> v92..v127, all lessons known
    # through the v127 cycle)
    ("v92..v121", "v92..v127"),
    # the lineage note (the source's prose pointer 'build-twohalf-v116.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v122' token)
    ("build-twohalf-v116.py", "build-twohalf-v122.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v122.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "build-twohalf-v122.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"v122|v92\.\.v121|refarbit122", residual_text)
if residual:
    print(f"RESIDUAL OLD TOKENS in {DST}: {sorted(set(residual))}")
    sys.exit(1)

# line-count preservation report
src_n = open(SRC, encoding="utf-8").read().count("\n")
dst_n = text.count("\n")
print(f"OK: {DST} derived — token swaps verified by normalize-back diff; zero residual")
print(f"line-count {DST}: {dst_n + 1} lines (source {src_n + 1}) — {'OK' if src_n == dst_n else 'DRIFT'}")
