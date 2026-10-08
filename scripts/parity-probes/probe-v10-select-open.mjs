// probe-v10-select-open.mjs — open the Type select, measure the popover + options
(() => {
  const out = {};
  // find the first closed combobox (Type) inside the dialog
  const combo = [...document.querySelectorAll("[role='combobox']")].find(c => !c.getAttribute("aria-expanded") || c.getAttribute("aria-expanded") === "false");
  if (!combo) return JSON.stringify({ err: "no combobox" });
  out.trigger = { txt: combo.textContent.trim(), w: Math.round(combo.getBoundingClientRect().width), h: Math.round(combo.getBoundingClientRect().height), fs: getComputedStyle(combo).fontSize, border: getComputedStyle(combo).borderBottomColor, radius: getComputedStyle(combo).borderRadius };
  combo.click();
  return JSON.stringify({ opened: true, trigger: out.trigger, note: "clicked — run popover probe next" });
})()
