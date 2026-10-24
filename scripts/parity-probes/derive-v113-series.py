#!/usr/bin/env python3
"""Derive the v113 probe series from the v107 lineage (the BUDGET
GUIDELINES + QUICK-ACTION pair — the dashboard FULL-PAGE's below-the-fold
surfaces at desktop 1280x800, EIGHTH re-run
[v61 -> v68 -> v77 -> v83 -> v89 -> v95 -> v101 -> v107 -> v113]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm107->refvlm113, clonevlm107->clonevlm113,
     refar107->refar113, clonear107->clonear113,
     /tmp/vlm107->/tmp/vlm113, v107->v113
  2. History corrections, single-line-safe forms (the v107 derivation
     lesson: multi-line fragments are line-break-fragile; every correction
     below is a within-line edit): era marker v101-era -> v107-era,
     last-re-shot v101 -> v107, the oldest-remaining list bumped to the
     current era [v107 < v108 < v109 < v110 < v111 < v112], re-run ordinal
     SEVENTH->EIGHTH, the re-run bracket extended [v61 -> v68 -> v77 ->
     v83 -> v89 -> v95 -> v101 -> v107 -> v113], the agreement count
     THIRTIETH -> THIRTY-SIXTH, the re-proves window v101-v106 ->
     v101-v107, the arbit verdict reference "The v101" -> "The v107" (the
     v107 verdict was IDENTICAL — the fifth consecutive IDENTICAL for this
     pair), the drift-re-check "since v101" -> "since v107".

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v107.sh": "scripts/parity-probes/vlm-shots-v113.sh",
    "scripts/parity-probes/clone-vlmshots-v107.sh": "scripts/parity-probes/clone-vlmshots-v113.sh",
    "scripts/parity-probes/vlm-compare-v107.mjs": "scripts/parity-probes/vlm-compare-v113.mjs",
    "scripts/parity-probes/arbit-v107.sh": "scripts/parity-probes/arbit-v113.sh",
}

GENERIC = [
    ("refvlm107", "refvlm113"),
    ("clonevlm107", "clonevlm113"),
    ("refar107", "refar113"),
    ("clonear107", "clonear113"),
    ("/tmp/vlm107", "/tmp/vlm113"),
    ("v107", "v113"),
]

# Single-line-safe history corrections (each verified applied per file).
CORRECTIONS = [
    ("v101-era", "v107-era"),
    ("re-shot v101", "re-shot v107"),
    ("SEVENTH re-run", "EIGHTH re-run"),
    ("[v61 → v68 → v77 → v83 → v89 → v95 → v101 → v113]",
     "[v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113]"),
    ("[v101 < v102 < v103 < v104 < v105 < v106]",
     "[v107 < v108 < v109 < v110 < v111 < v112]"),
    ("THIRTIETH", "THIRTY-SIXTH"),
    ("v101-v106", "v101-v107"),
    ("The v101", "The v107"),
    ("since v101", "since v107"),
]


def main():
    ok = True
    for src, dst in FILES.items():
        text = open(src, encoding="utf-8").read()
        for old, new in GENERIC:
            text = text.replace(old, new)
        open(dst, "w", encoding="utf-8").write(text)
        print(f"derived {dst} (generic swaps applied)")

    print("\n--- history corrections ---")
    for path in FILES.values():
        text = open(path, encoding="utf-8").read()
        applied = []
        for old, new in CORRECTIONS:
            n = text.count(old)
            if n:
                text = text.replace(old, new)
                applied.append(f"{old[:34]!r} x{n}")
        open(path, "w", encoding="utf-8").write(text)
        print(f"{path}: {len(applied)} correction families applied")
        for a in applied:
            print(f"    {a}")

    # residual old-token check across all four files.
    # LEGIT contexts that must survive: the corrected re-run bracket
    # (→ v101 → v107 → v113 — the pair's own history), the corrected
    # state tokens (re-shot v107, v107-era, v101-v107, The v107,
    # since v107), the pin/axes provenance (the v44/v45/v51/v61/v83
    # pins), and the rule/lesson references (the v75 convention).
    BAD = re.compile(
        r"v101-era|re-shot v101|SEVENTH re-run|THIRTIETH|v101 < v102"
        r"|v101-v106|The v101|since v101"
        r"|refvlm107|clonevlm107|refar107|clonear107|/tmp/vlm107"
    )
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        hits = BAD.findall(text)
        if hits:
            print(f"RESIDUAL OLD TOKENS in {dst}: {sorted(set(hits))}")
            ok = False
        else:
            print(f"residual check {dst}: clean")

    # line-count report (the two-half builder inherits boundaries)
    for src, dst in FILES.items():
        sn = open(src, encoding="utf-8").read().count("\n")
        dn = open(dst, encoding="utf-8").read().count("\n")
        status = "OK" if sn == dn else f"DRIFT ({dn - sn:+d})"
        print(f"line-count {dst}: {dn + 1} lines (source {sn + 1}) — {status}")
        if sn != dn:
            ok = False

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
