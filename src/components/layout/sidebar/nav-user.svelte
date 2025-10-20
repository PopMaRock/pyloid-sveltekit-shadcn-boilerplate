<script lang="ts">
  import { toggleMode } from "mode-watcher";
  import * as Avatar from "$components/ui/avatar/index.js";
  import * as DropdownMenu from "$components/ui/dropdown-menu/index.js";
  import LightSwitch from "$components/ui/light-switch/light-switch.svelte";
  import * as Sidebar from "$components/ui/sidebar/index.js";
  import { useSidebar } from "$components/ui/sidebar/index.js";
    import { LogOut } from "lucide-svelte";

  let { user }: { user?: { name?: string; class?: string; avatar?: string } } = $props();
  let personaSettingsIsOpen = $state(false);
  const sidebar = useSidebar();
</script>

<Sidebar.Menu>
  <Sidebar.MenuItem>
    <DropdownMenu.Root>
      <DropdownMenu.Trigger>
        {#snippet child({ props })}
          <Sidebar.MenuButton size="lg" class="mb-6 data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground" {...props}>
            <Avatar.Root class="size-8 rounded-lg">
              <Avatar.Image src={user?.avatar ??""} alt={user?.name ?? "CRL"} />
              <Avatar.Fallback class="rounded-lg">CN</Avatar.Fallback>
            </Avatar.Root>
            <div class="grid flex-1 text-left text-sm leading-tight">
              <span class="truncate font-medium">{user?.name ?? "CRL"}</span>
              <span class="truncate text-xs">{user?.class??"Svelte Donkey"}</span>
            </div>
            <!--<ChevronsUpDownIcon class="ml-auto size-4" />--> Icon
          </Sidebar.MenuButton>
        {/snippet}
      </DropdownMenu.Trigger>
      <DropdownMenu.Content
        class="w-(--bits-dropdown-menu-anchor-width) min-w-56 rounded-lg"
        side={sidebar.isMobile ? "bottom" : "right"}
        align="end"
        sideOffset={4}
      >
        <DropdownMenu.Label class="p-0 font-normal" onclick={() => (personaSettingsIsOpen = true)}>
          <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
            <Avatar.Root class="size-8 rounded-lg">
              <Avatar.Image src={user?.avatar??""} alt={user?.name??"CRL"} />
              <Avatar.Fallback class="rounded-lg">CN</Avatar.Fallback>
            </Avatar.Root>
            <div class="grid flex-1 text-left text-sm leading-tight">
              <span class="truncate font-medium">{user?.name ?? "CRL"}</span>
              <span class="truncate text-xs">{user?.class ?? "Svelte Donkey"}</span>
            </div>
          </div>
        </DropdownMenu.Label>
        <DropdownMenu.Separator />
        <DropdownMenu.Group>
          <DropdownMenu.Item class="cursor-pointer">
            Give money and/or abuse</DropdownMenu.Item
          >
        </DropdownMenu.Group>
        <DropdownMenu.Separator />
        <!--<DropdownMenu.Group>
					<DropdownMenu.Item>
						<CiWavyCheck />
						Account
					</DropdownMenu.Item>
				</DropdownMenu.Group>-->
        <DropdownMenu.Item class="cursor-pointer" onclick={() => toggleMode()}>
          <LightSwitch />
        </DropdownMenu.Item>
        <DropdownMenu.Separator />
        <DropdownMenu.Item class="cursor-pointer">
          <LogOut />
          Log out
        </DropdownMenu.Item>
      </DropdownMenu.Content>
    </DropdownMenu.Root>
  </Sidebar.MenuItem>
</Sidebar.Menu>
