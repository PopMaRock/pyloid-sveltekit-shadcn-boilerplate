<script>
  import { baseAPI, rpc } from 'pyloid-js';

  let message = '';
  async function handleGreet() {
    message = await rpc.call('greet', { name: 'John' });
  }

  function createWindow() {
    rpc.call('create_window');
  }
</script>

<div id="root">
  <div>
    <img src="/pyloid_icon.png" class="logo pyloid" alt="Pyloid logo" />
  </div>

  <h1>Pyloid App</h1>

  <div class="card">
    <button class="action-button" onclick={handleGreet}>
      Greet
    </button>
    <button class="action-button" onclick={createWindow}>
      Create Window
    </button>
    <button class="action-button" onclick={() => baseAPI.close()}>
      Close
    </button>
  </div>

  <div>
    <p>{message}</p>
    <a href="https://pyloid.com">Visit Pyloid</a>
  </div>
</div>
