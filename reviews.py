from database import get_connection

from database import get_connection

def view_all_reviews():
    """View all reviews in the database."""
    try:
        conn = get_connection()
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
    except Exception as e:
        print(f"Error viewing reviews: {e}")
    finally:
        conn.close()



def add_review(user_id, book_id, rating, review_text):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT BookID FROM Book WHERE BookID = ?", (book_id,))
        if not cursor.fetchone():
            print("Error: Invalid Book ID.")
            return
        cursor.execute("""
            INSERT INTO Review (BookID, UserID, Rating, ReviewText) VALUES (?, ?, ?, ?)
        """, (book_id, user_id, rating, review_text))
        conn.commit()
        print("Review added successfully!")
    except Exception as e:
        print(f"Error adding review: {e}")
    finally:
        conn.close()
