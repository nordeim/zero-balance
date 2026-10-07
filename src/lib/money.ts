// Money helpers — the arithmetic seam.
//
// Amounts are stored and exchanged as user-entered decimals (API parity with
// the reference app, which sends plain JSON numbers), but EVERY aggregation
// converts to integer cents first so IEEE-754 drift (0.1 + 0.2) can never
// reach a total. Display formatting mirrors the reference: "$5,000.00" with
// thousands separators, 2 decimals.

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

/** Format a decimal as "$5,000.00" (no sign). Negative amounts keep "-". */
export function formatMoney(amount: number): string {
  const abs = Math.abs(amount);
  const sign = amount < 0 ? "-" : "";
  return `${sign}$${abs.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

/** Format a decimal with an explicit leading sign: "+$5,000.00" / "-$1,500.00". */
export function formatSignedMoney(amount: number): string {
  if (amount === 0) return formatMoney(amount);
  const abs = Math.abs(amount);
  const sign = amount > 0 ? "+" : "-";
  return `${sign}$${abs.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

/** Format a net-worth style value with thousands separators: "$25,000.00". */
export function formatNetWorth(amount: number): string {
  return formatMoney(amount);
}

/** Header-style format without cents: "$25,000" (the net-worth tab headers). */
export function formatMoneyShort(amount: number): string {
  const abs = Math.abs(amount);
  const sign = amount < 0 ? "-" : "";
  return `${sign}$${abs.toLocaleString("en-US", { maximumFractionDigits: 0 })}`;
}

/** Format a ratio value with the reference's infinity handling ("∞"). */
export function formatRatio(ratio: number | null): string {
  if (ratio === null || !Number.isFinite(ratio)) return "∞";
  return ratio.toLocaleString("en-US", { maximumFractionDigits: 1 });
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
