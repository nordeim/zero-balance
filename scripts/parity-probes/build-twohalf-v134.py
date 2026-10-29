#!/usr/bin/env python3
"""Build ref-arbit-v134.sh + clone-arbit-v134.sh from arbit-v134.sh (the
two-half controlled form, BUILT FROM THE START — the v92..v133 lesson).
The ONE census JS block (SV_CENSUS_JS lines 38..190) is extracted ONCE
and embedded byte-identically in both halves (the contract, md5-verified).
Line numbers inherited verbatim from build-twohalf-v128.py — the v134
derivation is line-count-preserving (verified by derive-v134-series.py)."""
import hashlib

SRC = "scripts/parity-probes/arbit-v134.sh"
lines = open(SRC).read().split("\n")  # 0-indexed; line N = lines[N-1]

# The census JS block: from the 'SV_CENSUS_JS=' line (38) through the
# closing '})()"' line (190) inclusive.
census_start, census_end = 38, 190
census_block = "\n".join(lines[census_start - 1 : census_end])
assert census_block.startswith('SV_CENSUS_JS="(async () => {'), census_block[:60]
assert census_block.rstrip().endswith('})()"'), census_block[-60:]

# Header (lines 1..36): the shared provenance comments + REF var.
header = "\n".join(lines[0:36])

# The reference-side execution block: lines 193..224 (after the marker at
# 192), through the last SV_CENSUS_JS eval.
ref_exec = "\n".join(lines[192:224])
assert ref_exec.startswith('export AGENT_BROWSER_SESSION="refarbit134"'), ref_exec[:60]
assert 'agent-browser eval "$SV_CENSUS_JS"' in ref_exec, "ref_exec boundary wrong"

# The clone-side execution block: lines 227..256 (between the CLONE SIDE
# marker at 226 and the post-EOF blank at 256).
clone_exec = "\n".join(lines[226:256])
assert clone_exec.startswith('cd "$(dirname "$0")/../.."'), clone_exec[:60]
assert clone_exec.rstrip().endswith("EOF") or "EOF" in clone_exec[-40:], clone_exec[-60:]

TWOHALF_NOTE = """
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v133
# lesson): the combined arbit form's clone half is the chromium
# resource-exhaustion risk (the v89/v91-documented symptom class), so the
# census runs as two independent halves from the start; the census JS
# blocks are byte-identical across the halves (the md5 line-block
# contract).
"""

ref_half = f"""{header}
{TWOHALF_NOTE}
{census_block}

########## REFERENCE SIDE (the half) ##########
{ref_exec}
echo "=== ref arbit v134 half done ==="
"""

clone_half = f"""{header}
{TWOHALF_NOTE}
{census_block}

########## CLONE SIDE (the half) ##########
{clone_exec}

echo "=== seedcheck (the v66 discipline) ==="
cd "$(dirname "$0")/../.."
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== clone arbit v134 half done ==="
"""

open("scripts/parity-probes/ref-arbit-v134.sh", "w").write(ref_half)
open("scripts/parity-probes/clone-arbit-v134.sh", "w").write(clone_half)

# The md5 line-block contract: the census blocks byte-identical across halves.
def block_md5(path):
    text = open(path).read()
    start = text.index('SV_CENSUS_JS="(async () => {')
    end = text.index('})()"', start) + len('})()"')
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

rm, rn = block_md5("scripts/parity-probes/ref-arbit-v134.sh")
cm, cn = block_md5("scripts/parity-probes/clone-arbit-v134.sh")
assert rm == cm, f"CENSUS BLOCK MISMATCH: {rm} vs {cm}"
print(f"census JS block md5 {rm} — {rn} lines — byte-identical across halves OK")
print("halves written")
