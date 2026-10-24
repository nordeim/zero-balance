#!/usr/bin/env python3
"""Derive the v116 probe series from the v110 lineage (the SAVINGS pair —
the SAVINGS view at desktop 1280x800 FULL-PAGE, NINTH re-run
[v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> v104 -> v110 -> v116]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm110->refvlm116, clonevlm110->clonevlm116,
     refarbit110->refarbit116, clonearbit110->clonearbit116,
     /tmp/vlm110->/tmp/vlm116, v110->v116
  2. History corrections, single-line-safe forms (the v107 derivation
     lesson: multi-line fragments are line-break-fragile; every correction
     below is a within-line edit): the era re-pointed at the pair's latest
     re-run (the v104-era savings pair -> the v110-era), last re-shot
     v104 -> v110 (BOTH forms — "re-shot v104" line-internal in the arbit
     header, "v104, now the oldest" for the sh/mjs headers where the
     fragment wraps lines), the oldest-remaining list re-pointed
     [v110 < v111 < v112 < v113 < v114 < v115], re-run ordinal
     EIGHTH->NINTH, the plan attribution the v109 plan's -> the v115
     plan's, the agreement ordinal THIRTY-THIRD -> THIRTY-NINTH, and the
     re-run bracket extended [v58 -> ... -> v98 -> v104 -> v110 -> v116].

THE POST-SWAP-FRAGMENT RULE (the v115 lesson): the bracket correction
below is written against the POST-generic-swap state — the generic swap
consumes the version token first (v110 -> v116), so the correction
targets the already-swapped "-> v98 -> v104 -> v116]" form.

The census provenance tokens in arbit (the v74/v80 axes, the v80
titleRow geometry, the v58 DATA-CONDITIONAL footer class, the v57
conditional-footer contract, the v51/v54 390-only family, the v22
parked-pointer lesson, the v43 rule, the v46 rule, the v73 heredoc
lesson) are carried VERBATIM (the v85..v115 precedent).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v110.sh": "scripts/parity-probes/vlm-shots-v116.sh",
    "scripts/parity-probes/clone-vlmshots-v110.sh": "scripts/parity-probes/clone-vlmshots-v116.sh",
    "scripts/parity-probes/vlm-compare-v110.mjs": "scripts/parity-probes/vlm-compare-v116.mjs",
    "scripts/parity-probes/arbit-v110.sh": "scripts/parity-probes/arbit-v116.sh",
}

GENERIC = [
    ("refvlm110", "refvlm116"),
    ("clonevlm110", "clonevlm116"),
    ("refarbit110", "refarbit116"),
    ("clonearbit110", "clonearbit116"),
    ("/tmp/vlm110", "/tmp/vlm116"),
    ("v110", "v116"),
]

# Single-line-safe history corrections (each verified applied per file).
# NOTE: these run AFTER the generic swaps, so any correction fragment
# containing the current version (v116) must be written against the
# POST-swap state (THE POST-SWAP-FRAGMENT RULE — the v115 derivation
# lesson; the v114 precedent targeted the already-swapped
# "v96 -> v102 -> v114])" form).
CORRECTIONS = [
    ("the v104-era savings pair", "the v110-era savings pair"),
    ("re-shot v104", "re-shot v110"),
    ("v104, now the oldest", "v110, now the oldest"),
    ("[v104 < v105 < v106 < v107 < v108 < v109]", "[v110 < v111 < v112 < v113 < v114 < v115]"),
    ("EIGHTH re-run", "NINTH re-run"),
    # NOTE: the plan attribution fragment is the BARE "v109 plan's" form —
    # the line wraps between "the" (line N end) and "v109" (line N+1 start),
    # so the with-article form misses (the v107 line-break lesson again).
    ("v109 plan's", "v115 plan's"),
    ("THIRTY-THIRD consecutive agreement", "THIRTY-NINTH consecutive agreement"),
    ("→ v98 → v104 → v116]", "→ v98 → v104 → v110 → v116]"),
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
    # (-> v98 -> v104 -> v110 -> v116 — the pair's own history), the
    # corrected era/re-shot/oldest tokens (the v110-era savings pair /
    # re-shot v110 / [v110 < v111 ... < v115]), the census provenance
    # (The v74/v80 census axes, the v80 titleRow geometry, the v58
    # DATA-CONDITIONAL footer class, the v57 conditional-footer contract,
    # the v51/v54 390-only family — carried verbatim per the v85..v115
    # precedent), the rule/lesson references (the v22/v43/v46/v73
    # lessons), and the corrected attribution (the v115 plan's).
    BAD = re.compile(
        r"re-shot v104|EIGHTH re-run|the v104-era"
        r"|THIRTY-THIRD consecutive"
        r"|refvlm110|clonevlm110|refarbit110|clonearbit110|/tmp/vlm110"
        r"|\[v104 < v105"
        r"|v104, now the oldest"
        r"|v109 plan's"
        r"|v104 → v116\]"
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
