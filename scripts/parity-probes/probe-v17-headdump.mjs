// Dump the items-view header area (first 400 chars of main) to check format
(async () => {
  const main = document.querySelector("main") || document.body;
  return JSON.stringify({ url: location.pathname, head: main.innerText.slice(0, 350) });
})()
