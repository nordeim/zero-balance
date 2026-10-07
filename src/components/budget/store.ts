"use client";

// The single Zustand store: session, all server state (budget items, assets,
// liabilities), per-item line items, filter state, and the modal queue.
// Every mutation calls the typed API client, unwraps the envelope, updates
// local state, and surfaces success/error via toasts at the call site.

import { create } from "zustand";
import { api, ApiError } from "@/lib/api";
import { sumAmounts } from "@/lib/money";
import type {
  Asset,
  AssetFormData,
  BudgetItem,
  BudgetItemFormData,
  ExpenseLineItem,
  Liability,
  LiabilityFormData,
  LiabilityPayload,
  LineItemFormData,
  SessionUser,
} from "@/lib/types";

export interface ModalState {
  /** Add/Edit budget item; type presets the form when creating. */
  item: { mode: "create"; type: BudgetItem["type"] } | { mode: "edit"; item: BudgetItem } | null;
  /** Rent calculator, scoped to one expense item. */
  calculator: { item: BudgetItem } | null;
  /** Add/edit line item inside the calculator. */
  lineItem:
    | { mode: "create"; budgetItemId: string }
    | { mode: "edit"; lineItem: ExpenseLineItem }
    | null;
  asset: { mode: "create" } | { mode: "edit"; asset: Asset } | null;
  liability: { mode: "create" } | { mode: "edit"; liability: Liability } | null;
}

interface BudgetStore {
  user: SessionUser | null;
  booted: boolean;
  items: BudgetItem[];
  assets: Asset[];
  liabilities: Liability[];
  lineItems: Record<string, ExpenseLineItem[]>;
  modal: ModalState;

  boot: () => Promise<void>;
  refresh: () => Promise<void>;

  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string, name?: string) => Promise<void>;
  logout: () => Promise<void>;

  createItem: (data: BudgetItemFormData) => Promise<BudgetItem>;
  updateItem: (id: string, data: Partial<BudgetItemFormData>) => Promise<BudgetItem>;
  deleteItem: (id: string) => Promise<void>;

  loadLineItems: (budgetItemId: string) => Promise<ExpenseLineItem[]>;
  createLineItem: (data: LineItemFormData & { budgetItemId: string }) => Promise<void>;
  updateLineItem: (id: string, data: Partial<LineItemFormData>) => Promise<void>;
  deleteLineItem: (id: string) => Promise<void>;

  createAsset: (data: AssetFormData) => Promise<void>;
  updateAsset: (id: string, data: Partial<AssetFormData>) => Promise<void>;
  deleteAsset: (id: string) => Promise<void>;

  createLiability: (data: LiabilityPayload) => Promise<void>;
  updateLiability: (id: string, data: Partial<LiabilityPayload>) => Promise<void>;
  deleteLiability: (id: string) => Promise<void>;

  openItemModal: (modal: ModalState["item"]) => void;
  openCalculator: (item: BudgetItem) => void;
  openLineItemModal: (modal: ModalState["lineItem"]) => void;
  openAssetModal: (modal: ModalState["asset"]) => void;
  openLiabilityModal: (modal: ModalState["liability"]) => void;
  closeModals: () => void;
  /** Close ONLY the line-item dialog, keeping the calculator open (the
   *  reference's flow: save a line item → the calculator stays up with the
   *  recalculated banner + row). */
  closeLineItemModal: () => void;
}

function messageOf(error: unknown): string {
  if (error instanceof ApiError) return error.message;
  if (error instanceof Error) return error.message;
  return "Something went wrong";
}

export const useBudgetStore = create<BudgetStore>((set, get) => ({
  user: null,
  booted: false,
  items: [],
  assets: [],
  liabilities: [],
  lineItems: {},
  modal: {
    item: null,
    calculator: null,
    lineItem: null,
    asset: null,
    liability: null,
  },

  boot: async () => {
    try {
      const { user } = await api.get<{ user: SessionUser | null }>("/api/auth/me");
      set({ user, booted: true });
      if (user) await get().refresh();
    } catch {
      set({ user: null, booted: true });
    }
  },

  refresh: async () => {
    const [items, assets, liabilities] = await Promise.all([
      api.get<BudgetItem[]>("/api/budget-items"),
      api.get<Asset[]>("/api/assets"),
      api.get<Liability[]>("/api/liabilities"),
    ]);
    set({ items, assets, liabilities });
  },

  login: async (email, password) => {
    const { user } = await api.post<{ user: SessionUser }>("/api/auth/login", { email, password });
    set({ user });
    await get().refresh();
  },

  register: async (email, password, name) => {
    const { user } = await api.post<{ user: SessionUser }>("/api/auth/register", {
      email,
      password,
      name,
    });
    set({ user });
    await get().refresh();
  },

  logout: async () => {
    try {
      await api.post("/api/auth/logout", {});
    } finally {
      set({ user: null, items: [], assets: [], liabilities: [], lineItems: {} });
    }
  },

  createItem: async (data) => {
    const item = await api.post<BudgetItem>("/api/budget-items", data);
    set((s) => ({ items: [item, ...s.items] }));
    return item;
  },

  updateItem: async (id, data) => {
    const item = await api.patch<BudgetItem>(`/api/budget-items/${id}`, data);
    set((s) => ({ items: s.items.map((i) => (i.id === id ? item : i)) }));
    // A recalculated parent (line-item edit) may have changed the amount.
    if (get().modal.calculator?.item.id === id) {
      set({ modal: { ...get().modal, calculator: { item } } });
    }
    return item;
  },

  deleteItem: async (id) => {
    await api.delete(`/api/budget-items/${id}`);
    set((s) => {
      const lineItems = { ...s.lineItems };
      delete lineItems[id];
      return { items: s.items.filter((i) => i.id !== id), lineItems };
    });
  },

  loadLineItems: async (budgetItemId) => {
    const rows = await api.get<ExpenseLineItem[]>(
      `/api/line-items?budgetItemId=${encodeURIComponent(budgetItemId)}`,
    );
    set((s) => ({ lineItems: { ...s.lineItems, [budgetItemId]: rows } }));
    return rows;
  },

  createLineItem: async (data) => {
    const { lineItem, parentAmount } = await api.post<{
      lineItem: ExpenseLineItem;
      parentAmount: number | null;
    }>("/api/line-items", data);
    set((s) => ({
      lineItems: {
        ...s.lineItems,
        [lineItem.budgetItemId]: [lineItem, ...(s.lineItems[lineItem.budgetItemId] ?? [])],
      },
      items:
        parentAmount !== null
          ? s.items.map((i) => (i.id === lineItem.budgetItemId ? { ...i, amount: parentAmount } : i))
          : s.items,
    }));
  },

  updateLineItem: async (id, data) => {
    const { lineItem, parentAmount } = await api.patch<{
      lineItem: ExpenseLineItem;
      parentAmount: number | null;
    }>(`/api/line-items/${id}`, data);
    set((s) => ({
      lineItems: {
        ...s.lineItems,
        [lineItem.budgetItemId]: (s.lineItems[lineItem.budgetItemId] ?? []).map((li) =>
          li.id === id ? lineItem : li,
        ),
      },
      items:
        parentAmount !== null
          ? s.items.map((i) => (i.id === lineItem.budgetItemId ? { ...i, amount: parentAmount } : i))
          : s.items,
    }));
  },

  deleteLineItem: async (id) => {
    const { parentAmount } = await api.delete<{ deleted: boolean; parentAmount: number | null }>(
      `/api/line-items/${id}`,
    );
    set((s) => {
      const lineItems = { ...s.lineItems };
      let parentId: string | null = null;
      for (const [pid, rows] of Object.entries(lineItems)) {
        if (rows.some((r) => r.id === id)) {
          parentId = pid;
          lineItems[pid] = rows.filter((r) => r.id !== id);
        }
      }
      return {
        lineItems,
        items:
          parentAmount !== null && parentId
            ? s.items.map((i) => (i.id === parentId ? { ...i, amount: parentAmount } : i))
            : s.items,
      };
    });
  },

  createAsset: async (data) => {
    const asset = await api.post<Asset>("/api/assets", data);
    set((s) => ({ assets: [asset, ...s.assets] }));
  },

  updateAsset: async (id, data) => {
    const asset = await api.patch<Asset>(`/api/assets/${id}`, data);
    set((s) => ({ assets: s.assets.map((a) => (a.id === id ? asset : a)) }));
  },

  deleteAsset: async (id) => {
    await api.delete(`/api/assets/${id}`);
    set((s) => ({ assets: s.assets.filter((a) => a.id !== id) }));
  },

  createLiability: async (data) => {
    const liability = await api.post<Liability>("/api/liabilities", data);
    set((s) => ({ liabilities: [liability, ...s.liabilities] }));
  },

  updateLiability: async (id, data) => {
    const liability = await api.patch<Liability>(`/api/liabilities/${id}`, data);
    set((s) => ({ liabilities: s.liabilities.map((l) => (l.id === id ? liability : l)) }));
  },

  deleteLiability: async (id) => {
    await api.delete(`/api/liabilities/${id}`);
    set((s) => ({ liabilities: s.liabilities.filter((l) => l.id !== id) }));
  },

  openItemModal: (item) => set((s) => ({ modal: { ...s.modal, item } })),
  openCalculator: (item) => set((s) => ({ modal: { ...s.modal, calculator: { item } } })),
  openLineItemModal: (lineItem) => set((s) => ({ modal: { ...s.modal, lineItem } })),
  openAssetModal: (asset) => set((s) => ({ modal: { ...s.modal, asset } })),
  openLiabilityModal: (liability) => set((s) => ({ modal: { ...s.modal, liability } })),
  closeModals: () =>
    set({
      modal: { item: null, calculator: null, lineItem: null, asset: null, liability: null },
    }),
  closeLineItemModal: () => set((s) => ({ modal: { ...s.modal, lineItem: null } })),
}));

export { messageOf };
