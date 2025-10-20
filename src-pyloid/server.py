from pyloid.rpc import PyloidRPC, RPCContext

server = PyloidRPC()

@server.method()
async def greet(name: str):
    return f"Hello, {name}!"

@server.method()
async def create_window(ctx: RPCContext):
    win = ctx.pyloid.create_window(title="Google Window")
    win.load_url("https://www.google.com")
    win.show_and_focus()

#Simplified English must be used for method names.
@server.method()
async def window_minimise(ctx: RPCContext):
    ctx.window.minimize()
    return None
@server.method()
async def window_toggle_maximise(ctx: RPCContext):
    ctx.window.toggle_maximize()
    return None
@server.method()
async def window_close(ctx: RPCContext):
    ctx.window.close()
    return None