from models.book import Book
from models.user import User
from models.staff import Staff

class Library:
    def __init__(self):
        """
        Initialize the Library with empty lists for books and users.
        """
        self.books = []
        self.users = []

    def add_book(self, book):
        """
        Add a book to the library collection.
        """
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def add_user(self, user):
        """
        Register a new user in the library system.
        """
        self.users.append(user)
        print(f"User '{user.name}' registered.")

    def find_book_by_title(self, title):
        """
        Find a book by its title in the library collection.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f"Book '{title}' not found.")
        return None

    def find_user_by_id(self, user_id):
        """
        Find a user by their ID.
        """
        for user in self.users:
            if user.user_id == user_id:
                return user
        print(f"User with ID '{user_id}' not found.")
        return None

    def borrow_book(self, user, title):
        """
        Facilitate borrowing of a book by a user if available.
        """
        book = self.find_book_by_title(title)
        if book:
            user.borrow_book(book)

    def return_book(self, user, title):
        """
        Facilitate returning of a book by a user.
        """
        book = self.find_book_by_title(title)
        if book:
            user.return_book(book)

    def view_all_books(self):
        """
        Display all books in the library.
        """
        print("\nLibrary Collection:")
        for book in self.books:
            print(book)
