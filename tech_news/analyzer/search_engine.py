from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {'title': {'$regex': title, '$options': 'i'}}
    database_result = search_news(query)
    lista = []
    for res in database_result:
        tupla = (res['title'], res['url'])
        lista.append(tupla)

    return lista


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
