# Create a User class with _password.

# Rules:
    # Password must contain at least 8 characters.
    # Reject shorter passwords.
    # Do not print the password directly when displaying user information.

# Test different password lengths.
#-----------------------------------------------------------------------------------------------

class user:
    def __init__(self,password):
        self._password = password
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,new_password):
        if  len(new_password) >= 8:
            self._password = new_password
            print('Valid Password')
        else:
            print("Invalid Password! Minimum 8 characters required.")
    def show_password_length(self):
        print("Password Length =", len(self.password))

name = input('Enter The Name =')
age = int(input('Enter The Age ='))
p_word = input('Enter The User Password 8 Characters =')

obj = user(p_word)

obj.show_password_length()
        
