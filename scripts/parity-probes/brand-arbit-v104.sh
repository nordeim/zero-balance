#!/usr/bin/env bash
# brand-arbit-v104.sh — the ONE-SHOT both-sides probe of the rail's BRAND
# BLOCK family (never census'd as a whole: the v7 G4 pin holds the
# tile/icon/h2 size+weight ONLY — the h2 color/lh, the subtitle P's chrome,
# and the row chrome were never pinned at ANY viewport in ANY spec): the
# flex row + the text column + the "Budget Planner" subtitle typography.
# Run on BOTH sides to verify the family is byte-identical before the pin.
# READ-ONLY. Double-quoted-heredoc-safe.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

BRAND_JS="(async () => {
  const rail = document.querySelector('aside') || [...document.querySelectorAll('nav,aside,div')].find(d => {
    const r = d.getBoundingClientRect();
    return r.width > 180 && r.width < 320 && r.height > 700 && r.left === 0;
  });
  if (!rail) return JSON.stringify({ err: 'no rail' });
  const h2 = [...rail.querySelectorAll('h2')].find(h => (h.textContent || '').trim() === 'ZeroBalance');
  if (!h2) return JSON.stringify({ err: 'no h2' });
  const col = h2.parentElement;
  const tile = col ? col.previousElementSibling : null;
  const row = col ? col.parentElement : null;
  const sub = col ? col.querySelector('p') : null;
  const h2cs = getComputedStyle(h2);
  const scs = sub ? getComputedStyle(sub) : null;
  const rcs = row ? getComputedStyle(row) : null;
  const tcs = tile ? getComputedStyle(tile) : null;
  const icon = tile ? tile.querySelector('svg') : null;
  return JSON.stringify({
    h2: { fs: h2cs.fontSize, fw: h2cs.fontWeight, lh: h2cs.lineHeight, color: h2cs.color },
    subtitle: sub ? {
      text: (sub.textContent || '').trim().slice(0, 24),
      fs: scs.fontSize, fw: scs.fontWeight, color: scs.color,
    } : null,
    row: row ? { display: rcs.display, align: rcs.alignItems, gap: rcs.gap } : null,
    col: col ? { display: getComputedStyle(col).display } : null,
    tile: tile ? {
      w: Math.round(tile.getBoundingClientRect().width),
      h: Math.round(tile.getBoundingClientRect().height),
      radius: tcs.borderRadius,
    } : null,
    icon: icon ? {
      w: getComputedStyle(icon).width, h: getComputedStyle(icon).height,
    } : null,
  });
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="refbrand104"
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
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$BRAND_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonebrand104"
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
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$BRAND_JS" 2>/dev/null | tail -1
EOF
echo "=== brand probe v104 done ==="
