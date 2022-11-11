import requests
from time import sleep
from parsel import Selector
import re
from tech_news.database import create_news


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
    selector = Selector(html_content)

    url = selector.css('head link[rel=canonical]::attr(href)').get()

    title = selector.css('h1::text').get().replace('\xa0', '')

    timestamp = selector.css('li.meta-date::text').get()

    writer = selector.css('a.url::text').get()

    comments_count = len(selector.css('ol.comment-list li').getall())

    raw_html = selector.css('.entry-content p').get()
    CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(CLEANR, '', raw_html)
    summary = cleantext.strip()

    tags = selector.css('li a[rel=tag]::text').getall()

    category = selector.css('span.label::text').get()

    noticia = {
        'url': url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category
    }
    return noticia


# Requisito 5
def get_tech_news(amount):
    url = 'https://blog.betrybe.com/'
    fetch_result = fetch(url)
    news = []
    while len(news) < amount:
        noticias_links = scrape_novidades(fetch_result)
        for noticia in noticias_links:
            conteudo = fetch(noticia)
            scrape = scrape_noticia(conteudo)
            news.append(scrape)

        url = scrape_next_page_link(fetch_result)

    create_news(news)
    return news
