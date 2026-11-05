#!/usr/bin/env python3
"""Derive verify-twohalf-v154.py from verify-twohalf-v148.py (the direct
THREE-WAY extraction contract verifier — the NETWORTH+DRILL-DOWN
lineage's TWO census-block markers). Generic swap + the lineage-citation
extension (the documented contracts chain v124..v142, now + v148); the
digests themselves UNCHANGED (the census JS blocks carry no version
tokens, carried byte-identical through the version-swap derivation)."""
import re
import sys

SRC = "scripts/parity-probes/verify-twohalf-v148.py"
DST = "scripts/parity-probes/verify-twohalf-v154.py"

SWAPS = [
    ("v148", "v154"),
    ("v130/v136/v142 — carried forward", "v130/v136/v142/v148 — carried forward"),
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

# residual old-token check — 'v148' legitimately survives ONLY in the
# corrected citation chain (whitelisted before the scan); every other
# token carried to v154 by the generic swap
residual_text = text.replace("v130/v136/v142/v148 — carried forward", "", 1)
residual = re.findall(r"arbit-v148|ref-arbit-v148|clone-arbit-v148|/tmp/vlm148", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens (the citation chain extended v130/v136/v142 -> v130/v136/v142/v148)")
print("run it now: python3 scripts/parity-probes/verify-twohalf-v154.py")
