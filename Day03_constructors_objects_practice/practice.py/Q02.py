# Create a Laptop class with:
# 1.brand
# 2.model
# 3.ram
# 4.price

# Create a method:
# display_details()

# Create two laptop objects and display their details.
#-------------------------------------------------------------------

class laptop:
    def __init__(self,brand,model,ram,price):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.price = price

    def display_details(self):
        print(f'Brand = {self.brand}\nModel = {self.model}\nRam = {self.ram}\nPrice = {self.price}\n')
        print('------------------------------------------')

obj = laptop('Asus',2024,'1T',175000)
obj2 = laptop('Asusu Vivo Book',2024,'512GB',40000)


obj.display_details()
obj2.display_details()