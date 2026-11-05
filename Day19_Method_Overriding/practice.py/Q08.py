# Create an Animal class with an info() method. Override it in Dog and call the parent method.

#-------------------------------------------------------------------------------------------------------------


class Animal:

    def info(self):
        print(f'Animal Infomation')

class Dog(Animal):

    def info(self):
        super().info()
        print(f'Dogs are domesticated mammals known for loyalty, intelligence, and companionship, with diverse breeds that vary in size, temperament, and care needs.')

a = Dog()
a.info()