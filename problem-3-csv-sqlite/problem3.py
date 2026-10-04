import csv
import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

with open("users.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
        INSERT OR IGNORE INTO users (name, email)
        VALUES (?, ?)
        """, (row["name"], row["email"]))

connection.commit()

cursor.execute("SELECT * FROM users")

print("Users stored in database:")

for user in cursor.fetchall():
    print(user)

connection.close()