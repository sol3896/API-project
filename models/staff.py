from .user import User

class Staff(User):
    """
    Class representing a staff member with borrowing privileges.
    """
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def borrow_book(self, book):
        """
        Staff members can borrow books with extended time.
        """
        print(f"Staff privilege: {self.name} can borrow books for extended time.")
        super().borrow_book(book)
