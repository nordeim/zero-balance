#!/usr/bin/env bash
# stat-title-ref-v82.sh — DOM arbitration for the v82 drill-down VLM flag:
# "the 'Total Expense' card title is truncated to 'Total Expenses' in the
# clone". Measures the reference's stat card titles verbatim at 1280.
# READ-ONLY (the v46 rule).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

export AGENT_BROWSER_SESSION="refstat82"
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
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF stat card titles (verbatim) ==="
agent-browser eval "(async () => {
  const out = {};
  // The stat-row cards: the h3/h4/p headings containing 'Total '
  const heads = [...document.querySelectorAll('h1,h2,h3,h4,h5,p,span,div')].filter(e => {
    const t = (e.textContent || '').trim();
    return /^Total (Income|Savings|Expenses?)$/.test(t) && e.children.length === 0;
  });
  out.statTitles = heads.map(e => {
    const cs = getComputedStyle(e);
    return { text: e.textContent.trim(), tag: e.tagName, fs: cs.fontSize, fw: cs.fontWeight, color: cs.color };
  });
  // Any 'Total Expense' singular anywhere on the page
  const body = (document.querySelector('main') || document.body).textContent;
  out.hasSingular = /Total Expense(?!s)/.test(body);
  out.hasPlural = /Total Expenses/.test(body);
  return JSON.stringify(out);
})()" 2>/dev/null | tail -1
echo "=== ref stat titles done ==="
