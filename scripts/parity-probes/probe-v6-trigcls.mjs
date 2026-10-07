(() => {
  const b = document.querySelector('button[aria-label^="Actions for"]');
  return JSON.stringify({ cls: b?.className || null });
})()
