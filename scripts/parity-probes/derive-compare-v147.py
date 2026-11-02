#!/usr/bin/env python3
"""Derive compare-v147-census.py from compare-v141-census.py (the
axis-by-axis both-sides census comparator for the v147 LOGIN + CALCULATOR
pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v141 -> v147 swap (carries the half-log
     paths /tmp/vlm147/ref-arbit-full.log + /tmp/vlm147/clone-arbit-full.log).
  2. History corrections against the POST-swap state: the provenance
     citations re-pointed at the v141 measurement (the v147 census must
     reproduce the v141 census values EXACTLY, a drift re-check since
     v141; the lineage ordinal THIRTEENTH -> FOURTEENTH; the records chain
     extended v105/v111/v117/v123/v129/v135 -> +v141).
"""
import sys

SRC = "scripts/parity-probes/compare-v141-census.py"
DST = "scripts/parity-probes/compare-v147-census.py"

GENERIC = [
    ("/tmp/vlm141", "/tmp/vlm147"),
    ("v141", "v147"),
]

CORRECTIONS = [
    # docstring: the lineage ordinal (the family name preserved; the
    # ordinal bumped to the v147 re-run's own)
    ('''"""compare-v147-census.py — the AXIS-BY-AXIS comparison of the v147 two-half
census (the v129-era LOGIN + CALCULATOR pair's THIRTEENTH re-run).''',
     '''"""compare-v147-census.py — the AXIS-BY-AXIS comparison of the v147 two-half
census (the v129-era LOGIN + CALCULATOR pair's FOURTEENTH re-run).'''),
    # docstring: the records chain extended with the v141 measurement
    ('''Documented classes for this pair (the v105/v111/v117/v123/v129/v135 records + the v45/v10
construct conventions):''',
     '''Documented classes for this pair (the v105/v111/v117/v123/v129/v135/v141 records + the v45/v10
construct conventions):'''),
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

# residual old-token check — the era ordinal THIRTEENTH is gone; the family
# name "v129-era" survives by design (the lineage's own designation); the
# records-chain 'v141' is the corrected citation; the axis-provenance
# citations (the v99/v87/v45/v10/v7 classes) keep their axis names
import re
residual_text = text.replace("the v105/v111/v117/v123/v129/v135/v141 records", "", 1)
bad = []
for m in re.finditer(r"THIRTEENTH re-run|/tmp/vlm141|compare-v141", residual_text):
    bad.append(m.group(0))
if bad:
    print(f"RESIDUAL OLD TOKENS: {sorted(set(bad))}")
    sys.exit(1)
print("residual check: clean")

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"line-count {DST}: {dn + 1} lines (source {sn + 1}) — {'OK' if sn == dn else 'DRIFT'}")
sys.exit(0 if sn == dn else 1)
