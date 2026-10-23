#!/usr/bin/env python3
"""Derive the v108 probe series from the v102 lineage (the SEVENTH re-run
of the MOBILE 390 twins pair — BOTH mobile 390x844 full-page twins: the
/NETWORTH view [the v63-era pair's surface] + the DASHBOARD [the v62-era
mobile twin's surface]).

Files derived:
  vlm-shots-v102.sh       -> vlm-shots-v108.sh       (reference side)
  clone-vlmshots-v102.sh  -> clone-vlmshots-v108.sh  (clone side)
  vlm-compare-v102.mjs    -> vlm-compare-v108.mjs    (VLM pairwise)
  arbit-v102.sh           -> arbit-v108.sh           (both-sides DOM census)

Protocol (the v107 form): the GENERIC swaps first (session names, tmp dir,
version tokens), then the EXACT-FRAGMENT history corrections — each verified
applied (hit count reported), zero residual correctable fragments,
line-count preservation on all four, bash -n + node --check clean.
Every fragment is single-line-safe (the v107 derivation's own finding:
multi-line fragments are fragile; the v102 compare header wraps its
oldest-remaining bracket across lines 4-5, so the bracket is corrected as
two single-line halves).
"""
import subprocess, sys

SERIES = [
    ("vlm-shots-v102.sh", "vlm-shots-v108.sh"),
    ("clone-vlmshots-v102.sh", "clone-vlmshots-v108.sh"),
    ("vlm-compare-v102.mjs", "vlm-compare-v108.mjs"),
    ("arbit-v102.sh", "arbit-v108.sh"),
]
BASE = "scripts/parity-probes/"

# generic swaps (order matters: session names + tmp dir BEFORE the bare version)
GENERIC = [
    ("refvlm102", "refvlm108"),
    ("clonevlm102", "clonevlm108"),
    ("refarbit102", "refarbit108"),
    ("clonearbit102", "clonearbit108"),
    ("/tmp/vlm102", "/tmp/vlm108"),
    ("v102", "v108"),
]

# exact-fragment history corrections (applied AFTER the generic swaps, so the
# fragments use the POST-swap state; every fragment is single-line-safe)
CORRECTIONS = [
    # (fragment, replacement, {file-suffix: expected hit count})
    ("the v101 plan", "the v107 plan",
     {"vlm-shots-v108.sh": 1}),
    ("re-shot v96", "re-shot v102",
     {"vlm-shots-v108.sh": 1, "vlm-compare-v108.mjs": 1}),
    ("[v96 < v97 <", "[v102 < v103 <",
     {"vlm-shots-v108.sh": 1, "vlm-compare-v108.mjs": 1}),
    ("v98 < v99 < v100 < v101]", "v104 < v105 < v106 < v107]",
     {"vlm-shots-v108.sh": 1, "vlm-compare-v108.mjs": 1}),
    ("SIXTH", "SEVENTH",
     {"vlm-shots-v108.sh": 1, "vlm-compare-v108.mjs": 1, "arbit-v108.sh": 1}),
    ("v90 → v96 → v108", "v90 → v96 → v102 → v108",
     {"vlm-shots-v108.sh": 1, "vlm-compare-v108.mjs": 1, "arbit-v108.sh": 1}),
    ("the v84/v90/v96 re-runs", "the v84/v90/v96/v102 re-runs",
     {"vlm-compare-v108.mjs": 1, "arbit-v108.sh": 1}),
    ("The v96 census axes", "The v102 census axes",
     {"arbit-v108.sh": 1}),
]

# residual fragments that must be GONE after the corrections (specific forms
# only — the bare "v96" legitimately remains inside the re-run bracket's own
# history and the re-runs' verdict note; the pin-provenance tokens v41/v44/
# v45/v47/v51/v53/v61/v62/v63/v68/v73/v75/v84/v90 are whitelisted by context)
RESIDUAL_FRAGMENTS = [
    "the v101 plan", "re-shot v96", "SIXTH", "The v96 census",
    "[v96 <", "the v84/v90/v96 re-runs",
    "v97", "v98", "v99", "v100", "v101",
]

ok = True
derived_texts = {}
for src, dst in SERIES:
    text = open(BASE + src, encoding="utf-8").read()
    src_lines = text.count("\n")
    for old, new in GENERIC:
        text = text.replace(old, new)
    for frag, repl, expected in CORRECTIONS:
        n = text.count(frag) if dst in expected else 0
        exp = expected.get(dst, 0)
        if n != exp:
            print(f"MISS in {dst}: fragment {frag!r} expected {exp} hit(s), found {n}")
            ok = False
        else:
            text = text.replace(frag, repl)
    if text.count("\n") != src_lines:
        print(f"LINE-COUNT DRIFT in {dst}: {src_lines} -> {text.count(chr(10))}")
        ok = False
    derived_texts[dst] = text

# residual check across all four derived files (case-sensitive fragments)
joined = "\n".join(derived_texts.values())
for frag in RESIDUAL_FRAGMENTS:
    n = joined.count(frag)
    if n:
        print(f"RESIDUAL fragment {frag!r} still present: {n} hit(s)")
        ok = False

if ok:
    for dst, text in derived_texts.items():
        open(BASE + dst, "w", encoding="utf-8").write(text)
        print(f"derived {dst} ({text.count(chr(10))} lines)")
    for _, dst in SERIES:
        path = BASE + dst
        if dst.endswith(".mjs"):
            r = subprocess.run(["node", "--check", path], capture_output=True, text=True)
        else:
            r = subprocess.run(["bash", "-n", path], capture_output=True, text=True)
        print(f"{'node --check' if dst.endswith('.mjs') else 'bash -n'} {dst}: "
              f"{'clean' if r.returncode == 0 else r.stderr}")
        if r.returncode != 0:
            ok = False
else:
    sys.exit(1)

print("OK: v108 series derived — 8/8 corrections, zero residual, line counts preserved"
      if ok else "FAILED")
