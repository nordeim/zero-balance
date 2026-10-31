#!/usr/bin/env bash
# stathovershadow-arbit-v137.sh — the ONE-SHOT both-sides census for the
# v137 candidate pin family: the INTERACTIVE STAT CARD's OWN-HOVER SHADOW
# LADDER at 1280x800 on /dashboard — the never-pinned SHADOW path of the
# pinned hover family (the v40 pin the TAB stops + the geometry bands +
# the Enter/Space SUPERSET activation; the v51 F2 pin the AT-REST card
# chrome at 390 incl. the inline rest shadow; the v88 pin the count-row +
# divider; the v131 pin the own-hover REVEAL ladder [radial + chevron
# opacity]; the v45 F3b pin the QUICK-ACTION TWIN's LIVE hover:shadow-lg
# layers — the STAT card's hovered shadow held by NO spec at ANY
# viewport).
#
# THE CONSTRUCT UNDER TEST: the stat card carries BOTH the
# hover:shadow-lg utility AND an INLINE boxShadow (rgba(0, 0, 0, 0.06)
# 0px 4px 20px) — the v43 category-row precedent says the INLINE style
# beats the utility in the cascade, so the expected hovered end-state is
# the INLINE PERSISTENCE (the shadow unchanged across the ladder's
# rungs, the hover:shadow-lg inert) — measured LIVE on BOTH sides before
# any pin is written (the reference's own inert card may or may not
# carry the same class+inline construct).
#
# BOTH SIDES measured (READ-ONLY — login + passive navigation + a REAL
# pointer hover only, the v46 rule; the hover reveals chrome, it clicks
# nothing — the CLONE's card CLICKS NAVIGATE to the type view, so the
# card is NEVER clicked). The hover moves the REAL pointer to the card's
# OWN center (the coords read live after the scrollIntoView — never
# guessed; the mouse move takes x y as TWO args — the v123 lesson); the
# ladder parks at (5,5) first (the v22 lesson), reads the at-rest state,
# hovers, reads the end-state, parks back, and verifies the restore.
# The v73 heredoc lesson: the QUOTED <<'EOF' with the env-injected
# census JS; no literal dollar sequences in the census JS (the v64
# rule); no single quotes inside the single-quoted census strings (the
# v60 lesson).
set -u
cd "$(dirname "$0")/../.."

CARD_FINDER='(async () => {
  const h3 = [...document.querySelectorAll("h3")].find((x) =>
    (x.textContent || "").trim() === "Total Income");
  if (!h3) return JSON.stringify({err: "no Total Income h3"});
  let card = h3;
  while (card && card.parentElement) {
    const p = card.parentElement;
    const statCards = [...p.children].filter((c) =>
      [...c.querySelectorAll("h3")].some((h) =>
        /^(Total Income|Total Savings|Total Expenses)$/.test((h.textContent || "").trim())));
    if (statCards.length >= 2) break;
    card = p;
  }
  const first = [...card.parentElement.children].find((c) =>
    [...c.querySelectorAll("h3")].some((h) => (h.textContent || "").trim() === "Total Income"));
  if (!first) return JSON.stringify({err: "no first card"});
  first.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = first.getBoundingClientRect();
  // the PLAIN comma-pair return (the v116 convention)
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

STATE_JS='(async () => {
  const h3 = [...document.querySelectorAll("h3")].find((x) =>
    (x.textContent || "").trim() === "Total Income");
  if (!h3) return JSON.stringify({err: "no h3"});
  let card = h3;
  while (card && card.parentElement) {
    const p = card.parentElement;
    const statCards = [...p.children].filter((c) =>
      [...c.querySelectorAll("h3")].some((h) =>
        /^(Total Income|Total Savings|Total Expenses)$/.test((h.textContent || "").trim())));
    if (statCards.length >= 2) break;
    card = p;
  }
  const first = [...card.parentElement.children].find((c) =>
    [...c.querySelectorAll("h3")].some((h) => (h.textContent || "").trim() === "Total Income"));
  if (!first) return JSON.stringify({err: "no card in state read"});
  const cs = getComputedStyle(first);
  return JSON.stringify({
    cardHover: first.matches(":hover"),
    cardCursor: cs.cursor,
    // THE SHADOW AXIS — the full computed string, never truncated (the
    // v11 probe-hygiene rule: the visible layer may trail transparent
    // lead layers)
    boxShadow: cs.boxShadow,
    // the construct documentation: the hover:shadow-lg class token
    clsHasHoverShadowLg: (first.className || "").toString().includes("hover:shadow-lg"),
    transition: cs.transitionProperty + " " + cs.transitionDuration
  });
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refstsh137"
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
agent-browser open "$REF/dashboard" >/dev/null 2>&1
sleep 4

echo "=== REF: the stat-card finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$CARD_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
echo "$CENTER"
CX="${CENTER%,*}"
CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on REF"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: HOVERED (real pointer at the card center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
CARD_FINDER="$CARD_FINDER" STATE_JS="$STATE_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonestsh137"
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
agent-browser open "http://localhost:3200/dashboard" >/dev/null 2>&1
sleep 4

echo "=== CLONE: the stat-card finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$CARD_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
echo "$CENTER"
CX="${CENTER%,*}"
CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on CLONE"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: HOVERED (real pointer at the card center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>&1 | tail -8
echo "=== stathovershadow arbit v137 done ==="
