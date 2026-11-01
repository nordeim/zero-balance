#!/usr/bin/env bash
# searchhover-arbit-v140.sh — the ONE-SHOT both-sides census for the v140
# candidate pin family: the FILTER-CARD SEARCH INPUT's OWN-HOVER LADDER
# at desktop 1280x800 on /savings (the savings pair's own surface) — the
# never-pinned HOVER PATH of the pinned search family (the v37 S2 pin
# holds the input's focus-visible family + the REAL-key typing contract
# [on /income, the shared filter card]; the v64 census holds the /income
# at-rest geometry [w/h/pad/radius/border]; the v38 S2 pin holds the
# /savings instance's class-level chrome; the v134 survey measured the
# /savings at-rest + FOCUS ring — every search census AT-REST or FOCUS,
# never the hover END-STATE; the input's own-hover held by NO spec at ANY
# viewport — verified by the suite-wide survey).
#   the input ladder — the at-rest chrome -> the OWN-HOVERED end-state
#   -> the restored at-rest.
# The construct under test: the clone's input carries NO hover:
# utility (input.tsx:10 — the focus-visible + disabled + placeholder
# classes alone), so the expected own-hover end-state is the AT-REST
# CHROME PERSISTING (the inert-hover contract, the v138 tablist / v139
# select-trigger form). The reference's input: MEASURED (if it carries a
# hover tint the clone lacks, that is a GAP to repair; if inert both
# sides, NO GAP — the PIN-ONLY form).
# BOTH SIDES measured (READ-ONLY — login + passive navigation + REAL
# pointer MOVES only, the v46 rule; a mouse MOVE on an input dispatches
# no click and the input opens nothing on hover — the census cannot
# mutate state). The hover moves the REAL pointer to the input's OWN
# center (the coords read live after the settle — never guessed; the
# mouse move takes x y as TWO args — the v123 lesson); the ladder parks
# at (5,5) first (the v22 lesson), reads the at-rest state, hovers the
# input, reads, parks back, and verifies the restore. The v73 heredoc
# lesson: the QUOTED <<'EOF' with the env-injected census JS for the
# clone half; no literal dollar sequences in the census JS (the v64
# rule); no single quotes inside the single-quoted census strings (the
# v60 lesson); the plain comma-pair center return (the v116 convention);
# tr -d '"' on the extraction (the v124 lesson); STRUCTURAL finder (the
# rounded-2xl white card containing an input -> its ONLY input — the
# form shared by both sites, tag-agnostic per the v107 lesson; the
# placeholder cross-checked in the census output).
set -u
cd "$(dirname "$0")/../.."

CENTER_JS='(async () => {
  const card = [...document.querySelectorAll("div")].find((d) => {
    const cs = getComputedStyle(d);
    return cs.borderRadius === "16px" && cs.backgroundColor === "rgb(255, 255, 255)" && d.querySelector("input");
  });
  const input = card ? card.querySelector("input") : null;
  if (!input) return JSON.stringify({err: "no search input"});
  input.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = input.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

STATE_JS='(async () => {
  const card = [...document.querySelectorAll("div")].find((d) => {
    const cs = getComputedStyle(d);
    return cs.borderRadius === "16px" && cs.backgroundColor === "rgb(255, 255, 255)" && d.querySelector("input");
  });
  const input = card ? card.querySelector("input") : null;
  if (!input) return JSON.stringify({err: "no search input"});
  const cs = getComputedStyle(input);
  const r = input.getBoundingClientRect();
  return JSON.stringify({
    hoverMatch: input.matches(":hover"),
    placeholder: (input.getAttribute("placeholder") || "").slice(0, 26),
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
    caretColor: cs.caretColor
  });
})()'

# ---------- REFERENCE half (direct) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refsrch140"
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
agent-browser open "$REF/savings" >/dev/null 2>&1
sleep 5

echo "=== REF: the input center (live, never guessed) ==="
CENTER="$(agent-browser eval "$CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "search input center: $CENTER"
CX="${CENTER%,*}"; CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on REF"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: SEARCH-HOVERED (real pointer at the input center $CX,$CY) ==="
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
export AGENT_BROWSER_SESSION="clonesrch140"
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
agent-browser open "http://localhost:3200/savings" >/dev/null 2>&1
sleep 5

echo "=== CLONE: the input center (live, never guessed) ==="
CENTER="$(agent-browser eval "$CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "search input center: $CENTER"
CX="${CENTER%,*}"; CY="${CENTER#*,}"
if [ -z "$CX" ] || [ -z "$CY" ]; then echo "FINDER FAILED on CLONE"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX" "$CY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: SEARCH-HOVERED (real pointer at the input center $CX,$CY) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$STATE_JS" 2>/dev/null | tail -1
fi
echo "=== searchhover arbit v140 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
