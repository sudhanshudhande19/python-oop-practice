# Create a Book class with:

    # title
    # author
    # price

# Implement __repr__() to display the book information.

#---------------------------------------------------------------------------------------


class Book:
    def __init__(self,title,author,price):
        self.title =title
        self.author = author
        self.price = price


    def __repr__(self):
        return f'Title = {self.title!r}\nAuthor = {self.author!r}\nPrice = {self.price!r}'

