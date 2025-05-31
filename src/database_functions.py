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


