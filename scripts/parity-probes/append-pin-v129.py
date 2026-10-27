#!/usr/bin/env python3
"""Append the v129 describe block to tests/e2e/calculator.spec.ts (the
line-append form — the v112 dashboard.spec + v120 networth + v121/v127
items + v123 calculator precedents: the file is ~1.8k lines, the block
appended at EOF). The TDD order: this pin runs RED against the CURRENT
(unrepaired) build FIRST — the hovered-color axes (the ghost-hover family
gap) — then the repair (hover:text-accent-foreground at
calculator-dialog.tsx:138/239/247) turns it GREEN."""

BLOCK = r'''

// ---------------------------------------------------------------------------
// v129 — plan F4 (docs/remediation-plan-v129.md): the CALCULATOR
// GHOST-HOVER FAMILY's OWN-HOVER END-STATE census at 1280 — the X + the
// row actions' TINT + COLOR axes. The never-measured COLOR path: the
// close family fully held at REST (the v59 F1 pin the X's {w,h} at 1280;
// the v49 F3 pin {36,36} at 640; the v53 F2 pin {29,36} at 390; the v87
// pin the at-rest chrome {radius 6px / bg transparent / border 0px /
// display flex} — every pinned axis STATIC chrome, the v87 spec's own
// comment); the v27 G1 pin holds the hover:bg-accent CLASS TOKEN on the
// ITEM-DIALOG X — a DIFFERENT element in a different file; the v45 pin
// holds the row's hover:shadow-md + the actions' REVEAL (the group-hover
// opacity path). The computed own-hover end-states — the pointer ON each
// button itself — held by NO spec at ANY viewport. Measured by the
// both-sides one-shot census xhover-arbit-v129.sh + the reference-side
// family census rowaction-hover-ref-v129.sh: the TINT axis IDENTICAL
// both sides (the hovered bg rgb(245,245,245) — the accent #f5f5f5);
// THE COLOR AXIS A CLONE GAP — the reference's ghost family carries
// hover:text-accent-foreground (the hovered color rgb(23,23,23) — the
// same shadcn ghost-icon family the v27 G1 record documents), the
// clone's three buttons (calculator-dialog.tsx:138 the X, :239 the edit,
// :247 the trash) carried hover:bg-accent alone (the hovered color
// staying rgb(10,10,10)). THE REPAIR: hover:text-accent-foreground
// added to all three — the v27 G1 precedent's own fix form. This pin
// locks the repaired contract: the ladders at-rest -> hovered ->
// restored, the row actions' revealed-at-rest colors (the trash KEEPS
// its red at rest — rgb(220,38,38) — the hover-only accent-foreground
// transition), and both hovered states' bg + color.
// ---------------------------------------------------------------------------
test.describe("calculator ghost-hover family own-hover end-state census at 1280 (v129 — plan F4)", () => {
  test("the X + the row actions' own-hover ladders — the accent tint + the repaired accent-foreground color, the at-rest red trash, the restore", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    // the settle pattern: the seeded count subtitle before interacting
    // (the items views' formatMoney — no grouping: "$2235.00").
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();

    // Open the Rent calculator (the hover-revealed Calculate action; the
    // native locator click IS the full pointer sequence — the v46 lesson).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(400);

    // The X's state read — the v87 finder family: the clone's
    // aria-label="Close" superset finder first, the geometric fallback
    // (the 36x36 button in the panel's top band) name-independent.
    const xState = () =>
      page.evaluate(() => {
        const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
          (d.textContent || "").includes("Rent Calculator"),
        ) as HTMLElement | undefined;
        if (!panel) return null;
        const btns = [...panel.querySelectorAll("button")];
        const close =
          btns.find((b) => (b.getAttribute("aria-label") || "") === "Close") ||
          btns.find((b) => {
            const r = b.getBoundingClientRect();
            return (
              Math.abs(r.width - 36) < 3 &&
              Math.abs(r.height - 36) < 3 &&
              r.top < panel.getBoundingClientRect().top + 80 &&
              !/^add item$/i.test((b.textContent || "").trim())
            );
          });
        if (!close) return null;
        const cs = getComputedStyle(close);
        const r = close.getBoundingClientRect();
        return {
          hoverMatch: close.matches(":hover"),
          bg: cs.backgroundColor,
          color: cs.color,
          radius: cs.borderRadius,
          w: Math.round(r.width),
          h: Math.round(r.height),
        };
      });

    // === THE X LADDER — the at-rest rung (the pointer parked at (5,5)) ===
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const xRest = await xState();
    expect(xRest).not.toBeNull();
    // The at-rest contract — the v87 family re-affirmed (the static
    // chrome: transparent bg, the #0a0a0a icon, 36x36, rounded-md).
    expect(xRest!).toEqual({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      radius: "6px",
      w: 36,
      h: 36,
    });

    // === THE X LADDER — the OWN-HOVERED rung (the real pointer on the X) ===
    await dialog.getByRole("button", { name: "Close" }).hover();
    await page.waitForTimeout(300);
    const xHover = await xState();
    // THE REPAIRED AXES: the accent tint + the accent-foreground color —
    // the reference's ghost family contract (rgb(23,23,23) = #171717).
    expect(xHover!).toEqual({
      hoverMatch: true,
      bg: "rgb(245, 245, 245)",
      color: "rgb(23, 23, 23)",
      radius: "6px",
      w: 36,
      h: 36,
    });

    // === THE X LADDER — the restored rung (the pointer re-parked) ===
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const xRestored = await xState();
    expect(xRestored!).toEqual({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      radius: "6px",
      w: 36,
      h: 36,
    });

    // === THE ROW-ACTION LADDERS (the fixture form — the v66/v123 twin
    // state: "Contents Insurance" $25 through the real Add Item flow). ===
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Contents Insurance")).toBeVisible();
    await page.waitForTimeout(300);

    // The row actions' state read — the row's two small buttons (<=34px
    // square, the row scoped: the X is in the header, never caught).
    const actsState = () =>
      page.evaluate(() => {
        const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
          (d.textContent || "").includes("Rent Calculator"),
        ) as HTMLElement | undefined;
        if (!panel) return null;
        const rows = [...panel.querySelectorAll("div")].filter((d) => {
          const t = d.innerText || "";
          return (
            /Contents Insurance/i.test(t) &&
            d.getBoundingClientRect().height > 80 &&
            d.getBoundingClientRect().height < 140
          );
        });
        const row = rows[0];
        if (!row) return null;
        const acts = [...row.querySelectorAll("button")].filter((b) => {
          const r = b.getBoundingClientRect();
          return Math.round(r.width) <= 34 && Math.round(r.height) <= 34;
        });
        return acts.map((b) => {
          const cs = getComputedStyle(b);
          return {
            hoverMatch: b.matches(":hover"),
            bg: cs.backgroundColor,
            color: cs.color,
          };
        });
      });

    // The row hover FIRST (the group-hover reveal — the v45 contract),
    // the pointer on the row's text: the actions revealed at their
    // at-rest colors (the trash KEEPS its red — the hover-only family).
    await dialog.getByText("Contents Insurance").hover();
    await page.waitForTimeout(300);
    const actsRest = await actsState();
    expect(actsRest).not.toBeNull();
    expect(actsRest!).toHaveLength(2);
    expect(actsRest![0]).toEqual({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
    });
    expect(actsRest![1]).toEqual({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(220, 38, 38)",
    });

    // The EDIT button's own-hovered state (the real pointer on the
    // button — the group-hover stays engaged: the pointer is inside
    // the row): the tint + THE REPAIRED color axis.
    await dialog.getByRole("button", { name: "Edit Contents Insurance" }).hover();
    await page.waitForTimeout(300);
    const editHover = await actsState();
    expect(editHover![0]).toEqual({
      hoverMatch: true,
      bg: "rgb(245, 245, 245)",
      color: "rgb(23, 23, 23)",
    });

    // The TRASH button's own-hovered state: the tint + THE REPAIRED
    // color axis (the red goes accent-foreground under hover — the
    // reference's own contract, measured live on its Rent calculator).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).hover();
    await page.waitForTimeout(300);
    const trashHover = await actsState();
    expect(trashHover![1]).toEqual({
      hoverMatch: true,
      bg: "rgb(245, 245, 245)",
      color: "rgb(23, 23, 23)",
    });

    // The fixture-restore: the destructive Delete through the confirm
    // bar, then restoreRent — the e2e convention: every calculator
    // add/delete ends with restoreRent (a missing restore poisons every
    // later spec's dashboard arithmetic).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await expect(dialog.getByText("Delete this line item?")).toBeVisible();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(dialog.getByText("Based on 0 items")).toBeVisible();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });
});
'''

with open("tests/e2e/calculator.spec.ts", "a", encoding="utf-8") as f:
    f.write(BLOCK)
print("v129 describe block appended to tests/e2e/calculator.spec.ts")
