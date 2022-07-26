from distutils.command.build_scripts import first_line_re
import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = r"C:/Users/malak/Downloads"
to_dir = r"C:/Users/malak/Downloads"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"¡Oye, {event.src_path} ha sido creado")
    
    def on_deleted(self, event):
        print(f"¡Lo siento! ¡Alguien borró {event.src_path}!")
    
    def on_moved(self, event):
       print(f"¡Oye, alguien movió {event.src_path}!")
    
    def on_modified(self, event):
       print(f"¡Oye, se modificó {event.src_path}!")

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
  while True:
     time.sleep(2)
     print("ejecutando...")
except KeyboardInterrupt:
    print("error")
    observer.stop()
