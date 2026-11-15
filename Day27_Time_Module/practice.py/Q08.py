# Concept: time.perf_counter()

# Requirements:

    # Start the stopwatch.
    # Allow the user to stop it.
    # Calculate elapsed time.
    # Display the total duration
    # Record the starting time.
    # Wait for the user to press Enter.
    # Record the ending time.
    # Subtract starting time from ending time.
    # Display the elapsed seconds.

#-------------------------------------------------------------------------------------

import time

print('Stopwatch Started...')
start_time = time.perf_counter()

input('press Enter to stop Stopwatch')
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print("Elapsed Time:", elapsed_time, "seconds")