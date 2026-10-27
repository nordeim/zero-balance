#!/usr/bin/env python3
"""Derive compare-v124-census.py from compare-v118-census.py (the
networth + drill-down axis-by-axis comparator — the same documented-class
whitelists, the v118 census values now the standing classes the v124
census must reproduce EXACTLY).
Generic swap FIRST (v118 -> v124), then the census-era corrections (the
provenance citations re-pointed from the v112 measurement to the v118
measurement — the immediately-previous census, the v123 comparator's
own precedent: its v117 form cites the v105/v111/v117 censuses, the v124
form the v112/v118). Verified by normalize-back diff; line-count-
preserving."""
import sys

SRC = "scripts/parity-probes/compare-v118-census.py"
DST = "scripts/parity-probes/compare-v124-census.py"

SWAPS = [
    # generic version swap FIRST (v118 tokens -> v124, incl. the log paths;
    # NOTE /tmp/vlm118 carries no 'v118' substring — the v-prefix-less path
    # needs its own explicit swap, the same specific-first rule the series
    # derivation's GENERIC list follows)
    ("/tmp/vlm118", "/tmp/vlm124"),
    ("v118", "v124"),
    # census-era corrections (the provenance citations — within-line forms)
    ("the v112-era NETWORTH + DRILL-DOWN pair's NINTH re-run",
     "the v118-era NETWORTH + DRILL-DOWN pair's TENTH re-run"),
    ("the v106/v112 records", "the v112/v118 records"),
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

import re
residual = re.findall(r"v112-era|NINTH re-run|v106/v112|arbit-v118|vlm118", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
