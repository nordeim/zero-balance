(() => {
  const form = [...document.querySelectorAll('form')].find((f) => /Save Asset/.test(f.textContent || ''));
  if (!form) return JSON.stringify({ err: 'no form' });
  const walk = [];
  const describe = (el, depth) => {
    for (const ch of el.children) {
      const cs = getComputedStyle(ch);
      const t = (ch.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40);
      if (ch.tagName === 'LABEL' || ch.querySelector?.(':scope > label') || ['INPUT', 'TEXTAREA', 'BUTTON'].includes(ch.tagName) || /rounded-md border/.test(ch.className)) {
        walk.push(`${'  '.repeat(depth)}${ch.tagName}${ch.className ? '.' + ch.className.toString().split(' ').slice(0, 4).join('.') : ''} :: ${t}`);
      } else {
        walk.push(`${'  '.repeat(depth)}${ch.tagName} :: ${t.slice(0, 30)}`);
      }
      if (depth < 2 && ch.children.length && !['INPUT', 'TEXTAREA'].includes(ch.tagName)) describe(ch, depth + 1);
    }
  };
  describe(form, 0);
  return JSON.stringify(walk.slice(0, 60), null, 1);
})()
