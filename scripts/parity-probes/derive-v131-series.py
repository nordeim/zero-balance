#!/usr/bin/env python3
"""Derive the v131 probe series from the v125 lineage (the DASHBOARD at
desktop 1280x800 FULL-PAGE — the v61-era dashboard pair's ELEVENTH re-run
[v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v130-era docs' v131 queue names "the v125-era DASHBOARD pair
... the ELEVENTH re-run by the entries-minus-one convention to be verified
against vlm-shots-v125.sh's own header" — verified against the v125
lineage BEFORE this derivation: vlm-shots-v125.sh's own header reads "the
pair's TENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 →
v113 → v119 → v125]" — the TENTH ordinal on the 11-entry bracket [v61 the
original — 11 entries − the original = 10 re-runs], consistent, no
off-by-one this lineage. v131 = the ELEVENTH re-run by appending v131 to
that bracket. The FIFTY-FOURTH consecutive queue/ledger agreement
(v125 the FORTY-EIGHTH -> v126 49th -> v127 50th -> v128 51st -> v129 52nd
-> v130 53rd -> v131 54th).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm125->refvlm131, clonevlm125->clonevlm131,
     refar125->refar131, clonear125->clonear131 (the FOUR EXPLICIT
     session-token swaps — the arbit tokens carry '125' without the 'v'
     prefix, so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm125->/tmp/vlm131, v125->v131
  2. History corrections (the era marker last-re-shot v119 -> v125 + the
     oldest-remaining bracket [v119 < ... < v124] -> [v125 < ... < v130],
     the re-run ordinal TENTH -> ELEVENTH + the re-run bracket extended
     [-> v119 -> v125] -> [-> v119 -> v125 -> v131], the agreement ordinal
     FORTY-EIGHTH -> FIFTY-FOURTH, the re-proves chain v101-v119 ->
     v101-v125, the arbit verdict/census provenance citations
     "The v119 verdict"/"since v119" -> the v125 forms).
     NOTE: the v125 lineage carries NO plan pointer and NO later-pairs list
     (verified by the pre-derivation sweep — all era tokens confined to the
     file headers, lines 2..14).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v125.sh": "scripts/parity-probes/vlm-shots-v131.sh",
    "scripts/parity-probes/clone-vlmshots-v125.sh": "scripts/parity-probes/clone-vlmshots-v131.sh",
    "scripts/parity-probes/vlm-compare-v125.mjs": "scripts/parity-probes/vlm-compare-v131.mjs",
    "scripts/parity-probes/arbit-v125.sh": "scripts/parity-probes/arbit-v131.sh",
}

GENERIC = [
    ("refvlm125", "refvlm131"),
    ("clonevlm125", "clonevlm131"),
    ("refar125", "refar131"),
    ("clonear125", "clonear131"),
    ("/tmp/vlm125", "/tmp/vlm131"),
    ("v125", "v131"),
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
        "scripts/parity-probes/vlm-shots-v131.sh": [
            ("# v119-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v119 — now\n# the oldest remaining [v119 < v120 < v121 < v122 < v123 < v124]; the pair's TENTH\n# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v131] — the FORTY-EIGHTH consecutive\n# queue/ledger agreement).",
             "# v125-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the DASHBOARD at desktop 1280x800, FULL-PAGE, last re-shot v125 — now\n# the oldest remaining [v125 < v126 < v127 < v128 < v129 < v130]; the pair's ELEVENTH\n# re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131] — the FIFTY-FOURTH consecutive\n# queue/ledger agreement)."),
            ("# unpaired before v61]. The v131 re-run re-proves the v61-era surfaces after\n# v101-v119 (the mobile twins, the height pins, the stat-card divider pin).",
             "# unpaired before v61]. The v131 re-run re-proves the v61-era surfaces after\n# v101-v125 (the mobile twins, the height pins, the stat-card divider pin)."),
        ],
        "scripts/parity-probes/clone-vlmshots-v131.sh": [
            ("# v119-era pair (the re-run cadence's rotation — the pair's TENTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v131]): the DASHBOARD at desktop 1280x800",
             "# v125-era pair (the re-run cadence's rotation — the pair's ELEVENTH re-run\n# [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131]): the DASHBOARD at desktop 1280x800"),
            ("# v61-era surfaces, re-proved again by the v131 re-run after v101-v119). Runs",
             "# v61-era surfaces, re-proved again by the v131 re-run after v101-v125). Runs"),
        ],
        "scripts/parity-probes/vlm-compare-v131.mjs": [
            ("// vlm-compare-v131.mjs — the standing VLM pairwise RE-RUN (v131, the v119-era pair TENTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v131] — the FORTY-EIGHTH consecutive queue/ledger\n// agreement: the DASHBOARD's",
             "// vlm-compare-v131.mjs — the standing VLM pairwise RE-RUN (v131, the v125-era pair ELEVENTH re-run\n// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131] — the FIFTY-FOURTH consecutive queue/ledger\n// agreement: the DASHBOARD's"),
            ("the v131 TENTH re-run of the v119-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v131])",
             "the v131 ELEVENTH re-run of the v125-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131])"),
        ],
        "scripts/parity-probes/arbit-v131.sh": [
            ("# 1280x800 (the v119-era pair's TENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v131]\n# — the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET\n# GUIDELINES card + the QUICK-ACTION row, last re-shot v119). The v119\n# verdict was IDENTICAL with ZERO style flags; per the v75 convention the",
             "# 1280x800 (the v125-era pair's ELEVENTH re-run [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131]\n# — the dashboard FULL-PAGE's below-the-fold surfaces: the BUDGET\n# GUIDELINES card + the QUICK-ACTION row, last re-shot v125). The v125\n# verdict was IDENTICAL with ZERO style flags; per the v75 convention the"),
            ("# censuses are the v61/v83 qa-census axes re-measured (a drift re-check\n# since v119):",
             "# censuses are the v61/v83 qa-census axes re-measured (a drift re-check\n# since v125):"),
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
    # (→ v119 → v125 → v131) — the re-run chain's middle entries are
    # provenance, not stale era tokens; the corrected era marker (the
    # v125-era / last re-shot v125 / [v125 < v126 < ... < v130]); the
    # axis-provenance citations (the v45/v51/v61/v66/v75/v77/v83/v101/v107
    # pin families cited in the headers).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v119-era|re-shot v119|v119 < v120|TENTH re-run|FORTY-EIGHTH|"
            r"the v119 census|v119 verdict|since v119|v101-v119|"
            r"refvlm125|clonevlm125|refar125|clonear125|"
            r"/tmp/vlm125",
            text,
        ):
            bad.append(m.group(0))
        # bare-v119 sweep: the corrected bracket is the sole legitimate survivor
        for m in re.finditer(r"v119", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v119 → v125 → v131" in ctx:
                continue
            bad.append("v119 (outside the corrected bracket)")
        # bare-v120..v124 sweep: fully gone after the bracket correction
        for tok in ("v120", "v121", "v122", "v123", "v124"):
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
