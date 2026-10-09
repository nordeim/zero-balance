#!/usr/bin/env bash
# v28: clone-side card-click verification — does clicking an item card open
# anything on the clone? (the reference opens the Budget Item Details dialog)
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-cardclick-v28.sh
set -u
BASE="http://localhost:3200"

agent-browser open "$BASE/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  const set = (el, v) => {
    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
    setter.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" >/dev/null 2>&1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter((c) => c.querySelector('h4'));
  if (!cards.length) return JSON.stringify({ error: 'no cards' });
  const before = document.body.innerText.length;
  cards[0].click();
  await sleep(900);
  // any fixed overlay or dialog opened?
  const overlays = [...document.querySelectorAll('div')].filter((d) => {
    const cs = getComputedStyle(d);
    return (cs.position === 'fixed' || d.getAttribute('role') === 'dialog') && cs.zIndex !== 'auto' && cs.display !== 'none' && d.getBoundingClientRect().height > 100;
  }).map((d) => ({ z: getComputedStyle(d).zIndex, txt: (d.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 50) }));
  return JSON.stringify({ clicked: cards[0].querySelector('h4').textContent.trim(), overlays, textChanged: document.body.innerText.length !== before }, null, 1);
})()" 2>/dev/null
