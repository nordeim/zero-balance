#!/usr/bin/env python3
"""Derive the v130 probe series from the v124 lineage (the NETWORTH view +
the DASHBOARD's drill-down EXPANDED state at desktop 1280x800 — the v60-era
networth+drill-down pair's ELEVENTH re-run [v60 → v67 → v76 → v82 → v88 →
v94 → v100 → v106 → v112 → v118 → v124 → v130]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v129-era docs' v130 queue names "the v124-era NETWORTH +
drill-down pair ... the ELEVENTH re-run by the entries-minus-one convention
derived from vlm-shots-v124.sh's own header" — verified against the v124
lineage BEFORE this derivation: vlm-shots-v124.sh's own header reads "the
pair's TENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112
→ v118 → v124]" — the TENTH ordinal on the 11-entry bracket [v60 the
original — 11 entries − the original = 10 re-runs], consistent, no
off-by-one this lineage. v130 = the ELEVENTH re-run by appending v130 to
that bracket. The FIFTY-THIRD consecutive queue/ledger agreement.

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm124->refvlm130, clonevlm124->clonevlm130,
     refar124->refar130, clonear124->clonear130 (the FOUR EXPLICIT
     session-token swaps — the arbit tokens carry '124' without the 'v'
     prefix, so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm124->/tmp/vlm130, v124->v130
  2. History corrections (the era marker last-re-shot v118 -> v124 + the
     oldest-remaining bracket [v118 < ... < v123] -> [v124 < ... < v129],
     the re-run ordinal TENTH -> ELEVENTH + the re-run bracket extended
     [-> v118 -> v124] -> [-> v118 -> v124 -> v130], the agreement ordinal
     FORTY-SEVENTH -> FIFTY-THIRD, the arbit census provenance "the v118
     census axes re-measured" -> "the v124 census axes re-measured").
     NOTE: the v124 lineage carries NO plan pointer and NO later-pairs list
     (verified by the pre-derivation sweep — all era tokens confined to the
     file headers, lines 2..8).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v124.sh": "scripts/parity-probes/vlm-shots-v130.sh",
    "scripts/parity-probes/clone-vlmshots-v124.sh": "scripts/parity-probes/clone-vlmshots-v130.sh",
    "scripts/parity-probes/vlm-compare-v124.mjs": "scripts/parity-probes/vlm-compare-v130.mjs",
    "scripts/parity-probes/arbit-v124.sh": "scripts/parity-probes/arbit-v130.sh",
}

GENERIC = [
    ("refvlm124", "refvlm130"),
    ("clonevlm124", "clonevlm130"),
    ("refar124", "refar130"),
    ("clonear124", "clonear130"),
    ("/tmp/vlm124", "/tmp/vlm130"),
    ("v124", "v130"),
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
        "scripts/parity-probes/vlm-shots-v130.sh": [
            ("# v118-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v118-era pair last re-shot v118 —\n# now the oldest remaining [v118 < v119 < v120 < v121 < v122 < v123]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's TENTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112 → v118 → v130] — the FORTY-SEVENTH consecutive queue/ledger agreement. The v75",
             "# v124-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v124-era pair last re-shot v124 —\n# now the oldest remaining [v124 < v125 < v126 < v127 < v128 < v129]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's ELEVENTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130] — the FIFTY-THIRD consecutive queue/ledger agreement. The v75"),
        ],
        "scripts/parity-probes/clone-vlmshots-v130.sh": [
            ("# v118-era pair (the re-run cadence's rotation — the pair's TENTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v130], last re-shot v118, the FORTY-SEVENTH consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the",
             "# v124-era pair (the re-run cadence's rotation — the pair's ELEVENTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130], last re-shot v124, the FIFTY-THIRD consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the"),
        ],
        "scripts/parity-probes/vlm-compare-v130.mjs": [
            ("// re-run of the v118-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v118-era\n// pair last re-shot v118 — now the oldest remaining [v118 < v119 < v120 < v121\n// < v122 < v123]; the pair's TENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v130] —\n// the FORTY-SEVENTH consecutive queue/ledger agreement): (1) the NETWORTH view's",
             "// re-run of the v124-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v124-era\n// pair last re-shot v124 — now the oldest remaining [v124 < v125 < v126 < v127\n// < v128 < v129]; the pair's ELEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130] —\n// the FIFTY-THIRD consecutive queue/ledger agreement): (1) the NETWORTH view's"),
        ],
        "scripts/parity-probes/arbit-v130.sh": [
            ("# rule, at DESKTOP 1280x800 on BOTH sides (the v118-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v118; the pair's TENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v130] — the\n# FORTY-SEVENTH consecutive queue/ledger agreement). The censuses (the v118\n# census axes re-measured — a drift re-check):",
             "# rule, at DESKTOP 1280x800 on BOTH sides (the v124-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v124; the pair's ELEVENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130] — the\n# FIFTY-THIRD consecutive queue/ledger agreement). The censuses (the v124\n# census axes re-measured — a drift re-check):"),
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
    # (→ v118 → v124 → v130) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the corrected era marker (the
    # v124-era / last re-shot v124 / [v124 < v125 < ... < v129]); the
    # axis-provenance citations (the v41/v44/v46/v50/v53/v60/v63/v67/v75
    # pin families cited in the compare header).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v118-era|re-shot v118|v118 < v119|TENTH re-run|FORTY-SEVENTH|"
            r"the v118 census|refvlm124|clonevlm124|refar124|clonear124|"
            r"/tmp/vlm124",
            text,
        ):
            bad.append(m.group(0))
        # bare-v118 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v118", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v118 → v124 → v130" in ctx:
                continue
            bad.append("v118 (outside the corrected bracket)")
        # bare-v119..v123 sweep: fully gone after the bracket correction
        for tok in ("v119", "v120", "v121", "v122", "v123"):
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
