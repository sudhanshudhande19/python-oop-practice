# Create a parent class Payment with a method process_payment().

# Create child classes:
    # UPIPayment
    # CardPayment
    # CashPayment

# Override the method in each class to display a suitable payment message.

#-----------------------------------------------------------------------------------------------------

class Payment:
    def process_payment(self):
        print('Process The Payment')

class UPIPayment(Payment):
    def process_payment(self):
        print('Process the UPI Payment')

class CardPayment(Payment):
    def process_payment(self):
        print('Processing the card payment')

class CashPayment(Payment):
    def process_payment(self):
        print('Done the Cash Payment')

e = Payment()
e.process_payment()

e = UPIPayment()
e.process_payment()

e = CardPayment()
e.process_payment()

e = CashPayment()
e.process_payment()
