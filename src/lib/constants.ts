// Domain constants — the single source of truth for enums, labels, colors
// and icons shared by the API validators, the store, and the views.

export const ITEM_TYPES = ["income", "savings", "expense"] as const;
export type ItemType = (typeof ITEM_TYPES)[number];

export const CLASSIFICATIONS = ["need", "want", "savings"] as const;
export type Classification = (typeof CLASSIFICATIONS)[number];

export const FREQUENCIES = [
  "one-time",
  "weekly",
  "bi-weekly",
  "monthly",
  "quarterly",
  "annually",
] as const;
export type Frequency = (typeof FREQUENCIES)[number];

export const ITEM_STATUSES = ["planned", "active", "completed"] as const;
export type ItemStatus = (typeof ITEM_STATUSES)[number];

export const ASSET_TYPES = [
  "bank_account",
  "superannuation",
  "property",
  "investment",
  "vehicle",
  "other",
] as const;
export type AssetType = (typeof ASSET_TYPES)[number];

export const LIABILITY_TYPES = [
  "home_loan",
  "personal_loan",
  "credit_card",
  "car_loan",
  "student_loan",
  "other",
] as const;
export type LiabilityType = (typeof LIABILITY_TYPES)[number];

export const ASSET_LABELS: Record<AssetType, string> = {
  bank_account: "Bank Account",
  superannuation: "Superannuation",
  property: "Property",
  investment: "Investment",
  vehicle: "Vehicle",
  other: "Other",
};

export const LIABILITY_LABELS: Record<LiabilityType, string> = {
  home_loan: "Home Loan",
  personal_loan: "Personal Loan",
  credit_card: "Credit Card",
  car_loan: "Car Loan",
  student_loan: "Student Loan",
  other: "Other",
};

// The reference palette (measured :root CSS variables on the live app).
export const COLORS = {
  forestDark: "#1a3a2e",
  forestMedium: "#2d5a4a",
  limeGreen: "#8fbc3f",
  limeLight: "#b8d87e",
  orangeDark: "#e07a3b",
  orangeLight: "#f5a962",
  blueDark: "#2c5f7c",
  blueMedium: "#3b7ea1",
  neutralWarm: "#fafaf8",
} as const;

export const rgb = {
  forestDark: "rgb(26, 58, 46)",
  forestMedium: "rgb(45, 90, 74)",
  limeGreen: "rgb(143, 188, 63)",
  orangeDark: "rgb(224, 122, 59)",
  orangeLight: "rgb(245, 169, 98)",
  blueMedium: "rgb(59, 126, 161)",
  gray: "rgb(107, 114, 128)",
  border: "rgb(229, 231, 227)",
  cardTint: "rgb(245, 248, 245)",
} as const;

/** Per-type accent (dot, amount, icon, tint). */
export const TYPE_COLORS: Record<ItemType, string> = {
  income: COLORS.limeGreen,
  savings: COLORS.blueMedium,
  expense: COLORS.orangeDark,
};

export const TYPE_LABELS: Record<ItemType, string> = {
  income: "Income",
  savings: "Savings",
  expense: "Expense",
};

export const CLASSIFICATION_LABELS: Record<Classification, string> = {
  need: "need",
  want: "want",
  savings: "savings",
};

export const FREQUENCY_LABELS: Record<Frequency, string> = {
  "one-time": "One-time",
  weekly: "Weekly",
  "bi-weekly": "Bi-weekly",
  monthly: "Monthly",
  quarterly: "Quarterly",
  annually: "Annually",
};

export const STATUS_LABELS: Record<ItemStatus, string> = {
  planned: "planned",
  active: "active",
  completed: "completed",
};
