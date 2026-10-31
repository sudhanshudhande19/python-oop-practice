# Create a User class with:

    # Class variable: total_users = 0
    # Instance variables: username, email

# Requirements:

    # Increase the user count whenever an object is created.
    # Create a class method get_total_users().
    # Create at least five users.
    # Display the total registered users.

#-------------------------------------------------------------------------------

class user :
    total_user = 0

    def __init__(self,username,email):
        self.username = username
        self.email = email
        user.total_user += 1

    @classmethod
    def get_total_user(self):
        print(f'Total registered  User = {self.total_user}')


u1 =user('Sudhanshu','sudhanshudhande19@gmail.com')
u2 =  user('kunal','kunalbhai99@gmail.com')
u3=  user('kedar','kedarhemane11@gmail.com')
u4 = user('Aditya','adibhai90@gmail.com')
u5 = user('Ayush','AyushG@gmail.com')

user.get_total_user()
