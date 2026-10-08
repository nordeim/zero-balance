// probe-v15-loading4.mjs — what's under the reference's spinner overlay:
// the fixed overlay's background, and whether the rail/topbar/content DOM
// exists behind it during the fetch window.
(() => {
  const out = {};
  const ov = [...document.querySelectorAll('div')].find(
    (el) => (el.getAttribute('class') || '') === 'fixed inset-0 flex items-center justify-center' && el.getBoundingClientRect().width > 100
  );
  if (!ov) return JSON.stringify({ overlay: null, note: 'spinner gone' });
  const cs = getComputedStyle(ov);
  out.overlay = { cls: ov.getAttribute('class'), bg: cs.backgroundColor, z: cs.zIndex, pe: cs.pointerEvents, html: ov.outerHTML.slice(0, 250) };
  // what's in the body around it?
  out.bodyChildren = [...document.body.children].map((c) => ({
    tag: c.tagName.toLowerCase(),
    id: c.id || null,
    cls: (c.getAttribute('class') || '').slice(0, 60),
    childCount: c.children.length,
  }));
  // is the app root mounted/empty?
  const root = document.querySelector('#root, #__next, [id*="root"]');
  out.rootState = root ? { id: root.id, childCount: root.children.length, textLen: root.textContent.trim().length } : null;
  out.hasRail = !!document.querySelector('aside');
  out.hasHeader = !!document.querySelector('header');
  out.dataLoaded = /\$[\d,]+\.\d{2}/.test(document.body.textContent);
  return JSON.stringify(out, null, 1);
})()
