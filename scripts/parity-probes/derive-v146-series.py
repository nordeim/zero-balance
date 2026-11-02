#!/usr/bin/env python3
"""Derive the v146 probe series from the v140 lineage (the SAVINGS view
at desktop 1280x800 FULL-PAGE — the v58-era savings pair's FOURTEENTH
re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 →
v122 → v128 → v134 → v140 → v146]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v145-era docs' v146 queue names "the pair's FOURTEENTH
re-run bracket [v58 → ... → v134 → v140 → v146]... to be verified against
the v140 lineage's own records" — verified against the v140 lineage's own
records BEFORE this derivation: the v140 plan's own header reads "the
v134-era SAVINGS pair's THIRTEENTH re-run [v58 → v65 → v74 → v80 → v86 →
v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134 → v140]" — a
14-ENTRY bracket with the THIRTEENTH ordinal (v58 the original, the
entries-minus-one convention: 14 entries − the original = 13 re-runs, the
THIRTEENTH). v146 = the FOURTEENTH re-run by appending v146 to the v140
header's THIRTEENTH bracket. The SIXTY-NINTH consecutive queue/ledger
agreement. The v133–v138 second-pass pool is EXHAUSTED; the cadence is in
its THIRD PASS (the v139–v144 pool), the v140-era SAVINGS pair the oldest
remaining [v139 < v140 < v141 < v142 < v143 < v144 — the v139-era ITEMS
pair re-run at v145, the v140-era SAVINGS pair now the oldest remaining].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm140->refvlm146, clonevlm140->clonevlm146,
     refarbit140->refarbit146, clonearbit140->clonearbit146,
     /tmp/vlm140->/tmp/vlm146, v140->v146
  2. History corrections (the era marker last-re-shot v134 -> v140 + the
     oldest-remaining list v134..v138 -> v140..v144 + the queue source
     the v139 plan -> the v145 plan + the agreement counter
     SIXTY-THIRD -> SIXTY-NINTH; the re-run ordinal THIRTEENTH->FOURTEENTH,
     the re-run bracket extended [v58 -> ... -> v134 -> v140 -> v146]).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v140.sh": "scripts/parity-probes/vlm-shots-v146.sh",
    "scripts/parity-probes/clone-vlmshots-v140.sh": "scripts/parity-probes/clone-vlmshots-v146.sh",
    "scripts/parity-probes/vlm-compare-v140.mjs": "scripts/parity-probes/vlm-compare-v146.mjs",
    "scripts/parity-probes/arbit-v140.sh": "scripts/parity-probes/arbit-v146.sh",
}

GENERIC = [
    ("refvlm140", "refvlm146"),
    ("clonevlm140", "clonevlm146"),
    ("refarbit140", "refarbit146"),
    ("clonearbit140", "clonearbit146"),
    ("/tmp/vlm140", "/tmp/vlm146"),
    ("v140", "v146"),
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
        "scripts/parity-probes/vlm-shots-v146.sh": [
            ("# v134, now the oldest remaining [v134 < v135 < v136 < v137 < v138]; the\n# v139 plan's v146 queue suggestion, agreeing with the rotation ledger —\n# the SIXTY-THIRD consecutive agreement).",
             "# v140, now the oldest remaining [v140 < v141 < v142 < v143 < v144]; the\n# v145 plan's v146 queue suggestion, agreeing with the rotation ledger —\n# the SIXTY-NINTH consecutive agreement)."),
        ],
        "scripts/parity-probes/clone-vlmshots-v146.sh": [
            ("# v134, now the oldest remaining [v134 < v135 < v136 < v137 < v138]; the\n# pair's THIRTEENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134 → v146]).",
             "# v140, now the oldest remaining [v140 < v141 < v142 < v143 < v144]; the\n# pair's FOURTEENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134 → v140 → v146])."),
        ],
        "scripts/parity-probes/vlm-compare-v146.mjs": [
            ("// next-oldest candidate (the v128-era savings pair's THIRTEENTH re-run — last re-shot\n// v134, now the oldest remaining [v134 < v135 < v136 < v137 < v138] — agreeing with the rotation ledger, the SIXTY-THIRD consecutive agreement).",
             "// next-oldest candidate (the v128-era savings pair's FOURTEENTH re-run — last re-shot\n// v140, now the oldest remaining [v140 < v141 < v142 < v143 < v144] — agreeing with the rotation ledger, the SIXTY-NINTH consecutive agreement)."),
        ],
        "scripts/parity-probes/arbit-v146.sh": [
            ("# the v128-era savings pair's THIRTEENTH re-run, last re-shot v134 — now the\n# oldest remaining candidate [v134 < v135 < v136 < v137 < v138]).",
             "# the v128-era savings pair's FOURTEENTH re-run, last re-shot v140 — now the\n# oldest remaining candidate [v140 < v141 < v142 < v143 < v144])."),
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
    # (→ v134 → v140 → v146) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the SURFACE-FAMILY name
    # "the v128-era savings pair" (the lineage's own designation for the
    # pair's family, preserved exactly as the v140 form preserved
    # "the v128-era savings pair"); the era marker "last re-shot v140";
    # the axis-provenance citations (the v58 axes, the v65 page-header axes,
    # the v74/v80 census axes, the v51/v54 390-only family, the v43 rule,
    # the v46 rule, the v22 lesson, the v68 seedcheck).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v134|THIRTEENTH re-run|SIXTY-THIRD|the v139 plan|"
            r"v134 < v135|refvlm140|clonevlm140|refarbit140|"
            r"clonearbit140|/tmp/vlm140",
            text,
        ):
            bad.append(m.group(0))
        # bare-v134 sweep: the corrected bracket is the sole legitimate
        # survivor
        for m in re.finditer(r"v134", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v134 → v140 → v146" in ctx:
                continue
            if "v134" not in bad:
                bad.append("v134 (outside the corrected bracket)")
        # the old oldest-remaining list tokens must be wholly gone
        # (the corrected list re-points at v140..v144)
        for m in re.finditer(r"v13[5-8]", text):
            bad.append(f"{m.group(0)} (old oldest-remaining token)")
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
