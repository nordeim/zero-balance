#!/usr/bin/env python3
"""Derive the v152 probe series from the v146 lineage (the SAVINGS view
at desktop 1280x800 FULL-PAGE — the v58-era savings pair's FIFTEENTH
re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 →
v122 → v128 → v134 → v140 → v146 → v152]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v151-era docs' v152 queue names "the pair's FIFTEENTH
re-run bracket [v58 → ... → v140 → v146 → v152]... to be verified against
the v146 lineage's own records" — verified against the v146 lineage's own
records BEFORE this derivation: the v146 plan's own header reads "the
v140-era SAVINGS pair's FOURTEENTH re-run [v58 → v65 → v74 → v80 → v86 →
v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134 → v140 → v146]" — a
15-ENTRY bracket with the FOURTEENTH ordinal (v58 the original, the
entries-minus-one convention: 15 entries − the original = 14 re-runs, the
FOURTEENTH). v152 = the FIFTEENTH re-run by appending v152 to the v146
header's FOURTEENTH bracket. The SEVENTY-FIFTH consecutive queue/ledger
agreement. The v139–v144 rotation pool EXHAUSTED (through v150); the
cadence is in its THIRD PASS, the v146-era SAVINGS pair the oldest
remaining [v146 < v147 < v148 < v149 < v150 < v151].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm146->refvlm152, clonevlm146->clonevlm152,
     refarbit146->refarbit152, clonearbit146->clonearbit152,
     /tmp/vlm146->/tmp/vlm152, v146->v152
  2. History corrections (the era marker last-re-shot v140 -> v146, the
     re-run ordinal FOURTEENTH->FIFTEENTH, the re-run bracket extended
     [v58 -> ... -> v134 -> v140 -> v146 -> v152], the oldest-remaining
     list re-pointed at the CURRENT later re-runs [v146 < v147 < v148 <
     v149 < v150 < v151], the plan citation v145 -> v151, the agreement
     ordinal SIXTY-NINTH -> SEVENTY-FIFTH).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v146.sh": "scripts/parity-probes/vlm-shots-v152.sh",
    "scripts/parity-probes/clone-vlmshots-v146.sh": "scripts/parity-probes/clone-vlmshots-v152.sh",
    "scripts/parity-probes/vlm-compare-v146.mjs": "scripts/parity-probes/vlm-compare-v152.mjs",
    "scripts/parity-probes/arbit-v146.sh": "scripts/parity-probes/arbit-v152.sh",
}

GENERIC = [
    ("refvlm146", "refvlm152"),
    ("clonevlm146", "clonevlm152"),
    ("refarbit146", "refarbit152"),
    ("clonearbit146", "clonearbit152"),
    ("/tmp/vlm146", "/tmp/vlm152"),
    ("v146", "v152"),
]


def main():
    ok = True
    for src, dst in FILES.items():
        text = open(src, encoding="utf-8").read()
        for old, new in GENERIC:
            text = text.replace(old, new)
        open(dst, "w", encoding="utf-8").write(text)
        print(f"derived {dst} (generic swaps applied)")

    print("\n--- history corrections (against the POST-swap state) ---")
    corr_map = {
        "scripts/parity-probes/vlm-shots-v152.sh": [
            ("# v140, now the oldest remaining [v140 < v141 < v142 < v143 < v144]; the\n# v145 plan's v152 queue suggestion, agreeing with the rotation ledger —\n# the SIXTY-NINTH consecutive agreement). READ-ONLY: login + passive",
             "# v146, now the oldest remaining [v146 < v147 < v148 < v149 < v150 < v151]; the\n# v151 plan's v152 queue suggestion, agreeing with the rotation ledger —\n# the SEVENTY-FIFTH consecutive agreement). READ-ONLY: login + passive"),
        ],
        "scripts/parity-probes/clone-vlmshots-v152.sh": [
            ("# v140, now the oldest remaining [v140 < v141 < v142 < v143 < v144]; the\n# pair's FOURTEENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134 → v140 → v152]). Runs inside",
             "# v146, now the oldest remaining [v146 < v147 < v148 < v149 < v150 < v151]; the\n# pair's FIFTEENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134 → v140 → v146 → v152]). Runs inside"),
        ],
        "scripts/parity-probes/vlm-compare-v152.mjs": [
            ("// next-oldest candidate (the v128-era savings pair's FOURTEENTH re-run — last re-shot\n// v140, now the oldest remaining [v140 < v141 < v142 < v143 < v144] — agreeing with the rotation ledger, the SIXTY-NINTH consecutive agreement).",
             "// next-oldest candidate (the v128-era savings pair's FIFTEENTH re-run — last re-shot\n// v146, now the oldest remaining [v146 < v147 < v148 < v149 < v150 < v151] — agreeing with the rotation ledger, the SEVENTY-FIFTH consecutive agreement)."),
        ],
        "scripts/parity-probes/arbit-v152.sh": [
            ("# the v128-era savings pair's FOURTEENTH re-run, last re-shot v140 — now the\n# oldest remaining candidate [v140 < v141 < v142 < v143 < v144]).",
             "# the v128-era savings pair's FIFTEENTH re-run, last re-shot v146 — now the\n# oldest remaining candidate [v146 < v147 < v148 < v149 < v150 < v151])."),
        ],
    }
    for path, pairs in corr_map.items():
        text = open(path, encoding="utf-8").read()
        for old, new in pairs:
            if old not in text:
                print(f"MISS in {path}: {old[:70]!r}")
                ok = False
                continue
            text = text.replace(old, new)
            print(f"applied in {path}: {old[:52]!r} -> corrected")
        open(path, "w", encoding="utf-8").write(text)

    # residual old-token check across all four files
    # LEGIT contexts that must survive: the corrected re-run bracket
    # (→ v134 → v140 → v146 → v152) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the era marker "last re-shot v146";
    # the axis-provenance citations (the v58 axes, the v64/v65 axes, the
    # v74/v80 axes, the v51/v54 390-only family, the v68 dedupe, the v73
    # convention).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v140|FOURTEENTH re-run|SIXTY-NINTH|v145 plan|"
            r"refvlm146|clonevlm146|refarbit146|clonearbit146|/tmp/vlm146",
            text,
        ):
            bad.append(m.group(0))
        # bare-v140 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v140", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v134 → v140 → v146 → v152" in ctx:
                continue
            if "v140" not in bad:
                bad.append("v140 (outside the corrected bracket)")
        # the old oldest-remaining list tokens (v141..v145) must be wholly gone
        for m in re.finditer(r"v14[1-5]", text):
            bad.append(f"{m.group(0)} (old oldest-remaining/plan token)")
        if bad:
            print(f"RESIDUAL OLD TOKENS in {dst}: {sorted(set(bad))}")
            ok = False
        else:
            print(f"residual check {dst}: clean")

    # line-count report (the two-half builder inherits boundaries)
    for src, dst in FILES.items():
        sn = open(src, encoding="utf-8").read().count("\n")
        dn = open(dst, encoding="utf-8").read().count("\n")
        status = "OK" if sn == dn else f"DRIFT ({dn - sn:+d})"
        print(f"line-count {dst}: {dn + 1} lines (source {sn + 1}) — {status}")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
