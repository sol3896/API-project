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

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            try:
                available_copies = int(input("Enter available copies: "))
                book = Book(title, author, isbn, available_copies)
                library.add_book(book)
            except ValueError:
                print("Invalid input for available copies. Please enter a number.")

        elif choice == "2":
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            user_type = input("Is the user a 'Member' or 'Staff'? ").strip().lower()
            if user_type == "staff":
                user = Staff(user_id, name)
            else:
                user = User(user_id, name)
            library.add_user(user)

        elif choice == "3":
            user_id = input("Enter user ID for borrowing: ")
            title = input("Enter book title to borrow: ")
            user = library.find_user_by_id(user_id)
            if user:
                library.borrow_book(user, title)
            else:
                print("User not found!")

        elif choice == "4":
            user_id = input("Enter user ID for returning: ")
            title = input("Enter book title to return: ")
            user = library.find_user_by_id(user_id)
            if user:
                library.return_book(user, title)
            else:
                print("User not found!")

        elif choice == "5":
            library.view_all_books()

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
