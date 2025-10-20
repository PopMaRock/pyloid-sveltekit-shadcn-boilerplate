<script>
  import { Button } from "$components/ui/button";
  import { rpc } from "pyloid-js";

  //these are demo functions. Can be deleted.
  let message = "";
  async function handleGreet() {
    message = await rpc.call("greet", { name: "John" });
  }
  function createWindow() {
    rpc.call("create_window");
  }
</script>

<div id="root">
  <div class="mx-16">
    <div class="flex flex-wrap items-center justify-between mt-10 gap-4">
      <h1 class="mt-10 text-4xl font-bold tracking-tight sm:text-6xl">Pyloid-Sveltekit-Shadcn</h1>
      <p class="mt-6 text-lg leading-8">
        Create a desktop app that looks like every other creation out there by forcing pyloid (against it's will) to leverage the power
        of Svelte-Shadcn and sveltekit.<br/>
        <br/><br/>
        Note to self - SSR works in dev but probably won't work in production. Not to worry. Keep avoiding release and it won't matter.
      </p>
      <div class="mt-10 flex items-center gap-x-6">
        <Button variant="secondary" class="text-sm font-semibold">Pyloid</Button>
        <Button variant="default" href="#" class="text-sm font-semibold leading-6">Sveltekit <span aria-hidden="true">→</span></Button>
      </div>
    </div>
  </div>
</div>
