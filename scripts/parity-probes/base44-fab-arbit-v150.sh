#!/usr/bin/env bash
# base44-fab-arbit-v150.sh — the ONE-SHOT both-sides arbitration for the
# v150 MOBILE-TWINS re-run pair's FAB flags (the NETWORTH surface — noted
# in pass 1 as the IDENTICAL verdict's minor note: "In image 1, the figure
# '$25,000.00' in the Savings Account card is partially covered by the
# 'Edit with Base 44' overlay badge — an artifact of the screenshot, not a
# style difference" — and the DASHBOARD surface — claimed in pass 1 (the
# DIFFERENT verdict's layout flag #1): "Image 1 contains a black 'Edit
# with Base 44 X' badge/banner floating over the 'Total Expenses' row in
# the Net Zero Breakdown card, partially covering that row. Absent in
# image 2" + noted in pass 2 (the IDENTICAL verdict's own note: "data and
# one overlay badge differ") — ALL the platform-chrome class; the
# v97/v103/v108/v109/v115/v120/v123/v127/v129/v135/v141/v142/v143/v144
# standing disproof form: the FAB never renders in the app DOM on EITHER
# side — it lives in the reference's platform iframe chrome, outside the
# queryable body DOM):
# both flagged surfaces measured, both sides, MOBILE 390x844 (the pair's
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

echo "=== REFERENCE side (390, / + /networth — the TWO flagged surfaces, logged-in) ==="
export AGENT_BROWSER_SESSION="reffab150"
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
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census (the dashboard surface):"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census (the networth surface):"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1

echo "=== CLONE side (390, / + /networth — the TWO flagged surfaces, logged-in) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonefab150"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census (the dashboard surface):"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- FAB census (the networth surface):"
agent-browser eval "$FAB_JS" 2>/dev/null | tail -1
EOF
echo "=== base44-fab arbit v150 done ==="
