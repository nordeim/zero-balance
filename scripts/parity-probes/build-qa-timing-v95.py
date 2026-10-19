#!/usr/bin/env python3
"""build-qa-timing-v95.py — the supplemental two-half census for the v95
pin's own axes (the quick-action row's TRANSITION-TIMING family at 1280),
BUILT TWO-HALF from the start (the v87..v94 supplemental precedent): the
census JS block is embedded byte-identically across the reference half
(qa-timing-arbit-v95.sh) and the clone half (qa-timing-clone-v95.sh)."""
import hashlib

CENSUS_JS = r"""CENSUS_JS="(async () => {
  const out = { view: 'qa-timing-1280-v95' };
  const qas = [...document.querySelectorAll('button')].filter(
    (b) => /^Add (Income|Savings|Expense)$/.test((b.textContent || '').trim())
  );
  if (qas.length !== 3) return JSON.stringify({ err: 'qa count ' + qas.length });
  out.cards = qas.map((b) => {
    const cs = getComputedStyle(b);
    const svgs = [...b.querySelectorAll('svg')];
    const plus = svgs[svgs.length - 1];
    const tile = [...b.querySelectorAll('span, div')].find((s) => {
      const st = getComputedStyle(s);
      const sr = s.getBoundingClientRect();
      return st.borderRadius === '12px' && sr.width >= 30 && sr.width <= 60 && sr.height >= 30 && sr.height <= 60;
    });
    const pcs = plus ? getComputedStyle(plus) : null;
    const tcs = tile ? getComputedStyle(tile) : null;
    return {
      text: (b.textContent || '').trim(),
      cardTiming: cs.transitionTimingFunction,
      cardDelay: cs.transitionDelay,
      tileTransition: tcs ? { prop: tcs.transitionProperty, dur: tcs.transitionDuration, timing: tcs.transitionTimingFunction } : null,
      plusTransition: pcs ? { prop: pcs.transitionProperty, dur: pcs.transitionDuration, timing: pcs.transitionTimingFunction, delay: pcs.transitionDelay } : null
    };
  });
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()""" + '"'

REF_HALF = """#!/usr/bin/env bash
# qa-timing-arbit-v95.sh — the ONE-SHOT census for the v95 pin's own
# axes, REFERENCE half (the v87..v94 supplemental precedent, BUILT
# TWO-HALF from the start): the quick-action row's TRANSITION-TIMING
# family at desktop 1280 — the three cards' transitionTimingFunction +
# transitionDelay (the v89 pin holds the duration/property only), the
# three tinted tiles' transition-transform family (never pinned — the
# v61 F3 pin holds the tile's GEOMETRY), and the three plus icons'
# transition-opacity family (never pinned). Read-only (login + passive
# navigation — the v46 rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

{CENSUS}

export AGENT_BROWSER_SESSION="refqat95"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {{
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {{
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', {{ bubbles: true }}));
  }};
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
}})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "ref login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 5
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== PART T: REF qa-timing census at 1280 ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== ref qa-timing v95 half done ==="
""".replace("{CENSUS}", CENSUS_JS)

CLONE_HALF = """#!/usr/bin/env bash
# qa-timing-clone-v95.sh — the ONE-SHOT census for the v95 pin's own
# axes, CLONE half (BUILT TWO-HALF from the start): the quick-action
# row's TRANSITION-TIMING family at desktop 1280. Runs inside
# with-server.sh (the :3200 parity server). Read-only; the seedcheck
# at the end (the v66 discipline).
set -u
cd "$(dirname "$0")/../.."

{CENSUS}

CENSUS_JS="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneqat95"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 5
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== PART T: CLONE qa-timing census at 1280 ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== seedcheck (env -u DATABASE_URL — the documented pollution discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs
echo "=== clone qa-timing v95 half done ==="
EOF
""".replace("{CENSUS}", CENSUS_JS)

open("scripts/parity-probes/qa-timing-arbit-v95.sh", "w").write(REF_HALF)
open("scripts/parity-probes/qa-timing-clone-v95.sh", "w").write(CLONE_HALF)

# The md5 line-block contract: the census JS byte-identical across halves.
def census_md5(path):
    text = open(path).read()
    start = text.index('CENSUS_JS="(async () => {')
    end = text.index('})()"', start) + len('})()"')
    block = text[start:end]
    return hashlib.md5(block.encode()).hexdigest()[:8], block.count("\n") + 1

rm, rn = census_md5("scripts/parity-probes/qa-timing-arbit-v95.sh")
cm, cn = census_md5("scripts/parity-probes/qa-timing-clone-v95.sh")
assert rm == cm, f"CENSUS JS MISMATCH: {rm} vs {cm}"
print(f"census JS md5 {rm} — {rn} lines — byte-identical across halves OK")
print("qa-timing-arbit-v95.sh + qa-timing-clone-v95.sh built")
