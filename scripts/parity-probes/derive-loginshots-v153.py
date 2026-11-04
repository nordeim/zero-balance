#!/usr/bin/env python3
"""Derive the v153 LOGIN-shots pair from the v147 pair (the LOGIN half of
the v153 re-run — the v147-era login+calc pair's FIFTEENTH re-run; the
files keep the lineage's own "the v129-era LOGIN + CALCULATOR pair" family
designation, preserved per the v139/v140/v146/v152 convention).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the session tokens reflogin147->reflogin153 /
     clonelogin147->clonelogin153 (the EXPLICIT session-token swaps — the
     tokens carry '147' without the 'v' prefix, so the bare version swap
     cannot touch them; the v121-cycle stale-session-fix precedent),
     /tmp/vlm147->/tmp/vlm153, then the bare v147->v153.
  2. History corrections against the POST-swap state: the era marker
     (last re-shot v141 -> v147), the ordinal FOURTEENTH -> FIFTEENTH +
     the bracket extended [-> v123 -> v129 -> v135 -> v141 -> v153] ->
     [-> v123 -> v129 -> v135 -> v141 -> v147 -> v153], the agreement
     ordinal SEVENTIETH -> SEVENTY-SIXTH.
"""
import sys, re
import subprocess

PAIR = {
    "scripts/parity-probes/login-shots-v147.sh": "scripts/parity-probes/login-shots-v153.sh",
    "scripts/parity-probes/clone-login-shots-v147.sh": "scripts/parity-probes/clone-login-shots-v153.sh",
}

GENERIC = [
    ("reflogin147", "reflogin153"),
    ("clonelogin147", "clonelogin153"),
    ("/tmp/vlm147", "/tmp/vlm153"),
    ("v147", "v153"),
]

CORRECTIONS = {
    "scripts/parity-probes/login-shots-v153.sh": [
        ("# cycle's v129-era LOGIN + CALCULATOR pair, last re-shot v141 — the pair's\n# FOURTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v153], the SEVENTIETH consecutive\n# queue/ledger agreement).",
         "# cycle's v129-era LOGIN + CALCULATOR pair, last re-shot v147 — the pair's\n# FIFTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147 → v153], the SEVENTY-SIXTH consecutive\n# queue/ledger agreement)."),
    ],
    "scripts/parity-probes/clone-login-shots-v153.sh": [
        ("# cycle's v129-era LOGIN + CALCULATOR pair, last re-shot v141 — the pair's\n# FOURTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v153]). Runs",
         "# cycle's v129-era LOGIN + CALCULATOR pair, last re-shot v147 — the pair's\n# FIFTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147 → v153]). Runs"),
    ],
}

ok = True
for src, dst in PAIR.items():
    text = open(src, encoding="utf-8").read()
    for old, new in GENERIC:
        text = text.replace(old, new)
    open(dst, "w", encoding="utf-8").write(text)
    print(f"derived {dst} (generic swaps applied)")

for path, pairs in CORRECTIONS.items():
    text = open(path, encoding="utf-8").read()
    for old, new in pairs:
        if old not in text:
            print(f"MISS in {path}: {old[:70]!r}")
            ok = False
            continue
        text = text.replace(old, new)
        print(f"applied in {path}: history correction")
    open(path, "w", encoding="utf-8").write(text)

for dst in PAIR.values():
    text = open(dst, encoding="utf-8").read()
    bad = re.findall(r"re-shot v141|FOURTEENTH re-run|SEVENTIETH|reflogin147|clonelogin147|/tmp/vlm147", text)
    for tok in ("v123", "v117", "v129", "v135"):
        for m in re.finditer(tok, text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135 → v141 → v147 → v153" in ctx:
                continue
            if tok == "v129" and "v129-era" in ctx:
                continue
            bad.append(f"{tok} (outside the corrected bracket/family name)")
    # bare-v141 sweep: the corrected bracket ALONE (the era marker now
    # reads "last re-shot v147")
    for m in re.finditer(r"v141", text):
        ctx = text[max(0, m.start() - 40):m.end() + 40]
        if "→ v123 → v129 → v135 → v141 → v147 → v153" in ctx:
            continue
        bad.append("v141 (outside the corrected bracket)")
    # bare-v147 sweep: the corrected bracket + the corrected era marker
    for m in re.finditer(r"v147", text):
        ctx = text[max(0, m.start() - 40):m.end() + 40]
        if "→ v123 → v129 → v135 → v141 → v147 → v153" in ctx:
            continue
        if "re-shot" in ctx:
            continue
        bad.append("v147 (outside the corrected bracket/era marker)")
    if bad:
        print(f"RESIDUAL OLD TOKENS in {dst}: {sorted(set(bad))}")
        ok = False
    else:
        print(f"residual check {dst}: clean")
    subprocess.run(["bash", "-n", dst], check=True)

for src, dst in PAIR.items():
    sn = open(src, encoding="utf-8").read().count("\n")
    dn = open(dst, encoding="utf-8").read().count("\n")
    print(f"line-count {dst}: {dn + 1} lines (source {sn + 1}) — {'OK' if sn == dn else 'DRIFT'}")

sys.exit(0 if ok else 1)
