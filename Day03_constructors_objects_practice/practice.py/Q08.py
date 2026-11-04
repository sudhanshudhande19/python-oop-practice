# Create a BankAccount class with:
# account_holder
# balance

# Create methods:
# deposit(amount)
# withdraw(amount)
# check_balance()

# Rules:
# Deposit must be positive.
# Withdrawal must be positive.
# Withdrawal cannot exceed the balance.

# Test the account using multiple transactions.
#------------------------------------------------------------

class BankAccount:
    def __init__(self, account_holder, account_number, balance, amount):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.amount = amount

    def deposit(self):
        if self.amount > 0:
            return self.balance + self.amount
        else:
            return "Enter The Positive Amount"

    def withdraw(self):
        if self.amount <= self.balance:
            if self.amount > 0:
                return self.balance - self.amount
            else:
                return "Enter The Positive Withdraw Amount"
        else:
            return "Insufficient Balance"

    def check_balance(self):
        print(f"Account Holder Name = {self.account_holder}")
        print(f"Account Number = {self.account_number}")
        print(f'Deposit = {self.deposit()}')
        print(f'Withdraw = {self.withdraw()}')
        print(f"Balance = {self.balance}")


obj = BankAccount("Sudhanshu Dhande",23046719997002, 10000,5000)

obj.deposit()    # 20000 + 5000 = 25000
obj.withdraw()   # 25000 - 5000 = 20000
obj.check_balance()
