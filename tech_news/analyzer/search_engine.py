from tech_news.database import search_news
from datetime import datetime


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
    try:
        dateF = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
        query = {'timestamp': dateF}
        database_result = search_news(query)
        lista = []
        for res in database_result:
            tupla = (res['title'], res['url'])
            lista.append(tupla)
        return lista
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    query = {'tags': {'$regex': tag, '$options': 'i'}}
    database_result = search_news(query)
    lista = []
    for res in database_result:
        tupla = (res['title'], res['url'])
        lista.append(tupla)

    return lista


# Requisito 9
def search_by_category(category):
    query = {'category': {'$regex': category, '$options': 'i'}}
    database_result = search_news(query)
    lista = []
    for res in database_result:
        tupla = (res['title'], res['url'])
        lista.append(tupla)

    return lista
