from database import get_connection

def initialize_database():
    """Initialize the database and create tables."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        with open("schema.sql", "r") as schema_file:
            cursor.executescript(schema_file.read())
        with open("data.sql", "r") as data_file:
            cursor.executescript(data_file.read())
        conn.commit()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()
