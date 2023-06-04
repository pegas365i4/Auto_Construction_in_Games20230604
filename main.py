# pip install pynput

import time
import threading
# from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode, Controller

toggle_key = KeyCode(char='q') # Клавиша включения и выключения процесса
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.press('z')
            mouse.release('z')
            time.sleep(0.5)

            mouse.press('x')
            mouse.release('x')
            time.sleep(0.5)

            mouse.press('c')
            mouse.release('c')
            time.sleep(0.5)

def toggle_event(key):
    if key == toggle_key:
        global clicking
        clicking = not clicking

def main():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

