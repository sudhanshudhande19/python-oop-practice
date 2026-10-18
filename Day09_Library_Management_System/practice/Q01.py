# Create a Book class with these attributes:
    # book_id
    # title
    # author
    # price

# Requirements:
    # Initialize all attributes using __init__().
    # Create a method display_book().
    # Create three book objects and display their details.

#-----------------------------------------------------------------------------------------

class book:
    def __init__(self,book_id,title,author,price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price


    def display_book(self):
        print('======Book Details ===========')
        print(f'Book ID = {self.book_id}')
        print(f'Book Title = {self.title}')
        print(f'Author = {self.author}')
        print(f'Price = {self.price}')
        print('------------------------------------------------')

e = book(10123,'Python','sudhanshu',500)
e2 = book(10234,'java','pranay',800)
e3 = book(101235,'c++','Prachi',780)

e.display_book()
e2.display_book()
e3.display_book()