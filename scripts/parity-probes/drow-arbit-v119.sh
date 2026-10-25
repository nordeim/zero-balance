#!/usr/bin/env bash
# drow-arbit-v119.sh — the ONE-SHOT both-sides DOM census for the v119 F4
# candidate: the DASHBOARD PAGE-HEADER ROW at desktop 1280x800 (the desktop
# twin of the v114 F4 pin's 390 family — the element family every 1280
# dashboard census walked past: the v40 F1 Tab-order census pins the Add
# Item button's POSITION BAND [x 1121, w 127, h 36] only; the session-5 pin
# the button's gradient only; the v35 S2 pin the focus shadow; the G3 pin
# the Plus icon's default-viewport geometry; the v114 F4 pin the row's flex
# chrome + the block->button junction + the button's box chrome at 390
# ONLY; the v62 F2 pin the subtitle block's interior at 390 ONLY — the
# family's computed chrome at 1280 [the row's flex/flex-row/center/gap/mb,
# the h1's md:text-4xl 36px chrome, the subtitle's chrome, the block's
# h/w, the horizontal junction (the block's right -> the button's left:
# the row's gap-4), the row->stat-grid rhythm (the mb-8 rendered)] is
# never pinned in ANY spec at 1280).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors.
# The pin's axes stay DATA-INDEPENDENT (the h1/subtitle/button texts are
# FIXED strings, identical on both sites; the absolute x positions stay
# the v40 band's own — the v107 position-arithmetic discipline).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

DROW_JS="(async () => {
  const h1 = [...document.querySelectorAll('h1')].find(x => (x.textContent || '').trim() === 'Budget Dashboard');
  if (!h1) return JSON.stringify({ drow: 'no h1' });
  const block = h1.parentElement;
  const row = block ? block.parentElement : null;
  if (!block || !row) return JSON.stringify({ drow: 'no block/row' });
  const rcs = getComputedStyle(row);
  const rr = row.getBoundingClientRect();
  const br = block.getBoundingClientRect();
  const hcs = getComputedStyle(h1);
  const sub = [...block.children].find(c => c !== h1);
  const scs = sub ? getComputedStyle(sub) : null;
  const sr = sub ? sub.getBoundingClientRect() : null;
  const btn = [...row.querySelectorAll('button')].find(b => /Add Item/i.test(b.textContent || ''));
  const btnOut = btn ? (() => {
    const s = getComputedStyle(btn);
    const r = btn.getBoundingClientRect();
    const icon = btn.querySelector('svg');
    return {
      left: Math.round(r.left), top: Math.round(r.top),
      h: Math.round(r.height), w: Math.round(r.width),
      pad: s.padding, radius: s.borderRadius,
      fs: s.fontSize, fw: s.fontWeight, color: s.color,
      bg: (s.backgroundImage || '').replace(/\\s+/g, ' ').slice(0, 90),
      icon: icon ? { w: Math.round(icon.getBoundingClientRect().width), h: Math.round(icon.getBoundingClientRect().height) } : null
    };
  })() : null;
  const next = row.nextElementSibling;
  const nr = next ? next.getBoundingClientRect() : null;
  return JSON.stringify({
    view: 'dash-header-1280-v119',
    row: {
      display: rcs.display, flexDirection: rcs.flexDirection,
      align: rcs.alignItems, justify: rcs.justifyContent,
      gap: rcs.columnGap, mb: rcs.marginBottom,
      h: Math.round(rr.height), w: Math.round(rr.width)
    },
    h1: { fs: hcs.fontSize, fw: hcs.fontWeight, lh: hcs.lineHeight, color: hcs.color, h: Math.round(h1.getBoundingClientRect().height), mb: hcs.marginBottom },
    subtitle: sub && scs ? { fs: scs.fontSize, fw: scs.fontWeight, lh: scs.lineHeight, color: scs.color, h: Math.round(sr.height) } : 'not found',
    block: { h: Math.round(br.height), w: Math.round(br.width), right: Math.round(br.right), bottom: Math.round(br.bottom) },
    addBtn: btnOut,
    junction: btnOut ? { hGap: btnOut.left - Math.round(br.right), rowColGap: rcs.columnGap } : null,
    nextGap: nr ? { gap: Math.round(nr.top - rr.bottom), nextTag: next.tagName.toLowerCase() } : null,
    docSW: document.documentElement.scrollWidth
  });
})()"

echo "=== REFERENCE side (1280, /) ==="
export AGENT_BROWSER_SESSION="refdrow119"
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
  set(pw, '\$Abcd1234');
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
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$DROW_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /) ==="
cd "$(dirname "$0")/../.."
DROW_JS="$DROW_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonedrow119"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$DROW_JS" 2>/dev/null | tail -1
EOF
echo "=== drow arbit v119 done ==="
