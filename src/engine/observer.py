import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

if __name__ == "__main__":
    '''logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
'''
    class Handler(FileSystemEventHandler):
        def on_created(self, event):
            file_name = event.src_path
            subprocess.run(["python", "read_cfg_test.py"])
        def on_deleted(self, event):
            print(event)
        def on_moved(self, event):
            print(event)
        def on_modified(self, event):
            print(event)

    path ='.'
    #event_handler = LoggingEventHandler()
    observer = Observer()
    #observer.schedule(event_handler, path, recursive=True)
    observer.schedule(Handler(), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

