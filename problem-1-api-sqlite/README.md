# Problem 1 - API Data Retrieval and SQLite

# Overview

This project retrieves book information from the Open Library API and stores the data in a local SQLite database.

# Technologies Used

- Python
- Requests
- SQLite

# API

Open Library API

The program retrieves the following information:

- Book title
- Author
- Publication year

# Database

The retrieved book information is stored in a SQLite database named `books.db`.

The `books` table contains:

| Column | Description |
|---|---|
| id | Unique book ID |
| title | Book title |
| author | Author name |
| publication_year | Year the book was first published |

# Output

```text
Title: Fantastic Mr Fox
Author: Roald Dahl
Publication Year: 1970

Books stored in database:
(1, 'Fantastic Mr Fox', 'Roald Dahl', 1970)