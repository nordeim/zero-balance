#!/usr/bin/env python3
"""Derive the v142 probe series from the v136 lineage (the NETWORTH view +
the DASHBOARD's drill-down EXPANDED state at desktop 1280x800 — the v60-era
networth+drill-down pair's THIRTEENTH re-run [v60 → v67 → v76 → v82 → v88 →
v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v141-era docs' v142 queue names "the v136-era NETWORTH +
drill-down-DASHBOARD pair ... the pair's THIRTEENTH re-run bracket [v60 →
v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 →
v136 → v142] to be verified against the v136 lineage's own records" —
verified against the v136 lineage BEFORE this derivation: the v136 plan's
own header reads "the v130-era NETWORTH + drill-down-DASHBOARD pair's
TWELFTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 →
v118 → v124 → v130 → v136]" — a 13-ENTRY bracket with the TWELFTH ordinal
(v60 the original, the entries-minus-one convention: 13 entries − the
original = 12 re-runs, the TWELFTH), consistent, no off-by-one this
lineage; the v136 shots header carries the FULL bracket form. v142 = the
THIRTEENTH re-run by appending v142 to the v136 header's TWELFTH bracket.
The SIXTY-FIFTH consecutive queue/ledger agreement. The cadence is in its
SECOND PASS, the v136-era NETWORTH + drill-down pair the oldest remaining
[v136 < v137 < v138].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm136->refvlm142, clonevlm136->clonevlm142,
     refar136->refar142, clonear136->clonear142 (the FOUR EXPLICIT
     session-token swaps — the tokens carry '136' without the 'v' prefix,
     so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm136->/tmp/vlm142, v136->v142
  2. History corrections (the era marker last-re-shot v130 -> v136 + the
     oldest-remaining list [v130 < v131 < v132] -> [v136 < v137 < v138],
     the re-run ordinal TWELFTH -> THIRTEENTH + the re-run bracket extended
     [-> v118 -> v124 -> v130 -> v142] -> [-> v118 -> v124 -> v130 -> v136
     -> v142], the agreement ordinal FIFTY-NINTH -> SIXTY-FIFTH, the arbit
     census provenance "the v130 census axes re-measured" -> "the v136
     census axes re-measured").
     NOTE: the v136 lineage carries NO plan pointer and NO later-pairs list
     (verified by the pre-derivation sweep — all era tokens confined to the
     file headers, lines 2..8).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v136.sh": "scripts/parity-probes/vlm-shots-v142.sh",
    "scripts/parity-probes/clone-vlmshots-v136.sh": "scripts/parity-probes/clone-vlmshots-v142.sh",
    "scripts/parity-probes/vlm-compare-v136.mjs": "scripts/parity-probes/vlm-compare-v142.mjs",
    "scripts/parity-probes/arbit-v136.sh": "scripts/parity-probes/arbit-v142.sh",
}

GENERIC = [
    ("refvlm136", "refvlm142"),
    ("clonevlm136", "clonevlm142"),
    ("refar136", "refar142"),
    ("clonear136", "clonear142"),
    ("/tmp/vlm136", "/tmp/vlm142"),
    ("v136", "v142"),
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
        "scripts/parity-probes/vlm-shots-v142.sh": [
            ("# v130-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v130-era pair last re-shot v130 —\n# now the oldest remaining [v130 < v131 < v132]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's TWELFTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v142] — the FIFTY-NINTH consecutive queue/ledger agreement. The v75",
             "# v136-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v136-era pair last re-shot v136 —\n# now the oldest remaining [v136 < v137 < v138]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's THIRTEENTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142] — the SIXTY-FIFTH consecutive queue/ledger agreement. The v75"),
        ],
        "scripts/parity-probes/clone-vlmshots-v142.sh": [
            ("# v130-era pair (the re-run cadence's rotation — the pair's TWELFTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v142], last re-shot v130, the FIFTY-NINTH consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the",
             "# v136-era pair (the re-run cadence's rotation — the pair's THIRTEENTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142], last re-shot v136, the SIXTY-FIFTH consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the"),
        ],
        "scripts/parity-probes/vlm-compare-v142.mjs": [
            ("// re-run of the v130-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v130-era\n// pair last re-shot v130 — now the oldest remaining [v130 < v131 < v132];\n// the pair's TWELFTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v142] —\n// the FIFTY-NINTH consecutive queue/ledger agreement): (1) the NETWORTH view's",
             "// re-run of the v136-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v136-era\n// pair last re-shot v136 — now the oldest remaining [v136 < v137 < v138];\n// the pair's THIRTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142] —\n// the SIXTY-FIFTH consecutive queue/ledger agreement): (1) the NETWORTH view's"),
        ],
        "scripts/parity-probes/arbit-v142.sh": [
            ("# rule, at DESKTOP 1280x800 on BOTH sides (the v130-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v130; the pair's TWELFTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v142] — the\n# FIFTY-NINTH consecutive queue/ledger agreement). The censuses (the v130\n# census axes re-measured — a drift re-check):",
             "# rule, at DESKTOP 1280x800 on BOTH sides (the v136-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v136; the pair's THIRTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142] — the\n# SIXTY-FIFTH consecutive queue/ledger agreement). The censuses (the v136\n# census axes re-measured — a drift re-check):"),
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
    # (→ v118 → v124 → v130 → v136 → v142) — the re-run chain's middle
    # entries are provenance, not stale era tokens; the corrected era
    # marker (the v136-era / last re-shot v136 / [v136 < v137 < v138]); the
    # axis-provenance citations (the v41/v44/v46/v50/v53/v60/v63/v67/v75
    # pin families cited in the compare header).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v130-era|re-shot v130|v130 < v131|TWELFTH re-run|FIFTY-NINTH|"
            r"the v130 census|refvlm136|clonevlm136|refar136|clonear136|"
            r"/tmp/vlm136",
            text,
        ):
            bad.append(m.group(0))
        # bare-v130 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v130", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v118 → v124 → v130 → v136 → v142" in ctx:
                continue
            bad.append("v130 (outside the corrected bracket)")
        # bare-v131/v132 sweep: fully gone after the bracket correction
        for tok in ("v131", "v132"):
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
