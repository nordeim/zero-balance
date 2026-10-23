#!/usr/bin/env bash
# nw-facts-arbit-v106.sh — the ONE-SHOT both-sides probe of the networth
# ASSET CARD's FACTS-ROW interior family (never census'd: the v46 F2 pin
# holds the facts WRAPPER's {font, color} + the value→facts mb-4 gap ONLY;
# the per-row flex chrome, the 12×12 icon family, the row heights, and the
# space-y-2 vertical rhythm were never pinned at ANY viewport in ANY spec).
# Run on BOTH sides to verify the family is byte-identical before the pin.
# READ-ONLY: login + passive navigation only (the v46 rule). The parked
# pointer at (5,5). No literal dollar sequences in the census JS (the v64
# rule). Double-quoted-heredoc-safe.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

FACTS_JS="(async () => {
  // The first ASSET-LIABILITY card: an h4-titled card inside the tab
  // panels carrying a 24px/700 value — NOT the summary card (rounded-2xl,
  // no h4) and NOT the section rows.
  const cards = [...document.querySelectorAll('div')].filter((d) => {
    if (typeof d.className !== 'string') return false;
    if (!d.className.includes('rounded-xl')) return false;
    const h4 = d.querySelector('h4');
    const val = [...d.querySelectorAll('p')].find((p) => {
      const pcs = getComputedStyle(p);
      return pcs.fontSize === '24px' && pcs.fontWeight === '700';
    });
    return !!h4 && !!val;
  });
  if (!cards.length) return JSON.stringify({ err: 'no cards' });
  const card = cards[0];
  const h4 = card.querySelector('h4');
  // The facts wrapper: the deepest div containing an Updated text row,
  // font-size 12px, color gray.
  const updated = [...card.querySelectorAll('div')].find((e) => {
    const t = (e.textContent || '').trim();
    return t.startsWith('Updated') && e.querySelector('svg') && getComputedStyle(e).fontSize === '12px';
  });
  if (!updated) return JSON.stringify({ err: 'no Updated row' });
  const wrapper = updated.parentElement;
  if (!wrapper || wrapper === card) return JSON.stringify({ err: 'no facts wrapper' });
  const wcs = getComputedStyle(wrapper);
  const rows = [...wrapper.children].filter((c) => c.tagName === 'DIV');
  const rowCensus = rows.map((row) => {
    const rcs = getComputedStyle(row);
    const svg = row.querySelector('svg');
    const src = svg ? svg.getBoundingClientRect() : null;
    const scs = svg ? getComputedStyle(svg) : null;
    return {
      display: rcs.display, align: rcs.alignItems, gap: rcs.gap,
      h: Math.round(row.getBoundingClientRect().height),
      mt: rcs.marginBlockStart,
      text: (row.textContent || '').trim().slice(0, 28),
      iconW: src ? Math.round(src.width) : null,
      iconH: src ? Math.round(src.height) : null,
      iconColor: scs ? scs.color : null,
      iconViewBox: svg ? svg.getAttribute('viewBox') : null,
    };
  });
  return JSON.stringify({
    cardTitle: (h4 ? h4.textContent : '').trim().slice(0, 24),
    wrapper: {
      display: wcs.display, fs: wcs.fontSize, color: wcs.color,
      gap: wcs.gap, h: Math.round(wrapper.getBoundingClientRect().height),
      rowCount: rows.length,
    },
    rows: rowCensus,
    sw: document.documentElement.scrollWidth,
  });
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="refnwfacts106"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$FACTS_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280) ==="
cd "$(dirname "$0")/../.."
FACTS_JS="$FACTS_JS" bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonenwfacts106"
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
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "\$FACTS_JS" 2>/dev/null | tail -1
EOF
echo "=== nw-facts probe v106 done ==="
