(() => {
  const panel = document.querySelector('[role="tabpanel"][data-state="active"]') || document;
  const btns = [...panel.querySelectorAll('button')].filter((b) => /Add Liability/.test(b.textContent || ''));
  return JSON.stringify(btns.map((b) => {
    const cs = getComputedStyle(b);
    return {
      text: (b.textContent || '').trim(),
      bgImage: cs.backgroundImage.slice(0, 100),
      bg: cs.backgroundColor,
      color: cs.color,
      border: cs.borderColor,
      h: cs.height, w: Math.round(b.getBoundingClientRect().width),
      radius: cs.borderRadius,
      padding: cs.padding,
      svg: b.querySelectorAll('svg').length,
      font: cs.fontSize + '/' + cs.fontWeight,
    };
  }), null, 1);
})()
