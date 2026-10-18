# Extend your Library class.

# Create a method search_book(title) that:

#     Searches for a book by title.
#     Displays the matching book's details.
#     Displays a suitable message if no book is found.

# Test both existing and non-existing titles.

#----------------------------------------------------------------------------

class Library:
    def __init__(self):
        self.title = 'Python'
        self.author = 'Sudhanshu'
        self.price = 7100
    
    def search_book(self,title):
        if title == self.title:
            print(f'Title  = {title}')
            print(f'Author = {self.author}')
            print(f'Price = {self.price}')
        else:
            print('non-existing titles')

e = Library()
e.search_book('Python')