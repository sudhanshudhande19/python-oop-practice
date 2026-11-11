# Concept: Real-world Multilevel Inheritance.

# Requirements:

    # Create Library, LibraryItem, and Book classes.
    # Library stores library name.
    # LibraryItem stores item ID and title.
    # Book stores author and price.
    # Create a method to display book information.
    # Display all details.

#-----------------------------------------------------------------------------------------


class Library:
    def __init__(self,library_name):
        self.library_name = library_name

class library_item(Library):

    def __init__(self, library_name,id,title):
        super().__init__(library_name)
        self.id = id
        self.title = title

class Book(library_item):

    def __init__(self, library_name, id, title,author,price):
        super().__init__(library_name, id, title)
        self.author = author
        self.price = price

    def book_info(self):
        print(f'Library Name = {self.library_name}')
        print(f'Item ID =  {self.id}')
        print(f'Title   = {self.title}')
        print(f'Author  = {self.author}')
        print(f'Price   = {self.price}')

s = Book(
    'National Library',
    101,
    'Python Programming',
    'Sudhanshu',
    500
)
s.book_info()