#!/usr/bin/env bash
# drillhover-arbit-v142.sh — the ONE-SHOT both-sides census for the v142
# candidate pin family: the DASHBOARD DRILL-DOWN ROWS' OWN-HOVER LADDERS at
# desktop 1280x800 (the networth+drill-down pair's own surface — the
# drill-down EXPANDED state) — the never-pinned HOVER PATHS of the pinned
# drill-down family (the v60 F2 pin holds the drill-down sub/item STRUCTURE;
# the v41/v44 pins the at-rest row chrome + the chevron glyph contract; the
# v43 F2 repair measured the section row's own-hover tint live on BOTH
# sites [hover-v43.mjs — the arbitrary-hex repair: the clone's v4 named
# hover:bg-gray-50 computed lab(), the reference's engaged v3 gray-50
# computes rgb(249,250,251)] and documented the category rows' inline-bg
# INERTNESS on BOTH sites [the v29 class]; the v31 pin the drill-down
# keyboard path — every drill-down census AT-REST, CLICK-STRUCTURE or
# KEYBOARD, never the hover END-STATES; the rows' own-hover held by NO
# spec at ANY viewport — verified by the suite-wide survey [breakdown.spec.ts
# carries zero hover coverage; dashboard.spec.ts's hover pins cover only
# the stat cards + the quick actions]).
#   the ladder — the at-rest chrome -> the SECTION-ROW-HOVERED end-state
#   (the LIVE tint contract) -> the CATEGORY-ROW-HOVERED end-state (the
#   INERT contract) -> the restored at-rest.
# The construct under test: the clone's section row carries
# hover:bg-[#f9fafb] (dashboard-view.tsx:309 — the v43 F2 arbitrary-hex
# repair), so the expected own-hover end-state is the TINTED contract
# (bg rgb(249,250,251) under the section row's own hover — the reference's
# engaged v3 gray-50 computes the same value); the clone's category row
# carries hover:bg-gray-100 BUT ALSO an inline backgroundColor
# rgb(249,250,251) (dashboard-view.tsx:365 — the inline beats the utility,
# the v29 class), so its expected own-hover end-state is the INERT-HOVER
# contract (the at-rest inline bg persisting under its own hover — the
# reference's rows the same INERT form, both sites documented at v29/v43).
# BOTH SIDES measured (READ-ONLY — passive navigation + VIEW-STATE
# expansion clicks only + REAL pointer MOVES, the v46 incident rule: the
# drill-down rows mutate no data; a mouse MOVE on a button dispatches no
# click; the rows are NEVER clicked past the one expansion — the accordion
# toggles on click, out of bounds). The hover moves the REAL pointer to
# each row's OWN center (the coords read live after the settle — never
# guessed; the mouse move takes x y as TWO args — the v123 lesson); the
# ladder parks at (5,5) first (the v22 lesson), reads the at-rest state,
# hovers the section row, reads both rows, hovers the category row, reads
# both rows, parks back, and verifies the restore. The v73 heredoc lesson:
# the QUOTED <<'EOF' with the env-injected census JS for the clone half;
# no literal dollar sequences in the census JS (the v64 rule); no single
# quotes inside the single-quoted census strings (the v60 lesson); the
# plain comma-pair center return (the v116 convention); tr -d '"' on the
# extraction (the v124 lesson); STRUCTURAL finders (the breakdown card by
# its title leaf -> the section row = the button whose text carries
# 'Total Income'; the category row = the first button whose trimmed text
# starts with 'Salary' — both sites' first Income category).
set -u
cd "$(dirname "$0")/../.."

EXPAND_JS='(async () => {
  const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(e => (e.textContent||"").trim() === "Net Zero Breakdown");
  const card = leaf ? leaf.closest("div[class*=rounded-2xl]") : null;
  if (!card) return "no breakdown card";
  const sec = [...card.querySelectorAll("button")].find(b => /Total Income/i.test(b.textContent||""));
  if (!sec) return "no section";
  if (sec.getAttribute("aria-expanded") === "true") return "already expanded";
  sec.click();
  await new Promise((r) => setTimeout(r, 600));
  const cat = [...card.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith("Salary"));
  if (!cat) return "no category";
  return "expanded: section + first category visible";
})()'

CENSUS_JS='(async () => {
  const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(e => (e.textContent||"").trim() === "Net Zero Breakdown");
  const card = leaf ? leaf.closest("div[class*=rounded-2xl]") : null;
  if (!card) return JSON.stringify({err: "no card"});
  const sec = [...card.querySelectorAll("button")].find(b => /Total Income/i.test(b.textContent||""));
  const cat = [...card.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith("Salary"));
  if (!sec || !cat) return JSON.stringify({err: "no rows"});
  const rd = (el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      hoverMatch: el.matches(":hover"),
      txt: (el.textContent||"").trim().slice(0, 14),
      bg: cs.backgroundColor,
      color: cs.color,
      radius: cs.borderRadius,
      transitionProperty: cs.transitionProperty,
      transitionDuration: cs.transitionDuration,
      w: Math.round(r.width),
      h: Math.round(r.height)
    };
  };
  return JSON.stringify({section: rd(sec), category: rd(cat)});
})()'

SEC_CENTER_JS='(async () => {
  const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(e => (e.textContent||"").trim() === "Net Zero Breakdown");
  const card = leaf ? leaf.closest("div[class*=rounded-2xl]") : null;
  if (!card) return "no-card";
  const sec = [...card.querySelectorAll("button")].find(b => /Total Income/i.test(b.textContent||""));
  if (!sec) return "no-row";
  sec.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = sec.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

CAT_CENTER_JS='(async () => {
  const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(e => (e.textContent||"").trim() === "Net Zero Breakdown");
  const card = leaf ? leaf.closest("div[class*=rounded-2xl]") : null;
  if (!card) return "no-card";
  const cat = [...card.querySelectorAll("button")].find(b => (b.textContent||"").trim().startsWith("Salary"));
  if (!cat) return "no-row";
  cat.scrollIntoView({ block: "center" });
  await new Promise((r) => setTimeout(r, 300));
  const r = cat.getBoundingClientRect();
  return Math.round(r.x + r.width / 2) + "," + Math.round(r.y + r.height / 2);
})()'

# ---------- REFERENCE half (direct, logged-in) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refdrill142"
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

echo "=== REF: the one-time view-state expansion (the section row click) ==="
agent-browser eval "$EXPAND_JS" 2>/dev/null | tail -1
sleep 1

echo "=== REF: the rows' centers (live, never guessed) ==="
SEC_CENTER="$(agent-browser eval "$SEC_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
CAT_CENTER="$(agent-browser eval "$CAT_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "section center: $SEC_CENTER | category center: $CAT_CENTER"
SX="${SEC_CENTER%,*}"; SY="${SEC_CENTER#*,}"
CX2="${CAT_CENTER%,*}"; CY2="${CAT_CENTER#*,}"
if [ -z "$SX" ] || [ -z "$SY" ] || [ -z "$CX2" ] || [ -z "$CY2" ]; then echo "FINDER FAILED on REF"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$SX" "$SY" >/dev/null 2>&1
  sleep 1
  echo "=== REF: SECTION-HOVERED (real pointer at the section row center $SX,$SY) ==="
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX2" "$CY2" >/dev/null 2>&1
  sleep 1
  echo "=== REF: CATEGORY-HOVERED (real pointer at the category row center $CX2,$CY2) ==="
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== REF: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
fi
pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
EXPAND_JS="$EXPAND_JS" CENSUS_JS="$CENSUS_JS" SEC_CENTER_JS="$SEC_CENTER_JS" CAT_CENTER_JS="$CAT_CENTER_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonedrill142"
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

echo "=== CLONE: the one-time view-state expansion (the section row click) ==="
agent-browser eval "$EXPAND_JS" 2>/dev/null | tail -1
sleep 1

echo "=== CLONE: the rows' centers (live, never guessed) ==="
SEC_CENTER="$(agent-browser eval "$SEC_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
CAT_CENTER="$(agent-browser eval "$CAT_CENTER_JS" 2>/dev/null | tail -1 | tr -d '"')"
echo "section center: $SEC_CENTER | category center: $CAT_CENTER"
SX="${SEC_CENTER%,*}"; SY="${SEC_CENTER#*,}"
CX2="${CAT_CENTER%,*}"; CY2="${CAT_CENTER#*,}"
if [ -z "$SX" ] || [ -z "$SY" ] || [ -z "$CX2" ] || [ -z "$CY2" ]; then echo "FINDER FAILED on CLONE"; else
  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: AT-REST (pointer parked at 5,5) ==="
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$SX" "$SY" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: SECTION-HOVERED (real pointer at the section row center $SX,$SY) ==="
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

  agent-browser mouse move "$CX2" "$CY2" >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: CATEGORY-HOVERED (real pointer at the category row center $CX2,$CY2) ==="
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

  agent-browser mouse move 5 5 >/dev/null 2>&1
  sleep 1
  echo "=== CLONE: RESTORED (pointer re-parked at 5,5) ==="
  agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
fi
echo "=== drillhover arbit v142 done ==="
EOF

echo "=== seedcheck (the v66 discipline) ==="
env -u DATABASE_URL node scripts/parity-probes/db-seedcheck-v68.cjs 2>/dev/null | tail -8
