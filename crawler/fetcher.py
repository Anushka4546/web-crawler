import requests
import logging

class Fetcher:
    def __init__(self, timeout=5):
        self.timeout = timeout

    def fetch(self, url):
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.warning(f"Fetcher: Failed to fetch {url}: {e}")
            return None