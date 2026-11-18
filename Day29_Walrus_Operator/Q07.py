# Q7. Find Long Words

# Concept: Walrus Operator with list comprehension

# Requirements:

    # Create a list of words.
    # Calculate each word's length.
    # Store the length using :=.
    # Select words whose length is greater than 5.

# Steps to Solve:

    # Create a list of words.
    # Start a list comprehension.
    # Calculate each word's length.
    # Assign the length using :=.
    # Add a condition for lengths greater than 5.
    # Display the resulting list.

#----------------------------------------------------------------------------------------------------------------------------


word = ['sudhanshu','kuanl','kedar','pranay','aditya','kulbhushan','ayush','omkar']


long_word = [w for  w in word if(length := len(w)) > 5]
print(long_word)