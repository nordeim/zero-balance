#!/usr/bin/env bash
# qa-transition-arbit-v89.sh — the v89 pin's OWN AXES, measured on BOTH sides
# (the v87/v88 one-shot supplemental-census precedent — the pin's axes first
# measured byte-identical before the pin is written). The never-pinned family
# this cycle: the quick-action cards' TRANSITION family (transitionDuration
# "0.2s" + transitionProperty — the card census's transition axis, never
# pinned in dashboard.spec.ts at ANY viewport; items.spec.ts pins the ITEM
# card's own 0.2s family — a different component) + the PLUS icons' viewBox
# (the v77 pin holds the ICON's viewBox only — the first svg; the plus's own
# never) + the guidelines card BODY's display (the v61 F2 pin holds the
# body's pad only). READ-ONLY on both sides (login + passive navigation —
# the v46 rule). The v73 heredoc lesson (QUOTED <<'EOF', env-injected); the
# v64 rule (no literal dollar sequences); the v78 rule (no attribute-value
# selectors); the v87 rule (no accessible-name dependence for reference-side
# finders — geometry + text-content only).
set -u
REF="https://zero-balance-4885a8f3.base44.app"

CENSUS="(function () {
  const out = {};
  const qas = [...document.querySelectorAll(\"button\")].filter(
    (b) => /^Add (Income|Savings|Expense)\$/.test((b.textContent || \"\").trim())
  );
  if (qas.length !== 3) return JSON.stringify({ error: \"no quick-action trio\", count: qas.length });
  out.cards = qas.map((b) => {
    const cs = getComputedStyle(b);
    const svgs = [...b.querySelectorAll(\"svg\")];
    const plusSvg = svgs[svgs.length - 1];
    return {
      text: (b.textContent || \"\").trim(),
      transitionDuration: cs.transitionDuration,
      transitionProperty: cs.transitionProperty,
      plusViewBox: plusSvg ? (plusSvg.getAttribute(\"viewBox\") || \"\") : null,
      plusW: plusSvg ? Math.round(plusSvg.getBoundingClientRect().width) : null
    };
  });
  const heading = [...document.querySelectorAll(\"h1, h2, h3, div, span\")].find(
    (x) => (x.textContent || \"\").trim() === \"Budget Guidelines\" && x.children.length === 0
  );
  if (!heading) return JSON.stringify({ error: \"no guidelines heading\", out: out });
  let card = heading;
  while (card.parentElement) {
    const cs = getComputedStyle(card);
    if (cs.boxShadow !== \"none\" && cs.borderRadius !== \"0px\" && card.querySelector(\"p\")) break;
    card = card.parentElement;
  }
  const header = heading.parentElement;
  const body = [...card.children].find((c) => c !== header);
  out.guidelinesBody = body ? {
    display: getComputedStyle(body).display,
    pad: getComputedStyle(body).padding
  } : null;
  out.docSW = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()"

# ---------- REFERENCE side ----------
export AGENT_BROWSER_SESSION="refqa89"
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
  echo "ref login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "$REF/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/" >/dev/null 2>&1
sleep 5
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== REF: qa transition + plus viewBox + guidelines body census at 1280 ==="
agent-browser eval "$CENSUS" 2>/dev/null | tail -1

# ---------- CLONE side ----------
cd "$(dirname "$0")/../.."
CENSUS="$CENSUS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneqa89"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== CLONE: qa transition + plus viewBox + guidelines body census at 1280 ==="
agent-browser eval "$CENSUS" 2>/dev/null | tail -1
EOF

echo "=== qa-transition arbit v89 done ==="
