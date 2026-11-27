# Q10. Handle Invalid Intervals

# Concept: Exception handling and validation

# Requirements:

    # Ask the user for an interval.
    # Reject non-numeric input.
    # Reject zero and negative values.
    # Display a helpful error message.

# Steps to Solve:

    # Take interval input from the user.
    # Convert the input to an integer.
    # Handle invalid numeric conversion.
    # Check whether the value is greater than zero.
    # Display an appropriate message.

#--------------------------------------------------------------------------------------------------------

import time

try :
    
    user = int(input('Enter The Interval Time = '))

    if user > 0:
        print(" Valid Interval")

    else:
        print("Interval must be greater than zero.")

except ValueError:
    print(f'Invalid Input Please enter a numeric value')