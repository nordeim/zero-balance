(() => {
  const inner = document.querySelector("main .max-w-7xl");
  const first = inner?.firstElementChild;
  return JSON.stringify({ colW: first ? Math.round(first.getBoundingClientRect().width) : null });
})()
