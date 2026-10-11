#!/usr/bin/env bash
# v46: clone-side driver — the NET-WORTH CARD census at 1280 (the grid,
# the card chrome, the REAL-hover inert + kebab reveal) and the
# CONFIRM-BAR white-pill census (the clone's superset chrome — the
# reference's deletes are direct, no confirm bars, the v18-documented
# superset-fix-#6 family; the pin is a clone-only regression net).
# Runs INSIDE with-server.sh (the :3200 parity server).
set -u
BASE="http://localhost:3200"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="clone46"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 3

echo "=== CLONE net-worth card census at 1280 (Assets tab) ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" clone46 "$PB/nw-card-v46.mjs" 2>/dev/null | tail -1

echo ""
echo "--- value wrap + badge detail (the mb-4 vs mb-2 candidate) ---"
agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find((d) => {
    if (!d.className || typeof d.className !== 'string') return false;
    return d.className.includes('lg:grid-cols-3') && d.children.length >= 1;
  });
  const card = grid.children[0];
  const valueP = [...card.querySelectorAll('p')].find((p) => (p.textContent || '').includes('\$'));
  const badge = [...card.querySelectorAll('span')].find((s) => (s.textContent || '').trim().length > 3 && s.closest('.flex-1'));
  const bcs = badge ? getComputedStyle(badge) : null;
  return JSON.stringify({
    valueP: valueP ? { mb: getComputedStyle(valueP).marginBottom, wrapCls: (typeof valueP.parentElement.className === 'string' ? valueP.parentElement.className : '').slice(0, 40), wrapMb: getComputedStyle(valueP.parentElement).marginBottom, lh: getComputedStyle(valueP).lineHeight } : 'none',
    badge: bcs ? { bg: bcs.backgroundColor, pad: bcs.padding, radius: bcs.borderRadius, font: bcs.fontSize, weight: bcs.fontWeight, color: bcs.color, h: Math.round(badge.getBoundingClientRect().height), border: bcs.borderTopWidth + ' ' + bcs.borderTopColor } : 'none',
  });
})()" 2>/dev/null | tail -1

echo ""
echo "--- real hover (clone asset card: shadow + kebab reveal) ---"
agent-browser eval "(async () => {
  const grid = [...document.querySelectorAll('div')].find((d) => {
    if (!d.className || typeof d.className !== 'string') return false;
    return d.className.includes('lg:grid-cols-3') && d.children.length >= 1;
  });
  const card = grid.children[0];
  const kb = [...card.querySelectorAll('button')].find((b) => !(b.textContent || '').trim());
  card.setAttribute('data-v46-card', 'first');
  if (kb) kb.setAttribute('data-v46-kebab', 'first');
  return 'tagged';
})()" 2>/dev/null | tail -1
agent-browser hover '[data-v46-card="first"]' >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const c = document.querySelector('[data-v46-card=\"first\"]');
  const kb = document.querySelector('[data-v46-kebab=\"first\"]');
  return JSON.stringify({ boxShadow: getComputedStyle(c).boxShadow, kebabOpacity: kb ? getComputedStyle(kb).opacity : null, translateY: getComputedStyle(c).translate });
})()" 2>/dev/null | tail -1

echo ""
echo "=== CLONE confirm-bar white-pill census (the superset chrome) ==="
agent-browser eval "(async () => {
  const kb = document.querySelector('[data-v46-kebab=\"first\"]');
  if (!kb) return 'no kebab';
  kb.click();
  return 'menu opening';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(async () => {
  const item = [...document.querySelectorAll('[role=menuitem]')].find((i) => (i.textContent || '').trim() === 'Delete');
  if (!item) return 'no Delete item';
  item.click();
  return 'delete clicked — confirm bar should show';
})()" 2>/dev/null | tail -1
sleep 1
bash "$PB/run-probe.sh" clone46 "$PB/confirm-pill-v46.mjs" 2>/dev/null | tail -1

echo ""
echo "--- restore: click the bar's Cancel ---"
agent-browser eval "(async () => {
  const cancel = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === 'Cancel' && b.closest('div[style*=\"254, 242, 242\"]'));
  if (cancel) { cancel.click(); return 'cancelled'; }
  const anyCancel = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === 'Cancel');
  if (anyCancel) { anyCancel.click(); return 'cancelled (any)'; }
  return 'no Cancel button';
})()" 2>/dev/null | tail -1
sleep 1
