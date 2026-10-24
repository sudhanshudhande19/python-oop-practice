# Create a Book class with:

    # book_id
    # title
    # author
    # Private attribute __is_available

# Methods:

    # borrow_book()
    # return_book()
    # display_details()

# Requirements:

    # Prevent borrowing a book that is already borrowed.
    # Prevent returning a book that is already available.
    # Test all cases.

#-------------------------------------------------------------------------------------------------------


class BookL:
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title =title
        self.author = author
        self.__is_available = True

    def borrow_book(self):
        if self.__is_available == True:
            

