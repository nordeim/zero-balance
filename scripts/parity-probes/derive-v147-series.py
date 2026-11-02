#!/usr/bin/env python3
"""Derive the v147 probe series from the v141 lineage (the LOGIN view +
the CALCULATOR dialog at desktop 1280x800 — the v129-era login+calc pair's
FOURTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 →
v117 → v123 → v129 → v135 → v141 → v147]; the files keep the lineage's own
"the v129-era LOGIN + CALCULATOR pair" family designation, preserved
exactly as the v139 form preserved "the v57-era items pair" and the v140
form preserved "the v128-era savings pair").

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v146-era docs' v147 queue names "the v141-era LOGIN +
CALCULATOR pair ... the pair's FOURTEENTH re-run bracket [v59 → ... →
v129 → v135 → v141 → v147] to be verified against the v141 lineage's own
records" — verified against the v141 lineage BEFORE this derivation: the
v141 plan's own header reads "the v135-era LOGIN + CALCULATOR pair's
THIRTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 →
v117 → v123 → v129 → v135 → v141]" — a 14-ENTRY bracket with the THIRTEENTH
ordinal (v59 the original, the entries-minus-one convention: 14 entries −
the original = 13 re-runs, the THIRTEENTH). v147 = the FOURTEENTH re-run
by appending v147 to the v141 header's THIRTEENTH bracket. The SEVENTIETH
consecutive queue/ledger agreement. The cadence is in its THIRD PASS, the
v141-era LOGIN + CALCULATOR pair the oldest remaining
[v141 < v142 < v143 < v144].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm141->refvlm147, clonevlm141->clonevlm147,
     refcalc141arbit->refcalc147arbit, clonecalc141arbit->clonecalc147arbit,
     reflogin141arbit->reflogin147arbit, clonelogin141arbit->clonelogin147arbit
     (the SIX EXPLICIT session-token swaps — the tokens carry '141' without
     the 'v' prefix, so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm141->/tmp/vlm147, v141->v147
  2. History corrections (the era marker last-re-shot v135 -> v141 + the
     oldest-remaining list [v135 < v136 < v137 < v138] -> [v141 < v142 <
     v143 < v144], the plan pointer the v140 plan -> the v146 plan, the
     agreement ordinal SIXTY-FOURTH -> SEVENTIETH; the re-run ordinal
     THIRTEENTH -> FOURTEENTH, the re-run bracket extended
     [-> v123 -> v129 -> v135 -> v147] -> [-> v123 -> v129 -> v135 -> v141
     -> v147]).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v141.sh": "scripts/parity-probes/vlm-shots-v147.sh",
    "scripts/parity-probes/clone-vlmshots-v141.sh": "scripts/parity-probes/clone-vlmshots-v147.sh",
    "scripts/parity-probes/vlm-compare-v141.mjs": "scripts/parity-probes/vlm-compare-v147.mjs",
    "scripts/parity-probes/arbit-v141.sh": "scripts/parity-probes/arbit-v147.sh",
}

GENERIC = [
    ("refvlm141", "refvlm147"),
    ("clonevlm141", "clonevlm147"),
    ("refcalc141arbit", "refcalc147arbit"),
    ("clonecalc141arbit", "clonecalc147arbit"),
    ("reflogin141arbit", "reflogin147arbit"),
    ("clonelogin141arbit", "clonelogin147arbit"),
    ("/tmp/vlm141", "/tmp/vlm147"),
    ("v141", "v147"),
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
        "scripts/parity-probes/vlm-shots-v147.sh": [
            ("next-oldest candidate (the v129-era LOGIN + CALCULATOR pair, last re-shot\n# v135, now the oldest remaining [v135 < v136 < v137 < v138]; the\n# v140 plan's v147 queue suggestion, agreeing with the rotation ledger — the\n# SIXTY-FOURTH consecutive agreement; the pair's THIRTEENTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v147]). READ-ONLY: login + hover + dialog-open only — no",
             "next-oldest candidate (the v129-era LOGIN + CALCULATOR pair, last re-shot\n# v141, now the oldest remaining [v141 < v142 < v143 < v144]; the\n# v146 plan's v147 queue suggestion, agreeing with the rotation ledger — the\n# SEVENTIETH consecutive agreement; the pair's FOURTEENTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147]). READ-ONLY: login + hover + dialog-open only — no"),
        ],
        "scripts/parity-probes/clone-vlmshots-v147.sh": [
            ("# v129-era LOGIN + CALCULATOR pair, last re-shot v135 — the pair's THIRTEENTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v147]). Runs inside",
             "# v129-era LOGIN + CALCULATOR pair, last re-shot v141 — the pair's FOURTEENTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147]). Runs inside"),
        ],
        "scripts/parity-probes/vlm-compare-v147.mjs": [
            ("// pair last re-shot v135 [v135 < v136 < v137 < v138]; the pair's\n// THIRTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v147] — the SIXTY-FOURTH\n// consecutive queue/ledger agreement). Existing pins on these surfaces: the",
             "// pair last re-shot v141 [v141 < v142 < v143 < v144]; the pair's\n// FOURTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147] — the SEVENTIETH\n// consecutive queue/ledger agreement). Existing pins on these surfaces: the"),
        ],
        "scripts/parity-probes/arbit-v147.sh": [
            ("# the calculator dialog + the login view, last re-shot v135; the pair's\n# THIRTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v147]). The censuses:",
             "# the calculator dialog + the login view, last re-shot v141; the pair's\n# FOURTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141 → v147]). The censuses:"),
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
    # (→ v123 → v129 → v135 → v141 → v147) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the SURFACE-FAMILY name
    # "the v129-era LOGIN + CALCULATOR pair" (the lineage's own designation,
    # preserved exactly as the v139 form preserved "the v57-era items pair"
    # and the v140 form preserved "the v128-era savings pair"); the era
    # marker "last re-shot v141"; the axis-provenance citations (the v45,
    # v49, v59, v66, v73, v7, v55, v87 pin families cited in the compare
    # header; the v43/v46/v64/v73 rules).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v135|v135 < v136|THIRTEENTH re-run|SIXTY-FOURTH|"
            r"the v140 plan|refvlm141|clonevlm141|refcalc141arbit|"
            r"clonecalc141arbit|reflogin141arbit|clonelogin141arbit|"
            r"/tmp/vlm141",
            text,
        ):
            bad.append(m.group(0))
        # bare-v129 sweep: the corrected bracket + the family name are the
        # sole legitimate survivors
        for m in re.finditer(r"v129", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135 → v141 → v147" in ctx:
                continue
            if "v129-era" in ctx:
                continue
            bad.append("v129 (outside the corrected bracket/family name)")
        # bare-v123/v117 sweeps: the corrected bracket context alone
        for tok in ("v123", "v117"):
            for m in re.finditer(tok, text):
                ctx = text[max(0, m.start() - 60):m.end() + 60]
                if "→ v123 → v129 → v135 → v141 → v147" in ctx:
                    continue
                bad.append(f"{tok} (outside the corrected bracket)")
        # bare-v135 sweep: the corrected bracket context alone (the era
        # marker + the old oldest-remaining list are corrected away)
        for m in re.finditer(r"v135", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135 → v141 → v147" in ctx:
                continue
            bad.append("v135 (outside the corrected bracket)")
        # bare-v141 sweep: the corrected bracket + the corrected era marker
        # ("last re-shot v141" / "last re-shot\n# v141,") + the corrected
        # oldest-remaining list ("[v141 < v142 < v143 < v144]") are the sole
        # legitimate survivors
        for m in re.finditer(r"v141", text):
            ctx = text[max(0, m.start() - 40):m.end() + 40]
            if "→ v123 → v129 → v135 → v141 → v147" in ctx:
                continue
            if "re-shot" in ctx:
                continue
            if "oldest remaining [v141" in ctx:
                continue
            bad.append("v141 (outside the corrected bracket/era marker/list)")
        # bare-v140 sweep: fully gone after the plan-pointer correction
        for m in re.finditer(r"v140", text):
            bad.append("v140 (residual)")
        # the old oldest-remaining list tokens must be wholly gone
        # (the corrected list re-points at v141..v144)
        for m in re.finditer(r"v13[678]", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135 → v141 → v147" in ctx:
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
