# Q2. Check Voting Eligibility

# Concept: Walrus Operator with if

# Requirements:

    # Assign an age using :=.
    # Check whether the age is at least 18.
    # Display an eligible or not eligible message.

# Steps to Solve:

    # Use := to assign the age inside an if condition.
    # Check whether the age is greater than or equal to 18.
    # Display the appropriate message.

#---------------------------------------------------------------------------------------------------


if (age := 20) > 18:
    print('Age is Eligible')
else:
    print('Not Eligible')