(() => {
  // sidebar (first nav parent) bottom area: user chip, logout, etc.
  const nav = document.querySelector('nav') || document.querySelector('[class*="sidebar"]');
  if (!nav) return JSON.stringify({ err: 'no nav' });
  const side = nav.closest('div') || nav;
  // find bottom-anchored content: last children
  const all = [...side.querySelectorAll('button, a, [class*="logout"], [class*="user"]')];
  const txts = all.map((e) => ({ tag: e.tagName, text: (e.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40), cls: (e.className || '').toString().slice(0, 60) })).filter((x) => x.text);
  const sideText = (side.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 250);
  return JSON.stringify({ txts: txts.slice(-8), sideText }, null, 1);
})()
