# Create a Book class with:

# title
# author
# price

# Create two objects and compare their __dict__ values.

#-------------------------------------------------------------------------------------------------------


class Book:

    def __init__(self,title,author,price ):
        self.title = title
        self.author = author
        self.price = price


e1 = Book('IOT','sudhanshu Dhande',1000)
e2 = Book('Python with,OOP','Pranay',15000)

print(e1.__dict__)
print('----------------------------------')
print(e2.__dict__)