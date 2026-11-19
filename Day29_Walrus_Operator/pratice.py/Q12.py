# Q12. Login Attempt System

# Concept: Walrus Operator with while

# Requirements:

    # Ask the user to enter a password.
    # Allow repeated attempts.
    # Stop when the correct password is entered.
    # Display an appropriate message.

# Steps to Solve:

    # Define an expected password for this practice program.
    # Use a while loop.
    # Take password input inside the loop condition.
    # Assign the input using :=.
    # Continue until the password matches.
    # Display a success message.

#--------------------------------------------------------------------------------------------------------------------

correct_password = "python123"

while (password := input("Enter Password: ")) != correct_password:
    print("Incorrect Password! Try Again.")

print("Login Successful!")