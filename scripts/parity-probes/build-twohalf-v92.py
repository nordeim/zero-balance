#!/usr/bin/env python3
"""Build ref-arbit-v92.sh + clone-arbit-v92.sh from arbit-v92.sh (the
two-half controlled form, the v89/v91 lesson). The census JS block
(lines 38..190 of arbit-v92.sh, the SV_CENSUS_JS assignment) is extracted
ONCE and embedded byte-identically in both halves (the contract)."""
import hashlib

SRC = "scripts/parity-probes/arbit-v92.sh"
lines = open(SRC).read().split("\n")  # 0-indexed; line N = lines[N-1]

# The census JS block: from the 'SV_CENSUS_JS=' line (38) through the
# closing ')"()' line (190) inclusive.
census_start, census_end = 38, 190
census_block = "\n".join(lines[census_start - 1 : census_end])
assert census_block.startswith('SV_CENSUS_JS="(async () => {'), census_block[:60]
assert census_block.rstrip().endswith('})()"'), census_block[-60:]

# Header (lines 1..36): the shared provenance comments + REF var.
header = "\n".join(lines[0:36])

# The reference-side execution block: lines 193..224 (after the marker at
# 192), minus the marker line.
ref_exec = "\n".join(lines[192:224])

# The clone-side execution block: lines 227..256 (between the CLONE SIDE
# marker at 226 and the seedcheck at 258), minus the marker echo.
clone_exec = "\n".join(lines[226:256])

ref_half = f"""{header}

# THE TWO-HALF CONTROLLED FORM (the v89/v91 lesson): the combined
# arbit-v92.sh's clone half aborted in the sandbox's chromium resource
# exhaustion; this is the REFERENCE half, the census JS byte-identical
# to the clone half's (the md5 line-block contract).
{census_block}

########## REFERENCE SIDE (the half) ##########
{ref_exec}
echo "=== ref arbit v92 half done ==="
"""

clone_half = f"""{header}

# THE TWO-HALF CONTROLLED FORM (the v89/v91 lesson): the combined
# arbit-v92.sh's clone half aborted in the sandbox's chromium resource
# exhaustion; this is the CLONE half, the census JS byte-identical
# to the reference half's (the md5 line-block contract).
{census_block}

########## CLONE SIDE (the half) ##########
{clone_exec}
echo "=== clone arbit v92 half done ==="
"""

open("scripts/parity-probes/ref-arbit-v92.sh", "w").write(ref_half)
open("scripts/parity-probes/clone-arbit-v92.sh", "w").write(clone_half)

# The contract check: the census JS block must be byte-identical.
md5 = hashlib.md5(census_block.encode()).hexdigest()
print(f"census JS block md5: {md5}")
print(f"census block lines: {census_end - census_start + 1}")
print("halves written")
