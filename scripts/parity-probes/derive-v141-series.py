#!/usr/bin/env python3
"""Derive the v141 probe series from the v135 lineage (the LOGIN view +
the CALCULATOR dialog at desktop 1280x800 — the v59-era login+calc pair's
THIRTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 →
v117 → v123 → v129 → v135 → v141]; the files keep the lineage's own
"the v129-era LOGIN + CALCULATOR pair" family designation, preserved
exactly as the v139 form preserved "the v57-era items pair" and the v140
form preserved "the v128-era savings pair").

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v140-era docs' v141 queue names "the v135-era LOGIN +
CALCULATOR pair ... the pair's THIRTEENTH re-run bracket [v59 → ... →
v129 → v135 → v141] to be verified against the v135 lineage's own records"
— verified against the v135 lineage BEFORE this derivation: the v135
plan's own header reads "the v129-era LOGIN + CALCULATOR pair's TWELFTH
re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 →
v123 → v129 → v135]" — a 13-ENTRY bracket with the TWELFTH ordinal (v59
the original, the entries-minus-one convention: 13 entries − the original
= 12 re-runs, the TWELFTH). v141 = the THIRTEENTH re-run by appending
v141 to the v135 header's TWELFTH bracket. The SIXTY-FOURTH consecutive
queue/ledger agreement. The cadence is in its SECOND PASS, the v135-era
LOGIN + CALCULATOR pair the oldest remaining
[v135 < v136 < v137 < v138].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm135->refvlm141, clonevlm135->clonevlm141,
     refcalc135arbit->refcalc141arbit, clonecalc135arbit->clonecalc141arbit,
     reflogin135arbit->reflogin141arbit, clonelogin135arbit->clonelogin141arbit
     (the SIX EXPLICIT session-token swaps — the tokens carry '135' without
     the 'v' prefix, so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm135->/tmp/vlm141, v135->v141
  2. History corrections (the era marker last-re-shot v129 -> v135 + the
     oldest-remaining list [v129 < v130 < v131 < v132] -> [v135 < v136 <
     v137 < v138], the plan pointer the v134 plan -> the v140 plan, the
     agreement ordinal FIFTY-EIGHTH -> SIXTY-FOURTH; the re-run ordinal
     TWELFTH -> THIRTEENTH, the re-run bracket extended
     [-> v123 -> v129 -> v135] -> [-> v123 -> v129 -> v135 -> v141]).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v135.sh": "scripts/parity-probes/vlm-shots-v141.sh",
    "scripts/parity-probes/clone-vlmshots-v135.sh": "scripts/parity-probes/clone-vlmshots-v141.sh",
    "scripts/parity-probes/vlm-compare-v135.mjs": "scripts/parity-probes/vlm-compare-v141.mjs",
    "scripts/parity-probes/arbit-v135.sh": "scripts/parity-probes/arbit-v141.sh",
}

GENERIC = [
    ("refvlm135", "refvlm141"),
    ("clonevlm135", "clonevlm141"),
    ("refcalc135arbit", "refcalc141arbit"),
    ("clonecalc135arbit", "clonecalc141arbit"),
    ("reflogin135arbit", "reflogin141arbit"),
    ("clonelogin135arbit", "clonelogin141arbit"),
    ("/tmp/vlm135", "/tmp/vlm141"),
    ("v135", "v141"),
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
        "scripts/parity-probes/vlm-shots-v141.sh": [
            ("# next-oldest candidate (the v129-era LOGIN + CALCULATOR pair, last re-shot\n# v129, now the oldest remaining [v129 < v130 < v131 < v132]; the\n# v134 plan's v141 queue suggestion, agreeing with the rotation ledger — the\n# FIFTY-EIGHTH consecutive agreement; the pair's TWELFTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v141]). READ-ONLY: login + hover + dialog-open only — no",
             "# next-oldest candidate (the v129-era LOGIN + CALCULATOR pair, last re-shot\n# v135, now the oldest remaining [v135 < v136 < v137 < v138]; the\n# v140 plan's v141 queue suggestion, agreeing with the rotation ledger — the\n# SIXTY-FOURTH consecutive agreement; the pair's THIRTEENTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141]). READ-ONLY: login + hover + dialog-open only — no"),
        ],
        "scripts/parity-probes/clone-vlmshots-v141.sh": [
            ("# v129-era LOGIN + CALCULATOR pair, last re-shot v129 — the pair's TWELFTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v141]). Runs inside",
             "# v129-era LOGIN + CALCULATOR pair, last re-shot v135 — the pair's THIRTEENTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141]). Runs inside"),
        ],
        "scripts/parity-probes/vlm-compare-v141.mjs": [
            ("// re-run cycle's next-oldest candidate, the v129-era LOGIN + CALCULATOR\n// pair last re-shot v129 [v129 < v130 < v131 < v132]; the pair's\n// TWELFTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v141] — the FIFTY-EIGHTH\n// consecutive queue/ledger agreement). Existing pins on these surfaces: the",
             "// re-run cycle's next-oldest candidate, the v129-era LOGIN + CALCULATOR\n// pair last re-shot v135 [v135 < v136 < v137 < v138]; the pair's\n// THIRTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141] — the SIXTY-FOURTH\n// consecutive queue/ledger agreement). Existing pins on these surfaces: the"),
        ],
        "scripts/parity-probes/arbit-v141.sh": [
            ("# rule, at DESKTOP 1280x800 on BOTH sides (the v129-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v129; the pair's\n# TWELFTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v141]). The censuses:",
             "# rule, at DESKTOP 1280x800 on BOTH sides (the v129-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v135; the pair's\n# THIRTEENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135 → v141]). The censuses:"),
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
    # (→ v123 → v129 → v135 → v141) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the SURFACE-FAMILY name
    # "the v129-era LOGIN + CALCULATOR pair" (the lineage's own designation,
    # preserved exactly as the v139 form preserved "the v57-era items pair"
    # and the v140 form preserved "the v128-era savings pair"); the era
    # marker "last re-shot v135"; the axis-provenance citations (the v45,
    # v49, v59, v66, v73, v7, v55, v87 pin families cited in the compare
    # header; the v43/v46/v64/v73 rules).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v129|v129 < v130|TWELFTH re-run|FIFTY-EIGHTH|"
            r"the v134 plan|refvlm135|clonevlm135|refcalc135arbit|"
            r"clonecalc135arbit|reflogin135arbit|clonelogin135arbit|"
            r"/tmp/vlm135",
            text,
        ):
            bad.append(m.group(0))
        # bare-v129 sweep: the corrected bracket + the family name are the
        # sole legitimate survivors
        for m in re.finditer(r"v129", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135 → v141" in ctx:
                continue
            if "v129-era" in ctx:
                continue
            bad.append("v129 (outside the corrected bracket/family name)")
        # bare-v123/v117 sweeps: the corrected bracket context alone
        for tok in ("v123", "v117"):
            for m in re.finditer(tok, text):
                ctx = text[max(0, m.start() - 60):m.end() + 60]
                if "→ v123 → v129 → v135 → v141" in ctx:
                    continue
                bad.append(f"{tok} (outside the corrected bracket)")
        # bare-v134 sweep: fully gone after the plan-pointer correction
        for m in re.finditer(r"v134", text):
            bad.append("v134 (residual)")
        # the old oldest-remaining list tokens must be wholly gone
        # (the corrected list re-points at v135..v138)
        for m in re.finditer(r"v13[012]", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135 → v141" in ctx:
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
