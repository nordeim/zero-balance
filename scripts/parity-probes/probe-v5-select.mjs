// Session-8 (v5): select dropdown content + items chrome (when open).
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const opts = [...document.querySelectorAll('[role="option"]')];
  if (!opts.length) return JSON.stringify({ error: 'no options' });
  out.options = opts.slice(0, 4).map((o) => ({
    t: txt(o),
    color: cs(o, 'color'),
    size: cs(o, 'fontSize'),
    pad: cs(o, 'padding'),
    bg: cs(o, 'backgroundColor'),
    radius: cs(o, 'borderRadius'),
    highlighted: o.getAttribute('data-highlighted') !== null || o.getAttribute('data-state'),
  }));
  const content = opts[0].closest('[role="listbox"]');
  if (content) {
    out.content = { bg: cs(content, 'backgroundColor'), border: cs(content, 'borderWidth') + ' ' + cs(content, 'borderColor'), radius: cs(content, 'borderRadius'), pad: cs(content, 'padding'), shadow: (cs(content, 'boxShadow') || '').slice(0, 60) };
  }
  return JSON.stringify(out, null, 1);
})()
