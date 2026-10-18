# Create a Book class with:
    # title
    # author
    # publication_year

# Create a method display_info().
# Create at least three books and display their information.

#------------------------------------------------------------------------------------------

class Book:
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print('=======Book Details==========')
        print(f'Title = {self.title}')
        print(f'Author = {self.author}')
        print(f'Publication Year = {self.publication_year}')
        print('----------------------------------------------------------')

e = Book('Java','sudhanshu',2024)
r = Book('Python','kunal',2023)
o = Book('HTML','Devika',2026)

e.display_info()
r.display_info()
o.display_info()