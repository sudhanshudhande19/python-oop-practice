# Create a BankAccount class with:

    # account_holder
    # __balance

# Create methods:

    # deposit(amount)
    # withdraw(amount)
    # get_balance()

# Rules:

    # Deposit must be positive.
    # Withdrawal must be positive.
    # Withdrawal cannot exceed the balance.
    # Test different transactions.
#----------------------------------------------------------------------

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def get_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.__balance)


obj = BankAccount("Sudhanshu Dhande", 40000)

obj.get_balance()

obj.deposit(5000)
obj.get_balance()

obj.withdraw(4000)
obj.get_balance()

obj.withdraw(50000)
obj.deposit(-100)
obj.withdraw(-200)
