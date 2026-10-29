#!/usr/bin/env bash
# focusladder-arbit-v134.sh — the ONE-SHOT both-sides census for the v134
# candidate pin family: the SAVINGS GOAL-CARD KEBAB-TRIGGER's FOCUS-VISIBLE
# LADDER at desktop 1280x800 on /savings — the never-pinned FOCUS RING axis
# of the pinned reveal family (the v45 F1a pin the trigger's w/h/at-rest
# opacity on /income; the v116 pin the at-rest box chrome + the CARD-hover
# reveal on /savings; the v122 pin the OPEN+parked state; the v128 pin the
# OWN-HOVER tint ladder; the v36 S3 pin the keyboard REVEAL on /income —
# {fv, opacity} alone, NEVER the ring; the ring layer — the 1px #0a0a0a
# focus family every reference button carries — held by NO spec at ANY
# viewport):
#   the ladder — the at-rest rung (pointer parked at 5,5: opacity 0, bg
#   transparent) -> the REAL-TAB-FOCUSED rung (a REAL keyboard walk to the
#   trigger: the computed ring + the reveal state + the bg) -> the blurred
#   rung (restored).
# The target: the Emergency Fund goal card's trigger — the SAME-LABEL card
# on BOTH sides (the reference's only savings card; the clone's second
# card). The finder TAG-AGNOSTIC + STRUCTURAL (the h4 text -> the
# rounded-xl card -> the small square button, the v128 census's own form —
# the reference's trigger is UNLABELLED, the aria-label the clone's a11y
# superset).
# BOTH SIDES measured (READ-ONLY — login + passive navigation + a REAL
# keyboard walk only, the v46 rule; the Tab walk reveals chrome, it clicks
# nothing and NEVER presses Enter — the menu opens on click/Enter, both
# out of bounds; the v36 S3 Tab-walk precedent's own form). The walk is
# FINDER-BOUNDED (press Tab until the active element IS the target trigger
# — never a hardcoded count; the sites' stop orders differ: the reference
# 1 card, the clone 2 cards). The ladder parks at (5,5) first (the v22
# lesson); tr -d '"' on the extraction (the v124 lesson).
set -u
cd "$(dirname "$0")/../.."

KEBAB_FINDER='(async () => {
  // STRUCTURAL finder (the v128 form): the Emergency Fund h4 -> the
  // rounded-xl card -> the ONLY small square button (w 20..50, square-ish).
  const h4 = [...document.querySelectorAll("h4, h3, div")].find((el) => (el.textContent || "").trim() === "Emergency Fund" && el.children.length === 0);
  if (!h4) return JSON.stringify({err: "no Emergency Fund leaf"});
  let card = h4;
  while (card && card !== document.body) {
    const cls = typeof card.className === "string" ? card.className : "";
    if (cls.includes("rounded-xl")) break;
    card = card.parentElement;
  }
  if (!card || card === document.body) return JSON.stringify({err: "no rounded-xl card"});
  const btns = [...card.querySelectorAll("button")].filter((b) => {
    const r = b.getBoundingClientRect();
    return r.width >= 20 && r.width <= 50 && Math.abs(r.width - r.height) < 8;
  });
  if (btns.length !== 1) return JSON.stringify({err: "trigger count " + btns.length});
  const r = btns[0].getBoundingClientRect();
  return JSON.stringify({found: true, x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2)});
})()'

STATE_JS='(async () => {
  const h4 = [...document.querySelectorAll("h4, h3, div")].find((el) => (el.textContent || "").trim() === "Emergency Fund" && el.children.length === 0);
  if (!h4) return JSON.stringify({err: "no leaf"});
  let card = h4;
  while (card && card !== document.body) {
    const cls = typeof card.className === "string" ? card.className : "";
    if (cls.includes("rounded-xl")) break;
    card = card.parentElement;
  }
  const btns = card ? [...card.querySelectorAll("button")].filter((b) => {
    const r = b.getBoundingClientRect();
    return r.width >= 20 && r.width <= 50 && Math.abs(r.width - r.height) < 8;
  }) : [];
  if (btns.length !== 1) return JSON.stringify({err: "trigger count " + btns.length});
  const t = btns[0];
  const cs = getComputedStyle(t);
  const isFocused = document.activeElement === t;
  return JSON.stringify({
    focused: isFocused,
    fv: isFocused ? t.matches(":focus-visible") : false,
    hoverMatch: t.matches(":hover"),
    opacity: cs.opacity,
    bg: cs.backgroundColor,
    color: cs.color,
    boxShadow: cs.boxShadow,
    transitionDuration: cs.transitionDuration,
  });
})()'

FOCUS_WALK='(async () => {
  // FINDER-BOUNDED REAL keyboard walk: press real Tabs until the active
  // element IS the Emergency Fund trigger (bounded at 30 stops). NEVER
  // presses Enter (the menu opens on Enter/click — out of bounds).
  const h4 = [...document.querySelectorAll("h4, h3, div")].find((el) => (el.textContent || "").trim() === "Emergency Fund" && el.children.length === 0);
  if (!h4) return JSON.stringify({err: "no leaf"});
  let card = h4;
  while (card && card !== document.body) {
    const cls = typeof card.className === "string" ? card.className : "";
    if (cls.includes("rounded-xl")) break;
    card = card.parentElement;
  }
  const btns = card ? [...card.querySelectorAll("button")].filter((b) => {
    const r = b.getBoundingClientRect();
    return r.width >= 20 && r.width <= 50 && Math.abs(r.width - r.height) < 8;
  }) : [];
  if (btns.length !== 1) return JSON.stringify({err: "trigger count " + btns.length});
  const target = btns[0];
  const isTarget = () => document.activeElement === target;
  if (isTarget()) return JSON.stringify({walked: 0, landed: true});
  for (let i = 1; i <= 30; i++) {
    document.activeElement.dispatchEvent(new KeyboardEvent("keydown", {key: "Tab", bubbles: true}));
    // a REAL Tab via the agent-browser press command is driven by the
    // outer loop; this JS only REPORTS the landing state
    return JSON.stringify({walked: -1, landed: isTarget(), note: "outer-loop drives the real Tabs"});
  }
  return JSON.stringify({walked: -1, landed: false});
})()'

LANDING_JS='(async () => {
  // the landing probe: a PLAIN unquoted token (LANDED/NO) — immune to the
  // bash-quoted-JSON escaping that defeats grep on the census reads.
  const h4 = [...document.querySelectorAll("h4, h3, div")].find((el) => (el.textContent || "").trim() === "Emergency Fund" && el.children.length === 0);
  if (!h4) return "NO";
  let card = h4;
  while (card && card !== document.body) {
    const cls = typeof card.className === "string" ? card.className : "";
    if (cls.includes("rounded-xl")) break;
    card = card.parentElement;
  }
  const btns = card ? [...card.querySelectorAll("button")].filter((b) => {
    const r = b.getBoundingClientRect();
    return r.width >= 20 && r.width <= 50 && Math.abs(r.width - r.height) < 8;
  }) : [];
  if (btns.length !== 1) return "NO";
  return document.activeElement === btns[0] ? "LANDED" : "NO";
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="reffocus134"
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
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 5

echo "=== REF: the trigger finder ==="
agent-browser eval "$KEBAB_FINDER" 2>/dev/null | tail -1 | tr -d '"'
echo "=== REF: AT-REST (pointer parked at 5,5) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

echo "=== REF: the REAL-Tab walk (finder-bounded, never Enter) ==="
for i in $(seq 1 30); do
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.3
  LANDED=$(agent-browser eval "$LANDING_JS" 2>/dev/null | tail -1 | tr -d '"')
  if echo "$LANDED" | grep -q "LANDED"; then echo "landed after $i Tabs"; break; fi
done
echo "=== REF: FOCUSED (the real keyboard focus) ==="
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

echo "=== REF: BLURRED (the restore) ==="
agent-browser eval "document.activeElement.blur()" >/dev/null 2>&1
sleep 1
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
KEBAB_FINDER="$KEBAB_FINDER" STATE_JS="$STATE_JS" LANDING_JS="$LANDING_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonefocus134"
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
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 5

echo "=== CLONE: the trigger finder ==="
agent-browser eval "$KEBAB_FINDER" 2>/dev/null | tail -1 | tr -d '"'
echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

echo "=== CLONE: the REAL-Tab walk (finder-bounded, never Enter) ==="
for i in $(seq 1 30); do
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.3
  LANDED=$(agent-browser eval "$LANDING_JS" 2>/dev/null | tail -1 | tr -d '"')
  if echo "$LANDED" | grep -q "LANDED"; then echo "landed after $i Tabs"; break; fi
done
echo "=== CLONE: FOCUSED (the real keyboard focus) ==="
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

echo "=== CLONE: BLURRED (the restore) ==="
agent-browser eval "document.activeElement.blur()" >/dev/null 2>&1
sleep 1
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
echo "=== focusladder arbit v134 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
