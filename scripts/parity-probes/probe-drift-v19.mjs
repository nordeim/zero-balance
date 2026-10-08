// v19 session: reference data-drift probe — the 13th consecutive check.
// Captures the dashboard hero figures + the items-view census that the
// drift check has pinned since session 19.
(() => {
  const out = {};
  const hero = [...document.querySelectorAll('h3')].find((h) => /NET ZERO GOAL/i.test((h.textContent || '')));
  if (hero) {
    const card = hero.closest('div[class*="rounded"]');
    out.heroText = (card.innerText || '').split('\n').slice(0, 12).filter(Boolean);
  }
  // guideline percentages
  out.guidelines = [...document.querySelectorAll('div,span,p')].map((el) => el.textContent || '').filter((t) => /^\d+\.\d%$/.test(t.trim())).slice(0, 3);
  return JSON.stringify(out, null, 1);
})()
