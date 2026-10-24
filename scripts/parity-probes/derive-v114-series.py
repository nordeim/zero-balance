#!/usr/bin/env python3
"""Derive the v114 probe series from the v108 lineage (the MOBILE TWINS
pair — BOTH mobile 390x844 full-page twins: the /NETWORTH view [the
v63-era pair's surface] + the DASHBOARD [the v62-era mobile twin's
surface], EIGHTH re-run
[v62/v63 -> v69 -> v78 -> v84 -> v90 -> v96 -> v102 -> v108 -> v114]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm108->refvlm114, clonevlm108->clonevlm114,
     refarbit108->refarbit114, clonearbit108->clonearbit114,
     /tmp/vlm108->/tmp/vlm114, v108->v114
  2. History corrections, single-line-safe forms (the v107 derivation
     lesson: multi-line fragments are line-break-fragile; every correction
     below is a within-line edit): the queue attribution "the v107 plan"
     -> "the v113 plan", last-re-shot v102 -> v108, the oldest-remaining
     list bumped to the current era (both the one-line form and the
     wrapped two-line form in the compare file), re-run ordinal
     SEVENTH->EIGHTH, the re-run bracket extended [v62/v63 -> ... ->
     v102 -> v108 -> v114], the arbit census provenance "The v102 census
     axes" -> "The v108 census axes", and the two class-confirmation
     lists extended with v108 (the v84/v90/v96/v102 re-runs -> the
     v84/v90/v96/v102/v108 re-runs — the v108 verdicts were BOTH
     DIFFERENT, the pair's documented verdict class).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v108.sh": "scripts/parity-probes/vlm-shots-v114.sh",
    "scripts/parity-probes/clone-vlmshots-v108.sh": "scripts/parity-probes/clone-vlmshots-v114.sh",
    "scripts/parity-probes/vlm-compare-v108.mjs": "scripts/parity-probes/vlm-compare-v114.mjs",
    "scripts/parity-probes/arbit-v108.sh": "scripts/parity-probes/arbit-v114.sh",
}

GENERIC = [
    ("refvlm108", "refvlm114"),
    ("clonevlm108", "clonevlm114"),
    ("refarbit108", "refarbit114"),
    ("clonearbit108", "clonearbit114"),
    ("/tmp/vlm108", "/tmp/vlm114"),
    ("v108", "v114"),
]

# Single-line-safe history corrections (each verified applied per file).
# Order matters: the one-line oldest-remaining list (correction 3) runs
# BEFORE the wrapped-fragment forms (4, 5) so the two forms cannot
# double-apply.
CORRECTIONS = [
    ("the v107 plan", "the v113 plan"),
    ("re-shot v102", "re-shot v108"),
    ("[v102 < v103 < v104 < v105 < v106 < v107]",
     "[v108 < v109 < v110 < v111 < v112 < v113]"),
    ("[v102 < v103 <", "[v108 < v109 <"),
    ("v104 < v105 < v106 < v107]", "v110 < v111 < v112 < v113]"),
    ("SEVENTH re-run", "EIGHTH re-run"),
    ("v96 → v102 → v114])", "v96 → v102 → v108 → v114])"),
    ("The v102 census axes", "The v108 census axes"),
    ("the v84/v90/v96/v102 re-runs' own verdicts",
     "the v84/v90/v96/v102/v108 re-runs' own verdicts"),
    ("the v84/v90/v96/v102 re-runs):",
     "the v84/v90/v96/v102/v108 re-runs):"),
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
    for path in FILES.values():
        text = open(path, encoding="utf-8").read()
        applied = []
        for old, new in CORRECTIONS:
            n = text.count(old)
            if n:
                text = text.replace(old, new)
                applied.append(f"{old[:34]!r} x{n}")
        open(path, "w", encoding="utf-8").write(text)
        print(f"{path}: {len(applied)} correction families applied")
        for a in applied:
            print(f"    {a}")

    # residual old-token check across all four files.
    # LEGIT contexts that must survive: the corrected re-run bracket
    # (-> v102 -> v108 -> v114 — the pair's own history), the corrected
    # state tokens (re-shot v108, The v108 census axes, the v108-extended
    # class-confirmation lists), the surface-era markers (the v62/v63-era
    # surfaces), the pin/axes provenance (the v41/v44/v45/v51/v53/v60/v61/
    # v62/v63 pins), and the rule/lesson references (the v46/v75 rules).
    BAD = re.compile(
        r"the v107 plan|re-shot v102|SEVENTH re-run|The v102 census"
        r"|\[v102 < v103|v96 → v102 → v114\]\)"
        r"|v84/v90/v96/v102 re-runs"
        r"|refvlm108|clonevlm108|refarbit108|clonearbit108|/tmp/vlm108"
    )
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        hits = BAD.findall(text)
        if hits:
            print(f"RESIDUAL OLD TOKENS in {dst}: {sorted(set(hits))}")
            ok = False
        else:
            print(f"residual check {dst}: clean")

    # line-count report (the two-half builder inherits boundaries)
    for src, dst in FILES.items():
        sn = open(src, encoding="utf-8").read().count("\n")
        dn = open(dst, encoding="utf-8").read().count("\n")
        status = "OK" if sn == dn else f"DRIFT ({dn - sn:+d})"
        print(f"line-count {dst}: {dn + 1} lines (source {sn + 1}) — {status}")
        if sn != dn:
            ok = False

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
