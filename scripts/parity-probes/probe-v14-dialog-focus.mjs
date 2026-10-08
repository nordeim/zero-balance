// probe-v14-dialog-focus.mjs — what receives focus when an Add-Item dialog
// opens + the dialog's first-input geometry. Run right AFTER opening the dialog.
(() => {
  const out = {};
  const dlg = document.querySelector('[role="dialog"]');
  out.dialogFound = !!dlg;
  if (!dlg) return JSON.stringify(out);
  const ae = document.activeElement;
  out.activeElement = { tag: ae ? ae.tagName : null, id: ae ? ae.id : null, label: ae ? (ae.labels && ae.labels[0] ? ae.labels[0].textContent.trim() : (ae.getAttribute('aria-label') || null)) : null, isInput: ae ? /^(INPUT|TEXTAREA|SELECT|BUTTON)$/.test(ae.tagName) : false, ph: ae && ae.placeholder ? ae.placeholder : null };
  const r = dlg.getBoundingClientRect();
  out.dialog = { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y) };
  const inputs = [...dlg.querySelectorAll('input, select, textarea, button')].filter(i => i.getBoundingClientRect().height > 0);
  out.inputCount = inputs.length;
  out.firstInput = inputs[0] ? { tag: inputs[0].tagName, ph: inputs[0].placeholder || null, label: inputs[0].labels && inputs[0].labels[0] ? inputs[0].labels[0].textContent.trim() : null } : null;
  out.headerText = (dlg.querySelector('h1,h2,h3,[class*=header]')?.textContent || '').trim().slice(0, 50);
  return JSON.stringify(out, null, 1);
})()
