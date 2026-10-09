// v24 session: the sign-up form's row decomposition at the CURRENT viewport —
// per-row label/input geometry + inter-row gaps, so the reference's responsive
// family can be compared against the clone's field by field.
(() => {
  const form = document.querySelector('main form');
  if (!form) return JSON.stringify({ error: 'no form' });
  const rows = [];
  const fields = [...form.querySelectorAll('label')].map((l) => {
    const input = form.querySelector(`#${l.getAttribute('for')}`) || l.parentElement.querySelector('input');
    return { label: l, input };
  }).filter((f) => f.input);
  fields.forEach((f, i) => {
    const lr = f.label.getBoundingClientRect();
    const ir = f.input.getBoundingClientRect();
    rows.push({
      i,
      labelY: Math.round(lr.y), labelH: Math.round(lr.height),
      inputY: Math.round(ir.y), inputH: Math.round(ir.height),
      labelToInput: Math.round(ir.y - (lr.y + lr.height)),
      rowToRow: i > 0 ? Math.round(lr.y - (fields[i - 1].input.getBoundingClientRect().y + fields[i - 1].input.getBoundingClientRect().height)) : null,
    });
  });
  const btn = [...form.querySelectorAll('button')].find((b) => /Create account|Sign in/.test((b.textContent || '').trim()));
  const br = btn ? btn.getBoundingClientRect() : null;
  const lastInput = fields.length ? fields[fields.length - 1].input.getBoundingClientRect() : null;
  const h2 = document.querySelector('main h2');
  const h2r = h2 ? h2.getBoundingClientRect() : null;
  const firstLabel = fields.length ? fields[0].label.getBoundingClientRect() : null;
  return JSON.stringify({
    viewport: { w: innerWidth, h: innerHeight },
    rows,
    btn: br ? { y: Math.round(br.y), h: Math.round(br.height), gapFromLastInput: Math.round(br.y - (lastInput.y + lastInput.height)) } : null,
    h2: h2r ? { y: Math.round(h2r.y), h: Math.round(h2r.height), gapToFirstLabel: firstLabel ? Math.round(firstLabel.y - (h2r.y + h2r.height)) : null } : null,
  }, null, 1);
})()
