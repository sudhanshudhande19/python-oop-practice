class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.__account_number = account_number
        self.__balance = balance

    def display_account(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful:", amount)
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Withdrawal successful:", amount)

    @property
    def balance(self):
        return self.__balance

    def verify_account(self, account_number):
        if account_number == self.__account_number:
            print("Account verified!")
            return True
        else:
            print("Invalid account number!")
            return False


# Create three accounts
acc1 = BankAccount("Amit", "101", 5000)
acc2 = BankAccount("Priya", "102", 10000)
acc3 = BankAccount("Rahul", "103", 2000)

# Account 1
print("--- Account 1 ---")
acc1.display_account()
acc1.deposit(1000)
acc1.withdraw(2000)
print("Updated Balance:", acc1.balance)
acc1.verify_account("101")

# Account 2
print("\n--- Account 2 ---")
acc2.display_account()
acc2.withdraw(15000)
acc2.deposit(-500)
print("Current Balance:", acc2.balance)

# Account 3
print("\n--- Account 3 ---")
acc3.display_account()
acc3.deposit(500)
acc3.withdraw(1000)
print("Current Balance:", acc3.balance)
acc3.verify_account("999")