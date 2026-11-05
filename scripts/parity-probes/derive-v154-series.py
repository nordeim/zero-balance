#!/usr/bin/env python3
"""Derive the v154 probe series from the v148 lineage (the NETWORTH view +
the DASHBOARD's drill-down EXPANDED state at desktop 1280x800 — the v148-era
networth+drill-down pair's FIFTEENTH re-run [v60 → v67 → v76 → v82 → v88 →
v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v148 → v154];
the files keep the lineage's own "the v142-era pair" family designation,
preserved exactly as the v148 form preserved it from the v142 lineage and the
v153 form preserved "the v129-era LOGIN + CALCULATOR pair").

NOTE ON THE ORDINAL (the corrected entries-minus-one convention, codified
at v124): the v153-era docs' v154 queue names "the v148-era NETWORTH +
drill-down-DASHBOARD pair ... the pair's FIFTEENTH re-run bracket [v60 → ...
→ v142 → v148 → v154] to be verified against the v148 lineage's own
records" — verified against the v148 lineage BEFORE this derivation: the
v148 plan's own header reads "the v142-era NETWORTH + drill-down-DASHBOARD
pair's FOURTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 →
v112 → v118 → v124 → v130 → v136 → v142 → v148]" — a 15-ENTRY bracket with
the FOURTEENTH ordinal (v60 the original, the entries-minus-one convention:
15 entries − the original = 14 re-runs, the FOURTEENTH). v154 = the
FIFTEENTH re-run by appending v154 to the v148 header's FOURTEENTH bracket.
The SEVENTY-SEVENTH consecutive queue/ledger agreement. The cadence is in
its THIRD PASS, the v148-era networth+drill-down pair the oldest remaining
[v148 < v149 < v150 < v151 < v152 < v153].

Order of operations (the v95-session lesson: generic version swap FIRST,
then exact-fragment history corrections, each verified applied; fragments
written against the POST-generic-swap state per THE POST-SWAP-FRAGMENT RULE):
  1. Generic swaps: refvlm148->refvlm154, clonevlm148->clonevlm154,
     refar148->refar154, clonear148->clonear154
     (the FOUR EXPLICIT session-token swaps — the tokens carry '148' without
     the 'v' prefix, so the bare version swap cannot touch them; the v121-cycle
     stale-session-fix precedent), /tmp/vlm148->/tmp/vlm154, v148->v154
  2. History corrections (the era marker last-re-shot v142 -> v148 + the
     oldest-remaining list [v142 < v143 < v144] -> [v148 < v149 < v150 <
     v151 < v152 < v153], the agreement ordinal SEVENTY-FIRST ->
     SEVENTY-SEVENTH; the re-run ordinal FOURTEENTH -> FIFTEENTH, the
     re-run bracket extended [-> v130 -> v136 -> v142 -> v154] -> [-> v130
     -> v136 -> v142 -> v148 -> v154]; the arbit census provenance "the
     v142 census axes re-measured" -> "the v148 census axes re-measured").

Every replacement is checked; a miss is reported and fails the run.
The derivation is LINE-COUNT-PRESERVING (every correction is a
within-line edit; the line-count report must show OK on all four files).
"""
import sys, re

FILES = {
    "scripts/parity-probes/vlm-shots-v148.sh": "scripts/parity-probes/vlm-shots-v154.sh",
    "scripts/parity-probes/clone-vlmshots-v148.sh": "scripts/parity-probes/clone-vlmshots-v154.sh",
    "scripts/parity-probes/vlm-compare-v148.mjs": "scripts/parity-probes/vlm-compare-v154.mjs",
    "scripts/parity-probes/arbit-v148.sh": "scripts/parity-probes/arbit-v154.sh",
}

GENERIC = [
    ("refvlm148", "refvlm154"),
    ("clonevlm148", "clonevlm154"),
    ("refar148", "refar154"),
    ("clonear148", "clonear154"),
    ("/tmp/vlm148", "/tmp/vlm154"),
    ("v148", "v154"),
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
        "scripts/parity-probes/vlm-shots-v154.sh": [
            ("the v142-era pair last re-shot v142 —\n# now the oldest remaining [v142 < v143 < v144]): the desktop",
             "the v142-era pair last re-shot v148 —\n# now the oldest remaining [v148 < v149 < v150 < v151 < v152 < v153]): the desktop"),
            ("The pair's FOURTEENTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v154] — the SEVENTY-FIRST",
             "The pair's FIFTEENTH re-run [v60 → v67 → v76 →\n# v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v148 → v154] — the SEVENTY-SEVENTH"),
        ],
        "scripts/parity-probes/clone-vlmshots-v154.sh": [
            ("the pair's FOURTEENTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v154], last re-shot v142, the SEVENTY-FIRST consecutive",
             "the pair's FIFTEENTH re-run\n# [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v148 → v154], last re-shot v148, the SEVENTY-SEVENTH consecutive"),
        ],
        "scripts/parity-probes/vlm-compare-v154.mjs": [
            ("// pair last re-shot v142 — now the oldest remaining [v142 < v143 < v144];\n// the pair's FOURTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v154] —\n// the SEVENTY-FIRST consecutive queue/ledger agreement",
             "// pair last re-shot v148 — now the oldest remaining [v148 < v149 < v150 < v151 < v152 < v153];\n// the pair's FIFTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v148 → v154] —\n// the SEVENTY-SEVENTH consecutive queue/ledger agreement"),
        ],
        "scripts/parity-probes/arbit-v154.sh": [
            ("the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v142; the pair's FOURTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v154] — the\n# SEVENTY-FIRST consecutive queue/ledger agreement). The censuses (the v142\n# census axes re-measured — a drift re-check):",
             "the networth view + the dashboard drill-down EXPANDED state, last re-shot\n# v148; the pair's FIFTEENTH re-run [v60 → v67 → v76 → v82 → v88 → v94 → v100 → v106 → v112 → v118 → v124 → v130 → v136 → v142 → v148 → v154] — the\n# SEVENTY-SEVENTH consecutive queue/ledger agreement). The censuses (the v148\n# census axes re-measured — a drift re-check):"),
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
    # (→ v130 → v136 → v142 → v148 → v154) — the re-run chain's middle
    # entries are provenance, not stale era tokens; the SURFACE-FAMILY name
    # "the v142-era pair" (the lineage's own designation, preserved exactly
    # as the v148 form preserved it and the v153 form preserved "the
    # v129-era LOGIN + CALCULATOR pair"); the era marker "last re-shot
    # v148"; the oldest-remaining list "[v148 < v149 < v150 < v151 < v152 <
    # v153]"; the axis-provenance citations (the v41/v44/v46/v50/v53/v60/
    # v63/v67/v82 pin families cited in the compare header; the v43/v56/
    # v73/v75 rules); the corrected census provenance "the v148 census
    # axes re-measured".
    for dst in FILES.values():
        text = open(dst, encoding="utf-8").read()
        bad = []
        for m in re.finditer(
            r"re-shot v142|v142 < v143|FOURTEENTH re-run|SEVENTY-FIRST|"
            r"refvlm148|clonevlm148|refar148|clonear148|"
            r"/tmp/vlm148",
            text,
        ):
            bad.append(m.group(0))
        # bare-v142 sweep: the corrected bracket + the family name are the
        # sole legitimate survivors
        for m in re.finditer(r"v142", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v130 → v136 → v142 → v148 → v154" in ctx:
                continue
            if "v142-era" in ctx:
                continue
            bad.append("v142 (outside the corrected bracket/family name)")
        # v143/v144 sweep: the old oldest-remaining list tokens must be
        # wholly gone (the corrected list re-points at v148..v153)
        for m in re.finditer(r"v14[34]", text):
            bad.append(f"{m.group(0)} (old oldest-remaining token)")
        # bare-v148 sweep: the corrected bracket + the corrected era marker
        # ("last re-shot v148" / "last re-shot\n# v148;") + the corrected
        # oldest-remaining list ("[v148 < v149") + the corrected census
        # provenance ("the v148\n# census axes" — the line-wrapped form) are
        # the sole legitimate survivors
        for m in re.finditer(r"v148", text):
            ctx = text[max(0, m.start() - 60):m.end() + 60]
            if "→ v130 → v136 → v142 → v148 → v154" in ctx:
                continue
            if "re-shot" in ctx:
                continue
            if "oldest remaining [v148" in ctx:
                continue
            if "census axes re-measured" in ctx:
                continue
            bad.append("v148 (outside the corrected bracket/era marker/list/provenance)")
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
