#!/usr/bin/env python3
"""Derive the v129 LOGIN-shots pair from the v123 pair (the LOGIN half of
the v129 re-run — the v59-era login+calc pair's ELEVENTH re-run).

Order of operations (the POST-SWAP-FRAGMENT RULE):
  1. Generic swaps — the session tokens reflogin123->reflogin129 /
     clonelogin123->clonelogin129 (the EXPLICIT session-token swaps — the
     tokens carry '123' without the 'v' prefix, so the bare version swap
     cannot touch them; the v121-cycle stale-session-fix precedent),
     /tmp/vlm123->/tmp/vlm129, then the bare v123->v129.
  2. History corrections against the POST-swap state: the era marker
     (v117-era -> v123-era, last re-shot v117 -> v123), the ordinal
     TENTH -> ELEVENTH + the bracket extended [-> v117 -> v129] ->
     [-> v117 -> v123 -> v129], the agreement ordinal FORTY-SIXTH ->
     FIFTY-SECOND.
"""
import sys, re

PAIR = {
    "scripts/parity-probes/login-shots-v123.sh": "scripts/parity-probes/login-shots-v129.sh",
    "scripts/parity-probes/clone-login-shots-v123.sh": "scripts/parity-probes/clone-login-shots-v129.sh",
}

GENERIC = [
    ("reflogin123", "reflogin129"),
    ("clonelogin123", "clonelogin129"),
    ("/tmp/vlm123", "/tmp/vlm129"),
    ("v123", "v129"),
]

CORRECTIONS = {
    "scripts/parity-probes/login-shots-v129.sh": [
        ("# cycle's v117-era LOGIN + CALCULATOR pair, last re-shot v117 — the pair's\n# TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v129], the FORTY-SIXTH consecutive\n# queue/ledger agreement).",
         "# cycle's v123-era LOGIN + CALCULATOR pair, last re-shot v123 — the pair's\n# ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129], the FIFTY-SECOND consecutive\n# queue/ledger agreement)."),
    ],
    "scripts/parity-probes/clone-login-shots-v129.sh": [
        ("# cycle's v117-era LOGIN + CALCULATOR pair, last re-shot v117 — the pair's\n# TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v129]). Runs",
         "# cycle's v123-era LOGIN + CALCULATOR pair, last re-shot v123 — the pair's\n# ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129]). Runs"),
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
    bad = re.findall(r"v117-era|re-shot v117|TENTH re-run|FORTY-SIXTH|reflogin123|clonelogin123|/tmp/vlm123", text)
    for m in re.finditer(r"v117", text):
        ctx = text[max(0, m.start() - 60):m.end() + 60]
        if "→ v117 → v123 → v129" in ctx:
            continue
        bad.append("v117 (outside the corrected bracket)")
    if bad:
        print(f"RESIDUAL OLD TOKENS in {dst}: {sorted(set(bad))}")
        ok = False
    else:
        print(f"residual check {dst}: clean")
    import subprocess
    subprocess.run(["bash", "-n", dst], check=True)

for src, dst in PAIR.items():
    sn = open(src, encoding="utf-8").read().count("\n")
    dn = open(dst, encoding="utf-8").read().count("\n")
    print(f"line-count {dst}: {dn + 1} lines (source {sn + 1}) — {'OK' if sn == dn else 'DRIFT'}")

sys.exit(0 if ok else 1)
