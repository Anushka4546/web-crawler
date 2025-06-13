from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

class Fetcher:
    def __init__(self, timeout=10, driver_path='chromedriver'):
        self.timeout = timeout
        self.driver_path = driver_path
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.set_page_load_timeout(self.timeout)

    def fetch(self, url):
        try:
            self.driver.get(url)
            # Wait up to 20 seconds for at least one article or headline link
            WebDriverWait(self.driver, 20)
            # Optional: Scroll down to trigger lazy-loading
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            return self.driver  # Return driver instead of HTML!
        except Exception as e:
            logging.warning(f"Selenium Fetcher: Failed to fetch {url}: {e}")
            return None

    def close(self):
        try:
            self.driver.quit()
        except Exception:
            pass
