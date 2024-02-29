# 
# Accumulator Loop Example 2
# 
# COMP 1701 
# Winter 2024
# A. Fedoruk 

# Both counted loops and sentinel loops can be accumulator loops. 

# For this example we want to add the numbers between 1 and n. 

n = int(input("Enter n: "))

# we initialize our accumulator:
sum = 0
# intialize LCV
i = 1

while i <= n:
    sum = sum + i 
    i = i + 1 

print(f"The sum is {sum}")
print(f"The sum is {int(n * (n+1)/2)}")



