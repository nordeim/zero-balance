#!/usr/bin/env python3
"""Verify the v133 two-half census byte-identity contract by DIRECT
extraction (the v123/v124/v125/v126 form adapted to the ITEMS lineage's
single CENSUS_JS marker). Extracts the census JS block from
arbit-v133.sh (the source) + ref-arbit-v133.sh + clone-arbit-v133.sh by
marker scanning and compares md5 line-block digests across all three —
they must equal the documented v103/v109/v115/v121/v127 lineage contract
(b55dcd29) VERBATIM."""
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

CONTRACTS = {
    "CENSUS_JS": "b55dcd29",
}

ok = True
for name, expected in CONTRACTS.items():
    start = f'{name}="(async () => {{'
    end = '})()"'
    src = extract_block("scripts/parity-probes/arbit-v133.sh", start, end)
    ref = extract_block("scripts/parity-probes/ref-arbit-v133.sh", start, end)
    clone = extract_block("scripts/parity-probes/clone-arbit-v133.sh", start, end)
    m_src = hashlib.md5(src.encode()).hexdigest()[:8]
    m_ref = hashlib.md5(ref.encode()).hexdigest()[:8]
    m_clone = hashlib.md5(clone.encode()).hexdigest()[:8]
    three_way = "IDENTICAL" if m_src == m_ref == m_clone else "MISMATCH"
    contract = "CONTRACT-OK" if m_ref == expected else f"CONTRACT-FAIL (expected {expected})"
    print(f"{name}: src {len(src.splitlines())} lines md5 {m_src} | ref md5 {m_ref} | clone md5 {m_clone} -> three-way {three_way} vs documented {expected}: {contract}")
    if not (m_src == m_ref == m_clone and m_ref == expected):
        ok = False

print("CONTRACT:", "HELD — census blocks byte-identical across source + both halves, the documented lineage values VERBATIM" if ok else "BROKEN")
exit(0 if ok else 1)
