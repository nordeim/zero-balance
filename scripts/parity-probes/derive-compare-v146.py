#!/usr/bin/env python3
"""Derive compare-v146-census.py from compare-v140-census.py (the
axis-by-axis both-sides census comparator for the v146 SAVINGS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v140 -> v146 swap (carries the half-log
     paths /tmp/ref-arbit-v146.log + /tmp/clone-arbit-v146.log).
  2. History corrections against the POST-swap state: the provenance
     citations re-pointed at the v140 measurement (the v146 census must
     reproduce the v140 census values EXACTLY, a drift re-check since
     v140; the v140-documented standing classes).
"""
import sys

SRC = "scripts/parity-probes/compare-v140-census.py"
DST = "scripts/parity-probes/compare-v146-census.py"

GENERIC = [
    ("v140", "v146"),
]

CORRECTIONS = [
    # docstring: the whitelist provenance citation
    ('''every leaf
axis. Known documented classes are whitelisted (the v134 census values,
reproduced exactly):''',
     '''every leaf
axis. Known documented classes are whitelisted (the v140 census values,
reproduced exactly):'''),
    # the QUADS whitelist comment's provenance citation
    ('''# EXACT-QUAD whitelist: (axis, ref value, clone value) — the v134
# documented standing classes (the v146 census must reproduce the
# v134 values EXACTLY).''',
     '''# EXACT-QUAD whitelist: (axis, ref value, clone value) — the v140
# documented standing classes (the v146 census must reproduce the
# v140 values EXACTLY).'''),
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

# residual old-token check — the era tokens v134 outside the axis
# provenance citations (the v57/v70b-lineage classes keep their axis
# names; only the two provenance citations were era tokens)
import re
bad = []
for m in re.finditer(r"v134|/tmp/ref-arbit-v140|/tmp/clone-arbit-v140", text):
    bad.append(m.group(0))
if bad:
    print(f"RESIDUAL OLD TOKENS: {sorted(set(bad))}")
    sys.exit(1)
print("residual check: clean")

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"line-count {DST}: {dn + 1} lines (source {sn + 1}) — {'OK' if sn == dn else 'DRIFT'}")
sys.exit(0 if sn == dn else 1)
