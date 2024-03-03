from pynput import mouse, keyboard
import time as t

# Global variable to keep track of the current scroll position
current_scroll_position = 0

def on_scroll(x, y, dx, dy):
    global current_scroll_position
    # Update the current scroll position
    current_scroll_position += dy
    # Check if scrolling down
    if dy < 0:
        # trigger crouch button 'c
        keyboard.Controller().press(' ')
        keyboard.Controller().release(' ')
        t.sleep(0.004)
        keyboard.Controller().press('c')
        keyboard.Controller().release('c')


# Set up the listener for mouse scroll events
mouse_listener = mouse.Listener(on_scroll=on_scroll)
mouse_listener.start()

print("superglide start!")

# Keep the script running
mouse_listener.join()
