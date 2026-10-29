#!/usr/bin/env python3
"""Derive the v133 probe series from the v127 lineage (the ITEMS view
[income + expenses] at desktop 1280x800 FULL-PAGE — the v57-era items
pair's TWELFTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 →
v109 → v115 → v121 → v127 → v133]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v132-era docs' v133 queue names "the pair's TWELFTH re-run
bracket [v57 → ... → v121 → v127 → v133]... to be verified against
vlm-shots-v127.sh's own ELEVENTH/12-entry header" — verified against the
v127 header BEFORE this derivation: vlm-shots-v127.sh's own header reads
"the ELEVENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97
→ v103 → v109 → v115 → v121 → v127]" — a 12-ENTRY bracket with the
ELEVENTH ordinal (v57 the original, the entries-minus-one convention:
12 entries − the original = 11 re-runs, the ELEVENTH). v133 = the TWELFTH
re-run by appending v133 to the v127 header's ELEVENTH bracket. The
FIFTY-SIXTH consecutive queue/ledger agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm127->refvlm133, clonevlm127->clonevlm133,
     refarbit127->refarbit133, clonearbit127->clonearbit133,
     /tmp/vlm127->/tmp/vlm133, v127->v133
  2. History corrections (the era marker last-re-shot v121 -> v127, the
     re-run ordinal ELEVENTH->TWELFTH, the re-run bracket extended
     [v57 -> ... -> v121 -> v127 -> v133], the later-pairs list re-pointed
     at the CURRENT later re-runs [savings v128, login+calculator v129,
     networth+drill-down v130, budget-guidelines+quick-action v131,
     mobile twins v132] — the v127 lineage carried the v122..v126 list).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v127.sh": "scripts/parity-probes/vlm-shots-v133.sh",
    "scripts/parity-probes/clone-vlmshots-v127.sh": "scripts/parity-probes/clone-vlmshots-v133.sh",
    "scripts/parity-probes/vlm-compare-v127.mjs": "scripts/parity-probes/vlm-compare-v133.mjs",
    "scripts/parity-probes/arbit-v127.sh": "scripts/parity-probes/arbit-v133.sh",
}

GENERIC = [
    ("refvlm127", "refvlm133"),
    ("clonevlm127", "clonevlm133"),
    ("refarbit127", "refarbit133"),
    ("clonearbit127", "clonearbit133"),
    ("/tmp/vlm127", "/tmp/vlm133"),
    ("v127", "v133"),
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
        "scripts/parity-probes/vlm-shots-v133.sh": [
            ("# last re-shot v121 — the ELEVENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v133]; every other pair re-ran later [savings v122, login+calculator\n# v123, networth+drill-down v124, budget-guidelines+quick-action v125, mobile twins v126]).",
             "# last re-shot v127 — the TWELFTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133]; every other pair re-ran later [savings v128, login+calculator\n# v129, networth+drill-down v130, budget-guidelines+quick-action v131, mobile twins v132])."),
        ],
        "scripts/parity-probes/clone-vlmshots-v133.sh": [
            ("# last re-shot v121 — the ELEVENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v133]).",
             "# last re-shot v127 — the TWELFTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133])."),
        ],
        "scripts/parity-probes/vlm-compare-v133.mjs": [
            ("// OLDEST re-run candidate (the v57-era items pair, last re-shot v121 —\n// the ELEVENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v133]; every",
             "// OLDEST re-run candidate (the v57-era items pair, last re-shot v127 —\n// the TWELFTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133]; every"),
        ],
        "scripts/parity-probes/arbit-v133.sh": [
            ("# desktop 1280x800 on BOTH items views — the ELEVENTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v133]:",
             "# desktop 1280x800 on BOTH items views — the TWELFTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127 → v133]:"),
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
    # (→ v121 → v127 → v133) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the axis-provenance citations
    # (the v57 axes, the v64/v70 axes, the v65 axes, the v70b axes, the
    # v75 convention, the v79 census axes); the clone-vlmshots file needs
    # no corrections beyond its bracket (verified: zero other era tokens).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v121|ELEVENTH re-run|savings v122|login\+calculator\n# v123|"
            r"v121 < v122|refvlm127|clonevlm127|refarbit127|clonearbit127|/tmp/vlm127",
            text,
        ):
            bad.append(m.group(0))
        # bare-v121 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v121", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v121 → v127 → v133" in ctx:
                continue
            if "v121" not in bad:
                bad.append("v121 (outside the corrected bracket)")
        # the old later-pairs list tokens must be wholly gone from the shots
        # file (the corrected list re-points at v128..v132)
        if dst.endswith("vlm-shots-v133.sh"):
            for m in re.finditer(r"v12[23456]", text):
                ctx = text[max(0, m.start() - 60):m.end() + 60]
                if "→ v121 → v127 → v133" in ctx:
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
