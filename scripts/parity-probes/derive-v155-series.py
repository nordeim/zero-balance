#!/usr/bin/env python3
"""Derive the v155 probe series from the v149 lineage (the DASHBOARD at
desktop 1280x800 FULL-PAGE — the v149-era DASHBOARD pair's FIFTEENTH re-run
[v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 →
v131 → v137 → v143 → v149 → v155]; the files keep the lineage's own "the
v143-era pair" family designation, preserved exactly as the v149 form
preserved it from the v143 lineage).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v154-era docs' v155 queue names "the v149-era DASHBOARD
pair ... the pair's FIFTEENTH re-run bracket [v61 → ... → v143 → v149 →
v155] to be verified against the v149 lineage's own records" — verified
against the v149 lineage BEFORE this derivation: the v149 plan's own
header reads "the v143-era DASHBOARD pair's FOURTEENTH re-run [v61 → v68
→ v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 →
v137 → v143 → v149]" — a 15-ENTRY bracket with the FOURTEENTH ordinal
(v61 the original, the entries-minus-one convention: 15 entries − the
original = 14 re-runs, the FOURTEENTH). v155 = the FIFTEENTH re-run by
appending v155 to the v149 header's FOURTEENTH bracket. The
SEVENTY-EIGHTH consecutive queue/ledger agreement. The cadence is in its
THIRD PASS, the v149-era DASHBOARD pair the oldest remaining
[v149 < v150 < v151 < v152 < v153].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm149->refvlm155, clonevlm149->clonevlm155,
     refar149->refar155, clonear149->clonear155
     (the FOUR EXPLICIT session-token swaps — the tokens carry '149'
     without the 'v' prefix, so the bare version swap cannot touch them;
     the v121-cycle stale-session-fix precedent), /tmp/vlm149->/tmp/vlm155,
     v149->v155
  2. History corrections (the era marker last-re-shot v143 -> v149 + the
     oldest-remaining list [v143 < v144] -> [v149 < v150 < v151 < v152 <
     v153], the agreement ordinal SEVENTY-SECOND -> SEVENTY-EIGHTH; the
     re-run ordinal FOURTEENTH -> FIFTEENTH, the re-run bracket extended
     [-> v131 -> v137 -> v143 -> v155] -> [-> v131 -> v137 -> v143 ->
     v149 -> v155]; the re-proves-after windows v101-v143 -> v101-v149;
     the arbit census provenance "a drift re-check since v143" ->
     "since v149" + "The v143 verdict was IDENTICAL" -> "The v149
     verdict was IDENTICAL"; the compare banner's FOURTEENTH ->
     FIFTEENTH).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v149.sh": "scripts/parity-probes/vlm-shots-v155.sh",
    "scripts/parity-probes/clone-vlmshots-v149.sh": "scripts/parity-probes/clone-vlmshots-v155.sh",
    "scripts/parity-probes/vlm-compare-v149.mjs": "scripts/parity-probes/vlm-compare-v155.mjs",
    "scripts/parity-probes/arbit-v149.sh": "scripts/parity-probes/arbit-v155.sh",
}

GENERIC = [
    ("refvlm149", "refvlm155"),
    ("clonevlm149", "clonevlm155"),
    ("refar149", "refar155"),
    ("clonear149", "clonear155"),
    ("/tmp/vlm149", "/tmp/vlm155"),
    ("v149", "v155"),
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
        "scripts/parity-probes/vlm-shots-v155.sh": [
            ("last re-shot v143 — now\n# the oldest remaining [v143 < v144]; the pair's FOURTEENTH",
             "last re-shot v149 — now\n# the oldest remaining [v149 < v150 < v151 < v152 < v153]; the pair's FIFTEENTH"),
            ("re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v155] — the SEVENTY-SECOND consecutive",
             "re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v149 → v155] — the SEVENTY-EIGHTH consecutive"),
            ("v61-era surfaces after\n# v101-v143 (",
             "v61-era surfaces after\n# v101-v149 ("),
        ],
        "scripts/parity-probes/clone-vlmshots-v155.sh": [
            ("the pair's FOURTEENTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v155]): the DASHBOARD",
             "the pair's FIFTEENTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v149 → v155]): the DASHBOARD"),
            ("re-proved again by the v155 re-run after v101-v143). Runs",
             "re-proved again by the v155 re-run after v101-v149). Runs"),
        ],
        "scripts/parity-probes/vlm-compare-v155.mjs": [
            ("the v143-era pair FOURTEENTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v155] — the SEVENTY-SECOND consecutive queue/ledger",
             "the v143-era pair FIFTEENTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v149 → v155] — the SEVENTY-EIGHTH consecutive queue/ledger"),
            ("the v155 FOURTEENTH re-run of the v143-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v155]",
             "the v155 FIFTEENTH re-run of the v143-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v149 → v155]"),
        ],
        "scripts/parity-probes/arbit-v155.sh": [
            ("the v143-era pair's FOURTEENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v155]",
             "the v143-era pair's FIFTEENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131 → v137 → v143 → v149 → v155]"),
            ("last re-shot v143). The v143\n# verdict was IDENTICAL with ZERO style flags",
             "last re-shot v149). The v149\n# verdict was IDENTICAL with ZERO style flags"),
            ("a drift re-check\n# since v143):",
             "a drift re-check\n# since v149):"),
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
    # (→ v143 → v149 → v155) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the SURFACE-FAMILY name "the
    # v143-era pair" (the lineage's own designation, preserved exactly
    # as the v149 form preserved it); the era marker "last re-shot v149";
    # the oldest-remaining list "[v149 < v150 < v151 < v152 < v153]"; the
    # corrected census provenance "since v149" + "The v149 verdict".
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v143|v143 < v144|FOURTEENTH re-run|SEVENTY-SECOND|"
            r"v101-v143|since v143\)|The v143 verdict|"
            r"refvlm149|clonevlm149|refar149|clonear149|"
            r"/tmp/vlm149",
            text,
        ):
            bad.append(m.group(0))
        # bare-v143 sweep: the corrected bracket + the family name are the
        # sole legitimate survivors
        for m in re.finditer(r"v143", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v131 → v137 → v143 → v149 → v155" in ctx:
                continue
            if "v143-era" in ctx:
                continue
            bad.append("v143 (outside the corrected bracket/family name)")
        # v144 sweep: the old oldest-remaining token must be wholly gone
        for m in re.finditer(r"v144", text):
            bad.append(f"{m.group(0)} (old oldest-remaining token)")
        # bare-v149 sweep: the corrected bracket + the corrected era marker
        # ("last re-shot v149") + the corrected oldest-remaining list
        # ("[v149 < v150") + the corrected census provenance ("since v149" /
        # "The v149 verdict") + the re-proves windows ("v101-v149") are the
        # sole legitimate survivors
        for m in re.finditer(r"v149", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v131 → v137 → v143 → v149 → v155" in ctx:
                continue
            if "re-shot" in ctx:
                continue
            if "oldest remaining [v149" in ctx:
                continue
            if "since v149" in ctx:
                continue
            if "The v149 verdict" in ctx:
                continue
            if "v101-v149" in ctx:
                continue
            bad.append("v149 (outside the corrected bracket/era marker/list/provenance/windows)")
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
