# Q11. Large File Line Reader

# Concept: Generators and file handling

# Requirements:

# Read a text file.

    # Generate one line at a time.
    # Display each line.
    # Avoid loading the complete file into memory.

# Steps to Solve:

    # Create a sample text file with multiple lines.
    # Create a generator function that accepts a file path.
    # Open the file using a context manager.
    # Iterate through the file line by line.
    # Use yield to produce each line.
    # Display lines using a for loop.
    # Handle file-not-found errors.

#----------------------------------------------------------------------------------------------------------------------


def read_lines(file_path):

    try:
        with open(file_path, "r") as file:

            for line in file:
                yield line.strip()

    except FileNotFoundError:
        print("File not found!")


# Read and display file lines
for line in read_lines("Day33_Generators/sample.txt"):
    print(line)