#!/usr/bin/env python3
"""Derive the v145 probe series from the v139 lineage (the ITEMS view
[income + expenses] at desktop 1280x800 FULL-PAGE — the v57-era items
pair's FOURTEENTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 →
v109 → v115 → v121 → v127 → v133 → v139 → v145]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v144-era docs' v145 queue names "the pair's FOURTEENTH
re-run bracket [v57 → ... → v133 → v139 → v145]... to be verified against
the v139 lineage's own records" — verified against the v139 lineage's own
records BEFORE this derivation: the v139 plan's own header reads "the
v133-era ITEMS pair's THIRTEENTH re-run [v57 → v64 → v70 → v79 → v85 → v91
→ v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139]" — a 14-ENTRY
bracket with the THIRTEENTH ordinal (v57 the original, the
entries-minus-one convention: 14 entries − the original = 13 re-runs, the
THIRTEENTH). v145 = the FOURTEENTH re-run by appending v145 to the v139
header's THIRTEENTH bracket. The SIXTY-EIGHTH consecutive queue/ledger
agreement. The v133–v138 rotation pool is EXHAUSTED; the cadence is in its
THIRD PASS (the v139–v144 pool), the v139-era ITEMS pair the oldest
remaining [v139 < v140 < v141 < v142 < v143 < v144].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm139->refvlm145, clonevlm139->clonevlm145,
     refarbit139->refarbit145, clonearbit139->clonearbit145,
     /tmp/vlm139->/tmp/vlm145, v139->v145
  2. History corrections (the era marker last-re-shot v133 -> v139, the
     re-run ordinal THIRTEENTH->FOURTEENTH, the re-run bracket extended
     [v57 -> ... -> v133 -> v139 -> v145], the later-pairs list re-pointed
     at the CURRENT later re-runs [savings v140, login+calculator v141,
     networth+drill-down v142, budget-guidelines+quick-action v143,
     mobile twins v144] — the v139 lineage carried the v134..v138 list).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v139.sh": "scripts/parity-probes/vlm-shots-v145.sh",
    "scripts/parity-probes/clone-vlmshots-v139.sh": "scripts/parity-probes/clone-vlmshots-v145.sh",
    "scripts/parity-probes/vlm-compare-v139.mjs": "scripts/parity-probes/vlm-compare-v145.mjs",
    "scripts/parity-probes/arbit-v139.sh": "scripts/parity-probes/arbit-v145.sh",
}

GENERIC = [
    ("refvlm139", "refvlm145"),
    ("clonevlm139", "clonevlm145"),
    ("refarbit139", "refarbit145"),
    ("clonearbit139", "clonearbit145"),
    ("/tmp/vlm139", "/tmp/vlm145"),
    ("v139", "v145"),
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
        "scripts/parity-probes/vlm-shots-v145.sh": [
            ("# last re-shot v133 — the THIRTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v145]; every other pair re-ran later [savings v134, login+calculator\n# v135, networth+drill-down v136, budget-guidelines+quick-action v137, mobile twins v138]).",
             "# last re-shot v139 — the FOURTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v145]; every other pair re-ran later [savings v140, login+calculator\n# v141, networth+drill-down v142, budget-guidelines+quick-action v143, mobile twins v144])."),
        ],
        "scripts/parity-probes/clone-vlmshots-v145.sh": [
            ("# last re-shot v133 — the THIRTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v145]).",
             "# last re-shot v139 — the FOURTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v145])."),
        ],
        "scripts/parity-probes/vlm-compare-v145.mjs": [
            ("// OLDEST re-run candidate (the v57-era items pair, last re-shot v133 —\n// the THIRTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v145]; every",
             "// OLDEST re-run candidate (the v57-era items pair, last re-shot v139 —\n// the FOURTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v145]; every"),
        ],
        "scripts/parity-probes/arbit-v145.sh": [
            ("# desktop 1280x800 on BOTH items views — the THIRTEENTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v145]:",
             "# desktop 1280x800 on BOTH items views — the FOURTEENTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v145]:"),
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
    # (→ v133 → v139 → v145) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the era marker "last re-shot v139";
    # the axis-provenance citations (the v57 axes, the v64/v70 axes, the
    # v65 axes, the v70b axes, the v75 convention, the v79 census axes).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v133|THIRTEENTH re-run|savings v134|login\+calculator\n# v135|"
            r"v139 < v140|refvlm139|clonevlm139|refarbit139|clonearbit139|/tmp/vlm139",
            text,
        ):
            bad.append(m.group(0))
        # bare-v133 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v133", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v133 → v139 → v145" in ctx:
                continue
            if "v133" not in bad:
                bad.append("v133 (outside the corrected bracket)")
        # the old later-pairs list tokens must be wholly gone from the shots
        # file (the corrected list re-points at v140..v144)
        if dst.endswith("vlm-shots-v145.sh"):
            for m in re.finditer(r"v13[45678]", text):
                ctx = text[max(0, m.start() - 60):m.end() + 60]
                if "→ v133 → v139 → v145" in ctx:
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
