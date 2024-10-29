class Book:
    """
    Class representing a book in the library system.
    """
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._available_copies = available_copies  # Encapsulation

    def check_availability(self):
        """Check if the book is available for borrowing."""
        return self._available_copies > 0

    def borrow_book(self):
        """Reduce available copies by 1 if the book is available."""
        if self.check_availability():
            self._available_copies -= 1
            return True
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")
            return False

    def return_book(self):
        """Increase available copies by 1 when the book is returned."""
        self._available_copies += 1

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}), Available Copies: {self._available_copies}"
