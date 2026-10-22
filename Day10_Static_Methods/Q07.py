# Create a UserValidator class with a static method is_valid_password(password).

# Requirements:

    # Password must contain at least 8 characters.
    # Return True if it satisfies the length requirement.
    # Otherwise, return False.

#----------------------------------------------------------------------------------------------------------------


class UserValidator:

    @staticmethod
    def is_valid_password(password):
        if len(password) == 8:
            return True
        else:
            return False

kk = input('Enter The 8 Characters Password =')
r = UserValidator.is_valid_password(kk)
print(r)

kl = input('Enter The 8 Characters Password =')
r = UserValidator.is_valid_password(kl)
print(r)