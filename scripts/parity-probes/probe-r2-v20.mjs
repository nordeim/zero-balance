// v20 session: R2 — the sheet trap test. Synthetic-clicks the burger (the
// reference's own toast containers block the programmatic hit-test — its bug),
// waits for the sheet slide-in (500ms), taps the Income link, then reports
// whether the sheet + overlay are still up (the reference traps; the clone
// closes on nav — superset fix #2).
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const out = { url0: location.pathname };

  // 1. find the burger (mobile header's first button)
  const header = document.querySelector("header");
  const burger = header ? header.querySelector("button") : null;
  if (!burger) return JSON.stringify({ error: "no burger" });
  const br = burger.getBoundingClientRect();
  const bx = br.x + br.width / 2, by = br.y + br.height / 2;

  // 2. synthetic click sequence (bypasses elementFromPoint interception)
  for (const [type, ctor] of [
    ["pointerdown", PointerEvent], ["pointerup", PointerEvent],
    ["mousedown", MouseEvent], ["mouseup", MouseEvent],
  ]) {
    burger.dispatchEvent(new ctor(type, {
      bubbles: true, cancelable: true, composed: true,
      clientX: bx, clientY: by, button: 0, buttons: 1, pointerId: 1,
    }));
  }
  burger.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, composed: true, clientX: bx, clientY: by }));
  await sleep(700); // sheet slide-in 500ms + settle

  // 3. measure the open sheet + find the Income link
  const sheet = [...document.querySelectorAll("[role='dialog'], [data-state='open']")].find((el) => {
    const r = el.getBoundingClientRect();
    return r.width > 200 && r.width < 340; // the 288px sheet
  });
  if (!sheet) return JSON.stringify({ ...out, error: "sheet did not open" });
  const sr = sheet.getBoundingClientRect();
  out.sheet = { w: Math.round(sr.width), x: Math.round(sr.x) };

  const income = [...sheet.querySelectorAll("a, [role='link'], button")].find((el) =>
    (el.textContent || "").trim().toLowerCase().startsWith("income"));
  if (!income) return JSON.stringify({ ...out, error: "no income link in sheet" });
  const ir = income.getBoundingClientRect();
  out.incomeLink = { x: Math.round(ir.x), y: Math.round(ir.y), w: Math.round(ir.width), h: Math.round(ir.height) };

  // 4. tap Income
  const ix = ir.x + ir.width / 2, iy = ir.y + ir.height / 2;
  for (const [type, ctor] of [
    ["pointerdown", PointerEvent], ["pointerup", PointerEvent],
    ["mousedown", MouseEvent], ["mouseup", MouseEvent],
  ]) {
    income.dispatchEvent(new ctor(type, {
      bubbles: true, cancelable: true, composed: true,
      clientX: ix, clientY: iy, button: 0, buttons: 1, pointerId: 1,
    }));
  }
  income.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, composed: true, clientX: ix, clientY: iy }));
  await sleep(1200); // nav + slide-out (clone) vs nothing (ref)

  // 5. post-nav state
  out.url = location.pathname;
  const dialogs = [...document.querySelectorAll("[role='dialog'], [data-state='open']")].filter((el) => {
    const r = el.getBoundingClientRect();
    return r.width > 200 && r.width < 340 && r.height > 100;
  });
  out.sheetStillOpen = dialogs.length > 0;
  out.openDialogCount = dialogs.length;
  out.scrollWidth = document.documentElement.scrollWidth;
  return JSON.stringify(out, null, 1);
})()
