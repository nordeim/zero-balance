#!/usr/bin/env python3
"""Derive the v134 probe series from the v128 lineage (the SAVINGS view
at desktop 1280x800 FULL-PAGE — the v58-era savings pair's TWELFTH re-run
[v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 →
v128 → v134]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v133-era docs' v134 queue names "the pair's TWELFTH re-run
bracket [v58 → ... → v122 → v128 → v134]... to be verified against the
v128 lineage's own records" — verified BEFORE this derivation: the v128
shots header carries the SHORT form (the era + the agreement ordinal, no
bracket), so the bracket source is the v128 plan's own F3 record, which
reads "the ELEVENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 →
v104 → v110 → v116 → v122 → v128]" — a 12-ENTRY bracket with the ELEVENTH
ordinal (v58 the original, the entries-minus-one convention: 12 entries −
the original = 11 re-runs, the ELEVENTH). v134 = the TWELFTH re-run by
appending v134 to that bracket. The FIFTY-SEVENTH consecutive queue/ledger
agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm128->refvlm134, clonevlm128->clonevlm134,
     refarbit128->refarbit134, clonearbit128->clonearbit134,
     /tmp/vlm128->/tmp/vlm134, v128->v134
  2. History corrections (the era marker last-re-shot v122 -> v128, the
     oldest-remaining list re-pointed [v122 < ... < v127] -> [v128 < ... <
     v132], the plan pointer "the v127 plan's" -> "the v133 plan's", the
     agreement ordinal FIFTY-FIRST -> FIFTY-SEVENTH, the re-run ordinal
     ELEVENTH -> TWELFTH, the re-run bracket extended [-> v122 -> v128] ->
     [-> v122 -> v128 -> v134] in the files that carry the bracket).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v128.sh": "scripts/parity-probes/vlm-shots-v134.sh",
    "scripts/parity-probes/clone-vlmshots-v128.sh": "scripts/parity-probes/clone-vlmshots-v134.sh",
    "scripts/parity-probes/vlm-compare-v128.mjs": "scripts/parity-probes/vlm-compare-v134.mjs",
    "scripts/parity-probes/arbit-v128.sh": "scripts/parity-probes/arbit-v134.sh",
}

GENERIC = [
    ("refvlm128", "refvlm134"),
    ("clonevlm128", "clonevlm134"),
    ("refarbit128", "refarbit134"),
    ("clonearbit128", "clonearbit134"),
    ("/tmp/vlm128", "/tmp/vlm134"),
    ("v128", "v134"),
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
        "scripts/parity-probes/vlm-shots-v134.sh": [
            ("# re-run cycle's OLDEST candidate (the v122-era savings pair, last re-shot\n# v122, now the oldest remaining [v122 < v123 < v124 < v125 < v126 < v127]; the\n# v127 plan's v134 queue suggestion, agreeing with the rotation ledger —\n# the FIFTY-FIRST consecutive agreement).",
             "# re-run cycle's OLDEST candidate (the v128-era savings pair, last re-shot\n# v128, now the oldest remaining [v128 < v129 < v130 < v131 < v132]; the\n# v133 plan's v134 queue suggestion, agreeing with the rotation ledger —\n# the FIFTY-SEVENTH consecutive agreement)."),
        ],
        "scripts/parity-probes/clone-vlmshots-v134.sh": [
            ("# re-run cycle's OLDEST candidate (the v122-era savings pair, last re-shot\n# v122, now the oldest remaining [v122 < v123 < v124 < v125 < v126 < v127]; the\n# pair's ELEVENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v134]).",
             "# re-run cycle's OLDEST candidate (the v128-era savings pair, last re-shot\n# v128, now the oldest remaining [v128 < v129 < v130 < v131 < v132]; the\n# pair's TWELFTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128 → v134])."),
        ],
        "scripts/parity-probes/vlm-compare-v134.mjs": [
            ("// next-oldest candidate (the v122-era savings pair's ELEVENTH re-run — last re-shot\n// v122, now the oldest remaining [v122 < v123 < v124 < v125 < v126 < v127] — agreeing with the rotation ledger, the FIFTY-FIRST consecutive agreement).",
             "// next-oldest candidate (the v128-era savings pair's TWELFTH re-run — last re-shot\n// v128, now the oldest remaining [v128 < v129 < v130 < v131 < v132] — agreeing with the rotation ledger, the FIFTY-SEVENTH consecutive agreement)."),
        ],
        "scripts/parity-probes/arbit-v134.sh": [
            ("# the v122-era savings pair's ELEVENTH re-run, last re-shot v122 — now the\n# oldest remaining candidate [v122 < v123 < v124 < v125 < v126 < v127]).",
             "# the v128-era savings pair's TWELFTH re-run, last re-shot v128 — now the\n# oldest remaining candidate [v128 < v129 < v130 < v131 < v132])."),
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
    # (→ v122 → v128 → v134) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the axis-provenance citations
    # (the v58 axes, the v65 page-header axes, the v74/v80 census axes,
    # the v98-era pin candidate citation, the v51/v54 390-only family,
    # the v43 rule, the v46 rule, the v22 lesson, the v68 seedcheck).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v122|v122-era|ELEVENTH re-run|FORTY-FIFTH|FIFTY-FIRST|"
            r"v122 < v123|the v127 plan|refvlm128|clonevlm128|refarbit128|"
            r"clonearbit128|/tmp/vlm128",
            text,
        ):
            bad.append(m.group(0))
        # bare-v122 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v122", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v122 → v128 → v134" in ctx:
                continue
            if "v122" not in bad:
                bad.append("v122 (outside the corrected bracket)")
        # the old later-pairs list tokens must be wholly gone from the shots
        # file (the corrected list re-points at v129..v132)
        if dst.endswith("vlm-shots-v134.sh"):
            for m in re.finditer(r"v12[34567]", text):
                ctx = text[max(0, m.start() - 60):m.end() + 60]
                if "→ v122 → v128 → v134" in ctx:
                    continue
                bad.append(f"{m.group(0)} (old later-pairs token)")
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
