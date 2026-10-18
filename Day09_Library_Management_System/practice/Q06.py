# Create a Library class that stores books in a list.

# Requirements:
    # Create an empty list in __init__().
    # Create a method add_book(book).
    # Add at least five Book objects to the library.
    # Display all books.

#------------------------------------------------------------------------------------

class Library:
    def __init__(self):
        self.stores_book = []

    def add_book(self,book):
        self.stores_book.append(book)
        for i in self.stores_book:
            print(i)

b1 = Library()
b2 = Library()
b3 = Library()
b4 = Library()
b5 = Library()

b1.add_book('pyhton')
b2.add_book('java')
b3.add_book('c')
b4.add_book('c++')
b5.add_book('ML')


    