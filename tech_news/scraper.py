import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url: str) -> str:
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        response.raise_for_status()
        sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links = []
    for link in selector.css('h2.entry-title'):
        result = link.css('a::attr(href)').get()
        links.append(result)
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    next_page = Selector(html_content).css('a.next::attr(href)').get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
