from queue import Queue
import threading

class URLFrontier:
    def __init__(self):
        self.counter = 0
        self.queue = Queue()
        self.seen = set()
        self.lock = threading.Lock()

    def add_url(self, item):
        # Always treat input as (url, depth)
        url, depth = item if isinstance(item, tuple) else (item, 0)
        with self.lock:
            if url not in self.seen:
                print(self.counter)
                self.counter = self.counter + 1
                self.seen.add(url)
                self.queue.put((url, depth))

    def get_url(self):
        try:
            return self.queue.get(timeout=2)
        except:
            return None

    def task_done(self):
        self.queue.task_done()

    def qsize(self):
        return self.queue.qsize()