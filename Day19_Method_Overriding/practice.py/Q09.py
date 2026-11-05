# Create a Product class with a display() method. Override it in ElectronicProduct.

#--------------------------------------------------------------------------------------------------------


class Product:

    def display(self):
        print(f'Product Details')

class ElectronicProduct(Product):

    def display(self):
        super().display()
        print(f'TV\nMobile')

d = ElectronicProduct()
d.display()