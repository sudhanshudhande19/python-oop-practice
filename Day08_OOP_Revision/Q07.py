# Create a BankAccount class with:
    # account_holder
    # __balance

# Methods:
    # deposit(amount)
    # withdraw(amount)
    # get_balance()

# Rules:
    # Deposit must be positive.
    # Withdrawal must be positive.
    # Withdrawal cannot exceed the available balance.
    # Do not allow direct public modification of the balance.

#-------------------------------------------------------------------------------------------------

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit =", amount)
        else:
            print("Enter positive amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.__balance:
                print("Insufficient balance")
            else:
                self.__balance -= amount
                print("Withdraw =", amount)
        else:
            print("Enter positive amount")

    def get_balance(self):
        print("Account Holder =", self.account_holder)
        print("Balance =", self.__balance)
        print("-" * 30)


e = BankAccount("Sudhanshu", 40000)

e.get_balance()

e.deposit(5000)
e.get_balance()

e.withdraw(4000)
e.get_balance()