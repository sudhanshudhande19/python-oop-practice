# Create a BankAccount class with:
# account_holder
# account_number
# balance

# Create methods:
# deposit(amount)
# withdraw(amount)
# check_balance()

# Rules:
# Deposit amount must be greater than 0.
# Withdrawal amount must be greater than 0.
# Withdrawal should not be greater than the available balance.
# Display an appropriate message for invalid operations.

# Test the program with different values.
#----------------------------------------------------------------------

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Available Balance: ₹{self.balance}")

    def info(self):
        print("\n----- Account Details -----")
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        self.check_balance()


acc1 = BankAccount("Sudhanshu", "1234567890",10000)

acc1.info()

acc1.deposit(5000)
acc1.check_balance()

acc1.deposit(-100)


acc1.withdraw(3000)
acc1.check_balance()


acc1.withdraw(20000)


acc1.withdraw(-500)
acc1.check_balance()