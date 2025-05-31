import random
import string
import requests
from bs4 import BeautifulSoup

from sources_list import sources_list
from database_functions import already_shared, save_data

def select_random_source(sources_list: list) -> string:
    selected_url = random.choice(sources_list)
    
    return selected_url

def access_articles_on_source(url: string) -> list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "xml")
    articles = soup.find_all("item")
    
    return articles

def parse_article_information(article: list) -> list:
    informations = []

    article_title = article.find("title").text
    article_description = article.find("description").text
    article_link = article.find("link").text

    informations.append(article_title)
    informations.append(article_description)
    informations.append(article_link)

    return informations

def save_article_on_db(article_title: str) -> None:
    save_data(article_title)

def select_article():
    source = select_random_source(sources_list)
    articles_avaiables = access_articles_on_source(source)

    for article in articles_avaiables:
        article_metadata = parse_article_information(article)

        if already_shared(article_metadata[0]):
            continue

        save_article_on_db(article_metadata[0])
    
    return article_metadata