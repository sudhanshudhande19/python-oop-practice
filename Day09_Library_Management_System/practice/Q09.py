# Create a method borrow_book(book_id).

# Requirements:
    # Find the book by ID.
    # Check whether it is available.
    # If available, mark it as unavailable.
    # If already borrowed, display a suitable message.
    # If the book does not exist, display a suitable message.

# Test all three cases.

#------------------------------------------------------------------------------------

class Library:
    def __init__(self):
        self.id = 10123
        self.title = 'Python'
        self.author = 'Sudhanshu'
        self.price = 7100
        self.is_availble = True
    
    def borrow_book(self,book_id):
        if book_id == self.id:
            if self.is_availble == False:
                print('Book is already borrowed')
            else:
                self.is_available = False
                print('Book borrowed successfully')
                print(f'Book ID = {self.id}')
                print(f'Title  = {self.title}')
                print(f'Author = {self.author}')
                print(f'Price = {self.price}')
                print(f'Avaible = {self.is_availble}')
                print('------------------------------------')
        else:
            print('Book not found')



e = Library()

e.borrow_book(10123)
e.borrow_book(10123)
e.borrow_book(99999)