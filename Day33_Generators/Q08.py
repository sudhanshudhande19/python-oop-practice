# Q8. Generate Prime Numbers

# Concept: Conditions and generator functions

# Requirements:

    # Generate prime numbers within a given range.
    # Produce each prime number separately.
    # Display the results.

# Steps to Solve:

    # Create a generator function that accepts a limit.
    # Loop through numbers starting from 2.
    # Check whether each number is prime.
    # Use a separate helper function for prime checking if needed.
    # Use yield for prime numbers.
    # Display all generated primes.

#------------------------------------------------------------------------------------------------------


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def generate_primes(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num


for prime in generate_primes(20):
    print(prime)