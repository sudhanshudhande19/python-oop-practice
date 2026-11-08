# Create a BankAccount class and overload > and ==.

# Requirements:

    # Store account holder name.
    # Store account balance.
    # Define __gt__() to compare balances.
    # Define __eq__() to compare balances.
    # Test two different accounts.

#----------------------------------------------------------------------------------------------


class bankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder 
        self.balance = balance  

    def __gt__(self, other):
        return self.balance > other.balance

    def __eq__(self, value):
        return self.balance == value.balance

    def __str__(self):
        return f'Name = {self.account_holder}\nBalnce = {self.balance}\n---------------------'

a1 = bankAccount('Sudhanshu',5000)
a2 = bankAccount('Pranay',6000)
print(a1 > a2)
print(a1 == a2)

a3 = bankAccount("A", 5000)
a4 = bankAccount("B", 5000)

print(a3 == a4)