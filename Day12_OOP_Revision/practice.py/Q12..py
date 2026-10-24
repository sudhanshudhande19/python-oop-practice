# Create a parent class Payment with a method process_payment(amount).

# Create child classes:

    # UPIPayment
    # CardPayment
    # CashPayment

# Requirements:

    # Override the payment method in each child class.
    # Validate that the amount is positive.
    # Display a suitable message for each payment type.


#-------------------------------------------------------------------------------------------------------


class Payment:
    def process_payment(self, amount):
        if amount <= 0:
            print("Invalid amount! Amount must be positive.")
        else:
            print("Processing payment...")


class UPIPayment(Payment):
    def process_payment(self, amount):
        if amount <= 0:
            print("Invalid amount! Amount must be positive.")
        else:
            print(f"₹{amount} paid successfully using UPI.")


class CardPayment(Payment):
    def process_payment(self, amount):
        if amount <= 0:
            print("Invalid amount! Amount must be positive.")
        else:
            print(f"₹{amount} paid successfully using Card.")


class CashPayment(Payment):
    def process_payment(self, amount):
        if amount <= 0:
            print("Invalid amount! Amount must be positive.")
        else:
            print(f"₹{amount} paid successfully using Cash.")


#
upi = UPIPayment()
card = CardPayment()
cash = CashPayment()


upi.process_payment(500)
card.process_payment(1000)
cash.process_payment(200)


upi.process_payment(-100)
card.process_payment(0)
