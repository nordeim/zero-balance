#!/usr/bin/env python3
"""Derive the v121 probe series from the v115 lineage (the ITEMS pair —
the ITEMS view [income + expenses] at desktop 1280x800 FULL-PAGE, TENTH
re-run [v57 -> v64 -> v70 -> v79 -> v85 -> v91 -> v97 -> v103 -> v109
-> v115 -> v121]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm115->refvlm121, clonevlm115->clonevlm121,
     refarbit115->refarbit121, clonearbit115->clonearbit121,
     /tmp/vlm115->/tmp/vlm121, v115->v121
  2. History corrections, single-line-safe forms (the v107 derivation
     lesson: multi-line fragments are line-break-fragile; every correction
     below is a within-line edit): last-re-shot v109 -> v115, re-run
     ordinal NINTH->TENTH, the re-run bracket extended
     [v57 -> ... -> v103 -> v109 -> v115 -> v121], and the "every other pair
     re-ran later" list re-pointed at the CURRENT later re-runs
     (savings v116, login+calculator v117, networth+drill-down v118,
     budget-guidelines+quick-action v119, mobile twins v120).

The v115 lineage carries NO plan-attribution token and NO
class-confirmation list extension; the census provenance "The v79 census
axes (themselves the v70 census re-measured)" is carried VERBATIM (the
v85/v91/v97/v103/v109/v115 precedent).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v115.sh": "scripts/parity-probes/vlm-shots-v121.sh",
    "scripts/parity-probes/clone-vlmshots-v115.sh": "scripts/parity-probes/clone-vlmshots-v121.sh",
    "scripts/parity-probes/vlm-compare-v115.mjs": "scripts/parity-probes/vlm-compare-v121.mjs",
    "scripts/parity-probes/arbit-v115.sh": "scripts/parity-probes/arbit-v121.sh",
}

GENERIC = [
    ("refvlm115", "refvlm121"),
    ("clonevlm115", "clonevlm121"),
    ("refarbit115", "refarbit121"),
    ("clonearbit115", "clonearbit121"),
    ("/tmp/vlm115", "/tmp/vlm121"),
    ("v115", "v121"),
]

# Single-line-safe history corrections (each verified applied per file).
# NOTE: these run AFTER the generic swaps, so any correction fragment
# containing the current version (v121) must be written against the
# POST-swap state (the v114 derivation precedent: its bracket correction
# targeted the already-swapped "v96 → v102 → v114])" form).
CORRECTIONS = [
    ("re-shot v109", "re-shot v115"),
    ("NINTH re-run", "TENTH re-run"),
    ("→ v109 → v121", "→ v109 → v115 → v121"),
    ("[savings v110, login+calculator", "[savings v116, login+calculator"),
    ("v111, networth+drill-down v112, budget-guidelines+quick-action v113, mobile twins v114]).",
     "v117, networth+drill-down v118, budget-guidelines+quick-action v119, mobile twins v120])."),
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
    # (-> v103 -> v109 -> v115 -> v121 — the pair's own history), the
    # corrected state tokens (re-shot v115), the census provenance (The
    # v79 census axes / the v70 census — carried verbatim per the
    # v85..v115 precedent), the surface-era markers (the v57-era pair),
    # the pin/axes provenance (the v57/v64/v65/v70/v70b/v75 axes), and
    # the rule/lesson references (the v22/v43/v46/v56 rules).
    BAD = re.compile(
        r"re-shot v109|NINTH re-run"
        r"|refvlm115|clonevlm115|refarbit115|clonearbit115|/tmp/vlm115"
        r"|\[savings v110"
        r"|v111, networth\+drill-down v112"
        r"|budget-guidelines\+quick-action v113, mobile twins v114"
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
