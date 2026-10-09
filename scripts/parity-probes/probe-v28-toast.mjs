// v28 sweep: trigger a success toast (add an income item via the dialog)
// and dump the toast's structure + close button family. Runs entirely in
// one eval; the item is deleted afterwards by a separate step.
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const setVal = (el, v) => {
    const proto = el.tagName === "TEXTAREA" ? window.HTMLTextAreaElement.prototype : window.HTMLInputElement.prototype;
    Object.getOwnPropertyDescriptor(proto, "value").set.call(el, v);
    el.dispatchEvent(new Event("input", { bubbles: true }));
  };
  // open the Add Income dialog
  const add = [...document.querySelectorAll("button")].find((b) => (b.textContent || "").trim() === "Add Income" && b.getBoundingClientRect().width > 0);
  add.click();
  await sleep(800);
  // find the amount input (type=number or text with 0.00) and the name input
  const num = [...document.querySelectorAll('input')].find((i) => i.value === "0.00" || (i.getAttribute("type") === "number" && i.getBoundingClientRect().width > 100));
  const name = [...document.querySelectorAll("input")].find((i) => /e\.g\., Salary/i.test(i.placeholder || ""));
  if (!num || !name) return JSON.stringify({ error: "inputs not found", num: !!num, name: !!name });
  setVal(num, "222.22");
  setVal(name, "Toast Probe Two");
  // save
  const save = [...document.querySelectorAll("button")].find((b) => /save|add item/i.test((b.textContent || "").trim()) && b.getBoundingClientRect().width > 0);
  if (!save) return JSON.stringify({ error: "no save button" });
  save.click();
  await sleep(1100);
  // dump the toast: look in the fixed top-0 z-[100] containers' children
  const toasts = [...document.querySelectorAll("body > div > div, body > div")].filter((el) => {
    const cs = getComputedStyle(el);
    return cs.position === "fixed" && /z-?100|toast/i.test((el.className || "").toString()) === false && false;
  });
  // simpler: any element with toast-ish content near the top
  const fixedTops = [...document.querySelectorAll("div")].filter((el) => {
    const cs = getComputedStyle(el);
    return cs.position === "fixed" && cs.top === "0px" && el.getBoundingClientRect().width > 100;
  });
  const dump = [];
  fixedTops.forEach((f) => {
    [...f.querySelectorAll("div, li, section")].forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.width < 80 || r.height < 30) return;
      const t = (el.textContent || "").trim();
      if (!t || t.length > 120) return;
      dump.push({
        txt: t.replace(/\s+/g, " ").slice(0, 70),
        w: Math.round(r.width), h: Math.round(r.height),
        cls: (el.className || "").toString().slice(0, 160),
        buttons: [...el.querySelectorAll("button")].map((b) => ({
          aria: b.getAttribute("aria-label"), txt: (b.textContent || "").trim().slice(0, 8),
          w: Math.round(b.getBoundingClientRect().width), h: Math.round(b.getBoundingClientRect().height),
          cls: (b.className || "").toString().slice(0, 200),
        })),
      });
    });
  });
  return JSON.stringify({ toastCount: dump.length, toasts: dump.slice(0, 3) }, null, 1);
})()
