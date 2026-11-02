#!/usr/bin/env bash
# addfocus-arbit-v146.sh — the ONE-SHOT both-sides census for the v146
# candidate pin family: the ITEMS VIEW PAGE-HEADER ADD SAVINGS button's
# FOCUS-VISIBLE LADDER at desktop 1280x800 (the v140-era SAVINGS pair's own
# surface — the /savings view, the v58-era pair's own surface) — the never-pinned
# KEYBOARD PATH of the pinned Add-button family (the v65 pin holds the
# AT-REST chrome on the header row at 1280 [150×36, 6px radius, 8px/16px
# pad, 14px-500, white, the blue→blueLight gradient rgb(44,95,124)→rgb(59,126,161),
# the zb-btn-add family, the 16×16 plus icon]; the session-5/tokens pins hold the
# AT-REST gradient + the HOVER no-fade family [opacity stays 1 — the v11
# G4 contract, tokens.spec.ts:546]; the v11 G2c composite — the white
# zero-spread lead + the 1px #0a0a0a ring + the variant's ambient — pinned
# ONLY on the DIFFERENT-ELEMENT dashboard header Add Item button at 1280
# [the v35 S2 single-rung form] + the networth Add Asset button at 390
# [the v144 ladder] + the income header Add Income button at 1280
# [the v145 ladder]; the savings header Add Savings button's focused state
# held by NO spec at ANY viewport — verified by the suite-wide survey [rg
# 'Add Savings' across tests/e2e/*.spec.ts: 10 matches, ZERO focus/ladder
# matches — every one at-rest chrome [items.spec.ts:855 the blue gradient],
# click-through [dashboard.spec.ts:221], or text-list/quick-action
# assertions — NONE a focus pin]; the button is a real BUTTON on BOTH sites
# [the v65 cycle measured the reference's own savings header Add button
# live at 1280].
#   the ladder — the at-rest chrome -> the FOCUSED end-state
#   (focusVisible:true — the REAL Chromium FocusOptions member, the v35
#   S2 idiom; the v25 plain-focus lesson does not apply to the
#   focusVisible form) -> the blurred restore.
# The construct under test: the clone's Add Savings button carries the
# .zb-btn-add family (items-view.tsx:154 — the page-header button,
# className="zb-btn-add shrink-0" with the inline blue→blueLight
# gradient [ADD_BUTTON_GRADIENTS.savings]) so the expected focused end-state is the globals.css v11 G2c
# COMPOSITE — outline 2px TRANSPARENT + offset 2px (v3's outline-none
# form) + the FOUR-layer box-shadow (the white zero-spread lead + the
# shadcn 1px #0a0a0a ring + the gradient family's two ambient layers) —
# with the GRADIENT + opacity UNCHANGED under focus (the v11 G4
# no-hover-fade family: opacity stays 1; focus != hover). The reference's
# button measured live — the census documents whichever contract its side
# renders.
# BOTH SIDES measured (READ-ONLY — passive navigation only, NO clicks:
# the button opens the Add Item dialog on click, OUT OF BOUNDS under the
# v46 rule; focus() dispatches no click). The v73 heredoc lesson: the
# QUOTED <<'EOF' with the env-injected census JS for the clone half; no
# literal dollar sequences in the census JS (the v64 rule); STRUCTURAL
# finder (the v109 census's own finder family — main button, trimmed
# text startsWith 'Add', top < 200 — the page-header Add Savings button).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS='(async () => {
  const btn = [...document.querySelectorAll("main button")].find(b => (b.textContent||"").trim().startsWith("Add") && b.getBoundingClientRect().top < 200);
  if (!btn) return JSON.stringify({err: "no button"});
  btn.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const rd = (el) => {
    const cs = getComputedStyle(el);
    return {
      focused: document.activeElement === el,
      fv: el.matches(":focus-visible"),
      outlineStyle: cs.outlineStyle,
      outlineColor: cs.outlineColor,
      outlineWidth: cs.outlineWidth,
      outlineOffset: cs.outlineOffset,
      boxShadow: cs.boxShadow,
      opacity: cs.opacity,
      background: cs.backgroundImage
    };
  };
  return JSON.stringify(rd(btn));
})()'

FOCUS_JS='(async () => {
  const btn = [...document.querySelectorAll("main button")].find(b => (b.textContent||"").trim().startsWith("Add") && b.getBoundingClientRect().top < 200);
  if (!btn) return "no button";
  btn.focus({ focusVisible: true });
  await new Promise((r) => setTimeout(r, 450));
  return "focused";
})()'

BLUR_JS='(async () => {
  if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
  await new Promise((r) => setTimeout(r, 450));
  return "blurred";
})()'

# ---------- REFERENCE half (direct, logged-in) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refadd146"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser eval "(async () => {
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
})()" 2>/dev/null | tail -1
sleep 4
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== REF: AT-REST (no focus, pointer parked at 5,5) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== REF: FOCUSED (focusVisible:true on the Add Savings button) ==="
agent-browser eval "$FOCUS_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== REF: BLURRED (the restore) ==="
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
CENSUS_JS="$CENSUS_JS" FOCUS_JS="$FOCUS_JS" BLUR_JS="$BLUR_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneadd146"
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
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== CLONE: AT-REST (no focus, pointer parked at 5,5) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: FOCUSED (focusVisible:true on the Add Savings button) ==="
agent-browser eval "$FOCUS_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: BLURRED (the restore) ==="
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== addfocus arbit v146 done ==="
