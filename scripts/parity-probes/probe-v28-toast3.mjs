// v28 sweep: toast-render timing check — after saving an item, read the
// z-[100] viewport heights at 200ms / 900ms / 3.4s (a toast inflates the
// viewport beyond the 32px empty padding).
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const setVal = (el, v) => {
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set.call(el, v);
    el.dispatchEvent(new Event("input", { bubbles: true }));
  };
  const add = [...document.querySelectorAll("button")].find((b) => (b.textContent || "").trim() === "Add Income");
  add.click();
  await sleep(700);
  const num = [...document.querySelectorAll("input")].find((i) => i.getAttribute("type") === "number" && i.getBoundingClientRect().width > 100);
  const name = [...document.querySelectorAll("input")].find((i) => /e\.g\., Salary/i.test(i.placeholder || ""));
  setVal(num, "55.55");
  setVal(name, "Toast Probe Four");
  const save = [...document.querySelectorAll("button")].find((b) => /save/i.test((b.textContent || "").trim()));
  save.click();
  const read = () => [...document.querySelectorAll("div")].filter((el) => {
    const cs = getComputedStyle(el);
    return cs.position === "fixed" && /z-\[100\]/.test((el.className || "").toString());
  }).map((v) => Math.round(v.getBoundingClientRect().height));
  await sleep(200);
  const h200 = read();
  await sleep(700);
  const h900 = read();
  await sleep(2500);
  const h3400 = read();
  return JSON.stringify({ h200, h900, h3400 });
})()
