// v23 session: mobile-sheet focus-ring read — opens the sheet, presses one
// real Tab, reads the FULL computed box-shadow of the focused link (the
// visible focus indicator; the outline is transparent/none on both sites).
(async () => {
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
  const out = {};
  out.sheetLinkCount = [...document.querySelectorAll('[role=dialog] a, [data-state=open] a')].filter((a) => a.getBoundingClientRect().width > 100).length;
  return JSON.stringify(out);
})()
