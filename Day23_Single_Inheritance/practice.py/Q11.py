# Create a LibraryItem parent class and a Book child class.

# Concept: Real-World Inheritance and Encapsulation.

# Requirements:

    # Parent stores title and item ID.

    # Child stores author and price.

    # Protect price using an appropriate encapsulation approach.

    # Add a method to display item information.

    # Use super() to initialize parent attributes.

# --------------------------------------------------------------------------------------------------------------------------------


class LibraryItem:

    def __init__(self,title,item_id):
        self.title = title
        self.item_id = item_id


class Book(LibraryItem):

    def __init__(self, title, item_id,author,price):
        super().__init__(title, item_id)
        self.author = author
        self.price = price

    def details(self):
        print(f'Title = {self.title}')
        print(f'Book ID = {self.item_id}')
        print(f'Author = {self.author}')
        print(f'Price = {self.price}')

b = Book('Python','B112','Sudhanshu',500)
b.details()