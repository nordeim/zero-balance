#!/usr/bin/env bash
# qasibhover-discovery-v155.sh — the ONE-SHOT both-sides census for the v155
# candidate pin family: the QUICK-ACTION SIBLING CARDS' HOVER END-STATES at
# 1280x800 on /dashboard — the never-pinned HOVER PATH of the SIBLING cards
# (the hover family's sibling-completion form; the v125 pin holds the Add
# Income FIRST card's hover end-states ONLY — the tile's group-hover:scale-110
# reveal 40x40 -> 44x44 + the plus's group-hover:opacity-100 reveal 0.5 -> 1;
# the v143 pin the FIRST card's focus-visible ladder; the v149 pin the
# SIBLING cards' focus-visible ladders — the keyboard paths; the v45 F3b pin
# the CARD hover:shadow-lg layers; the v61 F3 + v107 pins the AT-REST chrome;
# the v95 pin the TRANSITION TIMING metadata — the Add Savings + Add Expense
# cards' HOVER end-states held by NO spec at ANY viewport [the suite-wide
# survey: ZERO hover/scale/opacity assertions on these two cards across all
# 24 spec files; the items.spec v146/v151 pins cover the SAVINGS/EXPENSES
# page-header BUTTONS — different elements on different views]):
#   (1) each sibling card's ICON TILE group-hover:scale-110 reveal — the
#       at-rest transform none / 40x40 -> the hovered scale 1.1 / 44x44 (the
#       rendered rect the parity contract; the COMPUTED form differs by
#       construction — the reference's Tailwind v3 computes a transform
#       matrix, the clone's v4 the `scale` property, the v95
#       transition-property computed-form class's hover-state twin — the
#       v125-documented class, expected to reproduce on the siblings);
#   (2) each sibling card's PLUS ICON group-hover:opacity-100 reveal — the
#       at-rest opacity 0.5 -> the hovered 1;
#   (3) the CARD's hover:shadow-lg end-state (the v45 F3b family) + the
#       SIBLING NON-INTERFERENCE cross-check (hovering one card leaves the
#       other at its at-rest contract — the v149 form).
# BOTH SIDES measured (READ-ONLY — login + passive navigation + a REAL
# pointer hover only, the v46 rule; the hover reveals chrome, it clicks
# nothing — the v125 precedent's own surface, the hover LIVE on both sites).
# The hover moves the REAL pointer to the card's OWN center (the coords
# read live after the scrollIntoView — never guessed; the mouse move takes
# x y as TWO args — the v123 lesson); the ladder parks at (5,5) first (the
# v22 lesson), reads the at-rest state, hovers, reads the end-states + the
# sibling cross-check, parks back, and verifies the restore. The v73
# heredoc lesson: the QUOTED <<'EOF' with the env-injected census JS; no
# literal dollar sequences in the census JS (the v64 rule); no single
# quotes inside the single-quoted census strings (the v60 lesson).
set -u
cd "$(dirname "$0")/../.."

# Parameterized per-card finder: the button whose trimmed text is exactly
# the card name; returns the live center as the PLAIN comma-pair (the v116
# convention — the JSON form breaks the shell-side extraction).
qa_finder() {
  cat <<QAF
(async () => {
  const b = [...document.querySelectorAll("button")].find((x) =>
    /^$1\$/.test((x.textContent || "").trim()));
  if (!b) return JSON.stringify({err: "no $1 button"});
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
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()
QAF
}

# Parameterized per-card state read: the card's hover end-state axes — the
# card shadow + hover match, the tile {transform, scale, w, h} + bg tint,
# the plus {opacity, w}. The tile band 25..65 covers BOTH rungs (the
# at-rest 40 and the hovered 44).
qa_state() {
  cat <<QAS
(async () => {
  const b = [...document.querySelectorAll("button")].find((x) =>
    /^$1\$/.test((x.textContent || "").trim()));
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
    tile: { transform: cs.transform, scale: cs.scale, w: Math.round(r.width), h: Math.round(r.height), bg: cs.backgroundColor },
    plus: { opacity: getComputedStyle(plus).opacity, w: Math.round(plus.getBoundingClientRect().width) },
  });
})()
QAS
}

run_side() {
  # $1 = side label, $2 = base URL, $3 = session name, $4 = login JS
  FINDER_JS="$(qa_finder "Add Savings")"
  STATE_SAV="$(qa_state "Add Savings")"
  STATE_EXP="$(qa_state "Add Expense")"
  FINDER_EXP="$(qa_finder "Add Expense")"
  export AGENT_BROWSER_SESSION="$3"
  agent-browser open "$2/login" >/dev/null 2>&1
  sleep 4
  for attempt in 1 2 3 4; do
    RESULT=$(agent-browser eval "$4" 2>/dev/null | tail -1)
    echo "$1 login attempt $attempt: $RESULT"
    if echo "$RESULT" | grep -q "submitted"; then break; fi
    agent-browser open "$2/login" >/dev/null 2>&1
    sleep 4
  done
  sleep 4
  agent-browser set viewport 1280 800 >/dev/null 2>&1
  sleep 1
  agent-browser open "$2/dashboard" >/dev/null 2>&1
  sleep 4

  for CARD in "Add Savings" "Add Expense"; do
    if [ "$CARD" = "Add Savings" ]; then OTHER="Add Expense"; else OTHER="Add Savings"; fi
    FINDER_JS="$(qa_finder "$CARD")"
    STATE_CUR="$(qa_state "$CARD")"
    STATE_OTHER="$(qa_state "$OTHER")"
    echo "=== $1 [$CARD]: the finder + live center (never guessed) ==="
    CENTER="$(agent-browser eval "$FINDER_JS" 2>/dev/null | tail -1 | tr -d '"')"
    echo "$CENTER"
    CX="${CENTER%,*}"
    CY="${CENTER#*,}"
    if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on $1 for $CARD"; else
      agent-browser mouse move 5 5 >/dev/null 2>&1
      sleep 1
      echo "=== $1 [$CARD]: AT-REST (pointer parked at 5,5) ==="
      agent-browser eval "$STATE_CUR" 2>/dev/null | tail -1

      agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
      sleep 1
      echo "=== $1 [$CARD]: HOVERED (real pointer at the card center $CX,$CY) ==="
      agent-browser eval "$STATE_CUR" 2>/dev/null | tail -1
      echo "=== $1 [$CARD]: SIBLING cross-check (the other card stays at-rest) ==="
      agent-browser eval "$STATE_OTHER" 2>/dev/null | tail -1

      agent-browser mouse move 5 5 >/dev/null 2>&1
      sleep 1
      echo "=== $1 [$CARD]: RESTORED (pointer re-parked at 5,5) ==="
      agent-browser eval "$STATE_CUR" 2>/dev/null | tail -1
    fi
  done
}

REF_LOGIN_JS="(async () => {
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

CLONE_LOGIN_JS="(async () => {
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
})()"

# ---------- REFERENCE half (direct) ----------
run_side "REF" "https://zero-balance-4885a8f3.base44.app" "refqahov155" "$REF_LOGIN_JS"
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
CLONE_LOGIN_JS="$CLONE_LOGIN_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneqahov155"

qa_finder() {
  cat <<QAF
(async () => {
  const b = [...document.querySelectorAll("button")].find((x) =>
    /^$1\$/.test((x.textContent || "").trim()));
  if (!b) return JSON.stringify({err: "no $1 button"});
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
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()
QAF
}

qa_state() {
  cat <<QAS
(async () => {
  const b = [...document.querySelectorAll("button")].find((x) =>
    /^$1\$/.test((x.textContent || "").trim()));
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
    tile: { transform: cs.transform, scale: cs.scale, w: Math.round(r.width), h: Math.round(r.height), bg: cs.backgroundColor },
    plus: { opacity: getComputedStyle(plus).opacity, w: Math.round(plus.getBoundingClientRect().width) },
  });
})()
QAS
}

for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$CLONE_LOGIN_JS" 2>/dev/null | tail -1)
  echo "CLONE login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
  sleep 4
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/dashboard" >/dev/null 2>&1
sleep 4

for CARD in "Add Savings" "Add Expense"; do
  if [ "$CARD" = "Add Savings" ]; then OTHER="Add Expense"; else OTHER="Add Savings"; fi
  FINDER_JS="$(qa_finder "$CARD")"
  STATE_CUR="$(qa_state "$CARD")"
  STATE_OTHER="$(qa_state "$OTHER")"
  echo "=== CLONE [$CARD]: the finder + live center (never guessed) ==="
  CENTER="$(agent-browser eval "$FINDER_JS" 2>/dev/null | tail -1 | tr -d '"')"
  echo "$CENTER"
  CX="${CENTER%,*}"
  CY="${CENTER#*,}"
  if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on CLONE for $CARD"; else
    agent-browser mouse move 5 5 >/dev/null 2>&1
    sleep 1
    echo "=== CLONE [$CARD]: AT-REST (pointer parked at 5,5) ==="
    agent-browser eval "$STATE_CUR" 2>/dev/null | tail -1

    agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
    sleep 1
    echo "=== CLONE [$CARD]: HOVERED (real pointer at the card center $CX,$CY) ==="
    agent-browser eval "$STATE_CUR" 2>/dev/null | tail -1
    echo "=== CLONE [$CARD]: SIBLING cross-check (the other card stays at-rest) ==="
    agent-browser eval "$STATE_OTHER" 2>/dev/null | tail -1

    agent-browser mouse move 5 5 >/dev/null 2>&1
    sleep 1
    echo "=== CLONE [$CARD]: RESTORED (pointer re-parked at 5,5) ==="
    agent-browser eval "$STATE_CUR" 2>/dev/null | tail -1
  fi
done
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v84.mjs 2>&1 | tail -2
echo "=== qasibhover discovery v155 done ==="
