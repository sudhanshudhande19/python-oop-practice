from functools import lru_cache

# Cached Functions

@lru_cache(maxsize=100)
def squares(n):
    return n * n

@lru_cache(maxsize=100)
def cube(n):
    return n * n * n

@lru_cache(maxsize=100)
def add(n, m):
    return n + m

@lru_cache(maxsize=100)
def multiplication(n, m):
    return n * m

@lru_cache(maxsize=100)
def power(n, m):
    return n ** m

@lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# ==========================
# Main Program
# ==========================

while True:
    print('\n==================================================')
    print('             SMART CALCULATION CACHE              ')
    print('==================================================')
    print('1. Square')
    print('2. Cube')
    print('3. Addition')
    print('4. Multiplication')
    print('5. Power')
    print('6. Fibonacci')
    print('7. Cache Information')
    print('8. Clear Cache')
    print('9. Exit')

    choice = input('Enter Your Choice: ')

    # Exit
    if choice == '9':
        print("Calculator Closed!")
        break

    # Cache Information
    elif choice == '7':
        print("\n===== Cache Information =====")
        print(f'Square Cache        : {squares.cache_info()}')
        print(f'Cube Cache          : {cube.cache_info()}')
        print(f'Addition Cache      : {add.cache_info()}')
        print(f'Multiplication Cache: {multiplication.cache_info()}')
        print(f'Power Cache         : {power.cache_info()}')
        print(f'Fibonacci Cache     : {fibonacci.cache_info()}')
        continue

    # Clear Cache
    elif choice == '8':
        squares.cache_clear()
        cube.cache_clear()
        add.cache_clear()
        multiplication.cache_clear()
        power.cache_clear()
        fibonacci.cache_clear()

        print("\nAll caches cleared successfully!")
        continue

    # Square
    elif choice == '1':
        try:
            n = int(input("Enter Number: "))
            print(f'Square of {n} = {squares(n)}')
        except ValueError:
            print("Invalid Input!")
        continue

    # Cube
    elif choice == '2':
        try:
            n = int(input("Enter Number: "))
            print(f'Cube of {n} = {cube(n)}')
        except ValueError:
            print("Invalid Input!")
        continue

    # Fibonacci
    elif choice == '6':
        try:
            n = int(input("Enter Fibonacci Position: "))
            print(f'Fibonacci({n}) = {fibonacci(n)}')
        except ValueError:
            print("Invalid Input!")
        continue

    # Addition, Multiplication, Power
    elif choice in ['3', '4', '5']:
        try:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
        except ValueError:
            print("Invalid Input!")
            continue

        if choice == '3':
            print(f'{a} + {b} = {add(a, b)}')

        elif choice == '4':
            print(f'{a} × {b} = {multiplication(a, b)}')

        elif choice == '5':
            print(f'{a}^{b} = {power(a, b)}')

    else:
        print("Invalid Choice! Please select between 1 and 9.")