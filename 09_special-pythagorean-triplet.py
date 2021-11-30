# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:
# (a ** 2) + (b ** 2) = (c ** 2)

# For example, (3 ** 2) + (4 ** 2) = 9 + 16 = 25 = (5 ** 2)
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc

import math

square_num_list = []
pythagorean_triplet_list = []
special_pythagorean_triplet = []

def square_number(x):
    return x ** 2

def is_pythagorean_triplet(num):
    half = num / 2
    i = 0
    while square_num_list[i] <= half:
        remainder = num - square_num_list[i]
        if remainder in square_num_list:
            add_to_list(square_num_list[i], remainder, num)
        i += 1

def add_to_list(num1, num2, num3):
    a = int(math.sqrt(num1))
    b = int(math.sqrt(num2))
    c = int(math.sqrt(num3))
    pythagorean_triplet_list.append([a, b, c])
    if is_special_triplet(a, b, c):
        special_pythagorean_triplet.append(a)
        special_pythagorean_triplet.append(b)
        special_pythagorean_triplet.append(c)

def is_special_triplet(a, b, c):
    return (a + b + c == 1000)

def calculate_product(special):
    return special[0] * special[1] * special[2]

for i in range(1, 999):
    square_num = square_number(i)
    square_num_list.append(square_num)
    is_pythagorean_triplet(square_num)

print(f'Special Pythagorean triplet: {special_pythagorean_triplet}')
print(f'PRODUCT: {calculate_product(special_pythagorean_triplet)}')