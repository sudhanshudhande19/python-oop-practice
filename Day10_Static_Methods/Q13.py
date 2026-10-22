# Create a BankUtility class with a static method is_valid_amount(amount).

# Requirements:

    # Return True only when the amount is greater than zero.
    # Test zero, negative, and positive amounts.

#----------------------------------------------------------------------------------------------------------------

class BankUtility:
    @staticmethod
    def is_valid_amount(amount):
        if amount > 0:
            return True
        elif amount == 0:
            return 'Zero Amount Not accept'
        else:
            return 'Negative Amount Not Accept'

print('-----------Bank Transaction ---------------')
ff = int(input('Enter The Amount = '))
r = BankUtility.is_valid_amount(ff)
print(r)