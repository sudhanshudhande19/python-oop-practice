# Library 
#---------------------------------------------
class Library:
    name = ''
    book_name = ''
    total_books = 0

    def issue_book(self):
        if self.total_books > 0:
            self.total_books -= 1
            print(f"{self.book_name} issued successfully.")
        else:
            print("Book not available.")

    def available_books(self):
        print(f"Available Copies = {self.total_books}")
    
    def info(self):
        print(f"Library Name = {self.name}")
        print(f"Book Name = {self.book_name}")
        print(f"Copies Available = {self.total_books}")
        print()

 # Object 1
lib1 = Library()
lib1.name = "City Library"
lib1.book_name = "Python Programming"
lib1.total_books = 5

# Object 2
lib2 = Library()
lib2.name = "College Library"
lib2.book_name = "Data Structures"
lib2.total_books = 3

lib1.info()
lib1.issue_book()
lib1.available_books()
print()

lib2.info()
lib2.issue_book()
lib2.available_books()