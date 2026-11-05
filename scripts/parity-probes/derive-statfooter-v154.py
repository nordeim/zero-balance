#!/usr/bin/env python3
"""Derive statfooter-arbit-v154.sh from statfooter-arbit-v148.sh (the
ONE-SHOT both-sides arbitration for the v154 cycle's stat-card-label
watch — the documented VLM text-misread sub-form, "Total Expense" singular
vs the clone's "Total Expenses" plural, disproven at v106/v112/v118/v136;
the v148 attempt's pass 1 re-flagged it, the v148 re-run's passes did NOT —
the standing disproof re-confirmed either way, per the v43 rule).

The v148-cycle derivation form: the header narrative REWRITTEN for the new
cycle (the v148 derivation rewrote the v136 header the same way), the body
swap-only (the session tokens refstatfooter148/clonestatfooter148 carry
'148' without the 'v' prefix, so they need the explicit swaps; then the
generic v148 -> v154). Verified by normalize-back diff (the header
correction reversed FIRST, then the generic swaps in reverse order)."""
import re
import sys

SRC = "scripts/parity-probes/statfooter-arbit-v148.sh"
DST = "scripts/parity-probes/statfooter-arbit-v154.sh"

GENERIC = [
    ("refstatfooter148", "refstatfooter154"),
    ("clonestatfooter148", "clonestatfooter154"),
    ("v148", "v154"),
]

# the header narrative correction (against the POST-swap state): the
# v148-cycle provenance stays historical truth — "the earlier v148
# attempt's pass 1 re-flagged it, this re-run's passes did NOT" becomes
# "the v148 attempt's pass 1 re-flagged it, the v148 re-run's passes did
# NOT" (the v154 cycle's own pass results are recorded in the v154 plan,
# not in this script's header)
HEADER_CORRECTION = (
    "disproven at v106/v112/v118/v136; the earlier v154 attempt's\n"
    "# pass 1 re-flagged it, this re-run's passes did NOT — the standing\n"
    "# disproof re-confirmed either way, per the v43 rule): the third stat\n"
    "# card's TITLE + the footer chrome measured on BOTH sides.",
    "disproven at v106/v112/v118/v136; the v148 attempt's\n"
    "# pass 1 re-flagged it, the v148 re-run's passes did NOT — the standing\n"
    "# disproof re-confirmed either way, per the v43 rule): the third stat\n"
    "# card's TITLE + the footer chrome measured on BOTH sides.",
)

text = open(SRC, encoding="utf-8").read()
missing = []
for old, new in GENERIC:
    if old not in text:
        missing.append(old)
    text = text.replace(old, new)

old, new = HEADER_CORRECTION
if old not in text:
    missing.append("HEADER_CORRECTION (post-swap fragment)")
else:
    text = text.replace(old, new)
    print("applied: the header narrative corrected (the v148-cycle provenance preserved)")

if missing:
    print("MISSING SOURCES:", missing)
    sys.exit(1)

# normalize back and prove swap+correction-only (the correction reversed
# FIRST, then the generic swaps in reverse order)
back = text
old, new = HEADER_CORRECTION
back = back.replace(new, old)
for old, new in reversed(GENERIC):
    back = back.replace(new, old)
original = open(SRC, encoding="utf-8").read()
if back != original:
    print("FAIL: not a pure swap+correction (normalize-back mismatch)")
    sys.exit(1)

open(DST, "w", encoding="utf-8").write(text)

# residual old-token check — the corrected header's historical 'v148'
# citations (the watch's provenance) are whitelisted before the scan
whitelist = "the v148 attempt's"
residual_text = text.replace(whitelist, "the ATTEMPT's").replace(
    "the v148 re-run's passes did NOT", "the RE-RUN's passes did NOT"
)
residual = re.findall(
    r"refstatfooter148|clonestatfooter148|v148|/tmp/vlm148|statfooter-1280-v148",
    residual_text,
)
if residual:
    print(f"FAIL: {DST} retains old tokens: {sorted(set(residual))}")
    sys.exit(1)

sn = original.count("\n")
dn = text.count("\n")
print(f"OK: {DST} derived ({dn + 1} lines, source {sn + 1}), normalize-back clean, zero old tokens (the header's v148 watch-provenance citations preserved)")
