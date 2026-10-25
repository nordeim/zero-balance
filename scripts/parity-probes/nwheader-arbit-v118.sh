#!/usr/bin/env bash
# nwheader-arbit-v118.sh — the ONE-SHOT both-sides DOM census for the v118
# pin candidate: the /NETWORTH PAGE-HEADER ROW at desktop 1280x800 (the
# gradient icon chip + the "Net Worth" h1 + the subtitle block — the
# element family every 1280 networth census walked past: the v60 view
# census jumps straight to the summary card's label; the v67/v82 the card
# interior; the v94 the GROUP headers; the v100 the tablist junction; the
# v106 the asset cards — the PAGE header row is pinned ONLY at 390 [the
# v69 F3 pin, measured on the CLONE only]; the v14 G3 test pins the chip's
# existence + gradient + x-positions; the family's computed chrome at 1280
# is never pinned in ANY spec).
# READ-ONLY (login + passive navigation only). The census JS is defined
# ONCE and eval'd on BOTH sides (byte-identical by construction).
# Double-quoted-heredoc-safe: no dollar sequences in the census JS; no
# backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

HEADER_JS="(async () => {
  const out = { view: 'nw-header-1280-v118', docSW: document.documentElement.scrollWidth, vw: window.innerWidth };
  // the h1: the page's own heading, found structurally (text match)
  const h1 = [...document.querySelectorAll('main h1')].find(h => (h.textContent || '').trim() === 'Net Worth');
  if (!h1) return JSON.stringify({ h1: 'not found' });
  const block = h1.parentElement;
  const row = block && block.parentElement;
  if (!row) return JSON.stringify({ row: 'not found' });
  const rcs = getComputedStyle(row);
  const rr = row.getBoundingClientRect();
  out.row = {
    display: rcs.display,
    alignItems: rcs.alignItems,
    gap: rcs.gap,
    mb: rcs.marginBottom,
    h: Math.round(rr.height),
  };
  // the chip: the row child that is NOT the text block — carries an svg
  const chip = [...row.children].find(c => c !== block && c.querySelector('svg'));
  if (chip) {
    const cs = getComputedStyle(chip);
    const cr = chip.getBoundingClientRect();
    const svg = chip.querySelector('svg');
    const sr = svg ? svg.getBoundingClientRect() : null;
    out.chip = {
      w: Math.round(cr.width),
      h: Math.round(cr.height),
      radius: cs.borderRadius,
      bgImage: cs.backgroundImage,
      svgW: sr ? Math.round(sr.width) : null,
      svgH: sr ? Math.round(sr.height) : null,
    };
  } else { out.chip = 'not found'; }
  // the h1 chrome
  const hcs = getComputedStyle(h1);
  out.h1 = { fs: hcs.fontSize, fw: hcs.fontWeight, lh: hcs.lineHeight, color: hcs.color, h: Math.round(h1.getBoundingClientRect().height) };
  // the subtitle: the block's non-h1 text child
  const sub = [...block.children].find(c => c !== h1);
  if (sub) {
    const scs = getComputedStyle(sub);
    out.subtitle = { fs: scs.fontSize, fw: scs.fontWeight, lh: scs.lineHeight, color: scs.color, h: Math.round(sub.getBoundingClientRect().height) };
  } else { out.subtitle = 'not found'; }
  // the block: its height is the h1 + subtitle stack (the v65/v69 lesson:
  // the TEXT BLOCK governs the row height, not the 48px chip)
  const br = block.getBoundingClientRect();
  out.block = { h: Math.round(br.height), w: Math.round(br.width) };
  // the row-to-card gap: the summary card found via its label (the v60
  // finder — the rounded-2xl container of 'Total Net Worth')
  const label = [...document.querySelectorAll('p, span, h2, div')].find(e => (e.textContent || '').trim() === 'Total Net Worth' && e.children.length === 0);
  if (label) {
    let card = label;
    while (card && card !== document.body) {
      const c = getComputedStyle(card);
      if (parseFloat(c.borderRadius) > 12 && card.getBoundingClientRect().width > 500) break;
      card = card.parentElement;
    }
    if (card && card !== document.body) {
      const cr = card.getBoundingClientRect();
      out.cardGap = Math.round(cr.top - rr.bottom);
      out.cardW = Math.round(cr.width);
    } else { out.cardGap = 'card not found'; }
  } else { out.cardGap = 'label not found'; }
  return JSON.stringify(out);
})()"

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

echo "=== REFERENCE side (1280, /networth — the page-header family) ==="
export AGENT_BROWSER_SESSION="refnwhead118"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
for attempt in 1 2 3; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- header census:"
agent-browser eval "$HEADER_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /networth — the page-header family) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonenwhead118"
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
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- header census:"
agent-browser eval "$HEADER_JS" 2>/dev/null | tail -1
EOF
echo "=== nwheader arbit v118 done ==="
