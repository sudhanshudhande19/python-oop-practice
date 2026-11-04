# Create a decorator named login_required.

# Create a function dashboard() that prints "Welcome to Dashboard".

# If the user is logged in, allow the function to run. Otherwise, print "Please log in first".

# Use a Boolean variable to represent login status.
#------------------------------------------------------------------------------------------------------------------

# Boolean variable representing login status
is_logged_in = True

def login_required(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Please log in first")
    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard")


dashboard()