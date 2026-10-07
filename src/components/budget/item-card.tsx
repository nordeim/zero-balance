"use client";

// One budget item card — the dot + name header, the ellipsis action menu
// (Edit/Delete; expenses carry inline Edit + Calculate buttons), the colored
// amount, the classification/frequency/status badges and the date + payment
// footer. Classes and inline colors mirror the measured reference card.

import * as React from "react";
import {
  CalendarIcon,
  CalculatorIcon,
  CircleAlertIcon,
  CreditCardIcon,
  EllipsisVerticalIcon,
  PencilIcon,
  Trash2Icon,
} from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { useBudgetStore } from "./store";
import { formatMoney } from "@/lib/money";
import { TYPE_COLORS, rgb } from "@/lib/constants";
import type { BudgetItem } from "@/lib/types";
import { cn } from "@/lib/utils";

const CLASSIFICATION_BADGES: Record<
  BudgetItem["classification"],
  { chip: string; text: string; border: string }
> = {
  need: { chip: "bg-red-50", text: "text-red-700", border: "border-red-200" },
  want: { chip: "bg-blue-50", text: "text-blue-700", border: "border-transparent" },
  savings: { chip: "bg-green-50", text: "text-green-700", border: "border-transparent" },
};

const STATUS_BADGES: Record<BudgetItem["status"], { chip: string; text: string }> = {
  planned: { chip: "bg-amber-50", text: "text-amber-700" },
  active: { chip: "bg-slate-50", text: "text-slate-700" },
  completed: { chip: "bg-green-50", text: "text-green-700" },
};

function formatDate(iso: string): string {
  const d = new Date(`${iso}T00:00:00`);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
}

export function BudgetItemCard({ item }: { item: BudgetItem }) {
  const openItemModal = useBudgetStore((s) => s.openItemModal);
  const openCalculator = useBudgetStore((s) => s.openCalculator);
  const deleteItem = useBudgetStore((s) => s.deleteItem);
  const [confirming, setConfirming] = React.useState(false);
  const accent = TYPE_COLORS[item.type];
  const clsBadge = CLASSIFICATION_BADGES[item.classification];
  const statusBadge = STATUS_BADGES[item.status];

  return (
    <div
      className="group cursor-pointer rounded-xl bg-white p-5 transition-all duration-200 hover:shadow-lg"
      style={{ border: `1px solid ${rgb.border}`, boxShadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px" }}
    >
      <div className="mb-3 flex items-start justify-between">
        <div className="flex-1">
          <div className="mb-1 flex items-center gap-2">
            <div className="h-2 w-2 rounded-full" style={{ backgroundColor: accent }} />
            <h4 className="font-semibold" style={{ color: rgb.forestDark }}>
              {item.category}
            </h4>
          </div>
          <p className="text-sm" style={{ color: rgb.gray }}>
            {item.subcategory ?? ""}
          </p>
        </div>
        <div className="flex items-center gap-1">
          {item.type === "expense" && (
            <>
              <button
                type="button"
                className="inline-flex h-8 items-center gap-1 rounded-md px-2 text-xs font-medium text-white transition-opacity hover:opacity-90"
                style={{ backgroundColor: accent }}
                onClick={() => openItemModal({ mode: "edit", item })}
              >
                <PencilIcon className="h-3.5 w-3.5" />
                Edit
              </button>
              <button
                type="button"
                className="inline-flex h-8 items-center gap-1 rounded-md px-2 text-xs font-medium text-white transition-opacity hover:opacity-90"
                style={{ backgroundColor: rgb.forestMedium }}
                onClick={() => openCalculator(item)}
              >
                <CalculatorIcon className="h-3.5 w-3.5" />
                Calculate
              </button>
            </>
          )}
          <DropdownMenu>
            <DropdownMenuTrigger
              className="inline-flex h-9 w-9 items-center justify-center rounded-md opacity-0 transition-opacity hover:bg-accent focus-visible:opacity-100 group-hover:opacity-100 data-[state=open]:opacity-100"
              aria-label={`Actions for ${item.category}`}
            >
              <EllipsisVerticalIcon className="h-4 w-4" />
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              <DropdownMenuItem onSelect={() => openItemModal({ mode: "edit", item })}>
                <PencilIcon />
                Edit
              </DropdownMenuItem>
              <DropdownMenuItem
                className="text-red-600 focus:text-red-600"
                onSelect={() => setConfirming(true)}
              >
                <Trash2Icon />
                Delete
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>

      <div className="mb-4">
        <p className="text-2xl font-bold" style={{ color: accent }}>
          {formatMoney(item.amount)}
        </p>
      </div>

      <div className="mb-3 flex flex-wrap gap-2">
        <span
          className={cn(
            "inline-flex items-center rounded-md border px-2.5 py-0.5 text-xs font-semibold",
            clsBadge.chip,
            clsBadge.text,
            clsBadge.border,
          )}
        >
          <CircleAlertIcon className="mr-1 h-3 w-3" />
          {item.classification}
        </span>
        <span className="inline-flex items-center rounded-md border border-transparent bg-purple-50 px-2.5 py-0.5 text-xs font-semibold text-purple-700">
          {item.frequency}
        </span>
        <span
          className={cn(
            "inline-flex items-center rounded-md border border-transparent px-2.5 py-0.5 text-xs font-semibold",
            statusBadge.chip,
            statusBadge.text,
          )}
        >
          {item.status}
        </span>
        {item.recurring && (
          <span className="inline-flex items-center rounded-md border border-transparent bg-slate-50 px-2.5 py-0.5 text-xs font-semibold text-slate-700">
            recurring
          </span>
        )}
      </div>

      <div className="flex items-center justify-between text-xs" style={{ color: rgb.gray }}>
        <span className="flex items-center gap-1">
          <CalendarIcon className="h-3 w-3" />
          {formatDate(item.date)}
        </span>
        {item.paymentMethod ? (
          <span className="flex items-center gap-1">
            <CreditCardIcon className="h-3 w-3" />
            {item.paymentMethod}
          </span>
        ) : null}
      </div>

      {confirming && (
        <div
          className="mt-4 flex items-center justify-between rounded-lg p-3"
          style={{ backgroundColor: "rgb(254, 242, 242)" }}
        >
          <p className="text-sm text-red-700">Delete this item?</p>
          <div className="flex gap-2">
            <button
              type="button"
              className="rounded-md bg-white px-3 py-1 text-xs font-medium text-slate-700 shadow-sm"
              onClick={() => setConfirming(false)}
            >
              Cancel
            </button>
            <button
              type="button"
              className="rounded-md bg-red-600 px-3 py-1 text-xs font-medium text-white"
              onClick={() => void deleteItem(item.id)}
            >
              Delete
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
