# Create a Book class with title, author, and price. Create one object and display the book details.
#--------------------------------------------------------------------------------------

class Book:
    title = input('Enter The Book Title Name =')
    author =input('Enter The Author Name =')
    price = int(input("Enter The Book Price ="))

    def apply_discount(self):
        print(f'Title = {self.title}\nAuthor = {self.author}\nDiscount Price = {self.price}')

obj = Book()
obj.apply_discount()
      