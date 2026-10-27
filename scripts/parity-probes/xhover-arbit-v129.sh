#!/usr/bin/env bash
# xhover-arbit-v129.sh — the ONE-SHOT both-sides census for the v129
# candidate pin family: the CALCULATOR DIALOG X (CLOSE BUTTON)'s OWN-HOVER
# END-STATE at 1280x800 on /expenses — the never-pinned TINT PATH of the
# pinned close family (the v59 F1 pin holds the X's {w, h} at 1280; the
# v49 F3 pin the {36, 36} at 640; the v53 F2 pin the {29, 36} at 390; the
# v87 pin the at-rest chrome {radius 6px / bg transparent / border 0px /
# display flex} at 1280 — every pinned axis STATIC chrome, the spec's own
# comment; the dialog-buttons v27 G1 pin holds the hover:bg-accent CLASS
# TOKEN on the ITEM-DIALOG X — a DIFFERENT element in a different file).
# The calculator X's OWN hover end-state — the pointer ON the X itself:
# the hover:bg-accent TINT (calculator-dialog.tsx:138) — held by NO spec
# at ANY viewport (every X assertion in the suite an at-rest read or a
# different-file class-token check):
#   the X's ladder — the at-rest state (bg transparent) -> the
#   OWN-HOVERED state (the accent tint rgb(245,245,245)) -> the restored
#   at-rest.
# BOTH SIDES measured (READ-ONLY per the v46 rule: login + hover +
# dialog-open only — the Calculate click OPENS the view-only dialog, no
# data mutation; the hover on the X reveals chrome, it clicks nothing —
# the v125 QA-hover / v127 badge-hover / v128 kebab-hover precedent's own
# form). The dialog opens via the REAL pointer press (mouse move to the
# Calculate center + mouse down + up — the v123 lineage's own form, never
# the synthetic eval click); the panel finder DUAL (the clone's Radix
# [role=dialog] first, the reference's PLAIN FIXED DIV [maxWidth 768px]
# the fallback — the v99 finder-artifact lesson: the reference's dialog
# carries NO role=dialog); the X finder TAG-AGNOSTIC + STRUCTURAL (the
# v87 form: the reference's X lost its accessible name — NEVER by
# aria-label alone; the geometric fallback finds the 36x36 button in the
# panel's top band on either side's DOM); the hover moves the REAL
# pointer to the X's live-read center (the coords read live after the
# dialog settle — never guessed; the mouse move takes x y as TWO args —
# the v123 lesson); the ladder parks at (5,5) FIRST — BEFORE the state
# reads — so the at-rest read is clean (the v22 lesson); the plain
# comma-pair center return (the v116 convention); tr -d '"' on the
# extraction (the v124 lesson); the v73 heredoc lesson: the QUOTED
# <<'EOF' with the env-injected census JS for the clone half; no literal
# dollar sequences in the census JS (the v64 rule); no single quotes
# inside single-quoted strings (the v60 lesson).
set -u
cd "$(dirname "$0")/../.."

PANEL_FINDER='const panel = [...document.querySelectorAll("[role=dialog]")].find((d) => /Rent Calculator/i.test((d.innerText || ""))) ||
  [...document.querySelectorAll("div")].find((d) => getComputedStyle(d).maxWidth === "768px" && d.getBoundingClientRect().width > 300);'

X_FINDER="(async () => {
  ${PANEL_FINDER}
  if (!panel) return JSON.stringify({err: \"no Rent Calculator panel\"});
  const btns = [...panel.querySelectorAll(\"button\")];
  const close =
    btns.find((b) => (b.getAttribute(\"aria-label\") || \"\") === \"Close\") ||
    btns.find((b) => {
      const r = b.getBoundingClientRect();
      return (
        Math.abs(r.width - 36) < 3 &&
        Math.abs(r.height - 36) < 3 &&
        r.top < panel.getBoundingClientRect().top + 80 &&
        !/^add item\$/i.test((b.textContent || \"\").trim()));
    });
  if (!close) return JSON.stringify({err: \"no X found\"});
  const r = close.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + \",\" + Math.round(r.y + r.height / 2);
})()"

STATE_JS="(async () => {
  ${PANEL_FINDER}
  if (!panel) return JSON.stringify({err: \"no panel in state read\"});
  const btns = [...panel.querySelectorAll(\"button\")];
  const close =
    btns.find((b) => (b.getAttribute(\"aria-label\") || \"\") === \"Close\") ||
    btns.find((b) => {
      const r = b.getBoundingClientRect();
      return (
        Math.abs(r.width - 36) < 3 &&
        Math.abs(r.height - 36) < 3 &&
        r.top < panel.getBoundingClientRect().top + 80 &&
        !/^add item\$/i.test((b.textContent || \"\").trim()));
    });
  if (!close) return JSON.stringify({err: \"no X in state read\"});
  const cs = getComputedStyle(close);
  const r = close.getBoundingClientRect();
  return JSON.stringify({
    hoverMatch: close.matches(\":hover\"),
    bg: cs.backgroundColor,
    color: cs.color,
    radius: cs.borderRadius,
    w: Math.round(r.width),
    h: Math.round(r.height),
    transitionProperty: cs.transitionProperty,
    transitionDuration: cs.transitionDuration,
  });
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
export AGENT_BROWSER_SESSION="refxhover129"
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
echo "=== REF: the X finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$X_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
echo "X center: $CENTER"
CX="${CENTER%,*}"; CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on REF"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: OWN-HOVERED (real pointer at the X center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
X_FINDER="$X_FINDER" STATE_JS="$STATE_JS" OPEN_CALC="$OPEN_CALC" CALC_BTN="$CALC_BTN" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonexhover129"
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
echo "=== CLONE: the X finder + live center (never guessed) ==="
CENTER="$(agent-browser eval "$X_FINDER" 2>/dev/null | tail -1 | tr -d '"')"
echo "X center: $CENTER"
CX="${CENTER%,*}"; CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on CLONE"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: OWN-HOVERED (real pointer at the X center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
echo "=== xhover arbit v129 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
