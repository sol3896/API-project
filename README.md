166910 Sol Ikamar
169388 Laura Chetalam

Library Management System Documentation
Overview
The Library Management System is a Python-based application designed to manage the operations of a library, 
enabling users to add, borrow, and return books. This system is built with Object-Oriented Programming (OOP) principles, 
including inheritance, polymorphism, encapsulation, and abstraction, and is organized into several modular components. 
The application is interactive, user-friendly, and provides functionality for both library members and staff.

Purpose
The system aims to:

Enable users to interact with the library by borrowing and returning books.
Allow staff to manage library resources by adding new books and registering users.
Track each book's availability and user borrowing status.
Demonstrate key OOP concepts in a practical library management application.
Main Components
Book: Represents a book in the library, with attributes such as title, author, ISBN, and available copies. It also provides methods for borrowing and returning books, with built-in checks for availability.

Person (Abstract Class): An abstract base class that defines the core structure for User and Staff classes, which represent the different types of library users.

User: Represents a library member, allowing them to borrow and return books. A user's borrowed books are tracked, and they must return borrowed books to make them available for others.

Staff: Inherits from User, representing library staff with similar privileges as members but with additional responsibilities, like managing the library collection.

Library: Manages the collection of books and users, providing methods for adding books, registering users, borrowing, returning, and viewing all available books. 
It also facilitates interactions between users and the library's book inventory.

Features
Interactive Menu: A command-line menu allows users to add books, register users, borrow/return books, and view the library's book collection.

Exception Handling: The system checks book availability when borrowing and validates user IDs to ensure only registered users can borrow or return books.

Encapsulation: Sensitive data, such as available copies of books, is kept private within classes.

Inheritance and Polymorphism: The User and Staff classes inherit from Person, with Staff also overriding certain behaviors to reflect their extended privileges.

Usage
Run the main.py file to start the Library Management System. Follow on-screen prompts to navigate the system, register users, add books, and manage borrowing/returning operations.
