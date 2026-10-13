# Create a parent class LibraryItem with
    # title
    # item_id
    # display_item()

# Create a child class Book with:
    # author
    # pages

# Use super() to initialize parent attributes and display all details.
#------------------------------------------------------------------------------------

class libraryitem:
    def __init__(self,title,item_id):
        self.title = title
        self.item_id = item_id

    def display_item(self):
        print(f'Title  = {self.title}\nItem ID = {self.item_id}')

class book(libraryitem):
    def __init__(self, title, item_id,author,pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages


e1 = book('Life is end',101,'Harry',254)
e1.display_item()
print('Author  =',e1.author)
print('Pages   =',e1.pages)
