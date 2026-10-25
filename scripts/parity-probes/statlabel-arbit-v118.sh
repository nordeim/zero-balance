#!/usr/bin/env bash
# statlabel-arbit-v118.sh — the ONE-SHOT both-sides arbitration for the
# v118 cycle's NEW flag (the VLM on the drill-down pair: "The label for the
# third card reads 'Total Expense' (singular) in image 1 [the reference]
# and 'Total Expenses' (plural) in image 2 [the clone]" — the dashboard's
# stat-card row at desktop 1280x800).
#   The census reads EVERY stat card in the dashboard's stat row on both
#   sides: the card's label text (trimmed), its font chrome, and the card
#   chrome — so the verdict covers the whole label family, not just the
#   flagged third card (one flag, the full family measured — the v43
#   measurement-is-the-authority rule).
# READ-ONLY. Double-quoted-heredoc-safe: no dollar sequences in the census
# JS; no backticks; no attribute-value selectors.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

STAT_JS="(async () => {
  // The stat row: the three cards under the hero, each carrying an amount
  // and a trend icon. Found structurally: cards whose first text child is
  // a small uppercase-ish label followed by a currency amount (the v72
  // structural-finder class — class strings never trusted).
  const cards = [...document.querySelectorAll('main div')].filter(el => {
    if (el.children.length < 2 || el.children.length > 5) return false;
    const r = el.getBoundingClientRect();
    if (r.width < 150 || r.width > 500 || r.height < 60 || r.height > 200) return false;
    const cs = getComputedStyle(el);
    if (cs.borderRadius === '0px') return false;
    const texts = [...el.querySelectorAll('p,span,h1,h2,h3,h4')].map(n => (n.textContent || '').trim()).filter(Boolean);
    if (texts.length < 2) return false;
    return /Total/i.test(texts[0]) && /\\$/.test(el.textContent || '');
  });
  const out = cards.map(el => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    const texts = [...el.querySelectorAll('p,span,h1,h2,h3,h4')].map(n => (n.textContent || '').trim()).filter(Boolean);
    const labelEl = [...el.querySelectorAll('p,span,h1,h2,h3,h4')].find(n => /Total/i.test((n.textContent || '').trim()));
    const lcs = labelEl ? getComputedStyle(labelEl) : null;
    return {
      label: texts[0],
      labelFs: lcs ? lcs.fontSize : null,
      labelFw: lcs ? lcs.fontWeight : null,
      labelColor: lcs ? lcs.color : null,
      cardW: Math.round(r.width),
      cardH: Math.round(r.height),
      pad: cs.padding,
      radius: cs.borderRadius,
    };
  });
  return JSON.stringify({ statCardCount: out.length, cards: out });
})()"

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

echo "=== REFERENCE side (1280, / — the dashboard stat row, logged-in) ==="
export AGENT_BROWSER_SESSION="refstat118"
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
echo "--- stat-label census:"
agent-browser eval "$STAT_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280, / — the dashboard stat row, logged-in) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonestat118"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser eval "(async () => {
  const em = document.querySelector('input[type=email], input[name=email]');
  const pw = document.querySelector('input[type=password]');
  if (!em || !pw) return 'already logged in?';
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "--- stat-label census:"
agent-browser eval "$STAT_JS" 2>/dev/null | tail -1
EOF
echo "=== statlabel arbit v118 done ==="
