from pynput.keyboard import Key
import init

def on_press(key):
    # print('{0} pressed'.format(key))
    init.keyboard_press.append(key)

def on_release(key):
    # print('{0} release'.format(key))
    if key == Key.esc:
        return False
