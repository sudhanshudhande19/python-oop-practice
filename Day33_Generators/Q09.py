# Q9. Generator Expression for Cubes

# Concept: Generator expressions

# Requirements:

    # Create a generator expression.
    # Generate cubes of numbers from 1 to 10.
    # Display each cube.
    # Compare it with a list comprehension.

# Steps to Solve:

    # Use a generator expression with range().
    # Calculate the cube of each number.
    # Store the generator expression in a variable.
    # Iterate through the generator.
    # Create a separate list comprehension.
    # Compare their types and outputs.

#------------------------------------------------------------------------------------------------------------------------

cube_gen = (i ** 3 for i in range(1, 11))


for r in cube_gen:
    print(r)

cube_list = [i ** 3 for i in range(1, 11)]
print("\nCubes using List Comprehension:")
print(cube_list)

print("\nType of Generator:", type(cube_gen))
print("Type of List:", type(cube_list))