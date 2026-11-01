#!/usr/bin/env python3
"""Derive verify-twohalf-v142.py from verify-twohalf-v136.py (the direct
THREE-WAY extraction contract verifier — the NETWORTH+DRILL-DOWN lineage's
TWO census-block markers). Generic swap + the lineage-citation extension (the
documented contracts chain v124/v125/v126/v127/v128/v129, now + v130/v136 —
the networth lineage's own prior verify records); the digests themselves
differ from the v136 cycle's by construction (the census JS blocks' view-label
tokens carry the version — 'drill-arbit-1280-v142' / 'nw-height-1280-v142' —
the within-cycle contract form: the digests must be byte-identical across
arbit-v142.sh + ref-arbit-v142.sh + clone-arbit-v142.sh, three-way within THIS
cycle)."""
import re
import sys

SRC = "scripts/parity-probes/verify-twohalf-v136.py"
DST = "scripts/parity-probes/verify-twohalf-v142.py"

SWAPS = [
    ("v136", "v142"),
    # the lineage-citation chain extension (the v136 form cites the
    # v124..v129 records; the v142 form extends with the networth
    # lineage's own v130/v136 measurements)
    ("the v124/v125/v126/v127/v128/v129 — carried forward",
     "the v124/v125/v126/v127/v128/v129/v130/v136 — carried forward"),
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

# residual old-token check — 'v136' legitimately survives nowhere in the
# derived verifier (the generic swap carries every token to v142)
residual = re.findall(r"arbit-v136|ref-arbit-v136|clone-arbit-v136", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/verify-twohalf-v142.py")
