(async () => {
  // v35 Surface B: focus the Add Item button (programmatic) — then a REAL Tab
  // out+back lands the focus-visible ring. Read here; the presses run outside.
  const btn = [...document.querySelectorAll('button')].find(x => /add item/i.test(x.textContent));
  if (!btn) return JSON.stringify({found: false});
  btn.focus();
  return JSON.stringify({focused: document.activeElement === btn, name: btn.textContent.trim()});
})()
