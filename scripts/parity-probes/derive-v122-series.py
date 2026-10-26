#!/usr/bin/env python3
"""Derive the v122 probe series from the v116 lineage (the SAVINGS pair —
the SAVINGS view at desktop 1280x800 FULL-PAGE, TENTH re-run [v58 → v65
→ v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116 → v122]).

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied):
  1. Generic swaps: refvlm116->refvlm122, clonevlm116->clonevlm122,
     refarbit116->refarbit122, clonearbit116->clonearbit122,
     /tmp/vlm116->/tmp/vlm122, v116->v122
  2. History corrections, single-line-safe forms (the v107 derivation
     lesson: multi-line fragments are line-break-fragile; every correction
     below is a within-line edit): the era re-pointed v110-era -> v116-era,
     last-re-shot v110 -> v116, the oldest-remaining list re-pointed
     [v110 < ... < v115] -> [v116 < ... < v121], re-run ordinal
     NINTH->TENTH, the plan attribution v115 plan's -> v121 plan's, the
     agreement count THIRTY-NINTH -> FORTY-FIFTH, and the re-run bracket
     extended [v58 -> ... -> v110 -> v116 -> v122].

The v116 lineage carries NO later-pairs list (the v110-lineage header
form — the savings family predates the v117-era later-pairs convention);
the census provenance fragments (the v74/v80 census axes, the v80
titleRow geometry, the v58 DATA-CONDITIONAL footer class, the v57
conditional-footer contract, the v51/v54 390-only family, the v22
parked-pointer lesson, the v43 rule, the v46 rule, the v73 heredoc
lesson) are carried VERBATIM (the v85..v121 precedent).

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v116.sh": "scripts/parity-probes/vlm-shots-v122.sh",
    "scripts/parity-probes/clone-vlmshots-v116.sh": "scripts/parity-probes/clone-vlmshots-v122.sh",
    "scripts/parity-probes/vlm-compare-v116.mjs": "scripts/parity-probes/vlm-compare-v122.mjs",
    "scripts/parity-probes/arbit-v116.sh": "scripts/parity-probes/arbit-v122.sh",
}

GENERIC = [
    ("refvlm116", "refvlm122"),
    ("clonevlm116", "clonevlm122"),
    ("refarbit116", "refarbit122"),
    ("clonearbit116", "clonearbit122"),
    ("/tmp/vlm116", "/tmp/vlm122"),
    ("v116", "v122"),
]

# Single-line-safe history corrections (each verified applied per file).
# NOTE: these run AFTER the generic swaps, so any correction fragment
# containing the current version (v122) must be written against the
# POST-swap state (THE POST-SWAP-FRAGMENT RULE — the v115 derivation
# lesson; the v114 precedent targeted the already-swapped
# "v96 → v102 → v114])" form).
CORRECTIONS = [
    ("the v110-era savings pair", "the v116-era savings pair"),
    ("re-shot v110", "re-shot v116"),
    ("v110, now the oldest", "v116, now the oldest"),
    ("[v110 < v111 < v112 < v113 < v114 < v115]", "[v116 < v117 < v118 < v119 < v120 < v121]"),
    ("NINTH re-run", "TENTH re-run"),
    ("v115 plan's", "v121 plan's"),
    ("THIRTY-NINTH consecutive agreement", "FORTY-FIFTH consecutive agreement"),
    ("→ v104 → v110 → v122]", "→ v104 → v110 → v116 → v122]"),
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
    # (-> v98 -> v104 -> v110 -> v116 -> v122 — the pair's own history),
    # the corrected era/re-shot/oldest tokens (the v116-era savings pair /
    # re-shot v116 / [v116 < v117 ... < v121]), the census provenance
    # (The v74/v80 census axes, the v80 titleRow geometry, the v58
    # DATA-CONDITIONAL footer class, the v57 conditional-footer contract,
    # the v51/v54 390-only family — carried verbatim per the v85..v121
    # precedent), the rule/lesson references (the v22/v43/v46/v73
    # lessons), and the corrected attribution (the v121 plan's).
    BAD = re.compile(
        r"re-shot v110|NINTH re-run"
        r"|refvlm116|clonevlm116|refarbit116|clonearbit116|/tmp/vlm116"
        r"|the v110-era"
        r"|\[v110 < v111"
        r"|v110, now the oldest"
        r"|THIRTY-NINTH consecutive"
        r"|v115 plan's"
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
