# Create a Library class with:

    # Class variable: library_name = "City Library"
    # Instance variables: book_name, author
    # Create three book objects and display their details with the library name.
    # Change the library name using the class name and observe the results.


#-------------------------------------------------------------------------------------------------------------------

class Library:
    library_name = "City Library"
    def __init__(self,book_name,author):
        self.book_name = book_name
        self.author = author


bk1 = Library('IOT','Sudhanshu')
bk2 = Library('Java','Kunal')
bk3 = Library('Python','Ayush')

print(f'Book Name = {bk1.book_name}, Author ={bk1.author}, Library = {Library.library_name}')
print(f'Book Name = {bk2.book_name}, Author ={bk2.author}, Library = {Library.library_name}')
print(f'Book Name = {bk3.book_name}, Author ={bk3.author}, Library = {Library.library_name}')
print('-------------------------------------------------------------------------------------------------')

Library.library_name = 'National Library'
print(f'Book Name = {bk1.book_name}, Author ={bk1.author}, Library = {Library.library_name}')
print(f'Book Name = {bk2.book_name}, Author ={bk2.author}, Library = {Library.library_name}')
print(f'Book Name = {bk3.book_name}, Author ={bk3.author}, Library = {Library.library_name}')
