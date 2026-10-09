// v28 sweep: add an income item, then IMMEDIATELY dump the z-[100] toast
// viewport's contents (the toast node + its close button family).
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const setVal = (el, v) => {
    const proto = el.tagName === "TEXTAREA" ? window.HTMLTextAreaElement.prototype : window.HTMLInputElement.prototype;
    Object.getOwnPropertyDescriptor(proto, "value").set.call(el, v);
    el.dispatchEvent(new Event("input", { bubbles: true }));
  };
  const add = [...document.querySelectorAll("button")].find((b) => (b.textContent || "").trim() === "Add Income" && b.getBoundingClientRect().width > 0);
  add.click();
  await sleep(700);
  const num = [...document.querySelectorAll("input")].find((i) => i.value === "0.00" || (i.getAttribute("type") === "number" && i.getBoundingClientRect().width > 100));
  const name = [...document.querySelectorAll("input")].find((i) => /e\.g\., Salary/i.test(i.placeholder || ""));
  setVal(num, "222.22");
  setVal(name, "Toast Probe Three");
  const save = [...document.querySelectorAll("button")].find((b) => /save|add item/i.test((b.textContent || "").trim()) && b.getBoundingClientRect().width > 0);
  save.click();
  await sleep(700); // toast slides in
  // dump ALL fixed z-100 viewport children (toast nodes)
  const vps = [...document.querySelectorAll("div")].filter((el) => {
    const cs = getComputedStyle(el);
    return cs.position === "fixed" && /z-\[100\]/.test((el.className || "").toString()) && el.getBoundingClientRect().width > 10;
  });
  const seen = new Set();
  const toasts = [];
  vps.forEach((vp) => {
    [...vp.querySelectorAll(":scope > *")].forEach((el) => {
      if (seen.has(el)) return;
      seen.add(el);
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      toasts.push({
        tag: el.tagName, txt: (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 80),
        w: Math.round(r.width), h: Math.round(r.height),
        cls: (el.className || "").toString().slice(0, 220),
        bg: cs.backgroundColor, color: cs.color, radius: cs.borderRadius, shadow: cs.boxShadow.slice(0, 100),
        buttons: [...el.querySelectorAll("button")].map((b) => {
          const bcs = getComputedStyle(b);
          const br = b.getBoundingClientRect();
          return {
            aria: b.getAttribute("aria-label"), txt: (b.textContent || "").trim().slice(0, 8),
            w: Math.round(br.width), h: Math.round(br.height),
            cls: (b.className || "").toString().slice(0, 220),
            color: bcs.color, bg: bcs.backgroundColor,
          };
        }),
      });
    });
  });
  return JSON.stringify({ toastCount: toasts.length, toasts }, null, 1);
})()
