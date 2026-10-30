#!/usr/bin/env bash
# focusx-arbit-v135.sh — the ONE-SHOT both-sides census for the v135
# candidate pin family: the CALCULATOR DIALOG X (CLOSE BUTTON)'s
# FOCUS-VISIBLE LADDER at 1280x800 on /expenses — the never-pinned FOCUS
# path of the pinned close family (the v59 F1 pin the X's {w,h} at 1280;
# the v49 F3 pin {36,36} at 640; the v53 F2 pin {29,36} at 390; the v87
# pin the at-rest chrome; the v129 pin the OWN-HOVER tint ladder — every
# pinned axis an at-rest or hover read; the keyboard path held by NO spec
# at ANY viewport on this surface).
# The ladder: park (5,5) FIRST (the v22 lesson) -> AT-REST -> the REAL
# agent-browser-press-Tab walk (FINDER-BOUNDED, never a hardcoded count,
# NEVER Enter — the dialog opens on click/Enter, both out of bounds; the
# v134 focusladder form) -> FOCUSED -> blurred -> RESTORED.
# BOTH SIDES measured (READ-ONLY per the v46 rule: login + dialog-open
# only — the Calculate click OPENS the view-only dialog, no data mutation;
# the Tab presses focus the X, they click nothing). The dialog opens via
# the REAL pointer press (the v123 lineage's form); the panel finder DUAL
# (the clone's Radix [role=dialog] first, the reference's plain
# maxWidth-768px div the fallback — the v99 lesson); the X finder
# TAG-AGNOSTIC + STRUCTURAL (the v87 form: the reference's X lost its
# accessible name — the aria-label first for the CLONE, the geometric
# 36x36-in-the-panel-top fallback for the reference); the landing probe
# returns a PLAIN unquoted token (the v134 lesson); the QUOTED <<'EOF'
# heredoc with the env-injected census JS for the clone half (the v73
# lesson); no literal dollar sequences in the census JS (the v64 rule).
set -u
cd "$(dirname "$0")/../.."

PANEL_FINDER='const panel = [...document.querySelectorAll("[role=dialog]")].find((d) => /Rent Calculator/i.test((d.innerText || ""))) ||
  [...document.querySelectorAll("div")].find((d) => getComputedStyle(d).maxWidth === "768px" && d.getBoundingClientRect().width > 300);'

CLOSE_EL='const btns = [...panel.querySelectorAll("button")];
  const close =
    btns.find((b) => (b.getAttribute("aria-label") || "") === "Close") ||
    btns.find((b) => {
      const r = b.getBoundingClientRect();
      return (
        Math.abs(r.width - 36) < 3 &&
        Math.abs(r.height - 36) < 3 &&
        r.top < panel.getBoundingClientRect().top + 80 &&
        !/^add item$/i.test((b.textContent || "").trim()));
    });'

X_FINDER="(async () => {
  ${PANEL_FINDER}
  if (!panel) return JSON.stringify({err: \"no Rent Calculator panel\"});
  ${CLOSE_EL}
  if (!close) return JSON.stringify({err: \"no X found\"});
  const r = close.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + \",\" + Math.round(r.y + r.height / 2);
})()"

STATE_JS="(async () => {
  ${PANEL_FINDER}
  if (!panel) return JSON.stringify({err: \"no panel in state read\"});
  ${CLOSE_EL}
  if (!close) return JSON.stringify({err: \"no X in state read\"});
  const cs = getComputedStyle(close);
  const r = close.getBoundingClientRect();
  return JSON.stringify({
    w: Math.round(r.width),
    h: Math.round(r.height),
    bg: cs.backgroundColor,
    color: cs.color,
    opacity: cs.opacity,
    fv: close.matches(\":focus-visible\"),
    focused: document.activeElement === close,
    outlineStyle: cs.outlineStyle,
    outlineWidth: cs.outlineWidth,
    outlineColor: cs.outlineColor,
    outlineOffset: cs.outlineOffset,
    boxShadow: cs.boxShadow.slice(0, 120),
  });
})()"

LANDING_JS="(async () => {
  ${PANEL_FINDER}
  if (!panel) return 'NO PANEL';
  ${CLOSE_EL}
  if (!close) return 'NO X';
  return (document.activeElement === close && close.matches(':focus-visible')) ? 'LANDED' : 'NO';
})()"

OPEN_CALC='(async () => {
  const main = document.querySelector("main")||document.body;
  const card = [...main.querySelectorAll("div.rounded-xl")].find((c) => (c.innerText||"").includes("Rent"));
  if (!card) return JSON.stringify({err: "no Rent card"});
  card.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 200));
  const r = card.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

CALC_BTN='(async () => {
  const main = document.querySelector("main")||document.body;
  const card = [...main.querySelectorAll("div.rounded-xl")].find((c) => (c.innerText||"").includes("Rent"));
  if (!card) return JSON.stringify({err: "no Rent card in calc finder"});
  const btn = [...card.querySelectorAll("button")].find((b) => /^Calculate$/i.test((b.textContent||"").trim()));
  if (!btn) return JSON.stringify({err: "no Calculate button"});
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="reffocx135"
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
sleep 4

echo "=== REF: open the Rent calculator (REAL pointer press — dialog-open only) ==="
CARD_CENTER="$(agent-browser eval "$OPEN_CALC" 2>/dev/null | tail -1 | tr -d '"')"
echo "rent card center: $CARD_CENTER"
CCX="${CARD_CENTER%,*}"; CCY="${CARD_CENTER#*,}"
agent-browser mouse move "$CCX" "$CCY" >/dev/null 2>&1
sleep 1
CALC_CENTER="$(agent-browser eval "$CALC_BTN" 2>/dev/null | tail -1 | tr -d '"')"
echo "calculate button center: $CALC_CENTER"
BCX="${CALC_CENTER%,*}"; BCY="${CALC_CENTER#*,}"
agent-browser mouse move "$BCX" "$BCY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3

echo "=== REF: park (5,5) FIRST so the at-rest read is clean ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF: AT-REST (pointer parked at 5,5) ==="
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

echo "=== REF: the REAL Tab walk to the X (finder-bounded, NEVER Enter) ==="
WALK="NO"
for i in $(seq 1 25); do
  L=$(agent-browser eval "$LANDING_JS" 2>/dev/null | tail -1 | tr -d '"')
  if [ "$L" = "LANDED" ]; then WALK="YES(after $i presses)"; break; fi
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.4
done
echo "walk: $WALK"
echo "=== REF: FOCUSED (the REAL keyboard walk) ==="
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
agent-browser eval "(async () => { document.activeElement.blur(); return 'blurred'; })()" >/dev/null 2>&1
sleep 1
echo "=== REF: RESTORED (blurred) ==="
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
X_FINDER="$X_FINDER" STATE_JS="$STATE_JS" LANDING_JS="$LANDING_JS" OPEN_CALC="$OPEN_CALC" CALC_BTN="$CALC_BTN" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonefocx135"
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
sleep 4

echo "=== CLONE: open the Rent calculator (REAL pointer press — dialog-open only) ==="
CARD_CENTER="$(agent-browser eval "$OPEN_CALC" 2>/dev/null | tail -1 | tr -d '"')"
echo "rent card center: $CARD_CENTER"
CCX="${CARD_CENTER%,*}"; CCY="${CARD_CENTER#*,}"
agent-browser mouse move "$CCX" "$CCY" >/dev/null 2>&1
sleep 1
CALC_CENTER="$(agent-browser eval "$CALC_BTN" 2>/dev/null | tail -1 | tr -d '"')"
echo "calculate button center: $CALC_CENTER"
BCX="${CALC_CENTER%,*}"; BCY="${CALC_CENTER#*,}"
agent-browser mouse move "$BCX" "$BCY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3

echo "=== CLONE: park (5,5) FIRST so the at-rest read is clean ==="
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

echo "=== CLONE: the REAL Tab walk to the X (finder-bounded, NEVER Enter) ==="
WALK="NO"
for i in $(seq 1 25); do
  L=$(agent-browser eval "$LANDING_JS" 2>/dev/null | tail -1 | tr -d '"')
  if [ "$L" = "LANDED" ]; then WALK="YES(after $i presses)"; break; fi
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.4
done
echo "walk: $WALK"
echo "=== CLONE: FOCUSED (the REAL keyboard walk) ==="
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
agent-browser eval "(async () => { document.activeElement.blur(); return 'blurred'; })()" >/dev/null 2>&1
sleep 1
echo "=== CLONE: RESTORED (blurred) ==="
agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
echo "=== focusx arbit v135 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
