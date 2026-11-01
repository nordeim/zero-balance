#!/usr/bin/env python3
"""Derive verify-twohalf-v139.py from verify-twohalf-v133.py (the direct
THREE-WAY extraction contract verifier — the ITEMS lineage's single
CENSUS_JS marker). Generic swap + the lineage-citation extension (the
documented contracts chain v103 -> v109 -> v115 -> v121 -> v127 -> v133,
now + v139); the digests themselves UNCHANGED (b55dcd29 — the census JS
block carries no version tokens, carried byte-identical through the
version-swap derivation)."""
import re
import sys

SRC = "scripts/parity-probes/verify-twohalf-v133.py"
DST = "scripts/parity-probes/verify-twohalf-v139.py"

SWAPS = [
    ("v133", "v139"),
    ("v103/v109/v115/v121/v127 lineage contract",
     "v103/v109/v115/v121/v127/v133 lineage contract"),
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

# normalize back and prove swap-only
back = text
for old, new in reversed(SWAPS):
    back = back.replace(new, old)
original = open(SRC, encoding="utf-8").read()
if back != original:
    print("FAIL: not a pure token swap (normalize-back mismatch)")
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)

# residual old-token check — 'v133' legitimately survives inside the
# corrected lineage-citation chain (v127 -> v133), so the scan excludes
# that single phrase before checking
residual_text = text.replace("v103/v109/v115/v121/v127/v133 lineage contract", "", 1)
residual = re.findall(r"arbit-v133|ref-arbit-v133|clone-arbit-v133", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/verify-twohalf-v139.py")
