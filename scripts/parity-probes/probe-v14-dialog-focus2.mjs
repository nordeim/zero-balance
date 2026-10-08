// probe-v14-dialog-focus2.mjs — initial focus in the Add-Item dialog. The
// reference's dialogs are plain fixed divs (no role=dialog) — find the panel
// via the "Add Budget Item" heading's fixed ancestor; the clone uses Radix
// [role=dialog] — support both.
(() => {
  const out = {};
  const h = [...document.querySelectorAll('h1,h2,h3')].find(x => /Add Budget Item/i.test(x.textContent));
  let dlg = null;
  if (h) {
    let n = h;
    while (n && n !== document.body) {
      const cs = getComputedStyle(n);
      if (cs.position === 'fixed' || n.getAttribute('role') === 'dialog') { dlg = n; break; }
      n = n.parentElement;
    }
  }
  out.dialogFound = !!dlg;
  if (!dlg) return JSON.stringify(out);
  const ae = document.activeElement;
  out.activeElement = {
    tag: ae ? ae.tagName : null,
    isInput: ae ? /^(INPUT|TEXTAREA|SELECT)$/.test(ae.tagName) : false,
    ph: ae && ae.placeholder !== undefined ? ae.placeholder : null,
    label: ae && ae.labels && ae.labels[0] ? ae.labels[0].textContent.trim() : null,
    bodyClass: ae && ae.tagName === 'BODY' ? 'BODY (no focus move)' : null
  };
  const r = dlg.getBoundingClientRect();
  out.dialog = { w: Math.round(r.width), h: Math.round(r.height) };
  const visInputs = [...dlg.querySelectorAll('input, textarea')].filter(i => i.getBoundingClientRect().height > 0);
  out.inputCount = visInputs.length;
  out.inputs = visInputs.slice(0, 3).map(i => ({ ph: i.placeholder || null, label: i.labels && i.labels[0] ? i.labels[0].textContent.trim() : null, type: i.type }));
  out.headingText = h.textContent.trim();
  return JSON.stringify(out, null, 1);
})()
