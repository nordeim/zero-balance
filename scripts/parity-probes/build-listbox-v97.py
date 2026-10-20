#!/usr/bin/env python3
"""Build listbox-arbit-v97.sh + listbox-clone-v97.sh — the supplemental
two-half census for the v97 pin's own axes (the filter LISTBOX PANEL +
OPTION-RESTING interior at 1280 on the income view's category filter),
BUILT TWO-HALF FROM THE START (the v92..v95 lesson, the v96 headrow
precedent). The census JS block is extracted ONCE from this builder and
embedded byte-identically in both halves (the md5 line-block contract)."""
import hashlib

# The census JS — shared byte-identically across both halves. Open the
# category filter, settle past the animate-in window, then census the
# PANEL chrome + the VIEWPORT pad + the first option's RESTING interior.
CENSUS_JS = """LBOX_JS="(async () => {
  const trig = [...document.querySelectorAll('button')].find(b => {
    const al = b.getAttribute('aria-label') || '';
    return al.includes('category') || /All Categories/.test(b.textContent || '');
  });
  if (!trig) return JSON.stringify({ err: 'no trigger' });
  trig.click();
  await new Promise(r => setTimeout(r, 700));
  const lb = document.querySelector('[role=listbox]');
  if (!lb) return JSON.stringify({ err: 'no listbox' });
  const cs = getComputedStyle(lb);
  const r = lb.getBoundingClientRect();
  const vp = lb.querySelector('[data-radix-select-viewport]') ||
    [...lb.children].find(c => getComputedStyle(c).padding === '4px');
  const vcs = vp ? getComputedStyle(vp) : null;
  const opt = lb.querySelector('[role=option]');
  const ocs = opt ? getComputedStyle(opt) : null;
  const or = opt ? opt.getBoundingClientRect() : null;
  return JSON.stringify({
    panel: {
      bg: cs.backgroundColor, radius: cs.borderRadius,
      border: cs.borderWidth + ' ' + cs.borderColor,
      shadow: cs.boxShadow, maxH: cs.maxHeight,
      overflow: cs.overflow, z: cs.zIndex, pos: cs.position,
      w: Math.round(r.width), h: Math.round(r.height)
    },
    viewport: vcs ? { pad: vcs.padding, display: vcs.display } : 'not found',
    opt0: ocs ? {
      fs: ocs.fontSize, fw: ocs.fontWeight, color: ocs.color,
      pad: ocs.padding, radius: ocs.borderRadius,
      h: or ? Math.round(or.height) : null
    } : null,
    optCount: lb.querySelectorAll('[role=option]').length,
    docSW: document.documentElement.scrollWidth
  });
})()"
"""

REF_HALF = """#!/usr/bin/env bash
# listbox-arbit-v97.sh — the REFERENCE half of the supplemental two-half
# census for the v97 pin's axes (the filter listbox PANEL + option-resting
# interior at 1280, the income view's category filter). READ-ONLY.
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v95 lesson).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

""" + CENSUS_JS + """
export AGENT_BROWSER_SESSION="reflboxarbit97"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 5
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$LBOX_JS" 2>/dev/null | tail -1
echo "=== ref listbox arbit v97 half done ==="
"""

CLONE_HALF = """#!/usr/bin/env bash
# listbox-clone-v97.sh — the CLONE half of the supplemental two-half
# census for the v97 pin's axes (the filter listbox PANEL + option-resting
# interior at 1280, the income view's category filter). READ-ONLY.
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v95 lesson).
# Runs inside with-server.sh (the :3200 parity server).
set -u
cd "$(dirname "$0")/../.."

""" + CENSUS_JS + """
LBOX_JS="$LBOX_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonelboxarbit97"
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
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 5
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$LBOX_JS" 2>/dev/null | tail -1
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== clone listbox arbit v97 half done ==="
"""

open("scripts/parity-probes/listbox-arbit-v97.sh", "w").write(REF_HALF)
open("scripts/parity-probes/listbox-clone-v97.sh", "w").write(CLONE_HALF)

# The md5 line-block contract: the census JS byte-identical across halves.
def block_md5(path, start_marker, end_marker):
    text = open(path).read()
    start = text.index(start_marker)
    end = text.index(end_marker, start) + len(end_marker)
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

rm, rn = block_md5("scripts/parity-probes/listbox-arbit-v97.sh",
                   'LBOX_JS="(async () => {', '})()"')
cm, cn = block_md5("scripts/parity-probes/listbox-clone-v97.sh",
                   'LBOX_JS="(async () => {', '})()"')
assert rm == cm, f"CENSUS BLOCK MISMATCH: {rm} vs {cm}"
print(f"block LBOX_JS md5 {rm} — {rn} lines — byte-identical across halves OK")

# The doubled-brace spot check (the v95 template-brace lesson).
import re
for path in ("scripts/parity-probes/listbox-arbit-v97.sh",
             "scripts/parity-probes/listbox-clone-v97.sh"):
    text = open(path).read()
    start = text.index('LBOX_JS="(async () => {')
    end = text.index('})()"', start)
    body = text[start:end]
    doubled = re.findall(r"\{\{|\}\}", body)
    if doubled:
        print(f"WARNING {path}: doubled braces in census body: {len(doubled)}")
    else:
        print(f"doubled-brace spot check {path}: clean")

print("listbox-arbit-v97.sh + listbox-clone-v97.sh built")
