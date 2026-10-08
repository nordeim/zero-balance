import { expect, test } from "@playwright/test";

// Empty states + content column (session-11 audit,
// docs/remediation-plan-v6.md G6/G12/G13). Measured live on the reference:
//
//   Items views (income/savings/expenses, including filter-to-zero): the
//   empty block is BARE — `text-center py-16` directly on the warm page bg,
//   NO white bordered card, NO tinted icon circle. The icon is a bare lucide
//   type icon (wallet / piggy-bank / receipt) `w-16 h-16 mx-auto mb-4
//   opacity-20` inheriting the near-black foreground rgb(10,10,10); heading
//   `mb-2` (8px); description 16px gray-500 rgb(107,114,128).
//
//   Net-worth tabs (inside the white rounded-2xl bordered card): same bare
//   icon treatment but circle-arrow-up (assets) / circle-arrow-down
//   (liabilities); heading mb-2; desc 16px; gradient Add button.
//
//   Content column: `min-h-screen p-4 md:p-8` OUTSIDE `max-w-7xl mx-auto` —
//   the column is min(vw − 256 − 64, 1280): 960px at a 1280 viewport and
//   1280px at ≥1568px (measured: reference cards 1280 @ x=448 at 1920).
//
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("empty states + content column (v6)", () => {
  test("items-view empty state is bare: no card, no circle, near-black icon, 16px desc (G12)", async ({
    page,
  }) => {
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByPlaceholder("Search income items...").fill("zzzz-no-match");
    await expect(page.getByText("No income items yet")).toBeVisible();

    const state = await page.evaluate(() => {
      const h = [...document.querySelectorAll("main h3, main h4")].find((x) =>
        /No income items yet/.test(x.textContent || ""),
      );
      if (!h) return null;
      const block = h.parentElement as HTMLElement;
      const bs = getComputedStyle(block);
      // climb one level: the ref renders the block directly on the page (no
      // white bordered card wrapper).
      const wrapper = block.parentElement as HTMLElement;
      const ws = getComputedStyle(wrapper);
      const svg = block.querySelector("svg");
      const scs = svg ? getComputedStyle(svg) : null;
      const r = svg ? svg.getBoundingClientRect() : null;
      const p = block.querySelector("p");
      return {
        blockClasses: block.className,
        blockBorder: `${bs.borderTopWidth} ${bs.borderTopStyle}`,
        wrapperBorder: `${ws.borderTopWidth} ${ws.borderTopStyle}`,
        wrapperBg: ws.backgroundColor,
        wrapperRadius: ws.borderRadius,
        icon: svg ? { w: Math.round(r!.width), h: Math.round(r!.height), color: scs!.color, opacity: scs!.opacity, mb: scs!.marginBottom } : null,
        iconClass: svg?.getAttribute("class") || null,
        headingMb: getComputedStyle(h).marginBottom,
        headingFs: getComputedStyle(h).fontSize,
        desc: p ? { size: getComputedStyle(p).fontSize, color: getComputedStyle(p).color } : null,
      };
    });

    expect(state).not.toBeNull();
    // Bare block: py-16 text-center, no border of its own…
    expect(state!.blockClasses.split(/\s+/).sort().join(" ")).toBe("py-16 text-center");
    expect(state!.blockBorder).toBe("0px solid");
    // …and NO card wrapper — the direct parent is the unstyled page column.
    expect(state!.wrapperBorder).toBe("0px solid");
    expect(state!.wrapperBg).toBe("rgba(0, 0, 0, 0)");
    expect(state!.wrapperRadius).toBe("0px");
    // Bare wallet icon: 64px, opacity 0.2, near-black, mb-4 (16px).
    expect(state!.iconClass).toContain("lucide-wallet");
    expect(state!.icon!.w).toBe(64);
    expect(state!.icon!.h).toBe(64);
    expect(state!.icon!.color).toBe("rgb(10, 10, 10)");
    expect(state!.icon!.opacity).toBe("0.2");
    expect(state!.icon!.mb).toBe("16px");
    // Heading mb-2 (8px) + text-xl (20px — the reference's empty-heading
    // size, measured live on its filtered income empty state; v11 G1) +
    // 16px gray-500 description.
    expect(state!.headingMb).toBe("8px");
    expect(state!.headingFs).toBe("20px");
    expect(state!.desc!.size).toBe("16px");
    expect(state!.desc!.color).toBe("rgb(107, 114, 128)");
  });

  test("net-worth liabilities empty state: circle-arrow-down, bare icon inside the card (G6)", async ({
    page,
  }) => {
    // Fixture: remove both seeded liabilities via the API (the spec shares
    // the seeded DB with the whole suite — restore in the same test).
    const list = await page.request.get("/api/liabilities");
    const { data } = (await list.json()) as { data: Array<Record<string, unknown>> };
    const original = data.map((l) => ({
      type: l.type,
      name: l.name,
      institution: l.institution,
      accountNumber: l.accountNumber,
      value: l.value,
      interestRate: l.interestRate,
      monthlyPayment: l.monthlyPayment,
      lastUpdated: l.lastUpdated,
      notes: l.notes,
    }));
    expect(original.length).toBeGreaterThan(0);
    for (const l of data) {
      await page.request.delete(`/api/liabilities/${l.id}`);
    }

    await page.goto("/networth");
    await page.getByRole("tab", { name: "Liabilities" }).click();
    await expect(page.getByText("No liabilities yet")).toBeVisible();

    const state = await page.evaluate(() => {
      const panel = document.querySelector('[role="tabpanel"][data-state="active"]');
      const h = [...(panel?.querySelectorAll("h3, h4") || [])].find((x) =>
        /No liabilities yet/.test(x.textContent || ""),
      );
      if (!h) return null;
      const block = h.parentElement as HTMLElement;
      const bs = getComputedStyle(block);
      const svg = block.querySelector("svg");
      const scs = svg ? getComputedStyle(svg) : null;
      const r = svg ? svg.getBoundingClientRect() : null;
      const p = block.querySelector("p");
      const btn = block.querySelector("button");
      return {
        blockClasses: block.className.replace(/\s+/g, " ").trim(),
        cardChrome: { border: `${bs.borderTopWidth} ${bs.borderTopStyle}`, bg: bs.backgroundColor, radius: bs.borderRadius, py: bs.paddingTop },
        iconClass: svg?.getAttribute("class") || null,
        icon: svg ? { w: Math.round(r!.width), color: scs!.color, opacity: scs!.opacity, mb: scs!.marginBottom } : null,
        circle: block.querySelector('div[class*="rounded-[9999px]"]') ? "PRESENT" : "ABSENT",
        headingMb: getComputedStyle(h).marginBottom,
        headingFs: getComputedStyle(h).fontSize,
        desc: p ? { size: getComputedStyle(p).fontSize, color: getComputedStyle(p).color } : null,
        btn: btn ? { text: (btn.textContent || "").trim(), bgImage: getComputedStyle(btn).backgroundImage.slice(0, 80) } : null,
      };
    });

    expect(state).not.toBeNull();
    // Reference net-worth empty state: ONE div carries the card chrome —
    // `text-center py-16 bg-white rounded-2xl` + a 1px border (measured
    // live on both of its tabs).
    expect(state!.blockClasses.split(/\s+/).sort().join(" ")).toBe("bg-white py-16 rounded-2xl text-center");
    expect(state!.cardChrome.border).toBe("1px solid");
    expect(state!.cardChrome.bg).toBe("rgb(255, 255, 255)");
    expect(state!.cardChrome.radius).toBe("16px");
    expect(state!.cardChrome.py).toBe("64px");
    // Bare circle-arrow-down icon (no tinted circle wrapper).
    expect(state!.iconClass).toContain("lucide-circle-arrow-down");
    expect(state!.icon!.w).toBe(64);
    expect(state!.icon!.color).toBe("rgb(10, 10, 10)");
    expect(state!.icon!.opacity).toBe("0.2");
    expect(state!.icon!.mb).toBe("16px");
    expect(state!.circle).toBe("ABSENT");
    // Heading mb-2 + text-xl 20px (v11 G1 — measured live on the ref's
    // liabilities empty state) + 16px gray-500 desc + the orange-gradient Add button.
    expect(state!.headingMb).toBe("8px");
    expect(state!.headingFs).toBe("20px");
    expect(state!.desc!.size).toBe("16px");
    expect(state!.desc!.color).toBe("rgb(107, 114, 128)");
    expect(state!.btn!.text).toBe("Add Liability");
    expect(state!.btn!.bgImage).toContain("linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))");

    // Restore the seeded liabilities exactly as they were — in REVERSE
    // capture order, so the recreated rows land with the same relative
    // createdAt ordering as the seed (GET orders by createdAt DESC; the
    // liabilities tab's type-group order follows it).
    for (const l of [...original].reverse()) {
      const res = await page.request.post("/api/liabilities", { data: l });
      expect(res.ok()).toBeTruthy();
    }
    await page.reload();
    await page.getByRole("tab", { name: "Liabilities" }).click();
    await expect(page.getByText("2 items · $311,250")).toBeVisible();
  });

  test("content column: padding outside max-w-7xl — 960px at 1280, 1280px at 1920 (G13)", async ({
    page,
  }) => {
    // The reference wraps `max-w-7xl mx-auto` INSIDE `min-h-screen p-4
    // md:p-8`, so the column = min(vw − 256 − 64, 1280). The clone had the
    // padding INSIDE the cap (column 64px too narrow ≥1568px).
    const columnWidth = async () =>
      page.evaluate(() => {
        const inner = document.querySelector("main .max-w-7xl");
        if (!inner) return null;
        const first = inner.firstElementChild as HTMLElement | null;
        return first ? Math.round(first.getBoundingClientRect().width) : null;
      });

    await page.setViewportSize({ width: 1920, height: 900 });
    for (const path of ["/dashboard", "/income", "/networth"]) {
      await page.goto(path);
      await expect(page.getByRole("heading", { name: "ZeroBalance" })).toBeVisible();
      const w = await columnWidth();
      expect(w, `${path} column at 1920`).toBe(1280);
    }

    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    expect(await columnWidth()).toBe(960);
  });
});
