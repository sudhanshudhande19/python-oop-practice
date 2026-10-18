# Update add_book(book).
# Requirements:
    # Every book must have a unique ID.
    # Before adding a book, check whether its ID already exists.
    # Reject duplicate IDs.
    # Test adding two books with the same ID.
#-------------------------------------------------------------------------------------

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
                }
        ]
    def add_book(self, book):
            for i in self.books:
                if i["id"] == book["id"]:
                    print("Reject: Duplicate book ID")
                    return

            self.books.append(book)
            print("Book added successfully")

e = Library()

e.add_book({
    "id": 101,
    "title": "Python",
    "author": "Sudhanshu",
    "is_available": True
})

e.add_book({
    "id": 103,
    "title": "C++",
    "author": "Amit",
    "is_available": True
})

print(e.books)