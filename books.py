from database import get_connection

def list_books():
    """List all books in the database."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Book")
        books = cursor.fetchall()
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}")
        else:
            print("No books found.")
    except Exception as e:
        print(f"Error retrieving books: {e}")
    finally:
        conn.close()

def search_books(search_term):
    """Search for books based on title, author, genre, or year."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM Book
            WHERE Title LIKE ? OR Author LIKE ? OR Genre LIKE ? OR PublicationYear LIKE ?
        """
        cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        books = cursor.fetchall()
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}")
        else:
            print("No books found matching your search.")
    except Exception as e:
        print(f"Error searching books: {e}")
    finally:
        conn.close()
