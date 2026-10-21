#!/usr/bin/env python3
"""Derive the v102 probe series from the v96 lineage (the MOBILE 390 twins
pair — BOTH mobile 390x844 full-page twins: the /NETWORTH view + the
DASHBOARD, SIXTH re-run [v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 ->
v102]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm96->refvlm102, clonevlm96->clonevlm102,
     refarbit96->refarbit102, clonearbit96->clonearbit102,
     /tmp/vlm96->/tmp/vlm102, v96->v102
  2. History corrections (queue source "the v95 plan"->"the v101 plan",
     last-re-shot version v90 -> v96, re-run bracket + ordinal FIFTH->SIXTH,
     the oldest-remaining bracket [v90 < ... < v95] -> [v96 < ... < v101],
     the re-runs' verdict note "the v84/v90 re-runs" -> "the v84/v90/v96
     re-runs", the census-axes provenance "The v90 census axes" -> "The v96
     census axes").

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (each correction replaces the same
number of lines) so build-twohalf-v102.py inherits the v96 line boundaries.
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v96.sh": "scripts/parity-probes/vlm-shots-v102.sh",
    "scripts/parity-probes/clone-vlmshots-v96.sh": "scripts/parity-probes/clone-vlmshots-v102.sh",
    "scripts/parity-probes/vlm-compare-v96.mjs": "scripts/parity-probes/vlm-compare-v102.mjs",
    "scripts/parity-probes/arbit-v96.sh": "scripts/parity-probes/arbit-v102.sh",
}

GENERIC = [
    ("refvlm96", "refvlm102"),
    ("clonevlm96", "clonevlm102"),
    ("refarbit96", "refarbit102"),
    ("clonearbit96", "clonearbit102"),
    ("/tmp/vlm96", "/tmp/vlm102"),
    ("v96", "v102"),
]

def main():
    ok = True
    for src, dst in FILES.items():
        text = open(src, encoding="utf-8").read()
        for old, new in GENERIC:
            text = text.replace(old, new)
        open(dst, "w", encoding="utf-8").write(text)
        print(f"derived {dst} (generic swaps applied)")
    print("\n--- history corrections ---")
    # corrections are applied file-by-file after the fact (fragments appear
    # in their POST-SWAP form)
    corr_map = {
        "scripts/parity-probes/vlm-shots-v102.sh": [
            ("The v102 queue (the v95 plan's own suggestion, now confirmed by the\n# rotation ledger: the twins last re-shot v90 = the oldest remaining\n# [v90 < v91 < v92 < v93 < v94 < v95]; the pair's FIFTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v102]). READ-ONLY: login + passive",
             "The v102 queue (the v101 plan's own suggestion, now confirmed by the\n# rotation ledger: the twins last re-shot v96 = the oldest remaining\n# [v96 < v97 < v98 < v99 < v100 < v101]; the pair's SIXTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102]). READ-ONLY: login + passive"),
        ],
        "scripts/parity-probes/clone-vlmshots-v102.sh": [
            # the post-swap header already reads "the v102 queue item" — the
            # correct current-cycle form; no history correction required.
        ],
        "scripts/parity-probes/vlm-compare-v102.mjs": [
            ("twins last re-shot v90 = the oldest remaining candidate [v90 < v91 <\n// v92 < v93 < v94 < v95]; the pair's FIFTH re-run [v62/v63 → v69 →\n// v78 → v84 → v90 → v102]) and (2) the DASHBOARD (the v62-era mobile twin's",
             "twins last re-shot v96 = the oldest remaining candidate [v96 < v97 <\n// v98 < v99 < v100 < v101]; the pair's SIXTH re-run [v62/v63 → v69 →\n// v78 → v84 → v90 → v96 → v102]) and (2) the DASHBOARD (the v62-era mobile twin's"),
            ("the v84/v90 re-runs' own verdicts were DIFFERENT",
             "the v84/v90/v96 re-runs' own verdicts were DIFFERENT"),
        ],
        "scripts/parity-probes/arbit-v102.sh": [
            ("The v90 census axes,\n# re-measured on BOTH sides at mobile 390 (the pair's FIFTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v102]):\n#   NETWORTH (the v63-era classes, re-confirmed live by the v84/v90 re-runs):",
             "The v96 census axes,\n# re-measured on BOTH sides at mobile 390 (the pair's SIXTH re-run\n# [v62/v63 → v69 → v78 → v84 → v90 → v96 → v102]):\n#   NETWORTH (the v63-era classes, re-confirmed live by the v84/v90/v96 re-runs):"),
        ],
    }
    for path, pairs in corr_map.items():
        text = open(path, encoding="utf-8").read()
        for old, new in pairs:
            if old not in text:
                print(f"MISS in {path}: {old[:60]!r}")
                ok = False
                continue
            text = text.replace(old, new)
            print(f"applied in {path}: {old[:48]!r} -> corrected")
        open(path, "w", encoding="utf-8").write(text)

    # residual old-token check across all four files
    # LEGIT contexts that must survive: the corrected re-run bracket
    # (v62/v63 ... v90 -> v96 -> v102), the new-era tokens (last re-shot
    # v96 / [v96 < v97 / the v84/v90/v96 re-runs), pin provenance
    # (v41/v45/v44/v46/v51/v53/v61/v62/v63/v68/v73/v75/v84/v90 tokens),
    # and the axes provenance (v62-era/v63-era).
    LEGIT = ("→ v96 → v102", "v96 < v97", "re-shot v96", "v84/v90/v96",
             "v62/v63", "v62-era", "v63-era", "v61 STRETCH", "v41 ",
             "v45/v44", "v46 ", "v51 F4", "v53 tablist", "v41 F3",
             "db-seedcheck-v68", "v73 heredoc", "v75 convention",
             "v66 discipline")
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(r"v90-era|FIFTH re-run|last re-shot v90|\[v90 <|the v95 plan|refvlm96|clonevlm96|refarbit96|clonearbit96|/tmp/vlm96", text):
            ctx = text[max(0, m.start() - 40):m.end() + 40]
            if any(l in ctx for l in LEGIT):
                continue  # legitimate provenance/bracket token
            bad.append(m.group(0))
        if bad:
            print(f"RESIDUAL OLD TOKENS in {dst}: {set(bad)}")
            ok = False
        else:
            print(f"residual check {dst}: clean")

    # line-count-preservation check (the two-half builder inherits boundaries)
    for src, dst in FILES.items():
        sn = open(src, encoding="utf-8").read().count("\n")
        dn = open(dst, encoding="utf-8").read().count("\n")
        status = "OK" if sn == dn else "LINE-COUNT DRIFT"
        print(f"line-count {dst}: {dn+1} lines (source {sn+1}) — {status}")
        if sn != dn:
            ok = False

    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
