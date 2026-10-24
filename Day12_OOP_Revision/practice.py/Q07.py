# Create a NumberUtility class with static methods:

    # is_even(number)
    # is_positive(number)
    # square(number)

# Call each method using the class name and test different values.

#-------------------------------------------------------------------------------------------------------------------

class NumberUtility:
    @staticmethod
    def is_even(number):
        if number %2 == 0:
            print(f'Even number = {True}')
        else:
            print(f'Even Number = {False}')

    @staticmethod
    def is_positive(number):
        if number >= 0:
            print(f'Number is Positive')
        else:
            print('Number is Negative')

    @staticmethod
    def square(number):
        print(f'Square {number} = {number *  number}')

e1 = NumberUtility.is_even(5)

e1 = NumberUtility.is_positive(5)

e1 = NumberUtility.square(5)
