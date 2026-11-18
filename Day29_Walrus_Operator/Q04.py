# Q4. Check List Length

# Concept: Walrus Operator with if

# Requirements:

    # Create a list of numbers.
    # Calculate its length.
    # Store the length using :=.
    # Check whether the list contains at least 5 elements.

# Steps to Solve:

    # Create a list.
    # Use len() to calculate its size.
    # Assign the result inside an if condition.
    # Display the size.
    # Display the appropriate message.

#_------------------------------------------------------------------------------------------------------------------


num = [10,20,30,40,50,60,70,80,90]

if (length := len(num)) > 5:
    print("List has more than 5 elements")
    print(f'Length = {length}')
else:
    print('List has less than 5 element')