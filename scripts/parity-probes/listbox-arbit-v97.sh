#!/usr/bin/env bash
# listbox-arbit-v97.sh — the REFERENCE half of the supplemental two-half
# census for the v97 pin's axes (the filter listbox PANEL + option-resting
# interior at 1280, the income view's category filter). READ-ONLY.
# THE TWO-HALF CONTROLLED FORM, BUILT FROM THE START (the v92..v95 lesson).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

LBOX_JS="(async () => {
  const trig = [...document.querySelectorAll('button')].find(b => {
    const al = b.getAttribute('aria-label') || '';
    return al.includes('category') || /All Categories/.test(b.textContent || '');
  });
  if (!trig) return JSON.stringify({ err: 'no trigger' });
  trig.click();
  await new Promise(r => setTimeout(r, 700));
  const lb = document.querySelector('[role=listbox]');
  if (!lb) return JSON.stringify({ err: 'no listbox' });
  const cs = getComputedStyle(lb);
  const r = lb.getBoundingClientRect();
  const vp = lb.querySelector('[data-radix-select-viewport]') ||
    [...lb.children].find(c => getComputedStyle(c).padding === '4px');
  const vcs = vp ? getComputedStyle(vp) : null;
  const opt = lb.querySelector('[role=option]');
  const ocs = opt ? getComputedStyle(opt) : null;
  const or = opt ? opt.getBoundingClientRect() : null;
  return JSON.stringify({
    panel: {
      bg: cs.backgroundColor, radius: cs.borderRadius,
      border: cs.borderWidth + ' ' + cs.borderColor,
      shadow: cs.boxShadow, maxH: cs.maxHeight,
      overflow: cs.overflow, z: cs.zIndex, pos: cs.position,
      w: Math.round(r.width), h: Math.round(r.height)
    },
    viewport: vcs ? { pad: vcs.padding, display: vcs.display } : 'not found',
    opt0: ocs ? {
      fs: ocs.fontSize, fw: ocs.fontWeight, color: ocs.color,
      pad: ocs.padding, radius: ocs.borderRadius,
      h: or ? Math.round(or.height) : null
    } : null,
    optCount: lb.querySelectorAll('[role=option]').length,
    docSW: document.documentElement.scrollWidth
  });
})()"

export AGENT_BROWSER_SESSION="reflboxarbit97"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
LOGIN_JS="(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'sepnetflix2023@outlook.com');
  set(pw, '\$Abcd1234');
  em.closest('form').requestSubmit();
  return 'submitted';
})()"
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 5
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$LBOX_JS" 2>/dev/null | tail -1
echo "=== ref listbox arbit v97 half done ==="
