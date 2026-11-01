#!/usr/bin/env python3
"""Derive verify-twohalf-v143.py from verify-twohalf-v137.py (the direct
THREE-WAY extraction contract verifier — the DASHBOARD lineage's THREE
census-block markers). Generic swap only (the v137 form carries no
lineage-citation chain — the v130 three-way form it adapted); the digests
themselves differ from the v137 cycle's by construction (the census JS
blocks' view-label tokens carry the version — the within-cycle contract
form: the digests must be byte-identical across arbit-v143.sh +
ref-arbit-v143.sh + clone-arbit-v143.sh, three-way within THIS cycle)."""
import re
import sys

SRC = "scripts/parity-probes/verify-twohalf-v137.py"
DST = "scripts/parity-probes/verify-twohalf-v143.py"

SWAPS = [
    ("v137", "v143"),
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

# residual old-token check — 'v137' legitimately survives nowhere in the
# derived verifier (the generic swap carries every token to v143)
residual = re.findall(r"arbit-v137|ref-arbit-v137|clone-arbit-v137", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/verify-twohalf-v143.py")
