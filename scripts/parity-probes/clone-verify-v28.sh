#!/usr/bin/env bash
# v28: live re-verification of the three fixes on the :3200 parity server —
# the details sheet (card click + mobile bottom-sheet geometry), the badge
# hover tint (REAL CDP hover), and the Edit button's real-Tab focus ring.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-verify-v28.sh
set -u
BASE="http://localhost:3200"

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

echo "=== 1. card click opens the details sheet (desktop) ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter((c) => c.querySelector('h4'));
  cards[0].querySelector('h4').click();
  await sleep(700);
  const dlg = document.querySelector('[role=dialog]');
  if (!dlg) return JSON.stringify({ open: false });
  const cs = getComputedStyle(dlg);
  const r = dlg.getBoundingClientRect();
  const hdr = dlg.querySelector('div.sticky');
  return JSON.stringify({
    open: true,
    title: (hdr.querySelector('h2') || {}).textContent,
    panel: { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), maxW: cs.maxWidth, radius: cs.borderRadius },
    text: dlg.innerText.replace(/\s+/g, ' | ').slice(0, 220),
  }, null, 1);
})()" 2>/dev/null

echo "=== 2. mobile bottom-sheet geometry (390x844) ==="
agent-browser eval "(async () => { const x = [...document.querySelectorAll('[role=dialog] button')].find((b) => b.getBoundingClientRect().width === 36); if (x) x.click(); return 'closed'; })()" 2>/dev/null
sleep 1
agent-browser set viewport 390 844 >/dev/null 2>&1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter((c) => c.querySelector('h4'));
  cards[0].querySelector('h4').click();
  await sleep(700);
  const dlg = document.querySelector('[role=dialog]');
  if (!dlg) return JSON.stringify({ open: false });
  const r = dlg.getBoundingClientRect();
  const cs = getComputedStyle(dlg);
  return JSON.stringify({ open: true, x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), bottom: Math.round(r.bottom), viewportH: innerHeight, radius: cs.borderRadius });
})()" 2>/dev/null

echo "=== 3. badge hover tint (REAL CDP hover) ==="
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
XY=$(agent-browser eval "(() => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter((c) => c.querySelector('h4'));
  const card = cards[0];
  const status = [...card.querySelectorAll('span')].find((e) => /^active\$/.test((e.textContent || '').trim()));
  status.scrollIntoView({ block: 'center' });
  const r = status.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + ' ' + Math.round(r.y + r.height / 2);
})()" 2>/dev/null | tr -d '"')
agent-browser mouse move $XY >/dev/null 2>&1
sleep 0.7
agent-browser eval "(() => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter((c) => c.querySelector('h4'));
  const status = [...cards[0].querySelectorAll('span')].find((e) => /^active\$/.test((e.textContent || '').trim()));
  const cs = getComputedStyle(status);
  return JSON.stringify({ matchesHover: status.matches(':hover'), bg: cs.backgroundColor, transition: cs.transitionDuration });
})()" 2>/dev/null

echo "=== 4. Edit button real-Tab focus ring ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
for i in $(seq 1 11); do
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.35
done
agent-browser eval "(() => {
  const el = document.activeElement;
  const cs = getComputedStyle(el);
  return JSON.stringify({ txt: (el.textContent || '').trim(), cls: (el.className || '').toString().slice(0, 160), boxShadow: cs.boxShadow, outline: cs.outlineStyle + ' ' + cs.outlineWidth, fv: el.matches(':focus-visible') });
})()" 2>/dev/null
