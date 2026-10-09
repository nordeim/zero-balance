#!/usr/bin/env bash
# v29: measure the X close button's computed chrome in the open details
# dialog on the CLONE (border/shadow/outline), right after open (initial
# focus state) — to verify the VLM's "visible border" claim.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-xchrome-v29.sh
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
agent-browser open "$BASE/expenses" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  try {
    const cards = [...document.querySelectorAll('main div.rounded-xl')].filter(c => c.querySelector('h4'));
    const card = cards.find(c => /Rent/i.test(c.textContent)) || cards[0];
    card.click();
    await new Promise(r => setTimeout(r, 1100));
    const dlg = document.querySelector('[role=dialog]');
    if (!dlg) return JSON.stringify({ error: 'no dialog' });
    const x = [...dlg.querySelectorAll('button')].find(b => /close/i.test((b.textContent || '') + (b.getAttribute('aria-label') || '')));
    if (!x) return JSON.stringify({ error: 'no X button', btns: [...dlg.querySelectorAll('button')].map(b => b.getAttribute('aria-label')) });
    const cs = getComputedStyle(x);
    return JSON.stringify({
      focused: document.activeElement === x,
      matchesFocusVisible: x.matches(':focus-visible'),
      border: cs.borderWidth + ' ' + cs.borderStyle + ' ' + cs.borderColor,
      boxShadow: cs.boxShadow,
      outline: cs.outlineWidth + ' ' + cs.outlineStyle + ' ' + cs.outlineColor,
      bg: cs.backgroundColor,
      w: x.getBoundingClientRect().width, h: x.getBoundingClientRect().height
    });
  } catch (e) { return JSON.stringify({ error: String(e) }); }
})()" 2>/dev/null
