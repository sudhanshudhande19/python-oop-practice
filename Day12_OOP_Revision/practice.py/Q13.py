# Create a Book class with:

    # book_id
    # title
    # author
    # Private attribute __is_available

# Methods:

    # borrow_book()
    # return_book()
    # display_details()

# Requirements:

    # Prevent borrowing a book that is already borrowed.
    # Prevent returning a book that is already available.
    # Test all cases.

#-------------------------------------------------------------------------------------------------------


class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__is_available = True

    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            print(f"{self.title} borrowed successfully.")
        else:
            print(f"{self.title} is already borrowed.")

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"{self.title} returned successfully.")
        else:
            print(f"{self.title} is already available.")

    def display_details(self):
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Available : {self.__is_available}")
        print("-" * 30)


# Testing all cases

book1 = Book(101, "Python", "Sudhanshu")

book1.display_details()

# Borrow book
book1.borrow_book()

# Borrow again
book1.borrow_book()

# Return book
book1.return_book()

# Return again
book1.return_book()

book1.display_details()