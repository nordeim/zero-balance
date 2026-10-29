#!/usr/bin/env bash
# itemhover-arbit-v133.sh — the ONE-SHOT both-sides census for the v133
# candidate pin family: the ITEM-CARD ACTION BUTTONS' OWN-HOVER LADDERS at
# desktop 1280x800 on /expenses — the never-pinned HOVER END-STATES of the
# v45-pinned at-rest family (the v45 F1b pin holds the action row's
# at-rest chrome [top/right/gap/btnH/padX/fs] + the buttons' at-rest
# shadow-md + the row's reveal [opacity 0 -> 1 on card hover] + the card's
# INERT hovered shadow; the v28 G2 pin holds the Edit button's
# hover:text-accent-foreground CLASS TOKEN — never the computed END-STATE;
# the hovered tints — Edit bg rgb(249,250,251) + color rgb(23,23,23),
# Calculate bg rgb(255,247,237) — held on THIS FILE by NO spec at ANY
# viewport):
#   the ladder — the at-rest rung (pointer parked at 5,5: both buttons
#   white, row opacity 0) -> the EDIT OWN-HOVERED rung (the real pointer
#   at the Edit button's live center: bg rgb(249,250,251) + color
#   rgb(23,23,23), the row revealed) -> the CALCULATE OWN-HOVERED rung
#   (the pointer at the Calculate button's live center: bg rgb(255,247,237),
#   the orange text unchanged) -> the restored rung (pointer re-parked).
# The target: the FIRST EXPENSE CARD (the grid-cols-3 first child) — the
# same card both sides (the reference's Miscellaneous + the clone's
# Entertainment); the buttons found by TEXT + the state-independent chrome
# guards (radius 6px + fs 12px + h 32 — shared by both sites per the v133
# survey probes: ref Edit 77x32 + Calculate 110x32, clone the same family).
# BOTH SIDES measured (READ-ONLY — login + passive navigation + a REAL
# pointer hover only, the v46 rule; the hover reveals chrome, it clicks
# nothing — the buttons OPEN dialogs on click, never clicked). The hover
# moves the REAL pointer to each button's OWN center (the coords read
# live — never guessed; the mouse move takes x y as TWO args — the v123
# lesson); the ladder parks at (5,5) first (the v22 lesson). The v73
# heredoc lesson: the QUOTED <<'EOF' with the env-injected census JS for
# the clone half; no literal dollar sequences in the census JS (the v64
# rule); tr -d '"' on the extraction (the v124 lesson); TAG-AGNOSTIC
# finders (the v107 lesson).
set -u
cd "$(dirname "$0")/../.."

BTN_FINDER='(async () => {
  // TAG-AGNOSTIC button finder: the first expense card (the grid-cols-3
  // first child), its Edit + Calculate buttons by TEXT + the
  // state-independent chrome guards (radius 6px + fs 12px — shared by
  // both sites per the v133 survey probe).
  const grid = [...document.querySelectorAll("div")].find((d) => typeof d.className === "string" && d.className.includes("grid-cols-3"));
  if (!grid) return JSON.stringify({err: "no grid"});
  const card = grid.children[0];
  const edit = [...card.querySelectorAll("button, [role=button]")].find((b) => (b.textContent || "").trim() === "Edit");
  const calc = [...card.querySelectorAll("button, [role=button]")].find((b) => (b.textContent || "").trim() === "Calculate");
  if (!edit || !calc) return JSON.stringify({err: "buttons missing"});
  const g = (cs) => cs.borderRadius === "6px" && cs.fontSize === "12px";
  if (!g(getComputedStyle(edit)) || !g(getComputedStyle(calc))) return JSON.stringify({err: "chrome guards failed"});
  const ec = edit.getBoundingClientRect();
  const cc = calc.getBoundingClientRect();
  return Math.round(ec.x + ec.width / 2) + "," + Math.round(ec.y + ec.height / 2) + ";" + Math.round(cc.x + cc.width / 2) + "," + Math.round(cc.y + cc.height / 2);
})()'

STATE_JS='(async () => {
  const grid = [...document.querySelectorAll("div")].find((d) => typeof d.className === "string" && d.className.includes("grid-cols-3"));
  if (!grid) return JSON.stringify({err: "no grid"});
  const card = grid.children[0];
  const edit = [...card.querySelectorAll("button, [role=button]")].find((b) => (b.textContent || "").trim() === "Edit");
  const calc = [...card.querySelectorAll("button, [role=button]")].find((b) => (b.textContent || "").trim() === "Calculate");
  if (!edit || !calc) return JSON.stringify({err: "buttons missing"});
  let row = edit.parentElement;
  while (row && row !== card) {
    const cs = getComputedStyle(row);
    if (cs.position === "absolute") break;
    row = row.parentElement;
  }
  const rd = (b) => {
    const cs = getComputedStyle(b);
    const r = b.getBoundingClientRect();
    return {hoverMatch: b.matches(":hover"), bg: cs.backgroundColor, color: cs.color, w: Math.round(r.width), h: Math.round(r.height)};
  };
  return JSON.stringify({
    edit: rd(edit), calc: rd(calc),
    rowOpacity: row ? getComputedStyle(row).opacity : null,
    cardHover: card.matches(":hover"),
    transitionDuration: getComputedStyle(edit).transitionDuration,
  });
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refitemhover133"
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
agent-browser open "$REF/expenses" >/dev/null 2>&1
sleep 5

echo "=== REF: the button finders + live centers (never guessed) ==="
CENTERS="$(agent-browser eval "$BTN_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
echo "$CENTERS"
EDIT_C="${CENTERS%;*}"
CALC_C="${CENTERS#*;}"
EX="${EDIT_C%,*}"; EY="${EDIT_C#*,}"
CX2="${CALC_C%,*}"; CY2="${CALC_C#*,}"
if [ -z "$EX" ] || [ -z "$CX2" ]; then echo "FINDER FAILED on REF"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$EX" "$EY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: EDIT OWN-HOVERED (real pointer at the Edit center $EX,$EY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX2" "$CY2" >/dev/null 2>&1
  sleep 1
  echo "=== REF: CALC OWN-HOVERED (real pointer at the Calculate center $CX2,$CY2) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
BTN_FINDER="$BTN_FINDER" STATE_JS="$STATE_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneitemhover133"
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
agent-browser open "http://localhost:3200/expenses" >/dev/null 2>&1
sleep 5

echo "=== CLONE: the button finders + live centers (never guessed) ==="
CENTERS="$(agent-browser eval "$BTN_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
echo "$CENTERS"
EDIT_C="${CENTERS%;*}"
CALC_C="${CENTERS#*;}"
EX="${EDIT_C%,*}"; EY="${EDIT_C#*,}"
CX2="${CALC_C%,*}"; CY2="${CALC_C#*,}"
if [ -z "$EX" ] || [ -z "$CX2" ]; then echo "FINDER FAILED on CLONE"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$EX" "$EY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: EDIT OWN-HOVERED (real pointer at the Edit center $EX,$EY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX2" "$CY2" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: CALC OWN-HOVERED (real pointer at the Calculate center $CX2,$CY2) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
echo "=== itemhover arbit v133 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
