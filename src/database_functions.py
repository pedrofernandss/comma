import os
import sqlite3

database_path = "./database/articles.db"

def initialize_database() -> None:
    """Create database"""

    db_directiory = os.path.dirname(database_path)

    if db_directiory and not os.path.exists(db_directiory):
        os.makedirs(db_directiory)

    try:
        connection = sqlite3.connect("./database/articles.db")
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOTE EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL            
        )
        ''')

        connection.commit()
        
    except sqlite3.Error as CreationDatabaseError:
        raise CreationDatabaseError


def save_data(article_title: str) -> None:
    """Save a new data on the database"""

    try:
        connection = sqlite3.connect("./database/articles.db")
        cursor = connection.cursor()

        cursor.execute('''
        INSERT INTO articles (title)
        VALUES (?)''', (article_title))

        connection.commit()

    except sqlite3.Error as ArticleSaveError:
        raise ArticleSaveError

def already_shared(article_title: str) -> bool:
    """Verify if the selected data already is on database"""
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute('SELECT 1 FROM articles WHERE title = ?', (article_title))
        result = cursor.fetchone()

        return result is not None
    except sqlite3.Error as ArticleCheckError:
        raise ArticleCheckError
