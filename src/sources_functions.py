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