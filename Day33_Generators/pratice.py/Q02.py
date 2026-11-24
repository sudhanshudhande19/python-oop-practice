# Q2. Generate Your Name Characters

# Concept: Generators and strings

# Requirements:

    # Create a generator that produces characters of a name.
    # Generate one character at a time.
    # Display all characters.

# Steps to Solve:

    # Create a function that accepts a string.
    # Use a loop to iterate through the string.
    # Use yield to produce each character.
    # Call the function with a name.
    # Display the generated characters.

#------------------------------------------------------------------------------------------------------------------------


def generate_characters(name):
    for ch in name:
        yield ch 


name = 'sudhanshu'

gen = generate_characters(name)

print("Characters in the name:")
for chr in gen:
    print(chr)