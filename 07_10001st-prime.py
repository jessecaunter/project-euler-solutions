# What is the 10,001st prime number?
nth_prime = 10001

import math

# Function which tests whether a number is prime
def is_prime(num):
    square_root = math.sqrt(num)

    for i in range(int(square_root), 1, -1):
        if (num % i == 0):
            return False
        
    return True

# Set loop variables
prime_counter = 0
i = 2
current_prime = 0

while prime_counter < nth_prime:
    if is_prime(i):
        current_prime = i
        prime_counter += 1

    i += 1

print(f'Prime number #{nth_prime}: {current_prime}')