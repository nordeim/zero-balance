// probe-v11-btn-shadows.mjs — button ambient-shadow + focus census: dialog Cancel/Save + page Add
(() => {
  const out = {};
  const snap = (btn) => {
    if (!btn) return null;
    const cs = getComputedStyle(btn); const r = btn.getBoundingClientRect();
    return {
      txt: (btn.textContent || '').trim().slice(0, 14),
      w: Math.round(r.width), h: Math.round(r.height),
      shadow: cs.boxShadow,
      outline: cs.outlineStyle + '/' + cs.outlineWidth + '/' + cs.outlineColor,
      bg: (cs.backgroundImage !== 'none' ? 'grad' : cs.backgroundColor).toString().slice(0, 30)
    };
  };
  // dialog panel buttons
  const panel = [...document.querySelectorAll('div')].filter(d => {
    const r = d.getBoundingClientRect(); const cs = getComputedStyle(d);
    return r.width > 500 && r.width < 750 && r.height > 200 && cs.backgroundColor === 'rgb(255, 255, 255)' && d.querySelectorAll('button').length > 0;
  }).sort((a, b) => (b.textContent || '').length - (a.textContent || '').length)[0];
  if (panel) {
    const cancel = [...panel.querySelectorAll('button')].filter(b => /cancel/i.test(b.textContent || '') && b.getBoundingClientRect().height > 0)[0];
    const save = [...panel.querySelectorAll('button')].filter(b => /save/i.test(b.textContent || '') && b.getBoundingClientRect().height > 0)[0];
    out.dialogCancel = snap(cancel);
    out.dialogSave = snap(save);
  } else { out.dialog = 'NOT OPEN'; }
  // page-level Add button
  const add = [...document.querySelectorAll('button')].filter(b => /^Add (Income|Savings|Expense|Asset|Liability)/.test((b.textContent || '').trim()) && b.getBoundingClientRect().top < 200 && b.getBoundingClientRect().height > 0)[0];
  out.pageAdd = snap(add);
  return JSON.stringify(out, null, 1);
})()
