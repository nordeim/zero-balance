#!/usr/bin/env python3
"""Derive compare-v154-census.py from compare-v148-census.py (the
axis-by-axis both-sides census comparator for the v154 NETWORTH +
DRILL-DOWN pair).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the raw v148 -> v154 swap (carries the half-log
     paths /tmp/vlm154/ref-census.log + /tmp/vlm154/clone-census.log and
     the census view tags drill-arbit-1280-v154 / nw-height-1280-v154).
  2. History corrections against the POST-swap state: the provenance
     citations re-pointed at the v148 measurement (the v154 census must
     reproduce the v148 census values EXACTLY, a drift re-check since
     v148; the lineage ordinal FOURTEENTH -> FIFTEENTH; the records chain
     extended v136/v142 -> v136/v142/v148).
"""
import sys

SRC = "scripts/parity-probes/compare-v148-census.py"
DST = "scripts/parity-probes/compare-v154-census.py"

GENERIC = [
    ("/tmp/vlm148", "/tmp/vlm154"),
    ("v148", "v154"),
]

CORRECTIONS = [
    # docstring: the lineage ordinal (the family name preserved; the
    # ordinal bumped to the v154 re-run's own)
    ('''"""compare-v154-census.py — the AXIS-BY-AXIS comparison of the v154 two-half
census (the v142-era NETWORTH + DRILL-DOWN pair's FOURTEENTH re-run).''',
     '''"""compare-v154-census.py — the AXIS-BY-AXIS comparison of the v154 two-half
census (the v142-era NETWORTH + DRILL-DOWN pair's FIFTEENTH re-run).'''),
    # docstring: the records chain extended with the v148 measurement
    ('''Documented classes for this pair (the v136/v142 records):''',
     '''Documented classes for this pair (the v136/v142/v148 records):'''),
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

# residual old-token check — the era ordinal FOURTEENTH is gone; the family
# name "v142-era" survives by design (the lineage's own designation); the
# records-chain 'v148' is the corrected citation; the axis-provenance
# citations (the v56/v82 classes) keep their axis names
import re
residual_text = text.replace("the v136/v142/v148 records", "", 1)
bad = []
for m in re.finditer(r"FOURTEENTH re-run|/tmp/vlm148|compare-v148", residual_text):
    bad.append(m.group(0))
if bad:
    print(f"RESIDUAL OLD TOKENS: {sorted(set(bad))}")
    sys.exit(1)
print("residual check: clean")

sn = open(SRC, encoding="utf-8").read().count("\n")
dn = text.count("\n")
print(f"line-count {DST}: {dn + 1} lines (source {sn + 1}) — {'OK' if sn == dn else 'DRIFT'}")
sys.exit(0 if sn == dn else 1)
