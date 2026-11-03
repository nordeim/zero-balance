#!/usr/bin/env bash
# tabqa2-discovery-v149.sh — the F4 DISCOVERY census for the v149 cycle's
# pin candidate: the remaining two QUICK-ACTION CARDS' FOCUS-VISIBLE
# LADDERS at desktop 1280x800 (the Add Savings + Add Expense cards — the
# never-pinned SIBLINGS of the v143-pinned Add Income card: the v143 pin
# + focusqa-arbit-v143.sh measured the FIRST card only [the structural
# finder: the button whose trimmed text starts with "Add Income"]; the
# suite-wide survey: ZERO focus-visible/ring assertions on the Add
# Savings / Add Expense DASHBOARD quick-action cards across all 24 spec
# files — the items.spec.ts v146 pin covers the SAVINGS page-header Add
# Savings BUTTON [a different element on a different view]; the v35 S2
# pin covers the header Add Item composite; the v125 pin the hover
# ladder; the v61/v107 pins the at-rest chrome).
# The expected form (the v143 contract, the same-component reasoning:
# dashboard-view.tsx renders the three cards from the same component
# with the same className — the ONLY per-card deltas the tile/icon/plus
# COLOR tokens): the UA-default ring contract at the focused rung
# (outlineStyle auto + outlineWidth 1px + outlineOffset 0px) with the
# card chrome UNCHANGED (focus != hover: boxShadow stays none, tileScale
# stays none, plusOpacity stays 0.5) — the ladder measured AT-REST ->
# FOCUSED (focusVisible:true) -> BLURRED, both sides.
# READ-ONLY (passive navigation + focus() only — NO clicks: the QA cards
# open the Add Item dialog on click, OUT OF BOUNDS under the v46 rule;
# focus() dispatches no click). The v73 heredoc lesson: the QUOTED
# <<'EOF' with the env-injected census JS for the clone half; no literal
# dollar sequences in the census JS (the v64 rule); no apostrophes in
# the single-quoted JS strings (the v60 lesson); the pointer parked at
# (5,5) so no hover state contaminates the ladder.
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS='(async () => {
  const read = (label) => {
    const btn = [...document.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith(label));
    if (!btn) return {err: "no " + label};
    const tile = [...btn.querySelectorAll("span, div")].find(s => {
      const t = getComputedStyle(s);
      const r = s.getBoundingClientRect();
      return t.borderRadius === "12px" && r.width >= 30 && r.width <= 60 && r.height >= 30 && r.height <= 60;
    });
    const plus = [...btn.querySelectorAll("svg")].filter(sv => {
      const r = sv.getBoundingClientRect();
      return r.width <= 20 && r.height <= 20;
    }).pop();
    const cs = getComputedStyle(btn);
    const tcs = tile ? getComputedStyle(tile) : null;
    return {
      card: label,
      focused: document.activeElement === btn,
      fv: btn.matches(":focus-visible"),
      outlineStyle: cs.outlineStyle,
      outlineColor: cs.outlineColor,
      outlineWidth: cs.outlineWidth,
      outlineOffset: cs.outlineOffset,
      boxShadow: cs.boxShadow,
      tileScale: tcs ? tcs.scale : null,
      tileBg: tcs ? tcs.backgroundColor : null,
      plusOpacity: plus ? getComputedStyle(plus).opacity : null
    };
  };
  return JSON.stringify({savings: read("Add Savings"), expense: read("Add Expense")});
})()'

FOCUS_JS='(async () => {
  const results = [];
  for (const label of ["Add Savings", "Add Expense"]) {
    const btn = [...document.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith(label));
    if (!btn) { results.push("no " + label); continue; }
    btn.focus({ focusVisible: true });
    await new Promise((r) => setTimeout(r, 450));
    results.push(label + " focused");
    btn.blur();
    await new Promise((r) => setTimeout(r, 450));
  }
  return results.join("; ");
})()'

FOCUS_HOLD_JS='(async () => {
  const btn = [...document.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith("Add Savings"));
  if (!btn) return "no card";
  btn.focus({ focusVisible: true });
  await new Promise((r) => setTimeout(r, 450));
  return "savings focused held";
})()'

FOCUS_HOLD2_JS='(async () => {
  const btn = [...document.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith("Add Expense"));
  if (!btn) return "no card";
  btn.focus({ focusVisible: true });
  await new Promise((r) => setTimeout(r, 450));
  return "expense focused held";
})()'

BLUR_JS='(async () => {
  if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
  await new Promise((r) => setTimeout(r, 450));
  return "blurred";
})()'

# ---------- REFERENCE half (direct, logged-in) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refqa2v149"
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
echo "=== REF: SAVINGS FOCUSED (focusVisible:true) ==="
agent-browser eval "$FOCUS_HOLD_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== REF: EXPENSE FOCUSED (focusVisible:true) ==="
agent-browser eval "$FOCUS_HOLD2_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== REF: BLURRED (the restore) ==="
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

# ---------- CLONE half (with-server, logged-in) ----------
# The QUOTED <<'EOF' with the env-injected census JS (the v73 lesson /
# the v143 focusqa form): the JS variables are passed as ENVIRONMENT
# variables to the child bash so the double-quoted heredoc expansion
# never re-parses the JS bodies' embedded double quotes; the clone login
# carries no dollar sequence (Demo1234!).
echo ""
echo "=== CLONE half ==="
CENSUS_JS="$CENSUS_JS" FOCUS_HOLD_JS="$FOCUS_HOLD_JS" FOCUS_HOLD2_JS="$FOCUS_HOLD2_JS" BLUR_JS="$BLUR_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="cloneqa2v149"
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
echo "=== CLONE: SAVINGS FOCUSED (focusVisible:true) ==="
agent-browser eval "$FOCUS_HOLD_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: EXPENSE FOCUSED (focusVisible:true) ==="
agent-browser eval "$FOCUS_HOLD2_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: BLURRED (the restore) ==="
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== clone discovery done ==="
EOF
echo "=== tabqa2 discovery v149 done ==="
