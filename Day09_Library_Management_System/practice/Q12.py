# Create a method display_available_books().

# Requirements:
    # Display only books whose availability status is True.
    # Do not display borrowed books in this list.
    # Display a message if no books are available.
#--------------------------------------------------------------------------------

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
    def display_available_books(self):
            found = False
            for book in self.books:
                if book["is_available"] == True:
                    found =True
                    print(f"Book ID = {book['id']}")
                    print(f"Title = {book['title']}")
                    print(f"Author = {book['author']}")
                    print(f"Available = {book['is_available']}")
                    print("-" * 35)
                
            if found == False:
                     print('No books are available')
    


e = Library()

e.display_available_books()

