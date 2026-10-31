# Create a Library class with:

    # library_name
    # books
    # add_book()
    # display_books()

# Use dir(), __dict__ and help() to inspect the class and its object.

#------------------------------------------------------------------------------------------------------------

class Library:

    def __init__(self,library_name):
        self.library_name = library_name
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def display_book(self):
        print(f'Library Name = {self.library_name}')
        print(f'Book = {self.books}')

e  =  Library('Nation Library')
e.add_books('Python')
e.display_book()

print(dir(e))
print(e.__dict__)
print(help(e))