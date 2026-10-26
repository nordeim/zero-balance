#!/usr/bin/env python3
"""Derive build-twohalf-v122.py from build-twohalf-v116.py (the same
arbit-file structure — SV_CENSUS_JS lines 38..190, header 1..36, ref_exec
193..224, clone_exec 227..256 — the v122 derivation is
line-count-preserving on the source arbit-v122.sh, itself a 262-line
corrected-swap of arbit-v116.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the stale-session fix, the lesson-range bump, the lineage-note
fixup LAST — the v110 swap-order rule).
NOTE the builder's ref_exec startswith assertion carries the BARE session
token 'refarbit116' — a no-'v'-prefix token the generic swap CANNOT touch
(the v116 cycle's own documented repair class: its builder fixed the v110
builder's stale 'refarbit110' explicitly; the same explicit fix applied in
this lineage, 'refarbit116' -> 'refarbit122' — the session name's purpose
preserved, the version now correct).
The census block (SV_CENSUS_JS, 153 lines) is version-free (the block's
own provenance tokens are the v51/v54/v58/v64/v65/v98 historical
references — carried verbatim), so the md5 line-block contract holds
across the halves at the inherited value [891ab9b6 — documented in
remediation-plan-v116.md]."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v116.py"
DST = "scripts/parity-probes/build-twohalf-v122.py"

SWAPS = [
    # generic version swap FIRST (raw v116 tokens -> v122)
    ("v116", "v122"),
    # the stale ref session token (the builder's ref_exec startswith
    # assertion carries the no-'v'-prefix bare token — the generic swap
    # cannot touch it; fixed explicitly, the v116-lineage repair class)
    ("refarbit116", "refarbit122"),
    # the TWOHALF_NOTE lesson range (the v116 builder carries the range
    # twice: the docstring + the note itself — the bare-range swap catches
    # both occurrences)
    ("v92..v115", "v92..v121"),
    # the lineage note (the source's prose pointer 'build-twohalf-v110.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v116' token)
    ("build-twohalf-v110.py", "build-twohalf-v116.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v116.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115/v116/v117/v118/v119/v120/v121 residual-precedent discipline).
# The md5-provenance tokens (891ab9b6, remediation-plan-v116.md) are
# LEGIT verbatim carries — deliberately not scanned.
import re
whitelist = "build-twohalf-v116.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"refarbit116|v92\.\.v115|arbit-v116|ref-arbit-v116|clone-arbit-v116", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived ({text.count(chr(10))} newlines), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/build-twohalf-v122.py")
