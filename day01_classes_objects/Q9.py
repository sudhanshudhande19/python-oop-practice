

class BankAccount:
    balance = int(input("Enter the Balance = "))

    def deposit(self):
        self.deposit = self.deposit + self.balance

    def withdraw(self):
        self.withdraw = self.withdraw - self.balance

    def info(self):
        print(f"Balamce = {self.balance}\nDeposit = {self.deposit}\nWithdraw = {self.withdraw}")

obj = BankAccount()
obj.deposit()
obj.withdraw()
obj.info()