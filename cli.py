from auth import register_user, login_user
import sys

def main_menu():
    """Display the main menu and handle user choices."""
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
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("List all books (Feature not yet implemented).")
        elif choice == "2":
            print("Search books (Feature not yet implemented).")
        elif choice == "3":
            print("View recommendations (Feature not yet implemented).")
        elif choice == "4":
            print("Add a review (Feature not yet implemented).")
        elif choice == "5":
            print("Manage Reading Lists (Feature not yet implemented).")
        elif choice == "6":
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            preferences = input("Enter your preferences (e.g., Fiction, Mystery): ")
            register_user(username, email, password, preferences)
        elif choice == "7":
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)
        elif choice == "8":
            print("Database initialization (Feature not yet implemented).")
        elif choice == "9":
            print("Exiting the system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
