# Create a Person class with _age.
# Rules:
    # Age cannot be negative.
    # Age cannot be greater than 120.
    # Valid age should be stored.

# Create an object and test the setter with valid and invalid values.
#-----------------------------------------------------------------------------------

class person:
    def __init__(self,with_age):
        self._with_age = with_age


    @property
    def with_age(self):
        return self._with_age

    @with_age.setter
    def with_age(self,new_age):
        self._with_age = new_age
        if new_age > 0 and new_age  <= 120:
            print('New Age =',new_age)
            print('valid Age')
        else:
            print('New Age =',new_age)
            print('Invalid Age')

obj = person(20)
print('Old Age =',obj.with_age)
obj.with_age = 100