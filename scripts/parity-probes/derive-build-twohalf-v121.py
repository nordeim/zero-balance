#!/usr/bin/env python3
"""Derive build-twohalf-v121.py from build-twohalf-v115.py (the same
arbit-file structure — CENSUS_JS lines 22..214, header 1..21, ref_exec
215..250, the clone side env-injection — the v121 derivation is
line-count-preserving on the source arbit-v121.sh, itself a 285-line
corrected-swap of arbit-v115.sh).
Token swaps only; verified by normalize-back diff (swap order: generic
FIRST, then the stale-session fix, the lesson-range bump, the lineage-note
fixup LAST — the v110 swap-order rule).
NOTE the v115 builder's clone_login carried the STALE session token
'clonearbit109' (inherited verbatim from build-twohalf-v109.py — the
same quirk class as the v114 builder's 'clonearbit108', fixed in the v120
lineage): fixed to 'clonearbit121' in this lineage (the token's purpose —
a session name distinct from the ref half's — preserved, the version now
correct).
The md5-provenance comment (the v103/v109 census block verbatim
[b55dcd29 — documented in remediation-plan-v109.md]) is carried VERBATIM
(the v120 builder's 'remediation-plan-v102.md' precedent — the historical
pointer to where the contract is documented)."""
import sys

SRC = "scripts/parity-probes/build-twohalf-v115.py"
DST = "scripts/parity-probes/build-twohalf-v121.py"

SWAPS = [
    # generic version swap FIRST (raw v115 tokens -> v121)
    ("v115", "v121"),
    # the stale clone session token (the v115 builder inherited it from
    # the v109 builder unbumped — the v120-lineage fix class; fixed here)
    ("clonearbit109", "clonearbit121"),
    # the TWOHALF_NOTE lesson range (the v115 builder carries the range
    # twice: the docstring + the note itself — the bare-range swap catches
    # both occurrences)
    ("v92..v114", "v92..v120"),
    # the lineage note (the source's prose pointer 'build-twohalf-v109.py'
    # — untouched by the generic swap, so the fragment is identical pre/post
    # swap; runs LAST so no later swap touches the inserted 'v115' token)
    ("build-twohalf-v109.py", "build-twohalf-v115.py"),
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
# fixup deliberately re-inserts 'build-twohalf-v115.py' (the source
# pointer), so that single occurrence is whitelisted before the scan
# (the v115/v116/v117/v118/v119/v120 residual-precedent discipline).
# The md5-provenance tokens (v103/v109, remediation-plan-v109.md,
# b55dcd29) are LEGIT verbatim carries — deliberately not scanned.
import re
whitelist = "build-twohalf-v115.py"
residual_text = text.replace(whitelist, "", 1)
residual = re.findall(r"clonearbit109|v92\.\.v114|arbit-v115|ref-arbit-v115|clone-arbit-v115", residual_text)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

print(f"OK: {DST} derived ({text.count(chr(10))} newlines), normalize-back clean, zero old tokens")
print("run it now: python3 scripts/parity-probes/build-twohalf-v121.py")
