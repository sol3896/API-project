from library.library import Library
from models.book import Book
from models.user import User
from models.staff import Staff

def main():
    # Initialize the library
    library = Library()
    
    print("Welcome to the Library Management System!")
    
    while True:
        print("\nMenu:")
        print("1. Add a new book")
        print("2. Register a new user")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                # Add a new book
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                isbn = input("Enter book ISBN: ").strip()

                if not title or not author or not isbn:
                    raise ValueError("Book title, author, and ISBN must not be empty.")

                available_copies = int(input("Enter available copies: "))
                if available_copies < 0:
                    raise ValueError("Available copies cannot be negative.")

                book = Book(title, author, isbn, available_copies)
                library.add_book(book)

            elif choice == "2":
                # Register a new user
                user_id = input("Enter user ID: ").strip()
                name = input("Enter user name: ").strip()
                user_type = input("Is the user a 'Member' or 'Staff'? ").strip().lower()

                if not user_id or not name:
                    raise ValueError("User ID and name must not be empty.")

                if user_type == "staff":
                    user = Staff(user_id, name)
                else:
                    user = User(user_id, name)
                library.add_user(user)

            elif choice == "3":
                # Borrow a book
                user_id = input("Enter user ID for borrowing: ").strip()
                title = input("Enter book title to borrow: ").strip()
                user = library.find_user_by_id(user_id)

                if user:
                    library.borrow_book(user, title)
                else:
                    print("User not found!")

            elif choice == "4":
                # Return a book
                user_id = input("Enter user ID for returning: ").strip()
                title = input("Enter book title to return: ").strip()
                user = library.find_user_by_id(user_id)

                if user:
                    library.return_book(user, title)
                else:
                    print("User not found!")

            elif choice == "5":
                # View all books
                library.view_all_books()

            elif choice == "6":
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
