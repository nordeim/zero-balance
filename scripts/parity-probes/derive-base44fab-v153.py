#!/usr/bin/env python3
"""Derive base44-fab-arbit-v153.sh from base44-fab-arbit-v147.sh (the
ONE-SHOT both-sides FAB arbitration for the v153 login pair's FAB flag —
the /login surface at desktop 1280x800, the v147 single-surface standing
disproof form). Swap-only: reffab147->reffab153, clonefab147->clonefab153,
v147->v153. Verified by normalize-back diff."""
import re
import sys

SRC = "scripts/parity-probes/base44-fab-arbit-v147.sh"
DST = "scripts/parity-probes/base44-fab-arbit-v153.sh"

SWAPS = [
    ("reffab147", "reffab153"),
    ("clonefab147", "clonefab153"),
    ("v147", "v153"),
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

residual = re.findall(r"reffab147|clonefab147|v147", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
