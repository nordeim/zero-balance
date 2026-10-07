(() => {
  const btns = [...document.querySelectorAll('button')].filter((b) => /Add (Asset|Liability|Income|Expense|Savings)/.test((b.textContent || '').trim()));
  return JSON.stringify(btns.slice(0, 3).map((b) => {
    const cs = getComputedStyle(b);
    return { text: (b.textContent || '').trim().slice(0, 16), bw: cs.borderWidth, bs: cs.borderStyle, bg: (cs.backgroundImage || 'none').slice(0, 90) };
  }), null, 1);
})()
