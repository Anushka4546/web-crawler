from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from urllib.parse import urljoin, urlparse

class Parser:
    def __init__(self, base_url=None):
        self.base_url = base_url

    def extract_links_selenium(self, driver):
        links = set()
        for elem in driver.find_elements(By.TAG_NAME, "a"):
            href = elem.get_attribute("href")
            if href and href.startswith("http"):
                links.add(href)
        return links
    
    
    def extract_title(self, html):
        """Extract the title of the page."""

        soup = BeautifulSoup(html, 'html.parser')
        title_tag = soup.title
        return title_tag.string.strip() if title_tag and title_tag.string else ''