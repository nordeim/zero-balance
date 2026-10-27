#!/usr/bin/env bash
# profilecard-arbit-v130.sh — the ONE-SHOT both-sides arbitration for the
# v130 networth pair's pass-2 profile-card flag (the VLM: "the 'Budget Pro'
# user profile card at the bottom of the left navigation rail has shifted
# vertically. In the reference image, it is positioned higher up (near the
# middle/bottom), whereas in the clone, it is pushed down to the very bottom
# of the viewport"): the sidebar is a FIXED inset-y-0 rail (sidebar.tsx:188
# on the clone), so the profile block pins to the VIEWPORT bottom on both
# sides regardless of the document height — the full-page seed-count
# difference (ref 1 asset card vs clone 3 cards in 3 groups) changes the
# DOCUMENT height, never the fixed rail's geometry. The census measures the
# profile block's viewport-anchored rect + the document heights, both sides,
# /networth at 1280x800, logged-in. READ-ONLY. Double-quoted-heredoc-safe:
# no dollar sequences; no backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

PROFILE_JS="(async () => {
  const cands = [...document.querySelectorAll('body *')].filter(el => {
    const t = (el.textContent || '').trim();
    const r = el.getBoundingClientRect();
    return /Budget Pro/.test(t) && el.children.length <= 6 && r.height > 40 && r.height < 200 && r.width > 0 && r.width < 400;
  });
  if (!cands.length) return JSON.stringify({ found: false });
  const t = cands.reduce((a, b) => {
    const ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
    return ra.width * ra.height <= rb.width * rb.height ? a : b;
  });
  const r = t.getBoundingClientRect();
  const aside = t.closest('aside');
  const asideR = aside ? aside.getBoundingClientRect() : null;
  return JSON.stringify({
    found: true,
    block: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height), bottomFromVH: Math.round(window.innerHeight - r.bottom) },
    aside: asideR ? { y: Math.round(asideR.y), h: Math.round(asideR.height), bottomFromVH: Math.round(window.innerHeight - asideR.bottom), position: getComputedStyle(aside).position } : null,
    vh: window.innerHeight,
    docH: document.documentElement.scrollHeight,
    label: (t.textContent || '').trim().slice(0, 24),
  });
})()"

echo "=== REFERENCE side (1280, /networth, logged-in) ==="
export AGENT_BROWSER_SESSION="refprof130"
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
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- profile-card census:"
agent-browser eval "$PROFILE_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, /networth, logged-in) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="cloneprof130"
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
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- profile-card census:"
agent-browser eval "$PROFILE_JS" 2>/dev/null | tail -1
EOF
echo "=== profilecard arbit v130 done ==="
