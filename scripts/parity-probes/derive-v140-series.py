#!/usr/bin/env python3
"""Derive the v140 probe series from the v134 lineage (the SAVINGS view
at desktop 1280x800 FULL-PAGE — the v58-era savings pair's THIRTEENTH
re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 →
v122 → v128 → v134 → v140]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v139-era docs' v140 queue names "the pair's THIRTEENTH
re-run bracket [v58 → ... → v128 → v134 → v140]... to be verified against
the v134 lineage's own records" — verified against the v134 lineage's own
records BEFORE this derivation: the v134 plan's own header reads "the
v128-era SAVINGS pair's TWELFTH re-run [v58 → v65 → v74 → v80 → v86 → v92 →
v98 → v104 → v110 → v116 → v122 → v128 → v134]" — a 13-ENTRY bracket with
the TWELFTH ordinal (v58 the original, the entries-minus-one convention:
13 entries − the original = 12 re-runs, the TWELFTH). v140 = the
THIRTEENTH re-run by appending v140 to the v134 header's TWELFTH bracket.
The SIXTY-THIRD consecutive queue/ledger agreement. The v127–v132
rotation pool is EXHAUSTED; the cadence is in its SECOND PASS (the
v133–v138 pool), the v134-era SAVINGS pair the oldest remaining
[v134 < v135 < v136 < v137 < v138].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm134->refvlm140, clonevlm134->clonevlm140,
     refarbit134->refarbit140, clonearbit134->clonearbit140,
     /tmp/vlm134->/tmp/vlm140, v134->v140
  2. History corrections (the era marker last-re-shot v128 -> v134 + the
     oldest-remaining list v128..v132 -> v134..v138 + the queue source
     the v133 plan -> the v139 plan + the agreement counter
     FIFTY-SEVENTH -> SIXTY-THIRD; the re-run ordinal TWELFTH->THIRTEENTH,
     the re-run bracket extended [v58 -> ... -> v128 -> v134 -> v140]).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v134.sh": "scripts/parity-probes/vlm-shots-v140.sh",
    "scripts/parity-probes/clone-vlmshots-v134.sh": "scripts/parity-probes/clone-vlmshots-v140.sh",
    "scripts/parity-probes/vlm-compare-v134.mjs": "scripts/parity-probes/vlm-compare-v140.mjs",
    "scripts/parity-probes/arbit-v134.sh": "scripts/parity-probes/arbit-v140.sh",
}

GENERIC = [
    ("refvlm134", "refvlm140"),
    ("clonevlm134", "clonevlm140"),
    ("refarbit134", "refarbit140"),
    ("clonearbit134", "clonearbit140"),
    ("/tmp/vlm134", "/tmp/vlm140"),
    ("v134", "v140"),
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
        "scripts/parity-probes/vlm-shots-v140.sh": [
            ("# re-run cycle's OLDEST candidate (the v128-era savings pair, last re-shot\n# v128, now the oldest remaining [v128 < v129 < v130 < v131 < v132]; the\n# v133 plan's v140 queue suggestion, agreeing with the rotation ledger —\n# the FIFTY-SEVENTH consecutive agreement).",
             "# re-run cycle's OLDEST candidate (the v128-era savings pair, last re-shot\n# v134, now the oldest remaining [v134 < v135 < v136 < v137 < v138]; the\n# v139 plan's v140 queue suggestion, agreeing with the rotation ledger —\n# the SIXTY-THIRD consecutive agreement)."),
        ],
        "scripts/parity-probes/clone-vlmshots-v140.sh": [
            ("# re-run cycle's OLDEST candidate (the v128-era savings pair, last re-shot\n# v128, now the oldest remaining [v128 < v129 < v130 < v131 < v132]; the\n# pair's TWELFTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v140]).",
             "# re-run cycle's OLDEST candidate (the v128-era savings pair, last re-shot\n# v134, now the oldest remaining [v134 < v135 < v136 < v137 < v138]; the\n# pair's THIRTEENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134 → v140])."),
        ],
        "scripts/parity-probes/vlm-compare-v140.mjs": [
            ("// next-oldest candidate (the v128-era savings pair's TWELFTH re-run — last re-shot\n// v128, now the oldest remaining [v128 < v129 < v130 < v131 < v132] — agreeing with the rotation ledger, the FIFTY-SEVENTH consecutive agreement).",
             "// next-oldest candidate (the v128-era savings pair's THIRTEENTH re-run — last re-shot\n// v134, now the oldest remaining [v134 < v135 < v136 < v137 < v138] — agreeing with the rotation ledger, the SIXTY-THIRD consecutive agreement)."),
        ],
        "scripts/parity-probes/arbit-v140.sh": [
            ("# the v128-era savings pair's TWELFTH re-run, last re-shot v128 — now the\n# oldest remaining candidate [v128 < v129 < v130 < v131 < v132]).",
             "# the v128-era savings pair's THIRTEENTH re-run, last re-shot v134 — now the\n# oldest remaining candidate [v134 < v135 < v136 < v137 < v138])."),
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
    # (→ v128 → v134 → v140) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the SURFACE-FAMILY name
    # "the v128-era savings pair" (the lineage's own designation for the
    # pair's family, preserved exactly as the v139 form preserved
    # "the v57-era items pair"); the era marker "last re-shot v134";
    # the axis-provenance citations (the v58 axes, the v65 page-header axes,
    # the v74/v80 census axes, the v51/v54 390-only family, the v43 rule,
    # the v46 rule, the v22 lesson, the v68 seedcheck).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v128|TWELFTH re-run|FIFTY-SEVENTH|the v133 plan|"
            r"v128 < v129|refvlm134|clonevlm134|refarbit134|"
            r"clonearbit134|/tmp/vlm134",
            text,
        ):
            bad.append(m.group(0))
        # bare-v128 sweep: the corrected bracket + the family name are the
        # sole legitimate survivors
        for m in re.finditer(r"v128", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v128 → v134 → v140" in ctx:
                continue
            if "v128-era savings pair" in ctx:
                continue
            if "v128" not in bad:
                bad.append("v128 (outside the corrected bracket/family name)")
        # the old oldest-remaining list tokens must be wholly gone
        # (the corrected list re-points at v134..v138)
        for m in re.finditer(r"v12[89]|v13[012]", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v128 → v134 → v140" in ctx:
                continue
            if "v128-era savings pair" in ctx:
                continue
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
