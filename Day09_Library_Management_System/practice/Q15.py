# Improve your Book class.

# Requirements:

    # Use a private attribute __is_available.
    # Create a read-only property named is_available.
    # Create controlled methods to borrow and return the book.
    # Prevent borrowing an already borrowed book.
    # Prevent returning a book that is already available.

# Test all valid and invalid operations.

#-------------------------------------------------------------------------------------------------------


class Book:
    def __init__(self, title):
        self.title = title
        self.__is_available = True

    @property
    def is_available(self):
        return self.__is_available

    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            print("Book borrowed successfully")
        else:
            print("Book is already borrowed")

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print("Book returned successfully")
        else:
            print("Book is already available")

    def display_status(self):
        print("Title:", self.title)
        print("Available:", self.is_available)


# Testing
b1 = Book("Python")

b1.display_status()

print("\n--- Borrow Operations ---")
b1.borrow_book()  # Valid
b1.borrow_book()  # Invalid: already borrowed

print("\n--- Return Operations ---")
b1.return_book()  # Valid
b1.return_book()  # Invalid: already available

print("\n--- Final Status ---")
b1.display_status()