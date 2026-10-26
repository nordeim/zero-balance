#!/usr/bin/env python3
"""Derive compare-v123-census.py from compare-v117-census.py (the
login+calculator axis-by-axis comparator — the same documented-class
whitelists, the v117 census values now the standing classes the v123
census must reproduce EXACTLY).
Generic swap FIRST (v117 -> v123), then the census-era corrections (the
provenance citations re-pointed from the v111 measurement to the v117
measurement — the immediately-previous census, the v122 comparator's
own precedent: its v116 form cites the v104/v110 censuses, the v122 form
the v116). Verified by normalize-back diff; line-count-preserving."""
import sys

SRC = "scripts/parity-probes/compare-v117-census.py"
DST = "scripts/parity-probes/compare-v123-census.py"

SWAPS = [
    # generic version swap FIRST (v117 tokens -> v123, incl. the log paths;
    # NOTE /tmp/vlm117 carries no 'v117' substring — the v-prefix-less path
    # needs its own explicit swap, the same specific-first rule the series
    # derivation's GENERIC list follows)
    ("/tmp/vlm117", "/tmp/vlm123"),
    ("v117", "v123"),
    # census-era corrections (the provenance citations — within-line forms)
    ("the v111-era LOGIN + CALCULATOR pair's NINTH re-run",
     "the v117-era LOGIN + CALCULATOR pair's TENTH re-run"),
    ("the v99/v105/v111 records", "the v105/v111/v117 records"),
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
residual = re.findall(r"v111-era|NINTH re-run|v99/v105/v111|arbit-v117|vlm117", text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens")
