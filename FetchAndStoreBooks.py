import requests
import sqlite3

API_URL = "https://mocki.io/v1/ecdf69aa-ac9e-48b2-9bb9-85d4ff9bcd52"

def database_creation():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER
        )
    """)

    conn.commit()
    conn.close()

def storebooksdata():
    responses = requests.get(API_URL)
    if responses.status_code == 200:
        return responses.json()
    else:
        print("Failed to fetch data from API")
        return []
    
def storingbooks(books):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    for book in books:
        cursor.execute("""INSERT INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
        """, (
            book.get("title"),
            book.get("author"),
            book.get("publication_year")
        ))
    conn.commit()
    conn.close()

def getallbooks():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, publication_year FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def displaydetails(books):
    print("\n Book list:")
    for book in books:
        print(f"Title: {book[0]}")
        print(f"Author: {book[1]}")
        print(f"Publication Year: {book[2]}")
        print("-" * 30)

def main():
    database_creation()

    books = storebooksdata()
    if books:
        storingbooks(books)

    stored_books = getallbooks()
    displaydetails(stored_books)

if __name__ == "__main__":
    main()

