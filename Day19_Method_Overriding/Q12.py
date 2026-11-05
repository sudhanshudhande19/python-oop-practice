# Create a parent class Notification with a send() method. Override it in EmailNotification and SMSNotification.

#---------------------------------------------------------------------------------------------------------------------------------------------

class Notification:

    def send(self):
        print(f'Notification')


class EmailNotification(Notification):

    def send(self):
        super().send()
        print(f'Email Notification is the best notification of job email')

class SMSNotification(EmailNotification):

    def send(self):
        super().send()
        print(f'SMS Notification is the very older notification ')


e = SMSNotification()
e.send()