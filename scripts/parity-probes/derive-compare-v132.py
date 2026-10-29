#!/usr/bin/env python3
"""Derive compare-v132-census.py from compare-v126-census.py (the
axis-by-axis both-sides census comparator for the v132 MOBILE TWINS pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the /tmp/vlm-path EXPLICIT swap FIRST (the bare
     v126 swap cannot touch 'vlm126' — no 'v126' substring; the same
     specific-first rule the series derivation's GENERIC list follows),
     then the raw v126 -> v132 swap.
  2. History corrections against the POST-swap state: the era/ordinal
     re-pointed (the MOBILE TWINS pair's TENTH re-run -> the ELEVENTH
     re-run, the bracket extended ... -> v120 -> v126 -> v132), the
     provenance citations re-pointed at the v126 measurement (must
     reproduce the v126 census values EXACTLY, a drift re-check since
     v126; the v126-documented standing classes).
NOTE: the v126 derivation's residual loop carried a latent 'textax'
typo (never hit — its scans found zero matches); this derivation writes
the correct text[max(0, ...)] slice form, the fix noted here per the
change-management discipline."""
import sys

SRC = "scripts/parity-probes/compare-v126-census.py"
DST = "scripts/parity-probes/compare-v132-census.py"

GENERIC = [
    ("/tmp/vlm126", "/tmp/vlm132"),
    ("v126", "v132"),
]

CORRECTIONS = [
    # docstring: the era/ordinal/bracket + the provenance citation
    ('''The v132 re-run (the MOBILE TWINS pair's TENTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v132])
must reproduce the v120 census values EXACTLY (a drift re-check since v120).''',
     '''The v132 re-run (the MOBILE TWINS pair's ELEVENTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114 -> v120 -> v126 -> v132])
must reproduce the v126 census values EXACTLY (a drift re-check since v126).'''),
    # the whitelist comment's provenance citation
    ('''All delta families below are the v120-documented standing classes
# (the v132 census must reproduce the v120 values EXACTLY):''',
     '''All delta families below are the v126-documented standing classes
# (the v132 census must reproduce the v126 values EXACTLY):'''),
    # the final print's provenance citation
    ('''print("(the v120 census values reproduced EXACTLY — zero drift since v120)")''',
     '''print("(the v126 census values reproduced EXACTLY — zero drift since v126)")'''),
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

# residual old-token check — the corrected bracket "-> v120 -> v126 -> v132])"
# is the one legitimate v120 survivor (the re-run chain's middle entries)
import re
bad = []
for m in re.finditer(r"re-shot v120|TENTH re-run|since v120|reproduce the v120|v120-documented|/tmp/vlm126", text):
    ctx = text[max(0, m.start() - 45):m.end() + 45]
    if "-> v120 -> v126 -> v132])" in ctx:
        continue  # the corrected bracket
    bad.append(m.group(0))
for m in re.finditer(r"v120", text):
    ctx = text[max(0, m.start() - 60):m.end() + 60]
    if "-> v120 -> v126 -> v132])" in ctx:
        continue  # the corrected bracket
    if "v120" not in bad:
        bad.append("v120 (outside the corrected bracket)")
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
