# 
# Accumulator Loop Example 
# 
# COMP 1701 
# Winter 2024
# A. Fedoruk 

# Both counted loops and sentinel loops can be accumulator loops. 

# Say we want to add a list of numbers. We can use our 
# loop to enter numbers until -1 is entered.

# we initialize our accumulator: 

sum = 0

# priming read
num = int(input("Enter a number, -1 to end: "))

while num != -1:
    print(f"num = {num}")
    sum = sum + num
    # We always need to update the LCV in the loop otherwise loop will never end. 
    num = int(input("Enter a number, -1 to end: "))

print(f"The sum is {sum}")






