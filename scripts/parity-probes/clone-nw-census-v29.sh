#!/usr/bin/env bash
# v29: clone-side net-worth census — asset card label classes + computed,
# tab triggers, card cursor. Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-nw-census-v29.sh
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

echo "=== net-worth tab triggers + tablist ==="
agent-browser eval "JSON.stringify((() => {
  const tab = document.querySelector('button[role=tab][aria-selected=true]');
  const tablist = document.querySelector('[role=tablist]');
  return {
    tabCls: tab ? tab.className : null,
    tabColor: tab ? getComputedStyle(tab).color : null,
    tabBg: tab ? getComputedStyle(tab).backgroundColor : null,
    tablistCls: tablist ? tablist.className : null,
    tablistBg: tablist ? getComputedStyle(tablist).backgroundColor : null,
    tablistW: tablist ? Math.round(tablist.getBoundingClientRect().width) : null
  };
})())" 2>/dev/null

echo "=== asset card + label (clone) ==="
agent-browser eval "JSON.stringify((() => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
  const card = cards.find(c => /Emergency|Vehicle|Retirement|Savings/i.test(c.textContent)) || cards[0];
  if (!card) return { error: 'no cards' };
  const label = [...card.querySelectorAll('span,div')].filter(e => { const t = (e.textContent||'').trim(); return t && t.length < 25 && e.children.length === 0 && !/^\$/.test(t); })[0];
  const r = label.getBoundingClientRect();
  return {
    card: card.querySelector('h4').textContent.trim(),
    cardCls: card.className,
    cardCursor: getComputedStyle(card).cursor,
    label: label ? { tag: label.tagName, txt: label.textContent.trim(), cls: label.className, bg: getComputedStyle(label).backgroundColor, color: getComputedStyle(label).color } : null,
    labelPos: { x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2) }
  };
})())" 2>/dev/null
