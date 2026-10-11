#!/usr/bin/env bash
# v46: reference-side driver — the NET-WORTH CARD census at 1280 (the
# queue's first surface: the 2-col grid, the card chrome, the REAL-hover
# inert pin, the kebab reveal) and the CONFIRM-BAR white-pill census (the
# queue's third surface: the five-site pill family's shadow-sm visible
# layer). Read-only discipline: the confirm bar's DELETE is never clicked
# (the driver clicks Cancel — the card survives by construction).
set -u
BASE="https://zero-balance-4885a8f3.base44.app"
PB=/home/z/my-project/zero-balance/scripts/parity-probes
export AGENT_BROWSER_SESSION="ref46"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
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

echo "=== REF net-worth card census at 1280 (Assets tab) ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref46 "$PB/nw-card-v46.mjs" 2>/dev/null | tail -1

echo ""
echo "--- real hover (asset card: shadow + kebab reveal) ---"
agent-browser hover '[data-v46-card="first"]' >/dev/null 2>&1
sleep 1
agent-browser eval "(async () => {
  const c = document.querySelector('[data-v46-card=\"first\"]');
  const kb = document.querySelector('[data-v46-kebab=\"first\"]');
  return JSON.stringify({ boxShadow: getComputedStyle(c).boxShadow, kebabOpacity: kb ? getComputedStyle(kb).opacity : null, translateY: getComputedStyle(c).translate });
})()" 2>/dev/null | tail -1

echo ""
echo "=== REF confirm-bar white-pill census (kebab → Delete → bar) ==="
# The JS click opens the menu (synthetic clicks fire handlers; only CSS
# :hover needs a REAL pointer — the v45 lesson).
agent-browser eval "(async () => {
  const kb = document.querySelector('[data-v46-kebab=\"first\"]');
  if (!kb) return 'no kebab';
  kb.click();
  return 'menu opening';
})()" 2>/dev/null | tail -1
sleep 1
# The menu's Delete item (role=menuitem or a plain div/button with text).
agent-browser eval "(async () => {
  const items = [...document.querySelectorAll('[role=menuitem], [role=menu] *')].filter((el) => (el.textContent || '').trim() === 'Delete' && el.closest('[role=menu], [data-state=open]'));
  const plain = [...document.querySelectorAll('button, div')].filter((el) => (el.textContent || '').trim() === 'Delete' && !el.closest('[data-v46-card]') && getComputedStyle(el).position !== 'fixed');
  const target = items[0] || plain[0];
  if (!target) return 'no Delete item — menu state?';
  target.click();
  return 'delete clicked';
})()" 2>/dev/null | tail -1
sleep 1
bash "$PB/run-probe.sh" ref46 "$PB/confirm-pill-v46.mjs" 2>/dev/null | tail -1

echo ""
echo "--- restore: click the bar's Cancel ---"
agent-browser eval "(async () => {
  const cancel = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === 'Cancel');
  if (cancel) { cancel.click(); return 'cancelled'; }
  return 'no Cancel button';
})()" 2>/dev/null | tail -1
sleep 1

echo ""
echo "=== REF data census (read-only check, before/after identical) ==="
agent-browser open "$BASE/" >/dev/null 2>&1
sleep 3
bash "$PB/run-probe.sh" ref46 "$PB/census-v35.mjs" 2>/dev/null | tail -1
