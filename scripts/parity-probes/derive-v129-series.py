#!/usr/bin/env python3
"""Derive the v129 probe series from the v123 lineage (the LOGIN view +
the CALCULATOR dialog at desktop 1280x800 — the v59-era login+calc pair's
ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 →
v117 → v123 → v129]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v128-era docs' v129 queue names "the v123-era LOGIN +
CALCULATOR pair ... the ELEVENTH re-run by the entries-minus-one convention
derived from vlm-shots-v123.sh's own header" — verified against the v123
lineage BEFORE this derivation: vlm-shots-v123.sh's own header reads "the
pair's TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111
→ v117 → v123]" — the TENTH ordinal on the 11-entry bracket [v59 the
original — 11 entries − the original = 10 re-runs], consistent, no
off-by-one this lineage. v129 = the ELEVENTH re-run by appending v129 to
that bracket. The FIFTY-SECOND consecutive queue/ledger agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm123->refvlm129, clonevlm123->clonevlm129,
     refcalc123arbit->refcalc129arbit, clonecalc123arbit->clonecalc129arbit,
     reflogin123arbit->reflogin129arbit, clonelogin123arbit->clonelogin129arbit
     (the SIX EXPLICIT session-token swaps — the tokens carry '123' without
     the 'v' prefix, so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm123->/tmp/vlm129, v123->v129
  2. History corrections (the era marker last-re-shot v117 -> v123 + the
     oldest-remaining bracket [v117 < ... < v122] -> [v123 < ... < v128],
     the re-run ordinal TENTH -> ELEVENTH + the re-run bracket extended
     [-> v117 -> v129] -> [-> v117 -> v123 -> v129], the plan pointer the
     v122 plan -> the v128 plan, the agreement ordinal FORTY-SIXTH ->
     FIFTY-SECOND).
     NOTE: the v123 lineage carries NO later-pairs list (verified by the
     pre-derivation sweep — all era tokens confined to the file headers).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v123.sh": "scripts/parity-probes/vlm-shots-v129.sh",
    "scripts/parity-probes/clone-vlmshots-v123.sh": "scripts/parity-probes/clone-vlmshots-v129.sh",
    "scripts/parity-probes/vlm-compare-v123.mjs": "scripts/parity-probes/vlm-compare-v129.mjs",
    "scripts/parity-probes/arbit-v123.sh": "scripts/parity-probes/arbit-v129.sh",
}

GENERIC = [
    ("refvlm123", "refvlm129"),
    ("clonevlm123", "clonevlm129"),
    ("refcalc123arbit", "refcalc129arbit"),
    ("clonecalc123arbit", "clonecalc129arbit"),
    ("reflogin123arbit", "reflogin129arbit"),
    ("clonelogin123arbit", "clonelogin129arbit"),
    ("/tmp/vlm123", "/tmp/vlm129"),
    ("v123", "v129"),
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
        "scripts/parity-probes/vlm-shots-v129.sh": [
            ("# next-oldest candidate (the v117-era LOGIN + CALCULATOR pair, last re-shot\n# v117, now the oldest remaining [v117 < v118 < v119 < v120 < v121 < v122]; the\n# v122 plan's v129 queue suggestion, agreeing with the rotation ledger — the\n# FORTY-SIXTH consecutive agreement; the pair's TENTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117 → v129]). READ-ONLY: login + hover + dialog-open only — no",
             "# next-oldest candidate (the v123-era LOGIN + CALCULATOR pair, last re-shot\n# v123, now the oldest remaining [v123 < v124 < v125 < v126 < v127 < v128]; the\n# v128 plan's v129 queue suggestion, agreeing with the rotation ledger — the\n# FIFTY-SECOND consecutive agreement; the pair's ELEVENTH re-run [v59 → v66 → v75 →\n# v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129]). READ-ONLY: login + hover + dialog-open only — no"),
        ],
        "scripts/parity-probes/clone-vlmshots-v129.sh": [
            ("# v117-era LOGIN + CALCULATOR pair, last re-shot v117 — the pair's TENTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v129]). Runs inside",
             "# v123-era LOGIN + CALCULATOR pair, last re-shot v123 — the pair's ELEVENTH\n# re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129]). Runs inside"),
        ],
        "scripts/parity-probes/vlm-compare-v129.mjs": [
            ("// re-run cycle's next-oldest candidate, the v117-era LOGIN + CALCULATOR\n// pair last re-shot v117 [v117 < v118 < v119 < v120 < v121 < v122]; the pair's\n// TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v129] — the FORTY-SIXTH\n// consecutive queue/ledger agreement).",
             "// re-run cycle's next-oldest candidate, the v123-era LOGIN + CALCULATOR\n// pair last re-shot v123 [v123 < v124 < v125 < v126 < v127 < v128]; the pair's\n// ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129] — the FIFTY-SECOND\n// consecutive queue/ledger agreement)."),
        ],
        "scripts/parity-probes/arbit-v129.sh": [
            ("# rule, at DESKTOP 1280x800 on BOTH sides (the v117-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v117; the pair's\n# TENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v129]). The censuses:",
             "# rule, at DESKTOP 1280x800 on BOTH sides (the v123-era pair's fresh sweep —\n# the calculator dialog + the login view, last re-shot v123; the pair's\n# ELEVENTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129]). The censuses:"),
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
    # (→ v117 → v123 → v129) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the corrected era marker (the
    # v123-era / last re-shot v123 / [v123 < v124 < ... < v128]); the
    # axis-provenance citations (the v45/v49/v59/v66/v73/v7/v55/v87 pin
    # families cited in the compare header).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v117-era|re-shot v117|v117 < v118|TENTH re-run|FORTY-SIXTH|"
            r"the v122 plan|refvlm123|clonevlm123|refcalc123arbit|"
            r"clonecalc123arbit|reflogin123arbit|clonelogin123arbit|"
            r"/tmp/vlm123",
            text,
        ):
            bad.append(m.group(0))
        # bare-v117 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v117", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v117 → v123 → v129" in ctx:
                continue
            bad.append("v117 (outside the corrected bracket)")
        # bare-v122 sweep: fully gone after the plan-pointer correction
        for m in re.finditer(r"v122", text):
            bad.append("v122 (residual)")
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
