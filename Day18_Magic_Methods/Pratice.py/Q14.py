# Create a Library class.

# Requirements:

    # Store a list of books.
    # Implement __len__().
    # Implement __contains__().
    # Use len() to count books.
    # Use in to check whether a book exists.

#------------------------------------------------------------------------------------

class Library:

    def __init__(self,book):
        self.book = book

    def __len__(self):
        return len(self.book)

    def __contains__(self, item):
        return item in self.book

e = Library(['OIT','java','python','c','c++'])

print(len(e))
print('python' in e)
print('Java' in e)