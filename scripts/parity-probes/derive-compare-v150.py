#!/usr/bin/env python3
"""Derive compare-v150-census.py from compare-v144-census.py (the
axis-by-axis both-sides census comparator for the v150 MOBILE TWINS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the /tmp/vlm-path EXPLICIT swap FIRST (the bare
     v144 swap cannot touch 'vlm144' — no 'v144' substring; the same
     specific-first rule the series derivation's GENERIC list follows),
     then the raw v144 -> v150 swap.
  2. History corrections against the POST-swap state: the era/ordinal
     re-pointed (the MOBILE TWINS pair's THIRTEENTH re-run -> the
     FOURTEENTH re-run, the bracket extended ... -> v120 -> v126 ->
     v132 -> v138 -> v144 -> v150), the provenance citations re-pointed
     at the v144 measurement (must reproduce the v144 census values
     EXACTLY, a drift re-check since v144; the v144-documented standing
     classes)."""
import re
import sys

SRC = "scripts/parity-probes/compare-v144-census.py"
DST = "scripts/parity-probes/compare-v150-census.py"

GENERIC = [
    ("/tmp/vlm144", "/tmp/vlm150"),
    ("v144", "v150"),
]

CORRECTIONS = [
    # docstring: the era/ordinal/bracket + the provenance citation
    ('''The v150 re-run (the MOBILE TWINS pair's THIRTEENTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126 -> v132 -> v138 -> v150])
must reproduce the v138 census values EXACTLY (a drift re-check since v138).''',
     '''The v150 re-run (the MOBILE TWINS pair's FOURTEENTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126 -> v132 -> v138 -> v144 -> v150])
must reproduce the v144 census values EXACTLY (a drift re-check since v144).'''),
    # the whitelist comment's provenance citation
    ('''All delta families below are the v138-documented standing classes
# (the v150 census must reproduce the v138 values EXACTLY):''',
     '''All delta families below are the v144-documented standing classes
# (the v150 census must reproduce the v144 values EXACTLY):'''),
    # the final print's provenance citation
    ('''print("(the v138 census values reproduced EXACTLY — zero drift since v138)")''',
     '''print("(the v144 census values reproduced EXACTLY — zero drift since v144)")'''),
]

text = open(SRC, encoding="utf-8").read()
for old, new in GENERIC:
    text = text.replace(old, new)

ok = True
for old, new in CORRECTIONS:
    if old not in text:
        print(f"MISS: {old[:70]!r}")
        ok = False
        continue
    text = text.replace(old, new)
    print(f"applied: {old[:52]!r} -> corrected")

# residual old-token check — the corrected bracket "-> v120 -> v126 -> v132 -> v138 -> v144 -> v150])"
# is the one legitimate v132/v138 survivor (the re-run chain's middle entries)
bad = []
for m in re.finditer(r"re-shot v138|TENTH re-run|ELEVENTH re-run|TWELFTH re-run|THIRTEENTH re-run|since v138|reproduce the v138|v138-documented|/tmp/vlm144|arbit-v144", text):
    ctx = text[max(0, m.start() - 60):m.end() + 60]
    if "-> v120 -> v126 -> v132 -> v138 -> v144 -> v150])" in ctx:
        continue  # the corrected bracket
    bad.append(m.group(0))
for m in re.finditer(r"v138", text):
    ctx = text[max(0, m.start() - 60):m.end() + 60]
    if "-> v120 -> v126 -> v132 -> v138 -> v144 -> v150])" in ctx:
        continue  # the corrected bracket
    if "v138 (outside the corrected bracket)" not in bad:
        bad.append("v138 (outside the corrected bracket)")
if bad:
    print(f"RESIDUAL OLD TOKENS: {sorted(set(bad))}")
    ok = False
else:
    print("residual check: clean")

if not ok:
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)
sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived — line-count {'preserved' if sn == dn else f'DRIFT ({dn - sn:+d})'} ({dn + 1} lines)")
