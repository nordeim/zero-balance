#!/usr/bin/env bash
# tile-interior-arbit-v90.sh — the supplemental one-shot both-sides census
# for the v90 pin's own axes (the v87/v88/v89 precedent: the pin's axes
# first measured byte-identical on BOTH sides BEFORE the pin is written).
# The v90 pin target: the net-worth summary card's STAT-TILE INTERIOR
# family at mobile 390 — per tile {the label P {fs/color/mb} + the value P
# {fs/fw/color}} — the v63 F3 pin holds the tile BOX chrome only; the
# interiors are never pinned at ANY viewport (grep-verified).
# READ-ONLY on the reference (the v46 rule). The census JS identical on
# both sides (the two-half controlled form, the v89 lesson).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

TILE_JS="(async () => {
  const label = [...document.querySelectorAll('p, span, h2, div')].find(
    (e) => (e.textContent || '').trim() === 'Total Net Worth' && e.children.length === 0
  );
  if (!label) return 'no Total Net Worth label';
  const card = label.closest('div.rounded-2xl');
  if (!card) return 'no card';
  const assetsLabel = [...card.querySelectorAll('p, span')].find(
    (e) => (e.textContent || '').trim() === 'Total Assets'
  );
  if (!assetsLabel) return 'no Total Assets label';
  const grid = assetsLabel.closest('[class*=\"grid\"]');
  if (!grid) return 'no grid';
  const tiles = [...grid.children].map(c => {
    const ps = [...c.querySelectorAll('p')];
    const r = c.getBoundingClientRect();
    const lcs = ps[0] ? getComputedStyle(ps[0]) : null;
    const vcs = ps[1] ? getComputedStyle(ps[1]) : null;
    const lr = ps[0] ? ps[0].getBoundingClientRect() : null;
    return {
      tile: { w: Math.round(r.width), h: Math.round(r.height) },
      label: lcs ? { tag: ps[0].tagName, text: (ps[0].textContent || '').slice(0, 20), fs: lcs.fontSize, color: lcs.color, mb: lcs.marginBottom, h: lr ? Math.round(lr.height) : null } : null,
      value: vcs ? { tag: ps[1].tagName, fs: vcs.fontSize, fw: vcs.fontWeight, color: vcs.color } : null
    };
  });
  return JSON.stringify({
    docSW: document.documentElement.scrollWidth,
    gridCols: getComputedStyle(grid).gridTemplateColumns,
    tiles: tiles
  });
})()"

echo "=== REFERENCE side (390): the stat-tile interiors ==="
export AGENT_BROWSER_SESSION="reftar90"
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
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$TILE_JS" 2>/dev/null | tail -1

echo "=== CLONE side (390): the stat-tile interiors ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonetar90"
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
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$TILE_JS" 2>/dev/null | tail -1
EOF
echo "=== tile-interior arbit v90 done ==="
