#!/usr/bin/env bash
# userfooter-probe-v103.sh — the ONE-SHOT both-sides probe of the rail's
# bottom USER-FOOTER family (never census'd at any viewport): the border-t
# wrapper + the tinted tile + the name/subtitle typography. Run on BOTH
# sides to verify the family is byte-identical before the pin.
# READ-ONLY. Double-quoted-heredoc-safe.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

UF_JS="(async () => {
  const rail = document.querySelector('aside') || [...document.querySelectorAll('nav,aside,div')].find(d => {
    const r = d.getBoundingClientRect();
    return r.width > 180 && r.width < 320 && r.height > 700 && r.left === 0;
  });
  if (!rail) return JSON.stringify({ err: 'no rail' });
  // the avatar: the v79 finder (round 1-2 char element)
  const avatar = [...rail.querySelectorAll('div,span,button')].find(el => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    const t = (el.textContent || '').trim();
    return r.width >= 30 && r.width <= 45 && Math.abs(r.width - r.height) < 3
      && parseFloat(cs.borderRadius) > 100 && t.length >= 1 && t.length <= 2;
  });
  if (!avatar) return JSON.stringify({ err: 'no avatar' });
  // the TILE: the avatar's nearest ancestor with a visible bg + radius
  let tile = avatar.parentElement;
  for (let i = 0; i < 4 && tile; i++) {
    const cs = getComputedStyle(tile);
    if (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && parseFloat(cs.borderRadius) > 0) break;
    tile = tile.parentElement;
  }
  if (!tile) return JSON.stringify({ err: 'no tile' });
  const tcs = getComputedStyle(tile);
  const tr = tile.getBoundingClientRect();
  // the wrapper: the tile's parent (border-t + p-4)
  const wrap = tile.parentElement;
  const wcs = wrap ? getComputedStyle(wrap) : null;
  // the name + subtitle: the tile's text leaves
  const texts = [...tile.querySelectorAll('p, span, div')].filter(el => {
    const t = (el.textContent || '').trim();
    return t.length > 2 && el.children.length === 0;
  });
  const leaf = (el) => {
    const cs = getComputedStyle(el);
    return {
      text: (el.textContent || '').trim().slice(0, 24),
      fs: cs.fontSize, fw: cs.fontWeight, color: cs.color,
      truncate: cs.textOverflow,
    };
  };
  return JSON.stringify({
    tile: {
      w: Math.round(tr.width), h: Math.round(tr.height),
      radius: tcs.borderRadius, pad: tcs.padding,
      bg: tcs.backgroundColor, display: tcs.display,
      align: tcs.alignItems, gap: tcs.gap,
    },
    wrapper: wcs ? {
      borderTop: wcs.borderTopWidth + ' ' + wcs.borderTopColor,
      pad: wcs.padding, gap: wcs.gap, display: wcs.display,
    } : null,
    avatar: { w: Math.round(avatar.getBoundingClientRect().width) },
    name: texts[0] ? leaf(texts[0]) : null,
    sub: texts[1] ? leaf(texts[1]) : null,
  });
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="refuf103"
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
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$UF_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="cloneuf103"
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
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$UF_JS" 2>/dev/null | tail -1
EOF
echo "=== userfooter probe v103 done ==="
