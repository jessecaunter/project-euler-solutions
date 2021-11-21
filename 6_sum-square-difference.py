# The sum of the squares of the first ten natural numbers is,
# (1 ** 2) + (2 ** 2) + ... + (10 ** 2) = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum

solution_range = 100

sum_of_squares = 0
sum = 0

def number_squared(num):
    return (num ** 2)

for i in range(1, (solution_range + 1)):
    sum_of_squares += number_squared(i)
    sum += i

square_of_sum = number_squared(sum)
difference = square_of_sum - sum_of_squares

print("Range: 1 -", solution_range)
print("Sum of squares:", sum_of_squares)
print("Square of sum:", square_of_sum)
print("DIFFERENCE:", difference)