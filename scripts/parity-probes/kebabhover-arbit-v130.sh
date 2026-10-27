#!/usr/bin/env bash
# kebabhover-arbit-v130.sh — the ONE-SHOT both-sides census for the v130
# candidate pin family: the NETWORTH ASSET-CARD KEBAB-TRIGGER's OWN-HOVER
# END-STATE at 1280x800 on /networth — the never-pinned TINT PATH of the
# pinned reveal family on the never-pinned networth file (the v46 F2 pin
# holds the trigger's w/h/at-rest opacity + the CARD-hover reveal ladder
# [the group-hover opacity path, the pointer on the CARD's center — the
# own-hover tint never engaged]; the v36 S3 pin the keyboard focus-visible
# reveal; the v124 pin the OPEN+parked state [the pointer at (5,5), the
# menu open — the own-hover never engaged; the open state's full box chrome
# w/h/radius held there — the V94-COLLISION criterion for THIS pin]; the
# v128 pin the SAME own-hover ladder on the SAVINGS item-card kebab
# [item-card.tsx:139 — a DIFFERENT FILE, the v122-cycle different-file
# immunity precedent]; the v98 pin the menu panel; the dialog-buttons v27
# G1 pin the hover:bg-accent CLASS TOKEN on the DIALOG X — a DIFFERENT
# element in a different file). The trigger's OWN hover end-state — the
# pointer ON the trigger itself: the hover:bg-accent TINT
# (net-worth-view.tsx:82 the asset twin + :192 the liability twin — the
# identical class string) + the hover:text-accent-foreground COLOR + the
# group-hover reveal (the trigger sits INSIDE the card, so the card's
# group-hover engages simultaneously) — held by NO spec at ANY viewport:
#   the trigger's ladder — the at-rest state (opacity 0, bg transparent)
#   -> the OWN-HOVERED state (opacity 1 + the accent tint + the
#   accent-foreground color) -> the restored at-rest.
# BOTH SIDES measured (READ-ONLY — login + passive navigation + a REAL
# pointer hover only, the v46 rule; the hover reveals chrome, it clicks
# nothing — the menu opens on CLICK, the hover alone never opens it —
# the v125 QA-hover / v127 badge-hover / v128 kebab-hover precedent's own
# form; the net-worth kebab flow is NEVER safe to probe past the menu
# open: the menu's Delete click IS the delete — the v124 pin's own note).
# The card finder = the v46 form (the lg:grid-cols-3 asset grid's first
# card — the reference's own asset grid carries the identical utility
# family, the v46 both-sides verification); the trigger finder by computed
# shape (the at-rest opacity-0 textless single-svg button — the v107
# tag-agnostic lesson), never by aria-label. The hover moves the REAL
# pointer to the trigger's OWN live-read center (the coords read live
# after the scrollIntoView — never guessed; the mouse move takes x y as
# TWO args — the v123 lesson); the ladder parks at (5,5) FIRST — BEFORE
# the finder — so the opacity-0 structural finder reads a clean at-rest
# trigger (the v22 lesson); the plain comma-pair center return (the v116
# convention); tr -d '"' on the extraction (the v124 lesson); the v73
# heredoc lesson: the QUOTED <<'EOF' with the env-injected census JS for
# the clone half; no literal dollar sequences in the census JS (the v64
# rule); no single quotes inside the single-quoted census strings (the
# v60 lesson).
set -u
cd "$(dirname "$0")/../.."

TRIGGER_FINDER='(async () => {
  const grid = [...document.querySelectorAll("div")].find((d) => {
    if (!d.className || typeof d.className !== "string") return false;
    return d.className.includes("lg:grid-cols-3") && d.children.length >= 1 && getComputedStyle(d).display === "grid";
  });
  if (!grid) return JSON.stringify({err: "no lg:grid-cols-3 card grid"});
  const card = grid.children[0];
  if (!card) return JSON.stringify({err: "no first card"});
  const buttons = [...card.querySelectorAll("button")];
  const trigger = buttons.find((b) => {
    const t = (b.textContent || "").trim();
    return t === "" && b.querySelectorAll("svg").length === 1 &&
      getComputedStyle(b).opacity === "0" &&
      Math.round(b.getBoundingClientRect().width) < 60;
  });
  if (!trigger) return JSON.stringify({err: "no at-rest trigger"});
  trigger.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = trigger.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

STATE_JS='(async () => {
  const grid = [...document.querySelectorAll("div")].find((d) => {
    if (!d.className || typeof d.className !== "string") return false;
    return d.className.includes("lg:grid-cols-3") && d.children.length >= 1 && getComputedStyle(d).display === "grid";
  });
  if (!grid) return JSON.stringify({err: "no grid in state read"});
  const card = grid.children[0];
  const buttons = [...card.querySelectorAll("button")];
  const trigger = buttons.find((b) =>
    (b.textContent || "").trim() === "" && b.querySelectorAll("svg").length === 1 &&
    Math.round(b.getBoundingClientRect().width) < 60 &&
    Math.round(b.getBoundingClientRect().height) < 60 &&
    (getComputedStyle(b).opacity === "0" || getComputedStyle(b).opacity === "1"));
  if (!trigger) return JSON.stringify({err: "no trigger in state read"});
  const cs = getComputedStyle(trigger);
  const r = trigger.getBoundingClientRect();
  return JSON.stringify({
    hoverMatch: trigger.matches(":hover"),
    cardHover: card.matches(":hover"),
    opacity: cs.opacity,
    bg: cs.backgroundColor,
    color: cs.color,
    radius: cs.borderRadius,
    w: Math.round(r.width),
    h: Math.round(r.height),
    transitionProperty: cs.transitionProperty,
    transitionDuration: cs.transitionDuration,
  });
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refkebabhover130"
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
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4

echo "=== REF: park (5,5) FIRST so the finder reads a clean at-rest trigger ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF: the trigger finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$TRIGGER_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
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
  echo "=== REF: OWN-HOVERED (real pointer at the trigger center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
TRIGGER_FINDER="$TRIGGER_FINDER" STATE_JS="$STATE_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonekebabhover130"
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
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4

echo "=== CLONE: park (5,5) FIRST so the finder reads a clean at-rest trigger ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== CLONE: the trigger finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$TRIGGER_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
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
  echo "=== CLONE: OWN-HOVERED (real pointer at the trigger center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
echo "=== kebabhover arbit v130 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
