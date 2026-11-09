# Create a User parent class and an Admin child class.

# Concept: Inheritance with Different Permissions.

# Requirements:

    # Parent stores username and email.
    # Parent has a login method.
    # Child stores admin level.
    # Child has a method to manage users.
    # Admin should be able to use the parent's login method.

# -------------------------------------------------------------------------------------------------------


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"{self.username} logged in successfully.")

class Admin(User):
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)
        self.admin_level = admin_level

    def manage_users(self):
        print(f"Admin {self.username} is managing users.")


admin1 = Admin("Sudhanshu", "sudhanshu@gmail.com", 1)
admin1.login()
admin1.manage_users()