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

# We can cut down on uneccessary iterations by calculating half of the number
# and only looping over numbers in this range.
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

# My approach is to iterate over each number in the range, square it, and then add it 
# to a list of square numbers. Then immediately check whether this number is a 
# Pythagorean triplet by calculating whether it's the sum of any two preceding
# numbers in the list. If so, the square root of all three of those numbers get added
# to a Pythagorean triplet list as a sub-list. We then immediately check whether
# this Pythagorean triplet is the special one we're looking for.
# As soon as the special Pythagorean triplet is found, the loop is broken and solution
# printed on the screen.
# Integrating all these steps as part of each loop iteration should make algorithm more
# efficient as it cuts down on total iterations.
for i in range(1, 999):
    square_num = square_number(i)
    square_num_list.append(square_num)
    is_pythagorean_triplet(square_num)
    if len(special_pythagorean_triplet) == 3:
        break

print(f'Special Pythagorean triplet: {special_pythagorean_triplet}')
print(f'PRODUCT: {calculate_product(special_pythagorean_triplet)}')