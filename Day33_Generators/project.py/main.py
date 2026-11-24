
print('==============================================')
print('                 SMART DATA GENERATOR         ')
print('==============================================')


while True:


    print()
    print('1. Generate Numbers')
    print('2. Generate Even Numbers')
    print('3. Generate Odd Numbers')
    print('4. Generate Prime Numbers')
    print('5. Generate Squares')
    print('6. Generate Fibonacci Series')
    print('7. Generate Data in Batches')
    print('8. Exit')
    print('----------------------------------')
    print()

    # Take the user's choice (convert the input string to an integer)
    option = int(input('Enter The Number = '))

    # ---------- Option 1: Numbers from 1 to 10 ----------
    if option == 1:

        print('Generate Numbers')

        # Generator function: yields one number at a time (memory efficient)
        def generate_numbers():
            for i in range(1, 10 + 1):
                yield i

        # Loop over the generator and print each value
        for num in generate_numbers():
            print(num)
        print('Successfully Generated Numbers')
        print('--------------------------------')


    # ---------- Option 2: Even numbers (1 to 20) ----------
    elif option == 2:

        print('Generate Even Numbers')

        def generate_even():
            for i in range(1, 21):
                # A number is even if it is divisible by 2 (remainder 0)
                if i % 2 == 0:
                    yield i

        for num in generate_even():
            print(num)
        print('Successfully Generated Even Numbers')
        print('-------------------------------------')


    # ---------- Option 3: Odd numbers (1 to 20) ----------
    elif option == 3:

        print('Generate Odd Numbers')

        def generate_odd():
            for i in range(1, 21):
                # A number is odd if the remainder after dividing by 2 is 1
                if i % 2 == 1:
                    yield i

        for num in generate_odd():
            print(num)

        print('Successfully Generated Odd Numbers')
        print('-------------------------------------')


    # ---------- Option 4: Prime numbers ----------
    elif option == 4:

        print('Generate Prime Numbers')

        # Helper function: checks whether a number is prime
        def is_prime(n):
            # Numbers smaller than 2 are not prime
            if n < 2:
                return False

            # Checking up to the square root is enough (faster)
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:       # a divisor was found -> not prime
                    return False

            return True              # no divisor found -> prime

        # Generator: yields all primes from 2 up to the given limit
        def generate_primes(limit):
            for num in range(2, limit + 1):
                if is_prime(num):
                    yield num

        for prime in generate_primes(21):
            print(prime)

        print('Successfully Generated Prime Numbers')
        print('-------------------------------------')


    # ---------- Option 5: Squares (1 to 20) ----------
    elif option == 5:

        print('Generate Squares')

        def generate_squares():
            for i in range(1, 21):
                Squares = i * i      # square of the number
                yield Squares

        for i in generate_squares():
            print(i)

        print('Successfully Generated Squares')
        print('-------------------------------------')


    # ---------- Option 6: Fibonacci series ----------
    elif option == 6:

        print('Generate Fibonacci Series')

        # The user decides how many terms to generate
        user = int(input('Enter The Number = '))

        def generate_fibonacci(user):
            # The series starts with 0 and 1
            a, b = 0, 1

            for num in range(user):
                yield a
                # Next term = sum of the previous two terms
                a, b = b, a + b

        for total in generate_fibonacci(user):
            print(total)

        print('Successfully Generated Fibonacci Series')
        print('-------------------------------------')


    # ---------- Option 7: Split data into batches ----------
    elif option == 7:

        print('Generate Data in Batches')

        # Generator: splits data into smaller chunks of size batch_size
        def batch_generator(data, batch_size):
            # The range step is batch_size, so each iteration gives the start of the next batch
            for i in range(0, len(data), batch_size):
                yield data[i:i + batch_size]    # slicing gives one batch

        # List of numbers from 1 to 100
        numbers = list(range(1, 101))

        # Prints the data in batches of 10
        for batch in batch_generator(numbers, 10):
            print(batch)
        print('Successfully Generated Data Batches')
        print('-------------------------------------')


    # ---------- Option 8: Exit the program ----------
    elif option == 8:

        print('Thank You')
        exit()    # terminates the program here