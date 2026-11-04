#!/usr/bin/env bash
# additemfocus-discovery-v153.sh — the ONE-SHOT both-sides census for the
# v153 candidate pin family: the CALCULATOR DIALOG "Add Item" BUTTON
# FOCUS-VISIBLE LADDER at desktop 1280x800 (the v147-era LOGIN + CALCULATOR
# pair own calculator surface — the Rent Calculator dialog opened on
# /expenses). The never-pinned KEYBOARD PATH of the pinned Add-button
# FAMILY DIALOG INSTANCE (the sibling-completion form, the v149/v150/
# v151/v152 precedent: the family focus ladders held on EVERY page-header
# sibling [the v35 S2 dashboard header Add Item at 1280 — the
# DIFFERENT-ELEMENT quick-action card family; the v144 networth Add Asset
# at 390; the v145 income header Add Income at 1280; the v146 savings
# header Add Savings at 1280; the v150 networth Add Liability at 390; the
# v151 expenses header Add Expense at 1280]; the family CALCULATOR dialog
# member — the zb-btn-add-sm variant inside the Rent Calculator dialog —
# held by NO spec at ANY viewport [the suite-wide survey: rg "Add Item"
# across tests/e2e/*.spec.ts — the focus/ladder matches are the
# DIFFERENT-ELEMENT dashboard quick-action card + the v145/v146/v151
# OUT-OF-BOUNDS comments; the v81 census holds this button AT-REST chrome
# only; the v129 own-hover pin finder EXPLICITLY EXCLUDES it; the v135
# focus pin is the dialog X close button only]; the button is a real
# BUTTON on BOTH sites [the v81 cycle measured the reference own
# calculator Add Item button live at 1280: 110x32, 12px/500, the orange
# gradient, white]).
#   the ladder — the at-rest chrome (the pointer parked at 5,5) -> the
#   FOCUSED end-state (focusVisible:true — the REAL Chromium FocusOptions
#   member, the v35 S2 idiom; the v25 plain-focus lesson does not apply
#   to the focusVisible form) -> the blurred restore.
# The construct under test: the clone Add Item button carries the
# globals.css v11 G2c composite (the .zb-btn-add family sm variant,
# calculator-dialog.tsx:176 — outline 2px TRANSPARENT + offset 2px [v3
# outline-none form] + the FOUR-layer box-shadow: the white zero-spread
# lead + the 1px #0a0a0a ring + the two ambient 0.1 layers, the orange
# gradient + opacity UNCHANGED under focus [the v11 G4 no-hover-fade
# family: focus != hover]). The reference button measured live — the
# census documents whichever contract its side renders (the anticipated
# form: the same v11 G2c composite the v11 cycle measured live on the
# reference own Save Item and Add First Item buttons).
# BOTH SIDES measured. The dialog OPEN path is the standing read-only
# form (the v45/v59/v81 censuses + the v147 arbit halves: the real-mouse
# Rent-card hover + the Calculate click — NO form saves, NO deletes; the
# Add Item button itself NEVER clicked [it opens the line-item modal —
# OUT OF BOUNDS under the v46 rule; focus() dispatches no click]). The
# reference dialog is a PLAIN fixed div (no role=dialog — the documented
# reference class) so the button finder is STRUCTURAL on BOTH sides: the
# unique button whose trimmed text is exactly "Add Item" inside a fixed
# overlay container. The v73 heredoc lesson: the QUOTED <<EOF with the
# env-injected census JS for the clone half; no literal dollar sequences
# in the census JS (the v64 rule); no apostrophes in JS comments (the
# v60 rule).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS='(async () => {
  const inOverlay = (b) => {
    let el = b;
    while (el && el !== document.body) {
      const s = getComputedStyle(el);
      if (s.position === "fixed" || el.getAttribute("role") === "dialog") return true;
      el = el.parentElement;
    }
    return false;
  };
  const btn = [...document.querySelectorAll("button")].find(b => (b.textContent || "").trim() === "Add Item" && inOverlay(b));
  if (!btn) return JSON.stringify({ err: "no calculator Add Item button" });
  btn.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const cs = getComputedStyle(btn);
  const r = btn.getBoundingClientRect();
  return JSON.stringify({
    focused: document.activeElement === btn,
    fv: btn.matches(":focus-visible"),
    outlineStyle: cs.outlineStyle,
    outlineColor: cs.outlineColor,
    outlineWidth: cs.outlineWidth,
    outlineOffset: cs.outlineOffset,
    boxShadow: cs.boxShadow,
    opacity: cs.opacity,
    background: cs.backgroundImage,
    color: cs.color,
    fs: cs.fontSize,
    fw: cs.fontWeight,
    w: Math.round(r.width),
    h: Math.round(r.height)
  });
})()'

FOCUS_JS='(async () => {
  const inOverlay = (b) => {
    let el = b;
    while (el && el !== document.body) {
      const s = getComputedStyle(el);
      if (s.position === "fixed" || el.getAttribute("role") === "dialog") return true;
      el = el.parentElement;
    }
    return false;
  };
  const btn = [...document.querySelectorAll("button")].find(b => (b.textContent || "").trim() === "Add Item" && inOverlay(b));
  if (!btn) return "no calculator Add Item button";
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
export AGENT_BROWSER_SESSION="refadditem153"
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
POS=""
for attempt in 1 2 3 4 5; do
  POS=$(agent-browser eval "(async () => {
    const main = document.querySelector('main')||document.body;
    const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent'));
    if (!card) return 'ERR';
    const r = card.getBoundingClientRect();
    return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
  })()" 2>/dev/null | tail -1 | tr -d '"')
  if [ "$POS" != "ERR" ] && [ -n "$POS" ]; then break; fi
  echo "rent card not ready (attempt $attempt), waiting..."
  sleep 4
done
echo "ref rent card center: $POS"
X=$(echo "$POS" | cut -d, -f1); Y=$(echo "$POS" | cut -d, -f2)
agent-browser mouse move "$X" "$Y" >/dev/null 2>&1
sleep 1
CALC=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
echo "ref calculate button center: $CALC"
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== REF: AT-REST (no focus, pointer parked at 5,5) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== REF: FOCUSED (focusVisible:true on the calculator Add Item button) ==="
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
export AGENT_BROWSER_SESSION="cloneadditem153"
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
POS=""
for attempt in 1 2 3 4 5; do
  POS=$(agent-browser eval "(async () => {
    const main = document.querySelector('main')||document.body;
    const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent'));
    if (!card) return 'ERR';
    const r = card.getBoundingClientRect();
    return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
  })()" 2>/dev/null | tail -1 | tr -d '"')
  if [ "$POS" != "ERR" ] && [ -n "$POS" ]; then break; fi
  echo "rent card not ready (attempt $attempt), waiting..."
  sleep 4
done
echo "clone rent card center: $POS"
X=$(echo "$POS" | cut -d, -f1); Y=$(echo "$POS" | cut -d, -f2)
agent-browser mouse move "$X" "$Y" >/dev/null 2>&1
sleep 1
CALC=$(agent-browser eval "(async () => {
  const main = document.querySelector('main')||document.body;
  const card = [...main.querySelectorAll('div.rounded-xl')].find(c => (c.innerText||'').includes('Rent'));
  if (!card) return 'ERR';
  const btn = [...card.querySelectorAll('button')].find(b => /^Calculate/i.test(b.textContent.trim()));
  if (!btn) return 'NOBTN';
  const r = btn.getBoundingClientRect();
  return Math.round(r.x + r.width/2) + ',' + Math.round(r.y + r.height/2);
})()" 2>/dev/null | tail -1 | tr -d '"')
echo "clone calculate button center: $CALC"
CX=$(echo "$CALC" | cut -d, -f1); CY=$(echo "$CALC" | cut -d, -f2)
agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
sleep 1
agent-browser mouse down >/dev/null 2>&1
sleep 1
agent-browser mouse up >/dev/null 2>&1
sleep 3
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== CLONE: AT-REST (no focus, pointer parked at 5,5) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: FOCUSED (focusVisible:true on the calculator Add Item button) ==="
agent-browser eval "$FOCUS_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: BLURRED (the restore) ==="
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== additemfocus discovery v153 done ==="
