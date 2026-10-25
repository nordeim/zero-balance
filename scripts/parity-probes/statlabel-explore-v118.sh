#!/usr/bin/env bash
# statlabel-explore-v118.sh — the exploratory probe for the reference's
# dashboard stat-card label family (the v118 NEW flag: 'Total Expense'
# singular vs the clone's 'Total Expenses'). READ-ONLY.
set -u
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refstat118b"

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

EXPLORE_JS="(() => {
  const hits = [...document.querySelectorAll('main p, main span, main h1, main h2, main h3, main h4')].filter(el => {
    const t = (el.textContent || '').trim();
    return /^Total/.test(t) && t.length < 30 && el.children.length === 0;
  });
  return JSON.stringify(hits.map(el => {
    const cs = getComputedStyle(el);
    let p = el;
    for (let i = 0; i < 6 && p.parentElement; i++) {
      p = p.parentElement;
      const pc = getComputedStyle(p);
      const pr = p.getBoundingClientRect();
      if (pc.borderRadius !== '0px' && pr.width > 100 && pr.width < 600 && pr.height > 50 && pr.height < 250) break;
    }
    const pr = p.getBoundingClientRect();
    const pc = getComputedStyle(p);
    return {
      text: (el.textContent || '').trim(),
      tag: el.tagName,
      fs: cs.fontSize,
      fw: cs.fontWeight,
      color: cs.color,
      cardTag: p.tagName,
      cardW: Math.round(pr.width),
      cardH: Math.round(pr.height),
      cardPad: pc.padding,
      cardRadius: pc.borderRadius,
      cardBg: pc.backgroundColor,
    };
  }));
})()"

agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
for attempt in 1 2 3; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- stat label explore:"
agent-browser eval "$EXPLORE_JS" 2>/dev/null | tail -1
echo "=== explore done ==="
