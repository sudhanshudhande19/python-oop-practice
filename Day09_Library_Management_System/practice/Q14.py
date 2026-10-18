# Create methods to calculate:

    # Total number of books.
    # Number of available books.
    # Number of borrowed books.

# Test the statistics before and after borrowing and returning books.
#----------------------------------------------------------------------------------------

class Library:
    def __init__(self):
        self.books = [
            {
                "id": 101,
                "title": "Python",
                "author": "Sudhanshu",
                "is_available": True
            },
            {
                "id": 102,
                "title": "Java",
                "author": "Rahul",
                "is_available": False
            },
            {
                "id": 103,
                "title": "C++",
                "author": "Amit",
                "is_available": True
            }
        ]

    def borrow_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                if book["is_available"]:
                    book["is_available"] = False
                    print("Book borrowed successfully")
                else:
                    print("Book is already borrowed")
                return

        print("Book not found")

    def return_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                if not book["is_available"]:
                    book["is_available"] = True
                    print("Book returned successfully")
                else:
                    print("Book is already available")
                return

        print("Book not found")

    def total_books(self):
        return len(self.books)

    def available_books(self):
        count = 0
        for book in self.books:
            if book["is_available"]:
                count += 1
        return count

    def borrowed_books(self):
        count = 0
        for book in self.books:
            if not book["is_available"]:
                count += 1
        return count

    def display_statistics(self):
        print("\n--- Library Statistics ---")
        print("Total books:", self.total_books())
        print("Available books:", self.available_books())
        print("Borrowed books:", self.borrowed_books())



library = Library()

print("BEFORE BORROWING")
library.display_statistics()

print("\nBorrowing book ID 101:")
library.borrow_book(101)
library.display_statistics()

print("\nReturning book ID 102:")
library.return_book(102)
library.display_statistics()