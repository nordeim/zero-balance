(() => {
  // locate the sub-dialog panel (white rounded) and dump its vertical structure
  const isClone = !!document.querySelector("[role=dialog]") && [...document.querySelectorAll("[role=dialog]")].length > 1;
  let sub;
  if (isClone) {
    const panels = [...document.querySelectorAll("[role=dialog]")];
    sub = panels[panels.length - 1];
  } else {
    sub = [...document.querySelectorAll("h2")].find(h => /Edit Line Item/i.test(h.textContent || ""))?.closest("[class*=fixed]");
    if (sub) {
      sub = [...sub.querySelectorAll("div")].filter(d => {
        const cs = getComputedStyle(d);
        return cs.backgroundColor === "rgb(255, 255, 255)" && parseFloat(cs.borderRadius) >= 8 && d.getBoundingClientRect().width > 200 && d.getBoundingClientRect().height > 300;
      })[0];
    }
  }
  if (!sub) return JSON.stringify({ error: "no sub panel" });
  const r = sub.getBoundingClientRect();
  // dump the panel's structural children (header/form/footer) with heights
  const dump = [...sub.children].map(c => ({
    cls: (c.className || "").toString().slice(0, 50),
    tag: c.tagName, h: Math.round(c.getBoundingClientRect().height),
    childCount: c.querySelectorAll("*").length,
  }));
  // the form's field rows
  const form = sub.querySelector("form");
  const formChildren = form ? [...form.children].map(c => ({
    tag: c.tagName, h: Math.round(c.getBoundingClientRect().height),
    text: (c.textContent || "").trim().slice(0, 30),
    cls: (c.className || "").toString().slice(0, 40),
  })) : null;
  return JSON.stringify({ panelH: Math.round(r.height), dump, formChildren }, null, 1);
})()
