#!/usr/bin/env bash
# v29: live re-verification of the G1 label fix — rest computed + REAL CDP
# hover tint on the clone's net-worth asset label.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-verify-v29.sh
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
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 3

echo "=== G1 rest state (expect rgb(243,244,246) / rgb(55,65,81)) ==="
POS=$(agent-browser eval "(() => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
  const label = [...cards[0].querySelectorAll('span')].find(e => { const t = (e.textContent||'').trim(); return t && t.length < 25 && e.children.length === 0; });
  const cs = getComputedStyle(label);
  const r = label.getBoundingClientRect();
  return JSON.stringify({ bg: cs.backgroundColor, color: cs.color, transition: cs.transitionDuration, cls: label.className.slice(0,110), x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2) });
})()" 2>/dev/null | tr -d '"')
echo "$POS"
XY=$(agent-browser eval "(() => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
  const label = [...cards[0].querySelectorAll('span')].find(e => { const t = (e.textContent||'').trim(); return t && t.length < 25 && e.children.length === 0; });
  const r = label.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ' ' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tr -d '"')
X=$(echo "$XY" | cut -d' ' -f1)
Y=$(echo "$XY" | cut -d' ' -f2)

echo "=== G1 REAL hover at $X $Y (expect rgba(245,245,245,0.8)) ==="
agent-browser mouse move "$X" "$Y" >/dev/null 2>&1
sleep 0.7
agent-browser eval "JSON.stringify((() => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
  const label = [...cards[0].querySelectorAll('span')].find(e => { const t = (e.textContent||'').trim(); return t && t.length < 25 && e.children.length === 0; });
  return { bgHover: getComputedStyle(label).backgroundColor, colorHover: getComputedStyle(label).color };
})())" 2>/dev/null

echo "=== liability label rest ==="
agent-browser snapshot -i >/dev/null 2>&1
agent-browser open "$BASE/networth" >/dev/null 2>&1
sleep 2
agent-browser eval "JSON.stringify((() => {
  const tabs = [...document.querySelectorAll('button[role=tab]')];
  const liab = tabs.find(t => /Liabilities/i.test(t.textContent));
  if (liab) liab.click();
  return 'tab';
})()" >/dev/null 2>&1
sleep 1.5
agent-browser eval "JSON.stringify((() => {
  const panel = document.querySelector('[data-state=active][role=tabpanel]');
  if (!panel) return { error: 'no panel' };
  const cards = [...panel.querySelectorAll('div.rounded-xl')].filter(c => c.querySelector('h4'));
  const label = cards[0] ? [...cards[0].querySelectorAll('span')].find(e => { const t = (e.textContent||'').trim(); return t && t.length < 25 && e.children.length === 0; }) : null;
  return label ? { txt: label.textContent.trim(), bg: getComputedStyle(label).backgroundColor, color: getComputedStyle(label).color } : { error: 'no label' };
})())" 2>/dev/null
