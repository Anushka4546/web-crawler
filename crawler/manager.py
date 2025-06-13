from .frontier import URLFrontier
from .parser import Parser
from .storage import Storage
from .worker import Worker

class Manager:
    def __init__(self, start_url, max_workers=5, max_pages=100, max_depth=2, driver_path='chromedriver', timeout=10):
        self.frontier = URLFrontier()
        self.parser = Parser()
        self.storage = Storage()
        self.max_workers = max_workers
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.driver_path = driver_path
        self.timeout = timeout

        self.frontier.add_url((start_url, 0))

    def start(self):
        workers = []
        for _ in range(self.max_workers):
            worker = Worker(
                self.frontier,
                self.parser,
                self.storage,
                self.max_depth,
                self.driver_path,
                self.timeout
            )
            worker.start()
            workers.append(worker)

        for worker in workers:
            worker.join()
