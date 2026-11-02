#!/usr/bin/env python3
"""Derive the 141st standing-checks pair from the 140th pair.

Three token families (the documented derivation protocol):
  1. v140 -> v141           (version tokens)
  2. 140th -> 141st         (ordinal tokens — a th->st plain replace,
                             the suffix following the number's English
                             form, the same plain-replace family as the
                             chain's prior st transitions, e.g. v138's
                             131st->132nd and the v121/v131 lineage's
                             121st/131st forms)
  3. ref140 -> ref141 / clone140 -> clone141   (bare session names)

After derivation, normalize BACK (v141->v140 etc.) and diff against the
originals to prove the files are version-bump-only (zero functional drift).
NOTE: the ordinal replacement runs FIRST and the bare-session replacement
runs BEFORE the version replacement (the documented ordering).
"""
import re
import subprocess
import sys

PAIR = [
    ("scripts/parity-probes/ref-standing-v140.sh",
     "scripts/parity-probes/ref-standing-v141.sh"),
    ("scripts/parity-probes/standing-checks-v140.sh",
     "scripts/parity-probes/standing-checks-v141.sh"),
]

def derive(src: str, dst: str) -> str:
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    # ordinal FIRST ("140th" -> "141st"), then bare session names, then version
    text = text.replace("140th", "141st")
    text = text.replace("ref140", "ref141")
    text = text.replace("clone140", "clone141")
    text = text.replace("v140", "v141")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)
    return text

def normalize_back(text: str) -> str:
    text = text.replace("141st", "140th")
    text = text.replace("ref141", "ref140")
    text = text.replace("clone141", "clone140")
    text = text.replace("v141", "v140")
    return text

ok = True
for src, dst in PAIR:
    derived = derive(src, dst)
    with open(src, "r", encoding="utf-8") as f:
        original = f.read()
    if normalize_back(derived) != original:
        ok = False
        print(f"FAIL: {dst} is NOT version-bump-only vs {src}")
    # residual old-token check on the derived file
    residual = re.findall(r"v140|140th|ref140|clone140", derived)
    if residual:
        ok = False
        print(f"FAIL: {dst} retains old tokens: {set(residual)}")

if not ok:
    sys.exit(1)

# syntax gates on both halves
for _, dst in PAIR:
    r = subprocess.run(["bash", "-n", dst], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"FAIL: bash -n {dst}: {r.stderr}")
        sys.exit(1)

# line-count preservation (the documented contract)
for src, _ in PAIR:
    with open(src, "r", encoding="utf-8") as f:
        src_lines = len(f.read().splitlines())
    print(f"{src}: {src_lines} lines")
for _, dst in PAIR:
    with open(dst, "r", encoding="utf-8") as f:
        dst_lines = len(f.read().splitlines())
    print(f"{dst}: {dst_lines} lines")

print("141st standing pair derived clean (ref-standing-v141.sh + standing-checks-v141.sh)")
