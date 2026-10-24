#!/usr/bin/env bash
# drow-arbit-v114.sh — the ONE-SHOT both-sides DOM census for the v114 F4
# candidate: the DASHBOARD mobile twin's HEADER-ROW interior family at 390
# (the family every dashboard header census walked past — the v62 pin walks
# the h1's PARENT BLOCK's interior (h1/P/block arithmetic), never the ROW
# that carries the block + the Add Item button; the session-5 pin the
# button's gradient only; the v35 S2 pin the focus shadow; the G3 pin the
# Plus icon at 1280). The axes:
#   the row's own flex chrome {display/flexDirection/align/justify/gap/mb},
#   the junction (the block's bottom -> the button's top: the row's gap-4),
#   the Add Item button's BOX chrome {h/w/pad/radius/fs/fw/color/bg/icon},
#   and the docSW guard.
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors.
# The pin's axes stay DATA-INDEPENDENT (the h1/subtitle/button texts are
# FIXED strings, identical on both sites; the block's/button's x positions
# unpinned — the v107 position-arithmetic discipline).
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
  const btn = [...row.querySelectorAll('button')].find(b => /Add Item/i.test(b.textContent || ''));
  const btnOut = btn ? (() => {
    const s = getComputedStyle(btn);
    const r = btn.getBoundingClientRect();
    const icon = btn.querySelector('svg');
    return {
      top: Math.round(r.top), h: Math.round(r.height), w: Math.round(r.width),
      pad: s.padding, radius: s.borderRadius,
      fs: s.fontSize, fw: s.fontWeight, color: s.color,
      bg: (s.backgroundImage || '').replace(/\\s+/g, ' ').slice(0, 90),
      icon: icon ? { w: Math.round(icon.getBoundingClientRect().width), h: Math.round(icon.getBoundingClientRect().height) } : null
    };
  })() : null;
  return JSON.stringify({
    row: {
      display: rcs.display, flexDirection: rcs.flexDirection,
      align: rcs.alignItems, justify: rcs.justifyContent,
      gap: rcs.rowGap, mb: rcs.marginBottom,
      h: Math.round(rr.height)
    },
    block: { h: Math.round(br.height), bottom: Math.round(br.bottom) },
    addBtn: btnOut,
    junction: btnOut ? { gap: btnOut.top - Math.round(br.bottom) } : null,
    docSW: document.documentElement.scrollWidth
  });
})()"

echo "=== REFERENCE side (390, /) ==="
export AGENT_BROWSER_SESSION="refdrow114"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$DROW_JS" 2>/dev/null | tail -1

echo "=== CLONE side (390, /) ==="
cd "$(dirname "$0")/../.."
DROW_JS="$DROW_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonedrow114"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$DROW_JS" 2>/dev/null | tail -1
EOF
echo "=== drow arbit v114 done ==="
