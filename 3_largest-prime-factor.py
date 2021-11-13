# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

# take any integer as input
x = 600851475143

def get_factors(x):
    factors = []
    square_root = math.sqrt(x)

    # create lower half of factors list
    i = 1
    while i <= int(square_root):
        if x % i == 0:
            factors.append(i)
        i += 1

    # create upper half of factors list
    e = -1
    for i in range(len(factors)):
        next = x // factors[e]
        if next != factors[e]:
            factors.append(next)
            e += -2
        else:
            e+= -1
    
    return factors

def is_prime(x):
    if len(get_factors(x)) == 2:
        return True

def get_prime_factors(x):
    factors = get_factors(x)
    prime_factors = []
    for i in range(len(factors)):
        if is_prime(factors[i]):
            prime_factors.append(factors[i])
    return prime_factors

factors = get_factors(x)
prime_factors = get_prime_factors(x)
largest_prime_factor = prime_factors[-1]

# print result
print("Input:", x)
print("Largest prime factor:", largest_prime_factor)