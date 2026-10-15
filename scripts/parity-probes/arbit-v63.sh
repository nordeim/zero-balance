#!/usr/bin/env bash
# arbit-v63.sh — the v63 pair's three flags, DOM-arbitrated per the v43 rule:
#   (1) the summary stat tiles side-by-side (ref) vs stacked (clone)
#   (2) the summary card taller (clone)
#   (3) the trend-icon circle "larger/more prominent" (clone)
# Census BOTH sides at 390x844: the summary card, the stat grid, the stat
# tiles, the medallion + trend icon (the v54 clipping-class check), docSW.
# READ-ONLY.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS_JS="(async () => {
  // the summary card: the dark gradient card at the page top (the only
  // card carrying a 135deg linear-gradient background)
  const cards = [...document.querySelectorAll('main div, div')].filter(d => {
    const s = getComputedStyle(d);
    return d.getBoundingClientRect().height > 100 && d.getBoundingClientRect().width > 200
      && s.backgroundImage && s.backgroundImage.includes('linear-gradient');
  });
  const card = cards.find(c => c.getBoundingClientRect().width < 500) || cards[0];
  if (!card) return 'no summary card found';
  const cr = card.getBoundingClientRect();
  // the stat grid: the grid element with 2+ children inside the card
  const grids = [...card.querySelectorAll('div')].filter(d => {
    const s = getComputedStyle(d);
    return s.display.includes('grid') && d.children.length >= 2 && d.getBoundingClientRect().height > 40;
  });
  const grid = grids[0];
  const g = grid ? getComputedStyle(grid) : null;
  const gr = grid ? grid.getBoundingClientRect() : null;
  const tiles = grid ? [...grid.children].map(c => {
    const r = c.getBoundingClientRect();
    return { w: Math.round(r.width), h: Math.round(r.height) };
  }) : [];
  // the medallion: the white/10% translucent circle near the card's top-right
  let med = null;
  for (const d of card.querySelectorAll('div, span')) {
    const s = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    if (r.width >= 40 && r.width <= 90 && Math.abs(r.width - r.height) < 2
      && s.backgroundColor && s.backgroundColor.includes('rgba(255, 255, 255')
      && !s.backgroundColor.includes('rgba(255, 255, 255, 1)')) { med = d; break; }
  }
  const mr = med ? med.getBoundingClientRect() : null;
  const medClip = med ? (mr.right > document.documentElement.clientWidth) : null;
  // the svg icon inside the medallion
  const svg = med ? med.querySelector('svg') : null;
  const sr = svg ? svg.getBoundingClientRect() : null;
  return JSON.stringify({
    docSW: document.documentElement.scrollWidth,
    vw: document.documentElement.clientWidth,
    card: { w: Math.round(cr.width), h: Math.round(cr.height), right: Math.round(cr.right) },
    statGrid: grid ? { cols: g.gridTemplateColumns, gap: g.gap, w: Math.round(gr.width), children: grid.children.length } : null,
    tiles: tiles,
    medallion: med ? { w: Math.round(mr.width), h: Math.round(mr.height), right: Math.round(mr.right), clipsViewport: medClip } : null,
    trendIcon: svg ? { w: Math.round(sr.width), h: Math.round(sr.height) } : null
  });
})()"

echo "=== REFERENCE side (390) ==="
export AGENT_BROWSER_SESSION="refarbit63"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
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
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (390) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbit63"
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
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== arbit v63 done ==="
