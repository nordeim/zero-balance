#!/usr/bin/env python3
"""Derive verify-twohalf-v138.py from verify-twohalf-v132.py (the direct
THREE-WAY extraction contract verifier — the MOBILE TWINS lineage's
NW_CENSUS/DASH_CENSUS marker names). Generic swap + the lineage-citation
extension (the documented contracts chain v102 -> v108 -> v114 -> v120 ->
v126 -> v132, now + v138); the digests themselves UNCHANGED (82cf8a43 /
85e4ec7e — the census JS blocks carry no version tokens, carried
byte-identical through the version-swap derivation)."""
import re
import sys

SRC = "scripts/parity-probes/verify-twohalf-v132.py"
DST = "scripts/parity-probes/verify-twohalf-v138.py"

SWAPS = [
    ("v132", "v138"),
    ("v102/v108/v114/v120/v126 lineage contracts",
     "v102/v108/v114/v120/v126/v132 lineage contracts"),
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

# residual old-token check — 'v132' legitimately survives inside the
# corrected lineage-citation chain (v126 -> v132), so the scan excludes
# that single phrase before checking
residual_text = text.replace("v102/v108/v114/v120/v126/v132 lineage contracts", "", 1)
residual = re.findall(r"arbit-v132|ref-arbit-v132|clone-arbit-v132", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/verify-twohalf-v138.py")
