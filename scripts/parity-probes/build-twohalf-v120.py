#!/usr/bin/env python3
"""Build ref-arbit-v120.sh + clone-arbit-v120.sh from arbit-v120.sh (the
two-half controlled form, BUILT FROM THE START — the v92..v119 lesson).
The TWO census JS blocks (NW_CENSUS lines 18..59, DASH_CENSUS lines 61..147)
are extracted ONCE and embedded byte-identically in both halves (the
contract, md5-verified). Line numbers inherited verbatim from
build-twohalf-v114.py — the v120 derivation is line-count-preserving
(verified by derive-v120-series.py). Expected md5s: the v102 census blocks
verbatim [82cf8a43 / 85e4ec7e — documented in remediation-plan-v102.md]."""
import hashlib

SRC = "scripts/parity-probes/arbit-v120.sh"
lines = open(SRC).read().split("\n")  # 0-indexed; line N = lines[N-1]

# Census JS blocks (1-indexed inclusive): NW_CENSUS 18..59, DASH_CENSUS 61..147.
blocks = {}
for name, start, end in (("NW_CENSUS", 18, 59), ("DASH_CENSUS", 61, 147)):
    block = "\n".join(lines[start - 1 : end])
    assert block.startswith(f'{name}="(async () => {{'), block[:60]
    assert block.rstrip().endswith('})()"'), block[-60:]
    blocks[name] = block

# Header (lines 1..16): the shared provenance comments + set -u + REF var.
header = "\n".join(lines[0:16])
assert 'set -u' in header and 'REF="https://' in header, "header boundary wrong"

# The reference-side execution block: lines 149..185 (the marker through the
# last DASH_CENSUS eval).
ref_exec = "\n".join(lines[148:185])
assert ref_exec.startswith('echo "=== REFERENCE side (390): networth ==="'), ref_exec[:60]
assert ref_exec.rstrip().endswith('agent-browser eval "$DASH_CENSUS" 2>/dev/null | tail -1'), ref_exec[-80:]

# The clone-side execution block — REWRITTEN into the env-injection form
# (the v73 heredoc lesson: QUOTED <<'EOF' with the census vars injected via
# the environment, so the census JS needs no heredoc escaping). Inherited
# verbatim from build-twohalf-v114.py with the session token bumped.
clone_login = """set -u
export AGENT_BROWSER_SESSION="clonearbit120"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser eval "$NW_CENSUS" 2>/dev/null | tail -1
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$DASH_CENSUS" 2>/dev/null | tail -1
"""

TWOHALF_NOTE = """
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v119
# lesson): the combined arbit form's clone half is the chromium
# resource-exhaustion risk (the v89/v91-documented symptom class), so the
# census runs as two independent halves from the start; the census JS
# blocks are byte-identical across the halves (the md5 line-block
# contract).
"""

ref_half = f"""{header}
{TWOHALF_NOTE}
{blocks["NW_CENSUS"]}

{blocks["DASH_CENSUS"]}

########## REFERENCE SIDE (the half) ##########
{ref_exec}
echo "=== ref arbit v120 half done ==="
"""

clone_half = f"""{header}
{TWOHALF_NOTE}
{blocks["NW_CENSUS"]}

{blocks["DASH_CENSUS"]}

########## CLONE SIDE (the half) ##########
# ---------- CLONE side (inside with-server, censuses env-injected) ----------
cd "$(dirname "$0")/../.."
NW_CENSUS="$NW_CENSUS" DASH_CENSUS="$DASH_CENSUS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
{clone_login}EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== arbit v120 done ==="
"""

open("scripts/parity-probes/ref-arbit-v120.sh", "w").write(ref_half)
open("scripts/parity-probes/clone-arbit-v120.sh", "w").write(clone_half)

# The md5 line-block contract: the census blocks byte-identical across halves.
def block_md5(path, start_marker, end_marker):
    text = open(path).read()
    start = text.index(start_marker)
    end = text.index(end_marker, start) + len(end_marker)
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

for marker in ('NW_CENSUS="(async () => {', 'DASH_CENSUS="(async () => {'):
    end_marker = '})()"'
    rm, rn = block_md5("scripts/parity-probes/ref-arbit-v120.sh", marker, end_marker)
    cm, cn = block_md5("scripts/parity-probes/clone-arbit-v120.sh", marker, end_marker)
    assert rm == cm, f"CENSUS BLOCK MISMATCH for {marker[:20]}: {rm} vs {cm}"
    print(f"block {marker[:12]}... md5 {rm} — {rn} lines — byte-identical across halves OK")

print("ref-arbit-v120.sh + clone-arbit-v120.sh built")
