#!/usr/bin/env bash
# drillfocus-discovery-v154.sh — the ONE-SHOT both-sides census for the
# v154 candidate pin family: the DASHBOARD DRILL-DOWN ROWS' FOCUS-VISIBLE
# LADDERS at desktop 1280x800 (the v148-era NETWORTH + drill-down pair's
# own drill-down surface — the Net Zero Breakdown card's EXPANDED state on
# /: the Total Income section open + its first category open, the pair's
# own VLM state). The never-pinned KEYBOARD PATH of the pinned drill-down
# family (the sibling-completion form, the v149/v150/v151/v152/v153
# precedent): the family's HOVER paths closed by the v142 pin (the section
# row's TINTED ladder + the category row's INERT ladder — at-rest ->
# hovered -> restored, the hoverMatch axes); the family's AT-REST censuses
# held by the v43/v44/v50/v53/v60 pins (the per-row chrome byte-identical
# at every level, both viewports); the v44 F1 pin the expansion ANIMATION;
# the v44 F4 pin the chevron GLYPH swaps; the breakdown spec's accordion
# pin the behavior — the rows' FOCUSED chrome held by NO spec at ANY
# viewport (the suite-wide survey: rg 'drill|section.*row|category.*row'
# across tests/e2e/*.spec.ts — ZERO focus-visible/ring assertions on the
# drill-down rows in any file; the v40 Tab-order walk ran on the COLLAPSED
# dashboard, its 16 stops never entering the expanded drill-down; the v31
# keyboard pin is the DONUT's sector focus, a different element).
#   the ladder — the at-rest chrome (the pointer parked at 5,5 + the
#   activeElement blurred clean) -> the FOCUSED end-state (focusVisible:
#   true — the REAL Chromium FocusOptions member, the v35 S2 idiom; the
#   v25 plain-focus lesson does not apply to the focusVisible form) ->
#   the blurred restore. BOTH ROWS measured at every rung (the sibling
#   non-interference form: the section row focused first [the category's
#   at-rest contract re-checked], then the category row focused [the
#   section's restore re-checked]).
# The construct under test: BOTH rows are real <button> elements with
# hover utilities but NO focus utilities (dashboard-view.tsx:306 the
# section row 'flex w-full -mx-2 cursor-pointer items-center
# justify-between rounded-lg p-2 transition-colors hover:bg-[#f9fafb]';
# :362 the category row 'flex w-full cursor-pointer items-center
# justify-between rounded-lg px-3 py-1.5 transition-colors
# hover:bg-gray-100' + the inline backgroundColor rgb(249,250,251) — the
# v29 inline-beats-utility class) — so the expected focused end-state is
# the UA-DEFAULT RING (outline auto / 1px / 0px — the v143/v149
# quick-action-card contract form) with each row's chrome UNCHANGED under
# focus (focus != hover: the section's hover tint NOT engaged, the
# category's inline bg persisting). The reference's rows measured live —
# the census documents whichever contract its side renders.
# BOTH SIDES measured. The drill-down OPEN path is the standing read-only
# form (the v148/v154 shots scripts: the section click + the category
# click — view-state expansion clicks only, the drill-down rows mutate no
# data — the v46 rule; focus() dispatches no click). The row finders are
# STRUCTURAL on BOTH sides (the reference's rows carry NO aria-expanded —
# the v32 S1 superset — so the finders are the shots scripts' own: the
# breakdown card by its 'Net Zero Breakdown' leaf, the section by the
# /Total Income/ text, the category by the first visible $-bearing
# non-Total button). The v73 heredoc lesson: the QUOTED <<EOF with the
# env-injected census JS for the clone half; no literal dollar sequences
# in the census JS (the v64 rule — the \$-regex written with the escaped
# backslash); no apostrophes in JS comments (the v60 rule).
set -u
cd "$(dirname "$0")/../.."

CENSUS_JS='(async () => {
  const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(e => (e.textContent||"").trim() === "Net Zero Breakdown");
  const card = leaf ? leaf.closest("div[class*=rounded-2xl]") : null;
  if (!card) return JSON.stringify({ err: "no breakdown card" });
  const sec = [...card.querySelectorAll("button")].find(b => /Total Income/i.test(b.textContent||""));
  const cat = [...card.querySelectorAll("button")].find(b => b.offsetParent !== null && /\$/.test(b.textContent||"") && !/Total|Net Balance/i.test(b.textContent||""));
  if (!sec || !cat) return JSON.stringify({ err: sec ? "no category row" : "no section row" });
  const read = (el) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      focused: document.activeElement === el,
      fv: el.matches(":focus-visible"),
      outlineStyle: cs.outlineStyle,
      outlineColor: cs.outlineColor,
      outlineWidth: cs.outlineWidth,
      outlineOffset: cs.outlineOffset,
      bg: cs.backgroundColor,
      boxShadow: cs.boxShadow,
      color: cs.color,
      fs: cs.fontSize,
      fw: cs.fontWeight,
      w: Math.round(r.width),
      h: Math.round(r.height)
    };
  };
  return JSON.stringify({ section: read(sec), category: read(cat) });
})()'

FOCUS_SEC_JS='(async () => {
  const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(e => (e.textContent||"").trim() === "Net Zero Breakdown");
  const card = leaf ? leaf.closest("div[class*=rounded-2xl]") : null;
  if (!card) return "no breakdown card";
  const sec = [...card.querySelectorAll("button")].find(b => /Total Income/i.test(b.textContent||""));
  if (!sec) return "no section row";
  sec.focus({ focusVisible: true });
  await new Promise((r) => setTimeout(r, 450));
  return "section focused";
})()'

FOCUS_CAT_JS='(async () => {
  const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(e => (e.textContent||"").trim() === "Net Zero Breakdown");
  const card = leaf ? leaf.closest("div[class*=rounded-2xl]") : null;
  if (!card) return "no breakdown card";
  const sec = [...card.querySelectorAll("button")].find(b => /Total Income/i.test(b.textContent||""));
  const cat = [...card.querySelectorAll("button")].find(b => b.offsetParent !== null && /\$/.test(b.textContent||"") && !/Total|Net Balance/i.test(b.textContent||""));
  if (!cat) return "no category row";
  if (sec && document.activeElement === sec) sec.blur();
  cat.focus({ focusVisible: true });
  await new Promise((r) => setTimeout(r, 450));
  return "category focused";
})()'

BLUR_JS='(async () => {
  if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
  await new Promise((r) => setTimeout(r, 450));
  return "blurred";
})()'

# ---------- REFERENCE half (direct, logged-in) ----------
REF="https://zero-balance-4885a8f3.base44.app"
export AGENT_BROWSER_SESSION="refdrillf154"
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
agent-browser open "$REF/" >/dev/null 2>&1
sleep 4
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const sec = [...card.querySelectorAll('button')].find(b => /Total Income/i.test(b.textContent||''));
  if (!sec) return 'no section';
  sec.click();
  return 'section clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const cat = [...card.querySelectorAll('button')].find(b => b.offsetParent !== null && /\\\$/.test(b.textContent||'') && !/Total|Net Balance/i.test(b.textContent||''));
  if (!cat) return 'no category';
  cat.click();
  return 'category clicked';
})()" 2>/dev/null | tail -1
sleep 1
# the clean at-rest: blur the click-left focus + park the pointer at (5,5)
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== REF: AT-REST (no focus, pointer parked at 5,5 — both rows) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== REF: SECTION FOCUSED (focusVisible:true — the category non-interference check) ==="
agent-browser eval "$FOCUS_SEC_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== REF: CATEGORY FOCUSED (focusVisible:true — the section restore check) ==="
agent-browser eval "$FOCUS_CAT_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== REF: BLURRED (the restore — both rows) ==="
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1

pkill -f "agent-browser" 2>/dev/null
sleep 3

# ---------- CLONE half (inside with-server, census JS env-injected) ----------
CENSUS_JS="$CENSUS_JS" FOCUS_SEC_JS="$FOCUS_SEC_JS" FOCUS_CAT_JS="$FOCUS_CAT_JS" BLUR_JS="$BLUR_JS" bash scripts/parity-probes/with-server.sh bash -s <<'EOF'
set -u
export AGENT_BROWSER_SESSION="clonedrillf154"
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
agent-browser open "http://localhost:3200/" >/dev/null 2>&1
sleep 4
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const sec = [...card.querySelectorAll('button')].find(b => /Total Income/i.test(b.textContent||''));
  if (!sec) return 'no section';
  sec.click();
  return 'section clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "(() => {
  const leaf = [...document.querySelectorAll('h1,h2,h3,h4,p,span')].find(e => (e.textContent||'').trim() === 'Net Zero Breakdown');
  const card = leaf ? leaf.closest('div[class*=rounded-2xl]') : null;
  if (!card) return 'no breakdown card';
  const cat = [...card.querySelectorAll('button')].find(b => b.offsetParent !== null && /\\\$/.test(b.textContent||'') && !/Total|Net Balance/i.test(b.textContent||''));
  if (!cat) return 'no category';
  cat.click();
  return 'category clicked';
})()" 2>/dev/null | tail -1
sleep 1
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser mouse move 5 5 >/dev/null 2>&1
sleep 1

echo "=== CLONE: AT-REST (no focus, pointer parked at 5,5 — both rows) ==="
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: SECTION FOCUSED (focusVisible:true — the category non-interference check) ==="
agent-browser eval "$FOCUS_SEC_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: CATEGORY FOCUSED (focusVisible:true — the section restore check) ==="
agent-browser eval "$FOCUS_CAT_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
echo "=== CLONE: BLURRED (the restore — both rows) ==="
agent-browser eval "$BLUR_JS" 2>/dev/null | tail -1
agent-browser eval "$CENSUS_JS" 2>/dev/null | tail -1
EOF
echo "=== drillfocus discovery v154 done ==="
