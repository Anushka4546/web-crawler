from queue import Queue
import threading

class URLFrontier:
    def __init__(self):
        self.queue = Queue()
        self.seen = set()
        self.lock = threading.Lock()

    def add_url(self, url):
        with self.lock:
            if url not in self.seen:
                self.seen.add(url)
                self.queue.put(url)
    
    def get_url(self):
        try:
            return self.queue.get(timeout=2)
        except:
            return None
        
    def task_done(self):
        self.queue.task_done()

    
    def qsize(self):
        return self.queue.qsize()