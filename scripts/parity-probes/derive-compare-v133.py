#!/usr/bin/env python3
"""Derive compare-v133-census.py from compare-v127-census.py (the
axis-by-axis both-sides census comparator for the v133 ITEMS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v127 -> v133 swap (carries the half-log
     paths /tmp/ref-arbit-v133.log + /tmp/clone-arbit-v133.log).
  2. History corrections against the POST-swap state: the provenance
     citations re-pointed at the v127 measurement (the v133 census must
     reproduce the v127 census values EXACTLY, a drift re-check since
     v127; the v127-documented standing classes).
"""
import sys

SRC = "scripts/parity-probes/compare-v127-census.py"
DST = "scripts/parity-probes/compare-v133-census.py"

GENERIC = [
    ("v127", "v133"),
]

CORRECTIONS = [
    # docstring: the whitelist provenance citation
    ('''every leaf axis. Known documented classes are whitelisted (the v121
census values, reproduced exactly):''',
     '''every leaf axis. Known documented classes are whitelisted (the v127
census values, reproduced exactly):'''),
    # the QUADS whitelist comment's provenance citation
    ('''# EXACT-QUAD whitelist: (view, axis, ref value, clone value) — the
# v121-documented standing classes (the v133 census must reproduce the
# v121 values EXACTLY).''',
     '''# EXACT-QUAD whitelist: (view, axis, ref value, clone value) — the
# v127-documented standing classes (the v133 census must reproduce the
# v127 values EXACTLY).'''),
]

text = open(SRC, encoding="utf-8").read()
missing = []
for old, new in GENERIC:
    if old not in text:
        missing.append(old)
    text = text.replace(old, new)

for old, new in CORRECTIONS:
    if old not in text:
        missing.append(old[:60])
        continue
    text = text.replace(old, new)
    print(f"applied: {old[:52]!r} -> corrected")

if missing:
    print("MISSING SOURCES:", missing)
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)

# residual old-token check — the era tokens v121 outside the axis
# provenance citations (the v57/v70b-lineage classes keep their axis
# names; only the two provenance citations were era tokens)
import re
bad = []
for m in re.finditer(r"v121|/tmp/ref-arbit-v127|/tmp/clone-arbit-v127", text):
    bad.append(m.group(0))
if bad:
    print(f"RESIDUAL OLD TOKENS: {sorted(set(bad))}")
    sys.exit(1)
print("residual check: clean")

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived — line-count {'preserved' if sn == dn else f'DRIFT ({dn - sn:+d})'} ({dn + 1} lines)")
