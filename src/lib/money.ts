// Money helpers — the arithmetic seam.
//
// Amounts are stored and exchanged as user-entered decimals (API parity with
// the reference app, which sends plain JSON numbers), but EVERY aggregation
// converts to integer cents first so IEEE-754 drift (0.1 + 0.2) can never
// reach a total.
//
// Display formatting mirrors the reference's TWO formatters (verified against
// the live site + its JS bundle):
//   - plain:  "$" + toFixed(2), NO thousands separator — dashboard, item
//     views and calculator all render "$5000.00" (bundle: `"$"+t.toFixed(2)`).
//   - grouped: toLocaleString with 2 fraction digits — net worth ONLY
//     (bundle: `o.toLocaleString(void 0,{minimumFractionDigits:2,...})`).
// The asset-to-liability ratio renders `0.21:1` (toFixed(2), no spaces) or
// `∞:1` when there are no liabilities.

/** Convert a user-entered decimal to integer cents. 5000 -> 500000. */
export function toCents(amount: number): number {
  return Math.round(amount * 100);
}

/** Convert integer cents back to a display decimal. 500000 -> 5000. */
export function fromCents(cents: number): number {
  return cents / 100;
}

/** Sum a list of decimal amounts in integer-cent space. */
export function sumAmounts(amounts: number[]): number {
  return fromCents(amounts.reduce((acc, a) => acc + toCents(a), 0));
}

/**
 * Plain reference format: "$5000.00" — no thousands separator, 2 decimals.
 * Used by the dashboard, the items views and the calculator.
 */
export function formatMoney(amount: number): string {
  const abs = Math.abs(amount);
  const sign = amount < 0 ? "-" : "";
  return `${sign}$${abs.toFixed(2)}`;
}

/**
 * Plain format with an explicit leading sign: "+$3475.00" / "-$3485.00"
 * (the breakdown Net Balance row).
 */
export function formatSignedMoney(amount: number): string {
  if (amount === 0) return formatMoney(amount);
  const sign = amount > 0 ? "+" : "-";
  return `${sign}$${Math.abs(amount).toFixed(2)}`;
}

/**
 * Grouped format: "$25,000.00" — net worth surfaces ONLY (the summary card,
 * asset/liability amounts, tab headers).
 */
export function formatMoneyGrouped(amount: number): string {
  const abs = Math.abs(amount);
  const sign = amount < 0 ? "-" : "";
  return `${sign}$${abs.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

/** Net-worth style value with thousands separators: "$25,000.00". */
export function formatNetWorth(amount: number): string {
  return formatMoneyGrouped(amount);
}

/** Header-style format without cents: "$25,000" (the net-worth tab headers). */
export function formatMoneyShort(amount: number): string {
  const abs = Math.abs(amount);
  const sign = amount < 0 ? "-" : "";
  return `${sign}$${abs.toLocaleString("en-US", { maximumFractionDigits: 0 })}`;
}

/**
 * Ratio value with the reference's formatting: `.toFixed(2)` (always two
 * decimals — the reference renders "0.21:1") or the literal "∞" when there
 * are no liabilities. The caller appends ":1".
 */
export function formatRatio(ratio: number | null): string {
  if (ratio === null || !Number.isFinite(ratio)) return "∞";
  return ratio.toFixed(2);
}

/** Percentage with one decimal, clamped to [0, 100] for progress bars. */
export function formatPercent(part: number, whole: number): string {
  if (whole <= 0) return "0.0%";
  return `${((part / whole) * 100).toFixed(1)}%`;
}

export function percentValue(part: number, whole: number): number {
  if (whole <= 0) return 0;
  return Math.min(100, Math.max(0, (part / whole) * 100));
}
