#!/usr/bin/env python3
"""Verify the v136 two-half census byte-identity contracts by DIRECT
extraction (the v124/v125/v126/v127/v128/v129 — carried forward three-way form, adapted to
the NETWORTH+DRILL-DOWN lineage's TWO census blocks). Extracts each census
JS block from arbit-v136.sh (the source) + ref-arbit-v136.sh +
clone-arbit-v136.sh by marker scanning and compares md5 line-block digests
across all three — they must be byte-identical (the documented two-half
contract)."""
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

CONTRACTS = ["ARBIT_A", "ARBIT_B"]
ok = True
for name in CONTRACTS:
    start, end = f"{name}='(async () => {{", "})()'"
    src = extract_block("scripts/parity-probes/arbit-v136.sh", start, end)
    ref = extract_block("scripts/parity-probes/ref-arbit-v136.sh", start, end)
    clone = extract_block("scripts/parity-probes/clone-arbit-v136.sh", start, end)
    digests = {
        "arbit-v136.sh": hashlib.md5(src.encode()).hexdigest(),
        "ref-arbit-v136.sh": hashlib.md5(ref.encode()).hexdigest(),
        "clone-arbit-v136.sh": hashlib.md5(clone.encode()).hexdigest(),
    }
    match = "IDENTICAL" if len(set(digests.values())) == 1 else "MISMATCH"
    print(f"{name} ({len(src.splitlines())} lines): " +
          " | ".join(f"{k} md5 {v}" for k, v in digests.items()) + f" -> {match}")
    if len(set(digests.values())) != 1:
        ok = False

print("CONTRACT:", "HELD — census blocks byte-identical across the source + both halves" if ok else "BROKEN")
exit(0 if ok else 1)
