#!/usr/bin/env python3
"""Derive verify-twohalf-v152.py from verify-twohalf-v146.py (the direct
three-way md5 extraction verifier for the v152 SAVINGS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v146 -> v152 swap (carries the three file
     paths arbit-v152.sh + ref-arbit-v152.sh + clone-arbit-v152.sh).
  2. History corrections against the POST-swap state: the lineage-citation
     extension "v122/v128/v134/v140 lineage contract" ->
     "v122/v128/v134/v140/v146 lineage contract" (the v151 form extended
     its own citation the same way); the digest itself UNCHANGED —
     SV_CENSUS_JS 891ab9b6, the cycle-invariant savings-lineage contract
     (the census JS block carries no version tokens).
"""
import sys

SRC = "scripts/parity-probes/verify-twohalf-v146.py"
DST = "scripts/parity-probes/verify-twohalf-v152.py"

GENERIC = [
    ("v146", "v152"),
]

CORRECTIONS = [
    ('''they must equal the documented v122/v128/v134/v140 lineage contract (891ab9b6)
VERBATIM.''',
     '''they must equal the documented v122/v128/v134/v140/v146 lineage contract (891ab9b6)
VERBATIM.'''),
]

text = open(SRC, encoding="utf-8").read()
missing = []
for old, new in GENERIC:
    if old not in text:
        missing.append(old)
    text = text.replace(old, new)

for old, new in CORRECTIONS:
    if old not in text:
        missing.append(old[:60])
        continue
    text = text.replace(old, new)
    print(f"applied correction: {old[:52]!r} -> corrected")

if missing:
    print("MISSING SOURCES:", missing)
    sys.exit(1)

# normalize back and prove swap-only (the CORRECTIONS reversed FIRST —
# their new fragments carry a v146 token that the generic reverse must
# not corrupt; the generic reverse runs LAST)
back = text
for old, new in reversed(CORRECTIONS):
    back = back.replace(new, old)
for old, new in reversed(GENERIC):
    back = back.replace(new, old)
original = open(SRC, encoding="utf-8").read()
if back != original:
    print("FAIL: not a pure token swap (normalize-back mismatch)")
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)

import re
# the only legitimate v146 survivor is the extended lineage citation
residual = re.findall(r"v146", text)
if len(residual) != 1:
    print(f"FAIL: {DST} v146 token count {len(residual)} != 1 (the lineage citation)")
    sys.exit(1)

print(f"derived {DST} (generic swap + lineage-citation extension; normalize-back clean)")
