# Create a Car class with( brand , model , price) Create one object and display the car information.
#--------------------------------------------------------------------------------

class car:
    brand = 'BMW'
    Model = 2023
    price = 800000

    def show(self):
        print(f'Brand = {self.brand}\nModel = {self.Model}\nPrice = {self.price}')

obj = car()
obj.show()