#!/usr/bin/env bash
# selecthover-arbit-v139.sh — the ONE-SHOT both-sides census for the v139
# candidate pin family: the FILTER-CARD SELECT TRIGGER's OWN-HOVER LADDER
# at desktop 1280x800 on /income (the items pair's own surface) — the
# never-pinned HOVER PATH of the pinned filter family (the v37 S1 pin
# holds the CLOSED category trigger's focus-visible family [the 1px
# #0a0a0a ring + ambient + the untinted border + 216x36]; the v64/v70
# censuses hold the at-rest geometry of BOTH triggers; the v53 F1/v50 F2
# forms hold the mobile/640 chrome — every select census AT-REST, never
# the hover END-STATE; the trigger's own-hover held by NO spec at ANY
# viewport — verified by the suite-wide survey).
#   the trigger ladder — the at-rest chrome -> the OWN-HOVERED end-state
#   -> the restored at-rest — for BOTH the CATEGORY (first) and the
#   FREQUENCY (second) trigger.
# The construct under test: the clone's trigger carries NO hover:
# utility (select.tsx:20-27 — the focus + data-[placeholder] + disabled
# classes alone), so the expected own-hover end-state is the AT-REST
# CHROME PERSISTING (the inert-hover contract, the v138 tablist form).
# The reference's trigger: MEASURED (if it carries a hover tint the
# clone lacks, that is a GAP to repair; if inert both sides, NO GAP —
# the PIN-ONLY form).
# BOTH SIDES measured (READ-ONLY — login + passive navigation + REAL
# pointer MOVES only, the v46 rule; the Radix Select opens on
# pointerdown/enter — the v120 lesson — and a mouse MOVE dispatches no
# pointerdown, so the census can never open the dropdown). The hover
# moves the REAL pointer to each trigger's OWN center (the coords read
# live after the settle — never guessed; the mouse move takes x y as
# TWO args — the v123 lesson); the ladder parks at (5,5) first (the v22
# lesson), reads the at-rest state, hovers the CATEGORY trigger, reads,
# hovers the FREQUENCY trigger, reads, parks back, and verifies the
# restore. The v73 heredoc lesson: the QUOTED <<'EOF' with the
# env-injected census JS for the clone half; no literal dollar
# sequences in the census JS (the v64 rule); no single quotes inside
# the single-quoted census strings (the v60 lesson); the plain
# comma-pair center return (the v116 convention); tr -d '"' on the
# extraction (the v124 lesson); POSITION-BASED finders (button[role=combobox]
# first/second — the reference's triggers carry NO aria-label, identified
# by their text "All Categories"/"All Frequencies"; the clone's carry the
# superset aria-labels — the position form is the ONLY form shared by both
# Radix sites; the text cross-checked in the census output).
set -u
cd "$(dirname "$0")/../.."

FIRST_CENTER_JS='(async () => {
  const triggers = [...document.querySelectorAll("button[role=combobox]")];
  const first = triggers[0];
  if (!first) return JSON.stringify({err: "no category trigger"});
  first.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = first.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

SECOND_CENTER_JS='(async () => {
  const triggers = [...document.querySelectorAll("button[role=combobox]")];
  const second = triggers[1];
  if (!second) return JSON.stringify({err: "no frequency trigger"});
  second.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = second.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

STATE_JS='(async () => {
  const triggers = [...document.querySelectorAll("button[role=combobox]")];
  const cat = triggers[0];
  const freq = triggers[1];
  if (!cat || !freq) return JSON.stringify({err: "triggers " + triggers.length});
  const grab = (t) => {
    const cs = getComputedStyle(t);
    const r = t.getBoundingClientRect();
    const icon = t.querySelector("svg");
    return {
      hoverMatch: t.matches(":hover"),
      text: (t.textContent || "").trim().slice(0, 20),
      bg: cs.backgroundColor,
      color: cs.color,
      shadow: cs.boxShadow,
      borderColor: cs.borderColor,
      borderWidth: cs.borderWidth,
      radius: cs.borderRadius,
      fs: cs.fontSize,
      fw: cs.fontWeight,
      transitionProperty: cs.transitionProperty,
      transitionDuration: cs.transitionDuration,
      w: Math.round(r.width),
      h: Math.round(r.height),
      iconColor: icon ? getComputedStyle(icon).color : null
    };
  };
  return JSON.stringify({ cat: grab(cat), freq: grab(freq) });
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refsel139"
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
agent-browser open "$REF/income" >/dev/null 2>&1
sleep 5

echo "=== REF: the trigger centers (live, never guessed) ==="
FCENTER="$(agent-browser eval "$FIRST_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
SCENTER="$(agent-browser eval "$SECOND_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "category center: $FCENTER / frequency center: $SCENTER"
FCX="${FCENTER%,*}"; FCY="${FCENTER#*,}"
SCX="${SCENTER%,*}"; SCY="${SCENTER#*,}"
if [ -z "$FCX" ] || [ -z "$FCY" ] || [ -z "$SCX" ] || [ -z "$SCY" ]; then echo "FINDER FAILED on REF"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$FCX" "$FCY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: CATEGORY-HOVERED (real pointer at the category trigger center $FCX,$FCY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$SCX" "$SCY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: FREQUENCY-HOVERED (real pointer at the frequency trigger center $SCX,$SCY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
FIRST_CENTER_JS="$FIRST_CENTER_JS" SECOND_CENTER_JS="$SECOND_CENTER_JS" STATE_JS="$STATE_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonesel139"
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
agent-browser open "http://localhost:3200/income" >/dev/null 2>&1
sleep 5

echo "=== CLONE: the trigger centers (live, never guessed) ==="
FCENTER="$(agent-browser eval "$FIRST_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
SCENTER="$(agent-browser eval "$SECOND_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "category center: $FCENTER / frequency center: $SCENTER"
FCX="${FCENTER%,*}"; FCY="${FCENTER#*,}"
SCX="${SCENTER%,*}"; SCY="${SCENTER#*,}"
if [ -z "$FCX" ] || [ -z "$FCY" ] || [ -z "$SCX" ] || [ -z "$SCY" ]; then echo "FINDER FAILED on CLONE"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$FCX" "$FCY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: CATEGORY-HOVERED (real pointer at the category trigger center $FCX,$FCY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$SCX" "$SCY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: FREQUENCY-HOVERED (real pointer at the frequency trigger center $SCX,$SCY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
echo "=== selecthover arbit v139 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
