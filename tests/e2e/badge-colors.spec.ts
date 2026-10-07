import { expect, test } from "@playwright/test";

// Item-card badge computed colors (session-15 audit,
// docs/remediation-plan-v8.md G2):
//
// The reference renders every chip with the plain Tailwind v3 palette —
// measured live (2026-10-08) on its income/expenses cards:
//   need       bg rgb(254,242,242)  text rgb(185,28,28)   border rgb(254,202,202)
//   want       bg rgb(239,246,255)  text rgb(29,78,216)   border rgb(191,219,254)
//   savings    bg rgb(240,253,244)  text rgb(21,128,61)   border rgb(187,247,208)
//   monthly    bg rgb(250,245,255)  text rgb(126,34,206)
//   active     bg rgb(248,250,252)  text rgb(51,65,85)
//   Recurring  bg rgb(240,253,244)  text rgb(21,128,61)   (measured after
//              flipping the reference item's Recurring switch on — its live
//              items ship recurring=false, so no badge renders at rest)
//
// The clone carried the same VALUES through named v3 classes — but Tailwind
// v4 computes them in Lab color space (`lab(97.16 3 -4.13)` etc.), exactly
// the drift AGENTS.md forbids on parity surfaces. These specs pin the
// plain-rgb computed styles; the fix hex-pins the classes.
// Contexts arrive AUTHENTICATED (setup-project storageState).
//
// The item-view pages are prerendered with an empty store — wait for the
// seeded card heading before querying badges (the prerender race convention).

type ChipStyle = { bg: string | null; color: string | null; border: string | null };

function chipProbe(page: import("@playwright/test").Page, cardText: string, chip: string) {
  return page.evaluate(
    ({ cardText, chip }) => {
      const card = [...document.querySelectorAll("main .group")].find((d) =>
        (d.textContent || "").includes(cardText),
      );
      if (!card) return null;
      const el = [...card.querySelectorAll("span")].find(
        (s) => (s.textContent || "").trim() === chip && s.querySelector("svg"),
      ) || [...card.querySelectorAll("span")].find(
        (s) => (s.textContent || "").trim() === chip,
      );
      if (!el) return null;
      const cs = getComputedStyle(el);
      return {
        bg: cs.backgroundColor,
        color: cs.color,
        border: `${cs.borderWidth} ${cs.borderColor}`,
      } satisfies { bg: string; color: string; border: string };
    },
    { cardText, chip },
  );
}

test.describe("item-card badge colors (v8 G2 — plain rgb, not lab)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
  });

  test("need badge: red-50/red-700/red-200 as plain rgb", async ({ page }) => {
    const chip = (await chipProbe(page, "Salary", "need")) as ChipStyle;
    expect(chip).not.toBeNull();
    expect(chip!.bg).toBe("rgb(254, 242, 242)");
    expect(chip!.color).toBe("rgb(185, 28, 28)");
    expect(chip!.border).toBe("1px rgb(254, 202, 202)");
  });

  test("want badge: blue-50/blue-700/blue-200 as plain rgb", async ({ page }) => {
    const chip = (await chipProbe(page, "Freelance", "want")) as ChipStyle;
    expect(chip).not.toBeNull();
    expect(chip!.bg).toBe("rgb(239, 246, 255)");
    expect(chip!.color).toBe("rgb(29, 78, 216)");
    expect(chip!.border).toBe("1px rgb(191, 219, 254)");
  });

  test("monthly frequency badge: purple-50/purple-700 as plain rgb", async ({ page }) => {
    const chip = (await chipProbe(page, "Salary", "monthly")) as ChipStyle;
    expect(chip).not.toBeNull();
    expect(chip!.bg).toBe("rgb(250, 245, 255)");
    expect(chip!.color).toBe("rgb(126, 34, 206)");
  });

  test("weekly frequency badge: blue-50/blue-700 as plain rgb", async ({ page }) => {
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Groceries" })).toBeVisible();
    const chip = (await chipProbe(page, "Groceries", "weekly")) as ChipStyle;
    expect(chip).not.toBeNull();
    expect(chip!.bg).toBe("rgb(239, 246, 255)");
    expect(chip!.color).toBe("rgb(29, 78, 216)");
  });

  test("savings classification badge: green family as plain rgb", async ({ page }) => {
    await page.goto("/savings");
    await expect(page.getByRole("heading", { name: "Emergency Fund" })).toBeVisible();
    const chip = (await chipProbe(page, "Emergency Fund", "savings")) as ChipStyle;
    expect(chip).not.toBeNull();
    expect(chip!.bg).toBe("rgb(240, 253, 244)");
    expect(chip!.color).toBe("rgb(21, 128, 61)");
    expect(chip!.border).toBe("1px rgb(187, 247, 208)");
  });

  test("Recurring badge: green-50/green-700 as plain rgb", async ({ page }) => {
    // Salary ships recurring=true in the seed, so the conditional badge
    // renders — the reference shows the same green pair when its item's
    // Recurring switch is on (measured live this session).
    const chip = (await chipProbe(page, "Salary", "Recurring")) as ChipStyle;
    expect(chip).not.toBeNull();
    expect(chip!.bg).toBe("rgb(240, 253, 244)");
    expect(chip!.color).toBe("rgb(21, 128, 61)");
  });

  test("status badge: slate-50/slate-700 as plain rgb", async ({ page }) => {
    const chip = (await chipProbe(page, "Salary", "active")) as ChipStyle;
    expect(chip).not.toBeNull();
    expect(chip!.bg).toBe("rgb(248, 250, 252)");
    expect(chip!.color).toBe("rgb(51, 65, 85)");
  });

  test("expense-card Calculate button: orange-600 text + orange-200 border as plain rgb", async ({
    page,
  }) => {
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();
    const btn = await page.evaluate(() => {
      const card = [...document.querySelectorAll("main .group")].find((d) =>
        (d.textContent || "").includes("Rent"),
      );
      if (!card) return null;
      const b = [...card.querySelectorAll("button")].find(
        (x) => (x.textContent || "").trim() === "Calculate",
      );
      if (!b) return null;
      const cs = getComputedStyle(b);
      return { color: cs.color, border: `${cs.borderWidth} ${cs.borderColor}` };
    });
    expect(btn).not.toBeNull();
    expect(btn!.color).toBe("rgb(234, 88, 12)");
    expect(btn!.border).toBe("1px rgb(254, 215, 170)");
  });
});
