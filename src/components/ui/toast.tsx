"use client";

// Toast system on @radix-ui/react-toast, styled to the reference's sonner
// positioning (top-center on mobile / bottom-right from sm, 420px max) with
// the pointer-events fix: the VIEWPORT is pointer-events-none so an empty
// toaster can never swallow clicks (the live app's container blocks the
// mobile hamburger — trap documented in AGENTS.md).

import * as React from "react";
import * as ToastPrimitive from "@radix-ui/react-toast";
import { CheckCircle2Icon, XCircleIcon } from "lucide-react";
import { cn } from "@/lib/utils";

type ToastVariant = "default" | "success" | "error";

export interface ToastItem {
  id: string;
  title: string;
  description?: string;
  variant?: ToastVariant;
}

const ToastContext = React.createContext<{
  toast: (t: Omit<ToastItem, "id">) => void;
} | null>(null);

export function ToastProvider({ children }: { children: React.ReactNode }) {
  const [toasts, setToasts] = React.useState<ToastItem[]>([]);

  const toast = React.useCallback((t: Omit<ToastItem, "id">) => {
    const id = Math.random().toString(36).slice(2);
    setToasts((prev) => [...prev, { ...t, id }]);
  }, []);

  return (
    <ToastContext.Provider value={{ toast }}>
      <ToastPrimitive.Provider swipeDirection="right" duration={4000}>
        {children}
        {toasts.map((t) => (
          <ToastPrimitive.Root
            key={t.id}
            className="zb-toast data-[swipe=move]:translate-x-[var(--radix-toast-swipe-move-x)] data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-80 data-[state=open]:slide-in-from-top-full data-[state=closed]:data-[swipe=end]:slide-out-to-right-full sm:data-[state=open]:slide-in-from-bottom-full"
            onOpenChange={(open) => {
              if (!open) setToasts((prev) => prev.filter((x) => x.id !== t.id));
            }}
          >
            {t.variant === "success" && (
              <CheckCircle2Icon className="h-4 w-4 shrink-0" style={{ color: "var(--lime-green)" }} />
            )}
            {t.variant === "error" && (
              <XCircleIcon className="h-4 w-4 shrink-0 text-red-600" />
            )}
            <div className="flex flex-col gap-0.5">
              <ToastPrimitive.Title className="text-sm font-medium">{t.title}</ToastPrimitive.Title>
              {t.description ? (
                <ToastPrimitive.Description className="text-xs" style={{ color: "rgb(107, 114, 128)" }}>
                  {t.description}
                </ToastPrimitive.Description>
              ) : null}
            </div>
          </ToastPrimitive.Root>
        ))}
        <ToastPrimitive.Viewport className="zb-toast-viewport" />
      </ToastPrimitive.Provider>
    </ToastContext.Provider>
  );
}

export function useToast() {
  const ctx = React.useContext(ToastContext);
  if (!ctx) throw new Error("useToast must be used within <ToastProvider>");
  return ctx;
}
