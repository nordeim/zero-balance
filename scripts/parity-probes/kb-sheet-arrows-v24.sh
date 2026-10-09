#!/usr/bin/env bash
# v24 session: mobile-sheet ARROW-key sweep (the session-46 log's suggestion
# 2 — Tab + Escape were swept in v23; Arrow-key behavior inside the open
# sheet was never compared). Opens the sheet (synthetic burger click that
# bypasses the reference's toast interception), then presses each arrow key,
# reading the focused element + sheet state after every press.
# Usage: kb-sheet-arrows-v24.sh <site-url>
set -u
SITE="$1"

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

read_focus () {
  agent-browser eval "(() => { const el = document.activeElement; const sheet = [...document.querySelectorAll('[role=dialog], [data-state=open]')].find(el2 => { const r = el2.getBoundingClientRect(); return r.width > 200 && r.width < 340 && r.height > 100; }); const sheetScroll = sheet ? { st: sheet.scrollTop, sh: sheet.scrollHeight, ch: sheet.clientHeight } : null; if (!el || el === document.body) return JSON.stringify({ focus: 'body', sheetOpen: !!sheet, sheetScroll }); const r = el.getBoundingClientRect(); return JSON.stringify({ focus: el.tagName + ':' + (el.getAttribute('aria-label') || el.textContent || '').trim().slice(0,20), fx: Math.round(r.x), fy: Math.round(r.y), sheetOpen: !!sheet, sheetScroll }); })()"
}

echo "--- baseline (sheet open, before any key) ---"
read_focus

for KEY in ArrowDown ArrowDown ArrowUp ArrowRight ArrowLeft; do
  agent-browser press "$KEY" >/dev/null 2>&1
  sleep 0.2
  echo "--- after $KEY ---"
  read_focus
done

echo "--- sheet still open after arrow loop? ---"
agent-browser eval "(() => JSON.stringify({ sheetOpen: [...document.querySelectorAll('[role=dialog], [data-state=open]')].some(el => { const r = el.getBoundingClientRect(); return r.width > 200 && r.width < 340 && r.height > 100; }), url: location.pathname }))()"
