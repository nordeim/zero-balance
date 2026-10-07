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

// ---------------------------------------------------------------------------
// Badge style maps — extracted verbatim from the reference's minified bundle
// (maps `b1e` for frequencies, `x1e` for classifications) and verified on the
// live DOM. `icon` names map to lucide components at the call sites.
// ---------------------------------------------------------------------------

/** Frequency badge chip classes (reference map b1e). */
export const FREQUENCY_BADGES: Record<Frequency, string> = {
  "one-time": "bg-gray-100 text-gray-700",
  weekly: "bg-blue-50 text-blue-700",
  "bi-weekly": "bg-blue-50 text-blue-700",
  monthly: "bg-purple-50 text-purple-700",
  quarterly: "bg-indigo-50 text-indigo-700",
  annually: "bg-pink-50 text-pink-700",
};

/** Classification badge styles (reference map x1e). */
export const CLASSIFICATION_BADGES: Record<
  Classification,
  { chip: string; icon: "circle-alert" | "heart" | "piggy-bank" }
> = {
  need: { chip: "bg-red-50 text-red-700 border-red-200", icon: "circle-alert" },
  want: { chip: "bg-blue-50 text-blue-700 border-blue-200", icon: "heart" },
  savings: { chip: "bg-green-50 text-green-700 border-green-200", icon: "piggy-bank" },
};

// ---------------------------------------------------------------------------
// Per-view gradients — measured as computed styles on the live reference
// (135deg pairs). The reference renders a DIFFERENT gradient per surface; the
// clone's solid-lime button was a session-1 approximation.
// ---------------------------------------------------------------------------

export const ADD_BUTTON_GRADIENTS = {
  /** Dashboard header "Add Item" + networth "Add Asset" — forest → lime. */
  dashboard: "linear-gradient(135deg, #2d5a4a, #8fbc3f)",
  income: "linear-gradient(135deg, #8fbc3f, #b8d87e)",
  savings: "linear-gradient(135deg, #2c5f7c, #3b7ea1)",
  expense: "linear-gradient(135deg, #e07a3b, #f5a962)",
  asset: "linear-gradient(135deg, #2d5a4a, #8fbc3f)",
  liability: "linear-gradient(135deg, #e07a3b, #f5a962)",
  /** Calculator "Add Item" (sm) — orange. */
  calculator: "linear-gradient(135deg, #e07a3b, #f5a962)",
} as const;

/** Items-view header icon chips — white icons over type gradients. */
export const HEADER_CHIP_GRADIENTS: Record<ItemType, string> = {
  income: "linear-gradient(135deg, #8fbc3f, #b8d87e)",
  savings: "linear-gradient(135deg, #2c5f7c, #3b7ea1)",
  expense: "linear-gradient(135deg, #e07a3b, #f5a962)",
};

// ---------------------------------------------------------------------------
// Budget Guidelines rows — tinted, bordered cards (live DOM), replacing the
// session-1 bare-chip approximation.
// ---------------------------------------------------------------------------

export const GUIDELINE_ROWS = [
  {
    label: "Needs",
    percent: "~50%",
    description: "Essential expenses like rent, utilities, groceries",
    bgColor: "#fff7f5",
    borderColor: "#fcddd5",
    color: "#e07a3b",
  },
  {
    label: "Wants",
    percent: "~30%",
    description: "Discretionary spending like entertainment, dining out",
    bgColor: "#f0f7fb",
    borderColor: "#d4e9f5",
    color: "#3b7ea1",
  },
  {
    label: "Savings",
    percent: "~20%",
    description: "Emergency fund, retirement, investments",
    bgColor: "#f5f9f0",
    borderColor: "#dfecd0",
    color: "#8fbc3f",
  },
] as const;
