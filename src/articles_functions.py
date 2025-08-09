from bs4.element import Tag
import random
import string
import requests
from bs4 import BeautifulSoup

from sources_list import sources_list
from database_functions import already_shared, initialize_database, save_data


def select_random_source(sources_list: list) -> str:
    selected_url = random.choice(sources_list)

    return selected_url


def access_articles_on_source(url: str) -> list:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "xml")
    articles = soup.find_all("item")
    return articles


def parse_article_information(article: Tag) -> list | None:
    informations = []

    title_tag = article.find("title")
    article_title = title_tag.text.strip() if title_tag and title_tag.text else None

    desc_tag = (
        article.find("description") or
        article.find("content:encoded") or
        article.find("content") or
        article.find("summary")
    )
    article_description = desc_tag.text if desc_tag and desc_tag.text else None

    if article_description:
        soup = BeautifulSoup(article_description, "html.parser")
        article_description = soup.get_text(separator=" ", strip=True)

    link_tag = article.find("link")
    article_link = link_tag.text.strip() if link_tag and link_tag.text else None

    informations.append(article_title)
    informations.append(article_description)
    informations.append(article_link)

    return informations

def save_article_on_db(article_title: str) -> None:
    save_data(article_title)

def select_article():
    initialize_database()

    source = select_random_source(sources_list)
    articles_avaiables = access_articles_on_source(source)

    for article in articles_avaiables:
        article_metadata = parse_article_information(article)
        if article_metadata is None:
            continue

        if already_shared(article_metadata[0]):
            continue

        save_article_on_db(article_metadata[0])
        return article_metadata