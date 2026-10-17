#!/usr/bin/env bash
# arbit-v78.sh — the v78 re-run pairs' both-sides DOM census (the v75
# convention: the census runs REGARDLESS of the VLM verdict — it documents
# the drift state and measures the pin's axes). The v69 census axes,
# re-measured on BOTH sides at mobile 390:
#   NETWORTH (the v63-era classes, re-confirmed live by the v69 re-run):
#     the summary card + stat grid + tiles + medallion + trend icon.
#   DASHBOARD (the v62-era twin's surfaces):
#     the subtitle wrap (the Range-walk line bucketing) + the breakdown
#     card + the Spending Breakdown donut card (the recharts-wrapper /
#     pie-sector counts that disprove any invented-chart claim).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no attribute-value selectors (geometry + text-content filters only).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

NW_CENSUS="(async () => {
  const cards = [...document.querySelectorAll('main div, div')].filter(d => {
    const s = getComputedStyle(d);
    return d.getBoundingClientRect().height > 100 && d.getBoundingClientRect().width > 200
      && s.backgroundImage && s.backgroundImage.includes('linear-gradient');
  });
  const card = cards.find(c => c.getBoundingClientRect().width < 500) || cards[0];
  if (!card) return 'no summary card found';
  const cr = card.getBoundingClientRect();
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

DASH_CENSUS="(async () => {
  const out = { docSW: document.documentElement.scrollWidth, vw: document.documentElement.clientWidth };
  // --- the subtitle (the h1 'Budget Dashboard' block's P) ---
  const h1 = [...document.querySelectorAll('h1')].find(h => (h.textContent || '').includes('Budget Dashboard'));
  if (h1) {
    const block = h1.parentElement;
    const p = block ? [...block.children].find(c => c.tagName === 'P') : null;
    if (p) {
      const pr = p.getBoundingClientRect();
      const ps = getComputedStyle(p);
      const tn = p.firstChild && p.firstChild.nodeType === 3 ? p.firstChild : null;
      let lines = null;
      if (tn) {
        const text = p.textContent;
        const range = document.createRange();
        const wordsArr = text.split(' ').filter(Boolean);
        const lineMap = [];
        let consumed = 0;
        for (const w of wordsArr) {
          const start = text.indexOf(w, consumed);
          range.setStart(tn, start); range.setEnd(tn, start + w.length);
          const r = range.getClientRects()[0] || range.getBoundingClientRect();
          const top = Math.round(r.top);
          const bucket = lineMap.find(b => Math.abs(b.top - top) <= 2);
          if (bucket) bucket.words.push(w); else lineMap.push({ top: top, words: [w] });
          consumed = start + w.length;
        }
        lines = lineMap.map(b => ({ top: b.top, text: b.words.join(' ') }));
      }
      out.subtitle = {
        text: (p.textContent || '').slice(0, 70),
        rect: { w: Math.round(pr.width), h: Math.round(pr.height), top: Math.round(pr.top) },
        computed: { fs: ps.fontSize, fw: ps.fontWeight, color: ps.color, lh: ps.lineHeight },
        blockH: block ? Math.round(block.getBoundingClientRect().height) : null,
        blockW: block ? Math.round(block.getBoundingClientRect().width) : null,
        lines: lines
      };
    } else { out.subtitle = 'no P in h1 block'; }
  } else { out.subtitle = 'no h1'; }
  // --- the Net Zero Breakdown card ---
  const bd = [...document.querySelectorAll('h1,h2,h3,h4')].find(e => (e.textContent || '').trim() === 'Net Zero Breakdown');
  if (bd) {
    let card = bd;
    for (let i = 0; i < 6; i++) {
      card = card.parentElement; if (!card) break;
      const s = getComputedStyle(card);
      if ((s.borderRadius && s.borderRadius !== '0px') || s.backgroundColor === 'rgb(255, 255, 255)') break;
    }
    if (card) {
      const cr = card.getBoundingClientRect();
      const svgs = [...card.querySelectorAll('svg')].map(s => {
        const r = s.getBoundingClientRect();
        return { w: Math.round(r.width), h: Math.round(r.height) };
      });
      out.breakdownCard = {
        rect: { w: Math.round(cr.width), h: Math.round(cr.height) },
        svgCount: svgs.length, svgs: svgs.slice(0, 4),
        rechartsWrappers: card.querySelectorAll('.recharts-wrapper').length,
        pieSectors: card.querySelectorAll('.recharts-pie-sector').length,
        children: [...card.children].map(c => {
          const r = c.getBoundingClientRect();
          return { tag: c.tagName, w: Math.round(r.width), h: Math.round(r.height) };
        }).slice(0, 6)
      };
    }
  } else { out.breakdownCard = 'no Net Zero Breakdown heading'; }
  // --- the Spending Breakdown donut card ---
  const sb = [...document.querySelectorAll('h1,h2,h3,h4')].find(e => (e.textContent || '').includes('Spending Breakdown'));
  if (sb) {
    let card2 = sb;
    for (let i = 0; i < 6; i++) {
      card2 = card2.parentElement; if (!card2) break;
      const s = getComputedStyle(card2);
      if ((s.borderRadius && s.borderRadius !== '0px') || s.backgroundColor === 'rgb(255, 255, 255)') break;
    }
    if (card2) {
      const cr2 = card2.getBoundingClientRect();
      out.spendingCard = {
        rect: { w: Math.round(cr2.width), h: Math.round(cr2.height) },
        svgCount: card2.querySelectorAll('svg').length,
        pieSectors: card2.querySelectorAll('.recharts-pie-sector').length,
        rechartsWrappers: card2.querySelectorAll('.recharts-wrapper').length
      };
    }
  } else { out.spendingCard = 'no Spending Breakdown heading'; }
  return JSON.stringify(out);
})()"

echo "=== REFERENCE side (390): networth ==="
export AGENT_BROWSER_SESSION="refarbit78"
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
agent-browser eval "$NW_CENSUS" 2>/dev/null | tail -1

echo "=== REFERENCE side (390): dashboard ==="
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$DASH_CENSUS" 2>/dev/null | tail -1

echo "=== CLONE side (390): networth + dashboard ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonearbit78"
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
EOF
echo "=== arbit v78 done ==="
