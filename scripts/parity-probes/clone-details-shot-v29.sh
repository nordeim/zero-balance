#!/usr/bin/env bash
# v29: capture the clone's item-details sheet screenshot for the VLM pair.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-details-shot-v29.sh
set -u
BASE="http://localhost:3200"
OUT="${1:-/tmp/vlm29/clone-item-details.png}"

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
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  // open the RENT card's details (matches the reference capture's shape: a
  // recurring monthly expense)
  const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
  const card = cards.find(c => /Rent/i.test(c.textContent)) || cards[0];
  card.click();
  await new Promise(r => setTimeout(r, 1100));
  return JSON.stringify({ opened: !!document.querySelector('[role=dialog]') });
})()" 2>/dev/null
agent-browser screenshot "$OUT" 2>&1 | head -1
