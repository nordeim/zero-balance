#!/usr/bin/env bash
# addfocus-arbit-v144.sh — the ONE-SHOT both-sides census for the v144
# candidate pin family: the NETWORTH ADD ASSET button's FOCUS-VISIBLE
# LADDER at mobile 390x844 (the v138-era MOBILE-TWINS pair's own surface —
# the /networth view, the v63-era twin) — the never-pinned KEYBOARD PATH of
# the pinned Add-Asset family (the v5 pin holds the GRADIENT at-rest; the
# v94 F4 pin the at-rest chrome on the section row at 1280 [36x134, the
# zb-btn-add family]; the v11 G2c composite — the white zero-spread lead +
# the 1px #0a0a0a ring + the variant's ambient — pinned ONLY on the
# DIFFERENT-ELEMENT dashboard header Add Item button at 1280 [the v35 S2
# single-rung form]; the networth Add Asset button's focused state held by
# NO spec at ANY viewport — verified by the suite-wide survey [rg 'Add
# Asset' across tests/e2e/*.spec.ts: zero hover/focus/ladder matches; the
# v35 S2 pin is the dashboard header instance; the v40 F1 Tab-walk's
# networth stops are structural axes only]; the button is a real BUTTON on
# BOTH sites [the v94 cycle measured the reference's own Add Asset button
# live at 1280]).
#   the ladder — the at-rest chrome -> the FOCUSED end-state
#   (focusVisible:true — the REAL Chromium FocusOptions member, the v35
#   S2 idiom; the v25 plain-focus lesson does not apply to the
#   focusVisible form) -> the blurred restore.
# The construct under test: the clone's Add Asset button carries the
# .zb-btn-add family (net-worth-view.tsx:427 — the section-header button,
# the FIRST 'Add Asset' button in DOM order; the empty-state twin renders
# only when assets.length === 0, NOT the case on either site) with the
# inline gradient background, so the expected focused end-state is the
# globals.css v11 G2c COMPOSITE — outline 2px TRANSPARENT + offset 2px
# (v3's outline-none form) + the FOUR-layer box-shadow (the white
# zero-spread lead + the shadcn 1px #0a0a0a ring + the gradient family's
# two ambient layers) — with the GRADIENT + opacity UNCHANGED under focus
# (the v11 G4 no-hover-fade family: opacity stays 1; focus != hover). The
# reference's button measured live — the census documents whichever
# contract its side renders.
# BOTH SIDES measured (READ-ONLY — passive navigation only, NO clicks:
# the button opens the Add Asset dialog on click, OUT OF BOUNDS under the
# v46 rule; focus() dispatches no click). The v73 heredoc lesson: the
# QUOTED <<'EOF' with the env-injected census JS for the clone half; no
# literal dollar sequences in the census JS (the v64 rule); STRUCTURAL
# finder (the button whose trimmed text starts with 'Add Asset' — both
# sites' Assets section-header button, the v94 census's own finder
# family).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS='(async () => {
  const btn = [...document.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith("Add Asset"));
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
  const btn = [...document.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith("Add Asset"));
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
export AGENT_BROWSER_SESSION="refadd144"
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
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== REF: AT-REST (no focus, pointer parked at 5,5) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== REF: FOCUSED (focusVisible:true on the Add Asset button) ==="
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
export AGENT_BROWSER_SESSION="cloneadd144"
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
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== CLONE: AT-REST (no focus, pointer parked at 5,5) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: FOCUSED (focusVisible:true on the Add Asset button) ==="
agent-browser eval "$FOCUS_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: BLURRED (the restore) ==="
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== addfocus arbit v144 done ==="
