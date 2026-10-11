# Create a User class with _email.

    # Create a getter and setter.
    # Reject an email that does not contain @.
    # Test with valid and invalid email values.

# Note: This is a beginner-level validation exercise
#---------------------------------------------------------------------------


class User:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if '@' in new_email and '.' in new_email:
            self._email = new_email
            print("Valid Email =", new_email)
        else:
            print("Invalid Email =", new_email)


obj = User('Sudhanshudhande19@gmail.com')
print("Current Email:", obj.email)

obj.email = 'kunalbhai55gmail.com'
print("Current Email:", obj.email)
