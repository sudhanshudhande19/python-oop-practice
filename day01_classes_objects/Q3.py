# Create a Mobile class with (brand ,model ,price) Create an object and display its details.

class Mobile:
    Brand = 'Samsung'
    Model = 2025
    price = 49000

    def info(self):
        print(f'Brand = {self.Brand}\nModel = {self.Model}\nPrice = {self.price}')

r1 = Mobile()
r1.info()