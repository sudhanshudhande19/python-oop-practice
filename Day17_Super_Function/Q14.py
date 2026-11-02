# Create a LibraryItem class with:

    # title
    # item_id
    # display_info()

# Create child classes:

    # Book
    # Magazine

# Requirements:

    # Use super() in constructors.
    # Override display_info().
    # Call the parent method using super().

#-------------------------------------------------------------------------------------------

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def display_info(self):
        print(f"Title = {self.title}")
        print(f"Item ID = {self.item_id}")


class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author = {self.author}")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_no):
        super().__init__(title, item_id)
        self.issue_no = issue_no

    def display_info(self):
        super().display_info()
        print(f"Issue No = {self.issue_no}")


b = Book("Python Programming", 101, "Sudhanshu Dhande")
m = Magazine("Tech Monthly", 202, 15)

print("Book Details:")
b.display_info()

print("\nMagazine Details:")
m.display_info()