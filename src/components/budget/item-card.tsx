"use client";

// One budget item card — the dot + name header, the per-classification /
// per-frequency badges, the conditional green "Recurring" badge, the always-
// slate status badge, the colored amount and the date + payment footer.
//
// Action chrome (live reference DOM):
//   - expense cards: a hover-revealed absolute Edit + Calculate button row
//     (white, shadow-md; Calculate carries text-orange-600 + orange border)
//   - income/savings cards: a hover-revealed ellipsis menu (Edit / Delete)
// The reference has NO delete affordance on expense cards; the clone keeps a
// superset delete via the edit dialog.

import * as React from "react";
import {
  CalculatorIcon,
  CalendarIcon,
  CircleAlertIcon,
  CreditCardIcon,
  EllipsisVerticalIcon,
  HeartIcon,
  PenIcon,
  PiggyBankIcon,
  RepeatIcon,
} from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { useToast } from "@/components/ui/toast";
import { messageOf, useBudgetStore } from "./store";
import { formatMoney } from "@/lib/money";
import {
  CLASSIFICATION_BADGES,
  FREQUENCY_BADGES,
  TYPE_COLORS,
  rgb,
} from "@/lib/constants";
import type { BudgetItem, Classification } from "@/lib/types";
import { cn } from "@/lib/utils";

/** Classification badge icons (reference map x1e: circle-alert / heart / piggy-bank). */
const CLASSIFICATION_ICONS: Record<
  Classification,
  React.ComponentType<{ className?: string }>
> = {
  need: CircleAlertIcon,
  want: HeartIcon,
  savings: PiggyBankIcon,
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
  const { toast } = useToast();
  const [confirming, setConfirming] = React.useState(false);
  const accent = TYPE_COLORS[item.type];
  const clsBadge = CLASSIFICATION_BADGES[item.classification];
  const ClsIcon = CLASSIFICATION_ICONS[item.classification];
  const freqBadge = FREQUENCY_BADGES[item.frequency] ?? "bg-[#f3f4f6] text-[#374151]";

  return (
    <div
      className={cn(
        "group cursor-pointer rounded-xl bg-white p-5 transition-all duration-200 hover:shadow-lg",
        item.type === "expense" && "relative",
      )}
      style={{ border: `1px solid ${rgb.border}`, boxShadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px" }}
    >
      {item.type === "expense" && (
        /* Hover-revealed action row (reference: absolute top-3 right-3, z-10,
           opacity-0 → group-hover:opacity-100; Edit = white/border-input with
           a pen icon, Calculate = white/text-orange-600/border-orange-200). */
        <div className="absolute top-3 right-3 z-10 flex gap-2 opacity-0 transition-opacity group-hover:opacity-100">
          <button
            type="button"
            title="Edit Category"
            className="inline-flex h-8 items-center justify-center gap-2 rounded-md border border-input bg-white px-3 text-xs font-medium shadow-md transition-colors hover:bg-[#f9fafb]"
            onClick={() => openItemModal({ mode: "edit", item })}
          >
            <PenIcon className="mr-1 h-3.5 w-3.5" />
            Edit
          </button>
          <button
            type="button"
            title="Open Calculator"
            className="inline-flex h-8 items-center justify-center gap-2 rounded-md border border-[#fed7aa] bg-white px-3 text-xs font-medium text-[#ea580c] shadow-md transition-colors hover:bg-[#fff7ed]"
            onClick={() => openCalculator(item)}
          >
            <CalculatorIcon className="mr-1 h-3.5 w-3.5" />
            Calculate
          </button>
        </div>
      )}

      <div className="mb-3 flex items-start justify-between">
        <div className={cn("flex-1", item.type === "expense" && "pr-24")}>
          <div className="mb-1 flex items-center gap-2">
            <div className="h-2 w-2 rounded-[9999px]" style={{ backgroundColor: accent }} />
            <h4 className="font-semibold" style={{ color: rgb.forestDark }}>
              {item.category}
            </h4>
          </div>
          <p className="text-sm" style={{ color: rgb.gray }}>
            {item.subcategory ?? ""}
          </p>
        </div>
        {item.type !== "expense" && (
          <DropdownMenu>
            <DropdownMenuTrigger
              className="inline-flex h-9 w-9 items-center justify-center rounded-md opacity-0 transition-opacity hover:bg-accent hover:text-accent-foreground focus-visible:opacity-100 group-hover:opacity-100 data-[state=open]:opacity-100"
              aria-label={`Actions for ${item.category}`}
            >
              <EllipsisVerticalIcon className="h-4 w-4" />
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              {/* Reference menu items are PLAIN TEXT — no icons (v6 G1). */}
              <DropdownMenuItem onSelect={() => openItemModal({ mode: "edit", item })}>
                Edit
              </DropdownMenuItem>
              <DropdownMenuItem
                className="text-[#dc2626] focus:text-[#dc2626]"
                onSelect={() => setConfirming(true)}
              >
                Delete
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        )}
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
          )}
        >
          <ClsIcon className="mr-1 h-3 w-3" />
          {item.classification}
        </span>
        <span
          className={cn(
            "inline-flex items-center rounded-md border border-transparent px-2.5 py-0.5 text-xs font-semibold",
            freqBadge,
          )}
        >
          {item.frequency}
        </span>
        {item.recurring && (
          <span className="inline-flex items-center rounded-md border border-transparent bg-[#f0fdf4] px-2.5 py-0.5 text-xs font-semibold text-[#15803d]">
            <RepeatIcon className="mr-1 h-3 w-3" />
            Recurring
          </span>
        )}
        <span className="inline-flex items-center rounded-md border border-transparent bg-[#f8fafc] px-2.5 py-0.5 text-xs font-semibold text-[#334155]">
          {item.status}
        </span>
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
              onClick={() =>
                // v18 G1 (third site): the delete failure must be CAUGHT,
                // not swallowed — the pre-fix `void deleteItem(item.id)`
                // left the rejection unhandled and silent (the same
                // accident as the net-worth confirm bars, same pass;
                // the EDIT dialog's own delete was always caught — this
                // is the card menu's inline confirm path). The reference's
                // failed delete is a silent no-op (card stays — measured
                // family); the clone keeps the surfaces and adds the
                // honest toast, matching the dialog's established text.
                deleteItem(item.id).catch((error: unknown) => {
                  toast({
                    title: "Could not delete the item",
                    description: messageOf(error),
                    variant: "error",
                  });
                })
              }
            >
              Delete
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
