# Create a BankAccount class with:

    # account_holder
    # account_number
    # balance

# Requirements:

    # Create a class method from_string(data).
    # Accept input in the format "Rahul,12345,10000".
    # Convert the balance into a numeric value.
    # Reject negative balances.
    # Display the account details.

#---------------------------------------------------------------------------------------------------


class BankAccount:

    def __init__(self,account_holder,account_number,balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    @classmethod
    def from_string(cls,data):
        name,number,balance = data.split(',')
        return cls(name,number,int(balance))

e1 = BankAccount.from_string('Rahul,12345,10000')

print(f'Holder Name = {e1.account_holder}')
print(f'Account Number = {e1.account_number}')

if e1.balance >= 0:
    print(f'Balance = {e1.balance}')
else:
    print('Raject the Negative Balance')