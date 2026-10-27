#!/usr/bin/env python3
"""Derive the v127 probe series from the v121 lineage (the ITEMS view
[income + expenses] at desktop 1280x800 FULL-PAGE — the v57-era items
pair's ELEVENTH re-run [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 →
v109 → v115 → v121 → v127]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v126-era docs' v127 queue names "the v121-era ITEMS pair ...
the ELEVENTH re-run by the entries-minus-one convention derived from
vlm-shots-v121.sh's own TENTH/11-entry header" — verified against the v121
header BEFORE this derivation: vlm-shots-v121.sh's own header reads "the
TENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 →
v109 → v115 → v121]" — an 11-ENTRY bracket with the TENTH ordinal (v57 the
original, the entries-minus-one convention: 11 entries − the original = 10
re-runs, the TENTH). v127 = the ELEVENTH re-run by appending v127 to the
v121 header's TENTH bracket. The FIFTIETH consecutive queue/ledger
agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm121->refvlm127, clonevlm121->clonevlm127,
     refarbit121->refarbit127, clonearbit121->clonearbit127,
     /tmp/vlm121->/tmp/vlm127, v121->v127
  2. History corrections (the era marker last-re-shot v115 -> v121, the
     re-run ordinal TENTH->ELEVENTH, the re-run bracket extended
     [v57 -> ... -> v115 -> v121 -> v127], the later-pairs list re-pointed
     at the CURRENT later re-runs [savings v122, login+calculator v123,
     networth+drill-down v124, budget-guidelines+quick-action v125,
     mobile twins v126] — the v121 lineage carried the v116..v120 list).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v121.sh": "scripts/parity-probes/vlm-shots-v127.sh",
    "scripts/parity-probes/clone-vlmshots-v121.sh": "scripts/parity-probes/clone-vlmshots-v127.sh",
    "scripts/parity-probes/vlm-compare-v121.mjs": "scripts/parity-probes/vlm-compare-v127.mjs",
    "scripts/parity-probes/arbit-v121.sh": "scripts/parity-probes/arbit-v127.sh",
}

GENERIC = [
    ("refvlm121", "refvlm127"),
    ("clonevlm121", "clonevlm127"),
    ("refarbit121", "refarbit127"),
    ("clonearbit121", "clonearbit127"),
    ("/tmp/vlm121", "/tmp/vlm127"),
    ("v121", "v127"),
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
        "scripts/parity-probes/vlm-shots-v127.sh": [
            ("# last re-shot v115 — the TENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v127]; every other pair re-ran later [savings v116, login+calculator\n# v117, networth+drill-down v118, budget-guidelines+quick-action v119, mobile twins v120]).",
             "# last re-shot v121 — the ELEVENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127]; every other pair re-ran later [savings v122, login+calculator\n# v123, networth+drill-down v124, budget-guidelines+quick-action v125, mobile twins v126])."),
        ],
        "scripts/parity-probes/clone-vlmshots-v127.sh": [
            ("# last re-shot v115 — the TENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v127]).",
             "# last re-shot v121 — the ELEVENTH re-run of the pair [v57 → v64 → v70 → v79 → v85\n# → v91 → v97 → v103 → v109 → v115 → v121 → v127])."),
        ],
        "scripts/parity-probes/vlm-compare-v127.mjs": [
            ("// OLDEST re-run candidate (the v57-era items pair, last re-shot v115 —\n// the TENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v127]; every",
             "// OLDEST re-run candidate (the v57-era items pair, last re-shot v121 —\n// the ELEVENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127]; every"),
        ],
        "scripts/parity-probes/arbit-v127.sh": [
            ("# desktop 1280x800 on BOTH items views — the TENTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v127]:",
             "# desktop 1280x800 on BOTH items views — the ELEVENTH re-run of the pair\n# [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121 → v127]:"),
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
    # (→ v115 → v121 → v127) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the axis-provenance citations
    # (the v57 axes, the v64/v70 axes, the v65 axes, the v70b axes, the
    # v75 convention, the v79 census axes); the clone-vlmshots file needs
    # no corrections beyond its bracket (verified: zero other era tokens).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v115|TENTH re-run|savings v116|login\+calculator\n# v117|"
            r"v115 < v116|refvlm121|clonevlm121|refarbit121|clonearbit121|/tmp/vlm121",
            text,
        ):
            bad.append(m.group(0))
        # bare-v115 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v115", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v115 → v121 → v127" in ctx:
                continue
            if "v115" not in bad:
                bad.append("v115 (outside the corrected bracket)")
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
