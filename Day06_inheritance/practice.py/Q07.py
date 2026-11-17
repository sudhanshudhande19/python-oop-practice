# Create a parent class User with:
    # username
    # email
    # login()

# Create a child class Admin with:
    # access_level
    # manage_users()

# Create an admin object and call all applicable methods.
#---------------------------------------------------------------------------------
class user:
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def login(self):
        print(f'Name = {self.username}\nEmail ={self.email}')

class admin(user):
    def __init__(self, username, email,acces_level):
        super().__init__(username, email)
        self.acces_level = acces_level

    def manage_users(self):
        print(f'Acces Level ={self.acces_level}')

e1 = admin('Sudhanshu Dhande','sudhanshudhande19@gmail.com',2)
e1.login()
e1.manage_users()