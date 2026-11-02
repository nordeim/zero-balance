#!/usr/bin/env python3
"""Derive verify-twohalf-v146.py from verify-twohalf-v140.py (the direct
THREE-WAY extraction contract verifier — the SAVINGS lineage's single
CENSUS_JS marker). Generic swap + the lineage-citation extension (the
documented contracts chain v122 -> v128 -> v134 -> v140, now + v146); the
digests themselves UNCHANGED (891ab9b6 — the census JS block carries no
version tokens, carried byte-identical through the version-swap
derivation)."""
import re
import sys

SRC = "scripts/parity-probes/verify-twohalf-v140.py"
DST = "scripts/parity-probes/verify-twohalf-v146.py"

SWAPS = [
    ("v140", "v146"),
    ("v122/v128/v134 lineage contract",
     "v122/v128/v134/v140 lineage contract"),
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

# residual old-token check — 'v134' and 'v140' legitimately survive inside
# the corrected lineage-citation chain (v128 -> v134 -> v140), so the scan
# excludes that single phrase before checking
residual_text = text.replace("v122/v128/v134/v140 lineage contract", "", 1)
residual = re.findall(r"arbit-v140|ref-arbit-v140|clone-arbit-v140", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/verify-twohalf-v146.py")
