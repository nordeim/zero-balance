#!/usr/bin/env python3
"""Build ref-arbit-v115.sh + clone-arbit-v115.sh from arbit-v115.sh (the
two-half controlled form, BUILT FROM THE START — the v92..v114 lesson).
The ONE census JS block (CENSUS_JS lines 22..214) is extracted ONCE and
embedded byte-identically in both halves (the contract, md5-verified).
Line numbers inherited verbatim from build-twohalf-v109.py — the v115
derivation is line-count-preserving (verified by derive-v115-series.py).
Expected md5: the v103/v109 census block verbatim [b55dcd29 — documented in
remediation-plan-v109.md]."""
import hashlib

SRC = "scripts/parity-probes/arbit-v115.sh"
lines = open(SRC).read().split("\n")  # 0-indexed; line N = lines[N-1]

# Census JS block (1-indexed inclusive): CENSUS_JS 22..214.
blocks = {}
for name, start, end in (("CENSUS_JS", 22, 214),):
    block = "\n".join(lines[start - 1 : end])
    assert block.startswith(f'{name}="(async () => {{'), block[:60]
    assert block.rstrip().endswith('})()"'), block[-60:]
    blocks[name] = block

# Header (lines 1..21): the shared provenance comments + set -u + REF var.
header = "\n".join(lines[0:21])
assert 'set -u' in header and 'REF="https://' in header, "header boundary wrong"

# The reference-side execution block: lines 216..250 (the marker through the
# last CENSUS_JS eval).
ref_exec = "\n".join(lines[215:250])
assert ref_exec.startswith('echo "=== REFERENCE side (1280) ==="'), ref_exec[:60]
assert ref_exec.rstrip().endswith('agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1'), ref_exec[-80:]

# The clone-side execution block — REWRITTEN into the env-injection form
# (the v73 heredoc lesson: QUOTED <<'EOF' with the census vars injected via
# the environment, so the census JS needs no heredoc escaping).
clone_login = """set -u
export AGENT_BROWSER_SESSION="clonearbit109"
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
echo "--- clone income ---"
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "--- clone expenses ---"
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
"""

TWOHALF_NOTE = """
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v114
# lesson): the combined arbit form's clone half is the chromium
# resource-exhaustion risk (the v89/v91-documented symptom class), so the
# census runs as two independent halves from the start; the census JS
# blocks are byte-identical across the halves (the md5 line-block
# contract).
"""

ref_half = f"""{header}
{TWOHALF_NOTE}
{blocks["CENSUS_JS"]}

########## REFERENCE SIDE (the half) ##########
{ref_exec}
echo "=== ref arbit v115 half done ==="
"""

clone_half = f"""{header}
{TWOHALF_NOTE}
{blocks["CENSUS_JS"]}

########## CLONE SIDE (the half) ##########
# ---------- CLONE side (inside with-server, censuses env-injected) ----------
cd "$(dirname "$0")/../.."
CENSUS_JS="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
{clone_login}EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== arbit v115 done ==="
"""

open("scripts/parity-probes/ref-arbit-v115.sh", "w").write(ref_half)
open("scripts/parity-probes/clone-arbit-v115.sh", "w").write(clone_half)

# The md5 line-block contract: the census blocks byte-identical across halves.
def block_md5(path, start_marker, end_marker):
    text = open(path).read()
    start = text.index(start_marker)
    end = text.index(end_marker, start) + len(end_marker)
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

for marker in ('CENSUS_JS="(async () => {',):
    end_marker = '})()"'
    rm, rn = block_md5("scripts/parity-probes/ref-arbit-v115.sh", marker, end_marker)
    cm, cn = block_md5("scripts/parity-probes/clone-arbit-v115.sh", marker, end_marker)
    assert rm == cm, f"CENSUS BLOCK MISMATCH for {marker[:20]}: {rm} vs {cm}"
    print(f"block {marker[:12]}... md5 {rm} — {rn} lines — byte-identical across halves OK")

# The doubled-brace spot check (the v95 template-brace lesson): the census
# body must not carry doubled {{ that would break the bash var literal.
import re
for path in ("scripts/parity-probes/ref-arbit-v115.sh", "scripts/parity-probes/clone-arbit-v115.sh"):
    text = open(path).read()
    start = text.index('CENSUS_JS="(async () => {')
    end = text.index('})()"', start)
    body = text[start:end]
    doubled = re.findall(r"\{\{|\}\}", body)
    if doubled:
        print(f"WARNING {path}: doubled braces in census body: {len(doubled)}")
    else:
        print(f"doubled-brace spot check {path}: clean")

print("ref-arbit-v115.sh + clone-arbit-v115.sh built")
