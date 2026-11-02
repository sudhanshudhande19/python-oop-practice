# Create a Payment class with a process_payment() method.

# Create child classes:

    # UPIPayment
    # CardPayment

# Each child class should call the parent method using super() and then display its payment details.

#-----------------------------------------------------------------------------------------------------------------------------------


class Payment:
    def process_payment(self):
        print('Payment Online Process')

class UPIPayment(Payment):
    def process_payment(self):
        super().process_payment()
        print('UPI payment Is Very fast ')

class cardPayment(UPIPayment):
    def process_payment(self):
        super().process_payment()
        print('Card Payment Proccesing')


e1 = cardPayment()

e1.process_payment()