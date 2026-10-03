import requests
import sqlite3

#-------- fetching data from the API---------

url = "https://openlibrary.org/search.json?isbn=9780140328721"

response = requests.get(url)

print(response.status_code)

data = response.json()

book = data["docs"][0]

title = book["title"]
author = book["author_name"][0]
publication_year = book["first_publish_year"]

print("Title:", title)
print("Author:", author)
print("Publication Year:", publication_year)

#-------- storing data in the SQLite database---------

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    author TEXT,
    publication_year INTEGER
)
""")

connection.commit()

cursor.execute("""
INSERT OR IGNORE INTO books (title, author, publication_year)
VALUES (?, ?, ?)
""", (title, author, publication_year))

connection.commit()

cursor.execute("SELECT * FROM books")

#-------- retrieving data from the SQLite database---------

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()