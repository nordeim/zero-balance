#!/usr/bin/env bash
# v29: clone-side asset-card dropdown menu class diff (the never-diffed
# net-worth card family part 2): panel + item classes + computed.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-nwmenu-v29.sh
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

echo "=== trigger + open the asset card dropdown ==="
agent-browser eval "JSON.stringify((() => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
  const card = cards[0];
  const r = card.getBoundingClientRect();
  return { x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2) };
})())" 2>/dev/null
agent-browser eval "JSON.stringify((() => {
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
  const r = cards[0].getBoundingClientRect();
  return JSON.stringify({ x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2) });
})()" >/dev/null 2>&1
# hover card to reveal trigger, then click it via ref
agent-browser mouse move 443 746 >/dev/null 2>&1
sleep 0.6
TRIG=$(agent-browser snapshot -i 2>/dev/null | grep -oE 'button "Actions for [^"]+" \[expanded=false, ref=(e[0-9]+)\]' | grep -oE 'e[0-9]+' | head -1)
echo "trigger ref: $TRIG"
agent-browser click "@$TRIG" >/dev/null 2>&1
sleep 0.9
agent-browser eval "JSON.stringify((() => {
  const menu = document.querySelector('[role=menu]');
  if (!menu) return { error: 'no menu' };
  const cs = getComputedStyle(menu);
  const item = [...menu.querySelectorAll('[role=menuitem]')][0];
  return {
    menuCls: menu.className.slice(0,130),
    menuBg: cs.backgroundColor,
    menuBorder: cs.borderWidth + ' ' + cs.borderColor,
    menuShadowFull: cs.boxShadow,
    menuRadius: cs.borderRadius,
    menuMinW: cs.minWidth,
    itemClsFull: item.className,
    itemColor: getComputedStyle(item).color,
    itemH: item.getBoundingClientRect().height,
    delColor: getComputedStyle([...menu.querySelectorAll('[role=menuitem]')][1]).color
  };
})())" 2>/dev/null
agent-browser press Escape >/dev/null 2>&1
