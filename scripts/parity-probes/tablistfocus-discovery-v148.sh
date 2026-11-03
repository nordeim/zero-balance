#!/usr/bin/env bash
# tablistfocus-discovery-v148.sh — the DISCOVERY census for the v148
# candidate: the networth tablist trigger FOCUS-VISIBLE composite at
# 390x844 (the never-pinned keyboard path of the pinned tablist family —
# the at-rest chrome pinned at 640/390 by v50/v53, the own-hover INERT
# ladder at 390 by v138, the roving arrow-key path by v30 G2 — the
# focus-visible END-STATE held by NO spec at ANY viewport, ZERO ring
# assertions across the suite). Maps BOTH sides construct (the outline
# family INCLUDING outlineColor [the v148-attempt follow-up lesson:
# the first pass measured the outline geometry without the color and
# could not resolve visibility], the full boxShadow string, the bg/color
# chrome, the geometry) at the three rungs: at-rest (pointer parked
# 5,5), FOCUSED (the REAL focusVisible idiom — focus({focusVisible:
# true}) dispatches NO click; the Radix tabs activate on pointerdown,
# the v120 lesson — READ-ONLY holds), restored (blur). Both triggers
# measured at every rung (the inactive twin the control).
# The v73 heredoc lesson: the QUOTED <<'EOF' with the env-injected census
# JS for the clone half; no literal dollar sequences in the census JS
# (the v64 rule); no apostrophes in the single-quoted census strings
# (the v60 lesson); tr -d '"' on the extraction (the v124 lesson).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS='(async () => {
  const triggers = [...document.querySelectorAll("button[role=tab]")];
  const active = triggers.find((t) => t.getAttribute("aria-selected") === "true");
  const inactive = triggers.find((t) => t.getAttribute("aria-selected") === "false");
  if (!active || !inactive) return JSON.stringify({err: "no tab triggers"});
  const grab = (t) => {
    const cs = getComputedStyle(t);
    const r = t.getBoundingClientRect();
    return {
      focused: document.activeElement === t,
      fv: t.matches(":focus-visible"),
      outlineStyle: cs.outlineStyle,
      outlineColor: cs.outlineColor,
      outlineWidth: cs.outlineWidth,
      outlineOffset: cs.outlineOffset,
      boxShadow: cs.boxShadow,
      bg: cs.backgroundColor,
      color: cs.color,
      w: Math.round(r.width),
      h: Math.round(r.height),
    };
  };
  const out = { view: "tablistfocus-discovery-390-v148" };
  out.atRest = { active: grab(active), inactive: grab(inactive) };
  active.focus({ focusVisible: true });
  await new Promise((res) => setTimeout(res, 450));
  out.activeFocused = { active: grab(active), inactive: grab(inactive) };
  active.blur();
  await new Promise((res) => setTimeout(res, 450));
  out.activeRestored = { active: grab(active), inactive: grab(inactive) };
  inactive.focus({ focusVisible: true });
  await new Promise((res) => setTimeout(res, 450));
  out.inactiveFocused = { active: grab(active), inactive: grab(inactive) };
  inactive.blur();
  await new Promise((res) => setTimeout(res, 450));
  out.inactiveRestored = { active: grab(active), inactive: grab(inactive) };
  return JSON.stringify(out);
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="reftabfocus148"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "$REF/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== REF: the tablist triggers focus-visible discovery (390) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1 | tr -d '"'
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
CENSUS_JS="$CENSUS_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonetabfocus148"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 4
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1
echo "=== CLONE: the tablist triggers focus-visible discovery (390) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1 | tr -d '"'
pkill -f "agent-browser" 2>/dev/null
echo "=== tablistfocus discovery v148 done ==="
EOF
