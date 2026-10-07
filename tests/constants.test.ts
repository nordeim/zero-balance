import { describe, expect, it } from "vitest";
import {
  ASSET_LABELS,
  ASSET_TYPES,
  CLASSIFICATION_LABELS,
  CLASSIFICATIONS,
  COLORS,
  FREQUENCIES,
  FREQUENCY_LABELS,
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
