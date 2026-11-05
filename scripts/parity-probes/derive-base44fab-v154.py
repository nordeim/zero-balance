#!/usr/bin/env python3
"""Derive base44-fab-arbit-v154.sh from base44-fab-arbit-v148.sh (the
ONE-SHOT both-sides FAB arbitration for the v154 networth+drill-down
pair's FAB flags — the NETWORTH + DASHBOARD drill-down surfaces at
desktop 1280x800, the v148 single-surface-pair standing disproof form).
Swap-only: reffab148->reffab154, clonefab148->clonefab154, v148->v154.
Verified by normalize-back diff."""
import re
import sys

SRC = "scripts/parity-probes/base44-fab-arbit-v148.sh"
DST = "scripts/parity-probes/base44-fab-arbit-v154.sh"

SWAPS = [
    ("reffab148", "reffab154"),
    ("clonefab148", "clonefab154"),
    ("v148", "v154"),
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

residual = re.findall(r"reffab148|clonefab148|v148", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
