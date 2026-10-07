import { describe, expect, it } from "vitest";
import { sumLineItemAmounts } from "@/lib/line-item-service";

// The calculator's recalculation rule (pure form): the parent BudgetItem's
// amount is the sum of its line items in integer-cent space. E2E coverage
// of the DB round-trip lives in tests/e2e/calculator.spec.ts.

describe("sumLineItemAmounts", () => {
  it("sums the reference's calculator scenario ($25 single line)", () => {
    expect(sumLineItemAmounts([25])).toBe(25);
  });

  it("sums multiple lines exactly (float drift proof)", () => {
    expect(sumLineItemAmounts([0.1, 0.2, 0.3])).toBe(0.6);
    expect(sumLineItemAmounts([25, 40.5, 134.25])).toBe(199.75);
  });

  it("treats no line items as a $0.00 category total", () => {
    expect(sumLineItemAmounts([])).toBe(0);
  });

  it("is the exact rule the service persists to the parent item", () => {
    // The seed scenario from the e2e spec: one $25 line → parent $25.
    const lines = [25];
    expect(sumLineItemAmounts(lines)).toBe(25);
    // After deleting the line → parent back to $0.
    expect(sumLineItemAmounts([])).toBe(0);
  });
});
