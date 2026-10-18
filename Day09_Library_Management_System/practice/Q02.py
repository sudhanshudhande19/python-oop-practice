# Create a Book class with:

    # title
    # is_available

# Requirements:

    # Set is_available to True initially.
    # Create a method display_status()
    # Display whether the book is available.

#--------------------------------------------------------------------------------

class Book:
    def __init__(self,title):
        self.title = title
        self.is_available = True

    def display_status(self):
            print(f'Book = {self.title}')
            print(f'Available = {self.is_available}')


e = Book('Python Programming')
e.display_status()