#!/usr/bin/env bash
# base44-fab-arbit-v151.sh — the ONE-SHOT both-sides arbitration for the
# v151 ITEMS re-run pair's FAB flags (the EXPENSES surface — noted in
# pass 1 [the DIFFERENT-data-only verdict's data list tail]: "Bottom-right
# 'Edit with Base 44' floating badge present in Reference, absent in Clone
# (likely an overlay, not page content)" — and the INCOME surface —
# claimed in pass 2 (the DIFFERENT-data-only verdict's layout/style list):
# "'Edit with Base44' black pill overlay bottom-right present only in
# img 1, absent in img 2" + re-noted on the expenses pair in pass 2:
# "Reference includes a black 'Edit with Base44' floating overlay in the
# bottom-right corner; the clone does not" — ALL the platform-chrome
# class; the v97/v103/v108/v109/v115/v120/v123/v127/v129/v135/v141/v142/
# v143/v144/v148/v149/v150 standing disproof form: the FAB never renders
# in the app DOM on EITHER side — it lives in the reference's platform
# iframe chrome, outside the queryable body DOM):
# both flagged surfaces measured, both sides, DESKTOP 1280x800 (the pair's
# own viewport), logged-in. READ-ONLY. Double-quoted-heredoc-safe: no
# dollar sequences in the FAB census JS; no backticks; no
# attribute-value selectors. The reference login JS carries the escaped
# '\$Abcd1234' form (the double-quoted shell string); the clone login
# carries no dollar sequence (Demo1234!).
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

echo "=== REFERENCE side (1280, /income + /expenses — the TWO flagged surfaces, logged-in) ==="
export AGENT_BROWSER_SESSION="reffab151"
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
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census (the income surface):"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census (the expenses surface):"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /income + /expenses — the TWO flagged surfaces, logged-in) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonefab151"
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
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census (the income surface):"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census (the expenses surface):"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
EOF
echo "=== base44-fab arbit v151 done ==="
