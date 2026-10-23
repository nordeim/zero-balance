#!/usr/bin/env bash
# moderow-arbit-v105.sh — the ONE-SHOT both-sides probe of the login's
# AUTH-MODE ACTION ROW family (never census'd as a whole: the v7 G2 pin
# holds the forgot-side button's {fs, lh, h, color} ONLY — the row's flex
# chrome, the signup-side button's typography, and the inner "Sign up"
# emphasis span were never pinned at ANY viewport in ANY spec): the flex
# row + the forgot button (context) + the "Need an account? Sign up"
# button + its emphasis span.
# Run on BOTH sides to verify the family is byte-identical before the pin.
# The /login surface is the LOGGED-OUT surface — passive navigation only,
# no session, no credentials (the v46 rule trivially holds).
# Double-quoted-heredoc-safe.
set -u
REF="https://zero-balance-4885a8f3.base44.app"

MODEROW_JS="(async () => {
  const form = document.querySelector('form');
  if (!form) return JSON.stringify({ err: 'no form' });
  const forgot = [...form.querySelectorAll('button')].find(b => /Forgot password\?/i.test((b.textContent||'').trim()));
  const signup = [...form.querySelectorAll('button')].find(b => /Need an account\?/i.test((b.textContent||'').trim()));
  if (!forgot || !signup) return JSON.stringify({ err: 'no buttons', hasForgot: !!forgot, hasSignup: !!signup });
  let row = forgot.parentElement;
  while (row && row !== document.body && !row.contains(signup)) row = row.parentElement;
  if (!row || row === document.body) return JSON.stringify({ err: 'no row' });
  const rcs = getComputedStyle(row);
  const fcs = getComputedStyle(forgot);
  const scs = getComputedStyle(signup);
  const span = signup.querySelector('span');
  const spcs = span ? getComputedStyle(span) : null;
  return JSON.stringify({
    row: {
      display: rcs.display, align: rcs.alignItems, justify: rcs.justifyContent, gap: rcs.gap,
      w: Math.round(row.getBoundingClientRect().width),
      h: Math.round(row.getBoundingClientRect().height),
    },
    forgot: {
      text: (forgot.textContent||'').trim().slice(0, 24),
      fs: fcs.fontSize, lh: fcs.lineHeight, fw: fcs.fontWeight, color: fcs.color,
      h: Math.round(forgot.getBoundingClientRect().height),
    },
    signup: {
      text: (signup.textContent||'').trim().slice(0, 32),
      fs: scs.fontSize, lh: scs.lineHeight, fw: scs.fontWeight, color: scs.color,
      h: Math.round(signup.getBoundingClientRect().height),
    },
    span: span ? {
      text: (span.textContent||'').trim().slice(0, 16),
      fs: spcs.fontSize, fw: spcs.fontWeight, color: spcs.color,
    } : null,
  });
})()"

echo "=== REFERENCE side (1280) ==="
export AGENT_BROWSER_SESSION="refmoderow105"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$MODEROW_JS" 2>/dev/null | tail -1

echo "=== CLONE side (1280) ==="
cd "$(dirname "$0")/../.."
bash scripts/parity-probes/with-server.sh bash -s <<EOF
set -u
export AGENT_BROWSER_SESSION="clonemoderow105"
agent-browser set viewport 1280 800 >/dev/null 2>&1
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$MODEROW_JS" 2>/dev/null | tail -1
EOF
echo "=== moderow probe v105 done ==="
