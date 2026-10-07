(() => {
  const nav = document.querySelector('nav');
  const side = nav?.closest('div') || nav;
  const txt = (side.textContent || '').replace(/\s+/g, ' ').replace(/:root \{[^}]*\}/, '[CSSVARS]').trim();
  // logout button?
  const logout = [...document.querySelectorAll('button, a')].find((e) => /log ?out|sign out/i.test(e.textContent || '') || e.getAttribute('aria-label')?.match(/log ?out/i));
  // bottom-most element in the sidebar rail
  const rail = [...side.querySelectorAll('div')].filter((d) => d.children.length && !d.querySelector('nav')).sort((a, b) => b.getBoundingClientRect().bottom - a.getBoundingClientRect().bottom)[0];
  return JSON.stringify({
    sideText: txt.slice(0, 400),
    logout: logout ? { tag: logout.tagName, text: (logout.textContent || '').trim(), inSidebar: !!logout.closest('nav, [class*="sidebar"]') } : 'NONE',
    bottomMost: rail ? { text: (rail.textContent || '').trim().slice(0, 60), cls: (rail.className || '').slice(0, 60) } : null,
  }, null, 1);
})()
