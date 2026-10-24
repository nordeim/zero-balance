#!/usr/bin/env python3
"""Derive the v110 probe series from the v104 lineage (the EIGHTH re-run
of the SAVINGS pair — the SAVINGS view at desktop 1280x800
[v58 -> v65 -> v74 -> v80 -> v86 -> v92 -> v98 -> v104 -> v110]).

Files derived:
  vlm-shots-v104.sh       -> vlm-shots-v110.sh       (reference side)
  clone-vlmshots-v104.sh  -> clone-vlmshots-v110.sh  (clone side)
  vlm-compare-v104.mjs    -> vlm-compare-v110.mjs    (VLM pairwise)
  arbit-v104.sh           -> arbit-v110.sh           (both-sides DOM census)

Protocol (the v107/v108/v109 form): the GENERIC swaps first (session names,
tmp dir, version tokens), then the EXACT-FRAGMENT history corrections —
each verified applied (hit count reported), zero residual correctable
fragments, line-count preservation on all four, bash -n + node --check
clean. Every fragment is single-line-safe (the v107 lesson).
"""
import subprocess, sys

SERIES = [
    ("vlm-shots-v104.sh", "vlm-shots-v110.sh"),
    ("clone-vlmshots-v104.sh", "clone-vlmshots-v110.sh"),
    ("vlm-compare-v104.mjs", "vlm-compare-v110.mjs"),
    ("arbit-v104.sh", "arbit-v110.sh"),
]
BASE = "scripts/parity-probes/"

# generic swaps (order matters: session names + tmp dir BEFORE the bare version)
GENERIC = [
    ("refvlm104", "refvlm110"),
    ("clonevlm104", "clonevlm110"),
    ("refarbit104", "refarbit110"),
    ("clonearbit104", "clonearbit110"),
    ("/tmp/vlm104", "/tmp/vlm110"),
    ("v104", "v110"),
]

# exact-fragment history corrections (applied AFTER the generic swaps, so the
# fragments use the POST-swap state; every fragment is single-line-safe)
CORRECTIONS = [
    # (fragment, replacement, {file-suffix: expected hit count})
    ("(the v98-era savings pair, last re-shot",
     "(the v104-era savings pair, last re-shot",
     {"vlm-shots-v110.sh": 1, "clone-vlmshots-v110.sh": 1}),
    ("# v98, now the oldest remaining [v98 < v99 < v100 < v101 < v102 < v103]; the",
     "# v104, now the oldest remaining [v104 < v105 < v106 < v107 < v108 < v109]; the",
     {"vlm-shots-v110.sh": 1, "clone-vlmshots-v110.sh": 1}),
    ("v103 plan's v110 queue suggestion",
     "v109 plan's v110 queue suggestion",
     {"vlm-shots-v110.sh": 1}),
    ("the TWENTY-SEVENTH consecutive agreement). READ-ONLY",
     "the THIRTY-THIRD consecutive agreement). READ-ONLY",
     {"vlm-shots-v110.sh": 1}),
    ("SEVENTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v110]",
     "EIGHTH re-run [v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110]",
     {"clone-vlmshots-v110.sh": 1}),
    ("(the v98-era savings pair's SEVENTH re-run — last re-shot",
     "(the v104-era savings pair's EIGHTH re-run — last re-shot",
     {"vlm-compare-v110.mjs": 1}),
    ("// v98, now the oldest remaining [v98 < v99 < v100 < v101 < v102 < v103] — agreeing with the rotation ledger, the TWENTY-SEVENTH consecutive agreement).",
     "// v104, now the oldest remaining [v104 < v105 < v106 < v107 < v108 < v109] — agreeing with the rotation ledger, the THIRTY-THIRD consecutive agreement).",
     {"vlm-compare-v110.mjs": 1}),
    ("the v98-era savings pair's SEVENTH re-run, last re-shot v98 — now the",
     "the v104-era savings pair's EIGHTH re-run, last re-shot v104 — now the",
     {"arbit-v110.sh": 1}),
    ("oldest remaining candidate [v98 < v99 < v100 < v101 < v102 < v103]).",
     "oldest remaining candidate [v104 < v105 < v106 < v107 < v108 < v109]).",
     {"arbit-v110.sh": 1}),
]

# residual fragments that must be GONE after the corrections (specific forms
# only — the corrected bracket "[v104 < v105 < ...]" and the new "re-shot
# v104" are the NEW history; the bare "v98" tokens that REMAIN are the
# legitimate history: clone's re-run bracket "v92 → v98 → v104 → v110" and
# arbit's "v98-era pin candidate" provenance (the v110 census's own axes
# comments); the pin-provenance tokens v43/v46/v51/v54/v57/v58/v64/v65/v68/
# v73/v74/v80 are whitelisted by context)
RESIDUAL_FRAGMENTS = [
    "v98-era savings pair", "SEVENTH", "TWENTY-SEVENTH", "[v98 <",
    "re-shot v98", "v99", "v100", "v101", "v102", "v103",
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

print("OK: v110 series derived — 9 corrections (11 hit-checks), zero residual, line counts preserved"
      if ok else "FAILED")
