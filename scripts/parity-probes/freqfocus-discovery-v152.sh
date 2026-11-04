#!/usr/bin/env bash
# freqfocus-discovery-v152.sh — the ONE-SHOT both-sides census for the
# v152 candidate pin family: the SAVINGS FILTER-CARD FREQUENCY SELECT
# TRIGGER's FOCUS-VISIBLE LADDER at desktop 1280x800 (the v146-era
# SAVINGS pair's own surface — the /savings view) — the never-pinned
# KEYBOARD PATH of the pinned filter-card Select family's FREQUENCY
# SIBLING (the sibling-completion form, the v149/v150/v151 precedent:
# the v37 S1 pin closed the CATEGORY trigger's focus-visible family at
# 1280 on /income [the REAL-Tab walk, the 1px #0a0a0a ring + ambient +
# untinted border + 216x36]; THIS census measures the FREQUENCY sibling
# on the savings pair's own /savings surface at the same viewport; the
# v139 pin holds BOTH triggers' OWN-HOVER ladders — the INERT-HOVER
# contract, hover only, NOT focus; the v64/v70 censuses hold both
# triggers' AT-REST geometry; the frequency trigger's FOCUSED state
# held by NO spec at ANY viewport — verified by the suite-wide survey
# [rg 'frequency' across tests/e2e/*.spec.ts: 19 matches, ZERO
# focus/ladder matches — one badge-color comment + the v139 hover pin;
# the v37 S1 pin is the CATEGORY sibling only]; the trigger is a real
# combobox BUTTON on BOTH sites [the same filter-card family the v37
# cycle measured live at 1280 on /income]).
#   the ladder — the at-rest chrome -> the FOCUSED end-state
#   (focusVisible:true — the REAL Chromium FocusOptions member, the v35
#   S2 idiom; the v25 plain-focus lesson does not apply to the
#   focusVisible form) -> the blurred restore.
# The construct under test: the clone's frequency trigger carries the
# shadcn select.tsx construct (focus:outline-none focus:ring-1
# focus:ring-ring — the 1px #0a0a0a ring layered over the ambient
# shadow-sm family, the border untinted, the geometry unchanged). The
# reference's trigger measured live — the census documents whichever
# contract its side renders (the anticipated form: the v148
# tablist-trigger invisible-construct class — the reference's v3
# transparent-outline + white-lead composite vs the clone's v4
# none-outline + transparent-lead composite, every lead invisible by
# construction, the VISIBLE ring composite the assertable family).
# BOTH SIDES measured (READ-ONLY — passive navigation only, NO clicks:
# the trigger opens the Select dropdown on click, OUT OF BOUNDS under
# the v46 rule; focus() dispatches no click). The v73 heredoc lesson:
# the QUOTED <<'EOF' with the env-injected census JS for the clone
# half; no literal dollar sequences in the census JS (the v64 rule);
# STRUCTURAL finder (the v139 convention: the button[role=combobox] whose
# trimmed text startsWith "All Frequencies" — the reference's triggers
# carry NO aria-labels, located by their text "All Categories"/
# "All Frequencies"; the clone's carry the aria-labels — the a11y
# superset).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS='(async () => {
  const trig = [...document.querySelectorAll("button[role=combobox]")].find(b => (b.textContent||"").trim().startsWith("All Frequencies"));
  if (!trig) return JSON.stringify({err: "no frequency trigger"});
  trig.scrollIntoView({ block: "center" });
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
      borderColor: cs.borderColor,
      borderWidth: cs.borderWidth,
      w: el.offsetWidth,
      h: el.offsetHeight
    };
  };
  return JSON.stringify(rd(trig));
})()'

FOCUS_JS='(async () => {
  const trig = [...document.querySelectorAll("button[role=combobox]")].find(b => (b.textContent||"").trim().startsWith("All Frequencies"));
  if (!trig) return "no frequency trigger";
  trig.focus({ focusVisible: true });
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
export AGENT_BROWSER_SESSION="reffreq152"
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
echo "=== REF: FOCUSED (focusVisible:true on the frequency trigger) ==="
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
export AGENT_BROWSER_SESSION="clonefreq152"
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
echo "=== CLONE: FOCUSED (focusVisible:true on the frequency trigger) ==="
agent-browser eval "$FOCUS_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: BLURRED (the restore) ==="
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== freqfocus discovery v152 done ==="
