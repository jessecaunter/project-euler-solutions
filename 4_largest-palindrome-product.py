# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

# Figure out range of possible values that could be the product of two 3-digit numbers.
lower_limit = 100 * 100
upper_limit = 999 * 999

def int_to_string(num):
    return str(num)

# If-else logic is based on the possible range for this particular problem
# Parameter will either have 5 or 6 digits
def is_palindrome(num):
    string_num = int_to_string(num)
    if (string_num[0] == string_num[-1] and string_num[1] == string_num[-2] and (string_num[2] == string_num[-3] or len(string_num) == 5)):
        return True
    else:
        return False

# Returns true if parameter is the product of two 3-digit numbers, false otherwise
def check_factors(num):
    square_root = math.sqrt(num)
    i = int(square_root)
    two_3_digit_factors = False
    while ((i <= 999) and (two_3_digit_factors == False)):
        if ((num % i == 0) and (len(int_to_string(num // i)) == 3)):
            # print("is the product of:", i, "x", num // i)
            two_3_digit_factors = True
        else:
            i += 1
    return two_3_digit_factors
        

# While loop through range (in descending order) until a palindrome is hit
# Then test this number to see whether it has two 3-digit factors
i = upper_limit
switch = False
while ((switch == False) and (i >= lower_limit)):
    if is_palindrome(i):
        # print("Palindrome:", i)
        if check_factors(i):
            print("SOLUTION --->", i)
            switch = True
        else:
            # print("...doesn't have two 3-digit factors")
            i -= 1
    else:
        i -= 1