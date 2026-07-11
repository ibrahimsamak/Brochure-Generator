from dataclasses import dataclass,field
from bs4 import BeautifulSoup
import requests

# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

@dataclass
class Scraper:
    url: str
    title: str
    body: str
    links: list[str] = field(default_factory=list)

def fetch_website_contents(url) -> Scraper:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string if soup.title else "No title found"
        if(soup.body):
            for ignore in soup.body(["script", "style", "img", "input"]):
                ignore.decompose()
            body = soup.body.get_text(separator="\n", strip=True)
        else:
            body = "" 
        return Scraper(url=url, title=title, body=body)


def fetch_website_links(url) -> Scraper:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        links = [link.get("href") for link in soup.find_all("a")]
        return Scraper(url=url, title="", body="", links=[link for link in links if link])

