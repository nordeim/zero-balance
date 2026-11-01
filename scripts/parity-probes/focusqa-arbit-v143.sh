#!/usr/bin/env bash
# focusqa-arbit-v143.sh — the ONE-SHOT both-sides census for the v143
# candidate pin family: the DASHBOARD QUICK-ACTION CARDS' FOCUS-VISIBLE
# LADDER at desktop 1280x800 (the v137-era DASHBOARD pair's own surface —
# the Quick-Action row below the fold) — the never-pinned KEYBOARD PATH of
# the pinned quick-action family (the v45 F3b pin holds the card's
# hover:shadow-lg layers ONLY; the v61 F3 + v107 pins the AT-REST chrome;
# the v95 pin the transition TIMING metadata; the v125 pin the HOVER
# end-state ladder [the tile scale + the plus opacity] — the focus-visible
# ring + the focused card's UNCHANGED chrome held by NO spec at ANY
# viewport — verified by the suite-wide survey [dashboard.spec.ts's focus
# pins cover the header Add Item button (v35 S2) + the Tab-order
# structural walk (v40 F1); no spec asserts the QA cards' ring]; the stat
# cards' focus path is SUPERSET-only [the reference's are inert divs —
# the v40 census], not a both-sides axis; the QA cards are real BUTTONS
# on BOTH sites [the v40 walk: the three quick-action cards are stops on
# both sides]).
#   the ladder — the at-rest chrome -> the FOCUSED end-state
#   (focusVisible:true — the REAL Chromium FocusOptions member, the v35
#   S2 idiom; the v25 plain-focus lesson does not apply to the
#   focusVisible form) -> the blurred restore.
# The construct under test: the cards carry NO focus classes on the clone
# (dashboard-view.tsx:885 — group rounded-2xl border p-6 text-left
# transition-all duration-200 hover:shadow-lg), so the expected focused
# end-state is the UA-DEFAULT RING contract (the engine's own focus ring,
# identical on both sites running the same Chromium) + the UNCHANGED
# card chrome under focus (the shadow-lg is :hover-only — focus != hover;
# the tile scale + the plus opacity are group-hover-only — both stay
# at-rest under focus). The reference's cards measured live — the census
# documents whichever contract its side renders.
# BOTH SIDES measured (READ-ONLY — passive navigation only, NO clicks:
# the QA cards open the Add Item dialog on click, OUT OF BOUNDS under the
# v46 rule; focus() dispatches no click). The v73 heredoc lesson: the
# QUOTED <<'EOF' with the env-injected census JS for the clone half; no
# literal dollar sequences in the census JS (the v64 rule); tr -d '"'
# on the extraction (the v124 lesson); STRUCTURAL finder (the button
# whose trimmed text starts with "Add Income" — both sites' first QA
# card, the v125 pin's own finder family).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS='(async () => {
  const btn = [...document.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith("Add Income"));
  if (!btn) return JSON.stringify({err: "no card"});
  btn.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const tile = [...btn.querySelectorAll("span, div")].find(s => {
    const t = getComputedStyle(s);
    const r = s.getBoundingClientRect();
    return t.borderRadius === "12px" && r.width >= 30 && r.width <= 60 && r.height >= 30 && r.height <= 60;
  });
  const plus = [...btn.querySelectorAll("svg")].filter(sv => {
    const r = sv.getBoundingClientRect();
    return r.width <= 20 && r.height <= 20;
  }).pop();
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
      tileScale: tile ? getComputedStyle(tile).scale : null,
      plusOpacity: plus ? getComputedStyle(plus).opacity : null
    };
  };
  return JSON.stringify(rd(btn));
})()'

FOCUS_JS='(async () => {
  const btn = [...document.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith("Add Income"));
  if (!btn) return "no card";
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
export AGENT_BROWSER_SESSION="refqa143"
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
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== REF: AT-REST (no focus, pointer parked at 5,5) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== REF: FOCUSED (focusVisible:true on the Add Income card) ==="
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
export AGENT_BROWSER_SESSION="cloneqa143"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== CLONE: AT-REST (no focus, pointer parked at 5,5) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: FOCUSED (focusVisible:true on the Add Income card) ==="
agent-browser eval "$FOCUS_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: BLURRED (the restore) ==="
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== focusqa arbit v143 done ==="
