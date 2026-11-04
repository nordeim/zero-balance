#!/usr/bin/env python3
"""Derive the v151 probe series from the v145 lineage (the ITEMS view
[income + expenses] at desktop 1280x800 FULL-PAGE — the v57-era items
pair's FIFTEENTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 →
v109 → v115 → v121 → v127 → v133 → v139 → v145 → v151]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v150-era docs' v151 queue names "the pair's FIFTEENTH
re-run bracket [v57 → ... → v139 → v145 → v151]... to be verified against
the v145 lineage's own records" — verified against the v145 lineage's own
records BEFORE this derivation: the v145 plan's own header reads "the
v139-era ITEMS pair's FOURTEENTH re-run [v57 → v64 → v70 → v79 → v85 → v91
→ v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v145]" — a
15-ENTRY bracket with the FOURTEENTH ordinal (v57 the original, the
entries-minus-one convention: 15 entries − the original = 14 re-runs, the
FOURTEENTH). v151 = the FIFTEENTH re-run by appending v151 to the v145
header's FOURTEENTH bracket. The SEVENTY-FOURTH consecutive queue/ledger
agreement. The v139–v144 rotation pool is EXHAUSTED (through v150); the
cadence is in its THIRD PASS (the v145–v150 pool), the v145-era ITEMS pair
the oldest remaining [v145 < v146 < v147 < v148 < v149 < v150].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm145->refvlm151, clonevlm145->clonevlm151,
     refarbit145->refarbit151, clonearbit145->clonearbit151,
     /tmp/vlm145->/tmp/vlm151, v145->v151
  2. History corrections (the era marker last-re-shot v139 -> v145, the
     re-run ordinal FOURTEENTH->FIFTEENTH, the re-run bracket extended
     [v57 -> ... -> v139 -> v145 -> v151], the later-pairs list re-pointed
     at the CURRENT later re-runs [savings v146, login+calculator v147,
     networth+drill-down v148, dashboard v149, mobile twins v150] — the
     v145 lineage carried the v140..v144 list).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v145.sh": "scripts/parity-probes/vlm-shots-v151.sh",
    "scripts/parity-probes/clone-vlmshots-v145.sh": "scripts/parity-probes/clone-vlmshots-v151.sh",
    "scripts/parity-probes/vlm-compare-v145.mjs": "scripts/parity-probes/vlm-compare-v151.mjs",
    "scripts/parity-probes/arbit-v145.sh": "scripts/parity-probes/arbit-v151.sh",
}

GENERIC = [
    ("refvlm145", "refvlm151"),
    ("clonevlm145", "clonevlm151"),
    ("refarbit145", "refarbit151"),
    ("clonearbit145", "clonearbit151"),
    ("/tmp/vlm145", "/tmp/vlm151"),
    ("v145", "v151"),
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
        "scripts/parity-probes/vlm-shots-v151.sh": [
            ("# last re-shot v139 — the FOURTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v151]; every other pair re-ran later [savings v140, login+calculator\n# v141, networth+drill-down v142, budget-guidelines+quick-action v143, mobile twins v144]).",
             "# last re-shot v145 — the FIFTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v145 → v151]; every other pair re-ran later [savings v146, login+calculator\n# v147, networth+drill-down v148, dashboard v149, mobile twins v150])."),
        ],
        "scripts/parity-probes/clone-vlmshots-v151.sh": [
            ("# last re-shot v139 — the FOURTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v151]).",
             "# last re-shot v145 — the FIFTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v145 → v151])."),
        ],
        "scripts/parity-probes/vlm-compare-v151.mjs": [
            ("// OLDEST re-run candidate (the v57-era items pair, last re-shot v139 —\n// the FOURTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v151]; every",
             "// OLDEST re-run candidate (the v57-era items pair, last re-shot v145 —\n// the FIFTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v145 → v151]; every"),
        ],
        "scripts/parity-probes/arbit-v151.sh": [
            ("# desktop 1280x800 on BOTH items views — the FOURTEENTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v151]:",
             "# desktop 1280x800 on BOTH items views — the FIFTEENTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139 → v145 → v151]:"),
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
    # (→ v133 → v139 → v145 → v151) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the era marker "last re-shot v145";
    # the axis-provenance citations (the v57 axes, the v64/v70 axes, the
    # v65 axes, the v70b axes, the v75 convention, the v79 census axes).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v139|FOURTEENTH re-run|savings v140|login\+calculator\n# v141|"
            r"v145 < v146|refvlm145|clonevlm145|refarbit145|clonearbit145|/tmp/vlm145",
            text,
        ):
            bad.append(m.group(0))
        # bare-v139 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v139", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v133 → v139 → v145 → v151" in ctx:
                continue
            if "v139" not in bad:
                bad.append("v139 (outside the corrected bracket)")
        # the old later-pairs list tokens (v140..v144) must be wholly gone
        # from the shots file (the corrected list re-points at v146..v150)
        if dst.endswith("vlm-shots-v151.sh"):
            for m in re.finditer(r"v14[0-4]", text):
                ctx = text[max(0, m.start() - 60):m.end() + 60]
                if "→ v133 → v139 → v145 → v151" in ctx:
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
