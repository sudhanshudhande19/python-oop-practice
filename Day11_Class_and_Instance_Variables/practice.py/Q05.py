
# Create a Product class with:

    # Class variable: category = "Electronics"
    # Instance variables: name, price

# Create three products and display their details along with the common category.

#---------------------------------------------------------------------------------------------------------

class Product:
    category = "Electronics"

    def __init__(self,name,price):
        self.name =name
        self.price = price



obj = Product('Tv',5000)
obj2 = Product('Mobile',50000)
obj3 = Product('Fan',1000)

print(f'Product Name {obj.name}  and price {obj.price}  and common category is {Product.category}')
print(f'Product Name {obj2.name} and price {obj2.price} and common category is {Product.category}')
print(f'Product Name {obj3.name} and price {obj3.price} and common category is {Product.category}')