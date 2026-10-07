"use client";

// The shared Income / Expenses / Savings view: page header with the type
// icon, "N items · $X" subtitle, the Add button, the search + category +
// frequency (+ payment method on expenses) filters, the item card grid, and
// the empty state. One component, driven by the route's type.

import * as React from "react";
import {
  PiggyBankIcon,
  PlusIcon,
  ReceiptIcon,
  SearchIcon,
  WalletIcon,
} from "lucide-react";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { useBudgetStore } from "./store";
import { useShallow } from "zustand/react/shallow";
import { BudgetItemCard } from "./item-card";
import { formatMoney, sumAmounts } from "@/lib/money";
import {
  ADD_BUTTON_GRADIENTS,
  HEADER_CHIP_GRADIENTS,
  TYPE_COLORS,
  rgb,
} from "@/lib/constants";
import { hexToRgba } from "@/lib/utils";
import type { ItemType } from "@/lib/types";

const META: Record<
  ItemType,
  {
    title: string;
    icon: React.ComponentType<{ className?: string; style?: React.CSSProperties }>;
    addLabel: string;
    searchPlaceholder: string;
    emptyTitle: string;
    emptyText: string;
  }
> = {
  income: {
    title: "Income",
    icon: WalletIcon,
    addLabel: "Add Income",
    searchPlaceholder: "Search income items...",
    emptyTitle: "No income items yet",
    emptyText: "Start by adding your first income source",
  },
  savings: {
    title: "Savings",
    icon: PiggyBankIcon,
    addLabel: "Add Savings",
    searchPlaceholder: "Search savings items...",
    emptyTitle: "No savings items yet",
    emptyText: "Start by adding your first savings goal",
  },
  expense: {
    title: "Expenses",
    icon: ReceiptIcon,
    addLabel: "Add Expense",
    searchPlaceholder: "Search expense items...",
    emptyTitle: "No expense items yet",
    emptyText: "Start by adding your first expense",
  },
};

const ALL = "__all__";

export function ItemsView({ type }: { type: ItemType }) {
  // useShallow: the selector derives an ARRAY (new reference on every
  // snapshot call) — without shallow comparison zustand v5's
  // useSyncExternalStore sees a changed snapshot every render and loops to
  // "Maximum update depth exceeded" (React #185) on the hydrated static
  // pages. useShallow returns the previous reference when the elements are
  // shallow-equal.
  const items = useBudgetStore(
    useShallow((s) => s.items.filter((i) => i.type === type)),
  );
  const openItemModal = useBudgetStore((s) => s.openItemModal);
  const meta = META[type];
  const Icon = meta.icon;
  const accent = TYPE_COLORS[type];

  const [search, setSearch] = React.useState("");
  const [category, setCategory] = React.useState(ALL);
  const [frequency, setFrequency] = React.useState(ALL);
  const [paymentMethod, setPaymentMethod] = React.useState(ALL);

  const categories = React.useMemo(
    () => Array.from(new Set(items.map((i) => i.category))).sort(),
    [items],
  );
  const paymentMethods = React.useMemo(
    () =>
      Array.from(new Set(items.map((i) => i.paymentMethod).filter((p): p is string => !!p))).sort(),
    [items],
  );

  const filtered = items.filter((item) => {
    const q = search.trim().toLowerCase();
    if (q) {
      const haystack = `${item.category} ${item.subcategory ?? ""} ${item.notes ?? ""}`.toLowerCase();
      if (!haystack.includes(q)) return false;
    }
    if (category !== ALL && item.category !== category) return false;
    if (frequency !== ALL && item.frequency !== frequency) return false;
    if (paymentMethod !== ALL && (item.paymentMethod ?? "") !== paymentMethod) return false;
    return true;
  });

  const total = sumAmounts(filtered.map((i) => i.amount));

  return (
    <div className="mx-auto w-full max-w-7xl p-4 md:p-8">
      <div className="mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div className="flex items-center gap-3">
          {/* Gradient chip with a white icon (live reference DOM). */}
          <div
            className="flex h-12 w-12 items-center justify-center rounded-xl"
            style={{ background: HEADER_CHIP_GRADIENTS[type] }}
          >
            <Icon className="h-6 w-6 text-white" />
          </div>
          <div>
            <h1 className="text-3xl font-bold" style={{ color: rgb.forestDark }}>
              {meta.title}
            </h1>
            {/* The reference always renders "N items" here — even for 1. */}
            <p style={{ color: rgb.gray }}>
              {items.length} items · {formatMoney(total)}
            </p>
          </div>
        </div>
        <button
          type="button"
          className="zb-btn-add shrink-0"
          style={{ background: ADD_BUTTON_GRADIENTS[type] }}
          onClick={() => openItemModal({ mode: "create", type })}
        >
          <PlusIcon className="mr-2 h-5 w-5" />
          {meta.addLabel}
        </button>
      </div>

      <div className="mb-6 flex flex-col gap-3 md:flex-row">
        <div className="relative flex-1">
          <SearchIcon
            className="absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2"
            style={{ color: rgb.gray }}
          />
          <Input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder={meta.searchPlaceholder}
            className="pl-9"
            aria-label={meta.searchPlaceholder}
          />
        </div>
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 md:w-auto md:grid-cols-3 md:gap-3">
          <Select value={category} onValueChange={setCategory}>
            <SelectTrigger className="md:w-[160px]" aria-label="Filter by category">
              <SelectValue placeholder="All Categories" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value={ALL}>All Categories</SelectItem>
              {categories.map((c) => (
                <SelectItem key={c} value={c}>
                  {c}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
          <Select value={frequency} onValueChange={setFrequency}>
            <SelectTrigger className="md:w-[160px]" aria-label="Filter by frequency">
              <SelectValue placeholder="All Frequencies" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value={ALL}>All Frequencies</SelectItem>
              <SelectItem value="one-time">One-time</SelectItem>
              <SelectItem value="weekly">Weekly</SelectItem>
              <SelectItem value="bi-weekly">Bi-weekly</SelectItem>
              <SelectItem value="monthly">Monthly</SelectItem>
              <SelectItem value="quarterly">Quarterly</SelectItem>
              <SelectItem value="annually">Annually</SelectItem>
            </SelectContent>
          </Select>
          {type === "expense" && (
            <Select value={paymentMethod} onValueChange={setPaymentMethod}>
              <SelectTrigger className="md:w-[170px]" aria-label="Filter by payment method">
                <SelectValue placeholder="All Payment Methods" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value={ALL}>All Payment Methods</SelectItem>
                {paymentMethods.map((p) => (
                  <SelectItem key={p} value={p}>
                    {p}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          )}
        </div>
      </div>

      {filtered.length === 0 ? (
        <div className="flex flex-col items-center justify-center rounded-2xl bg-white py-16 text-center" style={{ border: `1px solid ${rgb.border}` }}>
          <div
            className="mb-4 flex h-16 w-16 items-center justify-center rounded-full"
            style={{ backgroundColor: hexToRgba(accent, 0.125) }}
          >
            <Icon className="h-8 w-8" style={{ color: accent }} />
          </div>
          <h3 className="mb-1 text-lg font-semibold" style={{ color: rgb.forestDark }}>
            {meta.emptyTitle}
          </h3>
          <p className="mb-6 text-sm" style={{ color: rgb.gray }}>
            {meta.emptyText}
          </p>
          <button
            type="button"
            className="zb-btn-add"
            style={{ background: ADD_BUTTON_GRADIENTS[type] }}
            onClick={() => openItemModal({ mode: "create", type })}
          >
            <PlusIcon className="mr-2 h-5 w-5" />
            {meta.addLabel}
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
          {filtered.map((item) => (
            <BudgetItemCard key={item.id} item={item} />
          ))}
        </div>
      )}
    </div>
  );
}
