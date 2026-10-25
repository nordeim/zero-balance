#!/usr/bin/env bash
# nwheader-mechanism-v118.sh — the DRILL-DOWN census for the v118 page-header
# find: the /networth header row's mb axis reads 0px on the reference vs
# 32px on the clone, yet the VISUAL row-to-card gap is 32px on BOTH sides
# (the nwheader-arbit-v118.sh census). Something else on the reference
# creates its 32px. This census measures the mechanism on BOTH sides: the
# summary card's own margin-top, the header row's parent's display/gap, and
# every margin between the row's bottom and the card's top.
# READ-ONLY (login + passive navigation only).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

MECH_JS="(async () => {
  const out = { view: 'nw-mech-1280-v118', docSW: document.documentElement.scrollWidth };
  const h1 = [...document.querySelectorAll('main h1')].find(h => (h.textContent || '').trim() === 'Net Worth');
  if (!h1) return JSON.stringify({ h1: 'not found' });
  const block = h1.parentElement;
  const row = block && block.parentElement;
  if (!row) return JSON.stringify({ row: 'not found' });
  out.rowTag = row.tagName;
  out.rowClass = (typeof row.className === 'string' ? row.className : '').slice(0, 120);
  const rcs = getComputedStyle(row);
  out.rowMargin = { top: rcs.marginTop, bottom: rcs.marginBottom };
  out.rowRect = { top: Math.round(row.getBoundingClientRect().top), bottom: Math.round(row.getBoundingClientRect().bottom) };
  // the parent chain: main + the wrapper between main and the row
  const main = row.closest('main');
  let p = row.parentElement;
  out.parents = [];
  while (p && p !== main) {
    const pcs = getComputedStyle(p);
    out.parents.push({
      tag: p.tagName,
      cls: (typeof p.className === 'string' ? p.className : '').slice(0, 80),
      display: pcs.display,
      gap: pcs.gap,
      mt: pcs.marginTop,
      mb: pcs.marginBottom,
      pt: pcs.paddingTop,
      pb: pcs.paddingBottom,
    });
    p = p.parentElement;
  }
  if (main) {
    const mcs = getComputedStyle(main);
    out.main = { display: mcs.display, gap: mcs.gap, pt: mcs.paddingTop, mt: mcs.marginTop, pb: mcs.paddingBottom };
  }
  // the summary card: its own margins + the FIRST element after the header row
  const label = [...document.querySelectorAll('p, span, h2, div')].find(e => (e.textContent || '').trim() === 'Total Net Worth' && e.children.length === 0);
  if (label) {
    let card = label;
    while (card && card !== document.body) {
      const c = getComputedStyle(card);
      if (parseFloat(c.borderRadius) > 12 && card.getBoundingClientRect().width > 500) break;
      card = card.parentElement;
    }
    if (card && card !== document.body) {
      const ccs = getComputedStyle(card);
      out.card = {
        mt: ccs.marginTop,
        mb: ccs.marginBottom,
        top: Math.round(card.getBoundingClientRect().top),
        prevSiblingTag: card.previousElementSibling ? card.previousElementSibling.tagName : null,
        prevSiblingCls: card.previousElementSibling && typeof card.previousElementSibling.className === 'string' ? card.previousElementSibling.className.slice(0, 80) : null,
        prevSiblingMb: card.previousElementSibling ? getComputedStyle(card.previousElementSibling).marginBottom : null,
        parentTag: card.parentElement ? card.parentElement.tagName : null,
        parentDisplay: card.parentElement ? getComputedStyle(card.parentElement).display : null,
        parentGap: card.parentElement ? getComputedStyle(card.parentElement).gap : null,
      };
    }
  }
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

echo "=== REFERENCE side (1280, /networth — the spacing mechanism) ==="
export AGENT_BROWSER_SESSION="refnwmech118"
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
echo "--- mechanism census:"
agent-browser eval "$MECH_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /networth — the spacing mechanism) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonenwmech118"
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
echo "--- mechanism census:"
agent-browser eval "$MECH_JS" 2>/dev/null | tail -1
EOF
echo "=== mechanism census v118 done ==="
