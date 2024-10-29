from .person import Person

class User(Person):
    """
    Class representing a library member who can borrow books.
    """
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Allow user to borrow a book if available.
        """
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is not available.")

    def return_book(self, book):
        """
        Allow user to return a book they have borrowed.
        """
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title} borrowed.")

    def get_user_info(self):
        return f"User: {self.name}, ID: {self.user_id}"
