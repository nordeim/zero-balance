#!/usr/bin/env python3
"""Derive the v136 probe series from the v130 lineage (the NETWORTH view +
the DASHBOARD's drill-down EXPANDED state at desktop 1280x800 — the v60-era
networth+drill-down pair's TWELFTH re-run [v60 → v67 → v76 → v82 → v88 →
v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v135-era docs' v136 queue names "the v130-era NETWORTH +
drill-down-DASHBOARD pair ... the pair's TWELFTH re-run bracket [v60 → v67
→ v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136]
to be verified against the v130 lineage's own records" — verified against
the v130 lineage BEFORE this derivation: the v130 plan's own header reads
"the v124-era NETWORTH + drill-down pair's ELEVENTH re-run [v60 → v67 → v76
→ v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130]" — the ELEVENTH
ordinal on the 12-entry bracket [v60 the original — 12 entries − the
original = 11 re-runs], consistent, no off-by-one this lineage; the v130
shots header carries the FULL bracket form. v136 = the TWELFTH re-run by
appending v136 to that bracket. The FIFTY-NINTH consecutive queue/ledger
agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm130->refvlm136, clonevlm130->clonevlm136,
     refar130->refar136, clonear130->clonear136 (the FOUR EXPLICIT
     session-token swaps — the arbit tokens carry '130' without the 'v'
     prefix, so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm130->/tmp/vlm136, v130->v136
  2. History corrections (the era marker last-re-shot v124 -> v130 + the
     oldest-remaining bracket [v124 < ... < v129] -> [v130 < v131 < v132]
     — the rotation backlog shrank to three lineages, a within-line edit
     preserving the line count), the re-run ordinal ELEVENTH -> TWELFTH +
     the re-run bracket extended [-> v118 -> v124 -> v136] -> [-> v118 ->
     v124 -> v130 -> v136], the agreement ordinal FIFTY-THIRD ->
     FIFTY-NINTH, the arbit census provenance "the v124 census axes
     re-measured" -> "the v130 census axes re-measured").
     NOTE: the v130 lineage carries NO plan pointer and NO later-pairs list
     (verified by the pre-derivation sweep — all era tokens confined to the
     file headers, lines 2..8).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v130.sh": "scripts/parity-probes/vlm-shots-v136.sh",
    "scripts/parity-probes/clone-vlmshots-v130.sh": "scripts/parity-probes/clone-vlmshots-v136.sh",
    "scripts/parity-probes/vlm-compare-v130.mjs": "scripts/parity-probes/vlm-compare-v136.mjs",
    "scripts/parity-probes/arbit-v130.sh": "scripts/parity-probes/arbit-v136.sh",
}

GENERIC = [
    ("refvlm130", "refvlm136"),
    ("clonevlm130", "clonevlm136"),
    ("refar130", "refar136"),
    ("clonear130", "clonear136"),
    ("/tmp/vlm130", "/tmp/vlm136"),
    ("v130", "v136"),
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
        "scripts/parity-probes/vlm-shots-v136.sh": [
            ("# v124-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v124-era pair last re-shot v124 —\n# now the oldest remaining [v124 < v125 < v126 < v127 < v128 < v129]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's ELEVENTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v136] — the FIFTY-THIRD consecutive queue/ledger agreement. The v75",
             "# v130-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v130-era pair last re-shot v130 —\n# now the oldest remaining [v130 < v131 < v132]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's TWELFTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136] — the FIFTY-NINTH consecutive queue/ledger agreement. The v75"),
        ],
        "scripts/parity-probes/clone-vlmshots-v136.sh": [
            ("# v124-era pair (the re-run cadence's rotation — the pair's ELEVENTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v136], last re-shot v124, the FIFTY-THIRD consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the",
             "# v130-era pair (the re-run cadence's rotation — the pair's TWELFTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136], last re-shot v130, the FIFTY-NINTH consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the"),
        ],
        "scripts/parity-probes/vlm-compare-v136.mjs": [
            ("// re-run of the v124-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v124-era\n// pair last re-shot v124 — now the oldest remaining [v124 < v125 < v126 < v127\n// < v128 < v129]; the pair's ELEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v136] —\n// the FIFTY-THIRD consecutive queue/ledger agreement): (1) the NETWORTH view's",
             "// re-run of the v130-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v130-era\n// pair last re-shot v130 — now the oldest remaining [v130 < v131 < v132];\n// the pair's TWELFTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136] —\n// the FIFTY-NINTH consecutive queue/ledger agreement): (1) the NETWORTH view's"),
        ],
        "scripts/parity-probes/arbit-v136.sh": [
            ("# rule, at DESKTOP 1280x800 on BOTH sides (the v124-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v124; the pair's ELEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v136] — the\n# FIFTY-THIRD consecutive queue/ledger agreement). The censuses (the v124\n# census axes re-measured — a drift re-check):",
             "# rule, at DESKTOP 1280x800 on BOTH sides (the v130-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v130; the pair's TWELFTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136] — the\n# FIFTY-NINTH consecutive queue/ledger agreement). The censuses (the v130\n# census axes re-measured — a drift re-check):"),
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
    # (→ v118 → v124 → v130 → v136) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the corrected era marker (the
    # v130-era / last re-shot v130 / [v130 < v131 < v132]); the
    # axis-provenance citations (the v41/v44/v46/v50/v53/v60/v63/v67/v75
    # pin families cited in the compare header).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v124-era|re-shot v124|v124 < v125|ELEVENTH re-run|FIFTY-THIRD|"
            r"the v124 census|refvlm130|clonevlm130|refar130|clonear130|"
            r"/tmp/vlm130",
            text,
        ):
            bad.append(m.group(0))
        # bare-v124 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v124", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v118 → v124 → v130 → v136" in ctx:
                continue
            bad.append("v124 (outside the corrected bracket)")
        # bare-v125..v129 sweep: fully gone after the bracket correction
        for tok in ("v125", "v126", "v127", "v128", "v129"):
            for m in re.finditer(tok, text):
                bad.append(f"{tok} (residual)")
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
