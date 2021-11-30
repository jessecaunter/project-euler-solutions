# The sum of primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below 2 million.

import math

sum = 0

def add_to_sum(num):
    global sum 
    sum += num

def check_prime(num):
    sq_rt = math.sqrt(num)
    i = 2
    while i <= sq_rt:
        if num % i == 0:
            return
        i += 1
    add_to_sum(num)

for i in range(2, 2000000):
    check_prime(i)

print("SUM:", sum)