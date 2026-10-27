#!/usr/bin/env bash
# qahover-arbit-v125.sh — the ONE-SHOT both-sides census for the v125
# candidate pin family: the QUICK-ACTION card's HOVER END-STATES at
# 1280x800 on /dashboard — the never-pinned PATH of the pinned
# quick-action family (the v45 F3b pin holds the CARD's hover:shadow-lg
# layers only; the v61 F3 + v107 pins the AT-REST chrome — the tile
# 40x40/radius-12 + the icon offsets + the label/plus; the v95 pin the
# TRANSITION TIMING family; the tiles'/plus' hover END-STATES held by NO
# spec):
#   (1) the ICON TILE's group-hover:scale-110 reveal — the at-rest
#       transform none / 40x40 -> the hovered scale 1.1 / 44x44 (the
#       rendered rect the parity contract; the COMPUTED form differs by
#       construction — the reference's Tailwind v3 computes a transform
#       matrix, the clone's v4 the `scale` property, the v95
#       transition-property computed-form class's hover-state twin);
#   (2) the PLUS ICON's group-hover:opacity-100 reveal — the at-rest
#       opacity 0.5 -> the hovered 1 (identical computed form both
#       sides, the reference's own ml-auto opacity-50
#       group-hover:opacity-100 idiom).
# BOTH SIDES measured (READ-ONLY — login + passive navigation + a REAL
# pointer hover only, the v46 rule; the hover reveals chrome, it clicks
# nothing — the v45 F3b precedent's own surface, the hover LIVE on both
# sites). The hover moves the REAL pointer to the card's OWN center (the
# coords read live after the scrollIntoView — never guessed; the mouse
# move takes x y as TWO args — the v123 lesson); the ladder parks at
# (5,5) first (the v22 lesson), reads the at-rest state, hovers, reads
# the end-states, parks back, and verifies the restore. The v73 heredoc
# lesson: the QUOTED <<'EOF' with the env-injected census JS; no literal
# dollar sequences in the census JS (the v64 rule); no single quotes
# inside the single-quoted census strings (the v60 lesson).
set -u
cd "$(dirname "$0")/../.."

QA_FINDER='(async () => {
  const b = [...document.querySelectorAll("button")].find((x) =>
    /^Add Income$/.test((x.textContent || "").trim()));
  if (!b) return JSON.stringify({err: "no Add Income button"});
  // TAG-AGNOSTIC tile finder (the v107 DIV-vs-SPAN lesson: the reference
  // builds the tile/row as DIVs, the clone as spans — positional/shape
  // matching, never a tag match): the radius-12px box in the 30..60 band.
  const tile = [...b.querySelectorAll("span, div")].find((s) => {
    const cs = getComputedStyle(s);
    const r = s.getBoundingClientRect();
    return cs.borderRadius === "12px" && r.width >= 30 && r.width <= 60 && r.height >= 30 && r.height <= 60;
  });
  const svgs = [...b.querySelectorAll("svg")];
  if (!tile || svgs.length < 2) return JSON.stringify({err: "no tile/plus", svgCount: svgs.length});
  b.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = b.getBoundingClientRect();
  // the PLAIN comma-pair return (the v116 convention — the JSON form is
  // printed with escaped quotes that break the shell-side sed extraction)
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

STATE_JS='(async () => {
  const b = [...document.querySelectorAll("button")].find((x) =>
    /^Add Income$/.test((x.textContent || "").trim()));
  if (!b) return JSON.stringify({err: "no button"});
  const tile = [...b.querySelectorAll("span, div")].find((s) => {
    const cs = getComputedStyle(s);
    const r = s.getBoundingClientRect();
    return cs.borderRadius === "12px" && r.width >= 25 && r.width <= 65 && r.height >= 25 && r.height <= 65;
  });
  const svgs = [...b.querySelectorAll("svg")];
  if (!tile) return JSON.stringify({err: "no tile in state read"});
  const cs = getComputedStyle(tile);
  const r = tile.getBoundingClientRect();
  const plus = svgs[svgs.length - 1];
  return JSON.stringify({
    cardShadow: getComputedStyle(b).boxShadow,
    cardHover: b.matches(":hover"),
    tile: { transform: cs.transform, scale: cs.scale, w: Math.round(r.width), h: Math.round(r.height) },
    plus: { opacity: getComputedStyle(plus).opacity, w: Math.round(plus.getBoundingClientRect().width) },
  });
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refqahover125"
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

echo "=== REF: the QA finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$QA_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
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
QA_FINDER="$QA_FINDER" STATE_JS="$STATE_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneqahover125"
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

echo "=== CLONE: the QA finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$QA_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
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
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v84.mjs 2>&1 | tail -2
echo "=== qahover arbit v125 done ==="
