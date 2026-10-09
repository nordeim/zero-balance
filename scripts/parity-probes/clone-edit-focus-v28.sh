#!/usr/bin/env bash
# v28: full focus-family read of the clone's card Edit/Calculate buttons —
# complete box-shadow string + outline at real-Tab focus, inside one
# with-server invocation.
# Usage: bash scripts/with-server.sh bash scripts/parity-probes/clone-edit-focus-v28.sh
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
agent-browser mouse move 5 5 >/dev/null 2>&1

# dispatch a keydown Tab walk INSIDE one eval (the v27 discipline) until the
# Edit button is focused, then read its complete computed focus family
agent-browser eval "(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const out = { stops: [] };
  for (let i = 0; i < 14; i++) {
    document.activeElement.dispatchEvent(new KeyboardEvent('keydown', { key: 'Tab', bubbles: true, cancelable: true }));
    await sleep(120);
    const el = document.activeElement;
    if (el && el !== document.body) {
      const txt = (el.textContent || '').trim().slice(0, 12);
      if (txt === 'Edit' || txt === 'Calculate') {
        const cs = getComputedStyle(el);
        out.hit = {
          txt: txt,
          cls: (el.className || '').toString(),
          boxShadow: cs.boxShadow,
          outline: cs.outlineStyle + ' ' + cs.outlineWidth + ' ' + cs.outlineColor + ' offset ' + cs.outlineOffset,
          color: cs.color,
          bg: cs.backgroundColor,
          matchesFocusVisible: el.matches(':focus-visible'),
        };
        break;
      }
    }
  }
  // also read the FIRST Edit at rest (shadow-md ambient layers)
  const edit = [...document.querySelectorAll('button')].find((b) => (b.textContent || '').trim() === 'Edit' && b.getBoundingClientRect().width > 0);
  if (edit) {
    const cs = getComputedStyle(edit);
    out.rest = { boxShadow: cs.boxShadow, outline: cs.outlineStyle + ' ' + cs.outlineWidth + ' ' + cs.outlineColor };
  }
  return JSON.stringify(out, null, 1);
})()" 2>/dev/null
