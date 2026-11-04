#!/usr/bin/env python3
"""Derive the v153 probe series from the v147 lineage (the LOGIN view +
the CALCULATOR dialog at desktop 1280x800 — the v147-era login+calc pair's
FIFTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 →
v117 → v123 → v129 → v135 → v141 → v147 → v153]; the files keep the
lineage's own "the v129-era LOGIN + CALCULATOR pair" family designation,
preserved exactly as the v139 form preserved "the v57-era items pair", the
v140 form preserved "the v128-era savings pair" and the v147 form preserved
"the v129-era LOGIN + CALCULATOR pair").

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v152-era docs' v153 queue names "the v147-era LOGIN +
CALCULATOR pair ... the pair's FIFTEENTH re-run bracket [v59 → ... →
v129 → v135 → v141 → v147 → v153] to be verified against the v147
lineage's own records" — verified against the v147 lineage BEFORE this
derivation: the v147 plan's own header reads "the v141-era LOGIN +
CALCULATOR pair's FOURTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 →
v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147]" — a
15-ENTRY bracket with the FOURTEENTH ordinal (v59 the original, the
entries-minus-one convention: 15 entries − the original = 14 re-runs, the
FOURTEENTH). v153 = the FIFTEENTH re-run by appending v153 to the v147
header's FOURTEENTH bracket. The SEVENTY-SIXTH consecutive queue/ledger
agreement. The cadence is in its THIRD PASS, the v147-era LOGIN +
CALCULATOR pair the oldest remaining
[v147 < v148 < v149 < v150 < v151 < v152].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm147->refvlm153, clonevlm147->clonevlm153,
     refcalc147arbit->refcalc153arbit, clonecalc147arbit->clonecalc153arbit,
     reflogin147arbit->reflogin153arbit, clonelogin147arbit->clonelogin153arbit
     (the SIX EXPLICIT session-token swaps — the tokens carry '147' without
     the 'v' prefix, so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm147->/tmp/vlm153, v147->v153
  2. History corrections (the era marker last-re-shot v141 -> v147 + the
     oldest-remaining list [v141 < v142 < v143 < v144] -> [v147 < v148 <
     v149 < v150 < v151 < v152], the plan pointer the v146 plan -> the
     v152 plan, the agreement ordinal SEVENTIETH -> SEVENTY-SIXTH; the
     re-run ordinal FOURTEENTH -> FIFTEENTH, the re-run bracket extended
     [-> v123 -> v129 -> v135 -> v141 -> v153] -> [-> v123 -> v129 -> v135
     -> v141 -> v147 -> v153]).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v147.sh": "scripts/parity-probes/vlm-shots-v153.sh",
    "scripts/parity-probes/clone-vlmshots-v147.sh": "scripts/parity-probes/clone-vlmshots-v153.sh",
    "scripts/parity-probes/vlm-compare-v147.mjs": "scripts/parity-probes/vlm-compare-v153.mjs",
    "scripts/parity-probes/arbit-v147.sh": "scripts/parity-probes/arbit-v153.sh",
}

GENERIC = [
    ("refvlm147", "refvlm153"),
    ("clonevlm147", "clonevlm153"),
    ("refcalc147arbit", "refcalc153arbit"),
    ("clonecalc147arbit", "clonecalc153arbit"),
    ("reflogin147arbit", "reflogin153arbit"),
    ("clonelogin147arbit", "clonelogin153arbit"),
    ("/tmp/vlm147", "/tmp/vlm153"),
    ("v147", "v153"),
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
        "scripts/parity-probes/vlm-shots-v153.sh": [
            ("next-oldest candidate (the v129-era LOGIN + CALCULATOR pair, last re-shot\n# v141, now the oldest remaining [v141 < v142 < v143 < v144]; the\n# v146 plan's v153 queue suggestion, agreeing with the rotation ledger — the\n# SEVENTIETH consecutive agreement; the pair's FOURTEENTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v153]). READ-ONLY: login + hover + dialog-open only — no",
             "next-oldest candidate (the v129-era LOGIN + CALCULATOR pair, last re-shot\n# v147, now the oldest remaining [v147 < v148 < v149 < v150 < v151 < v152]; the\n# v152 plan's v153 queue suggestion, agreeing with the rotation ledger — the\n# SEVENTY-SIXTH consecutive agreement; the pair's FIFTEENTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147 → v153]). READ-ONLY: login + hover + dialog-open only — no"),
        ],
        "scripts/parity-probes/clone-vlmshots-v153.sh": [
            ("# v129-era LOGIN + CALCULATOR pair, last re-shot v141 — the pair's FOURTEENTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v153]). Runs inside",
             "# v129-era LOGIN + CALCULATOR pair, last re-shot v147 — the pair's FIFTEENTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147 → v153]). Runs inside"),
        ],
        "scripts/parity-probes/vlm-compare-v153.mjs": [
            ("// pair last re-shot v141 [v141 < v142 < v143 < v144]; the pair's\n// FOURTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v153] — the SEVENTIETH\n// consecutive queue/ledger agreement). Existing pins on these surfaces: the",
             "// pair last re-shot v147 [v147 < v148 < v149 < v150 < v151 < v152]; the pair's\n// FIFTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147 → v153] — the SEVENTY-SIXTH\n// consecutive queue/ledger agreement). Existing pins on these surfaces: the"),
        ],
        "scripts/parity-probes/arbit-v153.sh": [
            ("# the calculator dialog + the login view, last re-shot v141; the pair's\n# FOURTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v153]). The censuses:",
             "# the calculator dialog + the login view, last re-shot v147; the pair's\n# FIFTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147 → v153]). The censuses:"),
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
    # (→ v123 → v129 → v135 → v141 → v147 → v153) — the re-run chain's middle
    # entries are provenance, not stale era tokens; the SURFACE-FAMILY name
    # "the v129-era LOGIN + CALCULATOR pair" (the lineage's own designation,
    # preserved exactly as the v139 form preserved "the v57-era items pair"
    # and the v140 form preserved "the v128-era savings pair"); the era
    # marker "last re-shot v147"; the oldest-remaining list
    # "[v147 < v148 < v149 < v150 < v151 < v152]"; the axis-provenance
    # citations (the v45, v49, v59, v66, v73, v7, v55, v87 pin families
    # cited in the compare header; the v43/v46/v64/v73 rules).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v141|v141 < v142|FOURTEENTH re-run|SEVENTIETH|"
            r"the v146 plan|refvlm147|clonevlm147|refcalc147arbit|"
            r"clonecalc147arbit|reflogin147arbit|clonelogin147arbit|"
            r"/tmp/vlm147",
            text,
        ):
            bad.append(m.group(0))
        # bare-v129 sweep: the corrected bracket + the family name are the
        # sole legitimate survivors
        for m in re.finditer(r"v129", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135 → v141 → v147 → v153" in ctx:
                continue
            if "v129-era" in ctx:
                continue
            bad.append("v129 (outside the corrected bracket/family name)")
        # bare-v123/v117 sweeps: the corrected bracket context alone
        for tok in ("v123", "v117"):
            for m in re.finditer(tok, text):
                ctx = text[max(0, m.start() - 60):m.end() + 60]
                if "→ v123 → v129 → v135 → v141 → v147 → v153" in ctx:
                    continue
                bad.append(f"{tok} (outside the corrected bracket)")
        # bare-v135 sweep: the corrected bracket context alone (the era
        # marker + the old oldest-remaining list are corrected away)
        for m in re.finditer(r"v135", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135 → v141 → v147 → v153" in ctx:
                continue
            bad.append("v135 (outside the corrected bracket)")
        # bare-v141 sweep: the corrected bracket ALONE (the era marker now
        # reads "last re-shot v147" — v141 survives only as the bracket's
        # own provenance entry)
        for m in re.finditer(r"v141", text):
            ctx = text[max(0, m.start() - 40):m.end() + 40]
            if "→ v123 → v129 → v135 → v141 → v147 → v153" in ctx:
                continue
            bad.append("v141 (outside the corrected bracket)")
        # bare-v147 sweep: the corrected bracket + the corrected era marker
        # ("last re-shot v147" / "last re-shot\n# v147,") + the corrected
        # oldest-remaining list ("[v147 < v148 < v149 < v150 < v151 < v152]")
        # are the sole legitimate survivors
        for m in re.finditer(r"v147", text):
            ctx = text[max(0, m.start() - 40):m.end() + 40]
            if "→ v123 → v129 → v135 → v141 → v147 → v153" in ctx:
                continue
            if "re-shot" in ctx:
                continue
            if "oldest remaining [v147" in ctx:
                continue
            bad.append("v147 (outside the corrected bracket/era marker/list)")
        # bare-v146 sweep: fully gone after the plan-pointer correction
        for m in re.finditer(r"v146", text):
            bad.append("v146 (residual)")
        # the old oldest-remaining list tokens must be wholly gone
        # (the corrected list re-points at v147..v152)
        for m in re.finditer(r"v14[234]", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135 → v141 → v147 → v153" in ctx:
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
