<script lang="ts">
	import { Menubar as MenubarPrimitive } from "bits-ui";
	import type { Snippet } from "svelte";
	import { cn } from "$lib/utilities/utils.js";
	import { Square, X } from "lucide-svelte";
    import Minus from "@lucide/svelte/icons/minus";

	type Props = MenubarPrimitive.RootProps & {
		children?: Snippet;
		ondragstart?: (e: PointerEvent) => void;
		onminimize?: (e: MouseEvent) => void;
		onmaximize?: (e: MouseEvent) => void;
		onclose?: (e: MouseEvent) => void;
	};

	let { ref = $bindable(null), class: className, children, ondragstart, onminimize, onmaximize, onclose, ...restProps }: Props = $props();
</script>

<MenubarPrimitive.Root
	bind:ref
	data-slot="menubar"
	class={cn("bg-background shadow-xs flex h-9 items-center gap-1 rounded-md border p-1 justify-between", className)}
	{...restProps}
>
	<div class="flex flex-1 items-center gap-1" data-pyloid-drag-region>
		{#if children}
			{@render children()}
		{/if}
	</div>
	<div class="flex items-center gap-0.5">
		<button
			type="button"
			data-window-control
			onclick={onminimize}
			class="flex h-7 w-7 items-center justify-center rounded-sm transition-colors hover:bg-accent"
			aria-label="Minimise"
			title="Minimise"
		>
			<Minus class="h-4 w-4" />
		</button>
		<button
			type="button"
			data-window-control
			onclick={onmaximize}
			class="flex h-7 w-7 items-center justify-center rounded-sm transition-colors hover:bg-accent"
			aria-label="Maximize"
			title="Maximise"
		>
			<Square class="h-3.5 w-3.5" />
		</button>
		<button
			type="button"
			data-window-control
			onclick={onclose}
			class="flex h-7 w-7 items-center justify-center rounded-sm transition-colors hover:bg-destructive hover:text-destructive-foreground"
			aria-label="Close"
			title="Murder"
		>
			<X class="h-4 w-4" />
		</button>
	</div>
</MenubarPrimitive.Root>
