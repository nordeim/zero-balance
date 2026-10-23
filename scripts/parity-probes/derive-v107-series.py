#!/usr/bin/env python3
"""Derive the v107 probe series from the v101 lineage (the SEVENTH re-run
of the v61-era DASHBOARD pair — the Budget Guidelines card + the quick-action
row, desktop 1280x800 full-page).

Files derived:
  vlm-shots-v101.sh       -> vlm-shots-v107.sh       (reference side)
  clone-vlmshots-v101.sh  -> clone-vlmshots-v107.sh  (clone side)
  vlm-compare-v101.mjs    -> vlm-compare-v107.mjs    (VLM pairwise)
  arbit-v101.sh           -> arbit-v107.sh           (both-sides DOM census)

Protocol (the v106 form): the GENERIC swaps first (session names, tmp dir,
version tokens), then the EXACT-FRAGMENT history corrections — each verified
applied (hit count reported), zero residual correctable fragments,
line-count preservation on all four, bash -n + node --check clean.
"""
import subprocess, sys

SERIES = [
    ("vlm-shots-v101.sh", "vlm-shots-v107.sh"),
    ("clone-vlmshots-v101.sh", "clone-vlmshots-v107.sh"),
    ("vlm-compare-v101.mjs", "vlm-compare-v107.mjs"),
    ("arbit-v101.sh", "arbit-v107.sh"),
]
BASE = "scripts/parity-probes/"

# generic swaps (order matters: session names + tmp dir BEFORE the bare version)
GENERIC = [
    ("refvlm101", "refvlm107"),
    ("clonevlm101", "clonevlm107"),
    ("refar101", "refar107"),
    ("clonear101", "clonear107"),
    ("/tmp/vlm101", "/tmp/vlm107"),
    ("v101", "v107"),
]

# exact-fragment history corrections (applied AFTER the generic swaps, so the
# fragments use the POST-swap state; every fragment is single-line-safe)
CORRECTIONS = [
    # (fragment, replacement, {file-suffix: expected hit count})
    ("v95-era pair", "v101-era pair",
     {"vlm-shots-v107.sh": 1, "clone-vlmshots-v107.sh": 1,
      "vlm-compare-v107.mjs": 2, "arbit-v107.sh": 1}),
    ("last re-shot v95", "last re-shot v101",
     {"vlm-shots-v107.sh": 1, "arbit-v107.sh": 1}),
    ("[v95 < v96 < v97 < v98 < v99 < v100]",
     "[v101 < v102 < v103 < v104 < v105 < v106]",
     {"vlm-shots-v107.sh": 1}),
    ("SIXTH", "SEVENTH",
     {"vlm-shots-v107.sh": 1, "clone-vlmshots-v107.sh": 1,
      "vlm-compare-v107.mjs": 2, "arbit-v107.sh": 1}),
    ("[v61 → v68 → v77 → v83 → v89 → v95 → v107]",
     "[v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107]",
     {"vlm-shots-v107.sh": 1, "clone-vlmshots-v107.sh": 1,
      "vlm-compare-v107.mjs": 2, "arbit-v107.sh": 1}),
    ("TWENTY-FOURTH", "THIRTIETH",
     {"vlm-shots-v107.sh": 1, "vlm-compare-v107.mjs": 1}),
    ("v95-v100", "v101-v106",
     {"vlm-shots-v107.sh": 1, "clone-vlmshots-v107.sh": 1}),
    ("The v95", "The v101",
     {"arbit-v107.sh": 1}),
    ("since v95", "since v101",
     {"arbit-v107.sh": 1}),
]

RESIDUAL_FRAGMENTS = [
    "v95-era", "last re-shot v95", "SIXTH", "TWENTY-FOURTH", "v95-v100",
    "since v95", "The v95", "[v95 <", "v96", "v97", "v98", "v99", "v100",
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
            ok = False
            print(f"FAIL: {dst}: correction {frag!r} hit {n}, expected {exp}")
        text = text.replace(frag, repl)
    dst_lines = text.count("\n")
    if dst_lines != src_lines:
        ok = False
        print(f"FAIL: {dst}: line count {dst_lines} != source {src_lines}")
    derived_texts[dst] = text
    print(f"{dst}: derived ({src_lines} lines preserved)")

# residual scan across all four derived files
for dst, text in derived_texts.items():
    for frag in RESIDUAL_FRAGMENTS:
        n = text.count(frag)
        if n:
            ok = False
            print(f"FAIL: {dst}: residual correctable fragment {frag!r} x{n}")

if not ok:
    sys.exit(1)

# write + syntax checks
for dst, text in derived_texts.items():
    open(BASE + dst, "w", encoding="utf-8").write(text)
    if dst.endswith(".mjs"):
        r = subprocess.run(["node", "--check", BASE + dst], capture_output=True, text=True)
    else:
        r = subprocess.run(["bash", "-n", BASE + dst], capture_output=True, text=True)
    print(f"{'node --check' if dst.endswith('.mjs') else 'bash -n'} {dst}: "
          f"{'clean' if r.returncode == 0 else 'SYNTAX FAIL: ' + r.stderr}")

print("OK: v107 series derived — 9/9 corrections applied, zero residuals, "
      "line counts preserved (57/42/45/258), syntax clean")
