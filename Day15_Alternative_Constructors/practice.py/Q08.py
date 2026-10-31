# Create a Book class with:

    # book_id
    # title
    # author
    # price

# Requirements:

    # Create a class method from_list(data).
    # Accept a list containing all four values.
    # Create a Book object.
    # Display the book details.

#-----------------------------------------------------------------------------------------------------


class Book:
    def __init__(self,book_id,title,author,price):
        self.book_id = book_id
        self.title =  title
        self.author = author
        self.price = price


    @classmethod
    def from_list(cls,data):
        return cls(
            data[0],
            data[1],
            data[2],
            data[3]
        )

e1 = Book.from_list(['101','IOT','Sudhanshu','2000'])

print(f'Book ID = {e1.book_id}')
print(f'Title Name = {e1.title}')
print(f'Author = {e1.author}')
print(f'Price = {e1.price}')
