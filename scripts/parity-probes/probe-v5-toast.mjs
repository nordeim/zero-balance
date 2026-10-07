// Session-8 (v5): toast chrome (triggered by a validation error).
(() => {
  const out = {};
  const toasts = [...document.querySelectorAll('[data-sonner-toast], .sonner-toast, [role="status"], li[data-type]')].filter((t) => t.getBoundingClientRect().width > 50);
  if (!toasts.length) {
    // fallback: any toast-ish element with text
    const maybe = [...document.querySelectorAll('div')].filter((d) => {
      const c = (d.className || '').toString();
      return /toast/i.test(c) && (d.textContent || '').trim().length > 3 && d.getBoundingClientRect().width > 50;
    });
    if (!maybe.length) return JSON.stringify({ error: 'no toast found' });
    out.via = 'class-scan';
    out.toasts = maybe.slice(0, 2).map((t) => ({ cls: (t.className || '').toString().slice(0, 60), text: (t.textContent || '').trim().slice(0, 50), color: getComputedStyle(t).color, bg: getComputedStyle(t).backgroundColor }));
  } else {
    out.toasts = toasts.slice(0, 2).map((t) => {
      const cs = getComputedStyle(t);
      return { text: (t.textContent || '').trim().slice(0, 50), color: cs.color, bg: cs.backgroundColor, border: cs.borderWidth + ' ' + cs.borderColor, radius: cs.borderRadius };
    });
  }
  return JSON.stringify(out, null, 1);
})()
