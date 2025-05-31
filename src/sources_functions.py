import random
import string
import requests
from bs4 import BeautifulSoup

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