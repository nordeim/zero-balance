#!/usr/bin/env python3
"""Derive the v148 probe series from the v142 lineage (the NETWORTH view +
the DASHBOARD's drill-down EXPANDED state at desktop 1280x800 — the v60-era
networth+drill-down pair's FOURTEENTH re-run [v60 → v67 → v76 → v82 → v88 →
v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v148]).

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v147-era docs' v148 queue names "the v142-era NETWORTH +
drill-down-DASHBOARD pair ... the pair's FOURTEENTH re-run bracket [v60 →
v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 →
v136 → v142 → v148] to be verified against the v142 lineage's own records" —
verified against the v142 lineage BEFORE this derivation: the v142 plan's
own header reads "the v136-era NETWORTH + drill-down-DASHBOARD pair's
THIRTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 →
v118 → v124 → v130 → v136 → v142]" — a 14-ENTRY bracket with the THIRTEENTH
ordinal (v60 the original, the entries-minus-one convention: 14 entries −
the original = 13 re-runs, the THIRTEENTH), consistent, no off-by-one this
lineage; the v142 shots header carries the FULL bracket form. v148 = the
FOURTEENTH re-run by appending v148 to the v142 header's THIRTEENTH bracket.
The SEVENTY-FIRST consecutive queue/ledger agreement. The cadence is in its
THIRD PASS, the v142-era NETWORTH + drill-down pair the oldest remaining
[v142 < v143 < v144].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm142->refvlm148, clonevlm142->clonevlm148,
     refar142->refar148, clonear142->clonear148 (the FOUR EXPLICIT
     session-token swaps — the tokens carry '142' without the 'v' prefix,
     so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm142->/tmp/vlm148, v142->v148
  2. History corrections (the era marker last-re-shot v136 -> v142 + the
     oldest-remaining list [v136 < v137 < v138] -> [v142 < v143 < v144],
     the re-run ordinal THIRTEENTH -> FOURTEENTH + the re-run bracket
     extended [-> v118 -> v124 -> v130 -> v148] -> [-> v118 -> v124 ->
     v130 -> v136 -> v142 -> v148], the agreement ordinal SIXTY-FIFTH ->
     SEVENTY-FIRST, the arbit census provenance "the v136 census axes
     re-measured" -> "the v142 census axes re-measured").
     NOTE: the v142 lineage carries NO plan pointer and NO later-pairs list
     (verified by the pre-derivation sweep — all era tokens confined to the
     file headers, lines 2..8).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v142.sh": "scripts/parity-probes/vlm-shots-v148.sh",
    "scripts/parity-probes/clone-vlmshots-v142.sh": "scripts/parity-probes/clone-vlmshots-v148.sh",
    "scripts/parity-probes/vlm-compare-v142.mjs": "scripts/parity-probes/vlm-compare-v148.mjs",
    "scripts/parity-probes/arbit-v142.sh": "scripts/parity-probes/arbit-v148.sh",
}

GENERIC = [
    ("refvlm142", "refvlm148"),
    ("clonevlm142", "clonevlm148"),
    ("refar142", "refar148"),
    ("clonear142", "clonear148"),
    ("/tmp/vlm142", "/tmp/vlm148"),
    ("v142", "v148"),
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
        "scripts/parity-probes/vlm-shots-v148.sh": [
            ("# v136-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v136-era pair last re-shot v136 —\n# now the oldest remaining [v136 < v137 < v138]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's THIRTEENTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v148] — the SIXTY-FIFTH consecutive queue/ledger agreement. The v75",
             "# v142-era pair (the re-run cadence's rotation — the oldest remaining standing\n# pair: the v142-era pair last re-shot v142 —\n# now the oldest remaining [v142 < v143 < v144]): the desktop\n# 1280x800 FULL-PAGE state of (1) the NETWORTH view and (2) the DASHBOARD's\n# drill-down EXPANDED state. The pair's FOURTEENTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v148] — the SEVENTY-FIRST consecutive queue/ledger agreement. The v75"),
        ],
        "scripts/parity-probes/clone-vlmshots-v148.sh": [
            ("# v136-era pair (the re-run cadence's rotation — the pair's THIRTEENTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v148], last re-shot v136, the SIXTY-FIFTH consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the",
             "# v142-era pair (the re-run cadence's rotation — the pair's FOURTEENTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v148], last re-shot v142, the SEVENTY-FIRST consecutive\n# queue/ledger agreement): the desktop 1280x800 FULL-PAGE state of (1) the"),
        ],
        "scripts/parity-probes/vlm-compare-v148.mjs": [
            ("// re-run of the v136-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v136-era\n// pair last re-shot v136 — now the oldest remaining [v136 < v137 < v138];\n// the pair's THIRTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v148] —\n// the SIXTY-FIFTH consecutive queue/ledger agreement): (1) the NETWORTH view's",
             "// re-run of the v142-era pair (the re-run cadence's rotation — the oldest\n// remaining standing pair: the v142-era\n// pair last re-shot v142 — now the oldest remaining [v142 < v143 < v144];\n// the pair's FOURTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v148] —\n// the SEVENTY-FIRST consecutive queue/ledger agreement): (1) the NETWORTH view's"),
        ],
        "scripts/parity-probes/arbit-v148.sh": [
            ("# rule, at DESKTOP 1280x800 on BOTH sides (the v136-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v136; the pair's THIRTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v148] — the\n# SIXTY-FIFTH consecutive queue/ledger agreement). The censuses (the v136\n# census axes re-measured — a drift re-check):",
             "# rule, at DESKTOP 1280x800 on BOTH sides (the v142-era pair's fresh sweep —\n# the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v142; the pair's FOURTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v148] — the\n# SEVENTY-FIRST consecutive queue/ledger agreement). The censuses (the v142\n# census axes re-measured — a drift re-check):"),
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
    # (→ v118 → v124 → v130 → v136 → v142 → v148) — the re-run chain's middle
    # entries are provenance, not stale era tokens; the corrected era
    # marker (the v142-era / last re-shot v142 / [v142 < v143 < v144]); the
    # axis-provenance citations (the v41/v44/v46/v50/v53/v60/v63/v67/v75/v82
    # pin families cited in the compare header).
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"v136-era|re-shot v136|v136 < v137|THIRTEENTH re-run|SIXTY-FIFTH|"
            r"the v136 census|refvlm142|clonevlm142|refar142|clonear142|"
            r"/tmp/vlm142",
            text,
        ):
            bad.append(m.group(0))
        # bare-v130/v124/v118 sweeps: the corrected bracket context alone
        for tok in ("v130", "v124", "v118"):
            for m in re.finditer(tok, text):
                ctx = text[max(0, m.start() - 60):m.end() + 60]
                if "→ v118 → v124 → v130 → v136 → v142 → v148" in ctx:
                    continue
                bad.append(f"{tok} (outside the corrected bracket)")
        # bare-v136 sweep: the corrected bracket context alone (the era
        # marker + the old oldest-remaining list are corrected away)
        for m in re.finditer(r"v136", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v118 → v124 → v130 → v136 → v142 → v148" in ctx:
                continue
            bad.append("v136 (outside the corrected bracket)")
        # bare-v142 sweep: the corrected bracket + the corrected era marker
        # ("the v142-era" / "last re-shot v142") + the corrected census
        # provenance ("the v142\ncensus axes re-measured" — the token pair
        # spans the line wrap, so the whitelist matches the line's tail) +
        # the corrected oldest-remaining list ("[v142 < v143 < v144]") are
        # the sole legitimate survivors
        for m in re.finditer(r"v142", text):
            ctx = text[max(0, m.start() - 40):m.end() + 40]
            if "→ v118 → v124 → v130 → v136 → v142 → v148" in ctx:
                continue
            if "v142-era" in ctx:
                continue
            if "re-shot" in ctx:
                continue
            if "census axes re-measured" in ctx:
                continue
            if "oldest remaining [v142" in ctx:
                continue
            bad.append("v142 (outside the corrected bracket/era marker/list)")
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
