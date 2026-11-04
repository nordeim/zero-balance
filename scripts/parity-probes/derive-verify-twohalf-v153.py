#!/usr/bin/env python3
"""Derive verify-twohalf-v153.py from verify-twohalf-v147.py (the direct
THREE-WAY extraction contract verifier — the LOGIN+CALC lineage's TWO
census-block markers). Generic swap + the lineage-citation extension (the
documented contracts chain v124..v146, now + v152); the digests
themselves UNCHANGED (e1092d12d06677a4 + 9e5a52d2ab0f2ab9 — the census
JS blocks carry no version tokens, carried byte-identical through the
version-swap derivation)."""
import re
import sys

SRC = "scripts/parity-probes/verify-twohalf-v147.py"
DST = "scripts/parity-probes/verify-twohalf-v153.py"

SWAPS = [
    ("v147", "v153"),
    ("v124..v146 form", "v124..v152 form"),
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

# residual old-token check — 'v147' legitimately survives nowhere in the
# derived verifier (the generic swap carries every token to v153)
residual = re.findall(r"arbit-v147|ref-arbit-v147|clone-arbit-v147|v124\.\.v146", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/verify-twohalf-v153.py")
