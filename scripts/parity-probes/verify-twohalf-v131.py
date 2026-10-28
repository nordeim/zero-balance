#!/usr/bin/env python3
"""Verify the v131 two-half census byte-identity contracts by DIRECT
extraction (the v130 three-way form, adapted to the DASHBOARD lineage's
THREE census blocks). Extracts each census JS block from arbit-v131.sh
(the source) + ref-arbit-v131.sh + clone-arbit-v131.sh by marker scanning
and compares md5 line-block digests across all three — they must be
byte-identical (the documented two-half contract)."""
import hashlib

def extract_block(path, start_marker, end_marker):
    lines = open(path, encoding="utf-8").read().split("\n")
    block, inside = [], False
    for ln in lines:
        if not inside and ln.startswith(start_marker):
            inside = True
            block.append(ln)
            continue
        if inside:
            block.append(ln)
            if ln.rstrip().endswith(end_marker):
                break
    return "\n".join(block)

pairs = [
    ('ARBIT_G="(function () {', '})()"', "ARBIT_G"),
    ('ARBIT_Q="(function () {', '})()"', "ARBIT_Q"),
    ('ARBIT_X="(function () {', '})()"', "ARBIT_X"),
]
ok = True
for start, end, name in pairs:
    src = extract_block("scripts/parity-probes/arbit-v131.sh", start, end)
    ref = extract_block("scripts/parity-probes/ref-arbit-v131.sh", start, end)
    clone = extract_block("scripts/parity-probes/clone-arbit-v131.sh", start, end)
    digests = {
        "arbit-v131.sh": hashlib.md5(src.encode()).hexdigest(),
        "ref-arbit-v131.sh": hashlib.md5(ref.encode()).hexdigest(),
        "clone-arbit-v131.sh": hashlib.md5(clone.encode()).hexdigest(),
    }
    match = "IDENTICAL" if len(set(digests.values())) == 1 else "MISMATCH"
    print(f"{name} ({len(src.splitlines())} lines): " +
          " | ".join(f"{k} md5 {v}" for k, v in digests.items()) + f" -> {match}")
    if len(set(digests.values())) != 1:
        ok = False

print("CONTRACT:", "HELD — census blocks byte-identical across the source + both halves" if ok else "BROKEN")
exit(0 if ok else 1)
