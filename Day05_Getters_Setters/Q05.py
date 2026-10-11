# Create a BankAccount class with _balance.

    # Getter: return the current balance.
    # Setter: accept a new balance only if it is non-negative.

# Test the property with different values.
#-----------------------------------------------------------------
class BankAccount:
    def __init__(self, balance):
        self._balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
            print("New Balance =", new_balance)
        else:
            print("Invalid Balance Rejected")


obj = BankAccount(6000)
print("Current Balance =", obj.balance)

obj.balance = 500
print("Current Balance =", obj.balance)

obj.balance = 0
print("Current Balance =", obj.balance)

obj.balance = -100
print("Current Balance =", obj.balance)

        