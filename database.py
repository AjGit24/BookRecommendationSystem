import sqlite3

DB_FILE = "book_recommendation_system.db"

def get_connection():
    """Get a database connection."""
    return sqlite3.connect(DB_FILE)
