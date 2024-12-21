import sqlite3
import hashlib

DB_FILE = "book_recommendation_system.db"

def get_connection():
    """Establishes a connection to the database."""
    return sqlite3.connect(DB_FILE)

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password, preferences):
    """Register a new user."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Check if the username already exists
        cursor.execute("SELECT UserID FROM User WHERE LOWER(Username) = ?", (username.lower(),))
        if cursor.fetchone():
            return "Error: Username already exists."
        
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO User (Username, Email, Password, Preferences) VALUES (?, ?, ?, ?)",
                       (username, email, hashed_password, preferences))
        conn.commit()
        return "User registered successfully!"
    except Exception as e:
        return f"Error registering user: {e}"
    finally:
        conn.close()

def login_user(username, password):
    """Authenticate a user."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        cursor.execute("SELECT UserID, Preferences FROM User WHERE LOWER(Username) = ? AND Password = ?",
                       (username.lower(), hashed_password))
        user = cursor.fetchone()
        if user:
            return {"user_id": user[0], "preferences": user[1]}  # Return user_id and preferences
        else:
            return None
    except Exception as e:
        return None
    finally:
        conn.close()
