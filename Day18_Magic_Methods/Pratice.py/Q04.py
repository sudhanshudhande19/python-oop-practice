# Create a ShoppingCart class.

# Requirements:

    # Store a list of items.
    # Implement __len__().
    # Use len() to count items.

#-------------------------------------------------------------------------------


class ShoppingCart:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        return len(self.name)


s = ShoppingCart(['Harry','Sudhanshu','kedar','aditya','aniket','omkar','falgun','kunal','pranay','rohit'])
print(len(s))