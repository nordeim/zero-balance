#!/usr/bin/env python3
"""Derive the v139 probe series from the v133 lineage (the ITEMS view
[income + expenses] at desktop 1280x800 FULL-PAGE — the v57-era items
pair's THIRTEENTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 →
v109 → v115 → v121 → v127 → v133 → v139]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v138-era docs' v139 queue names "the pair's THIRTEENTH
re-run bracket [v57 → ... → v127 → v133 → v139]... to be verified against
the v133 plan's own header" — verified against the v133 lineage's own
records BEFORE this derivation: the v133 plan's own header reads "the
v127-era ITEMS pair's TWELFTH re-run [v57 → v64 → v70 → v79 → v85 → v91 →
v97 → v103 → v109 → v115 → v121 → v127 → v133]" — a 13-ENTRY bracket with
the TWELFTH ordinal (v57 the original, the entries-minus-one convention:
13 entries − the original = 12 re-runs, the TWELFTH). v139 = the
THIRTEENTH re-run by appending v139 to the v133 header's TWELFTH bracket.
The SIXTY-SECOND consecutive queue/ledger agreement. The v127–v132
rotation pool is EXHAUSTED; the cadence is in its SECOND PASS (the
v133–v138 pool), the v133-era ITEMS pair the oldest remaining
[v133 < v134 < v135 < v136 < v137 < v138].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm133->refvlm139, clonevlm133->clonevlm139,
     refarbit133->refarbit139, clonearbit133->clonearbit139,
     /tmp/vlm133->/tmp/vlm139, v133->v139
  2. History corrections (the era marker last-re-shot v127 -> v133, the
     re-run ordinal TWELFTH->THIRTEENTH, the re-run bracket extended
     [v57 -> ... -> v127 -> v133 -> v139], the later-pairs list re-pointed
     at the CURRENT later re-runs [savings v134, login+calculator v135,
     networth+drill-down v136, budget-guidelines+quick-action v137,
     mobile twins v138] — the v133 lineage carried the v128..v132 list).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v133.sh": "scripts/parity-probes/vlm-shots-v139.sh",
    "scripts/parity-probes/clone-vlmshots-v133.sh": "scripts/parity-probes/clone-vlmshots-v139.sh",
    "scripts/parity-probes/vlm-compare-v133.mjs": "scripts/parity-probes/vlm-compare-v139.mjs",
    "scripts/parity-probes/arbit-v133.sh": "scripts/parity-probes/arbit-v139.sh",
}

GENERIC = [
    ("refvlm133", "refvlm139"),
    ("clonevlm133", "clonevlm139"),
    ("refarbit133", "refarbit139"),
    ("clonearbit133", "clonearbit139"),
    ("/tmp/vlm133", "/tmp/vlm139"),
    ("v133", "v139"),
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
        "scripts/parity-probes/vlm-shots-v139.sh": [
            ("# last re-shot v127 — the TWELFTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v139]; every other pair re-ran later [savings v128, login+calculator\n# v129, networth+drill-down v130, budget-guidelines+quick-action v131, mobile twins v132]).",
             "# last re-shot v133 — the THIRTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139]; every other pair re-ran later [savings v134, login+calculator\n# v135, networth+drill-down v136, budget-guidelines+quick-action v137, mobile twins v138])."),
        ],
        "scripts/parity-probes/clone-vlmshots-v139.sh": [
            ("# last re-shot v127 — the TWELFTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v139]).",
             "# last re-shot v133 — the THIRTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139])."),
        ],
        "scripts/parity-probes/vlm-compare-v139.mjs": [
            ("// OLDEST re-run candidate (the v57-era items pair, last re-shot v127 —\n// the TWELFTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v139]; every",
             "// OLDEST re-run candidate (the v57-era items pair, last re-shot v133 —\n// the THIRTEENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139]; every"),
        ],
        "scripts/parity-probes/arbit-v139.sh": [
            ("# desktop 1280x800 on BOTH items views — the TWELFTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v139]:",
             "# desktop 1280x800 on BOTH items views — the THIRTEENTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133 → v139]:"),
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
    # (→ v121 → v127 → v133 → v139) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the era marker "last re-shot v133";
    # the axis-provenance citations (the v57 axes, the v64/v70 axes, the
    # v65 axes, the v70b axes, the v75 convention, the v79 census axes).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v127|TWELFTH re-run|savings v128|login\+calculator\n# v129|"
            r"v133 < v134|refvlm133|clonevlm133|refarbit133|clonearbit133|/tmp/vlm133",
            text,
        ):
            bad.append(m.group(0))
        # bare-v127 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v127", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v127 → v133 → v139" in ctx:
                continue
            if "v127" not in bad:
                bad.append("v127 (outside the corrected bracket)")
        # the old later-pairs list tokens must be wholly gone from the shots
        # file (the corrected list re-points at v134..v138)
        if dst.endswith("vlm-shots-v139.sh"):
            for m in re.finditer(r"v12[89]|v13[012]", text):
                ctx = text[max(0, m.start() - 60):m.end() + 60]
                if "→ v127 → v133 → v139" in ctx:
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
