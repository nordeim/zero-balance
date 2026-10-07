import { describe, expect, it } from "vitest";
import {
  ADD_BUTTON_GRADIENTS,
  ASSET_LABELS,
  ASSET_TYPES,
  CLASSIFICATION_BADGES,
  CLASSIFICATION_LABELS,
  CLASSIFICATIONS,
  COLORS,
  FREQUENCIES,
  FREQUENCY_BADGES,
  FREQUENCY_LABELS,
  GUIDELINE_ROWS,
  HEADER_CHIP_GRADIENTS,
  ITEM_STATUSES,
  ITEM_TYPES,
  LIABILITY_LABELS,
  LIABILITY_TYPES,
  STATUS_LABELS,
  TYPE_COLORS,
  TYPE_LABELS,
} from "@/lib/constants";

// The domain constants are the single source of truth for enums, labels,
// colors and icons — every option set below was recon-verified against the
// reference app's dropdowns.

describe("enum integrity", () => {
  it("ITEM_TYPES covers the reference's three item types", () => {
    expect([...ITEM_TYPES]).toEqual(["income", "savings", "expense"]);
  });

  it("FREQUENCIES covers the reference's six frequency options", () => {
    expect([...FREQUENCIES]).toEqual([
      "one-time",
      "weekly",
      "bi-weekly",
      "monthly",
      "quarterly",
      "annually",
    ]);
  });

  it("ITEM_STATUSES covers the reference's Planned/Active/Completed", () => {
    expect([...ITEM_STATUSES]).toEqual(["planned", "active", "completed"]);
  });

  it("ASSET_TYPES covers the reference's six asset types", () => {
    expect([...ASSET_TYPES]).toEqual([
      "bank_account",
      "superannuation",
      "property",
      "investment",
      "vehicle",
      "other",
    ]);
  });

  it("LIABILITY_TYPES covers the reference's six liability types", () => {
    expect([...LIABILITY_TYPES]).toEqual([
      "home_loan",
      "personal_loan",
      "credit_card",
      "car_loan",
      "student_loan",
      "other",
    ]);
  });
});

describe("label maps", () => {
  it("label every enum member (no undefined labels)", () => {
    for (const t of ASSET_TYPES) expect(ASSET_LABELS[t]).toBeTruthy();
    for (const t of LIABILITY_TYPES) expect(LIABILITY_LABELS[t]).toBeTruthy();
    for (const t of ITEM_TYPES) expect(TYPE_LABELS[t]).toBeTruthy();
    for (const c of CLASSIFICATIONS) expect(CLASSIFICATION_LABELS[c]).toBeTruthy();
    for (const f of FREQUENCIES) expect(FREQUENCY_LABELS[f]).toBeTruthy();
    for (const s of ITEM_STATUSES) expect(STATUS_LABELS[s]).toBeTruthy();
  });

  it("uses the reference's display strings", () => {
    expect(ASSET_LABELS.superannuation).toBe("Superannuation");
    expect(LIABILITY_LABELS.home_loan).toBe("Home Loan");
    expect(FREQUENCY_LABELS["bi-weekly"]).toBe("Bi-weekly");
    expect(TYPE_LABELS.savings).toBe("Savings");
  });
});

describe("the reference palette (measured :root vars)", () => {
  it("matches the recon-extracted hex values", () => {
    expect(COLORS.forestDark).toBe("#1a3a2e");
    expect(COLORS.forestMedium).toBe("#2d5a4a");
    expect(COLORS.limeGreen).toBe("#8fbc3f");
    expect(COLORS.orangeDark).toBe("#e07a3b");
    expect(COLORS.blueMedium).toBe("#3b7ea1");
    expect(COLORS.neutralWarm).toBe("#fafaf8");
  });

  it("assigns the per-type accents (income lime / savings blue / expense orange)", () => {
    expect(TYPE_COLORS.income).toBe("#8fbc3f");
    expect(TYPE_COLORS.savings).toBe("#3b7ea1");
    expect(TYPE_COLORS.expense).toBe("#e07a3b");
  });
});

// The maps below pin the reference's badge/gradient templates, extracted from
// its live DOM (computed styles) and minified bundle (maps b1e / x1e).

describe("frequency badge colors (bundle map b1e)", () => {
  it("colors each frequency like the reference", () => {
    expect(FREQUENCY_BADGES["one-time"]).toBe("bg-gray-100 text-gray-700");
    expect(FREQUENCY_BADGES.weekly).toBe("bg-blue-50 text-blue-700");
    expect(FREQUENCY_BADGES["bi-weekly"]).toBe("bg-blue-50 text-blue-700");
    expect(FREQUENCY_BADGES.monthly).toBe("bg-purple-50 text-purple-700");
    expect(FREQUENCY_BADGES.quarterly).toBe("bg-indigo-50 text-indigo-700");
    expect(FREQUENCY_BADGES.annually).toBe("bg-pink-50 text-pink-700");
  });

  it("labels every frequency with a badge class", () => {
    for (const f of FREQUENCIES) expect(FREQUENCY_BADGES[f]).toBeTruthy();
  });
});

describe("classification badge styles (bundle map x1e)", () => {
  it("matches the reference colors, borders and icons", () => {
    expect(CLASSIFICATION_BADGES.need.chip).toBe("bg-red-50 text-red-700 border-red-200");
    expect(CLASSIFICATION_BADGES.need.icon).toBe("circle-alert");
    expect(CLASSIFICATION_BADGES.want.chip).toBe("bg-blue-50 text-blue-700 border-blue-200");
    expect(CLASSIFICATION_BADGES.want.icon).toBe("heart");
    expect(CLASSIFICATION_BADGES.savings.chip).toBe("bg-green-50 text-green-700 border-green-200");
    expect(CLASSIFICATION_BADGES.savings.icon).toBe("piggy-bank");
  });
});

describe("per-view button gradients (computed styles on the live reference)", () => {
  it("maps every add-button surface to its 135deg gradient", () => {
    expect(ADD_BUTTON_GRADIENTS.dashboard).toBe("linear-gradient(135deg, #2d5a4a, #8fbc3f)");
    expect(ADD_BUTTON_GRADIENTS.income).toBe("linear-gradient(135deg, #8fbc3f, #b8d87e)");
    expect(ADD_BUTTON_GRADIENTS.savings).toBe("linear-gradient(135deg, #2c5f7c, #3b7ea1)");
    expect(ADD_BUTTON_GRADIENTS.expense).toBe("linear-gradient(135deg, #e07a3b, #f5a962)");
    expect(ADD_BUTTON_GRADIENTS.asset).toBe("linear-gradient(135deg, #2d5a4a, #8fbc3f)");
    expect(ADD_BUTTON_GRADIENTS.liability).toBe("linear-gradient(135deg, #e07a3b, #f5a962)");
    expect(ADD_BUTTON_GRADIENTS.calculator).toBe("linear-gradient(135deg, #e07a3b, #f5a962)");
  });

  it("maps the items-view header chips (white icons over type gradients)", () => {
    expect(HEADER_CHIP_GRADIENTS.income).toBe("linear-gradient(135deg, #8fbc3f, #b8d87e)");
    expect(HEADER_CHIP_GRADIENTS.savings).toBe("linear-gradient(135deg, #2c5f7c, #3b7ea1)");
    expect(HEADER_CHIP_GRADIENTS.expense).toBe("linear-gradient(135deg, #e07a3b, #f5a962)");
  });
});

describe("budget guidelines rows (live DOM)", () => {
  it("carries the tinted-card colors with borders", () => {
    expect(GUIDELINE_ROWS).toHaveLength(3);
    expect(GUIDELINE_ROWS[0]).toMatchObject({
      label: "Needs",
      percent: "~50%",
      bgColor: "#fff7f5",
      borderColor: "#fcddd5",
      color: "#e07a3b",
    });
    expect(GUIDELINE_ROWS[1]).toMatchObject({
      label: "Wants",
      percent: "~30%",
      bgColor: "#f0f7fb",
      borderColor: "#d4e9f5",
      color: "#3b7ea1",
    });
    expect(GUIDELINE_ROWS[2]).toMatchObject({
      label: "Savings",
      percent: "~20%",
      bgColor: "#f5f9f0",
      borderColor: "#dfecd0",
      color: "#8fbc3f",
    });
  });
});
