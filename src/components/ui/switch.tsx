"use client";

import * as React from "react";
import * as SwitchPrimitives from "@radix-ui/react-switch";
import { cn } from "@/lib/utils";

const Switch = React.forwardRef<
  React.ElementRef<typeof SwitchPrimitives.Root>,
  React.ComponentPropsWithoutRef<typeof SwitchPrimitives.Root>
>(({ className, ...props }, ref) => (
  <SwitchPrimitives.Root
    className={cn(
      // Reference switch (measured live incl. flipping its own Recurring
      // switch, plan v9 G5): track 36×20, unchecked bg = input #e5e5e5,
      // CHECKED bg rgb(23,23,23) — its --primary is shadcn's #171717, not
      // the clone's brand forest — so the checked state is hex-pinned.
      // rounded-full → 9999px (the reference's build; v4 emits infinity).
      "peer inline-flex h-5 w-9 shrink-0 cursor-pointer items-center rounded-[9999px] border-2 border-transparent shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-[#171717] data-[state=unchecked]:bg-input",
      className,
    )}
    {...props}
    ref={ref}
  >
    <SwitchPrimitives.Thumb
      className={cn(
        // Reference thumb: white (#ffffff — its --background), ring-0 (the
        // clone's ring-1 ring-border + #fafaf8 thumb both drift).
        "pointer-events-none block h-4 w-4 rounded-[9999px] bg-white shadow-lg ring-0 transition-transform data-[state=checked]:translate-x-4 data-[state=unchecked]:translate-x-0",
      )}
    />
  </SwitchPrimitives.Root>
));
Switch.displayName = SwitchPrimitives.Root.displayName;

export { Switch };
