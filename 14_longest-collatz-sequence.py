# The following iterative sequence is defined for the set of positive integers:

# n --> n/2 (n is even)
# n --> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go over one million.

# ------------------------------------------------------------------------------------------------------------

longest_chain_length = 0
solution = 0

def is_even(num):
    return (num % 2 == 0)

def generate_collatz(num):
    sequence = [num]
    while sequence[-1] != 1:
        if is_even(sequence[-1]):
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(sequence[-1] * 3 + 1)
    return sequence

for i in range(1, 1000000):
    sequence = generate_collatz(i)
    if len(sequence) > longest_chain_length:
        longest_chain_length = len(sequence)
        solution = i

print(f'SOLUTION: {solution} \nWith a chain of {longest_chain_length} numbers')