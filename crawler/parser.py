from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class Parser:
    def __init__(self, base_url=None):
        self.base_url = base_url

    def extract_links(self, html, current_url):
        """Extract all valid http(s) links from the HTML."""
        
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = urljoin(current_url, a_tag['href'])
            parsed = urlparse(href)
            if parsed.scheme in ['http', 'https']:
                links.add(href)
        
        return links
    
    
    def extract_title(self, html):
        """Extract the title of the page."""

        soup = BeautifulSoup(html, 'html.parser')
        title_tag = soup.title
        return title_tag.string.strip() if title_tag and title_tag.string else ''