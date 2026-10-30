#!/usr/bin/env python3
"""Derive the v135 LOGIN-shots pair from the v129 pair (the LOGIN half of
the v135 re-run — the v59-era login+calc pair's TWELFTH re-run).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the session tokens reflogin129->reflogin135 /
     clonelogin129->clonelogin135 (the EXPLICIT session-token swaps — the
     tokens carry '129' without the 'v' prefix, so the bare version swap
     cannot touch them; the v121-cycle stale-session-fix precedent),
     /tmp/vlm129->/tmp/vlm135, then the bare v129->v135.
  2. History corrections against the POST-swap state: the era marker
     (v123-era -> v129-era, last re-shot v123 -> v129), the ordinal
     ELEVENTH -> TWELFTH + the bracket extended [-> v123 -> v135] ->
     [-> v123 -> v129 -> v135], the agreement ordinal FIFTY-SECOND ->
     FIFTY-EIGHTH.
"""
import sys, re
import subprocess

PAIR = {
    "scripts/parity-probes/login-shots-v129.sh": "scripts/parity-probes/login-shots-v135.sh",
    "scripts/parity-probes/clone-login-shots-v129.sh": "scripts/parity-probes/clone-login-shots-v135.sh",
}

GENERIC = [
    ("reflogin129", "reflogin135"),
    ("clonelogin129", "clonelogin135"),
    ("/tmp/vlm129", "/tmp/vlm135"),
    ("v129", "v135"),
]

CORRECTIONS = {
    "scripts/parity-probes/login-shots-v135.sh": [
        ("# cycle's v123-era LOGIN + CALCULATOR pair, last re-shot v123 — the pair's\n# ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v135], the FIFTY-SECOND consecutive\n# queue/ledger agreement).",
         "# cycle's v129-era LOGIN + CALCULATOR pair, last re-shot v129 — the pair's\n# TWELFTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135], the FIFTY-EIGHTH consecutive\n# queue/ledger agreement)."),
    ],
    "scripts/parity-probes/clone-login-shots-v135.sh": [
        ("# cycle's v123-era LOGIN + CALCULATOR pair, last re-shot v123 — the pair's\n# ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v135]). Runs",
         "# cycle's v129-era LOGIN + CALCULATOR pair, last re-shot v129 — the pair's\n# TWELFTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135]). Runs"),
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
    bad = re.findall(r"v123-era|re-shot v123|ELEVENTH re-run|FIFTY-SECOND|reflogin129|clonelogin129|/tmp/vlm129", text)
    for m in re.finditer(r"v123", text):
        ctx = text[max(0, m.start() - 60):m.end() + 60]
        if "→ v123 → v129 → v135" in ctx:
            continue
        bad.append("v123 (outside the corrected bracket)")
    for m in re.finditer(r"v117", text):
        ctx = text[max(0, m.start() - 60):m.end() + 60]
        if "→ v123 → v129 → v135" in ctx:
            continue
        bad.append("v117 (outside the corrected bracket)")
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
