# Create a method return_book(book_id).

# Requirements:
    # Find the book by ID.
    # If the book is currently borrowed, mark it as available.
    # If it is already available, display a suitable message.
    # If it does not exist, display a suitable message.

# Test all cases.

#--------------------------------------------------------------------------------------------------------------------

class Library:
    def __init__(self):
        self.id = 10123
        self.title = 'Python'
        self.author = 'Sudhanshu'
        self.price = 7100
        self.is_availble = True
    
    def return_book(self,book_id):
        if book_id == self.id:
            if self.is_availble == False:
                self.is_availble = True
                print('Book returned successfully')
                
            else:
    
                print('Book is already available')
                print(f'Book ID = {self.id}')
                print(f'Title  = {self.title}')
                print(f'Author = {self.author}')
                print(f'Price = {self.price}')
                print(f'Avaible = {self.is_availble}')
                print('------------------------------------')
        else:
            print('Book not found')



e = Library()

e.return_book(10123)
e.return_book(10123)
e.return_book(99999)