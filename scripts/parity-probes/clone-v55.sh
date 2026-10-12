#!/usr/bin/env bash
# clone-v55.sh — the clone-side driver for the v55 surface: the
# GOAL-CARD's ICON GLYPH CENSUS at 390 (the same axes as ref-v55.sh —
# the classification chip's icon glyph + the footer calendar glyph +
# the /expenses same-glyph control census). Runs against the
# production standalone parity server on :3200 via with-server.sh.
set -u
cd "$(dirname "$0")/../.."

bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clone55"
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

echo ""
echo "=== CLONE surface: the SAVINGS GOAL-CARD's ICON GLYPHS at 390 ==="
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const h4 = [...document.querySelectorAll('h4')].find((x) =>
    (x.textContent || '').trim().length > 3);
  if (!h4) return 'no h4';
  let card = h4.closest('div.rounded-xl') || h4.parentElement;
  for (let i = 0; card && i < 5; i++) {
    const pcs = getComputedStyle(card.parentElement);
    if (pcs.display === 'grid') break;
    card = card.parentElement;
  }
  if (!card) return 'no card';
  // v55 refinement: grab EVERY shape child (path/circle/rect/line) — the
  // circle-alert glyph renders its ring as a <circle>, the calendar's box
  // as a <rect>; a path-only census reads 0 paths on circle-alert.
  const shapeDump = (svg) => {
    const shapes = [...svg.querySelectorAll('path,circle,rect,line,polyline,polygon')];
    return shapes.map((s) => {
      const tag = s.tagName.toLowerCase();
      if (tag === 'path') return 'P:' + (s.getAttribute('d') || '').replace(/\\s+/g, ' ');
      if (tag === 'circle') return 'C:' + (s.getAttribute('cx') || '') + ',' + (s.getAttribute('cy') || '') + ',r' + (s.getAttribute('r') || '');
      if (tag === 'rect') return 'R:' + (s.getAttribute('x') || '') + ',' + (s.getAttribute('y') || '') + ',' + (s.getAttribute('width') || '') + 'x' + (s.getAttribute('height') || '') + ',rx' + (s.getAttribute('rx') || '');
      return tag.toUpperCase() + ':' + [s.getAttribute('x1'), s.getAttribute('y1'), s.getAttribute('x2'), s.getAttribute('y2')].join(',');
    });
  };
  const glyphGrab = (svg) => {
    if (!svg) return null;
    const cs = getComputedStyle(svg);
    const r = svg.getBoundingClientRect();
    return {
      cls: (svg.getAttribute('class') || '').slice(0, 40),
      viewBox: svg.getAttribute('viewBox'),
      fill: svg.getAttribute('fill'),
      stroke: svg.getAttribute('stroke'),
      sw: svg.getAttribute('stroke-width'),
      slc: svg.getAttribute('stroke-linecap'),
      slj: svg.getAttribute('stroke-linejoin'),
      shapes: shapeDump(svg),
      w: Math.round(r.width), h: Math.round(r.height),
      color: cs.color, mr: cs.marginRight,
      display: cs.display, flexShrink: cs.flexShrink
    };
  };
  const rows = [...card.querySelectorAll('div')].filter((d) => {
    const cs = getComputedStyle(d);
    return cs.display === 'flex' && cs.flexWrap === 'wrap' &&
      [...d.children].every(c => getComputedStyle(c).display.includes('inline-flex') || getComputedStyle(c).display === 'flex') &&
      d.children.length >= 2;
  });
  const badgeRow = rows[0];
  if (!badgeRow) return 'no badge row';
  const chipIconGrab = (chip) => ({
    text: (chip.textContent || '').trim().slice(0, 14),
    chipColor: getComputedStyle(chip).color,
    icon: glyphGrab(chip.querySelector('svg'))
  });
  const footer = [...card.children].filter((d) => {
    const cs = getComputedStyle(d);
    return cs.display === 'flex' && cs.justifyContent === 'space-between' &&
      !d.querySelector('h4');
  }).pop();
  const dateSpan = footer ? footer.children[0] : null;
  return JSON.stringify({
    clsChips: [...badgeRow.children].map(chipIconGrab),
    dateSpanGlyph: dateSpan ? glyphGrab(dateSpan.querySelector('svg')) : null,
    docSW: document.documentElement.scrollWidth
  });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE control: the /expenses classification-chip glyphs (same-glyph compare) ==="
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  // v55 control: census EVERY card's classification chip on /expenses —
  // matched by classification text (need/want) for the same-glyph compare
  // (the seeds differ; the first cards classify differently).
  const cards = [...document.querySelectorAll('h4')].map((h4) => {
    let card = h4.closest('div.rounded-xl') || h4.parentElement;
    for (let i = 0; card && i < 5; i++) {
      const pcs = getComputedStyle(card.parentElement);
      if (pcs.display === 'grid') break;
      card = card.parentElement;
    }
    return card;
  }).filter(Boolean);
  const shapeDump = (svg) => {
    const shapes = [...svg.querySelectorAll('path,circle,rect,line,polyline,polygon')];
    return shapes.map((s) => {
      const tag = s.tagName.toLowerCase();
      if (tag === 'path') return 'P:' + (s.getAttribute('d') || '').replace(/\\s+/g, ' ');
      if (tag === 'circle') return 'C:' + (s.getAttribute('cx') || '') + ',' + (s.getAttribute('cy') || '') + ',r' + (s.getAttribute('r') || '');
      if (tag === 'rect') return 'R:' + (s.getAttribute('x') || '') + ',' + (s.getAttribute('y') || '') + ',' + (s.getAttribute('width') || '') + 'x' + (s.getAttribute('height') || '') + ',rx' + (s.getAttribute('rx') || '');
      return tag.toUpperCase() + ':' + [s.getAttribute('x1'), s.getAttribute('y1'), s.getAttribute('x2'), s.getAttribute('y2')].join(',');
    });
  };
  const out = [];
  for (const card of cards) {
    const rows = [...card.querySelectorAll('div')].filter((d) => {
      const cs = getComputedStyle(d);
      return cs.display === 'flex' && cs.flexWrap === 'wrap' &&
        [...d.children].every(c => getComputedStyle(c).display.includes('inline-flex') || getComputedStyle(c).display === 'flex') &&
        d.children.length >= 2;
    });
    const badgeRow = rows[0];
    if (!badgeRow) continue;
    const clsChip = [...badgeRow.children].find((c) =>
      ['need', 'want', 'savings'].includes((c.textContent || '').trim()));
    if (!clsChip) continue;
    const svg = clsChip.querySelector('svg');
    out.push({
      h4: (card.querySelector('h4')?.textContent || '').trim().slice(0, 18),
      cls: (clsChip.textContent || '').trim(),
      color: getComputedStyle(clsChip).color,
      icon: svg ? {
        cls: (svg.getAttribute('class') || '').slice(0, 40),
        viewBox: svg.getAttribute('viewBox'),
        sw: svg.getAttribute('stroke-width'),
        shapes: shapeDump(svg),
        w: Math.round(svg.getBoundingClientRect().width),
        color: getComputedStyle(svg).color,
        mr: getComputedStyle(svg).marginRight
      } : null
    });
  }
  return JSON.stringify({ nCards: cards.length, clsChips: out });
})()" 2>/dev/null | tail -1
EOF
echo ""
echo "=== clone-v55 done ==="
