import threading
from .fetcher import Fetcher

class Worker(threading.Thread):
    def __init__(self, frontier, parser, storage, max_depth=2, driver_path='chromedriver', timeout=10):
        super().__init__()
        self.frontier = frontier
        self.parser = parser
        self.storage = storage
        self.max_depth = max_depth
        self.driver_path = driver_path
        self.timeout = timeout

    def run(self):
        fetcher = Fetcher(timeout=self.timeout, driver_path=self.driver_path)
        while True:
            item = self.frontier.get_url()
            if item is None:
                break
            if isinstance(item, tuple):
                url, depth = item
            else:
                url, depth = item, 0
            if depth > self.max_depth:
                self.frontier.task_done()
                continue
            driver = fetcher.fetch(url)
            if driver:
                title = driver.title
                self.storage.add_result(url, title)
                links = self.parser.extract_links_selenium(driver)
                for link in links:
                    self.frontier.add_url((link, depth + 1))
            self.frontier.task_done()
        fetcher.close()

