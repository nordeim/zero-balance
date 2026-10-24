#!/usr/bin/env python3
"""Derive build-twohalf-v110.py from build-twohalf-v104.py (the same
arbit-file structure — SV_CENSUS_JS 38..190, header 1..36, ref_exec
193..224, clone_exec 227..256 — the v110 derivation is line-count-
preserving on the source arbit-v110.sh). Token swaps only; verified by
normalize-back diff (swap order: generic FIRST, then the lineage-note
fixups that must NOT be re-touched by later swaps)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v104.py"
DST = "scripts/parity-probes/build-twohalf-v110.py"

SWAPS = [
    # generic version swap FIRST (raw v104 tokens -> v110)
    ("v104", "v110"),
    # the session-name token (no 'v' prefix — untouched by the generic swap)
    ("refarbit104", "refarbit110"),
    # the TWOHALF_NOTE lesson range (single line, line 3 of the note)
    ("the v92..v103 lesson", "the v92..v109 lesson"),
    # the TWOHALF_NOTE lesson range (line-wrapped form: 'v92..v103\n# lesson')
    ("the v92..v103\n# lesson", "the v92..v109\n# lesson"),
    # the lineage note (post-generic state: 'build-twohalf-v98.py — the v110'
    # -> 'build-twohalf-v104.py — the v110'; runs LAST so no later swap
    # touches the inserted 'v104' token)
    ("Line numbers inherited verbatim from build-twohalf-v98.py — the v110",
     "Line numbers inherited verbatim from build-twohalf-v104.py — the v110"),
]

text = open(SRC, encoding="utf-8").read()
missing = []
for old, new in SWAPS:
    if old not in text:
        missing.append(old)
    text = text.replace(old, new)

# normalize back and prove version-swap-only
back = text
for old, new in reversed(SWAPS):
    back = back.replace(new, old)
original = open(SRC, encoding="utf-8").read()
if back != original:
    print("FAIL: not a pure token swap (normalize-back mismatch)")
    sys.exit(1)
if missing:
    print(f"NOTE: fragments not found in source: {missing}")

open(DST, "w", encoding="utf-8").write(text)
print(f"OK: {DST} derived ({text.count(chr(10))} lines), normalize-back clean")
