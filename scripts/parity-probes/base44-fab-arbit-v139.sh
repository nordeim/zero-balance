#!/usr/bin/env bash
# base44-fab-arbit-v139.sh — the ONE-SHOT both-sides arbitration for the
# v139 re-run pair's FAB flag (the INCOME surface — the VLM pass 1: "A
# black 'Edit with Base44' floating action button is present in the
# bottom-right corner of Image 2 [the clone], but absent in Image 1" and
# the VLM pass 2: "present in the bottom-right corner of Image 1 [the
# reference] but is absent in Image 2" — claimed in BOTH directions
# across the two passes, the documented perception-artifact form; the
# v97/v103/v108/v109/v115/v120/v123/v127/v129/v136 standing disproof
# form: the FAB never renders in the app DOM on EITHER side — it lives
# in the reference's platform iframe chrome, outside the queryable body
# DOM): the flagged surface measured, both sides, desktop 1280x800,
# logged-in. READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences
# in the FAB census JS; no backticks; no attribute-value selectors. The
# reference login JS carries the escaped '\$Abcd1234' form (the
# double-quoted shell string); the clone login carries no dollar
# sequence (Demo1234!).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

FAB_JS="(async () => {
  const hits = [...document.querySelectorAll('body *')].filter(el => {
    const t = (el.textContent || '').trim();
    return t.length > 0 && t.length < 40 && /Base44/i.test(t) && el.children.length <= 2;
  });
  const out = hits.map(el => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return {
      tag: el.tagName,
      text: (el.textContent || '').trim().slice(0, 30),
      fixed: cs.position,
      bottom: Math.round(window.innerHeight - r.bottom),
      right: Math.round(window.innerWidth - r.right),
      w: Math.round(r.width),
      h: Math.round(r.height),
      bg: cs.backgroundColor,
      color: cs.color,
    };
  });
  return JSON.stringify({ fabCount: out.length, fabs: out, bodyHasBase44: /Base44/.test(document.body.textContent || '') });
})()"

echo "=== REFERENCE side (1280, /income — the flagged surface, logged-in) ==="
export AGENT_BROWSER_SESSION="reffab139"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
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
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 4
echo "--- ref income FAB census ---"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /income — the flagged surface, logged-in) ==="
export AGENT_BROWSER_SESSION="clonefab139"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'no inputs';
  const set = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
  };
  set(em, 'demo@zerobalance.app');
  set(pw, 'Demo1234!');
  em.closest('form').requestSubmit();
  return 'submitted';
})()" 2>/dev/null | tail -1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 4
echo "--- clone income FAB census ---"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
echo "=== fab arbit v139 done ==="
