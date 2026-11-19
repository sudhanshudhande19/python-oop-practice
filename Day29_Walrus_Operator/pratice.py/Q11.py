# Q11. Student Marks Analyzer

# Concept: Walrus Operator with conditions

# Requirements:

    # Accept student marks.
    # Calculate the result.
    # Store the percentage using :=.
    # Display pass or fail based on the percentage.

# Steps to Solve:

    # Take marks from the user.
    # Calculate the percentage.
    # Store the percentage using :=.
    # Check the passing condition.
    # Display the percentage and result.

#-------------------------------------------------------------------------------------------------------


marks = int(input("Enter obtained marks: "))
total = int(input("Enter total marks: "))



if (avg := (marks / total) * 100) != 50:
    print(f'Percentage = {avg}')
    print(f'Result = Pass')
   
else:
    print(f'Percentage = {avg}')
    print(f'Result = Fail')