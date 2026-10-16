# Create a `User` class with:

# `username`
# `__password`

# Requirements:

    # - Create a method `set_password(password)`.
    # - Accept passwords containing at least 8 characters.
    # - Create a method `check_password(password)` that compares the supplied password with the stored password.
    # - Never print the stored password.

# Test correct and incorrect passwords.

#---------------------------------------------------------------------------------------------------------------------------


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = ""
        self.set_password(password)

    def set_password(self, password):
        if len(password) >= 8:
            self.__password = password
            print("Password set successfully")
        else:
            print("Password must contain at least 8 characters")

    def check_password(self, password):
        if password == self.__password:
            print("Correct password")
        else:
            print("Incorrect password")


# Create object
u1 = User("Sudhanshu", "Python@123")

# Test correct password
u1.check_password("Python@123")

# Test incorrect password
u1.check_password("Python456")

# Test short password
u1.set_password("abc")

# Check the previously stored password
u1.check_password("Python@123")
