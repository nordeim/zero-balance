#!/usr/bin/env python3
"""Derive compare-v134-census.py from compare-v128-census.py (the
axis-by-axis both-sides census comparator for the v134 SAVINGS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v128 -> v134 swap (carries the half-log
     paths /tmp/ref-arbit-v134.log + /tmp/clone-arbit-v134.log).
  2. History corrections against the POST-swap state: the provenance
     citations re-pointed at the v128 measurement (the v134 census must
     reproduce the v128 census values EXACTLY, a drift re-check since
     v128; the v128-documented standing classes).
"""
import sys

SRC = "scripts/parity-probes/compare-v128-census.py"
DST = "scripts/parity-probes/compare-v134-census.py"

GENERIC = [
    ("v128", "v134"),
]

CORRECTIONS = [
    # docstring: the whitelist provenance citation (carries no v128 token —
    # identical pre/post swap)
    ('''axis. Known documented classes are whitelisted (the v122 census values,
reproduced exactly):''',
     '''axis. Known documented classes are whitelisted (the v128 census values,
reproduced exactly):'''),
    # the QUADS whitelist comment's provenance citation (the middle line's
    # 'v128 census' is the POST-swap form; the outer v122 tokens are
    # pre/post-swap identical)
    ('''# EXACT-QUAD whitelist: (axis, ref value, clone value) — the v122
# documented standing classes (the v134 census must reproduce the
# v122 values EXACTLY).''',
     '''# EXACT-QUAD whitelist: (axis, ref value, clone value) — the v128
# documented standing classes (the v134 census must reproduce the
# v128 values EXACTLY).'''),
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

# residual old-token check — the era tokens v122 outside the axis
# provenance citations (the v57/v70b-lineage classes keep their axis
# names; only the two provenance citations were era tokens)
import re
bad = []
for m in re.finditer(r"v122|/tmp/ref-arbit-v128|/tmp/clone-arbit-v128", text):
    bad.append(m.group(0))
if bad:
    print(f"RESIDUAL OLD TOKENS: {sorted(set(bad))}")
    sys.exit(1)
print("residual check: clean")

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived — line-count {'preserved' if sn == dn else f'DRIFT ({dn - sn:+d})'} ({dn + 1} lines)")
