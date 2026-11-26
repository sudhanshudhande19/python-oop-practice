# Concept: time.perf_counter()

# Requirements:

    # Measure the time taken by a loop.
    # Store the starting time.
    # Run the loop.
    # Store the ending time.
    # Calculate the total duration.
    # Record time.perf_counter() before the loop.
    # Execute a loop with many iterations.
    # Record time.perf_counter() after the loop.
    # Calculate the difference.
    # Display the execution time.


#----------------------------------------------------------------------------------------------------------


import time

start_time = time.perf_counter()

i = 100
while i > 0:
    print(i)
    i -= 1

end_time = time.perf_counter()

execution_time = end_time - start_time

print("Execution Time:", execution_time, "seconds")