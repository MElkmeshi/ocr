from PIL import Image, ImageGrab
import time
import pyperclip
import pytesseract
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

# Create a custom event handler for new file creation


class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the new file is a screenshot (PNG format)
        if event.src_path.endswith(".png"):
            # Process the new screenshot
            process_screenshot()

# Define the function to process the screenshot


def process_screenshot():
    img = ImageGrab.grabclipboard()
    if isinstance(img, Image.Image):
        x = (pytesseract.image_to_string(ImageGrab.grabclipboard()))
        pyperclip.copy(x)


# Define the directory to monitor for new files
dir_path = Path.home() / "Pictures" / "Screenshots"

# Create a watchdog observer for the directory
event_handler = NewFileHandler()
observer = Observer()
observer.schedule(event_handler, dir_path, recursive=False)
observer.start()

# Loop forever to keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
