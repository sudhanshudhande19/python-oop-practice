# Create a parent class Payment with a pay() method. Override it in UPIPayment, CardPayment, and CashPayment.

#----------------------------------------------------------------------------------------------------------------


class Payment:
    def pay(self):
        print("Type of Payment method")

class UPIPayment(Payment):
    def pay(self):
        super().pay()
        print("UPI Payment is a very fast method")

class CardPayment(UPIPayment):
    def pay(self):
        super().pay()
        print("Card Payment method is also secure")

class CashPayment(CardPayment):
    def pay(self):
        super().pay()
        print("Cash payment is the oldest payment method")

d = CashPayment()
d.pay()