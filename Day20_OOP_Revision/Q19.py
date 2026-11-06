# Create a Library class that stores books in a list. Add, remove, search, and display books.

#---------------------------------------------------------------------------------------------------------------

class Library:
    def __init__(self):
        self.books = []

    def add(self, new_name):
        self.books.append(new_name)
        print(f"{new_name} added successfully.")

    def remove(self, name):
        if name in self.books:
            self.books.remove(name)
            print(f"{name} removed successfully.")
        else:
            print("Enter a valid book name.")

    def search(self, name):
        if name in self.books:
            print(f"Book Name = {name}")
        else:
            print("Book not found.")

    def display(self):
        print("Books in Library:")
        for book in self.books:
            print(book)


s = Library()

s.add("sudhanshu")
s.add("python")

s.display()

s.search("sudhanshu")

s.remove("python")

s.display()