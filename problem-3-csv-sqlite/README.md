# Problem 3 - CSV Data Import to SQLite

## Overview

This project reads user information from a CSV file and stores it in a local SQLite database.

## CSV Data

The CSV file contains:

- Name
- Email

## Database

The information is stored in a SQLite database named `users.db`.

The `users` table contains:

| Column | Description |
|---|---|
| id | Unique user ID |
| name | User name |
| email | User email |

## Processing

1. Read the CSV file using Python.
2. Connect to SQLite.
3. Create the users table if it does not exist.
4. Insert the CSV records into the database.
5. Display the stored records.

## How to Run

From the `problem-3-csv-sqlite` directory:

python3 problem3.py

Users stored in database:
(1, 'John Smith', 'john.smith@example.com')
(2, 'Emma Wilson', 'emma.wilson@example.com')
(3, 'David Brown', 'david.brown@example.com')
(4, 'Sophia Taylor', 'sophia.taylor@example.com')