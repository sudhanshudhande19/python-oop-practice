# Q9. Display Elapsed Time

# Concept: time.time()

# Requirements:

    # Record the starting time.
    # Wait for a few seconds.
    # Calculate elapsed time.
    # Display the result.

# Steps to Solve:

    # Record the starting timestamp.
    # Pause the program.
    # Record the ending timestamp.
    # Subtract the starting timestamp from the ending timestamp.
    # Display the elapsed time.



#---------------------------------------------------------------------------------------------------------------

import time


import time

print("Started Timestamp...")
start_time = time.perf_counter()

time.sleep(10)

print("Ending Timestamp...")
end_time = time.perf_counter()

total_time = end_time - start_time

print(f"Elapsed Time = {total_time:.2f} seconds")