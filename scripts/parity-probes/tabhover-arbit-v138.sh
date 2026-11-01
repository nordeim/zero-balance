#!/usr/bin/env bash
# tabhover-arbit-v138.sh — the ONE-SHOT both-sides census for the v138
# candidate pin family: the NETWORTH TABLIST TRIGGER's OWN-HOVER LADDER
# at mobile 390x844 on /networth — the never-pinned HOVER PATH of the
# pinned networth tablist family (the v5 G3 pin holds the at-rest 2-col
# grid + the active green state; the v30 G2 the ROVING keyboard; the
# v50 F2 the full chrome at 640; the v53 F1 the full chrome at 390 —
# networth.spec.ts's tab censuses are ALL AT-REST, never the hover
# END-STATE; the trigger's own-hover held by NO spec at ANY viewport).
#   the trigger ladder — the at-rest chrome -> the OWN-HOVERED end-state
#   -> the restored at-rest — for BOTH the ACTIVE (Assets) and the
#   INACTIVE (Liabilities) trigger.
# The construct under test: the clone's trigger carries NO hover:
# utility (tabs.tsx:24-38 — the focus-visible + data-[state=active]
# classes alone), so the expected own-hover end-state is the AT-REST
# CHROME PERSISTING (the inert-hover contract, the transition-all
# metadata aside). The reference's trigger: MEASURED (if it carries a
# hover tint the clone lacks, that is a GAP to repair; if inert both
# sides, NO GAP — the PIN-ONLY form).
# BOTH SIDES measured (READ-ONLY — login + passive navigation + REAL
# pointer MOVES only, the v46 rule; the Radix tabs activate on
# pointerdown — the v120 lesson — and a mouse MOVE dispatches no
# pointerdown, so the census can never flip the tab). The hover moves
# the REAL pointer to each trigger's OWN center (the coords read live
# after the settle — never guessed; the mouse move takes x y as TWO
# args — the v123 lesson); the ladder parks at (5,5) first (the v22
# lesson), reads the at-rest state, hovers the ACTIVE trigger, reads,
# hovers the INACTIVE trigger, reads, parks back, and verifies the
# restore. The v73 heredoc lesson: the QUOTED <<'EOF' with the
# env-injected census JS for the clone half; no literal dollar
# sequences in the census JS (the v64 rule); no single quotes inside
# the single-quoted census strings (the v60 lesson); the plain
# comma-pair center return (the v116 convention); tr -d '"' on the
# extraction (the v124 lesson); ROLE-BASED finders (the v53 form —
# button[role=tab] + aria-selected, shared by both Radix sites).
set -u
cd "$(dirname "$0")/../.."

ACTIVE_CENTER_JS='(async () => {
  const triggers = [...document.querySelectorAll("button[role=tab]")];
  const active = triggers.find((t) => t.getAttribute("aria-selected") === "true");
  if (!active) return JSON.stringify({err: "no active trigger"});
  active.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = active.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

INACTIVE_CENTER_JS='(async () => {
  const triggers = [...document.querySelectorAll("button[role=tab]")];
  const inactive = triggers.find((t) => t.getAttribute("aria-selected") === "false");
  if (!inactive) return JSON.stringify({err: "no inactive trigger"});
  inactive.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = inactive.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

STATE_JS='(async () => {
  const triggers = [...document.querySelectorAll("button[role=tab]")];
  const active = triggers.find((t) => t.getAttribute("aria-selected") === "true");
  const inactive = triggers.find((t) => t.getAttribute("aria-selected") === "false");
  if (!active || !inactive) return JSON.stringify({err: "triggers " + triggers.length});
  const grab = (t) => {
    const cs = getComputedStyle(t);
    const r = t.getBoundingClientRect();
    const icon = t.querySelector("svg");
    return {
      hoverMatch: t.matches(":hover"),
      bg: cs.backgroundColor,
      color: cs.color,
      shadow: cs.boxShadow,
      border: cs.border,
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
  return JSON.stringify({ active: grab(active), inactive: grab(inactive) });
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="reftab138"
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
sleep 5

echo "=== REF: the trigger centers (live, never guessed) ==="
ACENTER="$(agent-browser eval "$ACTIVE_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
ICENTER="$(agent-browser eval "$INACTIVE_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "active center: $ACENTER / inactive center: $ICENTER"
ACX="${ACENTER%,*}"; ACY="${ACENTER#*,}"
ICX="${ICENTER%,*}"; ICY="${ICENTER#*,}"
if [ -z "$ACX" ] || [ -z "$ACY" ] || [ -z "$ICX" ] || [ -z "$ICY" ]; then echo "FINDER FAILED on REF"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$ACX" "$ACY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: ACTIVE-HOVERED (real pointer at the Assets trigger center $ACX,$ACY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$ICX" "$ICY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: INACTIVE-HOVERED (real pointer at the Liabilities trigger center $ICX,$ICY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
ACTIVE_CENTER_JS="$ACTIVE_CENTER_JS" INACTIVE_CENTER_JS="$INACTIVE_CENTER_JS" STATE_JS="$STATE_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonetab138"
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
agent-browser set viewport 390 844 >/dev/null 2>&1
sleep 1
agent-browser open "http://localhost:3200/networth" >/dev/null 2>&1
sleep 5

echo "=== CLONE: the trigger centers (live, never guessed) ==="
ACENTER="$(agent-browser eval "$ACTIVE_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
ICENTER="$(agent-browser eval "$INACTIVE_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "active center: $ACENTER / inactive center: $ICENTER"
ACX="${ACENTER%,*}"; ACY="${ACENTER#*,}"
ICX="${ICENTER%,*}"; ICY="${ICENTER#*,}"
if [ -z "$ACX" ] || [ -z "$ACY" ] || [ -z "$ICX" ] || [ -z "$ICY" ]; then echo "FINDER FAILED on CLONE"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$ACX" "$ACY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: ACTIVE-HOVERED (real pointer at the Assets trigger center $ACX,$ACY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$ICX" "$ICY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: INACTIVE-HOVERED (real pointer at the Liabilities trigger center $ICX,$ICY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
echo "=== tabhover arbit v138 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
