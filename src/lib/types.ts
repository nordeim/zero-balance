// Client-side domain types — decoupled from Prisma's generated types so the
// store and components never import server code. Field names mirror the
// reference app's API payloads (camelCase here; the reference's snake_case
// names like payment_method map to paymentMethod).

export type ItemType = "income" | "savings" | "expense";
export type Classification = "need" | "want" | "savings";
export type Frequency = "one-time" | "weekly" | "bi-weekly" | "monthly" | "quarterly" | "annually";
export type ItemStatus = "planned" | "active" | "completed";
// Line items have their own status trio (reference's calculator form).
export type LineItemStatus = "active" | "pending" | "cancelled";

export interface BudgetItem {
  id: string;
  type: ItemType;
  classification: Classification;
  amount: number;
  category: string;
  subcategory?: string | null;
  paymentMethod?: string | null;
  frequency: Frequency;
  date: string;
  recurring: boolean;
  status: ItemStatus;
  notes?: string | null;
  createdAt: string;
  updatedAt: string;
}

export interface ExpenseLineItem {
  id: string;
  budgetItemId: string;
  name: string;
  amount: number;
  frequency: Frequency;
  provider?: string | null;
  policyNumber?: string | null;
  paymentMethod?: string | null;
  startDate?: string | null;
  endDate?: string | null;
  status: LineItemStatus;
  notes?: string | null;
  createdAt: string;
  updatedAt: string;
}

export type AssetType =
  | "bank_account"
  | "superannuation"
  | "property"
  | "investment"
  | "vehicle"
  | "other";

export interface Asset {
  id: string;
  type: AssetType;
  name: string;
  institution?: string | null;
  accountNumber?: string | null;
  value: number;
  lastUpdated: string;
  notes?: string | null;
  createdAt: string;
  updatedAt: string;
}

export type LiabilityType =
  | "home_loan"
  | "personal_loan"
  | "credit_card"
  | "car_loan"
  | "student_loan"
  | "other";

export interface Liability {
  id: string;
  type: LiabilityType;
  name: string;
  institution?: string | null;
  accountNumber?: string | null;
  value: number;
  interestRate?: number | null;
  monthlyPayment?: number | null;
  lastUpdated: string;
  notes?: string | null;
  createdAt: string;
  updatedAt: string;
}

export interface SessionUser {
  id: string;
  email: string;
  name: string | null;
}

/** Form payloads (client -> API) — dates and numbers as the forms produce them. */
export interface BudgetItemFormData {
  type: ItemType;
  classification: Classification;
  amount: number;
  category: string;
  subcategory: string;
  paymentMethod: string;
  frequency: Frequency;
  date: string;
  recurring: boolean;
  status: ItemStatus;
  notes: string;
}

export interface LineItemFormData {
  name: string;
  amount: number;
  frequency: Frequency;
  provider: string;
  policyNumber: string;
  paymentMethod: string;
  startDate: string;
  endDate: string;
  status: LineItemStatus;
  notes: string;
}

export interface AssetFormData {
  type: AssetType;
  name: string;
  institution: string;
  accountNumber: string;
  value: number;
  lastUpdated: string;
  notes: string;
}

export interface LiabilityFormData {
  type: LiabilityType;
  name: string;
  institution: string;
  accountNumber: string;
  value: number;
  interestRate: string;
  monthlyPayment: string;
  lastUpdated: string;
  notes: string;
}

/** API payload for liability mutations — numeric/null rate + payment. */
export type LiabilityPayload = Omit<LiabilityFormData, "interestRate" | "monthlyPayment"> & {
  interestRate: number | null;
  monthlyPayment: number | null;
};
