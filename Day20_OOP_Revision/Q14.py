# Create a Payment parent class and UPI, Card, and Cash payment classes with different payment methods.

#------------------------------------------------------------------------------------------------------------------


class Payment:
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


upi = UPI()
card = Card()
cash = Cash()

upi.pay(1000)
card.pay(2000)
cash.pay(500)