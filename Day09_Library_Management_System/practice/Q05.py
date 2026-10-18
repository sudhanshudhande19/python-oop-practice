# Create a Book class with a class attribute book_count.

# Requirements:
    # Increase the count whenever a new book object is created.
    # Create five book objects.
    # Display the total number of created book objects.
    # Hint: Use a class attribute and update it inside __init__().

#--------------------------------------------------------------------------------------------

class Book:
    book_count = 0

    def __init__(self, title):
        self.title = title
        Book.book_count += 1


b1 = Book("Python")
b2 = Book("Java")
b3 = Book("C++")
b4 = Book("AI")
b5 = Book("Machine Learning")

print("Total books created:", Book.book_count)