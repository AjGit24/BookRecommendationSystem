import sqlite3
import auth
import sys

DB_FILE = "book_recommendation_system.db"

def initialize_database():
    """Initialize the database and create tables."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        with open("schema.sql", "r") as schema_file:
            cursor.executescript(schema_file.read())
        with open("data.sql", "r") as data_file:
            cursor.executescript(data_file.read())
        conn.commit()
        print("Database initialized successfully!")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def list_books():
    """List all books in the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Book")
        books = cursor.fetchall()
        conn.close()
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}")
        else:
            print("No books found.")
    except sqlite3.Error as e:
        print(f"Error retrieving books: {e}")

def search_books(search_term):
    """Search for books based on title, author, genre, or year."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = """
            SELECT * FROM Book
            WHERE Title LIKE ? OR Author LIKE ? OR Genre LIKE ? OR PublicationYear LIKE ?
        """
        cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        books = cursor.fetchall()
        conn.close()
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}")
        else:
            print("No books found matching your search.")
    except sqlite3.Error as e:
        print(f"Error searching books: {e}")

def view_recommendations(user):
    """View recommendations for a user based on their favorite genre."""
    try:
        if not user:
            print("Please log in to view recommendations.")
            return

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Title, Author, Genre, PublicationYear 
            FROM Book 
            WHERE LOWER(Genre) = ?
        """, (user['preferences'].lower(),))
        recommendations = cursor.fetchall()
        conn.close()

        if recommendations:
            print(f"Recommended books for your favorite genre '{user['preferences']}':")
            for rec in recommendations:
                print(f"- {rec[0]} by {rec[1]} ({rec[3]}): {rec[2]}")
        else:
            print(f"No recommendations found for genre '{user['preferences']}'.")
    except sqlite3.Error as e:
        print(f"Error retrieving recommendations: {e}")

def add_review(user_id, book_id, rating, review_text):
    """Add a review for a book."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Review (BookID, UserID, Rating, ReviewText) VALUES (?, ?, ?, ?)
        """, (book_id, user_id, rating, review_text))
        conn.commit()
        print("Review added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding review: {e}")
    finally:
        conn.close()

        

def manage_reading_lists(user_id):
    """Manage a user's reading lists."""
    while True:
        print("\nReading List Management")
        print("1. Create a new reading list")
        print("2. Add a book to a reading list")
        print("3. View your reading lists")
        print("4. View books in a specific reading list")  # New option
        print("5. Go back")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_name = input("Enter a name for the new reading list: ")
            create_reading_list(user_id, list_name)
        elif choice == "2":
            list_name = input("Enter the name of the reading list: ")
            book_id = int(input("Enter the Book ID: "))
            add_book_to_list(user_id, list_name, book_id)
        elif choice == "3":
            view_reading_lists(user_id)
        elif choice == "4":
            list_name = input("Enter the name of the reading list: ")
            view_books_in_list(user_id, list_name)  # Call new function
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def create_reading_list(user_id, list_name):
    """Create a new reading list."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ReadingList (UserID, ListName) VALUES (?, ?)
        """, (user_id, list_name))
        conn.commit()
        print(f"Reading list '{list_name}' created successfully!")
    except sqlite3.Error as e:
        print(f"Error creating reading list: {e}")
    finally:
        conn.close()

def add_book_to_list(user_id, list_name, book_id):
    """Add a book to a reading list."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Retrieve ListID based on list_name and user_id
        cursor.execute("""
            SELECT ListID FROM ReadingList WHERE ListName = ? AND UserID = ?
        """, (list_name, user_id))
        result = cursor.fetchone()
        
        if result:
            list_id = result[0]
            cursor.execute("""
                INSERT INTO ReadingListBooks (ListID, BookID) VALUES (?, ?)
            """, (list_id, book_id))
            conn.commit()
            print(f"Book ID {book_id} added to reading list '{list_name}'")
        else:
            print(f"No reading list found with the name '{list_name}'.")
    except sqlite3.Error as e:
        print(f"Error adding book to reading list: {e}")
    finally:
        conn.close()

def view_reading_lists(user_id):
    """View all reading lists for a user."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ListName FROM ReadingList WHERE UserID = ?
        """, (user_id,))
        lists = cursor.fetchall()
        conn.close()
        if lists:
            print("Your Reading Lists:")
            for lst in lists:
                print(f"- {lst[0]}")
        else:
            print("You have no reading lists.")
    except sqlite3.Error as e:
        print(f"Error viewing reading lists: {e}")


def view_books_in_list(user_id, list_name):
    """View books in a specific reading list."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Retrieve the ListID for the given list name and user ID
        cursor.execute("""
            SELECT ListID FROM ReadingList WHERE ListName = ? AND UserID = ?
        """, (list_name, user_id))
        result = cursor.fetchone()
        
        if result:
            list_id = result[0]
            cursor.execute("""
                SELECT b.BookID, b.Title, b.Author, b.Genre, b.PublicationYear 
                FROM ReadingListBooks rb
                JOIN Book b ON rb.BookID = b.BookID
                WHERE rb.ListID = ?
            """, (list_id,))
            books = cursor.fetchall()
            
            if books:
                print(f"\nBooks in '{list_name}' Reading List:")
                for book in books:
                    print(f"- ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}")
            else:
                print(f"No books found in the reading list '{list_name}'.")
        else:
            print(f"No reading list found with the name '{list_name}'.")
    except sqlite3.Error as e:
        print(f"Error retrieving books in list: {e}")
    finally:
        conn.close()


def view_all_reviews():
    """View all reviews in the database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = """
        SELECT 
            r.ReviewID, 
            b.Title AS BookTitle, 
            u.Username AS Reviewer, 
            r.Rating, 
            r.ReviewText
        FROM 
            Review r
        JOIN 
            Book b ON r.BookID = b.BookID
        JOIN 
            User u ON r.UserID = u.UserID
        """
        cursor.execute(query)
        reviews = cursor.fetchall()
        conn.close()
        
        if reviews:
            print("\nAll Reviews:")
            for review in reviews:
                print(f"Review ID: {review[0]}")
                print(f"Book Title: {review[1]}")
                print(f"Reviewer: {review[2]}")
                print(f"Rating: {review[3]} / 5")
                print(f"Review Text: {review[4]}")
                print("-" * 50)
        else:
            print("No reviews found.")
    except sqlite3.Error as e:
        print(f"Error viewing reviews: {e}")


def main():
    current_user = None
    while True:
        print("\nBook Recommendation System")
        print("1. List all books")
        print("2. Search books")
        print("3. View recommendations")
        print("4. Add a review")
        print("5. Manage Reading Lists")
        print("6. Register")
        print("7. Login")
        print("8. Initialize Database")
        print("9. View all reviews")  
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_books()
        elif choice == "2":
            search_term = input("Enter search term (title, author, genre, year): ")
            search_books(search_term)
        elif choice == "3":
            if current_user:
                view_recommendations(current_user)
            else:
                print("Please log in first.")
        elif choice == "4":
            if current_user:
                book_id = int(input("Enter the Book ID: "))
                rating = int(input("Enter your rating (1-5): "))
                review_text = input("Enter your review: ")
                add_review(current_user["user_id"], book_id, rating, review_text)
            else:
                print("Please log in first.")
        elif choice == "5":
            if current_user:
                manage_reading_lists(current_user["user_id"])
            else:
                print("Please log in first.")
        elif choice == "6":
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            preferences = input("Enter your preferences (e.g., Fiction, Mystery): ")
            result = auth.register_user(username, email, password, preferences)
            print(result)
        elif choice == "7":
            username = input("Enter username: ")
            password = input("Enter password: ")
            current_user = auth.login_user(username, password)
            if current_user:
                print(f"Logged in as User ID: {current_user['user_id']}")
            else:
                print("Invalid login credentials.")
        elif choice == "8":
            initialize_database()
        elif choice == "9":  # Handle new option
            view_all_reviews()
        elif choice == "10":
            print("Exiting the system. Goodbye!")
            sys.exit()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
