#!/usr/bin/env python3
"""Derive base44-fab-arbit-v155.sh from base44-fab-arbit-v149.sh (the
ONE-SHOT both-sides FAB arbitration for the v155 dashboard pair's FAB
claims — the / dashboard surface at desktop 1280x800, logged-in).
Generic swap FIRST (reffab149->reffab155, clonefab149->clonefab155,
v149->v155 — the code census blocks + execution paths are pure swap),
then the header narrative corrected from the v149 no-claims standing
form to the v155 claims form (the v149 derivation's own precedent, in
the opposite direction — the v149 header was rewritten FROM the v143
claims form TO the no-claims form; the v155 cycle raised the FAB claim
in BOTH passes, ref-only, on the pair's own dashboard surface).
Verification: the post-swap buffer normalizes back cleanly BEFORE the
header correction; after the correction the final file differs from the
source ONLY in the swap lines + the header claims block."""
import re
import sys

SRC = "scripts/parity-probes/base44-fab-arbit-v149.sh"
DST = "scripts/parity-probes/base44-fab-arbit-v155.sh"

SWAPS = [
    ("reffab149", "reffab155"),
    ("clonefab149", "clonefab155"),
    ("v149", "v155"),
]

# The v149 header's no-claims block, in its POST-swap state (the generic
# swap relabels the verdict line 'the v149 VLM verdict' -> 'the v155 VLM
# verdict' and corrupts the chain's trailing 'v149' -> 'v155').
OLD_HEADER = """#   NO FAB claim raised this cycle (the v155 VLM verdict IDENTICAL x2 with
#   ZERO style flags — the cleanest pair form); the disproof runs as the
#   STANDING re-confirmation (the v97/v103/v108/v109/v115/v120/v123/v127/
#   v129/v135/v141/v142/v155/v148 standing disproof form: the FAB never
#   renders in the app DOM on EITHER side — it lives in the reference's
#   platform iframe chrome, outside the queryable body DOM).
"""

NEW_HEADER = """#   THE v155 FAB claims (the / dashboard surface at 1280, logged-in —
#   claimed in BOTH passes, one direction [ref-only]: the VLM pass 1:
#   "Image 1 shows an 'Edit with Base 44' floating badge; absent in
#   image 2" + the VLM pass 2: "The 'Edit with Base 44' floating badge
#   (bottom right of Budget Guidelines) appears only in image 1
#   (reference), not image 2" — the platform-chrome class; the
#   v97/v103/v108/v109/v115/v120/v123/v127/v129/v135/v141/v142/v143/
#   v148/v149/v154/v155 standing disproof form: the FAB never renders in
#   the app DOM on EITHER side — it lives in the reference's platform
#   iframe chrome, outside the queryable body DOM).
"""

text = open(SRC, encoding="utf-8").read()
missing = []
for old, new in SWAPS:
    if old not in text:
        missing.append(old)
    text = text.replace(old, new)
if missing:
    print("MISSING SOURCES:", missing)
    sys.exit(1)

# normalize back and prove swap-only BEFORE the header correction
back = text
for old, new in reversed(SWAPS):
    back = back.replace(new, old)
original = open(SRC, encoding="utf-8").read()
if back != original:
    print("FAIL: not a pure token swap (normalize-back mismatch)")
    sys.exit(1)

# the header narrative correction (the claims form)
if OLD_HEADER not in text:
    print("FAIL: the post-swap no-claims header block not found verbatim")
    sys.exit(1)
text = text.replace(OLD_HEADER, NEW_HEADER)

open(DST, "w", encoding="utf-8").write(text)

# residual old-token check (the corrected header's disproof chain carries
# the historical v143/v148/v149/v154 entries + the new v155 — provenance,
# not stale tokens; the code blocks must carry no v149 tokens)
residual = re.findall(r"reffab149|clonefab149|no-claims|NO FAB claim", text)
# bare-v149 in the CODE (outside the header's provenance chain)
code_zone = text.split("set -u", 1)[1]
for m in re.finditer(r"v149", code_zone):
    residual.append("v149 in code zone")
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), swap normalize-back clean, header narrative corrected, zero old tokens")
