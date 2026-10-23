# Create a Car class with:

# Class variable: wheels = 4
# Instance variables: brand, model

# Create three cars with different brands and models.
# Display the wheels and other details for each car.

#--------------------------------------------------------------------------------------------------------

class car:
    wheels = 4

    def __init__(self,brand, model):
        self.brand = brand
        self.model = model


emp1 = car('BMW',2023)
emp2 = car('Tesla',2024)
emp3 = car('Toyota',2026)


print(f'Brand of Name {emp1.brand} Model  is {emp1.model} and wheels is {car.wheels }')
print(f'Brand of Name {emp2.brand} Model  is {emp2.model} and wheels is {car.wheels }')
print(f'Brand of Name {emp3.brand} Model  is {emp3.model} and wheels is {car.wheels }')
