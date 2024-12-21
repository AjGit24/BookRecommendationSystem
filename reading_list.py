from database import get_connection

def create_reading_list(user_id, list_name):
    """Create a new reading list."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ReadingList (UserID, ListName) VALUES (?, ?)
        """, (user_id, list_name))
        conn.commit()
        print(f"Reading list '{list_name}' created successfully!")
    except Exception as e:
        print(f"Error creating reading list: {e}")
    finally:
        conn.close()

def add_book_to_list(user_id, list_name, book_id):
    """Add a book to a reading list."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ReadingListBook (UserID, ListName, BookID) VALUES (?, ?, ?)
        """, (user_id, list_name, book_id))
        conn.commit()
        print(f"Book ID {book_id} added to reading list '{list_name}'")
    except Exception as e:
        print(f"Error adding book to reading list: {e}")
    finally:
        conn.close()

def view_reading_lists(user_id):
    """View all reading lists for a user."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ListName FROM ReadingList WHERE UserID = ?
        """, (user_id,))
        lists = cursor.fetchall()
        if lists:
            print("Your Reading Lists:")
            for lst in lists:
                print(f"- {lst[0]}")
        else:
            print("You have no reading lists.")
    except Exception as e:
        print(f"Error viewing reading lists: {e}")
    finally:
        conn.close()



