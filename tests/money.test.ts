import { describe, expect, it } from "vitest";
import {
  formatMoney,
  formatMoneyShort,
  formatPercent,
  formatNetWorth,
  formatRatio,
  formatSignedMoney,
  fromCents,
  percentValue,
  sumAmounts,
  toCents,
} from "@/lib/money";

// The arithmetic seam: every aggregation converts to integer cents first so
// IEEE-754 drift (0.1 + 0.2) can never reach a total, and display formatting
// mirrors the reference's "$5,000.00" with thousands separators + 2 decimals.

describe("toCents / fromCents", () => {
  it("converts decimals to integer cents", () => {
    expect(toCents(5000)).toBe(500000);
    expect(toCents(25)).toBe(2500);
    expect(toCents(0.1)).toBe(10);
  });

  it("rounds the cent boundary honestly under IEEE-754", () => {
    // 1.005's binary representation is just BELOW the .5 boundary
    // (1.00499…), so Math.round lands on 100 cents — documented JS
    // behavior, identical to the reference which also sends plain numbers.
    expect(toCents(1.005)).toBe(100);
    expect(toCents(19.999)).toBe(2000); // 1999.899… → 2000
    expect(toCents(2.675)).toBe(268); // the classic 2.675 case
  });

  it("round-trips", () => {
    expect(fromCents(toCents(123.45))).toBe(123.45);
    expect(fromCents(toCents(0.1 + 0.2))).toBe(0.3);
  });
});

describe("sumAmounts", () => {
  it("sums exactly in integer-cent space — the 0.1 + 0.2 proof", () => {
    expect(sumAmounts([0.1, 0.2])).toBe(0.3);
    expect(sumAmounts([0.1, 0.2, 0.3])).toBe(0.6);
  });

  it("sums the reference's comma-scale values", () => {
    expect(sumAmounts([5200, 350])).toBe(5550);
    expect(sumAmounts([1850, 320, 65])).toBe(2235);
  });

  it("handles empty lists", () => {
    expect(sumAmounts([])).toBe(0);
  });
});

describe("formatMoney", () => {
  it("formats with thousands separators and 2 decimals", () => {
    expect(formatMoney(5000)).toBe("$5,000.00");
    expect(formatMoney(245950)).toBe("$245,950.00");
    expect(formatMoney(77.5)).toBe("$77.50");
    expect(formatMoney(0)).toBe("$0.00");
  });

  it("keeps a minus sign for negatives (no parentheses)", () => {
    expect(formatMoney(-245950)).toBe("-$245,950.00");
    expect(formatMoney(-0.5)).toBe("-$0.50");
  });
});

describe("formatSignedMoney", () => {
  it("prefixes + for positive net balances", () => {
    expect(formatSignedMoney(2065)).toBe("+$2,065.00");
  });

  it("prefixes - for negative net balances", () => {
    expect(formatSignedMoney(2065 - 5550)).toBe("-$3,485.00");
  });

  it("renders zero unsigned (the NET ZERO case)", () => {
    expect(formatSignedMoney(0)).toBe("$0.00");
  });
});

describe("formatMoneyShort / formatNetWorth", () => {
  it("drops cents for the tab headers", () => {
    expect(formatMoneyShort(80300)).toBe("$80,300");
    expect(formatMoneyShort(-245950)).toBe("-$245,950");
  });

  it("formatNetWorth keeps the 2-decimal long form", () => {
    expect(formatNetWorth(65300)).toBe("$65,300.00");
  });
});

describe("formatRatio", () => {
  it("renders the infinity symbol when there are no liabilities", () => {
    expect(formatRatio(null)).toBe("∞");
    expect(formatRatio(65300 / 0)).toBe("∞"); // Infinity
  });

  it("renders finite ratios with 1 decimal max", () => {
    expect(formatRatio(65300 / 311250)).toBe("0.2");
    expect(formatRatio(2)).toBe("2");
    expect(formatRatio(2.55)).toBe("2.6");
  });
});

describe("formatPercent / percentValue", () => {
  it("renders one decimal (the reference's 62.8% allocation)", () => {
    expect(formatPercent(3485, 5550)).toBe("62.8%");
    expect(formatPercent(0, 5550)).toBe("0.0%");
  });

  it("returns 0.0% when the whole is zero (empty workspace)", () => {
    expect(formatPercent(100, 0)).toBe("0.0%");
  });

  it("percentValue clamps progress bars to [0, 100]", () => {
    expect(percentValue(50, 100)).toBe(50);
    expect(percentValue(150, 100)).toBe(100);
    expect(percentValue(10, 0)).toBe(0);
  });
});
