# Create a BankAccount class with _balance.

    # Getter: return the current balance.
    # Setter: accept a new balance only if it is non-negative.

# Test the property with different values.
#-----------------------------------------------------------------

class bankaccount:
    def __init__(self,with_balance):
        self._with_balance = with_balance

    @property
    def with_balance(self):
        return self._with_balance

    @ with_balance.setter
    def with_balance(self,new_balance):
        self._with_balance = new_balance
        if new_balance > 0:
            print('New Balance =',new_balance)
            print('Accept The Positive Balance')
        else:
            print('New Balance =',new_balance)
            print('Not Accept The non-negative Balance')

obj = bankaccount(6000)
print('Old Balance =',obj.with_balance)
obj.with_balance = 500

        