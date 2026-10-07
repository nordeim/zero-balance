// Session-8 (v5): live post-fix — hovered inactive nav link bg + text.
(() => {
  const a = [...document.querySelectorAll('a')].find((x) => x.textContent.trim() === 'Expenses' && x.getBoundingClientRect().width > 50);
  if (!a) return JSON.stringify({ error: 'no link' });
  const cs = getComputedStyle(a);
  return JSON.stringify({ hovered: a.matches(':hover'), bg: cs.backgroundColor, color: cs.color });
})()
