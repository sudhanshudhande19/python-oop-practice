# Create a Book class with:
    # title
    # author
    # price
    # is_available

# Methods:
    # display_book()
    # borrow_book()
    # return_book()

# Requirements:

    # A book can be borrowed only when available.
    # Borrowing changes availability to unavailable.
    # Returning changes availability to available.
    # Display suitable messages for invalid operations.
#---------------------------------------------------------------------------------
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.is_available = True

    def display_book(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("Price :", self.price)
        print("Available:", self.is_available)
        print("-" * 30)

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' is already available.")

b1 = Book("Python Programming", "Sudhanshu", 499)

b1.display_book()

b1.borrow_book()
b1.display_book()

b1.borrow_book()     

b1.return_book()
b1.display_book()

b1.return_book()      