#!/usr/bin/env python3
"""Derive build-twohalf-v127.py from build-twohalf-v121.py (the same
arbit-file structure — CENSUS_JS lines 22..214, header 1..21, ref_exec
216..250 — the v127 derivation is line-count-preserving on the source
arbit-v127.sh, itself a 285-line corrected-swap of arbit-v121.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the lesson-range bump, the lineage-note fixup LAST — the
v110 swap-order rule)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v121.py"
DST = "scripts/parity-probes/build-twohalf-v127.py"

SWAPS = [
    # generic version swap FIRST (raw v121 tokens -> v127)
    ("v121", "v127"),
    # the session-token swap (the v121-cycle stale-session-fix precedent:
    # 'clonearbit121' carries no 'v121' substring, so the generic swap
    # cannot touch it — an EXPLICIT swap is required, the same form the
    # v121 cycle applied to its inherited clonearbit109)
    ("clonearbit121", "clonearbit127"),
    # the TWOHALF_NOTE lesson range (the v121 builder carries the range
    # twice: the docstring single-line + the note itself — the bare-range
    # swap catches both forms)
    ("v92..v120", "v92..v126"),
    # the lineage note (the source's prose pointer 'build-twohalf-v115.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v121' token)
    ("build-twohalf-v115.py", "build-twohalf-v121.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v121.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "build-twohalf-v121.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"v121|v92\.\.v120|clonearbit121", residual_text)
if residual:
    print(f"RESIDUAL OLD TOKENS in {DST}: {sorted(set(residual))}")
    sys.exit(1)
print(f"OK: {DST} derived — token swaps verified by normalize-back diff; zero residual")
