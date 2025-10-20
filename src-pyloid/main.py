from pyloid.tray import (
    TrayEvent,
)
from pyloid.utils import (
    get_production_path,
    is_production,
)
from pyloid.serve import pyloid_serve
from pyloid import Pyloid
from server import server
import time
'''
Let the window licking begin.....
'''
app = Pyloid(app_name="pyloid-sveltekit-shadcn-ui", single_instance=True, server=server)

app.set_icon(get_production_path("src-pyloid/icons/icon.png"))
app.set_tray_icon(get_production_path("src-pyloid/icons/icon.png"))
############################## Screen Size ##########################
monitor = app.get_primary_monitor()
size = monitor.size()
if isinstance(size, (tuple, list)) and len(size) == 1:
    size = size[0]
# keep 1200x800 ratio, fit within 90% of screen, prefer min scale if it fits
base_w, base_h = 1200, 800
sw, sh = size["width"], size["height"]
max_w, max_h = int(sw * 0.7), int(sh * 0.7)
scale = min(max_w / base_w, max_h / base_h)
min_scale = 0.75
if scale < min_scale and int(base_w * min_scale) <= max_w and int(base_h * min_scale) <= max_h:
    scale = min_scale
w, h = max(1, int(round(base_w * scale))), max(1, int(round(base_h * scale)))
############################## Tray ################################
def on_double_click():
    app.show_and_focus_main_window()


app.set_tray_actions(
    {
        TrayEvent.DoubleClick: on_double_click,
    }
)
app.set_tray_menu_items(
    [
        {"label": "Show Window", "callback": app.show_and_focus_main_window},
        {"label": "Exit", "callback": app.quit},
    ]
)
####################################################################

if is_production():
    url = pyloid_serve(directory=get_production_path("dist-front"))
    window = app.create_window(
        title="Pyloid sveltekit shadcn-ui",
        frame=False,
        transparent=True
    )
    window.load_url(url)
else:
    window = app.create_window(
        title="Pyloid sveltekit shadcn-ui-dev",
        dev_tools=True,
        frame=False,
        transparent=True
    )
    time.sleep(3)  #wait for 3 seconds to allow vite to start. Hacky. Better with splash screen
    window.load_url("http://localhost:5173")

window.set_size(w, h) #w, h comes from above screen size calculation
window.show_and_focus()

app.run()
