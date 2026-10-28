# Create a Library class with:

    # Class variable: library_name = "City Library"
    # Instance variables: book_title, author

# Requirements:

    # Create a class method change_library_name(new_name).
    # Create three book objects.
    # Change the library name.
    # Display the updated library name with each book.

#------------------------------------------------------------------------------------------------------

class Library:
    library_name = 'City Library'

    def __init__(self,book_title,author):
        self.book_title = book_title
        
        self.author = author

    @classmethod
    def chnage_library_name(cle,new_name):
        cle.library_name = new_name
        print(f'Library Name = {cle.library_name}')

    def show(self):
        print(f'Book Name = {self.book_title}')
        print(f'Author = {self.author}')
        print('-----------------------------')

b1 = Library('OIT','Sudhanshu Dhande')
b2 = Library('Java','Pranay Dhande')
b3 = Library('Pythn','Kunal')

Library.chnage_library_name('National Library')
b1.show()
b2.show()
b3.show()
