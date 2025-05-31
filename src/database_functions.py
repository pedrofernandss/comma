import sqlite3

connection = sqlite3.connect("./database/articles.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOTE EXISTS articles (
   id INTERGER PRIMARY KEY,
    title TEXT NOT NULL;              
)
''')

connection.commit()
connection.close()

def already_shared(article_title: str) -> bool:
    connection = sqlite3.connect("./database/articles.db")
    cursor = connection.cursor()

    cursor.execute('SELECT 1 FROM articles WHERE title = ?', (article_title))
    result = cursor.fetchone()

    connection.close()

    return result is not None
