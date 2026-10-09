"use client";

import * as React from "react";
import * as DialogPrimitive from "@radix-ui/react-dialog";
import {
  CalendarIcon,
  CircleAlertIcon,
  CreditCardIcon,
  DollarSignIcon,
  FileTextIcon,
  HeartIcon,
  PiggyBankIcon,
  RefreshCwIcon,
  TagIcon,
} from "lucide-react";
import { DialogPortal, DialogTitle, DialogCloseButton } from "@/components/ui/dialog";
import { useBudgetStore } from "./store";
import { COLORS, TYPE_COLORS, rgb } from "@/lib/constants";
import { formatMoney } from "@/lib/money";
import type { BudgetItem, Classification } from "@/lib/types";

/**
 * v28 G3 (docs/remediation-plan-v28.md) — the reference's read-only
 * "Budget Item Details" sheet, opened by ITEM-CARD BODY CLICK. Every
 * geometry/class/color below was measured live on the reference:
 *
 * - Overlay: `fixed inset-0 z-50` — rgba(26, 58, 46, 0.5) + blur(8px)
 *   (the same forest scrim the clone's zb-modal-overlay pins).
 * - Panel: bottom-sheet anchored at mobile (`bottom-0`, full width,
 *   rounded-t-3xl = 24px top corners), centered at md: (max-w-lg = 512px,
 *   rounded-2xl), `max-h-[85vh] overflow-y-auto`, shadow-2xl.
 * - The sticky header + 36×36 X close (the v27 ghost-icon family,
 *   DialogCloseButton). Body `p-6 space-y-6`: centered summary (type +
 *   classification pill badges, name text-2xl forest, amount text-4xl in
 *   the TYPE color), the tinted classification block, the fact rows
 *   (Date/Frequency/Recurring/Payment Method?/Status + a taller Notes?
 *   variant), and the Created/Last Updated meta footer.
 * - Radix gives the Escape + overlay-click close + focus trap (the
 *   reference's outside-click measured closing; Escape is the standing
 *   clone superset).
 */

/** Details-sheet classification family — measured on the reference. */
const DETAILS_CLS: Record<
  Classification,
  { bg: string; color: string; description: string; Icon: React.ComponentType<{ className?: string; style?: React.CSSProperties }> }
> = {
  need: {
    bg: "#fff7f5",
    color: COLORS.orangeDark,
    description: "Essential expenses like rent, utilities, and groceries",
    Icon: CircleAlertIcon,
  },
  want: {
    bg: "#f0f7fb",
    color: COLORS.blueMedium,
    description: "Discretionary spending like entertainment and dining out",
    Icon: HeartIcon,
  },
  savings: {
    bg: "#f5f9f0",
    color: COLORS.limeGreen,
    description: "Savings, investments, and future planning",
    Icon: PiggyBankIcon,
  },
};

/** The type badge bg — the type color at 12.5% alpha (measured). */
const typeBadgeBg = (type: BudgetItem["type"]): string => {
  const map: Record<BudgetItem["type"], string> = {
    income: "rgba(143, 188, 63, 0.125)",
    expense: "rgba(224, 122, 59, 0.125)",
    savings: "rgba(59, 126, 161, 0.125)",
  };
  return map[type];
};

const formatLongDate = (iso: string): string => {
  const d = new Date(`${iso}T00:00:00`);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" });
};

const formatShortDate = (iso: string): string => {
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
};

/** A standard fact row: icon + (label above, value below). */
function FactRow({
  label,
  value,
  Icon,
}: {
  label: string;
  value: string;
  Icon: React.ComponentType<{ className?: string; style?: React.CSSProperties }>;
}) {
  return (
    <div className="flex items-center gap-3 py-2">
      <Icon className="h-5 w-5 shrink-0" style={{ color: rgb.gray }} />
      <div className="flex-1">
        <p className="text-xs" style={{ color: rgb.gray }}>
          {label}
        </p>
        <p className="font-medium" style={{ color: COLORS.forestDark }}>
          {value}
        </p>
      </div>
    </div>
  );
}

export function ItemDetailsDialog() {
  const modal = useBudgetStore((s) => s.modal.details);
  const closeModals = useBudgetStore((s) => s.closeModals);
  if (!modal) return null;
  const { item } = modal;
  const cls = DETAILS_CLS[item.classification];
  const ClsIcon = cls.Icon;
  const typeColor = TYPE_COLORS[item.type];

  return (
    <DialogPrimitive.Root open onOpenChange={(open) => !open && closeModals()}>
      <DialogPortal>
        {/* The forest scrim + blur — inline-pinned (plan v7 G6: v4 computes
            named translucent colors as oklab; the reference renders plain
            rgba). No animation classes — the reference's sheet appears
            instantly (measured: zero animate-in classes on either layer). */}
        <DialogPrimitive.Overlay
          className="fixed inset-0 z-50"
          style={{
            backgroundColor: "rgba(26, 58, 46, 0.5)",
            backdropFilter: "blur(8px)",
            WebkitBackdropFilter: "blur(8px)",
          }}
        />
        <DialogPrimitive.Content
          aria-describedby={undefined}
          className="fixed bottom-0 left-1/2 z-50 max-h-[85vh] w-full max-w-lg -translate-x-1/2 overflow-y-auto rounded-t-3xl bg-white shadow-2xl md:bottom-auto md:top-1/2 md:-translate-y-1/2 md:rounded-2xl"
        >
          {/* Sticky header — the reference's border-b is the same
              #e5e7e3 family the clone's dialogs pin. */}
          <div
            className="sticky top-0 z-10 flex items-center justify-between rounded-t-3xl border-b bg-white px-6 py-4 md:rounded-t-2xl"
            style={{ borderColor: rgb.border }}
          >
            <DialogTitle className="text-lg font-bold" style={{ color: COLORS.forestDark }}>
              Budget Item Details
            </DialogTitle>
            <DialogCloseButton onClick={closeModals} />
          </div>

          <div className="space-y-6 p-6">
            {/* Summary — type + classification pill badges, name, amount. */}
            <div className="border-b pb-6 text-center">
              <div className="mb-3 flex items-center justify-center gap-2">
                <span
                  className="inline-flex items-center gap-2 rounded-full px-3 py-1 text-xs font-medium"
                  style={{ backgroundColor: typeBadgeBg(item.type), color: typeColor }}
                >
                  {item.type.toUpperCase()}
                </span>
                <span
                  className="inline-flex items-center gap-2 rounded-full border px-3 py-1 text-xs font-medium"
                  style={{ backgroundColor: cls.bg, color: cls.color }}
                >
                  <ClsIcon className="h-3 w-3" />
                  {item.classification.toUpperCase()}
                </span>
              </div>
              <h3 className="mb-2 text-2xl font-bold" style={{ color: COLORS.forestDark }}>
                {item.category}
              </h3>
              <p className="mt-4 text-4xl font-bold" style={{ color: typeColor }}>
                {formatMoney(item.amount)}
              </p>
            </div>

            {/* Classification block — tinted, icon-led. */}
            <div className="rounded-xl p-4" style={{ backgroundColor: cls.bg }}>
              <div className="flex items-start gap-3">
                <ClsIcon className="mt-0.5 h-5 w-5 shrink-0" style={{ color: cls.color }} />
                <div className="flex-1">
                  <p className="mb-1 font-semibold" style={{ color: cls.color }}>
                    {item.classification.charAt(0).toUpperCase() + item.classification.slice(1)}
                  </p>
                  <p className="text-sm" style={{ color: rgb.gray }}>
                    {cls.description}
                  </p>
                </div>
              </div>
            </div>

            {/* Facts — the reference's measured icon map. */}
            <div className="space-y-4">
              <FactRow label="Date" value={formatLongDate(item.date)} Icon={CalendarIcon} />
              <FactRow label="Frequency" value={item.frequency} Icon={RefreshCwIcon} />
              <FactRow label="Recurring" value={item.recurring ? "Yes" : "No"} Icon={TagIcon} />
              {item.paymentMethod ? (
                <FactRow label="Payment Method" value={item.paymentMethod} Icon={CreditCardIcon} />
              ) : null}
              <FactRow
                label="Status"
                value={item.status.charAt(0).toUpperCase() + item.status.slice(1)}
                Icon={DollarSignIcon}
              />
              {item.notes ? (
                <div className="flex items-start gap-3">
                  <FileTextIcon className="mt-0.5 h-5 w-5 shrink-0" style={{ color: rgb.gray }} />
                  <div className="flex-1">
                    <p className="mb-1 text-sm font-medium" style={{ color: COLORS.forestDark }}>
                      Notes
                    </p>
                    <p className="text-sm leading-relaxed" style={{ color: rgb.gray }}>
                      {item.notes}
                    </p>
                  </div>
                </div>
              ) : null}
            </div>

            {/* Meta footer — Created / Last Updated. */}
            <div className="border-t pt-4" style={{ borderColor: rgb.border }}>
              <div className="grid grid-cols-2 gap-4 text-xs">
                <div>
                  <p className="mb-1" style={{ color: rgb.gray }}>
                    Created
                  </p>
                  <p className="font-medium" style={{ color: COLORS.forestDark }}>
                    {formatShortDate(item.createdAt)}
                  </p>
                </div>
                <div>
                  <p className="mb-1" style={{ color: rgb.gray }}>
                    Last Updated
                  </p>
                  <p className="font-medium" style={{ color: COLORS.forestDark }}>
                    {formatShortDate(item.updatedAt)}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </DialogPrimitive.Content>
      </DialogPortal>
    </DialogPrimitive.Root>
  );
}
