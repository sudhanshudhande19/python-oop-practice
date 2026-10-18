# Create a method display_all_books().

# Requirements:
    # Display every book stored in the library.
    # Display the ID, title, author, and availability status.
    # If the library is empty, display an appropriate message.

#------------------------------------------------------------

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

    def display_all_books(self):
            if not self.books:
                 print('Library is Empty')
            else:
                for book in self.books:
                    print(f"Book ID = {book['id']}")
                    print(f"Title = {book['title']}")
                    print(f"Author = {book['author']}")
                    print(f"Available = {book['is_available']}")
                    print("-" * 35)


e = Library()

e.display_all_books()

