# Create a method search_by_id(book_id).
# Requirements:
    # Search for a book using its unique ID.
    # Return the matching book object if found.
    # Return None if no book is found.

# Test with valid and invalid IDs

#----------------------------------------------------------------------------------------

class Library:
    def __init__(self):
        self.id = 10123
        self.title = 'Python'
        self.author = 'Sudhanshu'
        self.price = 7100
    
    def search_by_id(self,book_id):
        if book_id == self.id:
            print('Valid Id')
            print(f'Book ID = {book_id}')
            print(f'Title  = {self.title}')
            print(f'Author = {self.author}')
            print(f'Price = {self.price}')
        else:
            print('Not Found ')
            print('InValid ID')


e = Library()
e.search_by_id(1012)