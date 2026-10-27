#!/usr/bin/env python3
"""Derive compare-v126-census.py from compare-v120-census.py (the
axis-by-axis both-sides census comparator for the v126 MOBILE TWINS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the /tmp/vlm-path EXPLICIT swap FIRST (the bare
     v120 swap cannot touch 'vlm120' — no 'v120' substring; the same
     specific-first rule the series derivation's GENERIC list follows),
     then the raw v120 -> v126 swap.
  2. History corrections against the POST-swap state: the era/ordinal
     re-pointed (the MOBILE TWINS pair's NINTH re-run -> the TENTH
     re-run, the bracket extended ... -> v114 -> v120 -> v126), the
     provenance citations re-pointed at the v120 measurement (must
     reproduce the v120 census values EXACTLY, a drift re-check since
     v120; the v120-documented standing classes).
"""
import sys

SRC = "scripts/parity-probes/compare-v120-census.py"
DST = "scripts/parity-probes/compare-v126-census.py"

GENERIC = [
    ("/tmp/vlm120", "/tmp/vlm126"),
    ("v120", "v126"),
]

CORRECTIONS = [
    # docstring: the era/ordinal/bracket + the provenance citation
    ('''The v126 re-run (the MOBILE TWINS pair's NINTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v126])
must reproduce the v114 census values EXACTLY (a drift re-check since v114).''',
     '''The v126 re-run (the MOBILE TWINS pair's TENTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126])
must reproduce the v120 census values EXACTLY (a drift re-check since v120).'''),
    # the whitelist comment's provenance citation
    ('''All delta families below are the v114-documented standing classes
# (the v126 census must reproduce the v114 values EXACTLY):''',
     '''All delta families below are the v120-documented standing classes
# (the v126 census must reproduce the v120 values EXACTLY):'''),
    # the final print's provenance citation
    ('''print("(the v114 census values reproduced EXACTLY — zero drift since v114)")''',
     '''print("(the v120 census values reproduced EXACTLY — zero drift since v120)")'''),
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

# residual old-token check — the corrected bracket "-> v114 -> v120 -> v126])"
# is the one legitimate v114 survivor (the re-run chain's middle entries)
import re
bad = []
for m in re.finditer(r"re-shot v114|NINTH re-run|since v114|reproduce the v114|v114-documented|/tmp/vlm120", text):
    ctx = text[max(0, m.start() - 45):m.end() + 45]
    if "-> v114 -> v120 -> v126])" in ctx:
        continue  # the corrected bracket
    bad.append(m.group(0))
for m in re.finditer(r"v114", text):
    ctx = text[max(0, m.start() - 60):m.end() + 60]
    if "-> v114 -> v120 -> v126])" in ctx:
        continue  # the corrected bracket
    if "v114" not in bad:
        bad.append("v114 (outside the corrected bracket)")
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
