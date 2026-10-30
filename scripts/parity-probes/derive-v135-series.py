#!/usr/bin/env python3
"""Derive the v135 probe series from the v129 lineage (the LOGIN view +
the CALCULATOR dialog at desktop 1280x800 — the v59-era login+calc pair's
TWELFTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 →
v117 → v123 → v129 → v135]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v134-era docs' v135 queue names "the v129-era LOGIN +
CALCULATOR pair ... the pair's TWELFTH re-run by the entries-minus-one
convention to be verified against the v129 lineage's own records" —
verified against the v129 lineage BEFORE this derivation: the v129 plan's
own F3 record reads "the ELEVENTH ordinal recorded in vlm-shots-v123.sh's
own header" on the 12-entry bracket [v59 the original — 12 entries − the
original = 11 re-runs], and vlm-shots-v129.sh's own header carries the FULL
bracket form "the pair's ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 →
v93 → v99 → v105 → v111 → v117 → v123 → v129]" — consistent, no off-by-one
this lineage. v135 = the TWELFTH re-run by appending v135 to that bracket.
The FIFTY-EIGHTH consecutive queue/ledger agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm129->refvlm135, clonevlm129->clonevlm135,
     refcalc129arbit->refcalc135arbit, clonecalc129arbit->clonecalc135arbit,
     reflogin129arbit->reflogin135arbit, clonelogin129arbit->clonelogin135arbit
     (the SIX EXPLICIT session-token swaps — the tokens carry '129' without
     the 'v' prefix, so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm129->/tmp/vlm135, v129->v135
  2. History corrections (the era marker last re-shot v123 -> v129 + the
     oldest-remaining bracket [v123 < ... < v128] -> [v129 < ... < v132],
     the re-run ordinal ELEVENTH -> TWELFTH + the re-run bracket extended
     [-> v123 -> v135] -> [-> v123 -> v129 -> v135], the plan pointer the
     v128 plan -> the v134 plan, the agreement ordinal FIFTY-SECOND ->
     FIFTY-EIGHTH).
     NOTE: the v129 lineage carries NO later-pairs list (verified by the
     pre-derivation sweep — all era tokens confined to the file headers).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v129.sh": "scripts/parity-probes/vlm-shots-v135.sh",
    "scripts/parity-probes/clone-vlmshots-v129.sh": "scripts/parity-probes/clone-vlmshots-v135.sh",
    "scripts/parity-probes/vlm-compare-v129.mjs": "scripts/parity-probes/vlm-compare-v135.mjs",
    "scripts/parity-probes/arbit-v129.sh": "scripts/parity-probes/arbit-v135.sh",
}

GENERIC = [
    ("refvlm129", "refvlm135"),
    ("clonevlm129", "clonevlm135"),
    ("refcalc129arbit", "refcalc135arbit"),
    ("clonecalc129arbit", "clonecalc135arbit"),
    ("reflogin129arbit", "reflogin135arbit"),
    ("clonelogin129arbit", "clonelogin135arbit"),
    ("/tmp/vlm129", "/tmp/vlm135"),
    ("v129", "v135"),
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
        "scripts/parity-probes/vlm-shots-v135.sh": [
            ("# next-oldest candidate (the v123-era LOGIN + CALCULATOR pair, last re-shot\n# v123, now the oldest remaining [v123 < v124 < v125 < v126 < v127 < v128]; the\n# v128 plan's v135 queue suggestion, agreeing with the rotation ledger — the\n# FIFTY-SECOND consecutive agreement; the pair's ELEVENTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v135]). READ-ONLY: login + hover + dialog-open only — no",
             "# next-oldest candidate (the v129-era LOGIN + CALCULATOR pair, last re-shot\n# v129, now the oldest remaining [v129 < v130 < v131 < v132]; the\n# v134 plan's v135 queue suggestion, agreeing with the rotation ledger — the\n# FIFTY-EIGHTH consecutive agreement; the pair's TWELFTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135]). READ-ONLY: login + hover + dialog-open only — no"),
        ],
        "scripts/parity-probes/clone-vlmshots-v135.sh": [
            ("# v123-era LOGIN + CALCULATOR pair, last re-shot v123 — the pair's ELEVENTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v135]). Runs inside",
             "# v129-era LOGIN + CALCULATOR pair, last re-shot v129 — the pair's TWELFTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135]). Runs inside"),
        ],
        "scripts/parity-probes/vlm-compare-v135.mjs": [
            ("// re-run cycle's next-oldest candidate, the v123-era LOGIN + CALCULATOR\n// pair last re-shot v123 [v123 < v124 < v125 < v126 < v127 < v128]; the pair's\n// ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v135] — the FIFTY-SECOND\n// consecutive queue/ledger agreement). Existing pins on these surfaces: the",
             "// re-run cycle's next-oldest candidate, the v129-era LOGIN + CALCULATOR\n// pair last re-shot v129 [v129 < v130 < v131 < v132]; the pair's\n// TWELFTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135] — the FIFTY-EIGHTH\n// consecutive queue/ledger agreement). Existing pins on these surfaces: the"),
        ],
        "scripts/parity-probes/arbit-v135.sh": [
            ("# rule, at DESKTOP 1280x800 on BOTH sides (the v123-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v123; the pair's\n# ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v135]). The censuses:",
             "# rule, at DESKTOP 1280x800 on BOTH sides (the v129-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v129; the pair's\n# TWELFTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135]). The censuses:"),
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
    # (→ v117 → v123 → v129 → v135) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the corrected era marker (the
    # v129-era / last re-shot v129 / [v129 < v130 < ... < v132]); the
    # axis-provenance citations (the v45/v49/v59/v66/v73/v7/v55/v87 pin
    # families cited in the compare header).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v123-era|re-shot v123|v123 < v124|ELEVENTH re-run|FIFTY-SECOND|"
            r"the v128 plan|refvlm129|clonevlm129|refcalc129arbit|"
            r"clonecalc129arbit|reflogin129arbit|clonelogin129arbit|"
            r"/tmp/vlm129",
            text,
        ):
            bad.append(m.group(0))
        # bare-v123 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v123", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135" in ctx:
                continue
            bad.append("v123 (outside the corrected bracket)")
        # bare-v117 sweep: same bracket context
        for m in re.finditer(r"v117", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v123 → v129 → v135" in ctx:
                continue
            bad.append("v117 (outside the corrected bracket)")
        # bare-v128 sweep: fully gone after the plan-pointer correction
        for m in re.finditer(r"v128", text):
            bad.append("v128 (residual)")
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
