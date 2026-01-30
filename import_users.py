import csv
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_FILE = os.path.join(BASE_DIR, "data", "users.csv")
DB_FILE = os.path.join(BASE_DIR, "database", "users.db")


def create_database():
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    conn.commit()
    conn.close()


def import_csv_to_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                cursor.execute(
                    "INSERT INTO users (name, email) VALUES (?, ?)",
                    (row["name"], row["email"])
                )
            except sqlite3.IntegrityError:
                print(f"Duplicate email skipped: {row['email']}")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    import_csv_to_db()
    print("CSV data imported successfully.")

