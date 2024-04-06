import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/reyacano/Downloads"
to_dir = "/Users/reyacano/Desktop/pretty wallpapers"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if not extension:
        continue
    if extension.lower() in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files", extension[1:])
        path3 = os.path.join(path2, file_name)
        if os.path.exists(path2):
            print(f"Moving {file_name} to {path2}")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print(f"Moving {file_name} to {path2}")
            shutil.move(path1, path3)

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'File created: {event.src_path}')

    def on_modified(self, event):
        print(f'File modified: {event.src_path}')

    def on_moved(self, event):
        print(f'File moved from: {event.src_path} to {event.dest_path}')

    def on_deleted(self, event):
        print(f'File deleted: {event.src_path}')

def main():
    from_dir = "</Users/reyacano/Downloads>"

    event_handler = FileEventHandler()

    observer = Observer()
    observer.schedule(event_handler, from_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
