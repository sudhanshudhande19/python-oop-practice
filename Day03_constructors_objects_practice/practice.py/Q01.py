# Create a Person class with:
# 1.name
# 2.age
# 3.city
# Use a constructor to initialize the values.

# Create a method:
# display_info()
# Display the person's complete information.
# Create 3 objects with different data.

#--------------------------------------------------------------

class person:
    def __init__(self,name ,age,city):
        self.name =name
        self.age = age
        self.city = city

    def display_info(self):
        print(f'Name = {self.name}\nAge = {self.age}\nCitya = {self.city}')
        print('---------------------------------------------------')

obj = person('Sudhanshu Dhande',21,'Sakoli')
obj2 = person('Pranay Dhande',22,'Bhandara')
obj3 = person('Nehal Dhande',17,'Nagpur')
obj.display_info()
obj2.display_info()
obj3.display_info()