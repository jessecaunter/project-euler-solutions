# Find the sum of all multiples of 3 or 5 below 1000

# for loop up to 999
# check whether number divides evenly into 3 or 5
# if so, add to sum total

sum = 0

for i in range(1000):
    if ((i % 3 == 0) or (i % 5 == 0)):
        sum += i

print(sum)