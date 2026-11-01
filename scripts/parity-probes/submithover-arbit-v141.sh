#!/usr/bin/env bash
# submithover-arbit-v141.sh — the ONE-SHOT both-sides census for the v141
# candidate pin family: the LOGIN SIGN-IN SUBMIT's OWN-HOVER LADDER at
# desktop 1280x800 on /login (the login pair's own surface, logged-out) —
# the never-pinned HOVER PATH of the pinned submit family (the v7 pin
# holds the submit's REST chrome [bg #0f172a, color white, h 48]; the v9
# pin the per-state geometry [h 48/44, fs 14]; the v25 pin the
# focus-visible ring family; the v45 F4 pin the REST shadow-sm; the v135
# survey measured the own-hover tint live on the reference
# [rgb(15,23,42)->rgb(30,41,59)] and confirmed the clone's existing class
# [login-card.tsx:357 hover:bg-[#1e293b]] matches — every submit census
# AT-REST or FOCUS, never the hover END-STATE; the submit's own-hover held
# by NO spec at ANY viewport — verified by the suite-wide survey).
#   the submit ladder — the at-rest chrome -> the OWN-HOVERED end-state
#   -> the restored at-rest.
# The construct under test: the clone's submit carries hover:bg-[#1e293b]
# (login-card.tsx:357 — the ACTIVE hover tint), so the expected own-hover
# end-state is the TINTED contract (the v129 active-hover form: bg
# rgb(30,41,59) under the submit's own hover, the color/shadow family
# unchanged). The reference's submit: MEASURED (if its hovered family
# differs, that is a GAP to repair; if the tint matches both sides, NO
# GAP — the PIN-ONLY form).
# BOTH SIDES measured (READ-ONLY — passive navigation + REAL pointer
# MOVES only, the v46 rule; a mouse MOVE on a button dispatches no click
# and the logged-out surface holds no session to mutate — the census
# cannot change state; the submit is NEVER clicked — a click would submit
# the form). The hover moves the REAL pointer to the submit's OWN center
# (the coords read live after the settle — never guessed; the mouse move
# takes x y as TWO args — the v123 lesson); the ladder parks at (5,5)
# first (the v22 lesson), reads the at-rest state, hovers the submit,
# reads, parks back, and verifies the restore. The v73 heredoc lesson:
# the QUOTED <<'EOF' with the env-injected census JS for the clone half;
# no literal dollar sequences in the census JS (the v64 rule); no single
# quotes inside the single-quoted census strings (the v60 lesson); the
# plain comma-pair center return (the v116 convention); tr -d '"' on the
# extraction (the v124 lesson); STRUCTURAL finder (button[type=submit]
# with the Sign in text — the form shared by both sites; the text
# cross-checked in the census output).
set -u
cd "$(dirname "$0")/../.."

CENTER_JS='(async () => {
  const submit = [...document.querySelectorAll("button[type=submit]")].find((b) => /Sign in/i.test((b.textContent || "").trim()));
  if (!submit) return JSON.stringify({err: "no submit"});
  submit.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = submit.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

STATE_JS='(async () => {
  const submit = [...document.querySelectorAll("button[type=submit]")].find((b) => /Sign in/i.test((b.textContent || "").trim()));
  if (!submit) return JSON.stringify({err: "no submit"});
  const cs = getComputedStyle(submit);
  const r = submit.getBoundingClientRect();
  return JSON.stringify({
    hoverMatch: submit.matches(":hover"),
    txt: (submit.textContent || "").trim().slice(0, 12),
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
    h: Math.round(r.height)
  });
})()'

# ---------- REFERENCE half (direct, logged-out) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refsubm141"
agent-browser open "$REF/login" >/dev/null 2>&1
sleep 4
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1

echo "=== REF: the submit center (live, never guessed) ==="
CENTER="$(agent-browser eval "$CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "submit center: $CENTER"
CX="${CENTER%,*}"; CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on REF"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: SUBMIT-HOVERED (real pointer at the submit center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
CENTER_JS="$CENTER_JS" STATE_JS="$STATE_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonesubm141"
agent-browser open "http://localhost:3200/login" >/dev/null 2>&1
sleep 3
agent-browser set viewport 1280 800 >/dev/null 2>&1
sleep 1

echo "=== CLONE: the submit center (live, never guessed) ==="
CENTER="$(agent-browser eval "$CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "submit center: $CENTER"
CX="${CENTER%,*}"; CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on CLONE"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: SUBMIT-HOVERED (real pointer at the submit center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
echo "=== submithover arbit v141 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
