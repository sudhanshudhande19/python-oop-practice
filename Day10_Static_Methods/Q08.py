# Create an EmailValidator class with a static method is_valid_email(email).
# For this beginner exercise, check whether the email contains @ and a . after the @.

# Note: This is a basic practice check, not complete email validation.


#-------------------------------------------------------------------------------------------------------------


class EmailValidator:
    @staticmethod
    def  is_valid_email(email):
        for i in email:
            if '@' in email:
                print('Valid Email')
                return True
            else:
                print('InValid Email')
                return False


tt = input("Enter The Email =")
r = EmailValidator.is_valid_email(tt)

print(r)