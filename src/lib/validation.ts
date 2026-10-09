// Zod schemas for every API input — the validation boundary. Unknown input
// is rejected with a 400 and a field-level message; nothing reaches Prisma
// unvalidated.

import { z } from "zod";
import {
  ASSET_TYPES,
  CLASSIFICATIONS,
  FREQUENCIES,
  ITEM_STATUSES,
  ITEM_TYPES,
  LIABILITY_TYPES,
  LINE_ITEM_STATUSES,
} from "./constants";

const money = z
  .number({ message: "Amount must be a number" })
  .finite()
  .min(0, "Amount must be at least 0")
  .max(1_000_000_000, "Amount is too large");

const isoDate = z
  .string()
  .regex(/^\d{4}-\d{2}-\d{2}$/, "Date must be YYYY-MM-DD")
  .refine((v) => {
    // A real calendar date: Date.parse alone ACCEPTS rollovers like
    // "2026-02-30" (→ March 2), so verify the components round-trip.
    const [y, m, d] = v.split("-").map(Number);
    const dt = new Date(Date.UTC(y, m - 1, d));
    return dt.getUTCFullYear() === y && dt.getUTCMonth() === m - 1 && dt.getUTCDate() === d;
  }, "Date is not a real calendar date");

/**
 * An optional date that also accepts an EMPTY STRING (the native date
 * inputs send "" when cleared — the line-item dialog's Start/End dates
 * are frequently blank). Normalizes "" → undefined before validating.
 */
const optionalIsoDate = z.preprocess(
  (v) => (typeof v === "string" && v.trim() === "" ? undefined : v),
  isoDate.optional(),
);

const optionalText = (max: number) =>
  z
    .string()
    .max(max)
    .transform((v) => v.trim())
    .transform((v) => (v === "" ? undefined : v))
    .optional();

export const emailSchema = z
  .string()
  .trim()
  .toLowerCase()
  .email("Enter a valid email address")
  .max(254);

export const passwordSchema = z
  .string()
  .min(8, "Password must be at least 8 characters")
  .max(128, "Password must be at most 128 characters");

export const registerSchema = z.object({
  email: emailSchema,
  password: passwordSchema,
  name: optionalText(120),
});

export const loginSchema = z.object({
  email: emailSchema,
  password: z.string().min(1, "Password is required").max(128),
});

// v21 G3: the register flow's email-verification gate (measured live on
// the reference — a 6-digit numeric code through six single-char inputs).
export const verifyEmailSchema = z.object({
  email: emailSchema,
  code: z
    .string()
    .regex(/^\d{6}$/, "Enter the 6-digit code from your email")
    .max(6),
});

export const resendSchema = z.object({
  email: emailSchema,
});

const budgetItemBase = {
  type: z.enum(ITEM_TYPES),
  classification: z.enum(CLASSIFICATIONS),
  amount: money,
  category: z.string().trim().min(1, "Category is required").max(120),
  subcategory: optionalText(120),
  paymentMethod: optionalText(120),
  frequency: z.enum(FREQUENCIES),
  date: isoDate,
  recurring: z.boolean().default(false),
  status: z.enum(ITEM_STATUSES).default("active"),
  notes: optionalText(2000),
};

export const createBudgetItemSchema = z.object(budgetItemBase);

export const updateBudgetItemSchema = z.object({
  type: z.enum(ITEM_TYPES).optional(),
  classification: z.enum(CLASSIFICATIONS).optional(),
  amount: money.optional(),
  category: z.string().trim().min(1).max(120).optional(),
  subcategory: optionalText(120),
  paymentMethod: optionalText(120),
  frequency: z.enum(FREQUENCIES).optional(),
  date: optionalIsoDate,
  recurring: z.boolean().optional(),
  status: z.enum(ITEM_STATUSES).optional(),
  notes: optionalText(2000),
});

const lineItemBase = {
  name: z.string().trim().min(1, "Item name is required").max(160),
  amount: money,
  frequency: z.enum(FREQUENCIES).default("monthly"),
  provider: optionalText(160),
  policyNumber: optionalText(80),
  paymentMethod: optionalText(120),
  startDate: optionalIsoDate,
  endDate: optionalIsoDate,
  // Line items carry their own status trio (reference's calculator form).
  status: z.enum(LINE_ITEM_STATUSES).default("active"),
  notes: optionalText(2000),
};

export const createLineItemSchema = z.object({
  budgetItemId: z.string().min(1),
  ...lineItemBase,
});

export const updateLineItemSchema = z.object({
  name: z.string().trim().min(1).max(160).optional(),
  amount: money.optional(),
  frequency: z.enum(FREQUENCIES).optional(),
  provider: optionalText(160),
  policyNumber: optionalText(80),
  paymentMethod: optionalText(120),
  startDate: optionalIsoDate,
  endDate: optionalIsoDate,
  status: z.enum(LINE_ITEM_STATUSES).optional(),
  notes: optionalText(2000),
});

const assetBase = {
  type: z.enum(ASSET_TYPES),
  name: z.string().trim().min(1, "Name is required").max(160),
  institution: optionalText(160),
  accountNumber: optionalText(80),
  value: money,
  lastUpdated: isoDate,
  notes: optionalText(2000),
};

export const createAssetSchema = z.object(assetBase);

export const updateAssetSchema = z.object({
  type: z.enum(ASSET_TYPES).optional(),
  name: z.string().trim().min(1).max(160).optional(),
  institution: optionalText(160),
  accountNumber: optionalText(80),
  value: money.optional(),
  lastUpdated: isoDate.optional(),
  notes: optionalText(2000),
});

const liabilityBase = {
  type: z.enum(LIABILITY_TYPES),
  name: z.string().trim().min(1, "Name is required").max(160),
  institution: optionalText(160),
  accountNumber: optionalText(80),
  value: money,
  interestRate: z
    .number()
    .finite()
    .min(0)
    .max(100)
    .optional()
    .nullable(),
  monthlyPayment: money.optional().nullable(),
  lastUpdated: isoDate,
  notes: optionalText(2000),
};

export const createLiabilitySchema = z.object(liabilityBase);

export const updateLiabilitySchema = z.object({
  type: z.enum(LIABILITY_TYPES).optional(),
  name: z.string().trim().min(1).max(160).optional(),
  institution: optionalText(160),
  accountNumber: optionalText(80),
  value: money.optional(),
  interestRate: z.number().finite().min(0).max(100).optional().nullable(),
  monthlyPayment: money.optional().nullable(),
  lastUpdated: isoDate.optional(),
  notes: optionalText(2000),
});
