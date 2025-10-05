import sqlite3
from .env import SQLITE_DB_PATH

def get_connection():
    print(f"DB path: {SQLITE_DB_PATH}")
    conn = sqlite3.connect(SQLITE_DB_PATH, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())
    cursor.close()
    return conn

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

def get_last_names_by_first_name(conn, first_name):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT last_name FROM people WHERE first_name = ?", (first_name,)
    )
    results = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return results
