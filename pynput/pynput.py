import threading
from pynput.mouse import Button, Controller

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()defon_press(key):if key == start_stop_key:if click_thread.running:
            click_thread.stop_clicking()else:
            click_thread.start_clicking()elif key == exit_key:
        click_thread.exit()
        listener.stop()with Listener(on_press=on_press)as listener:
    listener.join()