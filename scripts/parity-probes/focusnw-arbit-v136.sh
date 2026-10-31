#!/usr/bin/env bash
# focusnw-arbit-v136.sh — the ONE-SHOT both-sides census for the v136
# candidate pin family: the NETWORTH ASSET-CARD KEBAB-TRIGGER's
# FOCUS-VISIBLE LADDER at desktop 1280x800 on /networth — the never-pinned
# KEYBOARD path of the pinned reveal family on the networth file
# (net-worth-view.tsx:82 asset + :192 liability twins):
#   the v46 F2 pin the AT-REST opacity-0 + the CARD-hover group-hover
#   reveal at 640/390; the v124 pin the OPEN+parked state at 1280; the
#   v130 pin the OWN-HOVER tint ladder at 1280; the v132 pin the BADGE
#   own-hover at 390; the v36 S3 pin the keyboard reveal on /INCOME —
#   a DIFFERENT FILE (item-card.tsx:139), {fv, opacity} alone, NEVER the
#   ring; the v134 pin the focus ladder on /savings (item-card.tsx again —
#   the different-file immunity precedent); the networth twins' keyboard
#   path — the ring + the outline form + the reveal — held by NO spec at
#   ANY viewport.
#   the ladder — the at-rest rung (pointer parked at 5,5: opacity 0, bg
#   transparent, no ring) -> the REAL-TAB-FOCUSED rung (a REAL keyboard
#   walk to the trigger: the computed ring + the outline form + the reveal
#   state + the bg) -> the blurred rung (restored).
# The finder = the v130 STRUCTURAL form (the lg:grid-cols-3 asset grid ->
# the first card -> the textless single-svg square button — the reference's
# own asset grid carries the identical utility family, the v46 both-sides
# verification; the trigger is UNLABELLED on the reference — the geometric
# form, the v107 tag-agnostic lesson; the landing finder accepts opacity 0
# OR 1 so the focused trigger stays findable mid-walk).
# BOTH SIDES measured (READ-ONLY — login + passive navigation + a REAL
# keyboard walk only, the v46 rule; the Tab walk reveals chrome, it clicks
# nothing and NEVER presses Enter — the menu opens on click/Enter, both
# out of bounds — the net-worth kebab flow is NEVER safe to probe past
# the menu open: the menu's Delete click IS the delete, the v124 rule).
# The walk is FINDER-BOUNDED (press Tab until the active element IS the
# target trigger — never a hardcoded count). The ladder parks at (5,5)
# first (the v22 lesson); the PLAIN unquoted landing token (the v134
# lesson); tr -d '"' on the extraction (the v124 lesson); the v73 heredoc
# lesson: the QUOTED <<'EOF' with the env-injected census JS for the clone
# half; no literal dollar sequences in the census JS (the v64 rule).
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
      (getComputedStyle(b).opacity === "0" || getComputedStyle(b).opacity === "1");
  });
  if (!trigger) return JSON.stringify({err: "no trigger", btnCount: buttons.length});
  const r = trigger.getBoundingClientRect();
  return JSON.stringify({found: true, x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2), w: Math.round(r.width), h: Math.round(r.height)});
})()'

STATE_JS='(async () => {
  const grid = [...document.querySelectorAll("div")].find((d) => {
    if (!d.className || typeof d.className !== "string") return false;
    return d.className.includes("lg:grid-cols-3") && d.children.length >= 1 && getComputedStyle(d).display === "grid";
  });
  if (!grid) return JSON.stringify({err: "no grid"});
  const card = grid.children[0];
  const buttons = card ? [...card.querySelectorAll("button")] : [];
  const t = buttons.find((b) => {
    const x = (b.textContent || "").trim();
    return x === "" && b.querySelectorAll("svg").length === 1 &&
      (getComputedStyle(b).opacity === "0" || getComputedStyle(b).opacity === "1");
  });
  if (!t) return JSON.stringify({err: "no trigger"});
  const cs = getComputedStyle(t);
  const isFocused = document.activeElement === t;
  return JSON.stringify({
    view: "nwkebab-focus-1280-v136",
    focused: isFocused,
    fv: isFocused ? t.matches(":focus-visible") : false,
    opacity: cs.opacity,
    bg: cs.backgroundColor,
    color: cs.color,
    boxShadow: cs.boxShadow,
    outlineStyle: cs.outlineStyle,
    outlineWidth: cs.outlineWidth,
    outlineColor: cs.outlineColor,
    outlineOffset: cs.outlineOffset,
    transitionDuration: cs.transitionDuration,
  });
})()'

LANDING_JS='(async () => {
  const grid = [...document.querySelectorAll("div")].find((d) => {
    if (!d.className || typeof d.className !== "string") return false;
    return d.className.includes("lg:grid-cols-3") && d.children.length >= 1 && getComputedStyle(d).display === "grid";
  });
  if (!grid) return "NO";
  const card = grid.children[0];
  const buttons = card ? [...card.querySelectorAll("button")] : [];
  const t = buttons.find((b) => {
    const x = (b.textContent || "").trim();
    return x === "" && b.querySelectorAll("svg").length === 1 &&
      (getComputedStyle(b).opacity === "0" || getComputedStyle(b).opacity === "1");
  });
  return t && document.activeElement === t ? "LANDED" : "NO";
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="reffocusnw136"
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
sleep 5

echo "=== REF: the trigger finder ==="
agent-browser eval "$TRIGGER_FINDER" 2>/dev/null | tail -1 | tr -d '"'
echo "=== REF: AT-REST (pointer parked at 5,5) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

echo "=== REF: the REAL-Tab walk (finder-bounded, never Enter) ==="
for i in $(seq 1 40); do
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
TRIGGER_FINDER="$TRIGGER_FINDER" STATE_JS="$STATE_JS" LANDING_JS="$LANDING_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonefocusnw136"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
LOGIN_JS="(async () => {
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
for attempt in 1 2 3 4; do
  RESULT=$(agent-browser eval "$LOGIN_JS" 2>/dev/null | tail -1)
  echo "clone login attempt $attempt: $RESULT"
  if echo "$RESULT" | grep -q "submitted"; then break; fi
  agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
  sleep 3
done
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 5

echo "=== CLONE: the trigger finder ==="
agent-browser eval "$TRIGGER_FINDER" 2>/dev/null | tail -1 | tr -d '"'
echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

echo "=== CLONE: the REAL-Tab walk (finder-bounded, never Enter) ==="
for i in $(seq 1 40); do
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
pkill -f "agent-browser" 2>/dev/null
echo "=== focusnw arbit v136 done ==="
EOF
