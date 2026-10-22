# Create a NumberChecker class with a static method check_number(number).

# Return whether the number is positive, negative, or zero.

#----------------------------------------------------------------------------------------------


class NumberChecker:
    @ staticmethod
    def chech_number(number):
        if number > 0:
            return 'Positive'
        elif number == 0:
            return 'Zero'
        else:
            return 'Negative'
r = NumberChecker.chech_number(5)
print(r)

r = NumberChecker.chech_number(0)
print(r)

r = NumberChecker.chech_number(-1)
print(r)