#!/usr/bin/env python3
"""Derive the v128 probe series from the v122 lineage (the SAVINGS view
at desktop 1280x800 FULL-PAGE — the v58-era savings pair's ELEVENTH
re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 →
v122 → v128]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v127-era docs' v128 queue names "the v122-era SAVINGS pair ...
the ELEVENTH re-run by the entries-minus-one convention derived from
vlm-shots-v122.sh's own header" — verified against the v122 lineage BEFORE
this derivation by tracing the era chain through the headers: vlm-shots-v122.sh
reads "the v116-era savings pair, last re-shot v116" -> vlm-shots-v116.sh
reads "the v110-era ..." -> ... -> vlm-shots-v80.sh reads "the v58-era ..."
(the chain v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> v104 -> v110 ->
v116 -> v122 = 11 entries, v58 the original), and the v122 plan's own title
reads "the v116-era SAVINGS pair's TENTH re-run" — the TENTH ordinal on the
11-entry bracket, consistent, no off-by-one this lineage. v128 = the ELEVENTH
re-run by appending v128 to that bracket. The FIFTY-FIRST consecutive
queue/ledger agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm122->refvlm128, clonevlm122->clonevlm128,
     refarbit122->refarbit128, clonearbit122->clonearbit128,
     /tmp/vlm122->/tmp/vlm128, v122->v128
  2. History corrections (the era marker last-re-shot v116 -> v122 + the
     oldest-remaining bracket [v116 < ... < v121] -> [v122 < ... < v127],
     the re-run ordinal TENTH -> ELEVENTH + the re-run bracket extended
     [v58 -> ... -> v116 -> v122 -> v128], the plan pointer the v121 plan
     -> the v127 plan, the agreement ordinal FORTY-FIFTH -> FIFTY-FIRST).
     NOTE: the v122 lineage carries NO later-pairs list (simpler than the
     v121 lineage) — verified by the pre-derivation sweep.

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v122.sh": "scripts/parity-probes/vlm-shots-v128.sh",
    "scripts/parity-probes/clone-vlmshots-v122.sh": "scripts/parity-probes/clone-vlmshots-v128.sh",
    "scripts/parity-probes/vlm-compare-v122.mjs": "scripts/parity-probes/vlm-compare-v128.mjs",
    "scripts/parity-probes/arbit-v122.sh": "scripts/parity-probes/arbit-v128.sh",
}

GENERIC = [
    ("refvlm122", "refvlm128"),
    ("clonevlm122", "clonevlm128"),
    ("refarbit122", "refarbit128"),
    ("clonearbit122", "clonearbit128"),
    ("/tmp/vlm122", "/tmp/vlm128"),
    ("v122", "v128"),
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
        "scripts/parity-probes/vlm-shots-v128.sh": [
            ("# re-run cycle's OLDEST candidate (the v116-era savings pair, last re-shot\n# v116, now the oldest remaining [v116 < v117 < v118 < v119 < v120 < v121]; the\n# v121 plan's v128 queue suggestion, agreeing with the rotation ledger —\n# the FORTY-FIFTH consecutive agreement).",
             "# re-run cycle's OLDEST candidate (the v122-era savings pair, last re-shot\n# v122, now the oldest remaining [v122 < v123 < v124 < v125 < v126 < v127]; the\n# v127 plan's v128 queue suggestion, agreeing with the rotation ledger —\n# the FIFTY-FIRST consecutive agreement)."),
        ],
        "scripts/parity-probes/clone-vlmshots-v128.sh": [
            ("# re-run cycle's OLDEST candidate (the v116-era savings pair, last re-shot\n# v116, now the oldest remaining [v116 < v117 < v118 < v119 < v120 < v121]; the\n# pair's TENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v128]).",
             "# re-run cycle's OLDEST candidate (the v122-era savings pair, last re-shot\n# v122, now the oldest remaining [v122 < v123 < v124 < v125 < v126 < v127]; the\n# pair's ELEVENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122 → v128])."),
        ],
        "scripts/parity-probes/vlm-compare-v128.mjs": [
            ("// next-oldest candidate (the v116-era savings pair's TENTH re-run — last re-shot\n// v116, now the oldest remaining [v116 < v117 < v118 < v119 < v120 < v121] — agreeing with the rotation ledger, the FORTY-FIFTH consecutive agreement).",
             "// next-oldest candidate (the v122-era savings pair's ELEVENTH re-run — last re-shot\n// v122, now the oldest remaining [v122 < v123 < v124 < v125 < v126 < v127] — agreeing with the rotation ledger, the FIFTY-FIRST consecutive agreement)."),
        ],
        "scripts/parity-probes/arbit-v128.sh": [
            ("# the v116-era savings pair's TENTH re-run, last re-shot v116 — now the\n# oldest remaining candidate [v116 < v117 < v118 < v119 < v120 < v121]).",
             "# the v122-era savings pair's ELEVENTH re-run, last re-shot v122 — now the\n# oldest remaining candidate [v122 < v123 < v124 < v125 < v126 < v127])."),
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
    # (→ v116 → v122 → v128) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the axis-provenance citations
    # (the v58 axes, the v65 page-header axes, the v74/v80 census axes,
    # the v98-era pin candidate citation, the v51/v54 390-only family).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v116|v116-era|TENTH re-run|FORTY-FIFTH|v116 < v117|"
            r"refvlm122|clonevlm122|refarbit122|clonearbit122|/tmp/vlm122|"
            r"the v121 plan",
            text,
        ):
            bad.append(m.group(0))
        # bare-v116 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v116", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v116 → v122 → v128" in ctx:
                continue
            if "v116" not in bad:
                bad.append("v116 (outside the corrected bracket)")
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
