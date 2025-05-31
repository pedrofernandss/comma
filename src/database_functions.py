import sqlite3

database_path = "./database/articles.db"

connection = sqlite3.connect("./database/articles.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOTE EXISTS articles (
   id INTEGER PRIMARY KEY,
    title TEXT NOT NULL            
)
''')

connection.commit()
connection.close()

def already_shared(article_title: str) -> bool:
    """Verify if the selected article was previosly shared"""
    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.execute('SELECT 1 FROM articles WHERE title = ?', (article_title))
        result = cursor.fetchone()

        return result is not None
    except sqlite3.Error as exception:
        raise exception
