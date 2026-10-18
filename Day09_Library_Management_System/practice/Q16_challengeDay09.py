class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.__is_available = True

    @property
    def is_available(self):
        return self.__is_available

    def borrow(self):
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

    def display_book(self):
        print("ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Available:", self.is_available)
       


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book

        return None

    def borrow_book(self, book_id):
        book = self.search_by_id(book_id)

        if book is not None:
            book.borrow()
        else:
            print("Book not found!")

    def return_book(self, book_id):
        book = self.search_by_id(book_id)

        if book is not None:
            book.return_book()
        else:
            print("Book not found!")


# Create Book objects
b1 = Book(101, "Python", "Amit", 500)
b2 = Book(102, "Java", "Rahul", 600)
b3 = Book(103, "AI and ML", "Priya", 700)

# Create Library object
library = Library("KCEM Library")

# Add Book objects to the library
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

print("Library Name:", library.name)

# Search book by ID
book = library.search_by_id(102)

if book is not None:
    book.display_book()
else:
    print("Book not found!")

# Borrow and return a book
library.borrow_book(102)
library.return_book(102)

# Try an ID that does not exist
library.borrow_book(999)






b1 = Book(101,"Python",'Amit',500)
b1.display_book()

b1.borrow()
b1.borrow()

b1.return_book
b1.return_book
b1.display_book()
