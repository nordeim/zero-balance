#!/usr/bin/env python3
"""Derive build-twohalf-v134.py from build-twohalf-v128.py (the same
arbit-file structure — SV_CENSUS_JS lines 38..190, header 1..36, ref_exec
193..224, clone_exec 227..256 — the v134 derivation is line-count-
preserving on the source arbit-v134.sh, itself a 262-line corrected-swap
of arbit-v128.sh).
Token swaps only; verified by normalize-back diff (swap order: the generic
swap FIRST, then the lesson-range bump, the lineage-note fixup LAST — the
v110 swap-order rule).
NOTE: unlike the v126-lineage builder (which embedded a stale clone_login
literal — the v121/v132 stale-session-fix precedent), the v128-lineage
builder extracts ALL blocks (census + header + ref_exec + clone_exec)
from the source arbit file at RUN time — the session tokens
(refarbit134/clonearbit134) arrive already-corrected via the derived
arbit-v134.sh, so NO stale-session fix is needed this lineage."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v128.py"
DST = "scripts/parity-probes/build-twohalf-v134.py"

SWAPS = [
    # the session-token family FIRST (no 'v' prefix — untouched by the
    # generic swap; the builder's ref_exec assert carries 'refarbit128')
    ("refarbit128", "refarbit134"),
    # generic version swap (raw v128 tokens -> v134; carries the SRC/output
    # paths + the echo lines)
    ("v128", "v134"),
    # the TWOHALF_NOTE lesson range (the v128 builder carries the range
    # twice: the docstring + the note itself — the BARE range token catches
    # both forms, the v131 lesson)
    ("v92..v127", "v92..v133"),
    # the lineage note (the source's prose pointer 'build-twohalf-v122.py'
    # — untouched by the generic swap, so the fragments are identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v128' tokens)
    ("build-twohalf-v122.py", "build-twohalf-v128.py"),
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

# normalize back and prove version-swap-only
back = text
for old, new in reversed(SWAPS):
    back = back.replace(new, old)
original = open(SRC, encoding="utf-8").read()
if back != original:
    print("FAIL: not a pure token swap (normalize-back mismatch)")
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)

# residual old-token check on the derived builder — the lineage-note
# fixup deliberately re-inserts 'build-twohalf-v128.py' (the source
# pointer), so those occurrences are whitelisted before the scan
# (the v115/v116/v117/v118 residual-precedent discipline).
import re
whitelist = "build-twohalf-v128.py"
residual_text = text.replace(whitelist, "")
residual = re.findall(r"v122|v92\.\.v127|arbit-v128|ref-arbit-v128|clone-arbit-v128|clonearbit128|refarbit128", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived — version-swap-only (normalize-back diff clean), zero old tokens (the lineage-note 'build-twohalf-v128.py' whitelisted)")
