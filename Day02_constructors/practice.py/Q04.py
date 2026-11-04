# Create a Book class with a constructor that accepts:

#1.title
#2.author
#3.price

# Create one object and display the book information.
#------------------------------------------------------------------------------

class book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def info(self):
        print(f'Title ={self.title}\nAuthor ={self.author}\nPrice = {self.price}')

obj = book('Time is Money','Sudhanshu Dhande',500)
obj.info()