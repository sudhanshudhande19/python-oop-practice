# Q10. Find Numbers Greater Than Average

# Concept: Walrus Operator with list comprehension

# Requirements:

    # Create a list of numbers.
    # Calculate the average.
    # Store the average using :=.
    # Select numbers greater than the average.

# Steps to Solve:

    # Create a list of numbers.
    # Calculate the sum and length.
    # Calculate the average using an assignment expression.
    # Filter numbers greater than the average.
    # Display the average and selected numbers.

#-------------------------------------------------------------------------------------------------------------

number = [85,45,79,62,35,41,65,72,94,23,81]

all_avg = [num for num in number if num > (avg := sum(number) / len(number))]

print('Average = ',avg)
print('number grater than average =',all_avg)