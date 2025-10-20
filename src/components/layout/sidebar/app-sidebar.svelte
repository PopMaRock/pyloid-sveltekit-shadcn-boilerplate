<script lang="ts" module>

  // This is sample data.
  const data = {
    user: {
      name: "CRL",
      class: "Toilet Warrior",
      avatar: "",
    },
    navMain: [
      {
        title: "Head",
        url: "", //the path to your page. So for example, "/dashboard"
        icon: Book,
        isActive: true,
        items: [],
      },
      {
        title: "Shoulders",
        url: "/CRL/characters",
        icon: Music,
        items: [],
      },
      {
        title: "Knees",
        url: "",
        icon: Video,
        items: [],
      },
      {
        title: "Toes",
        url: "",
        icon: Banknote,
        items: [],
      },
    ],
    experiences: [
      {
        name: "How to take heroin",
        url: "",
        icon: Syringe,
      },
      {
        name: "Succeed where Guy Fawkes failed.",
        url: "",
        icon: Bomb,
      },
      {
        name: "Cosplay as Netanyahooooo",
        url: "",
        icon: ZapIcon,
      },
    ],
  };
</script>

<script lang="ts">
  import NavMain from "./nav-main.svelte";
  import NavExperiences from "./nav-experiences.svelte";
  import NavUser from "./nav-user.svelte";
  import * as Sidebar from "$components/ui/sidebar/index.js";
  import type { ComponentProps } from "svelte";
  import { goto } from "$app/navigation";
    import { Banknote, Bomb, Book, Music, Syringe, Video, ZapIcon } from "lucide-svelte";

  let { ref = $bindable(null), collapsible = "icon", ...restProps }: ComponentProps<typeof Sidebar.Root> = $props();
</script>

<Sidebar.Root {collapsible} {...restProps}>
  <Sidebar.Header>
    <Sidebar.Menu>
      <Sidebar.MenuItem>
        <!-- svelte-ignore a11y_click_events_have_key_events -->
        <!-- svelte-ignore a11y_no_static_element_interactions -->
        <div class="flex items-center mt-2 cursor-pointer" onclick={() => goto("/")}>
          <div class="text-sidebar-primary-foreground flex items-center w-10">
            <img src="/pyloid_icon.png" class="align-center w-12" alt="Logo. Clicking it will tack ya hame" />
          </div>
          <div class="flex-1 text-left text-sm leading-tight truncate mt-1">
            <span class="truncate font-medium">&nbsp; &nbsp;Pyloid</span><br />
            <span class="truncate text-sm">&nbsp; &nbsp;Python &amp; Sveltekit</span>
          </div>
        </div>
        <!-- icon -->
      </Sidebar.MenuItem>
    </Sidebar.Menu>
  </Sidebar.Header>
  <Sidebar.Content>
    <NavMain items={data.navMain} />
    <NavExperiences experiences={data.experiences} />
  </Sidebar.Content>
  <Sidebar.Footer>
    <NavUser user={data.user} />
  </Sidebar.Footer>
  <Sidebar.Rail />
</Sidebar.Root>
