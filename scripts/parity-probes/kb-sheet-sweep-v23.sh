#!/usr/bin/env bash
# v23 session: mobile-sheet KEYBOARD sweep (the session-44 log's suggestion 2 —
# the sheet's focus semantics under Tab/Escape were never swept; the desktop
# rail was). Opens the sheet, then presses REAL keys (agent-browser press =
# CDP key events, which move focus — synthetic dispatch does not), reading
# the focused element after each press.
# Usage: kb-sheet-sweep-v23.sh <site-url> [tab-count]
set -u
SITE="$1"
TABS="${2:-8}"

# open the sheet: synthetic burger click (bypasses the reference's toast
# interception — its bug) then settle for the slide-in
agent-browser open "$SITE/" >/dev/null 2>&1
sleep 2
agent-browser eval "(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const header = document.querySelector('header');
  const burger = header ? header.querySelector('button') : null;
  if (!burger) return 'no burger';
  const br = burger.getBoundingClientRect();
  const bx = br.x + br.width / 2, by = br.y + br.height / 2;
  for (const [type, ctor] of [['pointerdown', PointerEvent], ['pointerup', PointerEvent], ['mousedown', MouseEvent], ['mouseup', MouseEvent]]) {
    burger.dispatchEvent(new ctor(type, { bubbles: true, cancelable: true, composed: true, clientX: bx, clientY: by, button: 0, buttons: 1, pointerId: 1 }));
  }
  burger.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, composed: true, clientX: bx, clientY: by }));
  await sleep(700);
  return 'sheet-opened';
})()" >/dev/null 2>&1
sleep 0.5

echo "--- focus after sheet open (initial focus) ---"
agent-browser eval "(() => { const el = document.activeElement; if (!el || el === document.body) return JSON.stringify({body:true}); const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return JSON.stringify({ t: el.tagName, label: (el.getAttribute('aria-label') || el.textContent || '').trim().slice(0,24), x: Math.round(r.x), y: Math.round(r.y), outline: (cs.outlineStyle+' '+cs.outlineWidth+' '+(cs.outlineColor||'')).slice(0,44) }); })()"

for i in $(seq 1 "$TABS"); do
  agent-browser press Tab >/dev/null 2>&1
  sleep 0.15
  echo "--- focus after Tab #$i ---"
  agent-browser eval "(() => { const el = document.activeElement; if (!el || el === document.body) return JSON.stringify({body:true}); const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return JSON.stringify({ t: el.tagName, label: (el.getAttribute('aria-label') || el.textContent || '').trim().slice(0,24), x: Math.round(r.x), y: Math.round(r.y), outline: (cs.outlineStyle+' '+cs.outlineWidth+' '+(cs.outlineColor||'')).slice(0,44) }); })()"
done

echo "--- sheet still open after Tab loop? ---"
agent-browser eval "(() => JSON.stringify({ sheetOpen: [...document.querySelectorAll('[role=dialog], [data-state=open]')].some(el => { const r = el.getBoundingClientRect(); return r.width > 200 && r.width < 340 && r.height > 100; }) }))()"

echo "--- press Escape ---"
agent-browser press Escape >/dev/null 2>&1
sleep 0.8
agent-browser eval "(() => JSON.stringify({ sheetOpenAfterEscape: [...document.querySelectorAll('[role=dialog], [data-state=open]')].some(el => { const r = el.getBoundingClientRect(); return r.width > 200 && r.width < 340 && r.height > 100; }), url: location.pathname }))()"
