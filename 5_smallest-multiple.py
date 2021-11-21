# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Number must increase in multiples of 380
# This is the smallest number divisible by both 20 and 19
# Incrementing by this number will make algo run much faster
number = 380

def is_number_divisible_by(x):
    if number % x == 0:
        return True 
    else:
        return False

# While loop checks whether current number is evenly divisible by all numbers from 1 to 18 (in reverse)
exit_flag = False
while exit_flag == False:
    
    for i in range(18, 0, -1):
        if is_number_divisible_by(i) == True:
            print(".")
        else:
            print(number, "is not divisible by", i)
            number += 380
            break

        if i == 1:
            exit_flag = True
        
print("SOLUTION:", number)