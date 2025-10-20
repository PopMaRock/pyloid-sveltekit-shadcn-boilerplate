import { rpc } from "pyloid-js";

export async function pyloid_window_minimise(): Promise<void> {
    return await rpc.call("window_minimise");
}
export async function pyloid_window_toggle_maximise(): Promise<void> {
    return await rpc.call("window_toggle_maximise");
}
export async function pyloid_window_close(): Promise<void> {
    return await rpc.call("window_close");
}